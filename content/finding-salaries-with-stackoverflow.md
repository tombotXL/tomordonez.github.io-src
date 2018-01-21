Title: Finding Salaries With StackOverflow
Date: 2018-01-19 18:00
Category: Recruiting
Tags: recruiting, sourcing, stackoverflow
Slug: finding-salaries-with-stackoverflow
Author: Tom Ordonez
Status: published
Summary: Finding salaries with StackOverflow using their salary calculator or their Kaggle dataset.

Finding salaries with StackOverflow using their salary calculator or their Kaggle dataset.

<p>&nbsp;</p>
![Finding Salaries With StackOverflow]({filename}/images/finding-salaries-with-stackoverflow.jpg)
<p>&nbsp;</p>

This is what you need:

* A Kaggle account
* Analytical skills
* Coffee

These are some US states and cities where the salary question has been banned:

* Oregon
* California
* Massachusetts
* New Orleans
* New York City
* Philadelphia
* Pittsburgh
* Puerto Rico

## StackOverflow to the rescue

Maybe you have a few sources where to get stats for salaries but StackOverflow has an awesome tool to get salary stats.

The tool is based on their annual developer survey and it has the following fields:

* Role
* Location
* Education
* Years of experience
* Technologies

<p>&nbsp;</p>
![StackOverflow Salary Calculator]({filename}/images/stackoverflow-salary-calculator.jpg)
<p>&nbsp;</p>

For Role, you can select from the following:

* Backend Developer
* Data Scientist
* Database Administrator
* Designer
* Desktop Developer
* DevOps
* Embedded Developer
* Frontend Developer
* Full Stack Developer
* Graphics/Game Developer
* Mobile Developer
* QA/Test Developer
* System Administrator

For Location, you can type any city in the US.

For Education, you can select from the following:

* Less than a bachelors
* Bachelors degree
* Graduate degree
* Post-grad degree

For years of experience you can select from 0-20.

For technologies you can type any tech keyword.

## Salary Dataset from Kaggle

The StackOverflow salary calculator is a great tool to get all sorts of combinations.

If you want to analyze a larger dataset, you should get the data from Kaggle.

<p>&nbsp;</p>
![StackOverflow Salary Kaggle]({filename}/images/stackoverflow-salary-kaggle.jpg)
<p>&nbsp;</p>

These are some details about this dataset:

The column "Professional" has this data:

* Student
* Professional developer
* Professional non-developer who sometimes writes code
* Used to be a professional developer

The column "EmploymentStatus" has this data:

* Not employed, and not looking for work
* Employed part-time
* Employed full-time
* Independent contractor, freelancer, or self-employed

A few other columns are:

* CompanySize
* CompanyType
* WebDeveloperType
* MobileDeveloperType
* JobSeekingStatus
* Salary
* ExpectedSalary

## What to do with this data

This dataset has more than 65K records and it's about 12MB in size.

It's not a great idea to open this file in Excel.

If you have some Python skills you could open this there.

Or you could open it using Tableau and make some plots.

Looking at one of the discussions. Someone did an exploratory data analysis to get some general stats.

As seen <a href="https://www.kaggle.com/asindico/exploratory-analysis" target="_blank">here</a>.

The majority of records are from US, India and UK

<p>&nbsp;</p>
![StackOverflow Salary Kaggle Country]({filename}/images/stackoverflow-salary-kaggle-country.jpg)
<p>&nbsp;</p>

The top programming languages are Javascript, Java, C#, Python, PHP

<p>&nbsp;</p>
![StackOverflow Salary Kaggle Languages]({filename}/images/stackoverflow-salary-kaggle-languages.jpg)
<p>&nbsp;</p>

## StackOverflow Survey Results

StackOverflow has a detailed analysis of this dataset.

<p>&nbsp;</p>
![StackOverflow Survey Results]({filename}/images/stackoverflow-survey-results.jpg)
<p>&nbsp;</p>

What I recommend is writing down questions about things that you are looking for.

For instance I would be interested on these questions:

* How many hispanic people in the US are programmers that know Python
* How many of those are men and women
* What are their salary expectations
* How many of them are professional developers
* How many have a PhD
* What is their company type
* What is their job satisfaction

There are a lot of interesting results you can get from this data.

## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.
