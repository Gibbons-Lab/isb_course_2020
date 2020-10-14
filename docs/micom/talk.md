<!-- .slide: data-background="assets/isb/data-midnight.jpg" class="dark" -->

# Modeling microbiota-wide metabolism with MICOM

### Christian Diener, Gibbons Lab

<img src="assets/isb/logo.png" width="40%">

from the *ISB Microbiome Course 2020*

<br>
<div class="footer">
<a href="https://creativecommons.org/licenses/by-nc/4.0/"><i class="fa fa-bullhorn"></i>CC-BY-NC</a>
<a href="https://gibbons.isbscience.org/"><i class="fa fa-globe"></i>gibbons.isbscience.org</a>
<a href="https://github.com/gibbons-lab"><i class="fa fa-github"></i>gibbons-lab</a>
<a href="https://twitter.com/thaasophobia"><i class="fa fa-twitter"></i>@thaasophobia </a>
</div>

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

Let's get the slides first (use your computer, phone, TV, fridge)

*https://gibbons-lab.github.io/isb_course_2020/micom*

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## Quick reminder :clock:

<img src="assets/materials.png" width="80%">

<br>

<a href="https://colab.research.google.com/github/gibbons-lab/isb_course_2020/blob/master/micom.ipynb"
   target="_blank">Click me to open the notebook!</a>

---

# Functional analyses

Tries to predict what the microbiome *does* from sequencing data.

Uses gene/transcript/protein/metabolite abundances (metagenomics, metatranscriptomics, proteomics or metabolomics).

Gene content yields metabolic *capacity* or *potential*.

---

<!-- .slide: data-background="var(--secondary)" class="dark" -->

# Genes and metabolite abundances are cool but not what you really care about*

<div class="footnote">

hot take :fire:

</div>


---

## Fluxes

<img src="assets/fluxes.png" width="45%">
<video width="45%" autoplay loop>
  <source src="assets/fluxes.mp4" type="video/mp4">
</video>

<div class="footnote">

video courtesy of [S. Nayyak](https://twitter.com/Na_y_ak) and [J. Iwasa](https://twitter.com/janetiwasa)

</div>

---

<!-- .slide: data-background="var(--secondary)" class="dark" -->

# Flux Balance Analysis (FBA)

Can we infer the most likely fluxes in a biological system?

---

## The flux cone

<img src="assets/flux_cone.png" width="100%">

---

The goal of FBA is to *reduce* the flux space to a *biologically relevant* one.

---

## Genome-scale metabolic modeling

<img src="assets/fba.png" width="100%">

---

## Selecting biologically relevant fluxes via parsimony

<img src="assets/pfba.png" width="40%">

Reproduces experimental fluxes in <i>E. coli</i> [very well](https://dx.doi.org/10.1038%2Fmsb.2010.47).

Bacteria do not like to produce more enzymes than necessary.

---

# MICOM

<img src="assets/summary.png" width="100%">

<div class="footnote">

https://micom-dev.github.io/micom

</div>

---

<img src="assets/overview.png" width="120%">

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## Let's continue with our data

:computer: Let's switch to the notebook...

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## Community-wide growth is hard :cry:

In a single genome-scale model we only have a single growth rate $\mu$. In a microbial community
we have several $\mu_i$ and a community growth rate

$$
\mu_c = \sum_i a_i\cdot\mu_i
$$

Why is this so hard? Can't we just maximize the community growth rate? Well...

---

## When 2 leads to infinity...

<img src="assets/ctFBA.png" width="60%">

---

*Cooperative Tradeoff FBA* allows us to treat metagenome-scale models with the *same*
methods as genome-scale metabolic models (pFBA, minimal media, etc).

---

## But does it work?

<img src="assets/validation.png" width="100%">

<div class="footnote">

https://doi.org/10.1128/mSystems.00606-19

</div>

---

Easy peasy. What's taking so long then?

<br>

Well, metagenome-scale models are slightly larger... :sweat:

---

<img src="assets/model_gephi.png" width="50%">

<div class="footnote">

69,441 reactions / 46,883 metabolites / 292,699 connections

</div>

---

## The niche space

<img src="assets/fig4.png" width="100%">

---

## Metabolic connections with disease

<img src="assets/fig5.png" width="100%">

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

We observed that the *overall production flux* $v_p = \sum a_i\cdot v_i^{ex}$
is most directly related to the phenotype.

This is the flux the *intestinal cells* can interact with.

---

## Your turn

Check out how to use MICOM for a "n-of-1" analysis.

<img src="assets/coding.gif" width="50%">

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

### And we are done :clap:

# Thanks!
