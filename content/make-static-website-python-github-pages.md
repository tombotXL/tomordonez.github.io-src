Title: Make a Static Website with Python and Github Pages
Date: 2019-04-18 20:00
Category: Linux
Tags: coding, static website, python, github pages
Slug: make-static-website-python-github-pages
Author: Tom Ordonez
Status: published
Summary: A tutorial to make a static website using Python and Github Pages. It uses the Pelican static website generator and Cloudflare.

Follow this tutorial to **make a static website** with Python and Github Pages. It uses the Pelican static website generator. Hosted with Github pages using Cloudflare DNS and CDN.

I followed this procedure to setup the blog using Python and Pelican.
https://fedoramagazine.org/make-github-pages-blog-with-pelican/

## Create accounts

Make sure you have accounts at Github and Cloudflare.

## Creating repos on Github

You need to create 2 repos for your source files and your output files. The source files can be written in `Markdown`. Then you use a command to convert these source files into output `HTML` files.

For source files:

    youruser.github.io-src

For output files:

    youruser.github.io

## Setup virtualenv

    pip install virtualenv

Test your installation with:

    virtualenv --version

Create a directory such as:

    mkdir blog

    cd blog

Create the environment with:

    virtualenv env

Activate it with:

    source env/bin/activate

The prompt will change to:

    env $

Follow the steps to install packages. If you want to leave the environment deactivate it with:

    deactivate

## Install Pelican

Inside the environment, install Pelican:

    env $ pip install pelican
    env $ pip install Markdown
    env $ pip install typogrify

Setup the source repo

    env $ git clone https://github.com/youruser/youruser.github.io-src.git ghpages

    env $ cd ghpages

Setup the output repo

    env $ git submodule add https://github.com/youruser/youruser.github.io.git output

Run the Pelican setup:

    env $ pelican-quickstart

## Caching your Github user and password

Later on when we are ready to publish to Github. When you `git push`. It will ask for your Github user and password.

Everytime that you push it will ask for your credentials. Which can be annoying if you want to push a few times within a short period.

You can cache your Github credentials using the following setup.

Inside the Pelican root directory make sure you are on the right repo:

    env $ git remote -v

This should give you the `.io-src.git` repo.

    env $ git config --global credential.helper 'cache --timeout=3600'

This will cache your credentials for 1 hour.

Now do the same for the output repo.

    env $ cd output

    env $ git config --global credential.helper 'cache --timeout=3600'

    env $ cd ..

## Pelican Setup

Answer the questions like this:

* Where to create the new site: Click Enter
* URL: https://youruser.github.io
* Generate Makefile: Yes
* Autoreload & simpleHTTP: Yes
* Upload mechanism: Select No for all except for Github, select Yes.
* Is this your personal page: Yes

According to this tutorial:
https://fedoramagazine.org/make-github-pages-blog-with-pelican/

If you get an error saying that the output directory already exists, that this is fine.

## Development and Production

There are config files.

The development config file is called `pelicanconf.py`.

The production config file is called `publishconf.py`.

## Update publishconf.py file

Open the file `publishconf.py` using your favorite editor, such as `vim`.

    env $ vim publishconf.py

Add or edit this line so it's set to `False`

	DELETE_OUTPUT_DIRECTORY = False

## Update pelicanconf.py file:

Open the file `pelicanconf.py`.

    env $ vim pelicanconf.py

The default file usually looks like this:

	# -*- coding: utf-8 -*- #
	from __future__ import unicode_literals

	AUTHOR = u'Your Name'
	SITENAME = u'Your Site Title'
	SITEURL = ''

	PATH = 'content'

	TIMEZONE = 'America/New_York'

	DEFAULT_LANG = u'en'

	# Feed generation is usually not desired when developing
	FEED_ALL_ATOM = None
	CATEGORY_FEED_ATOM = None
	TRANSLATION_FEED_ATOM = None
	AUTHOR_FEED_ATOM = None
	AUTHOR_FEED_RSS = None

	# Blogroll
	LINKS = (('Pelican', 'http://getpelican.com/'),
	         ('Python.org', 'http://python.org/'),
	         ('Jinja2', 'http://jinja.pocoo.org/'),
	         ('You can modify those links in your config file', '#'),)

	# Social widget
	SOCIAL = (('You can add links in your config file', '#'),
	          ('Another social link', '#'),)

	# Uncomment following line if you want document-relative URLs when developing
	#RELATIVE_URLS = True

