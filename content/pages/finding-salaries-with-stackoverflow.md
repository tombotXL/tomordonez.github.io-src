Title: Finding Salaries With StackOverflow
Author: Tom Ordonez
Status: hidden
Slug: finding-salaries-with-stackoverflow
Summary: Finding salaries with StackOverflow using their salary calculator or use their Kaggle dataset to get insights.

Finding salaries with StackOverflow using their salary calculator or use their Kaggle dataset to get insights.

<p>&nbsp;</p>
![Finding Salaries With StackOverflow]({filename}/images/finding-salaries-with-stackoverflow.jpg)
<p>&nbsp;</p>

As more states ban salary-related questions there is an increased need for finding salary data. There are a few sources where to get this data:

* Salary.com
* Glassdoor
* Indeed
* Linkedin
* Payscale

## Salary data from Salary.com

Salary.com has an interesting search box that says "What are you worth?".

I used my favorite example:

Search for "data scientist" in Chicago.

But the result shows 2 ads, followed by a few titles and checkboxes to compare the results:

* Data Scientist
* Data Architect III
* Data Warehouse Specialist

If you know a little bit about data science you will know that comparing these results is sort of like comparing an electric guitar and an electric bass. They look similar but they don't do the same thing.

## Salary data from Glassdoor

Glassdoor has a similar search box but this one says "Search salaries and compensation".

A search for "data scientist" in Chicago gets to the point. The result shows:

* Average base pay
* Additional compensation
* A range from low to high
* A list of salaries by company

The source of data says that it comes from users that listed their salary for their company or that opted not to share their company name. Although is not clear how many data points were used to calculate the average base pay.

## Salary data from Indeed

Indeed has a simpler search box that says "Search and compare salaries". You can only enter a job title and there is no field for entering a location.

Indeed also gets to the point. But the salary result for "data scientist" is much higher.

The result now shows a drop down to select a location. I select Chicago. The average pay changed but it's still higher than the result from Glassdoor.

The source of data says that it comes from 1,657 employees, users and past and present job ads in the past 24 months.

## Salary data from Linkedin

Linkedin has a search box that says "Discover your earning potential". I like this tagline. You can search by job title and location.

The same search for "data scientist" and Chicago shows a salary result similar to Glassdoor.

Although to get details, it asks you to login to see insights.

The source of data says that it comes from Linkedin members to compute salary insights in aggregate for a given title and region. Although I am not sure where Linkedin would ask this. I don't remember anywhere in my profile the option to submit a salary to Linkedin.

We are going to skip Payscale. You have to go through too many hoops to get any salary data.

## These are some US states and cities where the salary question has been banned:

* Oregon
* California
* Massachusetts
* New Orleans
* New York City
* Philadelphia
* Pittsburgh
* Puerto Rico

I bet that more states will be added to the list. As a recruiter/sourcer/hiring manager there will be a greater need to rely on accurate salary data sources.

I bet that you can get salary data sets from Glassdoor or Indeed using their API. Which might cost money. I am not sure yet.

## Big data salary

What would you do with a salary data set? Thousands and thousands of salary data points. This data could provide some interesting insights.

But not only salary. What about demographics, education, experience, etc.

I would like to get an answer for this question:

"What are the salary expectations for a data scientist that knows Python and who is Hispanic and that has a PhD with 2+ years of experience and living in the US".

Powerful insights!

There is a Big Data dataset like that.

Hello StackOverflow.

And it's free to download :)

## This is what you need:

* A Kaggle account
* Analytical skills
* Coffee

## StackOverflow to the rescue

StackOverflow has an awesome tool to get salary stats. Which is similar to Glassdoor and Indeed, although with a few more options.

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

Looking at one of the discussions. Someone did an exploratory data analysis to get some general stats. As seen <a href="https://www.kaggle.com/asindico/exploratory-analysis" target="_blank">here</a>. The majority of records are from US, India and UK.

The top programming languages are Javascript, Java, C#, Python, PHP

<p>&nbsp;</p>
![StackOverflow Salary Kaggle Languages]({filename}/images/stackoverflow-salary-kaggle-languages.jpg)
<p>&nbsp;</p>


StackOverflow has a detailed analysis of this dataset but you can also analyze the data and get insights that matter to you.

## Next steps

What I recommend is writing down questions about things that you are looking for.

For instance I would be interested on these questions:

* How many hispanic people in the US are programmers that know Python
* How many of those are men and women
* What are their salary expectations
* How many of them are professional developers
* How many have a PhD
* What is their company type
* What is their job satisfaction

There are a lot of interesting results you can get from the StackOverflow data set.

## Got questions or comments?

* Read more awesome stories at <a href="https://www.tomordonez.com/" target="_blank">Tom Ordonez</a>.
* Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.
