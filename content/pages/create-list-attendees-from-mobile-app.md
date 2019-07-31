Title: Create a List of Attendees From a Mobile App
Author: Tom Ordonez
Status: hidden
Slug: create-list-attendees-from-mobile-app
Summary: Awesome tutorial to create a list of attendees from a mobile app.

This is an awesome tutorial to create a list of attendees from a mobile app. If you are learning to code or you are a little bit familiar with programming then you will enjoy this.

## What is the mission?

* Go to a mobile app.
* Find a conference.
* Go to attendees.
* Magically extract this list into your computer.
* Optionally, convert the list into CSV.

Why CSV?

Cause CSV stands for `Creative Sourcing Victory` :)

You could go to the app and scroll down. Then scroll down more and keep scrolling down. How do you get a list of names? There is no "export list".

When looking at a lot of data, Creative Sourcing Victory or "CSV" is often the best way to quickly review the data.

There are alternatives for data analysis like Tableau and Python. But most people. Perhaps 99% of them already know Excel.

## What is the challenge?

The mission is getting an attendee list from a mobile app.

How are we actually going to do this? It sounds like mission impossible.

Here are some recommended tools:

* A laptop
* A phone

That's it?

Sort of. Ideally your laptop is a Mac or Linux. Ideally you have some knowledge of the command line. Perhaps some knowledge of Python.

OK...got the feeling a lot of people are dropping out already. But wait. Just keep on reading. Pretend this is just an intake with a hiring manager and you are talking about all sorts of technologies. What do you do? Just take notes, pay attention and ask questions.

For now just read through this. If you don't get it. Just connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a> and ask me anything.

What tools do you really need? (for this tutorial):

* A laptop with Linux or Mac.
* An Iphone.
* The command line.
* Little bit of Python.

## How a mobile app works

We need to start by understanding how a mobile app works.

If you want to get more details search: `mobile app architecture`.

A mobile app has 3 layers:

* Presentation
* Business
* Data

Let's say I build a silly app called "Learn to Add".

The presentation layer shows `1` plus `2` and the Add button.

<p>&nbsp;</p>
![Learn to Add Mobile App]({static}/images/learn-to-add.gif)
<p>&nbsp;</p>

To keep it simple...the business layer is the one that decides that `1+2` is `3`.

And let's pretend that all the addition combinations are stored in a database. As silly as this sounds.

The app sends a request to a remote server. Probably AWS. Connects to the database and finds the row that says `1+2`. And pulls the result `3`.

The result comes into the local data on the app and magically the UI screen changes to show the number `3`.

The most important part to keep in mind in this explanation is that the mobile app sends a request to a server and the server returns a response.

## Capturing traffic from the web to a server

If you go to Google and search for a keyword. The request is sent to a server and a response is returned.

You can review the traffic sent from your computer to Google. For instance you can use Chrome developer tools to see this interaction.

In Chrome go to:

* Menu
* More tools
* Developer tools

<p>&nbsp;</p>
![Developer Tools Chrome]({static}/images/developer-tools-chrome.gif)
<p>&nbsp;</p>

A new window will open. Often by default it shows the `Elements` tab.

To look at the traffic sent from your browser to Google's server. Go to the tab that says `Network`.

<p>&nbsp;</p>
![Developer Tools Chrome Network]({static}/images/chrome-developer-tools-network.jpg)
<p>&nbsp;</p>

I am going to Google for the keyword `juanes` and see what happens.

<p>&nbsp;</p>
![Chrome Network Juanes]({static}/images/chrome-network-juanes.gif)
<p>&nbsp;</p>

The Network tab shows some output:

* Name of the request.
* Status: 200 (an HTTP request code that means "OK. Request fulfilled").
* Type: document, png, font, gif...etc.
* Initiator: A process that initiates a request.

Towards the bottom it says:

* 66 requests.
* 468 KB transferred.
* Load: 1.28s.

I think we can say that the initiator is the `Request` and the `Name` is the response.

I requested a search for `Juanes` and it returned the following:

* Google's logo.
* Font type: roboto.
* A png image with icons.
* Then all sorts of contents (Google results).

Go to any website or web app. Open the developer tools, Network and you can see all the traffic that is being requested and all the responses returned.

## Capturing traffic from mobile to server

Chrome developer tools is awesome right?

A lot of people also use this tool to inspect the HTML and CSS of a page.

You can also inspect the traffic requested and the response returned.

How can we do the same for a mobile app?

There is no such thing as "Developer Mode" for a mobile app.

To capture the traffic between the phone app and the server, we need to put something in the middle.

A laptop.

