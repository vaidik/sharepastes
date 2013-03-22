import re
import requests
import sys

from getpass import getpass
from .sharepastes import BaseSharePastes
from .sharepastes import get_config


class pastebin(BaseSharePastes):
    url = 'http://pastebin.com/api/api_post.php'
    params = {
        'api_dev_key': '',
        'api_user_key': '',
        'api_paste_private': 0,
        'api_paste_expire_date': '10M',
        'api_option': 'paste',
    }

    def __init__(self):
        config = get_config()

        try:
            self.set_keys(config.config['pastebin']['dev_key'],
                         config.config['pastebin']['user_key'])
        except KeyError:
            self._generate_keys()
            self.set_keys(config.config['pastebin']['dev_key'],
                         config.config['pastebin']['user_key'])

    def set_keys(self, api_dev_key='', api_user_key=''):
        self.params.update(api_dev_key=api_dev_key, api_user_key=api_user_key)

    def _generate_keys(self):
        config = get_config()

        def collect_client_keys():
            developer_key = raw_input('Pastebin Developer API Key: ')

            pb_config = {
                'dev_key': developer_key
            }

            config.config['pastebin'] = pb_config
            config.save()

        pb_config = config.config.get('pastebin', None)
        if not pb_config:
            collect_client_keys()
        else:
            if not pb_config.get('dev_key', None):
                collect_client_keys()

        username = raw_input('Pastebin Username: ')
        password = getpass('Pastebin Password: ')

        params = {
            'api_dev_key': config.config['pastebin']['dev_key'],
            'api_user_name': username,
            'api_user_password': password,
        }
        r = requests.post('http://pastebin.com/api/api_login.php', data=params)

        regex = re.compile('Bad')
        if not regex.match(r.text):
            user_key = r.text
            config.config['pastebin']['user_key'] = user_key
            config.save()
        else:
            print 'Error. Something went wrong.'
            sys.exit(1)

    def api_call(self, text):
        self.params.update({
            'api_paste_code': text,
            'api_paste_name': 'test',
        })

        resp = requests.post(self.url, data=self.params)

        regex = re.compile('http://pastebin.com/*')
        result = regex.match(resp.text)

        if result:
            print resp.text
        else:
            print 'Error'