## Create structure of the blog

By default Pelican is setup as a blog, where the home page shows a list of blog posts with their summary.

To setup content of type `Pages`. Create a directory inside `content` such as:

    env $ mkdir content/pages

To setup images that you can use for `Posts` or `Pages`. Create a directory inside `content` such as:

    env $ mkdir content/images

If you will use a custom domain. Create another directory like this:

    env $ mkdir content/extra

To setup pagination. Edit `pelicanconf.py` and add this line:

    DEFAULT_PAGINATION = 5

To create the path to `images` and to `CNAME` add these lines to `pelicanconf.py`:

    STATIC_PATHS = ['images', 'extra/CNAME']
    EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

## Create a CNAME file

If you have a custom domain, you need to create a CNAME file

    env $ vim content/extra/CNAME

Add your domain such as:

    www.yourdomain.com

## Create a blog post

To create a workflow from draft to published you need to edit `pelicanconf.py`:

    DEFAULT_METADATA = { 'status': 'draft', }

Create the blog posts inside `content` using markdown such as:

    env $ vim content/awesome-blog-post.md

Then use this format:

    Title: Awesome Blog Post Title
    Date: 2017-01-01 15:00
    Category: Awesome category
    Tags: tag1, tag2, tag3
    Slug: awesome-blog-post
    Author: Homer Simpson
    Status: draft
    Summary: Summary of this awesome blog post. This will be the SEO description

    Start your awesome blog post here. Blabla
    blabla
    etc...

## Build the html and run the server

Save the blog post and run this:

    env $ make html && make serve

Open the browser in `localhost:8000`.

Since you set the status of the blog post to `draft`. You won't see it on the home page. You would have to open it at the slug location such as:

    localhost:8000/awesome-blog-post

To stop the server use `Ctrl+C`.

The draft to published workflow works well if you want others to review your content without having these posts appear on the home page. Otherwise just set the `Status` to `published`.

## Create a page

You can create static pages such as the typical `about` page.

This type of content has to go inside the `content/pages` directory.

    env $ vim content/pages/about.md

Then follow a similar markdown format and status.

    Title: About
    Author: Your name
    Status: published
    Summary: awesome summary

    Start writing your awesome page here.

## Markdown crash course

Use this notation for hyperlinks:

    [square bracket for text](parenthesis for URL)

If you want to open the hyperlink in a new tab/window. This cannot be done with markdown. Instead you have the follow the html format:

    <a href="awesome-url" target="_blank">Awesome text</a>

Use this notation to add images:

    ![exclamation point and bracket for text]({filename}/images/image-file.jpg)

On the notation above you literally have to put `{filename}`. Then the location of the image, which can be `jpg` or `png`.

Formatting code, use:

    4 leading spaces or `backticks` for inline.

For headlines use `#` hashtags. For an `h2` headline use `##` 2 hashtags.

For bullet points use `*` stars for `ul` or numbers for `ol`.

## Adding a theme

To see the location of default themes:

    pelican-themes -lv

This might change depending on your setup but in my case I got this:

    /usr/lib/python2.7/site-packages/pelican/themes/notmyidea
    /usr/lib/python2.7/site-packages/pelican/themes/simple

To get more themes go to this <a href="http://pelicanthemes.com/" target="_blank">Pelican themes</a> site.

Go to the repo for the one you like.

