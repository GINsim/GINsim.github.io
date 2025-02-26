---
title: "Extract STG from HTG"
date: 2019-07-24T12:58:00Z
Summary: Build the STG underlying parts of a HTG
---


Starting from the Hierarchical Transition Graph (HTG) it is possible to 
generate the underlying STG.
The generated STG will contain all the states and edges corresponding 
to the set of selected hierarchical nodes.
The computed STG can also be extended to the states in the immediate neighborhood 
of the states of the selected hierarchical nodes.


Node selection in the HTG
-------------------------

Once the HTG is generated, it's possible to select the set of HTG nodes to be expanded, using the mouse together with the ``Ctrl`` (``Cmd`` on Mac OS X) key pressed.

After the selection of nodes, the ``HTG expansion`` tool can be launched through the ``Expand hierarchical nodes`` option of the ``Tools`` menu.


{{<fig src="htgExpandSelection.png" title="Selection of HTG nodes">}}
Selection of HTG nodes to be expanded in the corresponding STG.
{{</fig>}}



Running the STG extraction tool
-------------------------------

{{<fig src="htgExpandDialog.png" title="STG extraction dialog">}}
Dialog used to run the STG extraction tool.
This dialog presents an option to include the states in the immediate neighborhood of the selected states, and another for the definition/selection of perturbations to the model.
{{</fig>}}

The ``Expand hierarchical nodes`` option of the ``Tools`` menu,
will open a dialog GUI where the user is presented with two options:

* The option to include the states in the immediate neighborhood of the
  selected states, enriching the resulting STG;
* The option to define and/or select a perturbation to be applied to the
  model, which will affect transitions between states in the STG.


