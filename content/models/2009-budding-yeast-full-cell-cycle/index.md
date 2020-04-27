---
title: "Budding yeast cell cycle (Fauré et al. 2009)"
aliases:
- /node/21
taxon: 
- Yeast
- Budding yeast
process: 
- Cell cycle
submitter: Adrien Fauré (C. Chaouiya)
supporting_paper: "20"
files: 
- coupled_budding_yeast_CC.zginml
file_descriptions: 
- Logical model combining the budding yeast core cycling engine with the morphogenetic checkpoint and a detailed exit module
---


Leaning on former models, we have defined a logical model for three regulatory
modules involved in the control of the mitotic cell cycle in budding yeast,
namely the core cell cycle module, the morphogenetic checkpoint, and a module
controlling the exit from mitosis. Consistency with available data has been
assessed through a systematic analysis of model behaviours for various genetic
backgrounds and other perturbations.



Here, we take advantage of compositional facilities of the logical formalism
to combine these three models in order to generate a single comprehensive
model involving over thirty regulatory components. The resulting logical model
preserves all relevant characteristics of the original modules, while enabling
the simulation of more sophisticated experiments.



Chen et al (2004) {{<cite "models/22">}} discussed the possibility to graft 
the model of the morphogenesis checkpoint published in a "companion study"
by Ciliberto et al (2003) {{<cite "models/23">}} to their model of the cell
cycle, and to replace the hypothetical PPX by a more accurate version of the
network controlling mitotic exit. We have adapted all three modules in the
logical formalism, and coupled them together.



We have kept and left unchanged all components that were specific of the MCP
module (Mih1, Swe1, Mpk1 and Hsl1), and similarly, all components specific of
the core model. Among the components that were shared by both modules, MASS,
MBF and the BUD received no input from the variables specific of the MCP,
while their regulation amounted to a simplification of what had been proposed
in the core cycling engine model. Hence, we kept these variables and their
regulation from the core model and left them unchanged in the coupled model.
In contrast, in the coupled model, CycB get inputs from components specific of
each of the two modules. Moreover, in the MCP module, CycB is Boolean, whereas
it is multilevel in the core model. Based on the parameters of CycB in each of
the modules, we determined that CycB would have to satisfy the two sets of
conditions to be active in the coupled model. Consequently, the logical
formula giving the conditions of activation of CycB in the coupled model
amounts to a logical AND between its formulas in the core cycling engine and
in the MCP module. The main characteristics of the behaviour of the two
original modules are conserved in the coupled model, in the case of the
wild-type as for the different mutations simulated.



The next step was to fuse the exit module to the core cycling engine. We
followed the same method as with the coupling of the MCP. The first step was
to identify which components and interactions were to be kept in the coupled
model. Obviously, we chose to discard the hypothetical PPX, along with the
parameters of the components of the exit network that were present in the core
model (Net1, Cdc14, Tem1, Bub2-Bfa1, Cdc15 and Pds1), to replace them with
their equivalents from the new exit module, including the SeparaseEsp1,
PP2ACdc55 and Cdc5Polo that were not present in the core model. The logical
rules for Clb2, Cdh1 and Cdc20 in the exit module amount to simplifications of
their counterparts in the core model, so we kept the core model wiring and
regulation in the coupled model for these components. Last but not least, we
added regulation from Sic1 and Cdc6 towards Clb2 new targets to represent
sequestration of the cyclins by the CKI (see the [core cycling engine
model](../25) for more details). The resulting model fits the more recent
data used to built the exit module, and the behaviour of the core model is
preserved. Still, one difficulty arose regarding mutant simulations for the
exit module: the two mutants involving Cdk inhibition (see Queralt et
al., supplementary figure S6.4 {{<cite "models/24">}}) could not be simulated in
the coupled model, as inhibition of Cdk1 / Clb2 is the signal for cytokinesis in
this model. This points out towards the "TARGET model" hypothesis discussed in
Chen et al, where the trigger for cytokinesis would involve both a decrease of
Cdk1/Clb2 kinase activity and an increase in Cdc14 phosphatase activity.


