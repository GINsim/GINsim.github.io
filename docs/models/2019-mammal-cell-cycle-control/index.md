---
title: "Comprehensive Boolean model of the mammalian cell cyle control network"
taxon: 
- Mammal
- Human
process: 
- Cell cycle
- Signalling
submitter: Pedro Monteiro
supporting_paper: "255"
files: 
- CellCycleControl_Sizek_PCB_2019.zginml
- CellCycleControl_Sizek_PCB_2019.sbml
file_descriptions: 
- Sikek 2019 cell cycle archive file to be open with GINsim version >=3.0
- Sikek 2019 cell cycle model file in sbml-qual format (xml file)
---

Published by Sizek et al. in 2019, this Boolean model encompasses 87 components representing different molecular species and cellular processes involved in the regulation of cell proliferation versus apoptosis for a generic human cell. The authors conceived this complex model as an association of different functional modules:

- Growth Signalling module (green nodes): incorportates growth signalling pathways driving cell cycle commitment, responsible for modeling the dynamics of PI3K, AKT1, MAPK and mTORC.
- Restriction Switch (blue nodes): responsible for commitment to DNA synthesis.
- Origin Licensing switch (yellow nodes): responsible for licensing and firing of replication origins.
- Phase Switch (pink nodes): responsible for modeling cell cycle progression (G2 -> M -> G1). The switch was expanded to incorporate for the role of Polo like kinase 1 (Plk1) during mitosis.
- Apoptosis Switch (red nodes): responsible for modeling cell survival versus apoptosis.
- Cellular processes (orange nodes): helps to identify the phenotypic state and include some regulatory mechanisms.

The resulting model reproduces hyperactive PI3K-driven cytokinesis failure and genome duplication and predicts the molecular drivers responsible for these failures by linking hyperactive PI3K to mis-regulation of Polo-like kinase 1 (Plk1) expression late in G2.



