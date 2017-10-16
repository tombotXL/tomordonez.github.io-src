Title: Installing Ruby on Ubuntu
Date: 2017-09-11 20:00
Category: Coding
Tags: ruby, ubuntu
Slug: installing-ruby-on-ubuntu
Author: Tom Ordonez
Status: published
Summary: Follow this process to install Ruby on Ubuntu Linux

Follow this process to install Ruby on Ubuntu Linux

![Installing Ruby on Ubuntu]({filename}/images/installing-ruby-on-ubuntu.png)

## Installing Ruby on Ubuntu

As seen on <a href="http://rvm.io/" target="_blank">RVM</a>

Go to the terminal in Ubuntu.

Add the public key from RVM

    $ gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
    $ \curl -sSL https://get.rvm.io | bash -s stable

On the Terminal go to the `Menu/Edit/Profile Preferences/Title` and Command.

Check `Run command as a login shell`.

Close the Terminal and start a new one.

    $ type rvm | head -n 1

This should now say `rvm is a function`

Install Ruby. As of this writing the stable version was `2.4.2`

    $ rvm install 2.4.2
    $ rvm use 2.4.2 --default

## Use Gemsets

To work on different projects <a href="http://rvm.io/gemsets/creating" target="_blank">create a Gemset</a>.

    $ rvm use 2.4.2@name-of-project --create

List gemsets with:

    $ rvm gemset list

Switch gemsets with:

    $ rvm gemset use name-of-gemset


## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
