Title: Execute a Script in a Different Directory in Linux
Date: 2017-09-12 18:00
Category: Linux
Tags: linux, shell
Slug: execute-script-different-directory-linux
Author: Tom Ordonez
Status: published
Summary: Follow this to execute a script in a different directory in Linux.

Follow this to execute a script in a different directory in Linux.

![Execute a Script in a Different Directory in Linux]({filename}/images/execute-script-different-directory-linux.jpg)

I had a script in `~/Documents/scripts/awesome-script.sh` and wanted to run it inside a different directory `~/Documents/images/awesome-images/`.

## The Subshell

You can use parentheses to create a subshell. Once the command is completed, the subshell will close, such as...

    $ (cd ~/Documents/images/awesome-images/ && ~/Documents/scripts/awesome-script.sh)

This is how it works:

* Use parentheses to create a subshell
* `cd` into `~/Documents/images/awesome-images/`
* If this command is successful then
* Execute the script located in `~/Documents/scripts/awesome-script.sh`
* When this command is executed. Close the subshell

## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
