# -*- coding: utf-8 -*-
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    EXCLUDE,
    fields,
    Schema,
)
from marshmallow.validate import Length, Range

class FacilitySchema(Schema):
    code = fields.Str(required=True, validate=Length(min=1))
    name = fields.Str(required=True, validate=Length(min=3))

class SectorSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True, validate=Length(min=3))

class JobSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True, validate=Length(min=3))

class KoalaSchema(Schema):
    eventId = fields.Str(required=True, validate=Length(min=1))
    username = fields.Str(required=True, validate=Length(min=4))
    firstName = fields.Str(required=True, validate=Length(min=1))
    lastName = fields.Str(required=True, validate=Length(min=1))
    deviceId = fields.Str(required=True, validate=Length(min=1))
    facility = fields.Nested(FacilitySchema)
    sector = fields.Nested(SectorSchema)
    job = fields.Nested(JobSchema)
    expiration = fields.Integer(validate=Range(min=3600), missing=86400)

    class Meta:
        strict = True
        unknown = EXCLUDE

koala_schema = KoalaSchema()