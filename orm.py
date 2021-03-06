#!/usr/bin/env python3
from sqlalchemy import (Column,
                        ForeignKey,
                        SmallInteger,
                        Integer,
                        BigInteger,
                        String,
                        Boolean,
                        DateTime)
from sqlalchemy.dialects import postgresql
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Version(Base):
    __tablename__ = 'version'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), index=True, unique=True)

    def __repr__(self):
        return self.name


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), index=True, unique=True)

    def __repr__(self):
        return self.name


class Gamename(Base):
    __tablename__ = 'gamename'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), index=True, unique=True)

    def __repr__(self):
        return self.name


class Map(Base):
    __tablename__ = 'map'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), index=True, unique=True)

    def __repr__(self):
        return self.name


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name_short = Column(String(2), index=True, unique=True)
    name_long = Column(String(50), index=True, unique=True)

    def __repr__(self):
        return self.name_long


class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True)
    ip = Column(postgresql.INET, index=True, nullable=False)
    port = Column(SmallInteger, index=True, nullable=False)
    active = Column(Boolean)
    first_seen = Column(DateTime,
                        server_default=func.now())
    last_seen = Column(DateTime,
                       server_default=func.now(),
                       onupdate=func.now())

    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship(Country, lazy='joined')

    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game, lazy='joined')

    def __repr__(self):
        return '%s:%s' % (self.ip, self.port)


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(128))
    cheats = Column(SmallInteger)
    needpass = Column(SmallInteger)
    deathmatch = Column(SmallInteger)
    clients = Column(SmallInteger, default=0)
    maxclients = Column(SmallInteger)
    maxspectators = Column(SmallInteger)
    timelimit = Column(SmallInteger)
    fraglimit = Column(SmallInteger)
    protocol = Column(SmallInteger)
    dmflags = Column(Integer)
    uptime = Column(String(50))

    server_id = Column(Integer, ForeignKey('server.id'), nullable=False)
    server = relationship(Server, lazy='joined')

    map_id = Column(Integer, ForeignKey('map.id'))
    map = relationship(Map, lazy='joined')

    version_id = Column(Integer, ForeignKey('version.id'))
    version = relationship(Version, lazy='joined')

    gamename_id = Column(Integer, ForeignKey('gamename.id'))
    gamename = relationship(Gamename, lazy='joined')

    def __repr__(self):
        return self.hostname


class Player(Base):
    __tablename__ = 'player'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(128))
    score = Column(SmallInteger)
    ping = Column(SmallInteger)

    server_id = Column(Integer, ForeignKey('server.id'), nullable=False)
    server = relationship(Server, lazy='joined')

    def __repr__(self):
        return self.name


class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    running = Column(Boolean)
    started = Column(DateTime)
    ended = Column(DateTime)
