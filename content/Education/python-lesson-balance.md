---
title: Teaching Python by the (Note)Book
date: 2016-12-19 01:00
tags: software-carpentry, teaching, programming, python, jupyter
...

## This stuff is hard ##

In many ways, [teaching Python to scientists][swcarpentry]
is easier than just about every other audience.
The learning objective is clear: write code to make my science more accurate,
more efficient, and more impactful.
The motivation is apparent: data is increasingly plentiful and increasingly
complicated.
TODO: Fix the above sentence.
And the learners are engaged and used to putting in the effort needed to
acquire new skills.

But, despite all of the advantages, teaching _anybody_ to program is _hard_.
In my experience, one of the most challenging trade-offs for lesson planners
is between motivating the material and teaching a mental model
for code execution.

For example, scientists are easily motivated by simple data munging and
plotting using `pandas` and `matplotlib`;
these are features of the Python ecosystem which can convince a graduate
student to pay attention to the lesson instead of answering emails.
Actually _using_ these features, however, requires a long list of basic
concepts: Python syntax, libraries, function calls, objects and methods,
conditionals, and variable assignment, to name just a few.
A lesson planner can start from the basics, working in to these features
along the branches of the dependency tree, but that could require hours
(or even days) of "boring programming".
It's all too easy to dismiss learners who lose interest before you get
to the "good stuff", but this is more a reflection of the lesson materials and
instructor than the students.

At the other extreme, a lesson could start with a working code,
or, in the Software Carpentry style, the instructor could lead learners
through writing code that uses these features, before the concepts have
been fully introduced.
This in-at-the-deep-end approach quickly demonstrates exciting uses of Python,
but at the risk of intimidating learners, making them wonder if they're the
only one in the room who's confused by what's going on under the hood, and what
all of the syntax means.
I'm not aware of any studies on this topic (if you are, please pass them my
way), but I'm willing to speculate that this second approach has
a higher risk of subjecting learners from underrepresented groups to stereotype
threat, a major risk when teaching a subject, like programming,
that has a pervasive diversity problem.

Luckily for us all, there's a whole spectrum of approaches in between the
motivations-first and foundations-first extremes.
We can trust learners to self-motivate for a time, especially when we're
teaching scientists.
Attendees are there voluntarily (I would hope).
Likewise, learners will never have a perfect mental model for how their code is
working;
the key is to avoid unintentionally teaching pathological models that are
difficult for the instructor to diagnose and iterate beyond.

## State of the Python lesson ##

As of this writing, the current default Python lesson for Software Carpentry is
the ["Novice Inflammation" lesson][inflammation-lesson].
I have [written previously][previous-experience-blog-post] about my experience
with this lesson, and have not been shy with both my praise and criticism when
discussing it with fellow instructors.
There is a _lot_ to be positive about in the composition of this lesson.
It has been an effective approach to teaching Python to what at this point
must be probably several thousand workshop attendees.

However, this post is about how we can do better.
My primary criticism for this lesson focuses on the first section:
["Analyzing Patient Data"][inflammation-lesson-first-section].
The approach here falls towards the motivation-first extreme.
Learners are shown how one might go from raw data in a CSV to heatmaps
and line plots, two useful skills.

[inflammation-lesson-numpy]: http://swcarpentry.github.io/python-novice-inflammation/01-numpy/].

The downside, however, is that this happens without fully explaining the
syntax, what libraries are, `numpy` arrays versus Python lists, `dtypes` vs
built-in Python types, and more.
I think that by using this particular motivating example while glossing over
those details we're giving learners a challenging mental model to iterate
beyond.
What's more, I believe that this results in a _diversity_ of models
making later instruction more likely to leave some learners behind.
This lesson also gets stuck in the weeds over difficult concepts which, in my
opinion, aren't nearly as important for learners, for example, accumulating
over particular axes in `numpy` arrays.

For this and other reasons Greg Wilson spearheaded an attempt to
reinvent the Python lesson.
The ["Novice Gapminder" lesson][gapminder-lesson] is a from-scratch re-write.
Tangentially, I think it's interesting that SWC's normal pull-request model for
lesson development is unable to accommodate a major overhaul like this one.

Gapminder is different in several ways, for instance using `pandas` as a focal
library instead of `numpy`.
Notably for this commentary, though, it also takes a much more gradual approach
to motivating the material.
`pandas` and `matplotlib` are not introduced until the end of the first
half-day,
_after_ a thorough discussion of variable assignment, functions, and data
types.
The lesson also appears to lack any glaring distractions with lower priority
topics.

Overall, I think this lesson hits a superior balance between motivation
and basics, while also improve the structure and refining the details.
I have to applaud everyone who's contributed to its development.
I've now taught from this lesson once, and co-instructed a workshop which used
the first half of it.
The quality of lesson design was apparent both times.

## Continual improvement ##

That's not to say, however, that it cannot be improved.
[One discussion][gapminder-113] which has happened in a limited form on the
Github repository comes back to this same question of balance,
with a proposal to delay the data analysis motivating example, further
front-loading the basics.
Having now had some experience teaching the lesson I believe this is
unnecessary, learners did not appear to get intimidated nor mislead by the
example usage and I didn't notice much loss of engagement.

[gapminder-113]: https://github.com/swcarpentry/python-novice-gapminder/issues/113

Like many trade-offs in lesson design, the optimal position on the
motivations-foundations spectrum is context dependent.
I would be hesitant to focus on basic concepts for the first session if I were
teaching high school students or any learners skeptical about the utility of
the material.
A room full of scientists who were there specifically to learn Python, however,
could probably tolerate even more front-loading of syntax and control-flow.

I would like to nominate a slightly different approach to balancing between
motivation and building blocks.

[lo5an-comment]: https://github.com/swcarpentry/python-novice-gapminder/issues/113#issuecomment-256230540

Last week I co-taught an _unofficial_ SWC workshop teaching Python to
about 20 learners, primarily graduate students in the biological sciences.
My co-instructor, Jackie Cohen ([@jczetta][jczetta-twitter]),
taught the first half-day using the Gapminder lesson.
The positive reception from learners was testament not only to her skillful
instruction, but also the quality of the lesson.

[jczetta-twitter]: https://twitter.com/jczetta

I then taught second day with a customized lesson using the
same gapminder dataset and covering the same
topics as the latter half of the normal lesson.
Inspired by [a comment][lo5an-comment] in the Gapminder discussion,
I wrote up a unified, "realistic" analysis of the gapminder data as a Jupyter
notebook.
In particular, my analysis produced a nearly publication quality figure which
told a story about the relationship between per-capita GDP and
life-expectancy[^congrats].
I then had learners run this notebook to see the quality of analyses they could
produce with less than 100 lines of code.

[^congrats]: Apologies for the self-congratulatory tone.
             While I am proud of the figure, the gapminder data is also
             particularly great to work with.]



This modification also lends itself to a thematic unification, which I
found to be somewhat elegant.






Many of the most powerful features in Python (and in Python libraries)
are founded on high-level abstractions which obfuscate the underlying
flow of computation.
What's more, even "Pythonic" code frequently utilizes advanced language
features which would ideally be skipped in a two-day workshop.