We need to use the laptop sort of like a bridge between the mobile app and the remote server. And capture the traffic using the laptop.

If you want to get more details search: `man in the middle`.

This is a term mostly used in computer security. Or sometimes you find it as `man in the middle attack`.

Man in the middle is also commonly known as `MITM`.

In this tutorial we are not going to "attack" anyone. We are just going to setup a MITM system to capture the traffic from a mobile app (that you are using) and the remote server.

You wouldn't be able to capture any other traffic other than yours.

## Setting up the laptop

We are going to use the following here:

* The command line aka the Terminal.
* Sublime Text.
* Python

Now we are going to install a software called `mitmproxy`.

We are going to use `sudo` (admin privileges):

    $ sudo dnf install make gcc redhat-rpm-config python3-devel
     python3-pip libffi-devel openssl-devel

    $ sudo pip3 install mitmproxy

Now find your computer local IP number. I am in Linux Fedora so...

    $ ifconfig

Or just go to your Wifi settings. Select your WiFi network and find out the details of your connection. Somewhere in there is your IP number. It often starts with `192.168` or if you have a Comcast router it might start with `10.0`.

Mine says:

    10.0.0.18

Then launch the MITM (man in the middle) program:

    $ mitmproxy

## Setting up the phone

To setup the phone you need 2 things:

* Setup Proxy on the phone.
* Install a security certificate on the phone.

If you want to get more details search: `proxy server`.

By definition a proxy server is used as an intermediary between your client computer and the Internet. It allows your client computer to make indirect network connections to say...a remote server.

In our case the client computer is now the phone and the intermediary (the proxy server) is the laptop.

We are going to tell the phone: Instead of requesting data directly to the Internet. Request data to the laptop. Then the laptop will request data to the Internet.

We need to change the IP settings on the phone.

I have an Iphone so:

* Settings
* WiFi
* Select your WiFi network.
* Scroll down to where it says "HTTP PROXY".
* Server: Enter your computer IP (In my case: `10.0.0.18`).
* Port: `8080`

## More important tech stuff

We need to install a security certificate. 

If you want to get more details search: `CA certificate`.

`CA` stands for `Certificate Authority`. By definition a CA is an entity that issues digital certificates to verify your identity. The digital certificate certifies the ownership of a public key. A CA is a company like Verisign.

Here is a silly comparison to explain the CA certificate.

How do you get a drivers license?

* Go to the DMV.
* Pass the driving course.
* Provide your identification.
* Get your license.

In this case the Certificate Authority is the DMV. And the license is the certificate I am requesting.

To request this certificate I need to generate a key pair that has a Public Key and a Private Key.

That was tough right? Let's take a break by looking at this random cat that has nothing to do with this post...this cat reminds me of David Bowie (Cat People putting out fire).

<p>&nbsp;</p>
![David Bowie cat]({static}/images/david-bowie-cat.jpg)
<p>&nbsp;</p>

When connecting to secure sites on the Internet. The connection between you and the server is encrypted and it uses a digital certificate to verify your identity.

The digital certificate contains the Public Key. This Key is used by others to encrypt and send you data. Then you use your Private Key to decrypt the data.

Similar to buying something online. They know your address (Public Key) and they ship your product in a box. Nobody from the outside can see what the box has. It's "encrypted". The box ends up in your mailbox. You need to use your mail key (Private Key) to open it.

That's a silly example cause the mailman also has a key. But for now just understand that you are the only one with your Private Key.

## Install the CA certificate

Remember a few confusing paragraphs above when I told you that a `CA` is an entity that generates CA certificates?

In our case. The laptop needs to become a CA and generate its own certificates.

The first time that `mitmproxy` is run. The CA (certificate authority) is created in the config directory `~/.mitmproxy`.

As explained in the official docs. The CA is used for on-the-fly generation of dummy certificates for each SSL site that your client visits.

In English this means that your laptop will become a Certificate Authority and it will generate certificates for each secure site that you visit.

Let's just go ahead and set this up...Finally!

* On the phone, open safari.
* Go to `mitm.it`.
* It should open a page that says "Click to install the mitmproxy certificate".
* Tap on the Apple icon.
* It opens the Settings and says "Install profile".
* Tap on Install.
* Enter your phone password.

There is a warning that says:

Root certificate "Installing the certificate mitmproxy will add it to the list of trusted certificates on your Iphone".

Unverified profile "The authenticity of mitmproxy cannot be verified".

Tap on Install Twice.

Now it says "Profile Installed".

Tap on Done.

## Blue Pill or Red Pill

If you are still reading and have no idea how to get to this point. Please send me a message on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.

