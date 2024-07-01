# -*- coding: utf-8 -*-
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from flask import request
from flask_restful import Resource
from xivo.tenant_flask_helpers import Tenant

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource

from .schema import (
    koala_schema,
)


class KoalaLoginResource(AuthResource):

    def __init__(self, koala_service):
        self._koala_service = koala_service

    #@required_acl('confd.koala.create')
    def post(self):
        tenant = Tenant.autodetect()
        request_body = koala_schema.load(request.get_json(force=True))
        success = self._koala_service.add_koala_member(request_body, tenant.uuid)

        if success:
            return "Successfull login", 201
        esle:
            return "Error"", 400

class KoalaLogoutResource(AuthResource):

    def __init__(self, koala_service):
        self._koala_service = koala_service

    #@required_acl('confd.koala.create')
    def post(self):
        tenant = Tenant.autodetect()
        request_body = koala_schema.load(request.get_json(force=True))
        result = self._koala_service.remove_koala_member(request_body, tenant.uuid)

        return result, 201