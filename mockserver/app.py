'''
@author: bsahoo
'''
import os

from flask import Flask
from flask_restful import Api

from db import db
from resources.user import UserServiceSecure, UserService
from resources.mock import MockServiceTimeout, MockServiceHttpStatus
from resources.urlsvc import URLService, URLServiceGenerate
from PropertyFactory import PropertyFactory

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', PropertyFactory.DB_URL)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = PropertyFactory.APP_SECRET_KEY
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserServiceSecure, '/user')
api.add_resource(UserService, '/user/<string:email>')
api.add_resource(MockServiceTimeout, '/mock/timeout/<int:interval>')
api.add_resource(MockServiceHttpStatus, '/mock/status/<int:status>')
api.add_resource(URLService, '/u/<string:url_key>')
api.add_resource(URLServiceGenerate, '/url')


if __name__ == '__main__':
    app.run(port=PropertyFactory.APP_PORT, debug=False)