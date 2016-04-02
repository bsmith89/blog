#!/usr/bin/env python3
# This file is only used if you use `make publish_ghp` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

# Override some variables
SITEURL = "http://bsmith89.github.io/blog"

# GOOGLE_ANALYTICS = "UA-40659359-3"

LINKS += [('(The real site)', 'http://blog.byronjsmith.com')]
