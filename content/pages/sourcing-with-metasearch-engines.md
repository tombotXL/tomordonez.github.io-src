Title: Sourcing with Metasearch Engines
Author: Tom Ordonez
Status: hidden
Slug: sourcing-with-metasearch-engines
Summary: Metasearch engines aggregate multiple search engines. This is a review of sourcing with metasearch engines.

In simple terms a metasearch engine is an aggregator of data. It uses another search engine to produce results. In most cases it uses either several search engines or crawls specific pages.

I'd like to find software engineers or software developers that know Python, but don't show me any results about snakes. Using Google, the query would need to be formulated like this:

    ("software engineer" | "software developer") python -snake

This is a comparison of a few metasearch engines using this search query.


## 1. All the Internet
https://www.alltheinternet.com/

It is described as 'All the internet for Google Chrome'. Let's try the query:

    ("software engineer" | "software developer") python -snake

It opens a new window (tab) and the first 8 results are ads. Each result has a tag on the left of the hyperlink. The tag says either 'Ad' or 'Web'. There are more Ads than organic results.

Let's do a side by side comparison with Google.

Google results are mostly from: indeed, glassdoor, and greenhouse.

`Alltheinternet` shows results from these domains:

* daxx.com
* builtinla.com
* lifeatexpedia.com
* technical.ly
* deliveryhero.com
* codefellows.org

Despite the clutter homepage and all the Ad results, it gave some interesting results. The search engine also has a short Boolean help at the bottom of the home page.

## 2. eTools
https://www.etools.ch/

This one is branded as 'the transparent Metasearch engine from Switzerland'. The design is outdated. Let's try the query:

    ("software engineer" | "software developer") python -snake

Above all results there are two filter options:

* `Country`. Default is 'worldwide'
* `Language`. Default is 'all'

On the right side there are more filter options

* `Source`. Default is 'All', options are: Ask, Duckduckgo, Exalead, Google, Mojeek, Wikipedia, Yandex
* `Domain` (TLD)
* `Topic`. Jobs, programmer, technology, salaries, etc.

Let's see the results:

* No ads
* Each result shows the source. For instance the first result says `Source: Google | Yandex`
* On the left of each result it has a 'relevance' bar. The first result says `Relevance 10/10 | Sources: 2/7`

Each result has a link with `status`. The first result shows this:

    Status code:    200 - Document exists
    IP address:     169.45.207.200
    AS information:     AS36351 SoftLayer Technologies Inc.
    Cookie sent:    Yes
    Content type:   text/html;charset=UTF-8
    Content length:     Undefined
    Last modified:  Undefined
    Response duration:  1.40 seconds
    Server software:    nginx
    Server location:    ISO country code: US (United States) (US)
    External links:     RIPE | Netcraft | Alexa

It shows these results:

* stepstone.de
* youtube 'a day in the life of a software engineer python'
* startus.cc
* some wikipedia articles
* ziprecruiter

I watched a bit of that video and saw that youtube has dozens of videos that start with `a day in the life of a`.

This is a great metasearch engine so far.

## 3. qwant
https://www.qwant.com/

This one has a modern and responsive interface. It has a pop-up that says 'The only European search engine, we are cookie free, we don't keep any search history'.

Let's run the query:

    ("software engineer" | "software developer") python -snake

The query was really fast. The results don't show any ads. It doesn't have additional filters like `eTools`. Let's look at some of the results:

It has indeed, glassdoor, payscale, youtube, quora. The same youtube result. It auto loads when scrolling and it didn't show pagination. However it has a few other interesting results:

* letsintern.com
* educba.com
* workable.com
* naukri.com
* codementor.io

I looked into this last result in more detail and found a list of freelance python developers.

`Qwant` seems to be more of a platform than just a search engine. It has a well designed interface but I preferred the results and filters from eTools.

## 4. weboasis
https://weboas.is/

The interface reminds me of Neo looking for the Matrix. Upon entering the query:

    ("software engineer" | "software developer") python -snake

The search field has options to choose a search engine. I selected `SearchEncrypt`.

However the search didn't go through. It opened `SearchEncrypt` on a new tab. I've never used this search engine. I tried a similar query on this engine: `python "software engineer" -snake`. Other than the usual suspects, indeed and glassdoor, it has a lot of interesting results. Another rabbit hole.

Back to weboasis, under the search field, there are a few filters. One of them is related to coding sites. Here are some interesting options I found:

* hackwage
* awesome cheatsheets (for programming languages)
* public APIs

This is definitely a metasearch engine to source technical folks. It has a lot of rabbit holes that I hope you can explore.