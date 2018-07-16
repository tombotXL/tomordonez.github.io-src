Title: Additional Second Hard Drive in Ubuntu
Date: 2017-11-10 18:00
Category: Linux
Tags: linux, ubuntu, hard drive
Slug: additional-second-hard-drive-ubuntu
Author: Tom Ordonez
Status: published
Summary: Tutorial for installing an additional second hard drive in Ubuntu.

Tutorial for installing an additional second hard drive in Ubuntu.

I got a refurbished Thinkpad T430 for very cheap. It came with 250GB SSD but wanted to upgrade it 500GB.

I got a 500GB SSD.

When I got the computer and opened the hard drive panel I noticed that it was empty. I thought that maybe I got scammed.

After much head banging I learned that the hard drive was stored on the RAM panel. I first thought was a mini wireless card. But reading the label it said "256 GB". Uh? I learned it was an "mSATA SSD".

I couldn't fit the new SSD in the hard drive panel cause it was missing the tray.

I installed Ubuntu on the current drive.

Then I got a "Caddy" adapter that replaces the DVD drive with a way to insert another hard drive. That was pretty easy to install.

Now you need to configure the hard drive.

I followed this <a href="https://help.ubuntu.com/community/InstallingANewHardDrive" target="_blank">tutorial</a> from the Ubuntu docs. Although it has a section that is outdated.

## Find the logical name of the new drive

    $ sudo lshw -C disk

This means: `lshw` List hardware. `-C` with Class of type `disk`.

I identified the new disk because it said `product: Crucial`. Which is the brand I got. The size was `525GB`. And it didn't say "partitioned", while the other one said `capabilities: partitioned`.

The logical drive of the new SSD was `/dev/sda`

## Partition the disk using GParted

I started the process using the Terminal instructions. But got confused half way. I closed that and I decided to use the GUI. Then it took 5 seconds.

The tool should be under `Applications/System Tools/Administration`

In my case it wasn't there so I installed it with:

    $ sudo apt install gparted

After installing. I opened the tool and it asked for the root password.

When the program opens. There is a drop down to select the drive you want. I chose the new drive. 

In my case it was `/dev/sda`

## Create a partition table

Go to Device/Create Partition Table

Select `msdos`.

Then I clicked on the green check mark to apply.

## Create a partition

Then I right clicked on the white rectangle that said my drive name.

Selected: New
Chose: Primary Partition.

Filesystem: ext4
Add.

Green check mark to apply.

## Change the label of the drive

When I completed the process I realized that under "Places" my drive was listed as "525 GB blabla". Kind of boring name.

I right clicked on the white rectangle again and hit "Label File System". I entered an awesome name that I could remember.

## Create a mount point

    $ sudo mkdir /media/name_of_new_drive

For the `name_of_new_drive` I used the same name as the "label name".

Now you need to find the `UUID` of the new drive as mentioned <a href="https://help.ubuntu.com/community/UsingUUID" target="_blank">here</a>. UUID means "Universal Unique Identifier".

    $ sudo blkid

It says that `blkid` is used to "locate device attributes".

The result was something like this:

    /dev/sdb1: UUID="bunch of numbers with letters here" TYPE="ext4" PARTUUID="some other number here"
    /dev/sdb5: UUID="another bunch of numbers" TYPE="swap" PARTUUID="other number here"
    /dev/sda1: LABEL="awesome name I chose" UUID="number I need" TYPE="ext4" PARTUUID="number here"

Now you need to edit the file `fstab` like this:

    sudo nano -Bw /etc/fstab

The `-B` is used to create a backup of the file under `/etc/fstab~`.

The `w` is used to disable wrap of long lines.

Then I added this line to the end of the file:

    UUID="number I needed from above" /media/name_of_new_drive ext4 defaults 0 2

For `UUID` above you don't need to put the quotes.

Then quit the file with `Ctrl X`. It will ask if you want to save. Enter Yes.

## Mount all disks

The new disk should be mounted but just in case:

    sudo mount -a

## Restart and Update the BIOS

I restarted and realized that it wouldn't boot. I flipped out. I just enabled the Virtualization settings so I thought that probably I broke something.

I thought if it was booting from the 2nd hard drive and that was it.

Change the BIOS and make sure the sequence order starts with your main drive. Otherwise it won't boot.

## Last observation

Inside the `fstab` I noticed the following on my main SSD:

    errors=remount-ro

Not sure what that is.

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>