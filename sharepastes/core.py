import json
import os
import sys

from importlib import import_module


class BaseSharePastes(object):
    """ Base class that must be extended while writing a module to extend
    SharePastes. """

    def __init__(self):
        pass

    def api_call(self, text):
        """ Supposed to do the actual work of posting text to a service.

        :param str text: the text that is to be posted.
        :returns: a valid URL if posting to the service succeeds.

        .. note ::
            Must be implemented in the inherited class or else this method will
            raise a ``NotImplementedError`` exception.
        """
        raise NotImplementedError('api_call method must be implemented.')


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
    """ Handle configuration for your SharePastes extensions. """

    file_path = os.path.join(os.path.expanduser('~'), '.sharepastes.config')
    """ Path of the file where the config file lives. """

    config = None
    """ Static variable that holds the singleton `Config`_ object."""

    @staticmethod
    def get():
        """ Get the static Config object.

        :returns: the singleton *Config* object.
        """
        if not Config.config:
            config = Config()
            config.load()

        return config

    def load(self):
        """ Forcefully reload the configuration from the config file. """
        try:
            f = open(self.file_path, 'r')
            self.config = json.loads(f.read())
            f.close()
        except IOError:
            self.config = {}

    def save(self):
        """ Save configuration to the config file. """
        f = open(self.file_path, 'w')
        f.write(json.dumps(self.config))
        f.close()
