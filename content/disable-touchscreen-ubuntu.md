Title: Disable Touchscreen on Ubuntu
Date: 2017-09-05 18:00
Category: Linux
Tags: ubuntu, linux, touchscreen
Slug: disable-touchscreen-ubuntu
Author: Tom Ordonez
Status: published
Summary: Follow this process to disable touchscreen on Ubuntu.

Follow this process to **disable touchscreen on Ubuntu**.

![Disable Touchscreen on Ubuntu]({filename}/images/disable-touchscreen-ubuntu.jpg)

Go to the terminal and type `man xinput`

It says that `xinput` is a utility to configure and test X input devices.

It has a lot of options but the one we are interested in is `list`

Then do this:

    xinput --list

It will show you something like this:

    Virtual core pointer                            id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ SynPS/2 Synaptics TouchPad                id=13   [slave  pointer  (2)]
    ⎜   ↳ Raydium Corporation Raydium Touch System  id=15   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                         id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Video Bus                                 id=7    [slave  keyboard (3)]
        ↳ Video Bus                                 id=8    [slave  keyboard (3)]
        ↳ Sleep Button                              id=9    [slave  keyboard (3)]
        ↳ Integrated Camera                         id=11   [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=12   [slave  keyboard (3)]

Find the touchscreen system id and disable it.

I initially got confused between choosing Touchpad and Touch System.

I looked up Raydium Corporation and indeed they do touch screens.

In my case the `id` is `15`

So I did this:

    xinput disable 15

If you feel like you made a mistake and cannot live without the touchscreen then just do the opposite:

    xinput enable 15

Using obviously the `id` that corresponds to your config.

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>