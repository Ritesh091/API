from flask_restplus import Namespace
from flask_restplus import fields
from app.main.util.lookup_dto import LookupDto
from app.main.util.media_dto import MediaDto

""" parameters required to add or update user details"""

class CampaignDto:
    campaignApi = Namespace('Campaign', description=' ------------- CRUD Operations')

    campaignModel = campaignApi.model('campaignModel', {
        'id': fields.Integer(required=True, description='id of campaign', attribute = 'campaign_id'),
        'name': fields.String(required=True, description='name of campaign'),
        'description': fields.String(required=True, description='description of campaign'),
        'labels': fields.String(required=True, description='tags of campaign', attribute = 'tags'),
        'modifiedBy': fields.String(required=True, description='date of campaign created',
                              attribute=lambda x: x.modified_by_user.first_name + " " + x.modified_by_user.last_name),
        'modifiedDate': fields.DateTime(required=True, description='date of campaign modified', attribute = 'modified_date'),
        # 'user': fields.String(required=True, description='date of campaign created',
        #                       attribute=lambda x: x.modified_by_user.first_name + " " + x.modified_by_user.last_name),
    })

    campaignExploreModel = campaignApi.model('addOrUpdateCampaign', {
        'id': fields.Integer(required=True, description='id of campaign', attribute = 'campaign_id'),
        'name': fields.String(required=True, description='name of campaign'),
        'description': fields.String(required=True, description='description of campaign'),
        'labels': fields.String(required=True, description='tags of campaign', attribute = 'tags'),
        'user': fields.String(required=True, description='date of campaign created', attribute=lambda x: x.modified_by_user.first_name + " " + x.modified_by_user.last_name),
        'date': fields.DateTime(required=True, description='date of campaign modified', attribute = 'modified_date'),
        "lookupList": fields.List(fields.Nested(LookupDto.lookupModel), attribute="lookups"),
        "repositoryList": fields.List(fields.Nested(MediaDto.campaignMediaModel), attribute=lambda x: [camp_media.medias for camp_media in x.camp_medias])
    })