#!/usr/bin/env python3
import configparser
from sqlalchemy import create_engine

from orm import Base

config = configparser.ConfigParser()
config.read('config.ini')
dbstring = '{provider}://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(dbstring.format(provider=config['database'].get('provider', 'postgresql'),
                                       username=config['database']['username'],
                                       password=config['database']['password'],
                                       host=config['database']['host'],
                                       port=config['database']['port'],
                                       database=config['database']['database']))
Base.metadata.create_all(engine)
