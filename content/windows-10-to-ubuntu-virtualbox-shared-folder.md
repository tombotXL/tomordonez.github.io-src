Title: Windows 10 to Ubuntu VirtualBox Shared Folder
Date: 2017-09-11 18:00
Category: Linux
Tags: windows 10, virtualbox, ubuntu, linux
Slug: windows-10-ubuntu-virtualbox-shared-folder
Author: Tom Ordonez
Status: published
Summary: Follow this process to transfer files from Windows 10 to Ubuntu in VirtualBox.

Follow this process to transfer files from **Windows 10 to Ubuntu in VirtualBox**.

![Windows 10 to Ubuntu VirtualBox Shared Folder]({filename}/images/windows-10-ubuntu-virtualbox-shared-folder.jpg)

This applies when you have Ubuntu installed inside Windows 10. Where Windows is the host and Ubuntu is the guest.

This assumes that you already have Virtualbox installed with Ubuntu.

Follow this process to transfer files from Windows 10 to Ubuntu in VirtualBox.

In Windows 10, open Virtualbox...

## Install Guest Additions

If you haven't installed guest additions...

On the Virtualbox VM (virtual machine). In one of the menu drop downs there is an option that says "guest additions".

When you click on that, it should open a terminal on Linux. Follow the process that is shown there.

When that is completed, shut down the VM.

## Go to Shared Folder

Go to the VM settings. Then shared folders.

* Add Folder
* Use the drop down to lookup a folder (and create one)
* Check: Auto-mount
* OK and OK to update changes

Please note `your-folder-name` since you will need this soon.

Let's say that you call this folder `win10-ubuntu`

Start the VM.

## Go to Ubuntu and review the shared folder

Open a folder and you will see on the left side that a shared folder has been mounted. Following the example above. It would say `sf-win10-ubuntu`.

You won't be able to access the folder using the windows interface, since this directory is own by root.

The location of this folder is: `/media/sf-win10-ubuntu`

You can either use `sudo` to copy files from this directory to your local Linux directory. Such as:

    $sudo cp local-file.txt /media/sf-win10-ubuntu/

If you go back to Windows 10. This file will be on the shared folder you created.

Or you can change the ownership and permissions of this directory:

    $ sudo chown -R youruser:yourgroup /media/sf-win10-ubuntu/

On Linux you usually belong to a group that has the same name as your user.

For example my user is `tom` and my group is `tom`.

I would run the previous command like this:

    $ sudo chown -R tom:tom /media/sf-win10-ubuntu/

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>
