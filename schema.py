#!/usr/bin/env python3
from marshmallow import Schema, fields


class VersionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GameSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class GamenameSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class MapSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class CountrySchema(Schema):
    id = fields.Int(dump_only=True)
    name_short = fields.Str()
    name_long = fields.Str()


class ServerSchema(Schema):
    id = fields.Int(dump_only=True)
    ip = fields.Str()
    port = fields.Int()
    active = fields.Bool()
    first_seen = fields.DateTime()
    last_seen = fields.DateTime()

    country = fields.Nested(CountrySchema)
    game = fields.Nested(GameSchema, validate=must_not_be_blank)


class StatusSchema(Schema):
    id = fields.Int(dump_only=True)
    hostname = fields.Str()
    cheats = fields.Int()
    needpass = fields.Int()
    deathmatch = fields.Int()
    clients = fields.Int()
    maxclients = fields.Int()
    maxspectators = fields.Int()
    timelimit = fields.Int()
    fraglimit = fields.Int()
    protocol = fields.Int()
    dmflags = fields.Int()
    uptime = fields.Int()

    server = fields.Nested(ServerSchema, validate=must_not_be_blank)
    version = fields.Nested(VersionSchema, validate=must_not_be_blank)
    gamename = fields.Nested(GamenameSchema, validate=must_not_be_blank)


class PlayerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    score = fields.Int()
    ping = fields.Int()

    server = fields.Nested(ServerSchema, validate=must_not_be_blank)


class StateSchema(Schema):
    id = fields.Int(dump_only=True)
    started = fields.DateTime()
    ended = fields.DateTime()
