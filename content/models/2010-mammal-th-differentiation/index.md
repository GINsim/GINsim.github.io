---
title: "Control of Th1/Th2/Th17/Treg cells differentiation"
aliases:
- /node/79
taxon: 
- Mammal
process: 
- Differentiation
refs: 74 | 75 | 58
submitter: C. Chaouiya
supporting_paper: "74"
files: 
- Th_differentiation_full_annotated_model.zginml
- Th_differentiation_reduced_model.zginml
file_descriptions: 
- Complete model
- Reduced version used for reachability analysis
---


Alternative cell differentiation pathways are believed to arise from the
concerted action of signalling pathways and transcriptional regulatory
networks. However, the prediction of mammalian cell differentiation from the
knowledge of the presence of specific signals and transcriptional factors is
still a daunting challenge. In this respect, the vertebrate hematopoietic
system, with its many branching differentiation pathways and cell types, is a
compelling case study.



This model accounts for the regulatory network and signalling pathways
controlling Th cell differentiation.
As most available data are qualitative, it is relied on a logical formalism to
perform extensive dynamical analyses. To cope with the size and complexity of the
resulting network, it is used an original model reduction approach {{<cite "models/75">}},
together with a stable state identification algorithm {{<cite "models/58">}}. To assess the
effects of heterogeneous environments on Th cell differentiation, it is performed a
systematic series of simulations, considering various prototypic environments.


Consequently, it is identified stable states corresponding to canonical Th1,
Th2, Th17 and Treg subtypes, but these were found to coexist with other
transient hybrid cell types that co-express combinations of Th1, Th2, Treg and
Th17 markers in an environment-dependent fashion. In the process, the logical
analysis highlights the nature of these cell types and their relationships
with canonical Th subtypes. Finally, this logical model can be used to explore
novel differentiation pathways in silico.


