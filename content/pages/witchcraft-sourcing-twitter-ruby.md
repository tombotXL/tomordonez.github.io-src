Title: Witchcraft Sourcing with Twitter and Ruby
Author: Tom Ordonez
Status: hidden
Slug: witchcraft-sourcing-twitter-ruby
Summary: I will be presenting at Sourcecon in Austin about sourcing using Bash, Ruby, Python and R.

I will be presenting at Sourcecon in Austin about sourcing using Bash, Ruby, Python and R.

Here is how I look on a happy day. Feel free to say hi if you see me around. I am often friendly :)

You can also connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.
<p>&nbsp;</p>

![Tom Ordonez at Sourcecon]({filename}/images/tomordonez-sourcecon-2017.jpg)

<p>&nbsp;</p>
<p>&nbsp;</p>
## Check it out on Wednesday, September 27 • 2:25pm - 3:00pm under the Programmers track
<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({filename}/images/tomordonez-witchcraft-sourcing-sourcecon.jpg)

## This is a preview of witchcraft sourcing with Twitter and Ruby.

What you will learn from this awesome story:

* How to create a CSV file from any Twitter list
* The CSV file has valuable info about a user
* Use the data for automating personalized DMs

This is a preview of what this CSV looks like.

<p>&nbsp;</p>

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-csv-file.jpg)

<p>&nbsp;</p>

Twitter has about 100 million tweets a day.

Those are a lot of tweets.

100 million.

Actually is about 250 million.

Or maybe more.

Just to make math easy. Let's stick with 100 million tweets per day.

That's like 1,000 tweets per second.

These numbers are hard to visualize in your mind.

But if you have used a social media tool like Hootsuite you see how those tweets fly...

...at warp speed.

You cannot even read them. They appear on screen, they get pushed down your timeline and dissapear really fast.

So how do you keep up with so many tweets?

Drum roll...trrrrrrrr

## Twitter lists!

But Twitter lists can be both your best friend and your worst enemy.

If you have a moderate number of users added to a Twitter list then the tweets might not fly away as fast.

There is a good chance that you will be able to read your Twitter timeline using a Twitter list (with a social media tool).

Let's say that a "moderate number" is 50 users.

You can easily scroll up and down a day's worth of those 50 users.

What if your Twitter list has 500 users?

...feeling dizzy now.

What if it had 1,000 users?

...I need a bag...not feeling good.

So many users, so many tweets, so much data.

## Why is Twitter data useful?

You can do sentiment analysis using Twitter.

Google this: "twitter sentiment analysis".

![Twitter sentiment analysis]({filename}/images/twitter-sentiment-analysis.jpg)

You will get about 1 million results.

Sentiment analysis is used to find out if a piece of text is positive, negative or neutral.

Social media is all about emotions, right?

That's why emoticons are such a big thing.

That's why Facebook added emoticons to their "Like" button.

What if you could find the emotions from tweets. That would be awesome right?

What if you could find if someone is in a good mood. You contact them and they reply back.

But what if they are in a bad mood. You contact them and they block you.

It's a gold mine to have that knowledge. Positive, negative or neutral.

We will leave sentiment analysis for another life. As this can become very technical.

1.21 Gigawatts. Great Scott!

What the heck is a gigawatt?

yeah...that technical :)

For now we are going to focus on getting data from Twitter. You have to start somewhere right?

## Getting data from Twitter

Here is a summary for getting data from Twitter:

* Install Ruby
* Create a Twitter app
* Find Twitter lists
* Use magic potions to get Twitter data

## 0. Hardware

Let's start with zero.

I previously used a MacBook Air, 2011, 4GB.

I also used a Mac mini, 2013, 16GB.

A cheap Thinkpad, 16GB with Ubuntu Linux. Then I moved to Fedora.

I have used Windows since Windows 98. OMG I am feeling old right now.

I am a hardware geek.

![Hardware Geek]({filename}/images/hardware-geek.gif)

## What's your favorite hardware?

Ideally you are on Linux. Although there is a good chance you are on Mac or Windows.

In Windows it will be a little bit painful because you need a terminal to enter commands. And although Windows has one, it has different commands than Linux or OSX.

For Windows I recommend that you install a Linux Virtual Machine. If you search on Youtube "install linux virtualbox on windows" you will find a lot of good tutorials to follow.

![Linux Virtualbox]({filename}/images/install-linux-virtualbox.jpg)

## 1. Installing Ruby

Ruby is a programming language. Twitter was initially built using Ruby on Rails. Now they use Scala and Java.

Installing Ruby is (sort of) easy depending on your computer abilities :)

You can install Ruby using 2 ways:

* Follow the official Ruby <a href="https://www.ruby-lang.org/en/documentation/installation/" target="_blank">documentation</a>.
* Install using <a href="http://rvm.io/" target="_blank">Ruby Version Manager (RVM)</a>.

Ruby has a component called <code>gems</code> which are software packages with different features.

## 2. Installing the Twitter gem

There is a gem called <code>Twitter CLI</code> that uses the Twitter API and Ruby.

On your Terminal it's as simple as:

<code>gem install t</code>

## 3. Register an application on Twitter Developer

Go to <a href="https://apps.twitter.com/app/new" target="_blank">Twitter Application Management</a>.

* Sign-in using your Twitter account
* Click on Create New App
* Fill out the form
* Go to Permissions and set Access to "Read, Write and Access direct messages"

Go to the command line and type:

<code>t authorize</code>

This will send you to an URL to authorize the application.

## 4. Use magic potions to get Twitter data

Get a list of all available commands:

<code>t help</code>

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-t-help.jpg)

Send a tweet from the command line:

<code>t update "I am tweeting from the command line. So awesome"</code>

Get details about a Twitter user:

<code>t whois tomordonez</code>

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-t-whois.jpg)

## Get data from a Twitter list:

I see that Sourcecon has 5 lists.

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-sourcecon-lists.jpg)
<p>&nbsp;</p>
<p>&nbsp;</p>

The first list is called "SourceCon 2017 Speakers". It has 26 members (as of this writing). I just realized I am not one of them. sad face.
<p>&nbsp;</p>
<p>&nbsp;</p>

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-sourcecon-speakers.jpg)

This is the URL of this list:

<code>https://twitter.com/SourceCon/lists/sourcecon-2017-speakers</code>

What you need to get is the user name and the list name:

* User name: SourceCon
* List name: sourcecon-2017-speakers

Now let's create a CSV file with all the users that belong to that list.

<code>t list members -c SourceCon/sourcecon-2017-speakers > sourcecon-2017-speakers.csv</code>

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-csv-file.jpg)

These are some of the columns from the CSV file:

* Date joined
* Date of last tweet
* Number of tweets, favorites, listed, following, followers
* User name
* Name
* Bio
* Location
* URL

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-csv-details.gif)

## What to do with this data?

* Automate sending personalized DMs
* Sentiment analysis
* Data mining
* Create a data warehouse

## Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>
![Find me on Linkedin Tom Ordonez]({filename}/images/contact-tomordonez-linkedin.gif)
