from flask_restful import Resource, reqparse

from models.usermodel import UserModel

'''
UserServiceSecure class exposes create and update user services.
Intended to accept data in the request body.
'''
class UserServiceSecure(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="Email ID is Mandatory"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Password is Mandatory"
                        )
    parser.add_argument('name',
                        type=str,
                        required=False,
                        help="Please provide a name to identify you"
                        )
    '''
    Accept name, email, password in request body.
    If the email ID does not belong to an user account, create a new user account.
    '''
    def post(self):
        payload = UserServiceSecure.parser.parse_args()

        if UserModel.find_by_username(payload['email']):
            return {"message": f"An user with email '{payload['email']}' already exists"}, 400

        user = UserModel(**payload)
        user.save_to_db()

        return {"message": f"User with email '{payload['email']}' registered successfully!"}, 201

    '''
    Accept email, password in request body.
    If the email ID already belongs to an user account, update the remaining details provided.
    '''
    def put(self):
        payload = UserServiceSecure.parser.parse_args()
        user = UserModel.find_by_username(payload['email'])
        if not user:
            return {"message": f"User with email '{payload['email']}' not found"}, 404

        if payload['password']:
            user.password = payload['password']
        if payload['name']:
            user.name = payload['name']

        user.save_to_db()

        return {"message": f"User '{payload['email']}' has updated successfully!"}, 200

'''
UserService class exposes GET and delete user services.
Accepts the email as path parameter.
'''
class UserService(Resource):
    '''
    If an user account exists for the provided email id, return the user details (except the password).
    '''
    def get(self, email):
        user = UserModel.find_by_username(email)
        if user:
            return user.json()
        return {"message": f"User Account Not Found with email '{email}'"}, 404

    '''
    If an user account exists for the provided email id, delete the account.
    '''
    def delete(self, email):
        user = UserModel.find_by_username(email)
        if not user:
            return {"message": f"User Account Not Found with email {email}"}, 404

        user.delete_from_db()
        return {"message": f"User account '{email}' is deleted"}

