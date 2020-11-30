---
title: "Immunogenic Cell Death"
aliases:
- /node/242
- /model/ICD
taxon: 
- Mammal
process: 
- Cancer
submitter: Aurelien Naldi
supporting_paper: "241"
files: 
- ICD_phenomenological.bnd
- ICD_phenomenological.cfg
- ICD_phenomenological.upp
- ICD_phenomenological.ipynb
- ICD_extend.bnd
- ICD_extend.cfg
- ICD_extend.upp
- ICD_extend.ipynb
file_descriptions: 
- Phenomenological model: MaBoSS network description
- Phenomenological model: MaBoSS configuration
- Phenomenological model: UPMaBoSS population definition
- Phenomenological model: Analysis notebook
- Extended model: MaBoSS network description
- Extended model: MaBoSS configuration
- Extended model: UPMaBoSS population definition
- Extended model: Analysis notebook
---



This Boolean model covers the major cell types that intervene in immunogenic cell death (ICD), namely cancer cells, DCs, CD8+ and CD4+ T cells.
This model integrates intracellular mechanisms within each individual cell entity, and further incorporates intercellular communications between
them. The resulting cell population model recapitulates key features of the dynamics of ICD after an initial treatment, in particular the 
time-dependent size of the different cell populations.

Model dynamics has been simulated by means of a software tool, UPMaBoSS, which performs stochastic simulations with continuous time, considering 
the dynamics of the system at the cell population level with appropriate timing of events, and accounting for death and division of each cell type.

With this model, the time scales of some of the processes involved in ICD, which are challenging to measure experimentally, have been predicted. 
In addition, model analysis led to the identification of actionable targets for boosting ICD-induced antitumor response.

All computational analyses and results are compiled in interactive notebooks which cover the presentation of the network structure, model simulations, 
and calculations of parameter sensitivity analyses.

