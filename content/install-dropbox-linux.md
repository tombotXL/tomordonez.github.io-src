Title: Installing Dropbox on Linux
Date: 2017-12-01 18:00
Category: Linux
Tags: dropbox, linux
Slug: installing-dropbox-linux
Author: Tom Ordonez
Status: published
Summary: Short tutorial for installing Dropbox on Linux

Follow this short tutorial for installing Dropbox on Linux

![Installing Dropbox on Linux]({filename}/images/installing-dropbox-linux.gif)

Go <a href="https://www.dropbox.com/install-linux" target="_blank">here</a> and choose an installer.

There are 3 options:

* Ubuntu
* Fedora
* Compile from source

## Too Many Dropbox Directories

If you have too many directories. More than 10,000. Dropbox will stop running.

Stop dropbox:

    $ dropbox stop

Run this:

    $ echo fs.inotify.max_user_watches=100000 | sudo tee -a /etc/sysctl.conf; sudo sysctl -p

Restart Dropbox:

    $ dropbox start

## Questions about Dropbox on Linux? Comment below
