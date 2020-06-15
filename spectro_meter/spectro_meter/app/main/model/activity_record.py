from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from . import CustomInteger
from . import CustomTimestamp


class ActivityRecord(object):
    @declared_attr
    def created_by(cls):
        return Column(CustomInteger,
                      ForeignKey('user.user_id',
                                 ondelete='CASCADE',
                                 onupdate='CASCADE'),
                      nullable=False, index=True)

    @declared_attr
    def created_date(cls):
        return Column(CustomTimestamp, nullable=False, server_default=func.current_timestamp())

    @declared_attr
    def modified_by(cls):
        return Column(CustomInteger,
                      ForeignKey('user.user_id',
                                 ondelete='CASCADE',
                                 onupdate='CASCADE'),
                      nullable=False, index=True)

    @declared_attr
    def modified_date(cls):
        return Column(CustomTimestamp, nullable=False, server_default=func.current_timestamp(),
                      onupdate=func.current_timestamp())
