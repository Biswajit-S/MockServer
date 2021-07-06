from db import db

'''
User Model Class, holds for attributes for an User account.
- ID : Integer (Auto Generated, Primary Key in the DB)
- Email : String
- Password: String
- Name: String

Model Class also exposes services to find or delete an user account by email address.
'''
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name



    def json(self):
        return {'id':self.id, 'email': self.email, 'name': self.name}

    @classmethod
    def find_by_username(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
