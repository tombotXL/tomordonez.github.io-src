Title: How to Reload Tmuxinator
Date: 2018-08-29 22:00
Category: Coding
Tags: coding, linux, tmux, tmuxinator
Slug: reload-tmuxinator
Author: Tom Ordonez
Status: published
Summary: How to Reload Tmuxinator

This is how I reload Tmuxinator if I want to change my dashboard without having to exit all the panes.

Edit the `yml` Tmuxinator config project file:

    $ tmuxinator open your-project

Save the config file and close.

Stop the project session:

    $ tmuxinator stop your-project

Then start the project again:

    $ tmuxinator your-project

Now the session is reloaded with the new config changes.