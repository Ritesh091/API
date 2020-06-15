from app.main.model.media_model import MediaModel

def get_all_media(session):
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
    medias = session.query(MediaModel).all()
    return medias