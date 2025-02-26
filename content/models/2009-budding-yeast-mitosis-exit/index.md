---
title: "Budding yeast exit module"
aliases:
- /node/29
taxon: 
- Yeast
- Budding yeast
process: 
- Mitosis exit control
- Cell cycle
submitter: Adrien Fauré (C. Chaouiya)
supporting_paper: "20"
date: 2011-07-01T00:00:00Z
files: 
- exit.zginml
file_descriptions: 
- Exit module of the budding yeast cell cycle
---


This logical model focuses on the network controlling mitotic exit in 
budding yeast. It is inspired by the work of Queralt et al. {{<cite "models/24" />}},
which emphasises the role of PP2A down-regulation by separase in the triggering
of Cdc14 activation during anaphase. 
These authors developed a quantitative model for mitotic exit, integrating evidence
on the roles of FEAR (Cdc Fourteen Early Anaphase Release) components
Cdc5Polo, PP2ACdc55 and Esp1.


This model was then used to update our model for budding yeast core cycling
engine, that relied on an hypothetical inhibitor of Cdc14, called PPX,
activated by Pds1, in place of the FEAR reaction. Our logical model
qualitatively accounts for available data on the wild-type cell cycle, as well
as for nine different cycle perturbations described in Queralt et al, in terms
of Cdc14 activation.

