Title: Python Context Manager
Date: 2018-10-09 22:00
Category: Coding
Tags: coding, linux, python
Slug: python-context-manager
Author: Tom Ordonez
Status: published
Summary: A short tutorial about Python context manager: "with" statement.

A short tutorial about Python context manager: "with" statement.

![Python Context Manager]({filename}/images/python-context-manager.jpg)

Sources:

* This <a href="http://arnavk.com/posts/python-context-managers/" target="_blank">blog post</a> about context managers.
* The Python <a href="https://docs.python.org/3/library/stdtypes.html#typecontextmanager" target="_blank">docs</a>.

Here is a popular example:

    import csv

    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

The context manager `with` is used for allocation and releasing of resources.

This is alternative to doing this:

    import csv

    csvfile = open('output.csv', 'w', newline='')
    csvwriter = csv.writer(csvfile)
    csvfile.close()

Which is also similar to:

    import csv

    csvfile = open('output.csv', 'w', newline='')
    
    try:
        csvwriter = csv.writer(csvfile)
    finally:
        csvfile.close()

The blog post from the sources list has a good example:

    setup()
    try:
        do_something()
    finally:
        teardown()

Similar to:

    contextmanager.__enter__()
    try:
        do_something()
    finally:
        contextmanager.__exit__()

## Context Manager protocol

The context manager protocol follows two methods:

* `__enter__`
* `__exit__`

As seen in the Python docs. It "defines a runtime context that is entered before the statement body is executed and exited when the statement ends".

Following the same example:

    import csv

    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

For `contextmanager.__enter__()`:

* It returns an object assigned to the variable `csvfile` after `as`

For `contextmanager.__exit__()`:

* Exits the runtime context.
* Returns a boolean flag indicating if an exception should be supressed.

Get more details <a href="https://docs.python.org/3/library/stdtypes.html#typecontextmanager" target="_blank">here</a>.