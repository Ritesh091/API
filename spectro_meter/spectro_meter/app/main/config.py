import os
import json
import jsonschema
from os import path

basedir = os.path.abspath(os.path.dirname(__file__))

"""
Validation schema for database configuration. If any required value is missing then it will throw an exception.
"""
schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Schema for a recording",
    "type": "object",
    "definitions": {
        "user": {
            "type": "object",
            "properties": {
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string"}
            },
            "required": ["first_name", "last_name", "email", "password"]
        }
    },
    "properties": {
        "dialect": {"type": "string"},
        "driver": {"type": "string"},
        "db_name": {"type": "string"},
        "user_name": {"type": "string"},
        "password": {"type": "string"},
        "host": {"type": "string"},
        "port": {"type": "string"},
        "users": {
            "type": "array",
            "items": {"$ref": "#/definitions/user"}
        }
    },
    "required": ["dialect", "driver", "db_name", "users"]
}


class Config:
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    #STATIC_DIR_PATH = os.path.join("app", 'static')

    static_dir_path = os.getenv('STATIC_DIR_PATH')
    if path.exists(static_dir_path):
        STATIC_DIR_PATH = static_dir_path

    db_config_file = os.getenv('CALLOMATION_DB_CONFIG')
    # print("db config file : {}".format(db_config_file))
    DB_CONFIG = None
    if os.path.isfile(db_config_file):
        try:
            # Read in the JSON document
            with open(db_config_file) as config_file:
                DB_CONFIG = json.load(config_file)
            # And validate the result
            # print(DB_CONFIG)
            jsonschema.validate(DB_CONFIG, schema)
        except jsonschema.exceptions.ValidationError as e:
            raise SystemExit("Error in configuration file : ", e.message)
        except json.decoder.JSONDecodeError as e:
            raise SystemExit("Error in configuration file format(JSON):", e.msg)
    else:
        raise SystemExit("Database configuration file is missing. "
                         "Check your environmental variable CALLOMATION_DB_CONFIG.")


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = "visibility_meter_dev"

    # dialect + driver: // username: password @ host:port / database
    SQLALCHEMY_DATABASE_URI = Config.DB_CONFIG.get('dialect') \
                              + '+' \
                              + Config.DB_CONFIG.get('driver') \
                              + '://' \
                              + Config.DB_CONFIG.get('user_name') \
                              + ":" + Config.DB_CONFIG.get('password') \
                              + "@" + Config.DB_CONFIG.get('host') \
                              + ":" + Config.DB_CONFIG.get('port') \
                              + "/" + Config.DB_CONFIG.get('db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = "visibility_meter_dev"

    SQLALCHEMY_DATABASE_URI = Config.DB_CONFIG.get('dialect') \
                              + '+' \
                              + Config.DB_CONFIG.get('driver') \
                              + '://' \
                              + Config.DB_CONFIG.get('user_name') \
                              + ":" + Config.DB_CONFIG.get('password') \
                              + "@" + Config.DB_CONFIG.get('host') \
                              + ":" + Config.DB_CONFIG.get('port') \
                              + "/" + Config.DB_CONFIG.get('db_name')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
