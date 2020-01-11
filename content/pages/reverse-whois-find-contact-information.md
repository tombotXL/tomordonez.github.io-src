Title: Reverse Whois To Find Contact Information
Author: Tom Ordonez
Status: hidden
Slug: reverse-whois-find-contact-information
Summary: Using reverse whois to find contact information...for research purposes :)

Using reverse whois to find contact information...for research purposes :)

<p>&nbsp;</p>
![Reverse Whois To Find Contact Information]({static}/images/reverse-whois-find-contact-information.jpg)
<p>&nbsp;</p>

One day...I ran out of the free credits from Lusha.

I really wanted that email.

I know it's a gmail.

I did a quick search online but couldn't find it.

Now what?

Send an Inmail?

I am not a fan of those. I prefer to send an email.

## Who is Whois?

Whois is a "query and response protocol".

In English it means that it's a way to talk to a server to ask questions and get answers.

With `Whois` you can ask a database about a domain name and who registered that domain.

If you are curious how `Whois` actually works here are more details in layman terms.

Guess who invented `Whois`...

DARPA.

If you are a fan of the X-Files probably you know what DARPA is. They pretty much invented these:

* The Internet
* Drones
* Google Maps
* Siri
* Unix
* GPS

I might be wrong. You never know with DARPA. Probably I am being added to "a list" everytime I write the word DARPA.

Back in the days there was only one organization handling all domain registrations...Who? drum roll...DARPA.

This part is important:

There was only one server. Just like in Highlander. There can be only one.

DARPA comes up with a way to talk to that server to find out who registered a domain.

Bam! WHOIS is born.

They were also working on DARPANET which became what we call now "The Internet".

One day the NSF (aka National Science Foundation) said that domain registrations should be handled by commercial and third party organizations.

Check this out. This part is important too:

Let me translate Wikipedia for you. It says that later on you were able to search on these commercial servers using wild-card searches.

If you are familiar with a `wild-card`. This is often use to search all records in a database.

For instance a search such as:

    *con

In a database of conference names, would show all results that end with `con`:

* Sourcecon
* Pycon
* Beercon
* Bacon

It also says that a WHOIS query of someone's last name would result in all records with that name.

This is very important for what I will show you later on.

Read that again:

You can lookup someone's name and the result would be the domain registered by that someone.

Here is more...

A query with a keyword will result in all registered domains with that keyword.

A query for an admin contact will result in all domains that this admin is associated with.

As more registrars and commercial companies started to get involved then such open queries were no longer available.

## Who is ICANN

One day the management of top level domains (aka TLDs) was assigned to ICANN:

* .com
* .net
* .org

ICANN stands for "Internet Corporation for Assigned Names and Numbers". A non profit responsible for managing procedures of databases related to namespaces of the Internet.

To put it simple. ICANN tells you what you can or cannot do with those top level domains.

Until recently (10 years ago) more top level domains started to come out of nowhere.

* .co
* .us
* .biz
* .mx
* .uk

There are around 1,500 TLDs nowadays. And this list is maintained by a department of ICANN called IANA (Internet Assigned Numbers Authority)

## How to do a WHOIS

WHOIS is often used on the Terminal. The prompt on Windows or the Terminal on Mac/Linux.

Why would you use the Terminal? That's what they had back then. This was way before Windows or what you know as a GUI (graphical user interface)

Do you remember the movie Independence Day?

How did we kick out the aliens?

Using morse code.

Point is the Terminal is important. And it's (sort of) easy to learn.

On a terminal you would use WHOIS like this:

    $ whois sourcecon.com

Which in this case you won't get much info cause of domain privacy, which I will explain soon.

## Whois on Terminal or Web

Using WHOIS requires a WHOIS client.

If you are using Linux for the first time. For instance Fedora and you type `whois` it will tell you that this program is not installed and if you want to install it.

By default `whois` is not installed on the Terminal.

You can also use Whois using the web. If you google "whois". You will get a lot of results for a web-bases WHOIS client. And it will do the same as the Terminal.

