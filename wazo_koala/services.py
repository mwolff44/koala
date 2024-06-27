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
            'FacilityCode': params.get('facility').json['code'],
            'FacilityName': params.get('facility').json['name'],
            'SectorID': params.get('sector').json['id'],
            'SectorName': params.get('sector').json['name'],
            'JobID': params.get('job').json['id'],
            'JobName': params.get('job').json['name'],
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
            'FacilityCode': params.get('facility').json['code'],
            'FacilityName': params.get('facility').json['name'],
            'SectorID': params.get('sector').json['id'],
            'SectorName': params.get('sector').json['name'],
            'JobID': params.get('job').json['id'],
            'JobName': params.get('job').json['name'],
            'Expiration': params.get('expiration')
        }
        return 'OK'


