# -*- coding: utf-8 -*-
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    EXCLUDE,
    fields,
    Schema,
)
from marshmallow.validate import Length, Range

rom wazo_calld.plugin_helpers.mallow import StrictDict

class KoalaSchema(Schema):
    event_id = fields.Str(required=True, validate=Length(min=1))
    username = fields.Str(required=True, validate=Length(min=4))
    firstname = fields.Str(required=True, validate=Length(min=1))
    lastname = fields.Str(required=True, validate=Length(min=1))
    device_id = fields.Str(required=True, validate=Length(min=1))
    facility = StrictDict(code=fields.Str(required=True, validate=Length(min=1)),
                          name=fields.Str(required=True, validate=Length(min=3)),
                          missing=dict)
    sector = StrictDict(id=fields.Integer(required=True),
                         name=fields.Str(required=True, validate=Length(min=3)),
                         missing=dict)
    job = StrictDict(id=fields.Integer(required=True),
                     name=fields.Str(validate=Length(min=3)),
                     missing=dict)
    expiration = fields.Integer(validate=Range(min=3600), missing=86400)

    class Meta:
        strict = True
        unknown = EXCLUDE

koala_schema = KoalaSchema()