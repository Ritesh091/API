import sqlalchemy
from sqlalchemy.types import TypeDecorator
from sqlalchemy.types import INTEGER
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import Enum
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.types import TEXT
from sqlalchemy.types import FLOAT
from sqlalchemy.types import DATE
from sqlalchemy.types import TIME
from sqlalchemy.types import DATETIME


class CustomInteger(TypeDecorator):
    """Platform independent Integer value"""

    impl = INTEGER

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.INTEGER(unsigned=True))

class CustomFloat(TypeDecorator):
    """Platform independent Integer value"""

    impl = FLOAT

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.FLOAT(unsigned=True))

class CustomVarchar(TypeDecorator):
    """Platform independent Integer value"""

    impl = VARCHAR

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.VARCHAR(length=self.impl.length))


class PasswordVarchar(TypeDecorator):
    """Platform independent Integer value"""

    impl = VARCHAR

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

    def __repr__(self):
        return "<redacted>"

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.VARCHAR(length=self.impl.length))


class CustomTimestamp(TypeDecorator):
    """Platform independent Integer value"""

    impl = TIMESTAMP

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.TIMESTAMP())


class CustomEnum(TypeDecorator):
    """Platform independent Integer value"""

    impl = Enum

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.ENUM(self.impl.enums))


class CustomText(TypeDecorator):
    """platform independent Text value"""

    impl = TEXT

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(sqlalchemy.dialects.mysql.TEXT(length=self.impl.length))


class CustomDate(TypeDecorator):
    """platform independent Date Value"""

    impl = DATE

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

        def load_dialect_impl(self, dialect):
            if dialect.name == 'mysql':
                return dialect.type_descriptor(sqlalchemy.dialects.mysql.DATE())


class CustomTime(TypeDecorator):
    """platform independent TIME Value"""

    impl = TIME

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

        def load_dialect_impl(self, dialect):
            if dialect.name == 'mysql':
                return dialect.type_descriptor(sqlalchemy.dialects.mysql.TIME())

class CustomDateTime(TypeDecorator):
    """platform independent TIME Value"""

    impl = DATETIME

    def __init__(self, *arg, **kw):
        TypeDecorator.__init__(self, *arg, **kw)

        def load_dialect_impl(self, dialect):
            if dialect.name == 'mysql':
                return dialect.type_descriptor(sqlalchemy.dialects.mysql.DATETIME())
