import importlib
import json
import optparse
import os
import sys
import xerox


class BaseSharePastes(object):
    def __init__(self):
        pass

    def api_call(self, text):
        pass


class SharePastesFactory(object):
    @staticmethod
    def create(type='pastebin'):
        try:
            return getattr(importlib.import_module(type), type)()
        except ImportError:
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


def main():
    parser = optparse.OptionParser()
    using_help = '''
    the service that you want to use. For example: gist for Github's Gist,
    pastebin for PasteBin.com
    '''
    parser.add_option('-u', '--using', dest='using',
                      help=using_help)

    (options, args) = parser.parse_args()

    using = options.using
    if not using:
        using = 'pastebin'

    obj = SharePastesFactory.create(using)
    try:
        obj.api_call(xerox.paste)
    except xerox.base.XclipNotFound:
        print 'xclip not found. Install xclip for SharePastes to work.'
        sys.exit(1)


if __name__ == '__main__':
    main()
