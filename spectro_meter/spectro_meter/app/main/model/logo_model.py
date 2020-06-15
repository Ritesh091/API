import enum
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum
from app.main.model import CustomDateTime
from app.main.model import CustomVarchar
from app.main.model import CustomInteger
from app.main import Base
from app.main.model.activity_record import ActivityRecord

class StatusType(enum.Enum):
    submitted = 'submitted'
    review = 'review'
    approved = 'approved' 
    rejected = 'rejected'

class LogoModel(Base,ActivityRecord):
    """ lookup Model for storing logo related details """
    __tablename__ = "logo"

    logo_id = Column(CustomInteger, primary_key=True, nullable=False)
    name = Column(CustomVarchar(length=45), nullable=False)
    description = Column(CustomVarchar(length=45), nullable=True)
    filename = Column(CustomVarchar(length=45), nullable=False)
    mediaPath = Column(CustomVarchar(length=1000), nullable=False)
    model_filename = Column(CustomVarchar(length=1000), nullable=True)
    model_config = Column(CustomVarchar(length=1000), nullable=True)
    label_filename = Column(CustomVarchar(length=1000), nullable=True)
    model_class_id = Column(CustomInteger, nullable=True)
    status = Column(Enum(StatusType), nullable=False)
    # created_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # modified_by = Column(CustomInteger, ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    # created_date = Column(CustomDateTime, nullable=False)
    # modified_date = Column(CustomDateTime, nullable=False)
    created_by_user = relationship("UserModel", foreign_keys='[LogoModel.created_by]')
    modified_by_user = relationship("UserModel", foreign_keys='[LogoModel.modified_by]')

    campaigns = relationship("CampaignModel", back_populates="lookups")

    def __init__(self, **kwargs):

        """if user_id key value is 0 then insert operation else update operation"""
        if kwargs.get('logo_id') is not None:
            if kwargs.get('logo_id') > 0:
                self.logo_id = kwargs.get('logo_id')
        self.name = kwargs.get('title')
        self.description = kwargs.get('description')
        self.filename = kwargs.get('filename')
        self.model_filename = kwargs.get('model_filename')
        self.model_config = kwargs.get('model_config')
        self.label_filename = kwargs.get('label_filename')
        self.model_class_id = kwargs.get('model_class_id')
        self.status = kwargs.get('status')
        self.created_by = kwargs.get('created_by')
        self.modified_by = kwargs.get('modified_by')
        self.created_date = kwargs.get('created_date')
        self.modified_date = kwargs.get('modified_date')

        # self.campaign = []
        # """if user_organization key has data then perform add / update operation based on primary key"""
        # if kwargs.get('campaign'):
        #     for attrib in kwargs.get('campaign'):
        #         self.campaign.append(CampaignModel(**attrib))

