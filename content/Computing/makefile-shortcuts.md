---
title: 'Take five minutes to simplify your life with <em>Make</em>'
date: 2016-06-14 12:00
modified: 2016-06-15 18:20
tags: make, pipelines, bioinformatics, protips, git, venv, python
...

I use _GNU Make_ to automate my data processing pipelines.
I've written a [tutorial][bjs-tutorial] [^shorter-tutorials] for novices on the
basics of using _Make_ for reproducible analysis and I think that everyone who
writes more than one script, or runs more than one shell command to process
their data can benefit from automating that process.
[I'm][kbroman-tutorial] [not][bostock-tutorial]
[alone][zmjones-tutorial].

[bjs-tutorial]: make-analysis.html
[zmjones-tutorial]: http://zmjones.com/make/
[bostock-tutorial]: https://bost.ocks.org/mike/make/
[kbroman-tutorial]: http://kbroman.org/minimal_make/

[^shorter-tutorials]: My tutorial is designed to fill a three hour
        Software Carpentry lesson.  There are a number of much shorter
        primers to get you started (e.g. [#1][zmjones-tutorial],
        [#2][bostock-tutorial], [#3][kbroman-tutorial]).

However, the investment required to learn _Make_ and to convert an
entire project can seem daunting to many time-strapped researchers.
Even if you aren't
living the dream—rebuilding
a paper from raw data with a single invocation of
`make paper`—I still
think you can benefit from adding a simple `Makefile` to your project root.

When done right, scripting the tedious parts of your job _can_
save you time in the long run[^xkcd-refs].
But the time savings aren't the only reason to do it.
For me, a bigger advantage is that I get to save my mental energy for
more interesting problems[^cook-ref].
_Make_ goes a step further and lets me forget about everything but my
real objective.
With a `make [target]` invocation I don't even need to remember the name of the
script.

[^xkcd-refs]: Randall Munroe does not agree.
        Relevant XKCDs: [#1][xkcd-worth-it],
        [#2][xkcd-automation], and [#3][xkcd-long-run]

[^cook-ref]: John Cook makes [this argument][cook-automate] on his blog.

[xkcd-worth-it]: https://xkcd.com/1205/
[xkcd-automation]: https://xkcd.com/1319/
[xkcd-long-run]: https://xkcd.com/974/
[cook-automate]: http://www.johndcook.com/blog/2015/12/22/automate-to-save-mental-energy-not-time/


## The default makefile ##

TL;DR: All of the code in this post is available as a [gist][all-files-gist].

[all-files-gist]: https://gist.github.com/bsmith89/c6811893c1cbd2a72cc1d144a197bef2

Here's what a minimal makefile might look like:

```makefile

define PROJECT_HELP_MSG

Usage:
    make help                   show this message
    make clean                  remove intermediate files (see CLEANUP)

    make ${VENV}                make a virtualenv in the base directory (see VENV)
    make python-reqs            install python packages in requirements.pip
    make git-config             set local git configuration
    make setup                  git init; make python-reqs git-config

    make start-jupyter          launch a jupyter server from the local virtualenv
    make start-ipython          launch ipython from the local virtualenv

endef
export PROJECT_HELP_MSG

help:
	echo $$PROJECT_HELP_MSG | less

.git:
	git init

git-config: | .git 
	git config --local filter.dropoutput_jupyter.clean \
        drop_jupyter_output.sh
	git config --local filter.dropoutput_jupyter.smudge cat
	git config --local core.page 'less -x4'
	git config --local diff.daff-csv.command "daff.py diff --git"
	git config --local merge.daff-csv.name "daff.py tabular merge"
	git config --local merge.daff-csv.driver "daff.py merge --output %A %O %A %B"

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

${VENV}:
	python3 -m venv $@

python-reqs: requirements.pip | ${VENV}
	pip install --upgrade -r requirements.pip

setup: ${VENV} python-reqs git-config | .git

start-jupyter:
	jupyter notebook --config=jupyter_notebook_config.py

CLEANUP = *.pyc

clean:
	rm -rf ${CLEANUP}

.PHONY: help git-config start-jupter python-reqs setup clean

```

If you want to start using it right away, download the [gist][all-files-gist],
which includes a couple of other necessary files.
As long as you aren't saving it over another makefile, it won't mess anything
up.

But let's break it down so you can see how it's made and why it's awesome.

From the top!


## A help message for your project ##

```makefile

define PROJECT_HELP_MSG

Usage:
    make help                   show this message
    make clean                  remove intermediate files (see CLEANUP)

    make git-config             set local git configuration
    make ${VENV}                make a virtualenv in the base directory (see VENV)
    make python-reqs            install python packages in requirements.pip
    make setup                  git init; make python-reqs git-config

    make start-jupyter          launch a jupyter server from the local virtualenv
    make start-ipython          launch ipython from the local virtualenv

endef
export PROJECT_HELP_MSG

help:
	echo $$PROJECT_HELP_MSG

```

The top of our makefile is a help message.
Running the traditional invocation `make help` will call that recipe and we'll
see an abridged list of the available recipes printed to our terminal.
Since `help` is the very first recipe in the makefile, it will also be the
default recipe;
typing `make` alone prints the help message.

As you start adding additional recipes, fill out this usage message.
That way you'll have both documentation about the analysis targets, and also
a handy cheatsheet.

_Edit (2016-06-15):_ [On Reddit, /r/guepier][guepier-comment] suggests using a
nifty trick to auto-generate these help messages,
keeping documentation and recipes together in your makefile.

[guepier-comment]: https://www.reddit.com/r/bioinformatics/comments/4o7aaa/a_simple_makefile_to_make_your_life_simple_xpost/d4aa8ir

## Streamline git setup ##

```makefile
.git:
	git init

```

Every project should be [version controlled][ram2013].
I prefer git, but the makefile can probably be adapted for Mercurial,
Subversion, darcs, etc.
This recipe is so simple as to appear useless (since `make .git` is no easier
to type than `git init`) but we use the directory `.git/` as an
[order-only prerequisite][man-order-only]
for the next recipe:

[ram2013]: https://dx.doi.org/10.1186/1751-0473-8-7
[man-order-only]: https://www.gnu.org/software/make/manual/html_node/Prerequisite-Types.html

```makefile
git-config: | .git 
	git config --local filter.dropoutput_jupyter.clean \
        drop_jupyter_output.sh
	git config --local filter.dropoutput_jupyter.smudge cat
	git config --local core.page 'less -x4'
	git config --local \
        diff.daff-csv.command "daff.py diff --git"
	git config --local \
        merge.daff-csv.name "daff.py tabular merge"
	git config --local \
        merge.daff-csv.driver "daff.py merge --output %A %O %A %B"

```

Git configuration is _just_ annoying enough that I often put it off for a new
project.
With this recipe I don't have to!

There are three parts to the configuration above;
customize it for how you use git.


### Drop Jupyter Notebook output ###

```bash
git config --local filter.dropoutput_jupyter.clean \
    ./drop_jupyter_output.sh
git config --local filter.dropoutput_jupyter.smudge cat

```

I set up a [clean/smudge filter][git-filters] for my Jupyter notebooks.
Outputs of analysis should generally not be version controlled,
and this includes those outputs that are inlined in a Jupyter notebook.
Now, when you `git add` and `git diff` notebooks, the output from cells will
be automatically ignored.
Thankfully, using this filter won't change the contents of the `.ipynb` file
itself, just the contents of the diff.
This does mean, however, that when you `git checkout` an old version of your
notebook you'll have to re-execute all of the cells to get the results.

[git-filters]: https://git-scm.com/book/en/v2/Customizing-Git-Git-Attributes

Two other files are needed for this configuration to have any effect.
First, `.gitattributes` which is a tab-separated file mapping filename patterns
to special git configuration.
The first line in that file should be the following.

```
*.ipynb	filter=dropoutput_jupyter

```

(That's a tab after `*.ipynb`.)

The second file is the filter `drop_jupyter_output.sh`,
which needs to be executable.

```bash
#!/usr/bin/env bash
# run `chmod +x drop_jupyter_output.sh` to make it executable.

file=$(mktemp)
cat <&0 >$file
jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True \
    $file --stdout 2>/dev/null

```


### Display tabs as four spaces ###

I also configure `less` to show four spaces for tabs.
This makes `git diff`-ing my makefile much easier on the eyes.

```bash
git config --local core.page 'less -x4'

```


### Smart `diff`s for tabular data ###

Since git considers changes on a per-line basis, looking at
`diff`s of comma-delimited and tab-delimited files can get obnoxious.
The program [`daff`][daff-site] fixes this problem.

[daff-site]: http://paulfitz.github.io/daff/

We'll configure git to use `daff` for all tabular files.

```bash
git config --local \
    diff.daff-csv.command "daff.py diff --git"
git config --local \
    merge.daff-csv.name "daff.py tabular merge"
git config --local \
    merge.daff-csv.driver "daff.py merge --output %A %O %A %B"

```

Just like the output filter for Jupyter notebooks, we need to associate
this configuration with CSVs and TSVs in our `.gitattributes` file by adding
the following two lines.

```
*.[tc]sv diff=daff-csv
*.[tc]sv merge=daff-csv

```


## Automatic python virtual environments ##

There are plenty of [reasons][why-venv] to sandbox your python environments.
If you're like me and keep a separate virtual environment for every project,
you'll appreciate these recipes to automate creating them and updating
packages.

[why-venv]: https://www.davidfischer.name/2010/04/why-you-should-be-using-pip-and-virtualenv/

If you don't use python/pip, these recipes can be swapped out for other
sandboxing systems.

```makefile
VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export PATH := ${VIRTUAL_ENV}/bin:${PATH}

${VENV}:
	python3 -m venv $@

python-reqs: requirements.pip | ${VENV}
	pip install --upgrade -r requirements.pip

```

In the top block, we first set a variable `VENV` to be the location of our
virtual environment.
We then set `VIRTUAL_ENV` and prepend its `bin/` to our `PATH`.
By exporting these variables, all recipes run from this makefile will
use python packages and executables from the virtual environment.
We don't have to remember to `source .venv/bin/activate` first!

The next block is the recipe to initialize the virtual environment.
If you're not using Python 3 for your project you will have to edit this one.

And finally, a recipe to install and update all of the packages listed in
`requirements.pip`.
If you want to make a change to your python requirements, add it to
`requirements.pip` and re-run `make python-reqs`.

You can bootstrap other software installations similarly.
And, if you discipline yourself to make all changes to your execution
environment in this way, you'll have a permanently up-to-date record of your
system requirements.


## Single-command project setup ##

```makefile
setup: ${VENV} python-reqs git-config | .git

```

With this meta-target a simple `make setup` will have our new project
configured and ready to go.
This is particularly useful if you work on multiple machines:

```bash
git clone git@github.com:username/project.git
cd project
make setup

```

is all it takes to get up and running.


## Launch your tools without the hassle ##

I use Jupyter Notebook's a lot.
With this recipe (and the `PATH` we export above) I don't have to remember
to activate my virtual environment or invoke specific configuration files
when I launch a server.

```makefile
start-jupyter:
	jupyter notebook --config=jupyter_notebook_config.py

```

Put whatever you'd like into the [config file][jupyter-config].
I like to keep my notebooks in a subdirectory, so my invocation is a little different:

[jupyter-config]: http://jupyter-notebook.readthedocs.io/en/latest/config.html

```shell
jupyter notebook --config=ipynb/jupyter_notebook_config.py --notebook-dir=ipynb/

```

And my configuration automatically changes the working directory to
the project root when launching a new notebook.

Customize!
The same general idea works for any other software you can start from the shell
No need to remember any of the obnoxious command-line flags.


## Quick cleanup ##

```makefile
CLEANUP = *.pyc

clean:
	rm -rf ${CLEANUP}

```

A ubiquitous target for _Make_ is `clean` to tidy up the repository.
With this makefile, run `make clean` to remove all the `*.pyc` files.
Customize the `CLEANUP` variable with filenames and globs you find yourself
`rm`-ing repeatedly.
For me, this includes a bunch of `*.log` and `*.logfile` files.


## Fork this code! ##

That's all I've got for a default makefile.
And even this one is more complicated than it has to be;
any _one_ component from it can make your life easier when practicing
reproducible research.

The whole point is to hide as much of the humdrum stuff as you can so you get
to focus on what counts.
I've found this makefile saves me both time and, more importantly, mental
energy.

The `Makefile`, `.gitattributes`, `requirements.pip` and
`drop_jupyter_output.sh` described
here can all be downloaded from [this gist][all-files-gist][^bootstrap-idea].
Next time you're starting a project, download them to the project directory,
run `make setup`, and let me know what you think!

[^bootstrap-idea]: Even better, you could write a recipe to download those files
        on `make setup`!
