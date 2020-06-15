from flask_restplus import Namespace
from flask_restplus import fields

""" parameters required to add or update user details"""

class MediaDto:
    mediaApi = Namespace('Repository', description=' ------------- CRUD Operations')

    mediaModel = mediaApi.model('addOrUpdateMedia', {
        'id': fields.Integer(required=True, description='id of media', attribute = 'media_id'),
        'title': fields.String(required=True, description='title of media', attribute = 'name'),
        'description': fields.String(required=True, description='description of media'),
        'mediaThumbnailPath': fields.String(required=True, description='path of thumbnail'),
        'mediaThumbnailName': fields.String(required=True, description='name of thumbnail'),
        'mediaPath': fields.String(required=True, description='path of media'),
        'mediaName': fields.String(required=True, description='name of media', attribute = 'filename'),
        'user': fields.String(required=True, description='name of user', attribute = lambda x: x.modified_by_user.first_name + " " + x.modified_by_user.last_name),
        'date': fields.DateTime(required=True, description='date of media modified', attribute = 'modified_date')
    })

    # loginUserModel = userApi.model('loginUser', {
    #     'email': fields.String(required=True, description='email of user'),
    #     'password_hash': fields.String(required=True, description='password')
    # })


