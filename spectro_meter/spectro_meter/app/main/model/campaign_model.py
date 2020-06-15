from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
from sqlalchemy import ForeignKey
from app.main.model import CustomDateTime
from app.main.model import CustomVarchar
from app.main.model import CustomInteger
from app.main.model.activity_record import ActivityRecord

class CampaignModel(Base,ActivityRecord):
    """ user Model for storing user related details """
    __tablename__ = "campaign"

    campaign_id = Column(CustomInteger, primary_key=True, nullable=False)
    name = Column(CustomVarchar(length=100), nullable=False)
    description = Column(CustomVarchar(length=1000), nullable=True)
    tags = Column(CustomVarchar(length=200), nullable=True)
    logo_id = Column(CustomInteger, ForeignKey('logo.logo_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # media_id = Column(CustomInteger, ForeignKey('media.media_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # modified_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_date = Column(CustomDateTime, nullable=False)
    # modified_date = Column(CustomDateTime, nullable=False)

    lookups = relationship("LogoModel", back_populates="campaigns")
    camp_medias = relationship("CampaignMediaModel", back_populates = "campaigns")
    created_by_user = relationship("UserModel", foreign_keys='[CampaignModel.created_by]')
    modified_by_user = relationship("UserModel", foreign_keys='[CampaignModel.modified_by]')