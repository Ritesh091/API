from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal

from app.main import session_scope
from app.main.service.campaign_media_service import get_all_campaign_media, get_media_analysis
from app.main.controller import scoped_response
from app.main.controller import prepare_response
from app.main.util.campaign_media_dto import CampaignMediaDto

campaign_mediaApi = CampaignMediaDto.campaign_mediaApi

@campaign_mediaApi.route('campaignAnalysisDetail/<camp_media_id>')
class GetCampAnalysisDetail(Resource):
    @campaign_mediaApi.doc(responses={200: 'Details of logo',
                            400: 'Bad Request'})
    def get(self,camp_media_id):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            camp_media = get_media_analysis(session,camp_media_id)
            if camp_media:
                response_details['data'] = marshal(camp_media, CampaignMediaDto.campaign_mediaModel)
                response_details['message'] = "Successfully retrieve camp media details."
            else:
                response_details['data'] = None
                response_details['message'] = "No match found. Please use valid camp media id."

        return prepare_response(**response_details)
