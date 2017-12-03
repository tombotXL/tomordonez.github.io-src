Title: Regex Remove Lines Not Containing a Character
Date: 2017-12-03 9:00
Category: Coding
Tags: regex, remove lines, linux
Slug: regex-remove-lines-not-containing-character
Author: Tom Ordonez
Status: published
Summary: Use this regex pattern to remove lines not containing a character.

Use this regex pattern to remove lines not containing a character.

I want to remove lines that don't contain a space.
    
    ^(?!.* .*).+$

Or remove lines that don't contain numbers.
    
    ^(?!.*[0-9].*).+$

Or remove lines that don't contain UPPER CASE.
    
    ^(?!.*[A-Z].*).+$

Or remove lines that don't contain letters
    
    ^(?!.*[A-Za-z].*).+$

Or remove lines that don't contain an email
    
    ^(?!.*@.*).+$

## Got a Regex question? Please comment below