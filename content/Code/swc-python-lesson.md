---
title: First Time Teaching Python to Novices
date: 2015-08-11 4:00
tags: software-carpentry, teaching, programming, mistakes, python
...

This July I co-instructed with [Jennifer Shelton][shelton]
a Software Carpentry [workshop][workshop-page] at Stanford University,
targeted to researchers with genomic or evolutionary datasets.
Jennifer taught the shell (BASH) and version control with Git,
while I taught the general programming language Python.
I've been aware of the [organization][swc-site], which teaches software
development and computational methods to scientists, since going to a
workshop in 2012.
Since then I've served as a helper at one workshop
(troubleshooting individual learner's problems and helping catch them up with
the rest of the class),
and gone through the "accelerated", two day, instructor training at Michigan
State University.
After the Stanford workshop, I took part in new-instructor debriefing
on August 4th, during which I mentioned that I had to greatly pare down the
community-written lesson plan, [python-novice-inflammation][python-lesson],
to fit into the two half-day session we allotted it.

[shelton]: https://impactstory.org/JenniferShelton

[swc-site]: http://software-carpentry.org/

[python-lesson]: http://swcarpentry.github.io/python-novice-inflammation/

[workshop-page]: http://i5k-kinbre-script-share.github.io/2015-07-23-stanford/

Karin and Tiffany, who were running the debriefing, asked me to send a note
to the mentorship email list about which parts I removed and which I kept in.
I thought I'd also take the opportunity to comment on the material at large:
what worked for me and what didn't.
What started as an email quickly ballooned into this blog post.

To be explicit, I was teaching from the state of the repository at the time of
the workshop[^repo-state] .

[^repo-state]: [`76e3ea24406e4b8d684c9b45f3c5fd33e23ac71a`][commit]: still the
    HEAD as of this writing.

[commit]: https://github.com/swcarpentry/python-novice-inflammation/tree/76e3ea24406e4b8d684c9b45f3c5fd33e23ac71a

With this as my first workshop[^unprepared], I (incorrectly) thought
I could teach all of the topics straight through.
By the time it became apparent that this wasn't going to work,
adapting the first day's material had to be done on the fly.
After that experience, and
before the following afternoon,
I prepared a subset of the remaining material that I thought I could cover
I'm now relying on my (somewhat traumatic) memory of the first session,
and that outline I put together for the second day to write this summary.

[^unprepared]: and being insufficiently prepared

My plan going in was to split [the material][python-topics] after Topic 6,
getting learners up to writing functions on the first day,
so that we could discuss debugging and best-practices,
and transition from the Jupyter notebook to shell scripts, the next day.
Based on my co-instructors recommendation,
I did not have learners do all of the challenge questions for each topic,
but instead picked just one or two that I thought would be most useful.

[python-topics]: http://swcarpentry.github.io/python-novice-inflammation/index.html#topics

I found myself wishing (especially for Topic 1: "Analyzing Patient Data") that
some of the easier questions were integrated into the lesson itself, instead of
all at the bottom.
Learners should have had more chances to problem-solve early, instead of
listening to me for the entirety of each topic before getting their feet wet.

## Motivating Python ##

For that [first topic][topic-1] I did cover everything, but wish I hadn't,
since it was mostly focused on array operations and the specifics of working
with NumPy (e.g. operations along axes).
I appreciated that we were showing the learners powerful library features to
motivate the later work, but I didn't feel like it was great for this
workshop's "genomics" audience.
Maybe these initial motivating sections should be targeted the same way the
capstone projects are.
It was also too long relative to the other sections, in my opinion.

[topic-1]: http://swcarpentry.github.io/python-novice-inflammation/01-numpy.html

It _was_ very good, however, for introducing some python specifics, especially
things that learners coming from other languages like R or Mathematica might
not know (e.g. 0-indexing, slices, that variable assignment happens when each
line is executed, etc.).
It gave learners a chance to be surprised by their misconceptions and ask
questions.
We should do more of that.

It would have been helpful for the lesson to have pre-built explanations for
0-indexing and right-exclusive slicing, since these were the hard parts and I'm
not happy with the explanations I initially used.

