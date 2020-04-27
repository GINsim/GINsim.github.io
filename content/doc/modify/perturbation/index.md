---
title: "Perturbations"
date: 2019/07/24 12:58
Summary: Define perturbations of regulatory graphs
---


GINsim facilitates the definition of **perturbations** to define small changes to
the regulation of components in regulatory graphs. A perturbation is a set of
restrictions on the evolution of the activity level of one or several components.


Using Perturbations
====================

Some tools, notably Simulation and Stable state search, include a
perturbation selection panel to apply a perturbation before running.


Definition of Perturbations
============================

Perturbation can be defined using the following configuration panel.
The panel appears upon activation of the ``configure`` button in the
perturbation selection panel.


{{<fig src="perturbations.png" title="Perturbation definition panel">}}
This edition panel considers two types of perturbations: **simple perturbations**
which only affect the activity of a single component, and **multiple perturbations**
which group together a list of simple perturbations.
{{</fig>}}


Simple Perturbations
--------------------

The perturbation definition panel appears on the top-right part of the dialog above
when no simple perturbation is selected, or when clicking the ``+`` button.
To create a perturbation, one must first select the affected component using the combobox.
The restriction configuration panel will then appear, and the perturbation can be added using the ``create`` button.

The activity level of Boolean components can be fixed at ``0`` or at ``1``,
corresponding to the definition of a knockdown or ectopic activity respectively.
Radio buttons allows to choose between these two possibilities.

Multi-valued components offer more possibilities, that can be configured using
a range slider. Their activity level will be restricted in the selected range,
or completely fixed if the range corresponds to a single value.


{{<fig src="booleanperturbation.png" title="Perturbation creation panels">}}
TODO: add multivalued figure figures/mvaluedperturbation.png
{{</fig>}}


This enables the definition of simple perturbations where the activity level of a component is restricted to the selected value(s).

{{<notice note>}}
The definition of more subtle perturbations (conditional knockouts...)
still requires the modifications of the logical parameters. We plan to
add convenient means to define other types of perturbations in the future.
{{</notice>}}

{{<notice warning>}}
Simple perturbations can not be duplicated: when trying to add a 
simple perturbation that is already defined, nothing will happen.
{{</notice>}}



Multiple Perturbations
----------------------

The bottom part of the panel lists multiple perturbations.
Multiple perturbations can be created by selecting several
simple perturbation and clicking the button which appears
in the information panel.
These perturbations can then be ordered and deleted using 
the buttons on the right side.


{{<notice warning>}}
Deleting a simple perturbation will also remove all the
multiple perturbations using it.
{{</notice>}}

