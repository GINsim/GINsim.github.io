---
title: "Morphogenetic checkpoint of the budding yeast cell cycle"
aliases:
- /node/26
taxon: 
- Yeast
- Budding yeast
process: 
- Cell cycle
- Morphogenetic checkpoint
refs: 23 | 20 | 27
submitter: Adrien Fauré (C. Chaouiya)
supporting_paper: "20"
files: 
- MCP_budding_yeast_CC.zginml
file_descriptions: 
- Morphogenetic checkpoint of the budding yeast cell cycle
---


In budding yeast, the morphogenetic checkpoint (MCP) relies upon inhibitory
phosphorylation of Cdc2/Cyclin B by Swe1 to condition entry into mitosis to
the formation of a bud. Taking inspiration in the ODE model published by
Ciliberto et al. (2003) [1], we have developed a logical model of the MCP,
with the aim to plug it to our [core engine](25) of the budding yeast cell
cycle (cf. [2]).



The activity of Cdc28/Clb2 is controlled by the balance between Swe1 and Mih1.
Swe1, the budding yeast homologue of the tyrosine kinase wee1, inhibits Cdc28
by phosphorylation, whereas the phosphatase Mih1 (homologue of Cdc25) removes
the inhibitory phosphate. Swe1 itself is inhibited by phosphorylation by
Cdc28/Clb2, in a positive feed-back loop. Based on Ciliberto's model, we
assume that Swe1 is also somehow modified by Hsl1, a protein kinase activated
by bud formation, and that this modification of unknown nature - as Swe1 does
not appear to be a substrate of Hsl1- has an inhibitory effect on Swe1. The
checkpoint is reinforced by a MAPK pathway that inhibits Mih1 through Mpk1
activity in absence of a bud. An important point of the MCP is the possibility
for the cell to undergo adaptation, that is to evade the checkpoint and enter
mitosis in absence of a bud after some time. Ciliberto's model supports the
hypothesis that failure to make a bud creates a second threshold for mass for
the G2-M transition (the first threshold being at Start). Mass impacts cell
progression by increasing the synthesis of the cyclins, and in particular CycB
that is required for entry into mitosis (see the core model -LINK- for
details). Here, we have introduced a second threshold for the MASS variable,
to represent the idea that increased CycB synthesis can yield enough CycB
activity to overcome inhibition by Swe1. Our model accounts for the wild-type
as well as 14 mutants phenotypes described by Ciliberto et al. and in Harrison
et al (2001) [3] in terms of entry into mitosis – monitored by Clb2
activation. This model has then been to our model of the core cell cycle
engine of the budding yeast (see [coupled model](21)).


