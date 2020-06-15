from flask_restplus import Namespace
from flask_restplus import fields

""" parameters required to add or update user details"""

class UserDto:
    userApi = Namespace('User', description=' ------------- CRUD Operations')

    userModel = userApi.model('addOrUpdateUser', {
        'user_id': fields.Integer(required=True, description='id of user'),
        'first_name': fields.String(required=False, description='first name of user'),
        'last_name': fields.String(required=False, description='last name of user'),
        'email': fields.String(required=False, description='email of user'),
        'password': fields.String(required=False, description='password of user'),
        'token': fields.String(required=False, description='token'),
        'enabled': fields.Boolean(required=False, description='status of user'),
        "oldPassword": fields.String(required=False, description='old password of user'),
        "newPassword": fields.String(required=False, description='new password of user')
    })


    # userEnabledModel = userApi.model('addOrUpdateUser', {
    #     'user_id': fields.Integer(required=True, description='id of user'),
    #     'enabled': fields.Boolean(required=True, description='status of user')
    # })

    loginUserModel = userApi.model('loginUser', {
        'email': fields.String(required=True, description='email of user'),
        'password': fields.String(required=True, description='password')
    })


