---
title: "Control of Th1/Th2/Th17/Treg/Tfh/Th9/Th22 cell differentiation"
aliases:
- /node/185
taxon: 
- Mammal
- Blood cells
- T lymphocytes
process: 
- Differentiation
submitter: Pedro Monteiro
supporting_paper: "184"
files: 
- Frontiers-Th-Full-model-annotated.zginml
file_descriptions: 
- Complete Model
---


Logical modeling has proven suitable for the dynamical analysis of large
signaling and transcriptional regulatory networks. In this context, signaling
input components are generally meant to convey external stimuli, or
environmental cues. In response to such external signals, cells acquire
specific gene expression patterns modeled in terms of attractors (e.g. stable
states). The capacity for cells to alter or reprogram their differentiated
states upon changes in environmental conditions is referred to as cell
plasticity.



This model in an extended version of a published logical model of
T-helper cell differentiation and plasticity, which accounts for novel
cellular subtypes. The model encompasses 20 signaling pathways, a dozen of
transcription factors, and about 30 cytokines, amounting to 101 components in
total.



Computational methods recently developed to efficiently analyze large models
are first used to study static properties of the model (i.e. stables
states). Symbolic model checking is then applied to get further insights into
reachability properties between Th canonical subtypes upon changes of specific
prototypic environmental cues.



The model reproduces novel reported Th subtypes (Tfh, Th9, Th22) and predicts
additional Th hybrid subtypes in term of stables states. Using the model
checker NuSMV-ARCTL, an abstract view of the dynamics, called reprograming
graph, is produced providing a global and synthetic view of Th plasticity. The
model is consistent with experimental data showing the polarization of naïve
Th cells into the canonical Th subtypes. The model further predicts
substancial plasticity of Th subtypes depending on the signalling environment.


