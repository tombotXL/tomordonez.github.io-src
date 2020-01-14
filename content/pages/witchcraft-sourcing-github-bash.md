Title: Witchcraft Sourcing with Github and Bash
Author: Tom Ordonez
Status: hidden
Slug: witchcraft-sourcing-github-bash
Summary: I will be presenting at Sourcecon in Austin about sourcing using Bash, Ruby, Python and R.

I will be presenting at Sourcecon in Austin about sourcing using Bash, Ruby, Python and R.

Feel free to say hi if you see me around or let's hangout.

You can also connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>.
<p>&nbsp;</p>

![Tom Ordonez at Sourcecon]({static}/images/tomordonez-sourcecon-2017.jpg)

<p>&nbsp;</p>
<p>&nbsp;</p>
## Check it out on Wednesday, September 27 • 2:25pm - 3:00pm under the Programmers track
<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/tomordonez-witchcraft-sourcing-sourcecon.jpg)

## This is a preview of witchcraft sourcing with Github and Bash

What you will learn from this awesome story:

* Create a CSV file from Github profiles
* Collect location, email, website for each

This is a preview of what the CSV looks like:
<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-csv-details.jpg)

## Crash Course using the Terminal

If you want to talk to the computer you need to know some Linux commands.

These work on Linux and OSX. In Windows they are slightly different.

List all files and directories:

    $ ls

What is the current directory?

    $ pwd

Create a new directory called "awesome":

    $ mkdir awesome

Change to that directory

    $ cd awesome

Create a file using the "touch" command:

    $ touch file1.txt

Create and open a file using the editor "Vim":

    $ vim file2.txt

Use the pipe symbol `|` to send the output of a command to the input of another one.

    $ ps aux | grep "chrome"

It creates a list of all processes running in the computer, it sends this list (the output), to the input of the command "grep" to filter by the process name "chrome".

Use one greater than symbol `>` to add the output to a file

    $ ps aux | grep "chrome" > process.txt

Use two greater than symbol `>>` to append the output to a file

    $ ps aux | grep "firefox" >> process.txt

## Create a simple Bash script

    $ touch sample-script.sh

Open with your favorite text editor. In my case Vim:

    $ vim sample-script.sh

Add this to the file:

    #!/usr/bin/bash
    ps aux | grep "chrome" > browsers.txt
    printf "I will sleep for 10 seconds\n"
    sleep 10
    ps aux | grep "firefox" >> browsers.txt
    printf "Everything is awesome\n"

Save and close the file.

Change the file mode to become executable:

    $ chmod +x sample-script.sh

Run the script:

    $ ./sample-script.sh
    I will sleep for 10 seconds
    Everything is awesome

It will create a file called "browsers.txt" with computer processes, then filtered by "chrome" and "firefox" data.

## Go to a Github project

For example: Airbnb/Javascript
<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-airbnb-js.jpg)

Create a list of all contributors and add them to a file called `input.txt`.

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-input.jpg)

Create a Bash script called `awesome.sh` and add this:

    #!/usr/bin/bash
    while read -r line
    do
        wget --user-agent="Mozilla/5.0 (Windows NT 6.1)
        AppleWebKit/537.36 (KHTML, like Gecko) 
        Chrome/41.0.2228.0 Safari/537.36" -O - "$line"
        | pcregrep -M 'vcard-fullname d-block.*\n.*
        vcard-username d-block.*\n(.*\n){1,}.*
        aria-label="Home location".*\n.*aria-label=
        "Email".*\n.*aria-label="Blog or website"
        .*\n.*aria-label="Member since".*' >> output.txt
      sleep 10
    done < "$1"

This will take each Github profle from `input.txt` and download a section of the HTML. Then add this output to the file `output.txt`.

Run the file like this:

    $ ./awesome.sh input.txt

## Open the Output file

This file has HTML code.

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output.jpg)

## Cleaning the HTML file

Use regular expressions to convert the HTML file into a CSV file.

Regular expressions is a way to find patterns of data.

Download the editor `Sublime Text` to do this operation.

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex1.jpg)

Use the shortcut `Ctrl+H` to open Search and Replace.

Enable the buttons for `regular expressions` and `case sensitive`.

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex2.jpg)

Replace commas with semicolons. Otherwise you will go insane trying to put the commas in the CSV. Therefore called comma separated values :)

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex3.jpg)

Remove all blank space from the beginning of each line:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex4.jpg)

Find the pattern where each Github profile starts and ends.

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex5.jpg)

Remove new lines to move all lines into a single line

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex6.jpg)

It looks like this now:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex7.jpg)

Break the lines with the pattern you found where a profile ends and the other starts:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex8.jpg)

It looks like this now:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-regex9.jpg)

A few more replacements and the data will look like this:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-clean-csv.jpg)

## Those are not emails

Before you feel like I ripped you off...hold on a second...be happy :)

The emails are encoded.

Guess what!

We are going to decode them :)

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-quit.gif)

Please don't quit just yet we are almost there.

## Decoding emails using Bash

Create a new file called `decode.sh`

In this file add this:

    #!/usr/bin/bash
    while read -r line
    do
      echo -e "$line" >> tengo-hambre.txt
    done < "$1"

Set the file to execute:

    $ chmod +x decode.sh

Create a new input file with only one column with the encoded emails. Call this file `tacosconcarne.txt`.

Now run the script like this:

    $ ./decode.sh tacosconcarne.txt

Now open the output file `tengo-hambre.txt`.

You will get a file with emails:

<p>&nbsp;</p>

![Witchcraft Sourcing at Sourcecon]({static}/images/github-sourcing-tomordonez-profiles-output-emails.jpg)

## Connect with me on <a href="https://www.linkedin.com/in/tomordonez/" target="_blank">Linkedin</a>
![Find me on Linkedin Tom Ordonez]({static}/images/contact-tomordonez-linkedin.gif)
