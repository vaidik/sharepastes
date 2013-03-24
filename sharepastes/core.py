import json
import os
import sys

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
            print 'The service %s does not work with SharePastes.' % type
            sys.exit(1)


class Config(object):
    file_path = os.path.join(os.path.expanduser('~'), '.sharepastes.config')
    config = None

    @staticmethod
    def get():
        if not Config.config:
            config = Config()
            config.load()

        return config

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