I found the nature of the made-up data (maximum values smooth and minimum
values as a step-function along the first axis) distracting.
I also didn't know what they were supposed to represent (beyond inflammation
over time), so the "actually doing science" part of the motivation was a bit
lost.
Is there a reason we use these data?

## Python basics: lists, loops, conditionals, etc. ##

[Topics 2][topic-2] and [3][topic-3], "Repeating Actions with Loops" and
"Storing Multiple Values in Lists" respectively, were good and short.
I didn't feel like I had to cut anything out.
However, for-loop syntax was not explicitly covered early in the lesson plan.
It wasn't until I realized I had gotten ahead of myself that we talked about
loop variables, iterables[^iterables], and the indented code-block.


[topic-2]: http://swcarpentry.github.io/python-novice-inflammation/02-loop.html

[topic-3]: http://swcarpentry.github.io/python-novice-inflammation/03-lists.html

[^iterables]: Actually, we talked about getting values from lists and how
    strings are like lists, rather than about iterables in general.

I also thought the segue from Topic 1 to 2 was a bit weak.
This was a theme throughout, mixing the inflammation data with much simpler
stuff (e.g. looping over short strings and lists).
I realize we want to keep the motivation going, but, as a first-time
instructor, I found it to be distracting, and didn't know which I should be
emphasizing to the learners.

I also picked the wrong challenge question from Topic 1 (reverse `'Newton'`
using a loop), since we hadn't covered `range`, `append`ing to lists,
`''.join`, etc.
What novice audience is that question appropriate for?
Maybe the solution is simple and I'm just confused...

The material for [topic 4][topic-4], "Analyzing Data from Multiple Files"
worked well overall.
The only mistake I remember was copy-pasting the big chunk of code from the
lesson (looping over files and drawing sets of plots) instead of typing it out.
I figured since most of the code was library calls, learners wouldn't get
anything out of me taking the time to type all of it.
That may have been true, but it meant the learners weren't executing the code
at the
same time as me, which interrupted the flow of the lesson.

[topic-4]: http://swcarpentry.github.io/python-novice-inflammation/04-files.html

[Topic 5][topic-5], "Making Choice" (if-statements), was where things got
hairy.
I panicked a bit and went mostly off the lesson plan.
It did not go well.
When I tried to find something in the lesson to get me back on track,
I wished there was more explicit discussion of syntax and booleans.
I was able to review the topic the next day, which I think got any lost
learners
mostly caught up.

[topic-5]: http://swcarpentry.github.io/python-novice-inflammation/05-cond.html

As you can imagine, at this point we were nearing the end of the first day.
I did manage to show the learners the syntax for defining and using functions,
but I covered [topic 6][topic-6], "Creating Functions", in its entirety at the
start of the next
session.

[topic-6]: http://swcarpentry.github.io/python-novice-inflammation/06-func.html


## Learning my lesson ##

After the harrowing experience with conditionals on the first day, I took the
time to write out a personalized lesson outline for the next day with learning
objectives, steps in explaining difficult concepts, and pre-picked
understanding/challenge questions.
The exercise of writing an outline of learning objectives before the class was
very helpful, and something I intend to repeat before future workshops.

If I remember correctly[^metamemory], the second day I started once again with
functions, and largely based the lesson on the material in
[the topic][topic-6].
The temperature conversion formulas were an effective motivator for this
lesson.
I wonder if simple examples, like this one, can replace the more complex
(and, admittedly, more impressive)
inflammation tutorial to demonstrate the value of Python for scientists.
I also integrated material from the [topic on errors and exceptions][topic-7]:
tracebacks, syntax errors, etc.
In this combined topic I did not use the `import errors_01` example.
It was unclear to me why the lesson plan, as written, uses a black-box script
like `errors_01.py`, and not something more explicit, like an index or
attribute error, to dissect the traceback.
I think the explicit approach worked well for the learners in this workshop.
Since we were covering functions anyway, it wasn't hard to get a multi-level
traceback.
Syntax errors also combined nicely with learning function definition syntax.

[topic-7]: http://swcarpentry.github.io/python-novice-inflammation/07-errors.html

