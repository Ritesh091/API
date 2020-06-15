from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
import enum
from sqlalchemy import ForeignKey
from sqlalchemy.types import Enum
from app.main.model import CustomInteger

class StatusType(enum.Enum):
    new = 'new'
    queued = 'queued'
    processing = 'processing'
    completed = 'completed'

class CampaignMediaModel(Base):
    """ media Model for storing media related details """
    __tablename__ = "camp_media"

    id = Column(CustomInteger, primary_key=True, nullable=False)
    media_id = Column(CustomInteger, ForeignKey('media.media_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    campaign_id = Column(CustomInteger, ForeignKey('campaign.campaign_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    status = Column(Enum(StatusType), nullable=False)

    campaigns = relationship("CampaignModel", back_populates="camp_medias")
    medias = relationship("MediaModel", back_populates="camp_medias")
    attributes = relationship("AttributeModel", back_populates="camp_medias")
    camp_detail = relationship("CampaignDetailModel", back_populates="camp_medias")
