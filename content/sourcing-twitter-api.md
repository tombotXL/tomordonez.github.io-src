Title: Sourcing with the Twitter API
Date: 2017-09-15 18:00
Category: Recruiting
Tags: sourcing, recruiting, getting data, twitter api
Slug: sourcing-twitter-api
Author: Tom Ordonez
Status: published
Summary: Follow this process for sourcing with the Twitter API. Getting data using Ruby and the Twitter API

Follow this process for sourcing with the Twitter API. Getting data using Ruby and the Twitter API

![Sourcing with the Twitter API]({filename}/images/sourcing-twitter-api.jpg)

Twitter CLI is a command line interface program that allows you to interact with your Twitter account using the command line.

## Objectives

* Source on Twitter with the Twitter API.
* Convert data into a clean list of users.
* Get user information.
* Find websites, emails, phone numbers.
* Find out what users talk about to create a better outreach.

Get massive amounts of data with a simple one-liner "formula".

## Why?

Perhaps you only source with Linkedin. Perhaps you know boolean searches.

A boolean search is like a baby learning to swim. Learning how to source on Twitter with the API is like being Michael Phelps.

Do you want to be Michael Phelps? Continue reading.

## Requirements

This won't be easy. If it were easy then anybody could do it.

This requires:

* A general understanding about how computers work.
* You need to have: A Twitter account and a Twitter developer app.
* You need to have a Windows with a Linux Virtual Machine or a Mac or a computer with Linux.
* Ruby installed and some basic Ruby knowledge.
* Knowledge of the command line.
* Bash scripting knowledge.
* A lot of confidence and attention to detail

## Playing the Twitter game

The Twitter game has a few simple rules:

* I follow you. You follow me.
* Tweet often.
* Build relationships with mentions, favorites, retweets and direct messages.
* Create groups of people using lists.


## If I follow you. Will you follow me?

If the other person doesn't understand the Twitter game. They won't follow you.

Maybe the follow you and one day they unfollowed you. Why? Why????

Why would people stop following you on Twitter?

* You tweeted something too cute
* You tweeted something not cute
* They woke up in a bad mood
* Their dog unfollowed you


## A general understanding about how computers work

<iframe width="640" height="360" src="https://www.youtube.com/embed/LkqiDu1BQXY?rel=0&amp;controls=0&amp;showinfo=0&amp;t=1m7s" frameborder="0" allowfullscreen></iframe>

Computer. Computer!

