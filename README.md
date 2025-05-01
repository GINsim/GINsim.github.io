# Website for GINsim (Gene Interaction Network Simulator)

[](docs/ginsim.svg)

This repository generates the website for GINsim 
at [https://ginsim.github.io/](https://ginsim.github.io/) using MkDocs.

You if you want to test/run it locally, you need to install some dependencies using `pip`.

## Preparation

### Create a virtual environment

However, some distributions prevent the installation of `pip` packages system-wide.
If you're in this situation, please install/use a virtual environment.

Most likely you have the latest Python version. In this case, it suffices to run:
```
$ python -m venv myenv
$ source myenv/bin/activate
```

Alternatively, if you need a bit more flexibility you will need to install the package `virtualenv` and then run:
```
$ virtualenv myenv
$ source myenv/bin/activate
```

### Install mkdocs

Please install the necessary `Python` dependencies:
```
pip install mkdocs               # the website static generator
pip install mkdocs-material      # the site theme
pip install mkdocs-bibtex        # for bibliography support 
pip install mkdocs-macros-plugin # automatic generation of model repository
```

## Running mkdocs

If all the necessary dependencies are installed, you can now run `mkdocs` using the _live preview_ mode, where every file change that you do is immediately reflected on the webpage.

```
mkdocs serve
```
and see the following link where the GINsim website is being locally served:
```
INFO    -  [10:28:04] Serving on http://127.0.0.1:8000/
```

## Updating the website

### Website structure

The website has the following structure:
```
docs/
├── contact
├── css
├── documentation
│   ├── analyses
│   ├── dyn
│   ├── formats
│   ├── gui
│   ├── introduction
│   ├── layouts
│   └── lrg
├── install
└── models
```


### Adding a model

In `docs/models/` create a new directory, and put your model files and images inside the directory.
Create an `index.md` file inside respecting the format exemplified in the following example:
```
---
title: Blabla model of blabla
taxon: 
- SomeTaxon
- YetAnotherTaxon
process: 
- SomeProcess
- YetAnotherProcess
submitter: T. MyName
supporting_paper: KeyInBibTex
files: 
- GINsim_model_file.zginml
- SBML_model_file.smbl
file_descriptions: 
- GINsim logical model of blabla
- SBML-qual model of blabla
---

This is a description of the model ...

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
```

### Updating the [https://ginsim.github.io/](https://ginsim.github.io) website

Just commit your files, and the github pages workflow will run `mkdocs` and update the site in a few minutes.
You can check the status of the page build and deployment in the [Actions tab](https://github.com/GINsim/GINsim.github.io/actions) of github repository.