Although some websites will be annoying with ads and popups or they would ask you sign up or enter a captcha.

For me. I just want to get to the data without all the hoops so I just use the Terminal.

## What is Domain Privacy

Probably you figured...

OMG I can find who registered any domain? All those contacts. OMG!

If you are not in the business of spam and you follow good online citizen behavior then you would lookup some domains here and there and move on with your life.

But some people like to spam. Either in recruiting or not.

Domain privacy is a service you can buy when registering a domain. Or buy it now even if you had that domain for a while.

My recommendation is that if you have a domain you should buy domain privacy.

## TLDs and Domain Privacy

It turns out that domain privacy is different for all sorts of TLDs (top level domains).

For instance `.ca`. Which is the TLD for Canada. The Canadian authority no longer posts registration details. But some data still comes out.

    $ whois 500canada.ca

This is the domain for 500 Startups Canada.

    Domain name:           500canada.ca
    Domain status:         registered
    Creation date:         2016/03/10
    Expiry date:           2026/03/10
    Updated date:          2017/04/25
    DNSSEC:                Unsigned
    
    Registrar:
    Name:              Tucows.com Co.
    Number:            156
    
    Name servers:
    ns1.mdnsservice.com
    ns2.mdnsservice.com
    ns3.mdnsservice.com

Creation date, expiration date, updated date. This is useful information. But right now it doesn't help us much because it doesn't show contact info.

For `.uk`. They provide some domain privacy but some info is open. For example:

    $ whois startups.co.uk

It doesn't show contact info but it shows this info:

    Registrant:
    Marketing VF

    Registrant's address:
    Imperial Works
    London
    NW5 3ED
    United Kingdom

For `.us` privacy is forbidden. Yep you read that right. Same case for `.in`.

Let's do something fun...

Let's see if these domains are registered or not. I am using godaddy to check:

* Call.us
* Love.us
* Pets.us (available for $30K yikes)
* toysr.us

Let's try Call.us

    $ whois call.us

It shows the contact for a Law Office.

    $ whois love.us

It shows a company in California.

    $ whois Pets.us

Someone in Delaware

    $ whois toysr.us

This domain is taken by ToysRUs. And it shows a contact for someone in NJ.

What about this one:

    $ whois google.us

It shows a contact name for Google.

## Reverse whois to the rescue

Now that you are an expert in WHOIS. Let's review reverse WHOIS.

Remember what I said a few paragraphs up there about the history of WHOIS?

Let me remind you:

"You can lookup someone's name and the result would be the domain registered by that someone.".

Let's try that.

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
![Reverse Whois Jack Dorsey]({static}/images/reverse-whois-jack-dorsey.jpg)
<p>&nbsp;</p>

Then you can `whois` one of the results:

    $ whois tesse.xyz

Warning: I am not sure if this is the real Jack Dorsey. Proceed at your own risk :)

If you are not feeling the Neo or Trinity in you...

You can just:

Google "reverse whois" to find a few tools that allow you to enter person's name and in return it will give you domains registered under that name.

In another example (missing screenshots) I entered a first and last name and the result was a few domains that end with `.mx` which is the top level domain (TLD) for Mexico.

I am sure this person is not in Mexico. Or why would he buy domains with that top level domain? Very unlikely.

In the results there was also a domain that ended with `.us`.

Remember that...

This type of level domain doesn't allow secure private domain name registration.

This is when you `whois` a domain and it shows up as `private registration` and it doesn't show any contact info.

These are the restrictions for `.us` domains:

* Any US citizen or resident
* Any US org or corp

I think I am on the right track.

## Whois the domain

I prefer the Terminal for WHOIS so...

    $ whois awesomdomainfound.us


The result of a `whois` for a `.us` top level domain will always contain the registration name.

In this case I found the contact info for that person.

<p>&nbsp;</p>
![Reverse Whois OMG]({static}/images/reverse-whois-omg.gif)
<p>&nbsp;</p>

Now you are an expert at WHOIS and reverse WHOIS to find useful data about domains.


## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.