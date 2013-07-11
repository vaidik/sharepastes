import requests
import sys

from sharepastes.core import BaseSharePastes
from sharepastes.core import Config


class MozPastebin(BaseSharePastes):
    url = 'http://www.pastebin.mozilla.org'
    params = {
        'parent_pid': '',
        'format': 'text',
        'paste': 'Send',
        'expiry': 'd',
        'poster': '',
    }

    def api_call(self, text):
        self.params.update({
            'code2': text,
        })

        headers = {
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/29.0.1528.0 Safari/537.36'),
            'Origin': 'http://www.pastebin.mozilla.org',
        }
        resp = requests.post(self.url, data=self.params, allow_redirects=False,
                             headers=headers)

        if resp.raw.status == 302:
            print resp.headers['Location']
        else:
            print 'Error'

        return resp.headers['Location']
