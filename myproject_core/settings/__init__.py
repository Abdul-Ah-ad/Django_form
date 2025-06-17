from .base import *

try:
    from .local import *
except ImportError:
    raise ImportError("You need to create a local.py settings file from sample.local.py")
