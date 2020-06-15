from app.main.model.campaign_detail_model import CampaignDetailModel

def get_all_campaign_detail(session):
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
    camp_detail = session.query(CampaignDetailModel).all()
    return camp_detail