[^metamemory]: Despite the fact that I have those notes, I actually don't
    remember the details of that day's lesson as well.
    I wonder if there's some weird metamemory thing going on
    e.g. [this][google-memory] (unfortunately paywalled).

[google-memory]: http://www.sciencemag.org/content/333/6043/776.abstract



![The author dissecting an attribute error.[^photo-credit]][attribute-error]



[attribute-error]: {filename}/static/images/swc-stanford-byron.jpg

[^photo-credit]: Photo credit: Amy Hodge ([CC-BY][cc-by])

[cc-by]: https://creativecommons.org/licenses/by/2.0/

Somewhere in the process of talking about functions we got sidetracked with
`open()`.
I was surprised to see that the lesson plans have only limited discussion of
file objects, only really dealing with them in the section on `IOErrors`.
I think learners appreciated a chance to see how the array data they had used
the day before were saved as a CSV,
and how they could access the data directly.
It also gave us a chance to show that other objects besides lists and strings
can serve as iterators in for-loops.

I liked how the topic 6 [lesson plan][topic-6-defaults] used the library
function `numpy.loadtxt()` to talk about default arguments and the `help()`
built-in.
I jumped back and forth between examining that function and implementing
the same things (keywords, documentation) in a `center()` function we were
building.
The realized lesson was very similar to the repository's lesson plan,
but a little more integrated with errors and exceptions.

[topic-6-defaults]: http://swcarpentry.github.io/python-novice-inflammation/06-func.html#defining-defaults

I had the learners implement `rescale()` as a challenge question.
We then worked together as a class to add lower and upper bounds.
This was a much more difficult task than I expected
(even just deriving the correct formula),
and served nicely to demonstrate defensive programming and debugging.
While we touched on many of the concepts in [topics 8][topic-8] and
[9][topic-9],
these ideas, defensive programming and debugging, were spread throughout,
and I did not walk through either as an atomic lesson.

[topic-8]: http://swcarpentry.github.io/python-novice-inflammation/08-defensive.html

[topic-9]: http://swcarpentry.github.io/python-novice-inflammation/09-debugging.html

My ultimate goal on the second day was to write a program to calculate
the mean inflammation of each subject in the example files and then
transform the program into a command-line script that would operate as a
UNIX-style filter.
I remember Greg Wilson teaching Python scripting (along with BASH and SQL)
that way during my first workshop (as a _learner_!) at MSU
in May 2012[^swc-msu].
This [last topic][topic-10] seemed like a worthwhile mini-capstone,
since it would reintroduce ideas from the BASH lesson the day before,
and we could version-control our work with git.
While we managed to run our code as a script (rather than a cell in the
Jupyter notebook), the transition was a little rough around the edges, and we
didn't have time to add `sys.argv` or `sys.stdin`.

[^swc-msu]: The site for this historic event can still be found
    [here][msu-site].

[msu-site]: https://web.archive.org/web/20120514195748/http://software-carpentry.org/boot-camps/michigan-state-university-may-2012/

[topic-10]: http://swcarpentry.github.io/python-novice-inflammation/10-cmdline.html

## Take-aways ##

The second day of Python was much smoother than the first, and, while we
did not get to all of the material, I was satisfied with what we did cover.
It's quite remarkable that learners can go all the way from indexing into lists
to defensive programming and unit tests in just a few hours.
I'm not convinced that we got them far enough to jump right into using Python
for their own work, but I hope it was a good kick-start towards that goal.
I'm amazed some novice workshops only allocate a half-day session to the
programming language (be it Python, R, or Matlab),
although a quick survey of [upcoming workshops][upcoming] suggests that almost
_all_ of them do in fact use two sessions.
Is this the recommended approach (and if so where is it documented)
or have many instructors all independently come to the same conclusion?

[upcoming]: http://software-carpentry.org/workshops/index.html#future

Even so, there's still more material in python-novice-inflammation
than can be covered in two sessions.
I'm under the impression that the repository is sort of _meant_ to be like
that: way too big, so that instructors can pick and choose the parts that are
most salient for their audience.
This seems like a good idea, but
it was not sufficiently communicated to me as a first-time instructor,
and, while many of the difficulties I had could have been solved with more
comprehensive preparation,
having a "default" subset would have been helpful.
