from flask_restplus import Namespace
from flask_restplus import fields
from app.main.util.attribute_dto import AttributeDto

""" parameters required to add or update user details"""

class CampaignDetailDto:
    campaigndetailApi = Namespace('Campaign', description=' ------------- CRUD Operations')

    campaigndetailModel = campaigndetailApi.model('addOrUpdateCampaigndetail', {
        'visibility_score': fields.Float(required=True, description='score of campaign'),
        'appearance': fields.Float(required=True, description='appearance of campaign'),
        'bulls_eye': fields.Float(required=True, description='bulls eye of campaign', attribute = 'bulls_eye'),
        'corner_kings': fields.Float(required=True, description='corner kings of campaign'),
        'longest_logo_duration': fields.Float(required=True, description='longest logo duration of campaign'),
        'largest_area_percentage': fields.Float(required=True, description='largest area percentage of campaign'),
        'exposure_rate': fields.Float(required=True, description='exposure rate of campaign'),
        'annotated_video_path': fields.String(required=True, description='path of annotated video'),
    })