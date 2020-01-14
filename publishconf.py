#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.tomordonez.com'
RELATIVE_URLS = False

FEED_ALL_RSS= 'feeds/all.rss.xml'
CATEGORY_FEED_RSS= None

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

DISQUS_SITENAME = "tomordonez-com"
GOOGLE_ANALYTICS = "UA-56050409-28"
