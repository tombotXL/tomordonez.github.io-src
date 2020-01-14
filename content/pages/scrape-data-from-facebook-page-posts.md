Title: Scrape Data From Facebook Pages
Author: Tom Ordonez
Status: hidden
Slug: scrape-data-from-facebook-page-posts
Summary: A tutorial to scrape data from Facebook pages for research purposes.

This is a tutorial to **scrape data from Facebook pages** for research purposes.

<p>&nbsp;</p>
![Scrape Data From Facebook Page Posts]({static}/images/scrape-data-from-facebook-pages.jpg)
<p>&nbsp;</p>

I have been working with Facebook pages for a long time to create audiences. My process is setting up the templates, creating and automating content, generating likes, create custom audiences, facebook ads, landing pages and conversions with automated marketing funnels.

Often the question of most marketers is what content generates traffic. What copy should I use. What images should I use.

Facebook provides with analytics about your posts for both organic and paid. You cannot see analytics for a page that is not yours.

Would you like to get these analytics?

In this tutorial I will show you how to scrape data from Facebook pages using a Python program.

## Who is this for?

Everybody is talking about data and what to do with it.

Research purposes for scraping this data:

* Review data from any Facebook page
* Build analytic reports
* Find the most engaging content from a Facebook page
* Promote this content with Facebook Audiences.
* Track analytics for your careers blog or content website.

## Facebook Audiences

If you are familiar with Facebook ads then you might have used Facebook Audiences.

With Facebook Audiences you can research and select demographics from a variety of categories.

For instance I could target something like:

"Computer Science students from Stanford that might know Python, that might be data scientists and that might have a PhD".

You can create 3 types of audiences:

* A custom audience
* A lookalike audience
* A saved audience

The one I use the most for research is a saved audience. You can choose demographics, interests and behaviors and save them for ads.

If you have a website. Perhaps a career blog or any content website. You can install a tracking code on the website called a "pixel". So that you can track down which Facebook users that clicked on your ad, also ended on your website.

With a custom audience, you can connect with people that visited your website even if they didn't click on one of your ads. Oh yeah! You can also create a custom audience from your customer contacts or from your mobile app.

And the lookalike audience helps you reach people based on users that already liked your page.

## Facebook analytics

If you are a little bit familiar with Facebook pages and Facebook ads. Maybe you have seen Facebook analytics.

If we get very granular. The most basic data that you get from posting content on a page is: likes, comments and shares.

In this example. This post reached about 10.5K people. Has 343 likes, 42 shares and 26 comments.

<p>&nbsp;</p>
![Facebook analytics for a post]({static}/images/facebookAnalyticsPost.jpg)
<p>&nbsp;</p>

Here are more details about this post analytics:

* 10,673 people reached
* 443 likes: 366 on post, 77 on shares
* 9 love
* 2 wow
* 1 angry
* 55 comments: 37 on post, 18 on shares
* 1,242 post clicks

If you go to your Page Insights you can review this data:

* Actions on page
* Page views
* Page likes
* Reach
* Post engagements

There are also stats for recent posts and recommendations for pages to watch (aka possible competitors).

These pages to watch are a good source to review competitor analytics.

Although you only get some data:

* Total page likes
* Percentage increase from last week
* Number of posts this week
* Engagement this week

What you cannot see is post analytics from competitors. You cannot see the number of likes, shares and comments for each of their posts. You could do it manually by going to each of their posts and looking up the number of likes, shares and comments. But what if they have 100 posts or more. That would take forever right?

What I will show you is a way to get data from any Facebook page. You can download datasets from other Facebook pages and get these stats for each post:

* Number of likes
* Number of shares
* Number of comments

Then you can analyze this data using Excel or Tableau or Python or any software used for data analysis.

The result of this analysis is to answer questions. A question could be:

"What is the most engaging content for Phd computer science students that go to Stanford".

That would be some awesome insight. Right?

## Available data

Data is available for these types of content:

* Posts from public pages
* Posts from open groups
* Comments from page posts
* Comments from group posts

To review the code in detail, please review the source <a href="https://github.com/minimaxir/facebook-page-post-scraper" target="_blank">here</a>. Please note that I didn't write this code.

## Setup: Create a Facebook App ID

Create a Facebook `App ID`.

For this you need to have a Facebook developer account. Just go <a href="https://developers.facebook.com/" target="_blank">here</a>.

Then create a new app.

<p>&nbsp;</p>
![Facebook create app id]({static}/images/facebook-create-app-id.jpg)
<p>&nbsp;</p>

Open the app and lookup the `App ID` and `App Secret`.

<p>&nbsp;</p>
![Facebook get App ID]({static}/images/facebook-app-id.jpg)
<p>&nbsp;</p>

## Setup: Get the Facebook Page ID

For example...

Sometimes I get ideas from this Facebook page.

<p>&nbsp;</p>
![Facebook Page Example]({static}/images/facebook-page-example.jpg)
<p>&nbsp;</p>

The `ID` for this page is `ProgrammersCreateLife`.

## Setup: Modify Python Script

Getting the code is as simple as:

    $ git clone https://github.com/minimaxir/facebook-page-post-scraper.git

Then you can edit this file with your favorite editor. In my case vim:

    $ vim get_fb_posts_fb_page.py

This is what the section of the code looks like:

<p>&nbsp;</p>
![Facebook Page Post Setup]({static}/images/fb-page-post-code-setup.jpg)
<p>&nbsp;</p>

## Run the script

Running the script is simple:

    $ python3 get_fb_posts_fb_page.py

This is what the output looks like:

<p>&nbsp;</p>
![Facebook Page Post Output]({static}/images/fb-page-post-code-output.jpg)
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
![Facebook Page Post CSV]({static}/images/fb-page-post-csv.gif)
<p>&nbsp;</p>

## Using this data

If you feel wild, you could open these data sets with Python.

Or import to Tableau.

Or just open them in Excel and do some quick data analysis.

Ideally in this data analysis process you have some questions that you want to resolve with the data.

For instance you could ask yourself:

"What is the most engaging content to target Data Scientists with a PhD and living in Silicon Valley".

Then use the data analysis process to resolve questions like that.

This is powerful insight.

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>