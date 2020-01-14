Title: Python Jupyter Notebook in Linux
Date: 2020-01-14 18:30
Category: Python
Tags: python, jupyter, linux
Slug: python-jupyter-notebook-linux
Author: Tom Ordonez
Status: published
Summary: Setting up Python Jupyter Notebook in Linux

First, follow this to [install Miniconda on Linux](https://www.tomordonez.com/install-miniconda-linux.html).

Update conda

    $ conda update conda

Create a `yml` file, use a name and dependencies. Example:

File: `env_py_3.7.6.yml`

Contents of this file:

    name: awesome_name
    dependencies:
    - python=3.7.6
    - jupyter

Create the environment using this file:

    $ conda env create --file env_py_3.7.6.yml
    $ conda activate awesome_name

Check Python version

    $ which python
    $ python -V

Run Jupyter Notebook:

    $ jupyter notebook

If this doesn't work. Try it like this:

    $ jupyter notebook --ip=127.0.0.1
