params = {
    # Get your api_dev_key from http://pastebin.com/api#1.
    'api_dev_key': '',

    # Get your api_user_key using the api_user_key_generator.py
    'api_user_key': '',

    # Set this to 1 if you want to keep your postes private.
    'api_paste_private': '0',

    # Set an expiration date for your pastes.
    'api_paste_expire_date': '10M',

    # Don't touch this. Even I don't know/care how this works.
    'api_option': 'paste',
}

url = 'http://pastebin.com/api/api_post.php'

import pynotify
import re
import urllib2
from urllib import urlencode

import pygtk
pygtk.require('2.0')
import gtk

clipboard = gtk.clipboard_get()

params['api_paste_code'] = clipboard.wait_for_text()
params['api_paste_name'] = ''

request = urllib2.Request(url, urlencode(params))
response = urllib2.urlopen(request)

response = response.read()
regex = re.compile('http://pastebin.com/*')
result = regex.match(response)

init = pynotify.init('SharePastes')

if result:
    clipboard.set_text(response)
    clipboard.store()
    n = pynotify.Notification('Success', 'Clipboard text submitted. Press Ctrl+v to paste the URL.')
else:
    n = pynotify.Notification('Error', 'Couldn\'t submit the latest text from your clipboard.', 'dialog-error')

n.show()

