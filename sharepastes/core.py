import json
import optparse
import os
import sys
import xerox

from importlib import import_module


class BaseSharePastes(object):
    def __init__(self):
        pass

    def api_call(self, text):
        pass


class SharePastesFactory(object):
    @staticmethod
    def create(type='pastebin'):
        try:
            return getattr(import_module('.%s' % type, 'sharepastes'),
                           type)()
        except ImportError:
            raise
            print 'The service %s does not work with SharePastes.' % type
            sys.exit(1)


class ConfigFile(object):
    file_path = os.path.join(os.path.expanduser('~'), '.sharepastes.config')

    def load(self):
        try:
            f = open(self.file_path, 'r')
            self.config = json.loads(f.read())
            f.close()
        except IOError:
            self.config = {}

    def save(self):
        f = open(self.file_path, 'w')
        f.write(json.dumps(self.config))
        f.close()


# The common CONFIG object for every module
CONFIG = None


# function to return the CONFIG object
def get_config():
    global CONFIG
    if not CONFIG:
        CONFIG = ConfigFile()
        CONFIG.load()

    return CONFIG
