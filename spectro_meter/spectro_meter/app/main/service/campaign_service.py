from app.main.model.campaign_model import CampaignModel

def get_campaign(session,campaign_id):
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
    campaigns = session.query(CampaignModel).filter_by(campaign_id=campaign_id).all()
    return campaigns

def get_all_campaigns(session):
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
    campaigns = session.query(CampaignModel).all()
    return campaigns