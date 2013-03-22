import gtk
import importlib
import json
import optparse
import os
import sys


class BaseSharePastes(object):
    _clipboard = gtk.clipboard_get()

    def __init__(self):
        pass

    def get_copied_text(self):
        return self._clipboard.wait_for_text()

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
    obj.api_call(obj.get_copied_text())


if __name__ == '__main__':
    main()
