Title: Python Socket Save Data To File
Date: 2018-04-06 22:00
Category: Coding
Tags: coding, linux, python, regex
Slug: python-socket-save-data-to-file
Author: Tom Ordonez
Status: published
Summary: Using Python socket to save data to file. Also some Regex, Vim and Linux.

## Setup

* Python3
* Linux Fedora 27

This exercise is based on a lesson on sockets from Coursera.

This can be tested using 3 methods:

* telnet
* Chrome developer tools
* sockets

## Using Telnet

    $ telnet data.pr4e.org 80

The output should be something like:

    Trying 192.241.136.170...
    Connected to data.pr4e.org.
    Escape character is '^]'

Then enter the command:

    GET / HTTP/1.0

The output should be a response:

    HTTP/1.1 200 OK

And then the header of that page:

    Date: Fri, 06 Apr 2018 23:07:21 GMT
    Server: Apache/2.4.7 (Ubuntu)
    Last-Modified: Thu, 12 Nov 2015 19:12:19 GMT
    ETag: "2cf6-5245cb8c635cb"
    Accept-Ranges: bytes
    Content-Length: 11510
    Vary: Accept-Encoding
    Connection: close
    Content-Type: text/html

Then the output is the HTML page.

## Using Chrome developer tools

Open the page `data.pr4e.org`. Go to Developer tools. Network. Reload the page.

Under `Name`. Click on `data.pr4e.org`.

The `Headers` tab shows similar info:

    Request URL: http://data.pr4e.org/
    Request Method: GET
    Status Code: 200 OK
    Remote Address: 192.241.136.170:80
    Content-Length: 625
    Content-Type: text/html;charset=UTF-8
    Date: Fri, 06 Apr 2018 23:18:23 GMT
    Connection: keep-alive

## Using Python socket

    import socket
    import re

    host = input('Enter the host: ')
    port = int(input('Enter the port number: '))
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cmd = 'GET / HTTP/1.0\r\n\r\n'.encode()

    try:
        mysock.connect((host, port))
    except:
        print('Could not connect')

    print('Connected')

    try:
        mysock.send(cmd)
    except:
        print('Could not send data')

    print('Data sent')

    with open('data_stream.txt', 'w') as fhandle:
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            fhandle.write(data.decode())

    mysock.close()

    with open('data_stream.txt', 'r') as fhandle:
        for line in fhandle:
            match = re.match(r'Last-Modified: ([\w,: ]+)', line)
            if match:
                last_modified = match.group()
                print(last_modified)
            match2 = re.match(r'ETag: (["\w-]+)', line)
                etag = match.group()
                print(etag)

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>