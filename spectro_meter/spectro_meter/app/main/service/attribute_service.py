from app.main.model.attribute_model import AttributeModel

def get_all_attribute(session):
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
    attributes = session.query(AttributeModel).all()
    return attributes