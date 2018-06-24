Title: Cpp Indent Vim
Date: 2018-06-24 18:00
Category: Coding
Tags: coding, linux, fedora, c++
Slug: cpp-indent-vim
Author: Tom Ordonez
Status: published
Summary: How to indent C++ files in Vim

Given `.vimrc`:

    filetype plugin indent on

To indent C++ files in Vim. Create this directory:

    ~/.vim/after/ftplugin/

Inside that directory create the file:

    ~/.vim/after/ftplugin/cpp.vim

Add the lines:

    set expandtab
    set shiftwidth=2
    set softtabstop=2

That's using 2 spaces for indentation like they do it at Google.

When you create a file:

    vim awesome.cpp

It will indent to 2 spaces:

    #include <iostream>
    using namespace std;

    int main()
    {
      cout << "2 spaces" << endl;
      return 0;
    }