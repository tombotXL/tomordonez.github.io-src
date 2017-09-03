Title: Review of Programming for Everybody in Python from Coursera
Date: 2017-09-02 18:00
Category: Data Science
Tags: data science, coursera, python
Slug: review-programming-for-everybody-python-coursera
Author: Tom Ordonez
Status: published
Summary: This is a review of Programming for Everybody in Python from Coursera by University of Michigan

I have been on a data science quest on and off for about a year and a half.

About a month ago I decided to accelerate my progress and I signed up to Python for Everybody in Coursera.

I implemented some Python scripts in the past and this website uses Python. But I wanted to get some detailed foundations before moving on to using Python for data science.

The first course in the Python for Everybody path is called "Programming for Everybody (Getting Started with Python)".

It's the typical intro to programming.

They teach you basic syntax, types, conditionals and iterations.

They also teach you handling exceptions, which often is a more advanced topic but I am glad this was taught early on.

## Programming for Everybody in Python Curriculum

Here is the curriculum for programming for everybody in Python:

* Week 1: Why we program
* Week 2: Installing and using Python
* Week 3: Why we program (continued)
* Week 4: Variables and expressions
* Week 5: Conditional code
* Week 6: Functions
* Week 7: Loops and iteration

I completed this course in about a week. Spent around 3-4 hours per day for 7 days.

If you are familiar with C programming you can do this course in less than a week too.

If you know what this is, you will find this course very easy:

    for (i = 1; i <= 3; i++)

If you don't have previous knowledge of programming I suggest that you take each week and spend time to get the knowledge to sink in correctly in your brain :)

## Programming for Everybody in Python Example

Here is a Python example related to programming for everybody.

I have been buying a few things from <a href="https://www.shopyourway.com" target="_blank">Shop Your Way</a>.

Mostly related to tools for DIY things around the house.

A <a href="https://www.shopyourway.com/craftsman-home-series-26-wide-5-drawer-rolling-cabinet-red/323664575" target="_blank">Craftsman cabinet</a>. Which I am using to store my music and computer stuff.

![Software Craftsman-ship]({filename}/images/craftsman-cabinet-shopyourway.jpg)

I got a <a href="https://www.shopyourway.com/craftsman-30438-16-electric-corded-grass-trimmer/397281876" target="_blank">Craftsman electric trimmer</a> to cut the jungle-like grass from my patio.

![Craftsman Electric Trimmer]({filename}/images/craftsman-electric-trimmer-shopyourway.jpg)

When I used the trimmer I realized that it blew grass and sand really hard. Although I used sun glasses they were not good enough to protect my face. The machine also vibrated a lot. I guess I am not used to this kind of work :)

I got a few more things:

I got <a href="https://www.shopyourway.com/dewalt-router-safety-glass-with-clear-lens/156331544" target="_blank">safety glasses</a>.

And also <a href="https://www.shopyourway.com/craftsman-utility-gloves-large/21815380" target="_blank">utility gloves</a>.

Let's write a silly program that asks for the prices of these items and it calculates the total, the lowest and highest price.

Also print an error when you don't enter a number and finish when you enter the word "batman".

    lowest = None
    highest = None
    count = 0
    total = 0

    while True:
        price = input('Enter price: ')
	if price == 'batman'
	    break
	try:
	    price = float(price)

	 except:
	    print('Master Bruce please enter a number!')
	    continue
        
	total = total + price
	count = count + 1

	if highest is None or price > highest
	    highest = price
	if lowest is None or price < lowest
	    lowest = price

    print('Total is:', total)
    print('Number of items:', count)
    print('Highest price:', highest)
    print('Lowest price:', lowest)

Running the program shows:

![Programming for Everybody in Python from Coursera example]({filename}/images/programming-everybody-python-coursera.jpg)

The example uses all the lessons from the course with the exception of the for loop:

* while
* try and except
* if conditional
* input

## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
