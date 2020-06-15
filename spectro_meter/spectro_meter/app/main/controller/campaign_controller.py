from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal

from app.main import session_scope
from app.main.service.campaign_service import get_all_campaigns, get_campaign

from app.main.controller import scoped_response
from app.main.controller import prepare_response
from app.main.util.campaign_dto import CampaignDto

campaignApi = CampaignDto.campaignApi

@campaignApi.route('campaignList')
class GetAllCampaigns(Resource):
    @campaignApi.doc(responses={200: 'Details of logo',
                            400: 'Bad Request'})
    def get(self):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            campaigns = get_all_campaigns(session)
            if campaigns:
                response_details['data'] = marshal(campaigns, CampaignDto.campaignModel)
                response_details['message'] = "Successfully retrieve campaign details."
            else:
                response_details['data'] = None
                response_details['message'] = "No match found."

        return prepare_response(**response_details)

@campaignApi.route('campaignDetail/<campaign_id>')
class GetDetailById(Resource):
    @campaignApi.doc(responses={200: 'Details of logo',
                            400: 'Bad Request'})
    def get(self,campaign_id):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            camp_detail = get_campaign(session,campaign_id)
            if camp_detail:
                response_details['data'] = marshal(camp_detail, CampaignDto.campaignExploreModel)
                response_details['message'] = "Successfully retrieve campaign details."
            else:
                response_details['data'] = None
                response_details['message'] = "No match found. Please use valid campaign id."

        return prepare_response(**response_details)
