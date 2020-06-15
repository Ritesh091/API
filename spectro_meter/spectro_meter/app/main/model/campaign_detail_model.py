from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
from sqlalchemy import ForeignKey
from app.main.model import CustomDateTime
from app.main.model import CustomVarchar
from app.main.model import CustomInteger
from app.main.model import CustomFloat


class CampaignDetailModel(Base):
    """ media Model for storing media related details """
    __tablename__ = "media_detail"

    id = Column(CustomInteger, primary_key=True, nullable=False)
    camp_media_id = Column(CustomInteger, ForeignKey('camp_media.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    visibility_score = Column(CustomFloat,  nullable=False)
    appearance = Column(CustomFloat,  nullable=False)
    bulls_eye = Column(CustomFloat,  nullable=False)
    corner_kings = Column(CustomFloat,  nullable=False)
    longest_logo_duration = Column(CustomFloat,  nullable=False)
    largest_area_percentage = Column(CustomFloat,  nullable=False)
    exposure_rate = Column(CustomFloat,  nullable=False)
    annotated_video_path = Column(CustomVarchar(length=2000), nullable=False)

    camp_medias = relationship("CampaignMediaModel", back_populates="camp_detail")