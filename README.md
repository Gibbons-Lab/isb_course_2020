![GitHub release](https://img.shields.io/github/tag/Gibbons-Lab/ccmb_workshop.svg)
![Qiime 2 version](https://img.shields.io/badge/Qiime%202%20version-2018.11-blue.svg)
[![Website](https://img.shields.io/website-up-down-green-red/https/shields.io.svg?label=website)](https://gibbons-lab.github.io/ccmb_workshop)

# Data and Materials for CCMB workshop 2018

You can see the actual workshop walkthrough at
https://gibbons-lab.github.io/ccmb_workshop. Press `?` to get a list
of available live options such as slide overviews and speaker mode. Note that
some slides are grouped vertically, you can navigate the presentation using
the directional buttons on your keyboard.
A [PDF version](workshop.pdf) (lacks the output previews) is also available.

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

## Output

All output generated during the walkthrough can be found in the
[treasure chest](treasure_chest). The easiest way to get all of that
is to [download the entire repository](https://github.com/Gibbons-Lab/ccmb_workshop/archive/master.zip).

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

### Reproducibility

In order to ensure all commands in the presentation actually run there is a
[pytest](https://pytest.org/) setup that does the following things:

1. Extract all commands marked as bash or python and builds up a shell file
   running them all ([commands.sh](./commands.sh). Other languages are ignored,
   so you can use this to include optional or do-not-run commands.
2. Runs all commands individually in pytest and reports eventual errors.

To run the pytest setup you need pytest installed (available on conda or pip)
and call:

```bash
py.test test_commands.py
```

So in essence it should be enough to add new commands to the markdown file and
run the tests in order to verify that everything works as expected.


