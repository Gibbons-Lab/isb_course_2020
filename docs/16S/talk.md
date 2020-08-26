<!-- .slide: data-background="assets/isb/data-midnight.jpg" class="dark" -->

# Amplicon Sequencing Data Analysis with QIIME 2

### Christian Diener

<img src="assets/isb/logo.png" width="40%">

from the *ISB Microbiome Course 2020*

<br>
<div class="footer">
<a href="https://creativecommons.org/licenses/by-nc/4.0/"><i class="fa fa-bullhorn"></i>CC-BY-NC</a>
<a href="https://cdiener.com"><i class="fa fa-globe"></i>cdiener.com</a>
<a href="https://github.com/cdiener"><i class="fa fa-github"></i>cdiener</a>
<a href="https://twitter.com/thaasophobia"><i class="fa fa-twitter"></i>@thaasophobia </a>
</div>

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

# Hold your horses :horse:

Let's get the slides first (use your computer, phone, TV, fridge, anything with a 16:9 screen)

*https://gibbons-lab.github.io/isb_course_2020/16S*

---

# Organization of the course

<!-- .slide: data-background="var(--primary)" class="dark" -->

<img src="assets/materials.png" width="80%">

<br>

<a href="https://colab.research.google.com/github/gibbons-lab/isb_course_2020/blob/master/16S.ipynb"
   target="_blank">Click me to open the notebook!</a>

---

<!-- .slide: data-background="var(--secondary)" class="dark" -->

# QIIME (pronounced like *chime*)

Created ~2010 during the Human Microbiome Project (2007 - 2016) under the leadership
of Greg Caporaso and Rob Knight.

---

## What is QIIME?

> QIIME 2 is a powerful, extensible, and decentralized microbiome
analysis package with a focus on data processing and analysis transparency.

*Q*uantitative *i*nsights *i*nto *M*icrobial *E*cology

---

## So what is it really?

Essentially, QIIME is a set of *commands* to transform microbiome *data* into
*intermediate outputs* and *visualizations*.

<img src="assets/barplot.gif" width="100%">

It's commonly used via the *command line*.

---

