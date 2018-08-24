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

## Install Dropbox Tray Icon

I am using Fedora and recently followed this tutorial on another machine. I realized that the Dropbox was not on the tray. I wanted to sync only a few files. And without the icon is close to impossible.

    $ dropbox stop

On Chrome. Install <a href="https://extensions.gnome.org/" target="_blank">GNOME shell extensions</a>

If you don't have it installed. When you open this page. There will be a notification towards the top that says:

    To control GNOME Shell extensions using this site you must install
    GNOME Shell integration that consists of two parts:
    browser extension and native host messaging application.
    Click here to install browser extension.

Go to `Click here to install browser extension`.

A popup opens asking `Add GNOME shell integration?`. Hit `Add extension`.

A new notification (warning) message now shows:

    Although GNOME Shell integration extension is running,
    native host connector is not detected.

Install `chrome-gnome-shell`. Applicable to Ubuntu or Fedora. Mine is Fedora:

    $ sudo dnf install chrome-gnome-shell

Install `TopIcons Plus`. Go to chrome and install the <a href="https://extensions.gnome.org/extension/1031/topicons/" target="_blank">TopIcons extension</a>. Then set the switch to `ON`.

Restart dropbox:

    $ dropbox start

## Sync specific folder

Now the Dropbox icon should be on the taskbar.

Go to the Dropbox icon. Preferences. Sync. Selective Sync.

Then choose the folders that you want to sync.