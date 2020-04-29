---
title: "T cells response to CTLA4 and PD-1 checkpoint inhibitors"
aliases:
- /node/238
- /model/tcell-checkpoint-inhibitors-tcla4-pd1
taxon: 
- Mammal
process: 
- Differentiation
submitter: A. Naldi
supporting_paper: "Hernandez2020"
files: 
- Hernandez_TcellCheckPoints_13april2020.zginml
file_descriptions: 
- GINsim model
---

This comprehensive model integrates the available data on T cell activation,
taking into account CTLA4 and PD-1 checkpoint inhibitory pathways.
It encompasses 216 components and 451 regulatory arcs.

To ease the verification of the behaviour of this large logical model, we have designed
a modular approach based on a unit testing framework used in software development.
Furthermore, to compare the respective impact of the activation of the two checkpoints,
we have designed a value propagation technique enabling the analytical computation of all
the nodes frozen following the persisting activation or inhibition of any model component.
The model verification approach greatly eased the delineation of logical rules complying with
predefined dynamical specifications, while the use of the value propagation technique provided
interesting insights into the differential potential of CTLA4 and PD-1 immunotherapies.

All our analyses have been implemented into two python notebooks, enabling their reproduction
or extension with the most recent version of the CoLoMoTo Docker image (http://www.colomoto.org/notebook).

