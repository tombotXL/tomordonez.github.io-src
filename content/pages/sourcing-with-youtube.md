Title: Sourcing with Youtube
Author: Tom Ordonez
Status: hidden
Slug: sourcing-with-youtube
Summary: Youtube has 1.3 billion users. Here is a short tutorial for sourcing with Youtube.

Google search: `Youtube number of users`

Result: `1.3 billion users`

Google search: `world population`

Result: `7.5 billion`

On Youtube, I searched for `software engineer`.

The first result was `A Day in the Life of a Software Engineer`.

Other results:

* How I Spend My $250K Software Engineer Income
* Technical interview with a Google engineer
* Career Paths for Software Engineers and how to navigate it.
* Why Software Engineering is hard
* A Day In The Life of a Facebook Software Engineer Intern

Hold on. I gotta watch this last video...

OK it was about...nothing.

However, it had 254 comments.

Browse more results:

* A Day In the Life of a Software Engineer Intern In San Francisco
* What do I do as a Software Engineer?
* A Day in the Life of a Software Engineer | New York City

Then, the famous:

* How to: Work at Google — Example Coding/Engineering Interview

Then more of:

* A Day in the Life of Software Engineer, Jakarta
* 💻 One Day in Life of SAP Software Engineer
* Day In The Life: Software Engineer Intern @ WeWork

On the recommendations I saw this video from MIT `Dynamic Programming I: Fibonacci, Shortest Paths`. It had 568 comments.

This has to be valuable data...**the comments**.

## Scraping Youtube comments

How do I scrape these?

Google search query: `Scrape youtube comments`

Found this Github page `youtube-comment-scraper`.

It's built on `nodejs`. It has a website that says `Enter Youtube URL`.

Let's try the MIT video I found.

It says "Scraping comments"...sip of coffee.

And it's done.

![Youtube comments]({static}/images/youtube-comment-scrape.jpg)

It gives the option to download a `JSON` or a `CSV`.

Let's do `CSV`.

The file has this data:

* id
* user
* date
* timestamp
* comment text
* likes
* hasReplies
* numberOfReplies

A lot of interesting data in comments. Look at this comment:

    What I'm missing in the code?
    def fib (n):
     f=[]
     for k in range(1,n+1):
      if k<=2: 
       f=1
      else:
       f=f[k-1]+f[k-2]
      f[k]=f
     return f[n]
    
    for i in range(100):
     print(fib(i))

The comment has the full name of the username. The date is from a year ago.

Googled the name. Found his Github. Now his email. Found him on Linkedin.

You could compose a message like this...

## subject: fibonacci and shortest paths

Hey [don't forget to put his name here],

I ran into a youtube video from MIT about the shortest path algorithm. I don't want to sound like a creep but I found your comment and wonder if anybody replied to your question. If they didn't. Here is what might be missing from your code. [Add what the team suggested]. I know it has been a year, and I am sure you are beyond this. Anyhow, my team is looking for someone in [add city] to help us build [add what we are building]. We are currently [explain what we did]. I saw on your Github that you are working on [add project]. Super creepy I know :)

If you ever were to look for a new challenge, wondering what that would be. I am open to chat anytime. [add call to action]...