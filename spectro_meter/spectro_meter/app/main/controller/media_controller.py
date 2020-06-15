from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal

from app.main import session_scope
from app.main.service.media_service import get_all_media
from app.main.controller import scoped_response
from app.main.controller import prepare_response
from app.main.util.media_dto import MediaDto

mediaApi = MediaDto.mediaApi

@mediaApi.route('repositoryMediaList')
class GetMediaList(Resource):
    @mediaApi.doc(responses={200: 'Details of logo',
                            400: 'Bad Request'})
    def get(self):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            medias = get_all_media(session)
            if medias:
                response_details['data'] = marshal(medias, MediaDto.mediaModel)
                response_details['message'] = "Successfully retrieve logo details."
            else:
                response_details['data'] = None
                response_details['message'] = "No match found."

        return prepare_response(**response_details)
