Title: Reverse Whois To Find Contact Information
Author: Tom Ordonez
Status: hidden
Slug: reverse-whois-find-contact-information
Summary: Using reverse whois to find contact information...for research purposes :)

Using reverse whois to find contact information...for research purposes :)

<p>&nbsp;</p>
![Reverse Whois To Find Contact Information]({filename}/images/reverse-whois-find-contact-information.jpg)
<p>&nbsp;</p>

One day...I ran out of the free credits from Lusha.

I really wanted that email.

I know it's a gmail.

I did a quick search online but couldn't find it.

Now what?

Send an Inmail?

I am not a fan of those. I prefer to send an email.

## Reverse whois to the rescue

To use reverse whois in a programmatic way. You could use a Python script.

If you are a little bit familiar with Python. It's really easy to setup the script with just a few commands:

    $ git clone https://github.com/joekir/rwhois.git
    $ cd rwhois/
    $ virtualenv -p /usr/bin/python env
    $ source env/bin/activate
    $ python setup.py install
    $ pip install requests

Then you can use the script like this:

    $ python rwhois.py --t "Jack Dorsey"

The output for this example looks like this:

<p>&nbsp;</p>
![Reverse Whois Jack Dorsey]({filename}/images/reverse-whois-jack-dorsey.jpg)
<p>&nbsp;</p>

Then you can `whois` one of the results:

    $ whois tesse.xyz

Warning: I am not sure if this is the real Jack Dorsey. Proceed at your own risk :)

If you are not feeling the Neo or Trinity in you...

You can just:

Google "reverse whois" to find a few tools that allow you to enter person's name and in return it will give you domains registered under that name.

In another example (missing screenshots) I entered a first and last name and the result was a few domains that end with `.mx` which is the top level domain for Mexico.

I am sure this person is not in Mexico. Or why would he buy domains with that top level domain? Very unlikely.

In the results there was also a domain that ended with `.us`.

Guess what...

This type of level domain doesn't allow secure private domain name registration.

This is when you `whois` a domain and it shows up as `private registration` and it doesn't show any contact info.

These are the restrictions for `.us` domains:

* Any US citizen or resident
* Any US org or corp

I think I am on the right track.

## Whois the domain

I don't use a website to do `whois` but instead I use my own computer terminal.

    $ whois awesomdomainfound.us


The result of a `whois` for a `.us` top level domain will always contain the registration name.

In this case I found the contact info for that person.

<p>&nbsp;</p>
![Reverse Whois OMG]({filename}/images/reverse-whois-omg.gif)
<p>&nbsp;</p>

## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.