Title: Pelican Python Search Tutorial
Date: 2018-02-11 23:00
Category: Coding
Tags: python, pelican, static search
Slug: pelican-python-search-tutorial
Author: Tom Ordonez
Status: published
Summary: In this Python tutorial, I will show you how to install a search box on Pelican Python. A static site generator in Python.

In this Python tutorial, I will show you how to install a search box on Pelican Python. A static site generator in Python.

This article is based on <a href="http://mygeekdaddy.net/2014/11/17/adding-local-search-to-pelican/" target="_blank">this</a> blog post and <a href="http://www.tipue.com/search/docs/?d=1" target="_blank">this</a> one.

Pelican is a static site generator in Python. It doesn't have the typical search engine of a CMS like Wordpress. You could install a Google search engine but it might look weird.

## Tipue Search, a site search jQuery plugin

For those not familiar with jQuery. This is a Javascript library, basically used to manipulate DOM elements and handle events.

Here is a step by step on how to install Tipue Search for a Pelican Python website.

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>

## Download Tipue Search and jQuery

For Tipue Search you need to install 2 things:

* Let's call it "the main module"
* and the Pelican plugin

This is the link for the main module:

<a href="https://github.com/Tipue/Tipue-Search/tree/master/tipuesearch" target="_blank">https://github.com/Tipue/Tipue-Search/tree/master/tipuesearch</a>

This is the link for the Pelican plugin:

<a href="https://github.com/getpelican/pelican-plugins/tree/master/tipue_search" target="_blank">https://github.com/getpelican/pelican-plugins/tree/master/tipue_search</a>

To download these files you can use this awesome site called <a href="https://minhaskamal.github.io/DownGit/#/home" target="_blank">DownGit</a>.

Just enter the URL into the search box and hit Download.

This will create a zip file. Extract the contents and they will have these names:

* Main module: `tipuesearch`
* Pelican plugin: `tipue_search`.

Now download `jQuery`:

<a href="https://jquery.com/" target="_blank">https://jquery.com/</a>.

## How Tipue Search works

It creates a JSON file and uses jQuery to load the content into search results.

To create the JSON file you need to install `BeautifulSoup`.

    $ pip install beautifulsoup4

If that doesn't work. Try it with `sudo`.

If it's already installed, it might say:

    Requirement already satisfied: beautifulsoup4 in /usr/lib/python...

You can also test this way. Go to the Python shell:

    $ python
    >>> from bs4 import BeautifulSoup

After you configure a few things. When you generate the site. It will create a JSON file with all your blog posts.

## Placing the Tipue Search "main module"

After you download the directory `tipuesearch`.

You need to move it into your `themes` directory. Under `static`.

It should be at the same level as `css` and `fonts`.

If you open the `tipuesearch` directory, it should have these contents:

    css (this is a directory)
    search.png
    tipuesearch_content.js
    tipuesearch.js
    tipuesearch.min.js
    tipuesearch_set.js

Inside the `css` directory. You will find these files:

    normalize.css
    tipuesearch.css

## Placing the Tipue Search "pelican plugin"

After downloading, this directory should be called `tipue_search`.

You need to move it to your `plugins` directory.

## Placing the jQuery file

Inside your themes directory. Under `static`.

Create a directory called `js` if you don't have one.

Then place the jQuery file inside this directory.

## Updating pelicanconf.py

Add `DIRECT_TEMPLATES` if you don't have one:

    DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

Add the pelican plugin name `tipue_search`. For instance mine looks like this:

    PLUGINS = [
    'sitemap',
    'tipue_search'
    ]

## Review your THEME path

It's easy to get confused with the paths. I got confused too.

My config file has this:

    THEME = 'themes/pelican-alchemy/alchemy'

I am using a theme called `alchemy`.

My directory looks like this:

    themes/pelican-alchemy/alchemy/

Then I have these 2:

    static/
    templates/

Inside `static` I have:

    css
    fonts
    js
    tipuesearch

## Adding JS and CSS to the `base.html` template

This file should be under `templates`.

Add all these lines to the `head` before it closes.

This one makes the browser render elements more consistently:

    <link rel="stylesheet" href="{{ SITEURL }}/theme/tipuesearch/css/normalize.css">

This one loads `jQuery`:

    <script type="text/javascript" src="{{ SITEURL }}/theme/js/jquery-3.3.1.min.js"></script>

These ones load the search results:

    <script type="text/javascript" src="{{ SITEURL }}/theme/tipuesearch/tipuesearch_content.js"></script>
    <link rel="stylesheet" href="{{ SITEURL }}/theme/tipuesearch/css/tipuesearch.css">
    <script type="text/javascript" src="{{ SITEURL }}/theme/tipuesearch/tipuesearch_set.js"></script>
    <script type="text/javascript" src="{{ SITEURL }}/theme/tipuesearch/tipuesearch.min.js"></script>

## Adding a Search box to your menu

I have a search box right under my menu.

Inside the same `base.html` file. In the `body header` before it closes:

    <form action="{{ SITEURL }}/search.html" onsubmit="return validateForm(this.elements['q'].value);">
      <input id="tipue_search_input" type="text" name="q" placeholder="Search">
    </form>

It doesn't have a `Search` button. But you can add one if you want the "geocities" look :)

## Create the `search.html` template

This code is basically the same as <a href="http://mygeekdaddy.net/2014/11/17/adding-local-search-to-pelican/" target="_blank">this</a> source.

But I left only the `jQuery` code:

    {% extends "base.html" %}
    {% block title %}{{ SITENAME }} Search {% endblock %}
    {% block content %}

    <div class="entry-content">
	<script>
		$(document).ready(function() {
			$('#tipue_search_input').tipuesearch({
				'show': 8,
				'mode': 'json',
				'contentLocation': '{{ SITEURL }}/tipuesearch_content.json'
			});
		});
    </script>
    <div id="tipue_search_content">
    	<div id="tipue_search_loading"></div>
    </div>
    </div>
    {% endblock %}

## Test the Search

So far you should have done this:

* Downloaded and placed the "main module" `tipuesearch` under your `themes` path. Inside the `static` directory.
* Downloaded and placed the plugin `tipue_search` inside your plugins directory.
* Downloaded and placed `jQuery` inside your `themes/.../static/js` directory.
* Installed `BeautifulSoup`.
* Updated your `pelicanconf.py` config file.
* Added the `JS` and `CSS` to your `base.html` template.
* Created a search box inside `base.html`.
* Created a `search.html` template.

Now you can regenerate the site and open `localhost`.

    $ make html && make serve

## Troubleshooting the Search

In `locahost` in Chrome. Open the dev tools. (Right click/Inspect)

Go to `Sources`.

In the directory tree. It should have loaded the `theme` directory:

    css
    fonts
    js
    tipuesearch

The `jQuery` should show up inside the `js` directory.

Go to `Network`.

Try the search box.

Under the `Network` tab, you can view the files that were loaded.

Under `JS`. It should have loaded the `jQuery` file and the Tipue Search files.

## Content Delivery Network delays

If you are using a CDN like CloudFlare. You either have to wait a while for the changes to show up or you have to clear the cache on the CDN.

This situation could happen.

Maybe you decide not to download `jQuery` but instead load the library from the web.

If you make a change such as updating this library and you push to your server. You might still see the old version and you will go crazy trying to troubleshoot this.

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>