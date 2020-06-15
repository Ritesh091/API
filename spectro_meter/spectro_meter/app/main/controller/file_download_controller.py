from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal
from flask_restplus import Namespace
from flask import send_from_directory
from app.main import Config
import os

from app.main import session_scope
from app.main.controller import scoped_response
from app.main.controller import prepare_response

file_provider = Namespace('LookUp', description=' ------------- CRUD Operations')

@file_provider.route('visibility_data/<path:path>')
class GetFile(Resource):
    def get(self,path):
        return send_from_directory(Config.STATIC_DIR_PATH,path)
