---
title: "Multilevel mammalian cell cycle model"
aliases:
- /node/189
taxon: 
- Mammal
process: 
- Cell cycle
refs: 3
submitter: Pedro T. Monteiro
supporting_paper: "208"
files: 
- Traynard_MultiLevel_MamCC_Apr2016.zginml
- Traynard_MultiLevel_MamCC_Apr2016.sbml
- Traynard_Boolean_MamCC_Apr2016.zginml
- Traynard_Boolean_MamCC_Apr2016.sbml
- Traynard_MultiLevel_MamCC_Apr2016_specsSMV.smv
---


This model is an extension of the seminal model of the G1/S restriction point
control of mammalian cell cycle, published by Fauré et al {{<cite "models/Faure2006">}}.
We used model-checking and computing tree logics (CTL) to progressively refine
Fauré's model in order to fit recent experimental observations. The resulting
model accounts for the sequential activation of cyclins, the role of Skp2, and
emphasizes a multifunctional role for the cell cycle inhibitor Rb.
We provide GINsim and SBML versions of the original multivalued model as well
as of a Boolean translation.

Furthermore, we provide a script containing the main NuSMV queries used in the
article describing the methodology and the resulting revised model.

![](Traynard_MultiLevelMamCC_Oct2015.png)


