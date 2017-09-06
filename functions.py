#!/usr/bin/env python3
import configparser

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


def create_session():
    config = configparser.ConfigParser()
    config.read('config.ini')
    dbstring = '{provider}://{username}:{password}@{host}:{port}/{database}'
    engine = create_engine(dbstring.format(provider=config['database'].get('provider', 'postgresql'),
                                           username=config['database']['username'],
                                           password=config['database']['password'],
                                           host=config['database']['host'],
                                           port=config['database']['port'],
                                           database=config['database']['database']))
    Session = sessionmaker(bind=engine)
    return Session()
