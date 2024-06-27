# -*- coding: utf-8 -*-
# Copyright 024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_auth_client import Client as AuthClient
from wazo_confd_client import Client as ConfdClient

from .resources import (
    LoginResource
    )
from .services import KoalaService


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        token_renewer = dependencies['token_renewer']

        auth_client = AuthClient(**config['auth'])
        confd_client = ConfdClient(**config['confd'])

        token_renewer.subscribe_to_next_token_details_change(
            self.set_service_tenant_uuid
        )

        koala_service = KoalaService(confd_client)

        api.add_resource(QueuesResource, '/koala/login', resource_class_args=[koala_service])
        api.add_resource(QueuesResource, '/koala/logout', resource_class_args=[koala_service])
