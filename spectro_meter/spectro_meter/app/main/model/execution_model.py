from sqlalchemy import Column
from sqlalchemy.orm import relationship
from app.main import Base
from sqlalchemy import ForeignKey
from app.main.model import CustomDateTime
from app.main.model import CustomVarchar
from app.main.model import CustomInteger

class ExecutionModel(Base):
    """ user Model for storing user related details """
    __tablename__ = "execution"

    campaign_id = Column(CustomInteger, primary_key=True, nullable=False)
    filename = Column(CustomVarchar(length=1000), nullable=False)
    output_filename = Column(CustomVarchar(length=1000), nullable=True)
    duration = Column(CustomVarchar(length=100), nullable=True)
    video_fps = Column(CustomInteger, nullable=False)
    video_frames = Column(CustomInteger, nullable=False)
    video_width = Column(CustomInteger, nullable=False)
    video_height = Column(CustomVarchar(length=45), nullable=False)