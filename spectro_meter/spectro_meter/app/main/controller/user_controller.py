from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restplus import Resource
from flask_restplus import marshal

from app.main import session_scope, jwt_manager
from app.main.util.user_dto import UserDto
from app.main.service.user_service import add_or_update_user, user_login, logout_user
from app.main.service.user_service import get_user_by_id
from app.main.service.user_service import get_all_user
from app.main.controller import scoped_response
from app.main.controller import prepare_response

userApi = UserDto.userApi
addOrUpdateUserApiModel = UserDto.userModel
loginUserModel = UserDto.loginUserModel

""" api endpoint for add or update user"""


@userApi.route('users')
class AddOrUpdateUser(Resource):
    @userApi.doc(responses={200: 'New User is Added / Updated',
                            400: 'Bad Request'})
    @userApi.expect(addOrUpdateUserApiModel)
    def post(self):
        data = userApi.payload
        response_details = dict(scoped_response)
        response_details['user'] = data
        with session_scope(response_details) as session:
            updated_user = add_or_update_user(session, data)
            session.flush()
            response_details['user'] = marshal(updated_user, UserDto.userModel)
            response_details['message'] = "User details are add/updated."
        return prepare_response(**response_details)

    """ api endpoint for get details of all users """

    @userApi.doc(responses={200: 'List of all users',
                            400: 'Bad Request'})
    def get(self):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            users = get_all_user(session)
            response_details['user'] = marshal(users, UserDto.userModel)
            response_details['message'] = "Successfully retrieve users details."

        return prepare_response(**response_details)


""" api endpoint for get user by id"""


@userApi.route('users/<user_id>')
class GetUserById(Resource):
    @userApi.doc(responses={200: 'Details of user',
                            400: 'Bad Request'})
    def get(self, user_id):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            user = get_user_by_id(session, user_id)
            if user:
                response_details['user'] = marshal(user, UserDto.userModel)
                response_details['message'] = "Successfully retrieve user details."
            else:
                response_details['user'] = None
                response_details['message'] = "No match found. Please use valid user id."

        return prepare_response(**response_details)


@jwt_manager.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'ok': False,
        'message': 'Missing Authorization Header'
    }), 401


@userApi.route('doLogin')
class UserLogin(Resource):
    @userApi.doc(responses={200: 'user login',
                            400: 'Bad Request'})
    @userApi.expect(loginUserModel)
    def post(self):
        response_details = dict(scoped_response)
        with session_scope(response_details) as session:
            email = userApi.payload['email']
            password = userApi.payload['password']
            user_login_data = user_login(session, email, password)
            print(len(user_login_data))
            if (len(user_login_data) == 8):
                res_dict = {}
                res_dict['token'] = user_login_data[0]
                res_dict['first_name'] = user_login_data[3]
                res_dict['email'] = user_login_data[4]
                res_dict['enabled'] = user_login_data[5]
                res_dict['user_id'] = user_login_data[6]
                res_dict['last_name'] = user_login_data[7]
                response_details['user'] = res_dict
            else:
                pass
            response_details['message'] = user_login_data[1]
            response_details['status'] = user_login_data[2]

        return prepare_response(**response_details)


@userApi.route('doLogout')
class LogoutUser(Resource):
    @userApi.doc(responses={200: 'user logged out',
                            400: 'Invalid Argument'})
    # @userApi.expect(logoutUserModel)
    @jwt_required
    def get(self):
        response_details = dict(scoped_response)
        logout_user()
        response_details['message'] = "Logout successful."

        return prepare_response(**response_details)
