"""
SharePastes

Helps you quickly share code snippets via various services like Github Gist and
PasteBin.com.
"""

from .core import BaseSharePastes
from .core import Config
from .core import SharePastesFactory

extensions = {
    'gist': ('gist', 'Gist'),
    'pastebin': ('pastebin', 'Pastebin'),
}

__author__ = "Vaidik Kapoor <kapoor.vaidik@gmail.com>"
__license__ = "MIT"
__version__ = ".".join(map(str, (0, 2, 0)))
