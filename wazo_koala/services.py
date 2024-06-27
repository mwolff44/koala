# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging



class KoalaService(object):

    def __init__(self, confd):
        self.confd = confd

    def add_koala_member(self, params):
        add_member = {
            'EventID': params.get('eventId'),
            'Username': params.get('username'),
            'FirstName': params.get('firstName'),
            'LastName': params.get('lastName'),
            'DeviceID': params.get('deviceId'),
            'FacilityCode': params.get('facility')['code'],
            'FacilityName': params.get('facility')['name'],
            'SectorID': params.get('sector')['id'],
            'SectorName': params.get('sector')['name'],
            'JobID': params.get('job')['id'],
            'JobName': params.get('job')['name'],
            'Expiration': params.get('expiration')
        }
        return 'OK'


    def remove_koala_member(self, params):
        remove_member = {
            'EventID': params.get('eventId'),
            'Username': params.get('username'),
            'FirstName': params.get('firstName'),
            'LastName': params.get('lastName'),
            'DeviceID': params.get('deviceId'),
            'FacilityCode': params.get('facility')['code'],
            'FacilityName': params.get('facility')['name'],
            'SectorID': params.get('sector')['id'],
            'SectorName': params.get('sector')['name'],
            'JobID': params.get('job')['id'],
            'JobName': params.get('job')['name'],
            'Expiration': params.get('expiration')
        }
        return 'OK'


