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

Let's write a silly program that asks for the prices of items and calculate the total, the lowest and highest price.

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

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>