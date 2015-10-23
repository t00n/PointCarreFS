import os, imp

NETID = ""
PASSWORD = ""
DOTFILE = "~/.pointcarrefs/local_config.py"

try:
    from local_config import *  # pragma: no flakes
except ImportError:
    NETID = imp.load_source("local_config.NETID", os.path.expanduser(DOTFILE))
    PASSWORD = imp.load_source("local_config.PASSWORD", os.path.expanduser(DOTFILE))
