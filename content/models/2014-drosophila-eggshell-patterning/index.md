---
title: "Drosophila eggshell patterning"
aliases:
- /node/175
- /model/eggshell_patterning
taxon: 
- D. melanogaster
process: 
- Development
submitter: C. Chaouiya
supporting_paper: "174"
files: 
- phenomenological_cellular.zginml
- mechanistic_cellular.zginml
file_descriptions: 
- Single cell phenomenological model
- Single cell mechanistic model
---


The Drosophila eggshell constitutes a remarkable system for the study of
epithelial patterning, both experimentally and through computational modeling.
Dorsal eggshell appendages arise from specific regions in the anterior
follicular epithelium that covers the oocyte: two groups of cells expressing
broad (roof cells) bordered by rhomboid expressing cells (floor cells).
Despite the large number of genes known to participate in defining these
domains and the important modeling efforts put into this developmental system,
key patterning events still lack a proper mechanistic understanding and/or
genetic basis, and the literature appears to conflict on some crucial points.
We tackle these issues with an original, discrete framework that considers
single-cell models that are integrated to construct epithelial models. We
first build a phenomenological model that reproduces wild type follicular
epithelial patterns, confirming EGF and BMP signaling input as sufficient to
establish the major features of this patterning system within the anterior
domain. Importantly, this simple model predicts an instructive juxtacrine
signal linking the roof and floor domains. To explore this prediction, we
define a mechanistic model that integrates the combined effects of cellular
genetic networks, cell communication and network adjustment through
developmental events. Moreover, we focus on the anterior competence region,
and postulate that early BMP signaling participates with early EGF signaling
in its specification. This model accurately simulates wild type pattern
formation and is able to reproduce, with unprecedented level of precision and
completeness, various published gain-of-function and loss-of-function
experiments, including perturbations of the BMP pathway previously seen as
conflicting results. The result is a coherent model built upon rules that may
be generalized to other epithelia and developmental systems.



Here, we provide the two single cell models (phenomenological and
mechanistic).
The multicellular model versions are further available in the
[EpiLog model repository](http://epilog-tool.org/model/eggshell_patterning).
The Python prototype to simulate epithelial models together with all model
files are given on a [different page](http://ginsim.org/node/176/).