Git clone the repo. For example:

    env $ (cd ~/Downloads/ && git clone https://awesome-repo)

Let's say that the theme is called `homer`. The location will be `~/Downloads/homer/`.

Install the theme using this:

    env $  pelican-themes --install ~/Downloads/homer/ --verbose

What this will do is just copy the whole directory into your virtualenv:

    ~/.../env/lib/python2.7/site-packages/pelican/themes/homer

Now you have to add something to the `pelicanconf.py` config file:

    THEME = 'homer'

Depending on the theme there might be a requirement to specify the css file. In which case you would need to add something like this:

    COLOR_SCHEME_CSS = 'awesome.css'

## Deploy to Github

Edit your `.gitignore` file and add this line:

    *.pyc

Use this to generate the site:

    env $ make publish

This will generate the site using the production settings. Which is the `publishconf.py` file.

This will also run the development config file because this file has this line:

    from pelicanconf import *

Deploying to Github requires to `git push` both repos. The source and the output.

Deploy the output.

    env $ cd output

    env $ git add .

    env $ git commit -m "Describe your commit here"

    env $ git push -u origin master

This will ask for your Github credentials. They will be cached for 1 hour.

Now deploy the source.

    env $ cd ..

    env $ git add .

    env $ git commit -m "Describe your commit here"

    env $ git push -u origin master

Browse to you blog:

    https://youruser.github.io

## Custom Domain

This requires to make some changes to Github, your DNS provider and Cloudflare

## Change the DNS settings

Create these records:

    Type    Name               Content
    ALIAS   yoursite.com       youruser.github.io
    CNAME   www.yoursite.com   youruser.github.io
    TXT     yoursite.com       youruser.github.io

Change your DNS name server to the Cloudflare ones:

    aria.ns.cloudflare.com
    jay.ns.cloudflare.com

## Change the Github settings

Go to your output repo `github.io`.

Go to `Settings`.

Under `Custom domain` enter: www.yoursite.com

Save.

## Change the Cloudflare settings

Add A records as seen here:

https://help.github.com/articles/setting-up-an-apex-domain/

Verify with Google webmaster tools.

* Add property
* Add TXT google verification code


Thanks to <a href="https://www.jonathan-petitcolas.com/2017/01/13/using-https-with-custom-domain-name-on-github-pages.html" target="_blank">this awesome post</a>. This is how you setup Cloudflare.

Setup these Page rules.

    https://www.yoursite.com/*
    Cache Level: Cache Everything

    https://yoursite.com/*
    Forwarding URL: (Status Code: 301 - Permanent Redirect, URl: https://www.yoursite.com$1)

    http://www.yoursite.com/*
    Always Use HTTPS

In your Overview dashboard make sure you have these settings (if you are on the free plan)

* Security level: medium
* SSL: Full
* Caching level: Standard

## Change the Pelican production config file

Inside `publishconf.py` change this setting from:

    SITEURL = 'https://youruser.github.io'

to:

    SITEURL = 'https://www.yoursite.com'

## Push Custom domain changes to Github

Deploy the output.

    env $ make html && make publish

    env $ cd output

    env $ git add .

    env $ git commit -m "Custom domain update"

    env $ git push -u origin master

This might ask for your Github credentials. Unless they were cached.

Now deploy the source.

    env $ cd ..

    env $ git add .

    env $ git commit -m "Custom domain update"

    env $ git push -u origin master

## Setup SEO

Create a `robots.txt` file.

Create a `favicon.ico` file.

Create a `sitemap.xml` file.

But first follow this. These files will be created later.

Modify your `pelicanconf.py` file so it looks like this:

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

	### Plugins

	PLUGIN_PATHS = [
	        'pelican-plugins'
	          ]

	PLUGINS = [
	          'sitemap', 
	          ]

	# Sitemap
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

Go to your Pelican root directory and create the `robots.txt` file

    env $ vim content/extra/robots.txt

Add this line to the file:

    User-agent: *

Go to the directory `content/extra/` and add a `favicon.ico` image.

Create a directory for the plugins in the Pelican root directory:

    env $ mkdir pelican-plugins

Create a directory for the sitemap plugin:

    env $ mkdir pelican-plugins/sitemap

As seen on the <a href="https://github.com/getpelican/pelican-plugins/tree/master/sitemap" target="_blank">Sitemap page</a>. Copy the 3 files from this repo into the `pelican-plugins/sitemap` directory.

The directory should contain these files:

    Readme.rst
    __init__.py
    sitemap.py

Generate the site:

    env $ make publish

Verify that the `sitemap.xml` was generated inside the `output` directory.

Deploy the output.

    env $ cd output

    env $ git add .

    env $ git commit -m "sitemap, robots, favicon"

    env $ git push -u origin master

This might ask for your Github credentials. Unless they were cached.

Now deploy the source.

    env $ cd ..

    env $ git add .

    env $ git commit -m "sitemap, robots, favicon"

    env $ git push -u origin master
