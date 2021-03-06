Title: Bash Script Tutorial
Date: 2017-09-03 18:00
Category: Linux
Tags: linux, bash, scripts, vim
Slug: bash-script-tutorial
Author: Tom Ordonez
Status: published
Summary: In this bash script tutorial you will learn the basics to create bash scripts.

In this bash script tutorial you will learn the basics to create bash scripts.

![Bash Script Tutorial]({filename}/images/bash-script-tutorial.jpg)

## Bash Script Environment

In this bash script tutorial I am using Linux. But you can also use a Mac and perhaps Windows.

## Bash Script Linux

My preference is creating bash scripts in Linux. Although I have the feeling that if you are in Linux you already know some Bash :)

If you are not using Bash. Maybe you know some Linux commands? If not no problem. First find where `bash` is installed in your system.

Open the terminal and type:

    which $BASH

It might say:

    /bin/bash

If you are on Mac it might say:

    /usr/local/bin/bash

Keep this in mind for later.

## Vim Text Editor

I love Vim because it has a mouse free environment and helps you become hyperfocused. Although Vim has kind of a steep learning curve.

Installing Vim on Ubuntu Linux:

    sudo apt install vim

Installing Vim on Fedora Linux:

    sudo dnf install vim

Installing Vim on Mac:

    brew install vim

Although keep in mind that for the Mac to use `brew` you need to install `homebrew`. Just go to <a href="https://brew.sh" target="_blank">Homebrew</a> and copy paste the command shown on the homepage into the terminal.

## Sublime Text Editor

Sublime is less geek and it looks just like any program. You can download it from <a href="https://www.sublimetext.com/3" target="_blank">here</a>.

## Bash Script Windows

What I recommend is to install Linux using Virtualbox. A video will soon be posted here.

## Bash Script Basics

Create a new file either and save it as `awesome-file.sh`. Yeah it ends with `.sh`.

In the first line type in the location of bash.

For Linux bin bash is often:

    #!/bin/bash

For Mac bin bash is often:

    #!/usr/local/bin/bash

The character `#!` is called a `shebang` or a `hashbang`.

What follows the `shebang` is the location of bash binaries. In other words it tells the file what you want to execute the file with Bash.

## Bash script simple silly example

It's downhill from here :)

Below the bin bash line enter a new line and add this line:

    echo "Hello"

With bin bash on Linux:

    #!/bin/bash
    echo "Hello"

Or with bin bash on Mac:

    #!/usr/local/bin/bash
    echo "Hello"

Save and close the file.

## Change the bash script file to execute

Go back to the terminal and change directories to where the file is.

Type this command to make the bash script executable:

    chmod +x awesome-file.sh

## Execute this simple silly bash script example

On the terminal type this to execute this bash script example:

    ./awesome-file.sh

This means to execute in the current directory.

The result should be:

    Hola

## These are other advanced examples

How to declare variables and initialize some to zero.

    declare -i filenumber=0
    declare -i sponsornumber=0
    declare -i counter=0
    declare -i directory_size

## Assign a string to a variable

    filetype=".jpg"

## Calculate the directory size where the files are stored

    directory_size="$(ls -l ./ | grep 'jpg' | wc -l)"

## Rename files in the directory to a random number

    for file in *.jpg; do
      number="$RANDOM"
      mv "$file" "$number$filetype"
    done

## Use a random number within a range

Random number from 1 to 10:

    number="$(((RANDOM % 10) + 1))"

Random number from 1 to 100:

    number="$(((RANDOM % 100) + 1))"

## Rename files into a sequential number 1, 2, 3...etc

    for file in *.jpg; do
      filenumber="$(($filenumber + 1))"
      mv "$file" "$filenumber$filetype"
    done

## Insert files at intervals in current directory

Copy files in this sequence: 2, 8, 14...etc.
The sequence requires the algorithm: `2 + (6 * n)
The files are copied like this: 2a, 8a, 14a.

    while [ $counter -lt $directory_size ]; do
      sponsornumber="$(((6 * $counter) + 2))"
      cp sponsor_directory/sponsor_file.jpg "$sponsornumber"a"$filetype"
      counter="$(($counter + 1))"
    done

## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
