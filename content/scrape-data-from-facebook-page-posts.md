Title: Scrape Data From Facebook Pages
Date: 2018-01-18 18:00
Category: Coding
Tags: sourcing, scraping, Facebook
Slug: scrape-data-from-facebook-page-posts
Author: Tom Ordonez
Status: published
Summary: A tutorial to scrape data from Facebook pages for research purposes.

This is a tutorial to scrape data from Facebook pages for research purposes.

<p>&nbsp;</p>
![Scrape Data From Facebook Page Posts]({filename}/images/scrape-data-from-facebook-pages.jpg)
<p>&nbsp;</p>

I have been working with Facebook pages for a long time to create audiences. My process is setting up the templates, creating and automating content, generating likes, create custom audiences, facebook ads, landing pages and conversions with automated marketing funnels.

Often the question of most marketers is what content generates traffic. What copy should I use. What images should I use.

Facebook provides with analytics about your posts for both organic and paid. You cannot see analytics for a page that is not yours. Would you like to get these analytics?

In this tutorial I will show you how to scrape data from Facebook pages using a Python program.

## Who is this for?

Everybody is talking about data and what to do with it.

Research purposes for scraping this data:

* Review data from any Facebook page
* Build analytic reports
* Find the most engaging content from a Facebook page
* Find out what works and what doesn't from a Facebook page

## Available data

Data is available for these types of content:

* Posts from public pages
* Posts from open groups
* Comments from page posts
* Comments from group posts

To review the code in detail, please review the source <a href="https://github.com/minimaxir/facebook-page-post-scraper" target="_blank">here</a>.

## Setup: Create a Facebook App ID

Create a Facebook `App ID`.

For this you need to have a Facebook developer account. Just go <a href="https://developers.facebook.com/" target="_blank">here</a>.

Then create a new app.

<p>&nbsp;</p>
![Facebook create app id]({filename}/images/facebook-create-app-id.jpg)
<p>&nbsp;</p>

Open the app and lookup the `App ID` and `App Secret`.

<p>&nbsp;</p>
![Facebook get App ID]({filename}/images/facebook-app-id.jpg)
<p>&nbsp;</p>

## Setup: Get the Facebook Page ID

For example...

Sometimes I get ideas from this Facebook page.

<p>&nbsp;</p>
![Facebook Page Example]({filename}/images/facebook-page-example.jpg)
<p>&nbsp;</p>

The `ID` for this page is `ProgrammersCreateLife`.

## Setup: Modify Python Script

Getting the code is as simple as:

    $ git clone https://github.com/minimaxir/facebook-page-post-scraper.git

Then you can edit this file with your favorite editor. In my case vim:

    $ vim get_fb_posts_fb_page.py

This is what the section of the code looks like:

<p>&nbsp;</p>
![Facebook Page Post Setup]({filename}/images/fb-page-post-code-setup.jpg)
<p>&nbsp;</p>

## Run the script

Running the script is simple:

    $ python3 get_fb_posts_fb_page.py

This is what the output looks like:

<p>&nbsp;</p>
![Facebook Page Post Output]({filename}/images/fb-page-post-code-output.jpg)
<p>&nbsp;</p>

You can interrupt the process with `Ctrl+C`.

## Output file

This creates a CSV file with these columns:

* Post title
* Type of post
* Post link
* number of comments
* number of shares
* number of likes
* etc...

This is how the file looks:

<p>&nbsp;</p>
![Facebook Page Post CSV]({filename}/images/fb-page-post-csv.gif)
<p>&nbsp;</p>

## Using this data

If you feel wild, you could open these data sets with Python.

Or import to Tableau.

Or just open them in Excel and do some quick data analysis.


## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.
