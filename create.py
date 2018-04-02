#!/usr/bin/env python3
import configparser

from orm import Base
from functions import create_db_conn


config = configparser.ConfigParser()
config.read('config.ini')
engine = create_db_conn(config['general'].get('environment', 'testing'))
Base.metadata.create_all(engine)
