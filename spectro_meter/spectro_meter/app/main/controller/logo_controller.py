from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal

from app.main import session_scope
from app.main.service.logo_service import get_all_logo
from app.main.controller import scoped_response
from app.main.controller import prepare_response
from app.main.util.lookup_dto import LookupDto

lookupApi = LookupDto.lookupApi

@lookupApi.route('lookupList')
class GetLookupId(Resource):
    @lookupApi.doc(responses={200: 'Details of logo',
                            400: 'Bad Request'})
    def get(self):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            logo = get_all_logo(session)
            if logo:
                response_details['data'] = marshal(logo, LookupDto.lookupModel)
                response_details['message'] = "Successfully retrieve logo details."
            else:
                response_details['data'] = None
                response_details['message'] = "No match found."

        return prepare_response(**response_details)
