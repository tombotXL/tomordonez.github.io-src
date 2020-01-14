Title: OSINT Scraping On A Ramen Budget
Author: Tom Ordonez
Status: hidden
Slug: osint-scraping-ramen-budget
Summary: OSINT is collecting data from public sources for intel. Here is a tool for OSINT scraping.

OSINT stands for Open-source intelligence. It is the process of collecting data from public sources to be used in an intel context.

Google search query: `OSINT`

Result: Search results for you to review :)

I won't go into more detail about what OSINT is or what is used for. Instead I am going to focus on reviewing a tool that I found on Github to perform OSINT searches.

The tool is called Skiptracer. Find the code here:
https://github.com/xillwillx/skiptracer

Further disclosure, I didn't write this code, use at your own risk. Risk means, if you install it, your computer will self destroy in 3, 2, ..., just kidding.

I borrowed the author's great description of this tool for my blog post. The author describes it as "OSINT framework...on a ramen noodle budget."

## Installing Skiptracer

Here is when I am going to lose a lot of readers.

To install this tool you have to type some commands on your command terminal.

...pageviews just dropped...bounce rate 99%.

If you are still reading. I will assure you that it's not that hard. It uses Python2.

Here is a good tutorial for installing Python on Windows and Mac: https://realpython.com/installing-python/

It will take you just 5 minutes to install it. It's that easy.

Let's start by cloning the repo.

OK...mmm. Most likely this is a good tool if you know what Github is or you are somehow familiar with Github.

Open your terminal, go to wherever you want to download the repository:

    $ git clone https://github.com/xillwillx/skiptracer.git skiptracer
    $ cd skiptracer

Now you need to set a virtual environment to use Python2.

I lost you, right?

I need to build a sort of container in my computer to install this tool and it won't affect anything else in my system.

    $ virtualenv -p /usr/bin/python env
    $ source env/bin/activate

Now we have to install the requirements for skiptracer:

    $ pip install -r requirements.txt

That's it. That wasn't so horrible, right?

## Using Skiptracer

Just use this command:

    $ python skiptracer.py

Now you will get this awesome menu.

![Skiptracer menu]({static}/images/skiptracer-menu.jpg)

The menu has these lookup options:

* Email
* Name
* Phone
* ScreenName
* License plate
* Domain

## OSINT Email

Let's start with `Email`. I googled this: `Bill Gates email` and got this: `bill.gates@microsoft.com`

On the menu I typed `1` to select `Email`.

Now I got this menu:

![Skiptracer menu]({static}/images/skiptracer-email-menu.jpg)

The menu has these options:

    [1] All - Run all modules associated to the email module group
    [2] LinkedIn - Check if user exposes information through LinkedIn
    [3] HaveIBeenPwned - Check email against known compromised networks
    [4] Myspace - Check if users account has a registered account
    [5] AdvancedBackgroundChecks - Run email through public page of paid access
    [6] Reset Target - Reset the Email to new target address
    [7] Back - Return to main menu

When trying option `[5] AdvancedBackgroundChecks`, I got these results:

![Skiptracer menu]({static}/images/skiptracer-email-bill.jpg)

The results show this data:

* Aliases
* Phone numbers
* Email addresses
* Address, street, city
* Previous address

## OSINT Phone

Let's go back to the previous menu and try a phone number. I googled `spacex los angeles` and got the phone number listed on Google Maps.

Back in our Terminal, selecting the `Phone` option shows this menu:

![Skiptracer menu]({static}/images/skiptracer-menu-phone.jpg)

The menu has these options:

    [1] All - Run all modules associated to the phone module group
    [2] TruePeopleSearch - Run email through public page of paid access
    [3] WhoCalld - Reverse phone trace on given number
    [4] 411 - Reverse phone trace on given number
    [5] AdvancedBackgroundChecks - Run number through public page of paid access

After adding the phone number, I selected the option for `[1] All`. It started showing some results:

* Name, age, alias
* Related associates
* Addresses
* Related phone numbers

## OSINT Screenname

Back to the main menu. Let's try Screenname.

What's Elon Musk's Twitter handle? On Twitter I typed `Elon Musk` and...

It's `@elonmusk`.

The second result says `@BoredElonMusk`. It has 1.7M followers. Described as a parody account of Elon Musk.

Back on SkipTracer, I chose the option for `Screenname`

![Skiptracer menu]({static}/images/skiptracer-menu-screen.jpg)

It has these options:

    [1] All - Run all modules associated to the email module group
    [2] Knowem - Run screenname through to determin registered sites
    [3] NameChk - Run screenname through to determin registered sites
    [4] Tinder - Run screenname and grab information if registered

The results from `NameChk` shows:

    [+] Acct Exists: https://facebook.com/BoredElonMusk                                 
    [+] Acct Exists: https://twitter.com/BoredElonMusk                                  
    [+] Acct Exists: https://www.instagram.com/BoredElonMusk                            
    [+] Acct Exists: https://plus.google.com/+BoredElonMusk/posts            
    [+] Acct Exists: https://www.reddit.com/user/BoredElonMusk/                         
    [+] Acct Exists: https://www.pinterest.com/BoredElonMusk/                           
    [+] Acct Exists: https://BoredElonMusk.yelp.com

And about a dozen more links.

## OSINT License Plate

I tried a few vanity license plates but couldn't find results. This requires more experimentation.

I tried these for California:

* MLENG
* DATAENG
* VOID
* JAVAENG

OSINT is an interesting process to find more data from different sourcers. You just need some basic knowledge of the command line to use this tool.