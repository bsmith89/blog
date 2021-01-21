---
title: Things I'm Glad I Learned
subtitle: Skills, concepts, techniques, and models
date: 2021-01-18 18:00
tags: open science, biology, computational biology, education
modified: 2021-01-21 12:00
...

_(WARNING: This post has not yet been revised. It therefore
contains all kinds of typos, spelling errors, grammatical issues, and
delusions of grandeur, wisdom, and writing ability.)_

This post is intended as a living document&mdash;a
gratitude journal of sorts&mdash;of some things that I'm glad I learned.
I expect many of the items on this list will be relevant to computation
biology, but that may change in the future.

The big idea is that for every item on this list I am (A) glad that
someone introduced me to it,
and (B) think more people should know about it.
This post is my chance to "pay it backwards", as it were;
maybe someone else will be grateful for something they find for the first time
on this list.

It may also double as an inspiration list for future posts.

My goal is to write a small blurb for each item, explaining what it is,
how it connects to other items, why I'm grateful for it,
when, and why I first learned about it.
I may add additional links in future edits.
Beyond that, I'll likely leave further discovery up to the reader.

## Computing

#### Dependency Graphs (e.g. GNU Make, Snakemake)

Many computer people have used GNU Make (or one of its variants) to build
software, but not everyone realizes that it is actually a much more generally
applicable tool.
Make's core idea is that every file that you want to construct requires zero
or more other files as prerequisites.
When you have multiple files, and some of them are prerequisites of
each other, you end up with a directed, acyclic graph describing all of the
chains of dependency.
This description is encoded in Make's domain specific language (DSL) in a
`Makefile`.

The beauty of this dependency graph is that it directly implies optimal
procedures for a whole bunch of useful operations.
First, and most useful, for any target file and set of existing files, Make can
determine the sequence of file constructions that will get from A to B.
As a corollary, it can also determine what _doesn't_ need to be built
given what already exists.
If you tack on instructions for building each file from its prerequisites, Make
can run those procedures for you automatically.
And if you have timestamps for each file, it can update files only when they're
out of date.

While this was originally designed for software compilation, it works just
as well for data workflows (or building static HTML for a blog...)

Since discovering the power of the dependency graph representation and tooling,
I've since upgraded to Snakemake, which fills some additional gaps that come up
in bioinformatics, but is exactly the same concept.
At this point, the Snakefile is the core of all of my (computational) research
projects, and provides me with a version-controlled, and highly modular,
description of all of the steps in my project.

I think I need to thank C. Titus Brown for introducing me to Make, probably
in summer of 2011 while I was rotating in his lab (but maybe later).

#### Probabilistic Programming (e.g. PyMC3, Pyro)

Since first learning about model based inference, at ELME in 2012,
I've been enthralled with frameworks that allow me to take full advantage
of the modularity and flexibility of graphical models without
programming the core algorithms from scratch.
It was actually the process of learning PyMC3 that taught me almost everything
I now know about Bayesian statistics (with a foundation of key concepts
imparted by many other teachers along the way).
Having access to such a powerful DSL makes graphical modeling the hammer for
which I now see an abundance of nails.

More recently I've started to use Pyro (a different probabilistic programming
framework) as well.
While it was a chore to reshape my mental model of probabilistic programming
with a whole new ecosystem, that has undoubtedly been a valuable learning
experience, and the incredibly fast, GPU accelerated, stochastic gradient
descent algorithms for MAP estimation have been a breakthrough for my research.

I honestly have no idea who first introduced me to PP, but based on my
GitHub I was teaching myself PyMC3 starting in 2016.

#### Containers (e.g. Docker, Singularity)

The newest item on this list (as of December 2020)!

Containers take what Conda promised (encapsulated, reproducible
software environments), and actually deliver it.
I think the Docker/Singularity combo may have finally solved all of my
software installation problems... Lol.

This is a hard one to assign thanks, because containerization has been
marketed to me by probably five different people since 2014 or so.
Very grateful that I finally picked it up in 2020!
Should I also thank the incredibly frustrating experience of trying to install
PyMC3/Theano (on a slightly outdated CentOS server, repeatedly, every 6 months)
for finally convincing me to try it out?

