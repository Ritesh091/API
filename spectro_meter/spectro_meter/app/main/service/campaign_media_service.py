from app.main.model.campaign_media_model import CampaignMediaModel
from app.main.model.media_model import MediaModel

def get_all_campaign_media(session,campaign_id):
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
    campaign_medias = session.query(CampaignMediaModel).filter_by(campaign_id=campaign_id).all()
    return campaign_medias

def get_media_analysis(session,camp_media_id):
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
    media_analysis = session.query(CampaignMediaModel).filter_by(id=camp_media_id).all()
    return media_analysis