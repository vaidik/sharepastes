.. SharePastes documentation master file, created by
   sphinx-quickstart on Sun Mar 24 17:33:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Extending SharePastes
=====================

SharePastes can be easily extended to work with other similar services.

Deciding an identifier
----------------------

You first need to decide an identifier for your service that will be used by
SharePastes to identify your extension. For example:

* ``gist`` is for Github's Gist.
* ``pastebin`` is for Pastebin.com.

This identifier will be used to name your ``module`` and ``class``.

Creating the module for your new extension
------------------------------------------

Lets assume that name of your extension's identifier is ``gdocs`` and you are
writing this to get support for Google Docs. Then, the name of your module will
be ``gdocs.py`` and the class that you will create in your module will also be
``gdocs``.

Sample code for your extension's module (``gdocs.py``): ::

    import json
    import requests
    import sys

    from sharepastes import BaseSharePastes
    from sharepastes import Config

    # notice that the name of the class here is gdocs and it extends
    # BaseSharePastes
    class gdocs(BaseSharePastes):
        def __init__(self):
            pass

        # you have to implement api_call method. Make sure that you add an
        # argument to receive the text from your clipboard.
        def api_call(self, text):
            # do something awesome here
            # make API calls to Google Docs to create a new document

            # something like (obviously you must checkout GoogleDocs API docs):
            r = requests.post('http://docs.google.com/document',
                              data=json.dumps({ 'document': text }),
                              headers={ 'Authorization': 'Your auth token' })

            # check if it really happened
            if r.status_code != 201:
                # if not, then exit.
                print 'Error.'
                sys.exit(1)
            else:
                # if it worked, then somehow get the URL of the new document
                # from the response
                response = json.loads(r.text)
                print 'Done: ' + response.document_url

                # Return the document URL that you would want to share.
                # This URL will be copied to your clipboard by SharePastes so
                # that you can quickly paste it.
                return response.document_url

BaseSharePastes Class
+++++++++++++++++++++

.. autoclass:: sharepastes.core.BaseSharePastes
   :members:

Saving Configuration
--------------------

Since you are dealing with APIs, you would want to store user credentials or
API tokens or auth keys.

SharePastes provides a way to store such information in text files which are
saved in ``$HOME_DIR`` by the name ``.sharepastes.conf`` on Mac and Linux and
similarly on an equivalent location on Windows.

**Note:** The contents of the config file are JSON encoded.

Using Config (Example)
++++++++++++++++++++++

Lets say you want to save your auth token for Google Docs. This is what you may
do: ::

    import json
    import requests
    import sys

    from sharepastes import BaseSharePastes
    from sharepastes import Config

    # notice that the name of the class here is gdocs and it extends
    # BaseSharePastes
    class gdocs(BaseSharePastes):
        def __init__(self):
            pass

        def _generate_key(self):
            # do something to get your API keys
            r = requests.post('http://www.google.com/authorize/',
                              auth=('username', 'password'))
            if r.status_code == 200:
                resp = json.loads(r.text)

                # get the Config object
                config = Config.get()

                # The config.config variable returns a dict
                # Use it to store your auth keys.
                # Create a new key for your extension by your extension's
                # unique identifier.
                config.config['gdocs'] = {
                    'token' = resp.token
                }

                # finally, save it so that the changes are committed to the
                # conf file.
                config.save()
            else:
                print 'Error'
                sys.exit(1)

        def api_call(self, text):
            config = Config.get()
            try:
                auth_token = config.config['gdocs]'['token']
            except KeyError:
                self._generate_key()
                auth_token = config.config['gdocs]'['token']

            # do something awesome here
            # make API calls to Google Docs to create a new document
            # something like (obviously you must checkout GoogleDocs API docs):
            r = requests.post('http://docs.google.com/document',
                              data=json.dumps({ 'document': text }),
                              headers={ 'Authorization': auth_token })

Config Class
++++++++++++

.. autoclass:: sharepastes.core.Config
    :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