#### Command-line / UNIX

I'm thankful that I have a glue environment, the UNIX command-line,
for all of my computational work.
Working with a command-line interace (CLI) is foundational for all of the
other headings in this "Computing" section.
I'm (as of now) not including Vim as a separate item, but it really is the
combination of Bash and (Neo)Vim that I'm most grateful for.

I'm not sure who to thank for this one. Maybe Google, because they sent me a
free Chromebook in the early days (which I used extensively for college
work until the wi-fi broke...).
It was hacking around on that Chromebook's terminal that got me into Linux,
and ultimately resulted in me replacing Windows with Ubuntu on my main laptop.

I probably wouldn't be the scientist that I am now if it weren't for that
experience.

[Relevant XKCD](https://xkcd.com/519/)

#### Python

Anything that I'm capable of programming, I'm capable of programming in Python.

I'm glad that I know at least one language very well.
I think it makes me a
better teacher (of Python, but also of other languages).
I think it makes
it easier for me to learn new languages and programming concepts.
And I almost never need to decide what language to work in when I'm
doing something complicated; it's always Python.

Thanks for introducing me to Python goes to Dr. John Hayes, a postdoc
(neuroscientist) I worked with briefly while I was doing undergraduate research
in Margaret Saha's Lab at The College of William &amp; Mary.

#### Functional Programming

I'm a Haskell beginner, maybe intermediate depending on who you ask.
I don't do any of my work in Haskell, although I sometimes look for
opportunites.
On the other hand, almost _all_ of my programming is in a functional style.
I think (without any empirical evidence) I've probably saved myself a lot of
problems by taking pains to:

- Never reuse variable names for different things
- Avoid mutation ("in the large")
- Use higher-level functions and composition instead of conditionals to control
  program flow
- Keep side-effects away from core logic

#### Plain-text

Simple text-files and a smattering of UNIX tools will take you 2/3rds to
being a bioinformatician.
Text files are the ultimate form of portability and I believe they should be
used until there is a good reason not to.

I think Software Carpentry is probably responsible for my positive relationship
with plain-text.

#### Version Control (e.g. Git)

If most of your work is plain text, you also get to use version control for
tracking your progress, archiving, sharing, collaboration, and fancy
branching that sometimes comes in handy.

I am very thankful for having been introduced to Git by Software Carpentry.
It has saved my ass many times.

#### Jupyter notebooks

Jupyter Notebooks (and their kin) are great, but only for prototyping and
interactive work; never for reproducible automation.
Notebooks are a core part of my workflow, and the exploratory data analysis
phase of my work is very much done in the Jupyter environment.
On the other hand, my love of workflow managers like Snakemake means that
I try to keep interactive work at the "tips" of my data processing DAG.
Notebooks are a great place to do prototyping, but the second I need the
resulting data for a downstream step it's probably time to convert it to a
script.

I was introduced to IPython by Greg Wilson and IPython (now Jupyter) Notebooks
by C. Titus Brown during my first Software Carpentry class in 2012.
I'm thankful for all of the work that has gone into making Jupyter Notebooks
the phenomenal tool that they are.

## Biology

#### Organic Chemistry

I think having first-principles knowledge about how biology is built out of
chemistry has served me very well.

Not sure there's much more for me to say than that.

#### Neutral Evolution / Spandrils

Not everything is adaptive (e.g. I'm 99% sure eye color doesn't affect survival
or reproduction.)
Not everything that seems adaptive, even when there's evidence for convergent
evolution, actually is.
It's incredibly infuriating to see so many Appeals to Natural Selection
(a new logical fallacy I'm naming here first, 2021-01-18) in our
general discourse.

Some traits are due to random events (neutrality).
Some traits are a natural consequence of physical reality (spandrils).
I'd guess these are important parts of a full answer to a key question in my
field: "why do animals have such fancy microbiomes?"

If I had to guess, I learned about both neutral evolution and spandrils first
in my evolutionary biology class in college.
I'm sure I can figure out who taught that class if I dig into my emails,
but I'm going to put that off for another day.

#### Microbial Communities

I have no doubt that the research I did in high school with Dr. May Voytek at
the USGS (in 2006 and 2007) was one of the most important experiences for my
career development.
I was enthralled then&mdash;as I am now&mdash;with the ways in which microbial
metabolisms can combine in complex communities to perform immensely important
processes.
Microbiomes are a great example of an emergence, and I find that very exciting.

## Statistics

#### Linear Algebra

It's true what they say. Linear Algebra is the core of statistic(al computing).

I learned linear algebra, in a course by that name, my sophomore year of
college,
and have taken a number of courses since then that improved my competence
markedly.
These include mathematical biology classes at W&M (2010?),
graduate level statistics courses
(2012?), and a class on matrix population models in ecology taught by Hal
Caswell (2012).

#### Graphical Models

My introduction to graphical models were back-to-back one-week workshop on
maximum likelihood estimation and structural equation modeling taught by Colin
Kremer and Don Schoolmaster, respectively, during two sessions of ELME
("Enhanced Linkages between Mathematics and Ecology") at Kellogg Biological
Station in the summer of 2012.

Modularizing probability into graphs of relationships between latent
and observed variables is incredibly powerful and is the basis for the
entirety of my statistical understanding.

#### Bayesian Statistics

It's not the elegance of Bayes's Rule that I'm enamoured with;
it's how Bayesian statistics _democratizes_ inference (e.g. the Inference
Button).
If you have a data generating model and some data, you can make
logically consistent statements about it's parameters.
_And_ you get propagation of uncertainty for free!
How cool is that??

The first material impact on my understanding of Bayesian stats
was probably in Statistics for Ecologists (was that the class name?),
taught by Dr. Ian Dworkin at Michigan State University.
ELME also played a key role in priming me to understand what Dr. Dworkin was
teaching, although I still only got a whiff of the importance.
It was probably another 4+ years before I learned enough basics to
start calling myself a Bayesian by self-teaching PyMC3.

#### Causal Inference

I am by no means fully competent with causal inference, but I aspire to be.

The idea that we can automate the scientific method
(`observation -> hypothesis -> experiment` and all its variations), has been
super influential on the way I think about my work.

I'd like to do more of this in the coming data.

## Teaching

#### Learning Objectives / Concept Inventories

It's like the truism that I don't know how to attribute: "The most important
part being able to play a song, is knowing how it goes".
The most important part of teaching is knowing what you are teaching.

I think the biggest mistake that I've made (and seen made) as a teacher
is not knowing what I'm trying to teach.
Explicit and carefully vetted learning objectives, especially those written
using best practices
(i.e. "At the conclusion of this activity, participants will be able to...")
are a key tool to solve this problem.
Following that with simple questions that (A) assess whether those objectives
have been met, and (B) identify exactly how students' understanding is lacking,
is the real win.
Collections of those questions, called "concept inventories", can (and should
be) shared as a key component of collaborative lesson development.

I think I have to thank Greg Wilson and Software Carpentry instructor training
(in 2016?) for opening my eyes to the power of this combination.

#### Expert Bias

The more we know about a subject the harder it is for us to empathize with
those just starting to learn it.
(See Cognitive Biases, below)
I see it everywhere and staying self-aware about how it limits my
ability to teach has been really important.

This is another one I picked up from Greg Wilson and Software Carpentry
training.


#### Learning By Teaching

For me (and undoubtedly many other people too), I learn something the best
when I have to teach it.
This served me very well during my undergraduate genetics class when
Nishant Kishore and I would cram the night before a test by me "teaching" him
the material to the extent that I had understood it.

This compounds with other ideas in pedagogy, like Expert Bias, and I think
its a big part of why the Think-Pair-Share tactic works so well.

## Life

#### Growth Mindset

It feels incredibly powerful to see your current self as just a single stage
in the development of your full capabilities.

I think I really first learned this in Multivariate Calculus my sophomore
year; I distinctly remember how gratifying it was to go from absolutely zero
understanding to a B-minus on the final; a bad grade relative to my other
classes but I'm very proud of it nonetheless.

Knowing that I am a work in progress is both liberating and empowering.

#### Deficit Model of Persuasion

People who disagree with you about the way the world works often have all the
same facts as you do.
We don't convince people of our world view by giving them more facts.

I find this depressing. But on the flip side you _can_ be much more effective
at persuasion by doing two key things (to my limited understanding):

- Share your emotional reasons for your beliefs
  (e.g. I'm super **excited** to be able to travel and hug my parents again
  after they and I are vaccinated for COVID-19.
  I've been **scared** about their safety, and vaccination feels like an
  opportunity for **optimism**.)
- Demonstrate that their community shares that belief.
  This is usually done by making them part of _your_ community.
  (I think it's really great that **our** family/college/neighborhood has
  really come together to get everyone vaccinated.)

This is obviously key for science communication.

#### Privelege

Recognizing my advantages has been really helpful in building empathy for
disadvantaged groups in the world.
I'd like everyone to have the same access and opportunities for success and
contribution that I have had.

I probably internalized this sense circa 2015...ish.
Not sure if there's any one person to thank.

#### Talking About Yourself (e.g. "I feel..." Language)

I think that my interpersonal relationships have been bolstered by
a mutual ability to communicate about our own feelings instead
of claiming some objective sense of reality ("I am... You are...").

I can say with some certainty that communication is much more likely to
transition into a fight when I break this rule.

I realize this is common advice, but it has served me well.

#### Cognitive Biases

Especially the "Fundamental Attribution Error".

Mostly because I am also subject to all of the same biases, but also
because it helps me to understand peoples' behavior, even at large scales.

#### Profit and Monopoly

I think I have a hobbyist's understanding of economic theory.
As I understand it, in an idealized world (perfect market efficiency) no
producer should be able to make a marginal profit in the long run.
Obviously this is not really the case, since e.g. doctors are making
great money for their time.
I think it's fascinating that in many (most?) cases where value is being
captured by a small group of people this can be assigned to some sort of
monopoly power.
For instance

- doctors have the American Medical Association controlling the supply of
  medical labor,
- Genentech has various patents and corporate secrets, and
- ISPs have both cartel power and huge barriers to entry in most regions.

Monopolies aren't all evil (left as an exercise to the reader).
Appropriately regulating these monopolies seems to me to be a key
role of governments.

#### Intentional Communities

In this millennium, many people (including me) are suffering from less community
than the previous one.
This would appear to be due to geographic mobility (loss of family and
friends), secularization, an extended youth, etc.

I think it has been empowering to realize that we can choose to have those
communities if we're willing to work for it.
Intentional communities (e.g. communes, kibbutzim) prove it, and give me
something to aspire to.

#### Getting Things Done (GTD)

I don't actually use the GTD system, so why is this one on the list?
For me, GTD taught me to use to-do lists as a plan for the day, rather than
(only) record-keeping about what I need to do.
Specifically GTD introduced me to the tactic of giving myself a short list of
_only_ the tasks that are currently a priority, and using my own behavior to
re-assess if things are _actually_ important.

To-do lists can serve other purposes as well, but motivation and prioritization
are two key ones for me.

#### Habits

I very much believe that the most important factor in whether or not we
demonstrating self-control in our lives is the degree to which we actually
have to flex that muscle.
Habits are an important way that we can unload the weight of "I should really
do X" while _still doing X_.

#### Rituals

For me at least, lots of the stress in life comes from worrying or thinking
about things in a non-productive way or over which I don't have control.
Rituals have been valuable for me in putting clear landmarks in my
day/week/year that allow me to reset my mental state.
Many of them are also just enjoyable on their own.
Some key rituals that come to mind:

- Daily:
    - Reading the news as I wake up
    - Making/drinking coffee in the morning
    - Ending the core of my workday with a beer/cocktail
    - Washing my hands thoroughly when getting to work, home
- Week:
    - Going for a run/walk without a schedule or destination
    - Cooking an expansive dinner
- Yearly
    - Traveling to be with my family
    - Deep-cleaning my home

I still want to be intentional about building more of these into my life.
