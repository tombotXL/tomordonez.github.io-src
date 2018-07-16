Title: Linkedin Recruiter Bookmarklet
Date: 2018-07-13 22:00
Category: Sourcing
Tags: sourcing, linkedin recruiter
Slug: linkedin-recruiter-bookmarklet
Author: Tom Ordonez
Status: published
Summary: Linkedin recruiter bookmarklets to convert a project into list view and visualize hundreds of rows.

This is a sourcing trick that helps you in Linkedin recruiter.

I cannot remember how I came up with this. I think from a recruiting conference or a website. I remember modifying the code. But if you are the original source. Please comment so I can link you.

* Chrome
* Bookmark manager
* Add boomark
* For name enter the title
* For URL enter the code

## Linkedin JS Project List View

Go to a Linkedin recruiter project. It shows pagination with 10 results per page.

To convert to a longer list. Use this bookmarklet.

    javascript:(function(){var loc=location.href;loc=loc.replace('linkedin.com/recruiter/projects/','linkedin.com/cap/project/savedProfiles/');loc=loc+'?max=500';location.replace(loc)})()

## Linkedin JS Results 250

Once you convert to a longer list. It is easier to visualize as many results as possible. This shows up to 250 results.

    javascript: (function() {var loc = location.href;loc = loc.replace('&page=1&start=0&count=25', '&page=1&start=0');loc = loc + '&count=250';location.replace(loc) })()

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>