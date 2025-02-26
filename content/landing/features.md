---
title: "Main features"
date: 2019-07-18T12:58:00Z
weight: 5
style: hg2
---

{{<box class="feat">}}
# Model editor

Build qualitative models in a graphical interface.

![GINsim](/edit.svg#lefty)


The [regulatory graph](doc/lrg) represent interactions between biological entities.

[Logical rules](doc/lrg/rules) define the dynamical behaviour of each component.

[Annotations](doc/lrg/annotations) keep track of the underlying knowledge.

Apply [perturbations](doc/modify/perturbation) to account for mutants or alternative hypothesis.

[Reduce](doc/modify/reduction) complex models by hiding intermediate components.

{{</box>}}


{{<box class="feat">}}
# Dynamical analysis

![STG](/simulation.svg#lefty)

Visualize simulation results as [state transition graphs](doc/simulation/transition_graphs).

The non-deterministic trajectories represent alternative cell fates.

Efficient identification of some dynamical properties, up to complex models.

[Fixed points](doc/static_analysis/fixpoints) and [trap spaces](doc/static_analysis/trapspaces) are attractors of the system.

[Functional circuits](doc/static_analysis/circuits) highlight key interactions in the model.

{{</box>}}


{{<box class="feat">}}
# Interoperability

![CoLoMoTo](/colomoto.svg#lefty)

GINsim can load and export models from the [SBML qual](https://sbml.org/documents/specifications/level-3/version-1/qual/) format,
enabling to share them with other software tools. Its integration in the [CoLoMoTo notebook](http://colomoto.org/notebook) enables
the definition of complex, reproducible anlysis workflows.

* Efficient reachability analysis using [pint](http://loicpauleve.name/pint),
* Complex reachability analysis using the [NuSMV model checker](https://nusmv.fbk.eu),
* Quantification of reachability probabilities using [MaBoSS](https://maboss.curie.fr),
* 2D modelling of a cellular tissue using [Epilog](http://epilog-tool.org).

{{</box>}}