If everything is set correctly. 

Now go back to the Terminal and there should be output.

<p>&nbsp;</p>
![Mobile traffic output]({static}/images/mobile-traffic-output1.jpg)
<p>&nbsp;</p>

To navigate the output use this:

* Use the arrow keys (up/down) or `J` and `K`.
* Press enter on any item to get more details.
* In inspect mode. Use the keys `H` and `L` to switch tabs.
* Use q to go back to the main list.

## Google Juanes on your phone

Go to your phone and open safari. Go to Google and search for `juanes`. Then look at the Terminal in your laptop to see some action.

Similar to the test we did in Chrome with developer tools. The Terminal will show some results.

Like this one:

It captured the autocomplete as I typed each letter in the keyword `juanes`.

<p>&nbsp;</p>
![Mobile traffic output]({static}/images/safari-juanes-autocomplete.jpg)
<p>&nbsp;</p>

As I keep scrolling down on the terminal I see things like:

* GET...some google URL with a `q=juanes`.
* POST...another google URL.
* GET...a URL with the Google logo.
* URLs for images and the result of the search.

I also see that is sending `GET` and `POST` to Quora.

Weird right?

Now that I see on my phone. I have an old Safari window where I was reading Quora. Why is it sending traffic to Quora when I didn't have that window open?

Now you can really answer "What data is my phone sending?"

## Get a list of attendees from a mobile app

I launched a conference app and searched for a conference. This one is called "Ignite". I looked at the terminal and there was output.

I went to the tab that said "Attendees". Then back to the Terminal:

It has a tab called `Request` and it has some info like:

* Host
* Accept
* Connection
* Cookie

Another tab says `Query` and it has:

* api_version: 3
* client: iphone-event
* device: iPhone7
* email: my email
* event: name of conference

Under `Response` it has:

* Server
* Date
* Content-Type
* and all sorts of data

There is also a big JSON file. It starts with some categories and stats such as:

* All attendees: 300
* Organizers: 20
* Press: 4
* Speakers: 40
* Sponsors: 70

Then it has a list with data such as:

* Name
* Title
* Company
* City
* Picture URL
* and all sorts of awesome data.

If I keep scrolling down I see that this JSON file is pretty big. But how do I get this out?

## Exporting the JSON file

Exporting this file depends on your editor. If you setup Sublime as your default editor on your Terminal. Then the file will open in Sublime and you can celebrate.

Otherwise you need to setup the editor `vim`.

On the mac you can install it like this:

    $ brew install vim

That is if you have the package `homebrew` installed. Otherwise Google: `install homebrew on mac`.

On Linux is really easy. In Ubuntu:

    $ apt install vim

In Linux Fedora:

    $ dnf install vim

Now to set Vim as the default editor in your Terminal. You need to edit a file called `.bashrc`.

Find the file in your home folder using your Terminal.

Add this line:

    export EDITOR='vim'

Save and quit the file. Then run:

    source ~/.bashrc

On the tab where you have the JSON file.

Tap the key letter `E`.

This will open the default text editor of your Terminal.

First it will show this output:

`Edit response (cookies, code, message, header, raw body)?`.

We are interested in `raw` so just tap the letter `r`.

Now there is a giant JSON file which seems to be saved in this location: `/tmp/weirdnumberhere`.

Since the file opened using Vim. You can save this file in another location by typing:

    :w ~/Downloads/attendees_copy.json

Then type `:q` to quit the current file to go back to `mitmproxy`.

Now I am going to open this JSON file with Sublime Text.

<p>&nbsp;</p>
![JSON list attendees]({static}/images/json_list_attendees.gif)
<p>&nbsp;</p>

The JSON file has a lot of attendee information from this conference such as:

* Name
* Title
* Company
* City
* Picture URL
* and more...

## Next steps

This was a complex tutorial. But the results are awesome.

The next step is taking this JSON file and convert it into CSV. We will leave this for another episode.

There are JSON to CSV web conversions. But I don't trust these sites too much. There is no assurance that they won't use your data for their own purpose.

A safer way to convert this data is using Python and is not that hard.

There are other uses for looking at mobile traffic:

* Get a list of anything from a mobile app.
* Review traffic sent and received from a mobile app.
* Reverse engineer an API or build an unofficial API.

The official doc for `mitmproxy` has an interesting tutorial about cheating on a game and submitting the highest score to show up as the winner on a leaderboard.

There is a blog post somewhere about reviewing traffic from Tinder.

You can research data from all sorts of mobile apps.

This is an awesome tool but you should use it to review traffic from your own phone only.


## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.

