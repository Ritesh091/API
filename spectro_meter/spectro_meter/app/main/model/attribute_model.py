from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
from sqlalchemy import ForeignKey
from app.main.model import CustomText
from app.main.model import CustomFloat
from app.main.model import CustomInteger
from app.main.model import CustomVarchar

class AttributeModel(Base):
    """ media Model for storing media related details """
    __tablename__ = "attribute"

    id = Column(CustomInteger, primary_key=True, nullable=False)
    camp_media_id = Column(CustomInteger, ForeignKey('camp_media.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    time = Column(CustomVarchar(length=13), nullable=False)
    visibility_score = Column(CustomFloat, nullable=False)

    camp_medias = relationship("CampaignMediaModel", back_populates="attributes")