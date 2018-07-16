Title: Install Chromedriver in Linux
Date: 2018-03-27 20:00
Category: Coding
Tags: coding, linux, chromedriver, python
Slug: install-chromedriver-linux
Author: Tom Ordonez
Status: published
Summary: A short step by step on installing Chromedriver in Linux

This is a short tutorial to **install Chromedriver in Linux**.

Based on this <a href="https://gist.github.com/natritmeyer/6522446" target="_blank">git</a> about installing Chromedriver in Linux Fedora. And setting up the correct file location in your Python scripts.

This is the directory where to **<a href="https://sites.google.com/a/chromium.org/chromedriver/downloads" target="_blank">download Chromedriver</a>**.

    $ wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
    $ unzip chromedriver_linux64_2.3.zip
    $ sudo cp chromedriver /usr/bin/chromedriver
    $ sudo chown root /usr/bin/chromedriver
    $ sudo chmod +x /usr/bin/chromedriver
    $ sudo chmod 755 /usr/bin/chromedriver

Then setup Chromedriver using the right location.

    driver = webdriver.Chrome('/usr/bin/chromedriver')

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>