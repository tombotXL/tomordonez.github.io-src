Title: USB Stuck in Read Only in Linux
Date: 2018-10-31 23:00
Category: Linux
Tags: linux, usb
Slug: usb-stuck-read-only-linux
Author: Tom Ordonez
Status: published
Summary: Fixing a usb stuck in read only in Linux

Fixing a usb stuck in read only in Linux

![USB Stuck in Read Only in Linux]({static}/images/usb-stuck-read-only-linux.jpg)

As seen <a href="https://askubuntu.com/questions/563764/usb-devices-showing-as-read-only" target="_blank">here</a>.

I have an external drive that I used for backing up some files. I plugged it in again and tried to copy some files but got an error saying that the drive was in "read-only".

This is applicable to Linux.

The solution was doing this:

    $ killall nautilus