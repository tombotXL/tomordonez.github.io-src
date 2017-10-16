Title: Redirect stdout and stderr in bash
Date: 2017-09-14 18:00
Category: Linux
Tags: linux, bash, stdout, stderr
Slug: redirect-stdout-stderr-bash
Author: Tom Ordonez
Status: published
Summary: This is how to redirect stdout and stderr in bash

This is how to redirect stdout and stderr in bash.

![Redirect stdout and stderr in bash]({filename}/images/redirect-stdout-stderr-bash.png)

Search for:

* IO redirection in Linux
* input redirection Linux
* output redirection Linux
* file descriptors bash

As seen <a href="http://tldp.org/LDP/abs/html/io-redirection.html" target="_blank">here</a>.

Redirect stdout to file "filename."

    1>filename

Redirect and append stdout to file "filename."

    1>>filename

Redirect stderr to file "filename."

    2>filename

Redirect and append stderr to file "filename."

    2>>filename

Redirect both stdout and stderr to file "filename."

    &>filename
    
Redirect stderr to stdout.

    2>&1


## If you have questions or comments please add them below

![Ask Question or Comment]({filename}/images/tomordonez-ask-question-comment.gif)