[QIIME 2](https://doi.org/10.1038/s41587-019-0209-9)
was introduced in 2016 and improves upon Qiime 1, based on user experiences during the HMP.

Major changes:

- integrated tracking of *data provenance*
- semantic *type system*
- extendable *plugin* system
- multiple *user interfaces* (in progress)



---

## Where to find help?

QIIME 2 comes with a lot of help, including a wide range of [tutorials](https://docs.qiime2.org/2020.6/tutorials/)
[general documentation](https://docs.qiime2.org/2020.6/) and a
[user forum](https://forum.qiime2.org/) where you can ask questions.

---

## Artifacts, actions and visualizations

QIIME 2 manages *artifacts*, which are basically intermediate data that feed
into *actions* to either produce other artifacts or *visualizations*.

<img src="assets/key.png" width="50%"><img src="assets/overview.png" width="50%">

---

## Remember

Artifacts often represent *intermediate steps*, but Visualizations are *end points*
meant for human consumption :point_up:.

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## Analyzing gut microbial composition during recurrent <i>C. diff</i> infections

16S amplicon sequencing data of the V4 region from human fecal samples

4 healthy donors and 4 individuals with recurrent infection.

https://doi.org/10.1186/s40168-015-0070-0

---


## The <i>C. diff</i> infection cycle

<img src="assets/cycle.png" height="550vh">

<div class="footnote">

courtesy of [Stephanie Swegle](https://see.isbscience.org/steam2019/stephanie-3/)

</div>

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

# Setup

:computer: Let's switch to the notebook and get started

---

### Wait... what?

<img src="assets/guide.png" width="30%">

*All* output we generate can be found in the `treasure_chest` folder at

https://github.com/gibbons-lab/isb_course_2020/treasure_chest

or `materials/treasure_chest` in the Colaboratory notebook.

---

## What will we do today?

<img src="assets/steps.png" width="100%">

---

## Illumina FastQ files (Basespace)

<img src="assets/illumina.png" width="60%">

```plaintext
@SRR2143527.13917 13917 length=251
TACGTAGGTGGCGAGCGTTATCCGGAATTATTGGGCGTAAA...
+
BBBBAF?A@D2BEEEGGGFGGGHGGGCFGFHHCFHCEFGGH...
```

---

We have our raw sequencing data but QIIME 2 only operates on artifacts. How
do we convert our data into an artifact??

:egg: ↔ :hatched_chick:

---

## Our first QIIME 2 commands

We can import the data with the `import` action. For that we have to give
QIIME 2 a *manifest* (list of raw files) and tell it what *type of data* we
are importing and what *type of artifact* we want.

:computer: let's jump back to the open Colaboratory notebook...

---

## View a QIIME 2 visualization

There are two ways to look at a QIIME 2 visualization:

- visit https://view.qiime2.org and load the file
- use `qiime tools view [file.qzv]` if you have QIIME 2 installed

:thinking_face: What do you observe across the length of the read? Where would you truncate the reads?

---

QIIME 2 commands can get pretty long. Here are some pointers to remember the
structure of a command:

```
qiime plugin action --i-argument1 ... --o-argument2 ...
```

Argument types usually begin with a letter denoting their meaning:

- `--i-...` = input files
- `--o-...` = output files
- `--p-...` = parameters
- `--m-...` = metadata

---

## Time to bring in the big guns :bomb::zap:

We will now run the DADA2 plugin, which will do 3 things:

1. filter and trim the reads
2. find the most likely original sequences in the sample (ASVs)
3. remove chimeras
4. count the abundances

---

## Identifying amplicon sequence variants (ASVs)

<img src="assets/dada2.png" width="80%">

Expectation-Maximization (EM) algorithm to find alternative sequence variants
(ASVs) and the real error model at the same time.

---

## PCR chimeras

<img src="assets/chimera.png" width="60%">

The primers used in this study were F515/R806. How long is the amplified fragment?

---

We now have a table containing the counts for each ASV in each sample.
We also have a list of ASVs.

<br>

:thinking_face: Do you have an idea for what we could do with those two data sets? What quantities
might we be interested in?

---

## Relationship between ASVs

One of the basic things we might want to look at is how the sequences across
all samples are related to one another. That is, we are often interested in their *phylogeny*.


---

You can visualize your tree using iTOL (https://itol.embl.de/).

<img src="assets/tree.png" width="75%">

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## Diversity

In microbial community analysis we are usually interested in two different families of diversity metrics,
*alpha diversity* (ecological diversity within a sample) and *beta diversity* (ecological differences between samples).

---

## Alpha diversity

How diverse is a single sample?

<br>

- how many taxa do we observe? → richness (# observed taxa)
- how evenly are abundances distributed across taxa? → evenness
- metrics that combine both richness and evenness → Shannon entropy

---

## Beta diversity

How different are two or more samples/donors/sites from one another other?

<br>

- how many taxa are *shared* between samples? → Jaccard index
- do shared taxa have the *similar abundances*? → Bray-Curtis distance
- do samples share *phylogenetically similar* sets of taxa? → weighted or unweighted UniFrac

---

## Principal Coordinate Analysis

<img src="assets/pcoa.png" width="100%">


---

<!-- .slide: data-background="var(--primary)" class="dark" -->

## But what organisms are there in our sample?

We are still just working with sequences and have no idea what *organisms*
those correspond to.

<br>

:thinking_face: What would you do to go from a sequence to an organism's name?

---

## Taxonomic ranks

<img src="assets/ranks.png" width="40%">

---

Even though directly aligning our sequences to a *database of known genes*
seems most intuitive, this does not always work well in practice. Why?

<br>

Alternative methods use *subsequences (k-mers)* and their counts to *predict* the
lineage/taxonomy with *machine learning* methods. For 16S amplicon fragments this
often provides better *generalization* and faster results.

---

## Your turn

What is the relationship between particular *taxa* and the disease state?

<img src="assets/coding.gif" width="50%">

---

<!-- .slide: data-background="var(--primary)" class="dark" -->

### And we are done :clap:

# Thanks!

