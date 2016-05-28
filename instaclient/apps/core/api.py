#-*- coding: utf-8 -*-

from instaclient.settings.secret import access_token

import requests
import json


class InstaApi(object):

    results = []

    def __init__(self, hashtag):
        try:
            url = "https://api.instagram.com/v1/tags/{0}/media/recent?access_token={1}".format(hashtag, access_token)
            self.results = (requests.get(url)).json()['data']
        except:
            self.results = []

    def get_images(self):
        return [result['images'] for result in self.results]
