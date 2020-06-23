![GitHub release](https://img.shields.io/github/tag/Gibbons-Lab/isb_course_2020.svg)
![Qiime 2 version](https://img.shields.io/badge/Qiime%202%20version-2020.2-blue.svg)
[![part 1](https://img.shields.io/website-up-down-green-red/https/shields.io.svg?label=website)](https://gibbons-lab.github.io/isb_course_2020/16S)
[![part 2](https://img.shields.io/website-up-down-green-red/https/shields.io.svg?label=website)](https://gibbons-lab.github.io/isb_course_2020/micom)


# Data and Materials for the ISB microbiome course

## Output

All output generated during the walkthrough can be found in the
[treasure chest](treasure_chest). The easiest way to get all of that
is to [download the entire repository](https://github.com/Gibbons-Lab/isb_course_2020/archive/master.zip).

## Part 1: Amplicon Sequencing Analysis

You can see the actual workshop walkthrough at
https://gibbons-lab.github.io/isb_course_2020/16S. Press `?` to get a list
of available live options such as slide overviews and speaker mode. Note that
some slides are grouped vertically, you can navigate the presentation using
the directional buttons on your keyboard.
A [PDF version](part1.pdf) (lacks the output previews) is also available.


## Part 2: Metagenome-scale Modeling with MICOM

You can see the actual workshop walkthrough at
https://gibbons-lab.github.io/isb_course_2020/micom. Press `?` to get a list
of available live options such as slide overviews and speaker mode. Note that
some slides are grouped vertically, you can navigate the presentation using
the directional buttons on your keyboard.
A [PDF version](part2.pdf) (lacks the output previews) is also available.


# For teachers

## Use case

The course is meant to use all equipments available to the students so they
can be encouraged to open it on their smartphone (landscape mode looks better)
while they run commands on the terminal.

It focuses on the command line
interface of Qiime 2 and basically works with the command line alone. So it should
be usable even if you use a server or cloud deployment of Qiime 2. Make sure
to give clear instructions how to connect to the server across different operating
systems though :point_up:

In order to minimize the need to transfer files between a server and the local
machine all output is pre-generated and the visualizations are included directly
in the presentation.

## Technicalities

### How does it work?

The presentation itself is a webpage hosted on GitHub Pages. It basically
renders dynamically from a [markdown file that includes the course](docs/talk.md).
Editing the markdown file is sufficient to change the content of the presentation.

See the [reveal docs](https://github.com/hakimel/reveal.js/#markdown) for more info.

### Preview locally

Open a terminal in the `docs` folder in the repo and use:

```bash
python -m http.server
```

This will preview the talk at `localhost:8000` in a browser. Editing the
markdown and reloading the page should be enough.

### PDF output

To generate a PDF of the course open up the website in chromium or chrome and
append `?print-pdf` to the address. For instance if you ran it locally as
described above open `localhost:8000?print-pdf` in the browser. Then choose
print to PDF with the browser (choose margins: none).



