#!/usr/bin/env python3
import configparser
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_or_create(session, model, **kwargs):
    """
    Copied from:
    https://stackoverflow.com/questions/2546207/does-sqlalchemy-have-an-equivalent-of-djangos-get-or-create
    """

    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def create_db_conn(environment):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'config.ini'))
    dbstring = '{provider}://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(dbstring.format(provider=config[environment].get('provider', 'postgresql'),
                                           username=config[environment]['username'],
                                           password=config[environment]['password'],
                                           host=config[environment].get('host', 'localhost'),
                                           port=config[environment].get('port', '5432'),
                                           database=config[environment]['database']))

    return engine


def create_db_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
