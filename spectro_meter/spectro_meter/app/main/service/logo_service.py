from app.main.model.logo_model import LogoModel

def get_all_logo(session):
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
    logos = session.query(LogoModel).all()
    return logos