#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import config
import datetime

# http://webo.mf/bbs/login_check.php
# mb_id
# mb_password

class WeboLatest(object):
    def __init__(self):
        self.session = requests.Session()
        self.last_datetime = datetime.datetime.now()

    def Check(self):
        r = self.session.get('http://webo.mf/bbs/newsfeed.json.php')
        jsonData = r.json()

        if 'ERROR' in jsonData:
            self.RefreshSession()
            # retry
            r = self.session.get('http://webo.mf/bbs/newsfeed.json.php')
            jsonData = r.json()

        ret = []
        try:
            for article in jsonData['recent_article']:
                article_datetime = datetime.datetime.strptime(article['wr_datetime'], '%Y-%m-%d %H:%M:%S')
                if self.last_datetime < article_datetime:
                    ret.append(article)
        except:
            pass

        self.last_datetime = datetime.datetime.now()
        return ret

    def RefreshSession(self):
        postData = {'mb_id': config.config['webo_account'][0],
                    'mb_password': config.config['webo_account'][1]}
        self.session.post('http://webo.mf/bbs/login_check.php', data=postData)