(the computer doesn't answer. He tries with the mouse)

Hello computer.

(still nothing happens)

Just use the keyboard!

## Layers of abstraction

This is a computer science concept that explains the interaction between the human and the machine.

Have you tried to fix a computer? Maybe. Maybe not.

Probably you know that inside the computer you will find a circuit board with electronic components.

A motherboard with a processor. RAM memory. Wireless circuit card. Hard drive. Battery and other components.

These components only understand 1s and 0s.

But you. The human. You only understand English.

You communicate with the computer through "layers of abstraction".

1s and 0s are very abstract. If you don't know about binary numbers. This layer is difficult to understand.

A layer above this is "machine code".

Machine code looks sort of like this:

    0x51a12
    0x51a20
    0x519fe

Still very abstract.

A layer above this looks like this:

    while (fahr <= upper) {
      celsius = (5.0/9.0) * (fahr-32.0);
      printf("%3.0f %6.1f\n", fahr, celsius);
      fahr = fahr + step;
      }

Less abstract right? It starts to look like some sort of math.

A layer above this looks like this:

    File.readlines('file.txt').each do |line|
      puts line
    end

It starts to look more like English.

One more layer above this is typing "instructions" to a program like Excel or Word or Gmail.

For this tutorial we need to talk at this level:

    File.readlines('file.txt').each do |line|
      puts line
    end

While you don't have to become a programmer. You can get away with just learning a little bit of code.

## You need to have a Twitter account

If you don't have a Twitter account. Something must be wrong in the Universe.


## You need to have a Twitter developer app

Go to <a href="https://apps.twitter.com/app/new" target="_blank">Twitter Application Management</a>

Sign-in using your Twitter account.

Click on Create New App.

Fill out the form.

Go to Permissions and set Access to "Read, Write and Access direct messages"

You might need to authorize your Twitter account with your mobile phone. Go to: <a href="https://mobile.twitter.com/settings" target="_blank">Mobile Twitter settings</a>.

Towards the bottom it should have a "Phone" listed.

## If you are on Windows you need Linux in a Virtual Machine

Your computer should have at least 8GB of RAM for this.

A Virtual Machine (VM) is used to install an operating system inside another one. Therefore a "virtual machine".

In this case we need to install Linux inside Windows.

Install the VM from <a href="https://www.virtualbox.org/wiki/Downloads" target="_blank">Virtualbox</a>.

Choose `Virtualbox for Windows`

Download and install the defaults.

Now download Linux Ubuntu from <a href="http://www.ubuntu.com/download/desktop" target="_blank">here</a>.

This downloads a file of type `.iso`

DO NOT double click on this file to open it. We will only open this file with VirtualBox.

Open VirtualBox:

* Click on the button "New"
* Name: Ubuntu
* Memory size: 4096
* Choose: Create a virtual hard drive now
* Hard drive file type: VDI (VirtualBox Disk Image)
* Storage on physical hard drive: Dynamically allocated
* Select the size of the virtual hard drive: 10.00 GB

A new VM has been created with name "Ubuntu". With status "Powered Off".

Click on the arrow "Start".

Choose the Ubuntu "iso" file that you downloaded.

The VM will load with Ubuntu. Then follow the instructions to install the defaults.

## Do You have a Mac?

You are almost all set here.

Just need to install 2 programs:

The text editor Sublime. <a href="https://www.sublimetext.com/" target="_blank">Download here</a>.

The terminal iTerm. <a href="https://www.iterm2.com/" target="_blank">Download here</a>.

## You need to have Knowledge of the command line.

In Windows there is a program called the "Command Prompt". (We are not going to use this)

In Mac or Linux there is a program called the "Terminal" aka "the shell" aka "the bash shell" aka "the command line"

This "command line" helps you communicate with the computer by using code.

A few basic "command line" examples are:

Open the terminal and type this code to see who is the current user logged in:

    $ whoami

You don't need to type in the `$` dollar sign. This is the Terminal "prompt" inviting you to talk to the computer. Whenever you see the dollar sign. It means this is a command line code.

Type this code to see a list of directories:

    $ ls

Type this code to change directories:

    $ cd Downloads

Type this code to copy the contents of one file to another:

    $ cp this_file to_this_file

There are a lot more "commands" that you can use to communicate with the computer. Later, I will explain a few more.

## You need to install Ruby

Ruby is a "high level programming language" that reads sort of like English.

Ruby has "modules" called "Gems" that adds more functionality to a program.

For instance if you are developing a web app that requires a login authentication. There is already a Ruby gem for login authentication that's (almost) plug and play. That way you don't have to build this feature from scratch.

Ruby gems are open source and most are supported by the open source community. Some are also supported by organizations.

Ruby and Ruby gems are constantly updated and they work together to create a functional application.

Ruby is supported by a core team. Some Ruby gems are also supported by this team. But many other Gems are supported by other developers of the open source community.

This creates a challenge.

Similar to the way that Windows works. Excel 98 worked with Windows 98. As Windows kept updating the operating system then other programs had to be properly maintained to work properly with Windows. Excel 98 won't work with Windows 7.

Something similar happens with Ruby and many other programming languages.

There is a gem called `oauth` that add authentication functionality to a Ruby application.

The version I have installed is `0.4.7`.

While the Ruby version I have is `2.3.0`

If the Ruby core team decides to launch version `3.0.0` then `oauth` might stop working. Unless the `oauth` team makes sure that the gem is updated and works with such version of Ruby.

## Ruby on Windows with Linux Virtual Machine

Open VirtualBox and start the Ubuntu virtual machine.

Open the terminal.

Follow this guideline to <a href="https://www.tomordonez.com/installing-ruby-on-ubuntu.html" target="_blank">Install Ruby on Ubuntu</a>.

## Ruby on Mac

If you have a Mac. The installation process is similar to Ubuntu.


## You need to Install Twitter CLI ruby gem

Twitter CLI aka `t` is a Ruby gem that helps you connect with the Twitter API using the command line. Say that out loud 3 times.

In the Terminal type:

    $ gem install t

Previously you created an app on Twitter. We need to authenticate this app with our (Twitter CLI) ruby gem.

    $ t authorize

This will send you to an URL to authorize the application that you previously created on Twitter.

## Input and Output to send data

There is another important computer science concept that you need to learn.

Input and Output.

* When you type into Word. The input is the keyboard and the output is the Word document.
* When you want to print the document. The input is the Word document. The output is the printer

You can redirect data in different ways using simple code.

## Redirecting data with Add and Append

    > A greater than sign means "add".
    >> Two greater than signs mean "append".

When you use a command line such as `ls` to list the contents of your current directory. The output is sent to the "standard output" aka "stdout". Which is the Terminal screen.

Instead we could list the contents of a current directory and send the output to a file.

    $ ls > directory-contents.txt

In this example we are using `ls` to list the contents of the current directory. Then we are using `>` to "add" the output to the file `directory-contents.txt`.

## Redirecting data with Pipe

    | This symbol is called a "Pipe".

With pipes you can redirect the output of one side to the input of another side.

    $ ls | wc -l

In this example we are using `ls` again to ask the computer for the contents in the current directory.

    wc is another command called "word count" that helps you count words from a text file.

If you use it like this: `wc -l` it will count the number of lines from a text file.

We use the pipe `|` to send the output of `ls` (the contents of the current directory) to the command `wc -l` to count the number of lines.

## How to source on Twitter

Open the Terminal.

Get a list of all available commands:

    $ t help

## Send a tweet from the command line

    $ t update "I am tweeting from the command line"

## Get details about a Twitter user

    $ t whois tomordonez

## Create a List of People That Don't Follow You

First, count the number of people that you follow that don’t follow you back:

    $ t leaders | wc -l

With `leaders` you can get a list of people that you follow but don't follow you.

With `|` you are redirecting the output to the command `wc -l` to count the number of lines.

If there is 1 user for each line. Then you will get the number of users. 

Now create a Twitter list:

    $ t list create NameoftheList

Add those people to the list. Keep in mind that it might get stuck up to 500 users. Just wait a few minutes and try it again.

    $ t leaders | xargs t list add NameoftheList

In this example we are using `t leaders` again to get a list of people that you follow but don't follow you back.

We are sending that output to `xargs`. Which reads the output line by line and executes the next command `t list add NameoftheList`, to add every user to that Twitter list.

## Download Users That Belong To A Twitter list

Let's get back to the Ruby developer example.

The most famous Ruby conference is called "Ruby Conf" and they often use the Twitter hashtag #RubyConf.

You can create a Twitter list and add people that use this hashtag.

Go to the Terminal and use this code to get a list of all your Twitter lists:

    $ t lists your-username

Replacing "your-username" with your Twitter username. With or without the `@`. It doesn't matter.

Find the Twitter list you created. Let's say that the Twitter list is called `rubyconf`.

    $ t lists tomordonez

This will display all my lists and it might be hard to find the one I am looking for.

    $ t lists tomordonez | grep 'ruby'

This code is using the pipe `|` to send the output of `t lists tomordonez` to the input of `grep 'ruby'`.

`grep` is another command that "filters" data. In this case is filtering the output of all my Twitter lists and find only those that contain the word `ruby`

It will find a list such as:

    @tomordonez/rubyconf

With the name of the Twitter list now we can download the list of all users that are members of this list.

    $ t list members -c @tomordonez/rubyconf > twitter-list-rubyconf-members.csv

This code is using the redirection `>` which sends the output of `t list members @tomordonez/rubyconf` to the input of `twitter-list-rubyconf-members.txt`.

This code is pulling the list of members that belong to that list and saving them into that csv file.

## Create a CSV file from a Sourcecon Twitter list

I see that Sourcecon has 5 lists.

![Twitter Sourcing with Tom Ordonez]({filename}/images/twitter-sourcing-tomordonez-sourcecon-lists.jpg)
<p>&nbsp;</p>
<p>&nbsp;</p>

The first list is called "SourceCon 2017 Speakers". It has 26 members.
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

## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
