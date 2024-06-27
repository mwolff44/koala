# -*- coding: utf-8 -*-
# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from wazo_auth_client import Client as AuthClient
from wazo_confd_client import Client as ConfdClient

from .http import KoalaLoginResource, KoalaLogoutResource
from .services import KoalaService

logger = logging.getLogger(__name__)

class Plugin:

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        token_changed_subscribe = dependencies['token_changed_subscribe']

        auth_client = AuthClient(**config['auth'])
        confd_client = ConfdClient(**config['confd'])

        token_changed_subscribe(confd_client.set_token)

        koala_service = KoalaService(confd_client)

        api.add_resource(
            KoalaLoginResource,
            '/koala/login',
            resource_class_args=[koala_service]
        )
        api.add_resource(
            KoalaLogoutResource,
            '/koala/logout',
            resource_class_args=[koala_service]
        )
