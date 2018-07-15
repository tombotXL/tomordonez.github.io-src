Title: Install a Plugin in Vim
Date: 2018-07-14 20:00
Category: Coding
Tags: coding, linux, vim
Slug: install-plugin-vim
Author: Tom Ordonez
Status: published
Summary: How to install a plugin in Vim

A short one on how to *install a plugin in Vim*.

Install `Vundle`. More details <a href="https://github.com/VundleVim/Vundle.vim" target="_blank">here</a>.

    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Edit the `.vimrc` file and add these lines:

    set nocompatible
    filetype off
    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required

This is how I **install Vim plugins**:

1. Go to a plugin that says you can install using `Vundle`.
2. For instance. This plugin auto saves when you are editing a file: <a href="https://github.com/907th/vim-auto-save" target="_blank">auto-save</a>.
3. The Github project should have a directory called `plugin`.
4. Add the `user/project` from Github to your `.vimrc` file. In the `auto-save` example. The user is `907th` and the project is `vim-auto-save`. I will add this line to my `.vimrc` file: `Plugin 907th/vim-auto-save` before a specific line as noted above.
5. Save `vimrc`. Source it with `:so %`.
6. List all `Vundle` plugins. Still inside Vim: `:PluginList`. Make sure the Plugin is listed. You can do `:q` to exit this view.
7. Inside Vim: `:PluginInstall`. This will install recently added Plugins.

This particular `Plugin` for `auto-save` had a few more lines that had to be added. Depending on the `Plugin` readme page, please follow those specific instructions.

For `auto-save`. You need to add these lines to the `.vimrc` file:

    let g:auto_save = 1
    let g:auto_save_in_insert_mode = 0

Here is a list of `Vim` plugins:

    http://vim-scripts.org/vim/scripts.html

<form style="border:1px solid #ccc;padding:3px;text-align:center;" action="https://tinyletter.com/tomordonez" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/tomordonez', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><h2><label for="tlemail">Tom's Data Science Quest</label></h2><p>I am doing a MS in Computer Science at Georgia Tech with a focus in Machine Learning. I am writing a weekly newsletter about my lessons learned. Follow my quest to conquer data science.</p><p><input type="text" style="width:140px" name="email" id="tlemail" value placeholder=" tony@stark.com" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>