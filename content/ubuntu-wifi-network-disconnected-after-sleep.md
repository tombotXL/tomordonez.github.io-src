Title: Ubuntu Wifi Network Disconnected After Sleep
Date: 2017-09-07 18:00
Category: Linux
Tags: ubuntu, linux, wifi
Slug: ubuntu-wifi-network-disconnected-after-sleep
Author: Tom Ordonez
Status: published
Summary: Ubuntu Wifi disconnected after sleep. This is how I fixed this problem.

Ubuntu Wifi disconnected after sleep. This is how I fixed this problem.

![Ubuntu Wifi Network Disconnected After Sleep]({filename}/images/ubuntu-wifi-network-disconnected-after-sleep.jpg)

I got a Thinkpad and I thought I switched off the Wifi. The right side of the laptop has a switch to turn the Wifi on and off.

That didn't work.

I went to the settings and I disabled/enabled the Wifi.

That didn't work.

I saw a great solution <a href="http://askubuntu.com/questions/761180/wifi-doesnt-work-after-suspend-after-16-04-upgrade" target="_blank">here</a>.

## Assemble the minions

Open the terminal and run this:

    sudo systemctl restart network-manager.service

Let this witchcraft take effect.

Happiness unlocked.

If that didn't work. You can try one of these solutions:

Check if this file has the setting `managed` to false

    $ cat /etc/NetworkManager/NetworkManager.conf

The output could be:

    [main]
    plugins=ifupdown,keyfile,ofono
    dns=dnsmasq

    [ifupdown]
    managed=false

Set `managed` to `true`

    $ sudo vim /etc/NetworkManager/NetworkManager.conf

Edit:

    managed=true

Then run:

    sudo service network-manager restart

## Other solution

Follow this <a href="https://ubuntuforums.org/showthread.php?t=1592020" target="_blank">thread</a> for another solution.

This thread describes the problem when trying to connect to wifi, it would ask for the password over and over again.

It also describes the problem when trying to connect to wifi via an ad-hoc network.

The thread goes into several infinite rabbit holes. If you have a definite solution please add a comment below.

## Ubuntu official documentation

This is the official documentation about <a href="https://help.ubuntu.com/stable/ubuntu-help/net-wireless-disconnecting.html" target="_blank">Ubuntu</a> - wireless network disconnecting.

It shows 4 basic "solutions". Although I would call them more: riddles for you to figure it out:

* Weak wireless signal
* Network connection not being established properly
* Unreliable wireless drivers
* Busy wireless networks

Not great solutions but I would say: information to think about why your Ubuntu wireless network keeps disconnecting.

There is also the <a href="https://help.ubuntu.com/stable/ubuntu-help/net-wireless-troubleshooting.html" target="_blank">Ubuntu wireless network troubleshooter</a>.

And the official documentation to <a href="https://help.ubuntu.com/stable/ubuntu-help/net-wireless-connect.html" target="_blank">connect to a wireless network in Ubuntu</a>.


