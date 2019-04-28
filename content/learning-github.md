Title: Learning Github
Date: 2019-04-21 22:00
Category: Coding
Tags: coding, git, github
Slug: learning-github
Author: Tom Ordonez
Status: published
Summary: Learning Github. An interactive process to learn git and Github.

Learning Github. An interactive process to learn git and Github.

For a while I have been thinking of an interactive process to learn and improve skills in git and Github, without contributing to someone else's repository.

How could I contribute to my own repository from another computer or another Github account?

I invest great efforts in documenting learning. I recently completed the mind-blowing "Learn how to Learn" course in Coursera, and reading the course instructor's book.

My problem started with publishing this blog. It uses a static generator in Python, which I installed on an old and upgraded laptop. I now use this laptop on my homemade standup desk. My solution was to use the standup desk to write blog posts.

What I found is that when I am in focused mode, I need to document these ideas right away. Shifting from my main desk to my standup desk often, would disrupt my flow of thoughts.

## Two Github Accounts

I thought of setting up my sitting desk with the same publishing platform using the same Github account. However, I wanted to find a way to improve my Git, and Github skills. I also wanted to improve my skills in collaborating on a repo.

**Standing desk**

* aka Server
* Main Github account
* Static generator platform

**Sitting desk**

* aka Local
* 2nd Github account
* Forked repo

## Writing blog posts in Local

I created a new branch called `newposts`. I create the content and push to my forked repo on the 2nd Github account.

    git add .
    git commit -m "new blog post draft"
    git push -u origin newposts

## Create a pull request

On my 2nd Github account. I navigate to my original repo and create a pull request.

I did some research on naming conventions and came up with this one:

    [newpost] name of the blog post

I don't add comments to the pull request.

## Merge pull request

This is where it can become complex and where most of the learning will take place.

My Local branch is ahead of master.

On my Main Github account, I went to my repo and confirmed that I got a pull request. There are no conflicts and I am able to merge the commit into master.

Things could be different if I were to work on Server and Local at the same time. This is where the opportunity of improving collaboration skills could occur. A sort of Jekyll and Hyde collaboration.

## SSH to my LAN Server

This is how I [remote access Linux](https://www.tomordonez.com/remote-access-linux-fedora.html).

From my Local computer, I SSH into my LAN server using the server's IP address.

    ssh server-IP

I attach to my Server tmux environment. Using already a Local tmux, inside Server tmux I have to use the prefix twice `Ctrl+a Ctrl+a` before any binding.

Then I pull the changes and publish the blog.

    git pull
    make html && make publish

I am having a problem here. I usually review the changes before publishing with `make serve`. However, using this command runs the engine on the Server and not on Local. I am not able to browse the server localhost on local. I also cannot open the output html with `google-chrome filename.html`, because it tries to open the file on Server and not on Local.

For now I have to trust that Mr Hyde's draft has the correct markdown syntax.

## Publishing the blog

Once I generate the static pages, I just follow my usual process. Push the HTML output.

    cd output
    git add .
    git commit -m "new post by Hyde"
    git push -u origin master

Then push the source.

    cd ..
    git add .
    git commit -m "new post by Hyde"
    git push -u origin master


