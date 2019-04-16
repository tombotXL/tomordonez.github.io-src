# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Ordonez'
SITENAME = u'Tom Ordonez'
SITESUBTITLE = 'Data Science, Machine Learning, Software Engineering'
SITEIMAGE = ''
DESCRIPTION = 'I am Tom Ordonez. I like data science, machine learning, and software development. I use Fedora Linux, Vim, Python, Javascript, C.'

SITEURL = ''
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

PATH = 'content'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# ICONS
ICONS = (
    ('linkedin', 'https://www.linkedin.com/in/tomordonez/'),
    ('twitter', 'https://twitter.com/tomordonez'),
    ('instagram', 'https://www.instagram.com/tomordonez/'),
    ('github', 'https://github.com/tomordonez')
)
    
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/robots.txt',
    'extra/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

DEFAULT_METADATA = {
    'status': 'draft',
    }

# Theme settings
THEME = 'themes/pelican-alchemy/alchemy'
CSS_FILE = 'style.css'

PLUGIN_PATHS = [
    'pelican-plugins',
    ]

PLUGINS = [
    'sitemap',
    'tipue_search'
    ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
