from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean

from app.main.model import CustomInteger
from app.main.model import CustomVarchar
from app.main.model import PasswordVarchar
from app.main import Base
from app.main.model.logo_model import LogoModel
from app.main.model.media_model import MediaModel
from app.main.model.campaign_model import CampaignModel

class UserModel(Base):
    """ user Model for storing user related details """
    __tablename__ = "user"

    user_id = Column(CustomInteger, primary_key=True, nullable=False)
    first_name = Column(CustomVarchar(length=255), nullable=False)
    last_name = Column(CustomVarchar(length=255), nullable=False)
    email = Column(CustomVarchar(length=255), unique=True, nullable=False)
    password_hash = Column(PasswordVarchar(length=60), nullable=False)
    enabled = Column(Boolean, nullable=False, default=True)

    """ defining relationship of user table with user-organization table"""
    # user_organization_logo = relationship("LogoModel", back_populates="user_logo")
    # user_organization_media = relationship("MediaModel", back_populates="user_media")
    # user_organization_campaign = relationship("CampaignModel", back_populates="user_campaign")

    def __init__(self, **kwargs):

        """if user_id key value is 0 then insert operation else update operation"""
        if kwargs.get('user_id') is not None:
            if kwargs.get('user_id') > 0:
                self.user_id = kwargs.get('user_id')
        self.first_name = kwargs.get('first_name')

        self.last_name = kwargs.get('last_name')
        self.email = kwargs.get('email')
        self.password_hash = kwargs.get('password')
        self.enabled = kwargs.get('enabled')

        self.user_organization_logo = []
        """if user_organization key has data then perform add / update operation based on primary key"""
        if kwargs.get('user_organization_logo'):
            for attrib in kwargs.get('user_organization_logo'):
                self.user_organization_logo.append(LogoModel(**attrib))

        self.user_organization_media = []
        """if user_organization key has data then perform add / update operation based on primary key"""
        if kwargs.get('user_organization_media'):
            for attrib in kwargs.get('user_organization_media'):
                self.user_organization_media.append(MediaModel(**attrib))

        self.user_organization_campaign = []
        """if user_organization key has data then perform add / update operation based on primary key"""
        if kwargs.get('user_organization_campaign'):
            for attrib in kwargs.get('user_organization_campaign'):
                self.user_organization_campaign.append(CampaignModel(**attrib))

    # @validates('email')
    # def validate_dates(self, key, field):
    #     regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    #     if not re.search(regex, field):
    #         raise AssertionError("Invalid Email Address.")
    #
    #     return field