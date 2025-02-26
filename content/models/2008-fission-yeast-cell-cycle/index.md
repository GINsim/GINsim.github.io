---
title: "Fission Yeast Cell Cycle (Davidich and Bornholdt, 2008)"
aliases:
- /node/37
taxon: 
- Yeast
- Fission yeast
process: 
- Cell cycle
refs: 36 | 30
submitter: Adrien Fauré (C. Chaouiya)
supporting_paper: "30"
files: 
- fissionYeastDavidich2008.zginml
- fissionYeastDavidich2008Modified.zginml
file_descriptions: 
- Fission Yeast cell cycle (from Davidich & Bornholdt)
- Fission Yeast cell cycle (adapted from Davidich & Bornholdt)
---


This model is a direct transcription of the Boolean model published by
Davidich & Bornholdt {{<cite "models/36" />}}. Dynamical rules are defined
on the basis of the network structure, as the sum of the positive and
negative influences exerted on each nodes by its regulators.
(Fig. 1, bottom left in {{<cite "models/30" />}}; see text for more details).


The model yields a main stable state, corresponding to G0/G1, that gathers
most trajectories in the state transition graph; and several alternative,
artefactual states.


The two Boolean components representing the different levels of activity
of Cdc2_Cdc13 have been replaced by a ternary component. In addition, the
loops originally placed on Start, SK, PP, and Slp1 nodes have been removed, as
they do not represent true auto-regulations, and are compensated by the
introduction of priorities to account for the maintenance of the start signal
and its effect on Rum1 and Ste9.


For proper logical rules, the model has a single stable state, corresponding
to the G1 state of Davidich & Bornholdt (with only Ste9, Rum1 and Wee1_Mick1
activated). This means that the other 11 spurious stable states obtained by
these authors have been eliminated.


Activation of Start leads to SK inactivation and then to inhibition of Ste9
and Rum 1, launching a to a sequence of state transitions matching that
defined by Davidich & Bornholdt {{<cite "models/36" />}}, as well as available
kinetic data (see Model Documentation for proper setting of the logical simulation).


