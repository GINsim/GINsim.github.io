---
title: "Core engine controlling the budding yeast cell cycle"
aliases:
- /node/25
taxon: 
- Yeast
- Budding yeast
process: 
- Cell cycle
- Core engine
submitter: Adrien Fauré (C. Chaouiya)
supporting_paper: "20"
date: 2006/08
files: 
- core_engine_budding_yeast_CC.zginml
file_descriptions: 
- Core engine controlling the budding yeast cell cycle
---


Leaning on the differential model published by Chen et al. in 2004 {{<cite "models/22">}},
we have delineated a discrete, logical model that reproduces the main qualitative
results reported in this study, in terms of cycle viability or arrest in a
particular stable state, for the wild type as well as over one hundred mutant
conditions.

In a first step, we have defined a regulatory graph encompassing the main
documented interactions between core regulators of the cell cycle (Cdk/cyclins,
APC, Cdk inhibitors).
For proper logical rules, in the wild type situation, our model accounts for
the following sequence of events: firing of the origins of replication (ORI
goes up), spindle alignment (SPN goes up), inhibition of the securin (Pds1
goes down), division (MITOSIS goes up to level 2) after the formation of a bud
(BUD must reach at least transiently the level 1), and origin relicensing (ORI
goes down). This sequence serves as a criterion to evaluate the viability of
the cell. Based on the levels of activity of key variables (Clb5, Clb2, Pds1),
we can divide the cycle into three different phases: G0/G1 (low Clb5 and Clb2
activity, either OFF or sequestered by Sic1/Cdc6), S/G2 (high Clb5 activity,
i.e. not sequestered by the CKI, and low Clb2), and M (high Clb2 activity).
The M phase is itself subdivided into prophase/metaphase (high Pds1, low Esp1,
sister chromatids not separated) and anaphase/telophase (low Pds1, high Esp1).
These rules are used to characterised cell arrests in various mutants.
Although the logical formalism is particularly well suited to represent
information fluxes (activation, inhibition), it is not adapted to the
representation of mass flow, reactant consumption, or complex formation.
Consequently, we represent the complexes implicitly: a complex is considered
present if all its components are present; all components, whether regulatory
or enzymatic subunits, regulate the targets of the enzymatic member, with a
logical AND rule (or AND NOT in the case of sequestration). For example, in
the case of the inhibition of the Clbs by the CKI, we have represented
inhibition of the Clbs by introducing arrows from the CKI towards the Clbs
targets, so that inhibition of the Clbs is represented by an inhibition of the
components they activate and by an activation of the components they inhibit.
In Chen's model, cytokinesis was triggered by a fall of clb2's activity below
a certain threshold. To formulate this rule in the logical formalism, we
introduced a multilevel CYTOKINESIS variable. This variable is fully activated
(level 2) only when CycB is inactivated, either by a decrease of CycB level
from level 2 to level 1, or by an increase of the CKI activity when Clb2 is
still high. To differentiate between a rise and a fall of CycB activity,
CYTOKINESIS has to be pre-activated (up to level 1) by high Clb2 activity
before being allowed to reach level 2. Our model simulations qualitatively
agree with the behaviour reported for the wild-type Yeast, as well as for over
one hundred mutant conditions. This led us to further develop this model by
defining additional regulatory modules such as the [morphogenetic
checkpoint](../26). We also developed a model for [mitotic exit](../29) based on
more recent evidence. The resulting logical models are presented as separate
entries of our model repository. In conclusion, our core cell cycle model
served as a benchmark to assess the power of logical modelling applied to a
complex oscillatory system, as well as the first step towards the development
of a more comprehensive model of the budding yeast cell cycle network
{{<cite "models/23">}}.

