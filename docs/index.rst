.. SharePastes documentation master file, created by
   sphinx-quickstart on Sun Mar 24 17:33:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SharePastes's documentation!
=======================================

Helps you quickly share code snippets via various services like `Github Gist <http://gist.github.com/>`_ and `PasteBin.com <http://pastebin.com/>`_.


What does SharePastes do?
-------------------------

SharePastes provides you with a simple and minimal command line tool that you can use to quickly share whatever you have copied to your clipboard.

Contents
--------

.. toctree::
   :maxdepth: 2

   extending

Requirements
------------

* Python 2.7 (that's what I have tested it with).
* ``xclip`` command for **Linux** must be installed.
    * ``yum install xclip`` for **Fedora**.
    * ``apt-get install xclip`` for **Ubuntu**.

Installation
------------

``sudo pip install https://github.com/vaidikkp/sharepastes/archive/master.zip``

How to use?
-----------
1. Copy anything to your clipboard.
2. Run the following command:
   ``sharepastes --using <service-name>``

   where ``<service-name>`` is the service that you want to use:
    - ``gist`` for Github's Gist
    - ``pastebin`` for Pastebin.com
3. After successful execution of the above command, you will get link to your
   post in your terminal and the same will be copied to your clipboard as well.
4. Go ahead and share it with whoever you want to. Simply use your Operating
   System's shortcut for pasting to paste the URL.

Creating Shortcuts
------------------

Obviously, you wouldn't want to run that command everytime you want to share something. So the best use of SharePastes is by creating a shortcut for the above command i.e. ``sharepastes --using <service-name>``.

You may create shortcuts in:

1. Linux
    1. GNOME - System Settings > Keyboard > Shortcuts
    2. *If you use anyother desktop experience software and know the way to do
       this, please send a pull request.*
2. Mac OS - See `this link <http://superuser.com/questions/153890/assign-a-shortcut-to-running-a-script-in-os-x/>`_.


**Note:** before using your shortcut for the first time, make sure you use the command from the terminal first because SharePastes needs API keys of the service you intend to post your text to.

Extending SharePastes
---------------------

SharePastes currently supports only Github Gist and Pastebin. But, it can be extended to work with any other similar service that provides an API for the same.

What's next?
------------

1. Perhaps support for more used services.
2. OS notifications using something like PyNotify for Linux and similar for Mac OS and Windows.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

