params = {
    # Get your api_dev_key from http://pastebin.com/api#1.
    'api_dev_key': '',

    # Use your Pastebin.com username.
    'api_user_name': '',

    # Use your Pastebin.com password.
    'api_user_password': '',
}
url = 'http://pastebin.com/api/api_login.php'

import re
import urllib2
from urllib import urlencode

request = urllib2.Request(url, urlencode(params))
response = urllib2.urlopen(request)

response = response.read()
regex = re.compile('bad', re.IGNORECASE)
result = regex.match(response)

if not result:
    print 'Success: fetched your api_user_key\n'
    print 'Copy this api_user_key, open sharepastes.py and set api_user_key to this value.'
    print response
else:
    print 'Error: couldn\'t fetch your api_user_key. Check login credentials and try again.'

