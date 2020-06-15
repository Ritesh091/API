from flask_restplus import Namespace
from flask_restplus import fields
from app.main.model.logo_model import StatusType

""" parameters required to add or update user details"""

class LookupDto:
    lookupApi = Namespace('LookUp', description=' ------------- CRUD Operations')

    lookupModel = lookupApi.model('addOrUpdateLogo', {
        'id': fields.Integer(required=True, description='id of logo', attribute="logo_id"),
        'title': fields.String(required=True, description='title of logo', attribute="name"),
        'description': fields.String(required=True, description='description of logo'),
        'mediaPath': fields.String(required=True, description='path of media'),
        'mediaName': fields.String(required=True, description='name of media', attribute = 'filename'),
        'status': fields.String(attribute=lambda x: str(StatusType(x.status).name)),
        'user': fields.String(required=True, description='id of user', attribute=lambda x: x.modified_by_user.first_name + " " + x.modified_by_user.last_name),
        'date': fields.DateTime(required=True, description='date of logo created', attribute="modified_date")
    })

    # loginUserModel = userApi.model('loginUser', {
    #     'email': fields.String(required=True, description='email of user'),
    #     'password_hash': fields.String(required=True, description='password')
    # })


