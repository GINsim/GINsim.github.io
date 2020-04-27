---
title: "T-helper cell plasticity"
summary: Model checking to assess Th plasticity
aliases:
- /node/181
---


This page describes the analysis of a
[model of Th differentiation and plasticity ](/models/2014-mammal-th-differentiation/).

The model encompasses 20 signaling pathways, a dozen of transcription factors,
and about 30 cytokines, amounting to 101 components in total.

It is composed by several layers, namely:

* the cytokine inputs along with the Antigen Presenting Cells (APC);
* the cytokine receptors and their subchains, along with the T cell receptor
  (TCR) and the co-stimulatory receptor CD28;
* the intracellular signaling factors, including "Stat" family proteins 
  (Stat1, Stat3, Stat4, Stat5, Stat6), the TCR and co-stimulatory signaling
  components (NFAT, IκB, NFκB), the master regulators (Tbet, Gata3, Rorγt,
  Foxp3, Bcl6), along with additional transcription factors involved in Th
  differentiation (cMaf, PU.1, Smad3, IRF1, Runx3);
* the main cytokines secreted by Th cells;
* a component modeling the proliferation of the cell.


# Model analysis

To reproduce the model analysis results:

* open the T-helper cell full model with GINsim, and perform the strict reduction 
  using the already selected components to be reduced;
* perform a stable state analysis to obtain the 82 context-dependent stable states;
* export the reduced model to NuSMV format;
* specify the properties, used in the manuscript, at the end of the NuSMV model
  specification file;
* download the [NuSMV-ARCTL model checker](http://lvl.info.ucl.ac.be/Tools/NuSMV-ARCTL-TLACE)
  (an extension of NuSMV which supports the verification of ARCTL temporal formulas);
* perform the verification of the NuSMV model specification file.


NuSMV only supports the simultaneous verification of multiple properties if and only if they all share the same (set of) initial state(s). It is therefore advisable to specify as many NuSMV model specification files, as the number of different (set of) initial state(s). 


# NuSMV specification file example

As an example, we provide a NuSMV specification file for the T-helper cell reduced model,
containing properties specified as ARCTL formulas at the end.
These ARCTL formulas correspond to instantiation of the generic property 1,
specified in section 3.3 of the main manuscript:

INIT c1; EAF(e)(c2 ∧ AAG(e)(c2)),

where c1 corresponds to the definition of the cell type Th0,
c2 (e) corresponds to all the possible Th patterns (input conditions)
defined in Table 2 (Table 3) of the main manuscript.
Meaning that it will test the reachability of all Th patterns under all
input conditions from the Th0 cell type.

Download the [NuSMV specification file](2014-Frontiers-Th_reduced_INIT_Th0.smv).


# Building the reprogramming graph

Once the NuSMV specification files for all Th subtypes (Th0, Th1, Th2, Tfh, Th9,
Th17, Th22 and Treg) are generated, with the corresponding ARCTL properties,
one should run NuSMV-ARCTL for each of the Th subtypes file.

One can then build a reprogramming graph, where the Th subtypes represent the nodes,
and the ARCTL properties that are evaluated as true represent the authorized transitions.

In Figure 3 of the manuscript, we represent this reprogramming graph with labels on the
transitions, indicating which input conditions were present for the verification of each
specific reachability property.

The representation of the graph in Figure 3 of the manuscript was done using Tikz.
In alternative we could have used Graphviz or other similar software.

