---
title: "Main features"
date: 2019/07/18 12:58
weight: 5
style: hg2
---

{{<box class="feat">}}
# Model editor

Build qualitative models in a graphical interface.

![GINsim](/edit.svg#lefty)


The **regulatory graph** represent interactions between biological entities.

**Logical rules** define the dynamical behaviour of each component.

**Annotations** keep track of the underlying knowledge.

Apply **perturbations** to account for mutants or alternative hypothesis.

**Reduce** complex models by hiding intermediate components.

{{</box>}}


{{<box class="feat">}}
# Dynamical analysis

![STG](/simulation.svg#lefty)

Visualize simulation results as **state transition graphs**.

The non-deterministic trajectories represent alternative cell fates.

Efficient identification of some dynamical properties, up to complex models.

**Stable states** and **stable motifs** are attractors of the system.

**Functional circuits** highlight key interactions in the model.

{{</box>}}


{{<box class="feat">}}
# Interoperability

![CoLoMoTo](/colomoto.svg#lefty)

GINsim can load and export models from the **SBML qual** format,
enabling to share them with other software tools.
Its integration in the **CoLoMoTo notebook** enables the definition
of complex, reproducible anlysis workflows.

* Efficient reachability analysis using **pint**,
* Complex reachability analysis using the **NuSMV** model checker,
* Quantification of reachability probabilities using **MaBoSS**,
* 2D modelling of a cellular tissue using **Epilog**.

{{</box>}}

