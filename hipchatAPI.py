#!/usr/bin/python

import requests

class HipchatAPI(object):
    access_token = ''
    def __init__(self, access_token):
        self.access_token = access_token

    def rooms(self):
        r = requests.get('https://api.hipchat.com/v1/rooms/list?auth_token=' + self.access_token)
        return r.json()

    def message(self, room_id, from_, message, message_format=None):
        if not message_format:
            message_format = 'text'

        payload = {'room_id': room_id,
                   'from': from_,
                   'message': message,
                   'message_format': message_format,
                   'auth_token': self.access_token}
        r = requests.get('https://api.hipchat.com/v1/rooms/message', params=payload)
        return r.text
