import json
import requests
import sys

from getpass import getpass
from pygithub3 import Github
from requests.exceptions import HTTPError
from .core import BaseSharePastes
from .core import Config


class Gist(BaseSharePastes):
    _auth_url = 'https://api.github.com/authorizations'

    def _generate_keys(self):
        config = Config.get()

        def collect_client_keys():
            print '''
Your Github Client Application Keys are missing. First go to the following
link: https://github.com/settings/applications. Create a new application and
generate client keys for SharePastes.
            '''
            client_id = raw_input('Github Client ID: ')
            client_secret = raw_input('Github Client Secret: ')

            try:
                g_config = config.config['gist']
            except KeyError:
                g_config = {}

            g_config.update({
                'client_id': client_id,
                'client_secret': client_secret,
            })

            config.config['gist'] = g_config
            config.save()

        gist_config = config.config.get('gist', None)
        if gist_config:
            if gist_config.get('client_id',
                               None) and gist_config.get('client_secret',
                                                         None):
                pass
            else:
                collect_client_keys()
        else:
            collect_client_keys()

        print '''
Now you must login so that SharePastes can get your API token. SharePastes
does not store passwords.
        '''
        username = raw_input('Github Username: ')
        password = getpass('Github Password: ')

        data = {
            'client_id': config.config['gist']['client_id'],
            'client_secret': config.config['gist']['client_secret'],
            'scopes': ['gist'],
        }

        resp = requests.post(self._auth_url, data=json.dumps(data),
                             headers={'content-type': 'application/json'},
                             auth=(username, password))

        if resp.status_code != 201:
            print 'Error occurred.'
            sys.exit(1)
        else:
            resp_text = json.loads(resp.text)
            config.config['gist'].update({
                'token': resp_text['token'],
            })
            config.save()

    def api_call(self, text):
        config = Config.get()
        try:
            token = config.config['gist']['token']
        except KeyError:
            self._generate_keys()
            token = config.config['gist']['token']

        auth = dict(token=token)
        gh = Github(**auth)

        try:
            r = gh.gists.create(dict(description='', public=True,
                                files={'sharepaste': {'content': text}}))
            print r.html_url
        except HTTPError:
            print 'Error'
            sys.exit(1)

        return r.html_url
