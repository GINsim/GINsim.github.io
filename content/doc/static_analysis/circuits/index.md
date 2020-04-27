---
title: Circuit analysis
date: 2019/07/18 12:58
summary: Analyse regulatory circuits
weight: 40
---


Regulatory circuits play crucial roles in the dynamical behaviour of a system.
Indeed, positive circuits are required for the existence of several attractors,
whereas negative circuits may generate cyclic attractors {{<cite Thieffry2007>}}.


Many regulatory graphs currently under study contain a large number of circuits,
but a relatively small number of them often plays a more important role.
In {{<cite Naldi2007>}}, we describe a method to compute a **functionality context**
for all circuits, to determine which circuits are more likely to affect the
attractor configuration of the system.


Note that the functionality contexts identified here give the conditions on the
immediate regulators of the circuits under which it is fully effective. These
conditions may be impossible to maintain according to the dynamical rules of
the model, especially in the case of model perturbations.


Usage
=====

The ``Circuits Functionality`` entry of the ``Action`` menu opens the circuit
analysis dialog. This dialog provides a interface to lookup all circuits in the
regulatory graph or a subset of circuits matching some filtering rules (length,
involved components).

{{<fig src="circuitsConfig.png" title="Select regulatory circuits for analysis">}}
A first dialog enables to select which circuits will be analysed, by specifying
constraints on the length of the circuits or on the involved actors. By default all
circuits are considered.
{{</fig>}}


The dialog then allows to analyse the selected circuits, it will then show the
circuit for which a **functionality context** was found. The analysis can be
repeated for various perturbations.

{{<fig src="circuits.png" title="Result of the functionality analysis">}}
When the analysis is completed, the dialog classifies the
selected circuits, according to their computed sign.
When a circuit is selected, its functionality context is
shown at the bottom of the dialog box.
{{</fig>}}



Availability
============

Circuit analysis was implemented in GINsim 2.3

