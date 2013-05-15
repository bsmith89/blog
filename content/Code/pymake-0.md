Title: PyMake I: Another GNU Make Clone
Date: 2013-05-07 19:00
Tags: python, software, development, make, pipelines, bioinformatics
Slug: my-pipeline-is-not-a-makefile
Summary: In which I introduce the rationale for a little piece of software
         written by me.


_This is the first of two posts about my program
[PyMake](http://github.com/bsmith89/pymake/).  I'll post the link to Part II
here when I've written it._

I am an aspiring but unskilled (not yet skilled?) computer geek.
You can observe this for yourself by watching me fumble my way through
[`vim` configuration](https://github.com/bsmith89/dotfiles),
multi-threading/processing in Python, and `git` merges.

Rarely do I actually feel like my products are worth sharing with
the wider world.  The only reason I have a GitHub account is personal
convenience and absolute confidence that no one else will ever look at it
besides me.  (Yes, I realize that I am invalidating the previous sentence
with that glaring "Fork me on GitHub" ribbon in the top-right corner of
this page.  I'm putting myself out there!  OKAY?!)

As an aspiring scientist, too, I've had plenty of opportunities to practice
the relevant skill sets.  A laboratory rotation with
[Titus Brown](http://ivory.idyll.org/blog/), and the resulting exposure to his
reproducible research and [Software Carpentry](http://software-carpentry.org)
evangelizing, has certainly influenced the tools and techniques in my belt.

I try to use the `NumPy`/`SciPy`/`Pandas`/`matplotlib` stack for my
computational and visualization tasks.  I am a relatively competent `BASH`-ist
and I work hard to write my scripts so that they'll
make sense to me 5 years from now.  I have even been known to do some of my
data analysis in IPython notebooks.

# A Pipeline is only sometimes a Makefile

Despite (or maybe because of) my obsession with writing simple,
reproducible pipelines, one tool I have never come to terms with is
GNU `make`.  While it's not quite mainstream for bioinformaticians and
other computational folk, `make`
[promises](http://archive.nodalpoint.org/2007/03/18/a_pipeline_is_a_makefile)
to tie all those *`NIX` style
scripts together seamlessly and with built-in
parallelization, selective re-running, and more, all under a declarative
language syntax.  I say 'promises' because, for me, it never did any of those
things.

Now, I don't want to suggest that this ubiquitous piece of GNU software
doesn't work well.  I recognize that it does much of what the average
user needs, but for my particular pipeline it just wasn't the right tool.

My problem was a seemingly simple one.  I had a set of gene models (HMMs)
and a set of FASTQ formatted sequences from an Illumina
sequencer.  The goal was to search every sample for every gene using HMMER3
and to output the results (plus a respectable amount of pre- and
post-processing).  The problem is, `make` is designed for
software compilation. Processing `foo.c` and `bar.h` into `foo.o` is easy.
I, however, was asking `make` to generate the product of $n$ samples and $m$
models (**complete aside**: if you're curious about how I got the
$\LaTeX$ formatting, see
[this](http://www.ceremade.dauphine.fr/~amic/blog/mathjax-and-pelican-en.html)).

While, after a dozen hours of smashing my head against the table, I was able
to get my `Makefile` to work, it required some _really_ ugly tricks like
secondary expansion and gratuitous calls to `sed` in my macros (for others
with similar problems see [here](http://stackoverflow.com/q/3745177/848121),
and [here](http://stackoverflow.com/q/2880975/848121)).  Plus, debugging
`make` is torture, surely against the Geneva Conventions.

I _wanted_ to use `make`, I swear I did.  It's open source, well used,
extensively tested, available on all relevant systems, etc.
And I probably could have... but only by keeping the ugly hack or hard-coding
the recipe for each model, and that just didn't jive with my
recently acquired simple/reproducible mentality.  Converts always are
the most zealous, afterall.


# They say graduate school is a time to explore
So what did I do?  No, I didn't immediately start writing a make replacement
with all of the features I wanted like some over-eager graduate student.
Jeeze!  What do you people think of me!? First I checked out the
[extant alternatives](http://freecode.com/articles/make-alternatives)...
I hated everything.  So _then_ I started writing a make replacement with all
of the features I wanted.

The result was one of the first pieces of general purpose software to come
off my laptop which I wouldn't be entirely ashamed to show to an experienced
programmer.  It's rough, don't get me wrong, but it does everything I need
and is actually kinda pretty internally.  Well, at least it was before I
fixed some glaring problems.  Whatever.  The point is I want to share
[it](https://github.com/bsmith89/pymake) with
the world; what better stage exists for its introduction than this blog, which
absolutely no one reads?

...Yeah, I'll probably post it to [/r/python](http://reddit.com/r/python) too.

Tune in for Part II, in which I explain why _you_ should use my software.
