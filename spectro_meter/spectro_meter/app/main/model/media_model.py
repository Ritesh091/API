from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
from sqlalchemy import ForeignKey
from app.main.model import CustomDateTime
from app.main.model import CustomVarchar
from app.main.model import CustomInteger
from app.main.model.activity_record import ActivityRecord

class MediaModel(Base,ActivityRecord):
    """ media Model for storing media related details """
    __tablename__ = "media"

    media_id = Column(CustomInteger, primary_key=True, nullable=False)
    name = Column(CustomVarchar(length=100), nullable=False)
    description = Column(CustomVarchar(length=1000), nullable=True)
    mediaThumbnailPath = Column(CustomVarchar(length=200), nullable=False)
    mediaThumbnailName = Column(CustomVarchar(length=1000), nullable=False)
    mediaPath = Column(CustomVarchar(length=200), nullable=False)
    filename = Column(CustomVarchar(length=200), nullable=False)
    model_filename = Column(CustomVarchar(length=1000), nullable=False)
    duration = Column(CustomVarchar(length=45), nullable=False)
    #created_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    #modified_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_date = Column(CustomDateTime, nullable=False)
    # modified_date = Column(CustomDateTime, nullable=False)
    
    camp_medias = relationship("CampaignMediaModel", back_populates="medias")
    # attributes = relationship("AttributeModel", back_populates = "medias")
    # camp_detail = relationship("CampaigndetailModel", back_populates="medias")
    created_by_user = relationship("UserModel", foreign_keys='[MediaModel.created_by]')
    modified_by_user = relationship("UserModel", foreign_keys='[MediaModel.modified_by]')