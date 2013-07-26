Title: Even pathogens hate a cheater
Date: 2013-06-19 12:00
Tags: microbiology, cheaters, evolution, pathogens


_I would like to apologize for the long delay since my last post.  The excuse
(I keep telling myself) is that, having already written too many computational
articles, it was time to prove that I could write about biology too.
Unfortunately I'm not nearly as good at reading the literature as I should be.
Anyway, it's done.  You can stop complaining now._


One barrier to engineering bacteria for biofuel production or any other human
endeavor is that evolutionary rates are scaled by population sizes and growth
rates.  For an organism with massive population sizes (trillions of individuals
or more) and doubling times on the order of hours, evolution can occur quite
quickly.  Genetic variants within the population which are capable of growing
faster will quickly take over.  For an organism which is, for example, wasting
a huge fraction of its energy producing your future gasoline, you can bet this
months graduate stipend that mutants which put more resources into growth will
sweep the population.

See kids, cheaters _do_ win in the end!   In the above example the microbes are
"cheating" the metabolic engineers out of their valuable chemical products, but
the same sort of evolutionary trend: favoring fitness over (and often at the
expense of) any other metric we can think of, has big implications for other
bacteria as well.  My current research explores the impact of selection on
growth rate versus resource use efficiency, but I'll write more about that some
other time.

Many microbial populations engage in cooperative behavior. [_Salmonella_
Typhimurium][wiki-salmonella], for instance, a human pathogen, uses a type III
secretion system (imagine bacteria using tiny syringes to pump toxins into your
cells) to induce wide-spread inflamation in the gut.  By inducing enough
inflamation, a population of _Salmonella_ can make a niche for themselves in
which they outcompete the non-pathogenic (commensal) bacteria already present.
Those syringes are expensive, but without them the _Salmonella_ can't colonize
at all, so everyone works together for the common good.

[wiki-salmonella]: http://en.wikipedia.org/wiki/Salmonella_enterica

Unfortunately (for _Salmonella_ at least) evolution doesn't really care about
the common good.  Every so often a mutant will come along which has lost the
type III secretion system genes, or doesn't express them as frequently or at
such high levels.  Since this new strain doesn't have to waste resources on
producing the costly virulence factor, but can still take advantage of the
inflamation being induced by all his straight-laced bretheren, he grows faster
than all the normal ("wild-type") _Salmonella_.  Even when it's almost entirely
cheaters and the population's ability to inflame the host is greatly reduced,
even when they're all struggling to outcompete the commensal bacteria, the
mutant is still a _little_ better off because it's not wasting resources on
that silly syringe.

The cheater wins again!  In this example it's not the metabolic engineers
that are being deprived of their liquid fuel, but the wild-type _Salmonella_
which is being cheated out of its public resource: inflamation.  Of course
winning for the cheater also means that the entire population is wiped out.
Without sufficient inflamation _Salmonella_ can't survive, but up until that last
cell is killed or expelled, at least the cheater was doing better _relative to_
the wild-type.  And, in the short-term, that's what winning _is_ in the Game of
Evolution.

"But wait just a minute", says the astute reader, "why have I been cooking my
eggs all these years if _Salmonella_ can so easily be wiped out by this internal
rebellion?"  Aha!  That's the exact question raised by Médéric Diard and
co-authors in their recent paper, "[Stabilization of cooperative virulence by
the expression of an avirulent phenotype.][the-article]"

[the-article]: http://www.nature.com/nature/journal/v494/n7437/abs/nature11913.html

What they found was that wild-type _Salmonella_ Typhimurium was playing chess
with the mutant, sacrificing a Knight in order to take the King.  Diard et al.
discovered that a fraction of the wild-type Typhimurium population was not
expressing the costly virulence factors.  These are not cheaters; their
genotype is identical to cooperators which _are_ expressing the type III
secretion system.  Their phenotype, however, is identical to the cheaters.  By
choosing to not expend the energy needed for the construction of those microscopic
syringes, they achieve the same fitness as the mutant.

It's not a complete equilizer.  Their daughters still have some probability of
expressing the virulence factors (or else they might as well be _real_
cheaters), but their fitness deficit is not as great.  This boost was bought,
however at the price of a reduced population size.  Since only a fraction of
their ranks are inducing host inflamation, the total virulence of the
population is reduced.

"But wait again", you might point out, "just because the fitness benefit of
cheating has been minimized does not mean that it has been eliminated entirely.
The cheaters will still take over the population in the end, no?"  You're
right, cheaters will still grow faster in the long run, since they _never_
cooperate, but **it will require additional time for them to take over**.

The rate at which an allele fixes in the population is positively related to
the relative fitness of that allele and therefore the cheater will not fix as
quickly.  In a pathogen like _Salmonella_, the ultimate goal is to infect a new
host.  If the cooperators can sustain a sufficiently large population for long
enough, their host is likely to pass them on to another unsuspecting (and
un-hand-washing) individual.  The cheater's success was all for nothing;
without the type III secretion system, the mutant will never colonize another
host.  While they may have won the figurative battle, they lost the war.
They've painted themselves into a corner.  (Insert additional cliches here.)

Diard et al., in their article, do some fantastic simulations, showing all of
the dynamics at play.  I encourage you to check it out.  One of the most
exciting sentences is the second to last (see, a snoodier blogger would have
said "penultimate"), the authors point out that this tendency for mutants to
out-compete the wild-type pathogen, and therefore reduce the negative effects
on the host, suggests a potential [therapy][evol-med]: treat those suffering
from _Salmonella_ with a large dose of cheaters!

[evol-med]: http://en.wikipedia.org/wiki/Evolutionary_medicine
