# Basins of attraction

The study of attractors (stable states and/or cyclic attractors) of biological regulatory systems relates to its asymptotic behaviours. The identification of such attractors has received some attention from the logical modelling community, yielding several methodologies for its identification.
However, the identification of the corresponding basins of attraction has received less attention, due to the need to explicitly generate the associated dynamics (which is computationally heavy).

Here, we present a methodology to compute the basins of attraction of a given logical model, based on the computation of the reverse dynamics starting from each attractor of interest.

For this, it relies on a set of Python scripts to control the calls to the [boolSim/genYsis](https://www.sib.swiss/vital-it/research-software) simulation tool and the [bioLQM](https://github.com/colomoto/biolqm) Logical Qualitative Models library.

---

## Download

You can get all the necessary code containing the scripts and tools (for MacOSX and Linux) here: [2017-ReverseModels-Code.tgz](2017-ReverseModels-Code.tgz).

    ├── examples
    │   ├── calzone2010
    │   │   ├── Calzone_2010_reduced.sbml
    │   │   └── Calzone_2010.sbml
    │   └── toy_multivalued
    │       └── toymultivalued.sbml
    ├── get_pattern.py
    ├── README_pattern.txt
    ├── README.txt
    ├── reverse_study.py
    ├── TODO_aurelien.txt
    └── tools
        ├── bioLQM
        │   ├── bioLQM-0.4-SNAPSHOT-jar-with-dependencies.jar
        │   └── reverse.js
        ├── boolSim
        │   ├── Linux
        │   │   ├── boolSim
        │   │   └── boolSim_setutils
        │   ├── MacOSX
        │   │   ├── boolSim
        │   │   └── boolSim_setutils
        │   └── README.txt
        └── espresso
            ├── Linux
            │   └── espresso-64bit
            └── MacOSX
                └── espresso-64bit

(Please ensure that you have execution permission on the `boolSim`, `boolSim_setutils` and `espresso-64bit` binaries on your filesystem).

---

## Computing basins of attraction

The Python script `reverse_study.py` from an initial logical model, in the .sbml format, performs the following steps to obtain the basins of attraction.


### a) Boolean/reverse models

Given a logical model `model.sbml`, using the bioLQM Logical Qualitative Models library, it computes:

1. the corresponding Boolean model (it will be the same if all model variables are Boolean the corresponding Boolean), saving it at `model_bool.sbml`;
1. then it takes the Boolean model and computes its corresponding reverse model, saving it at `model_bool_reversed.sbml`.


### b) Attractors

Using the [BoolSim](https://www.sib.swiss/vital-it/research-software) simulation tool, it takes the Boolean model `model_bool.sbml` and computes all reachable attractors, saving them with the following filenames:

    model_attractor_1.txt
    ...
    model_attractor_2.txt


### c) Basins of attraction

Using the reverse Boolean model `model_bool_reversed.sbml`, for each of the attractors found at step b), it computes all the reachable states. The states reachable from the attractor using the reverse Boolean model, will correspond to the states defining the basin of attraction in the original Boolean model. Each of these sets of states are saved with the following filenames:

    model_reached_1.txt
    ...
    model_reached_n.txt


### d) Strict basins of attraction

In the case of more than one attractor (and basin of attraction), it uses the `boolSim_setutils` to compute differences between all basins of attraction and obtain the strict basin of attraction of each attractor.
Each of these sets of states are saved with the following filenames:

    model_reached_strict_1.txt
    ...
    model_reached_strict_n.txt

### Usage

You can launch the `reverse_study.py` Python script to obtain to compute the (strict) basins of attraction for more than one model file, in the following manner:

    $ python reverse_study.py model1.sbml model2.sbml


---

## Minimising patterns

The Python script `get_pattern.py` permits to take a set of input files, containing a set of patterns/states, and obtain a minimal set of patterns (if possible) representing the initial set of patterns/states.

In order to do this, it relies on the tool `ESPRESSO` heuristic logic minimizer (Brayton et al., 1984, Logic Minimization Algorithms for VLSI Synthesis, Kluwer Academic Publishers).

### Input formats

Each input file must have a .txt extension, and must be either an output file from BoolSim or an output file from `ESPRESSO`.
The script takes the filename `<some_file.txt>` and writes the output in a filename `<some_file_pattern.txt>`.


### BoolSim output file

BoolSim output files describe a set of states/patterns as a matrix, where each line represent a state/pattern and each column represents the values of a given component throughout all states/patterns. This is the transposed output representation (`--transpose` option enabled). Without it, columns describe states/patterns and lines describe components.
Value **2** is used to represent both values 0 and 1.

    GeneA GeneB GeneC GeneD
    1     0     2     0
    0     2     1     0
    1     1     1     0


### ESPRESSO output file

ESPRESSO output files also describe a set of states/patterns as a matrix, where each line represent a state/pattern and each column represents the values of a given component throughout all states/patterns (following the transposed BoolSim representation). It contains some additional information, like the number of variables and the number of patterns found.
Here, symbol **-** is used to represent both values 0 and 1.

    .i 4
    .o 1
    .p 2
    --10 1
    10-0 1
    .e


### Output format

The `get_pattern.py` produces a possibly minimal representation of a set of states/patterns as a file with [tab-separated values](https://web.archive.org/web/20250124073127/https://en.wikipedia.org/wiki/Tab-separated_values), having a .tsv extension.
This file can be easily imported in a spreadsheet software (e.g., Excel or Libreoffice).
Symbol ***** is used to represent both values 0 and 1.

    GeneA GeneB GeneC GeneD
    *     0     1     0
    1     0     *     0

The first line containing the information regarding the name of each variable, is only generated if the input file is a BoolSim output file, since ESPRESSO does not keep that information.


### Usage

You can launch the `get_pattern.py` Python script to obtain the patterns of more than one file, in the following manner:

    $ python get_pattern.py file1.txt subdir/file2.txt 
    In: file1.txt
        is_espresso
        Pattern: file1_pattern.txt
    In: subdir/file2.txt
        is_boolsim
        has_espresso
        Pattern: subdir/file2_pattern.txt


