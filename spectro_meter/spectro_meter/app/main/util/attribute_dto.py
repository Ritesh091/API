from flask_restplus import Namespace
from flask_restplus import fields

""" parameters required to add or update user details"""

class AttributeDto:
    AttributeApi = Namespace('Campaign', description=' ------------- CRUD Operations')

    attributeModel = AttributeApi.model('Attributes', {
        'camp_media_id': fields.String(required=True, description='camp_media_id of Campaign Media'),
        'time': fields.String(required=True, description='time of attribute'),
        'visibility_score': fields.Float(required=True, description='score of attribute')
    })