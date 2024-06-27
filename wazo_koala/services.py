# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging



class KoalaService(object):

    def __init__(self, confd):
        self.confd = confd

    def add_koala_member(self, params, tenant.uuid):
        users = self._get_user_list(tenant_uuid)
        self._remove_old_koala_member(params, tenant.uuid, users)
        self._assign_koala_member(params, tenant_uuid)
        

        add_member = {
            'eventID': params.get('eventId'),
            'username': params.get('username'),
            'firstName': params.get('firstName'),
            'lastName': params.get('lastName'),
            'deviceID': params.get('deviceId'),
            'facilityCode': params.get('facility')['code'],
            'facilityName': params.get('facility')['name'],
            'sectorID': params.get('sector')['id'],
            'sectorName': params.get('sector')['name'],
            'jobID': params.get('job')['id'],
            'jobName': params.get('job')['name'],
            'expiration': params.get('expiration')
        }
        return 'OK'

    def remove_koala_member(self, params, tenant.uuid):
        users = self._get_user_list(tenant_uuid)
        self._remove_old_koala_member(params, tenant.uuid, users)

        remove_member = {
            'eventID': params.get('eventId'),
            'username': params.get('username'),
            'firstName': params.get('firstName'),
            'lastName': params.get('lastName'),
            'deviceID': params.get('deviceId'),
            'facilityCode': params.get('facility')['code'],
            'facilityName': params.get('facility')['name'],
            'sectorID': params.get('sector')['id'],
            'sectorName': params.get('sector')['name'],
            'jobID': params.get('job')['id'],
            'jobName': params.get('job')['name'],
            'expiration': params.get('expiration')
        }
        return 'OK'

    def _get_user_list(self, tenant_uuid):
        return self.confd.users.list(tenant_uuid=tenant_uuid)

    def _find_wazo_user(self, users, deviceID):
        for user in users:
            if str(user['email']) == deviceID:
                return user['id']
            if str(user['firstname']) == deviceID:
                return user['id']

    def _find_wazo_user_associated_with_username(self, users, username):
        for user in users:
            if str(user['userfield']) == username:
                return user['id']

    def _find_group(self, tenant_uuid, group_name):
        # Get group id based on group name
        groups = self.confd.groups.list(tenant_uuid=tenant_uuid)
            for group in groups['items']:
                if str(group['label']) == group_name:
                    return group['id']
                
    def _add_member_groups(self, wazo_user_id, sector_name, username):
        # Add the Wazo user form Groups
        # Get sector group_id
        group_sector_id = self._find_group(tenant_uuid, sector_name)
        # Get user group_id
        group_user_id = self._find_group(tenant_uuid, username)       
        # Add Wazo user to group
        self.confd.users.relations(wazo_user_id).update_groups([{'id': group_sector_id, 'id': group_user_id}])

    def _remove_member_groups(self, wazo_user_id):
        # Remove the Wazo user form Groups
        self.confd.users.relations(wazo_user_id).update_groups([])

    def _remove_old_koala_member(self, params, tenant.uuid, users):
        # Check if this deviceID is already assigned to a wazo user
        old_wazo_user_id = self._find_wazo_user_associated_with_username(users, params.get('username'))
        if old_wazo_user_id:
            # ToDo : Clear koala user info
            # ToDo : Remove fallbacks
            # ToDo : Reset name in main user line
        else:
            print("deviceID not assigned to a wazo user")

        wazo_device_id = self._find_wazo_user(users, params.get('deviceId'))
        if wazo_device_id:
            _remove_member_groups(wazo_device_id)
        else:
            print("deviceID not assigned to goups")

    def _assign_koala_member(self, params, tenant_uuid):
        wazo_user_id = self._find_wazo_user(users, params.get('deviceId'))
        if wazo_user_id:
            # Todo : Affect the koala user to wazo device
            # Todo : Change firstname and lastname in wazo user
            # Todo : Change name in main user line

            # Affect Wazo device to groups
            self._add_member_groups(
                wazo_user_id,
                params.get('deviceId'),
                params.get('sector')['name']
            )
        else:
            print("deviceID unknown")