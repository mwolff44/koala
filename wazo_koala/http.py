# -*- coding: utf-8 -*-
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from flask import request
from flask_restful import Resource
from xivo.tenant_flask_helpers import Tenant

from wazo_confd.auth import required_acl
from wazo_confd.http import AuthResource

from .schema import (
    koala_schema,
)


class KoalaResource(AuthResource):

    def __init__(self, koala_service):
        self.koala_service = koala_service

    #@required_acl('confd.koala.create')
    def login(self):
        request_body = intercept_schema.load(request.get_json(force=True))
        result = self._koala_service.login(request_body)

        return result, 201

    #@required_acl('confd.koala.create')
    def logout(self):
        request_body = intercept_schema.load(request.get_json(force=True))
        result = self._koala_service.login(request_body)

        return result, 201