import os, imp

NETID = ""
PASSWORD = ""
DOTFILE = os.path.expanduser("~/.pointcarrefs/local_config.py")

try:
    from local_config import *  # pragma: no flakes
except ImportError:
    NETID = imp.load_source("local_config", DOTFILE).NETID
    PASSWORD = imp.load_source("local_config", DOTFILE).PASSWORD
