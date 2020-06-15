from flask_restplus import Namespace
from flask_restplus import fields
from app.main.util.media_dto import MediaDto
from app.main.util.attribute_dto import AttributeDto
from app.main.util.campaign_detail_dto import CampaignDetailDto

""" parameters required to add or update user details"""

class CampaignMediaDto:
    campaign_mediaApi = Namespace('Campaign', description=' ------------- CRUD Operations')

    campaign_mediaModel = campaign_mediaApi.model('Get campaign by id', {
        'media_id': fields.Integer(required=True, description='id of campaign_media'),
        'title':fields.String(required=True, description='title of campaign_media',  attribute=lambda x:x.medias.name),
        'mediaName': fields.String(required=True, description='name of media', attribute=lambda x:x.medias.filename),
        'mediaPath': fields.String(required=True, description='path of media', attribute=lambda x:x.medias.mediaPath),
        'camp_detail': fields.List(fields.Nested(CampaignDetailDto.campaigndetailModel)),
        'attributes': fields.List(fields.Nested(AttributeDto.attributeModel)),
    })