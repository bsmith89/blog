#!/usr/bin/env python3
# This file is only used if you use `make publish_ghp` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

# Override SITEURL
SITEURL = "http://bsmith89.github.io/blog"

LINKS = LINKS + [('(The real site)', 'http://blog.byronjsmith.com')]
