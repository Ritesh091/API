# import User model
from flask_jwt_extended import create_refresh_token, create_access_token, get_jwt_identity, get_raw_jwt

from app.main import flask_bcrypt, black_list
from app.main.model.user_model import UserModel as User

""" function for adding or updating user details"""


def add_or_update_user(session, data):
    """
         Add or update user details in database.
         :param session: current session
         :param data: that contains user fields details
    """
    """ querying to add/update user to database """
    if 'user_id' in data.keys() and data.get('user_id') != 0: ## Update existing user
        # Updating the user status enabled/disabled
        user_id = data.get('user_id')
        user = session.query(User).filter(User.user_id.in_([user_id])).first()

        if 'enabled' in data.keys():
            user.enabled = data.get('enabled')
        if 'oldPassword' in data.keys() and 'newPassword' in data.keys():
            if flask_bcrypt.check_password_hash(user.password_hash, str(data['oldPassword'])):
                user.password_hash = flask_bcrypt.generate_password_hash(data['newPassword'])
        if 'first_name' in data.keys():
            user.first_name = data.get('first_name')
        if 'last_name' in data.keys():
            user.last_name = data.get('last_name')
    else:   ## Create a new user
        data['password'] = flask_bcrypt.generate_password_hash(data['password'])
        user = User(**data)
    #data.pop('password_hash', None)
    updated_user = session.merge(user)
    # print(updated_user)
    # if 'first_name' in data.keys():
        # updated_user.first_name = data['first_name']
    return updated_user


"""function for selecting user by id"""


def get_user_by_id(session, user_id):
    """
       Service to get candidate details by user(primary key).
       :param session: current session
       :param user_id: user_id to get user details
       :returns : {
          "status": "Success/Failure",
          "message": "appropriate message of success or bad request",
          "data": user details
        }
    """
    """querying database to fetch user details from user_id"""
    user = session.query(User).filter(
        User.user_id.in_([user_id])).first()
    return user


"""function to get all users"""


def get_all_user(session):
    """
       Service to get all user details .
       :param session: current session
       :returns : {
          "status": "Success/Failure",
          "message": "appropriate message of success or bad request",
          "data": all user details
        }
    """
    """querying database to fetch all user details"""
    users = session.query(User).all()
    return users


"""function for user login"""


def user_login(session, email, password):
    """
       User login service .
        :param session: current session
        :param email: email id of user
        :param password_hash: password of user
        :returns : {
          "status": "Success/Failure",
          "message": "appropriate message of Login successful or bad request",
          "data": "Token"
        }
    """
    """querying database to fetch all user details"""
    user = session.query(User).filter_by(email=email).first()
    if user:
        if flask_bcrypt.check_password_hash(user.password_hash, str(password)):
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            print('logged in user: ' + str(user.first_name))
            print(access_token)
            return access_token, 'Login Successful', True, user.first_name, email, user.enabled, user.user_id, user.last_name
        else:
            return None, 'Invalid password', False
    else:
        return None, 'Email address not found', False


"""function for user logout"""


def logout_user():
    """
        logout service .
        :returns : {
        "status": "logout Success/Failure",
        "message": "appropriate message of logout successful or bad request",
        "data": ""
        }
    """
    jti = get_raw_jwt()['jti']
    black_list.append(jti)
    print(black_list)
