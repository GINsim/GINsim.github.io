---
title: "Interaction functionnality"
date: 2019/07/24 12:58
summary: Verify the consistency of signed interaction with the logical rules
weight: 20
---

Motivation
==========

The ``Compute interaction functionality`` tool determines the correct sign of 
the interactions in a LRG according to the logical rules defined for each node.
These rules, are used to compute the conditions for which a given interaction
has a dual, positive, negative or no effect.

Usage
======

The ``Compute interaction functionality`` entry on the ``Tools`` menu opens
the interaction functionality dialog.
This dialog first provides the option to select a perturbation to be applied
to the model before computing the interaction functionality, and it is divided
into three main sections:

* The **perturbation selection**, where the user can select (and define) perturbations.
* The ``save report`` button, where the user can export a summary table
  of all the conditions of each interaction into a XHTML file, to be visualised 
  in a browser.
* The **execution options**, where the user can run the computation
  and visualise the colors computed by the method or restore the colors
  of the original graph.

{{<fig src="interactionfunctionality.png" title="Example of interaction functionality analysis">}}
**Left:** The interaction functionality dialog box.
**Right:** The logical regulatory graph, where the sign of
the interactions are highlighted.
{{</fig>}}

After running the tool, the logical regulatory graph interactions will change colour
depending on their function. Their colour code representation will be:
**green**, for interactions having an activatory effect;
**red**, for interactions with an inhibitory effect;
**blue**, for interactions having a dual effect;
and **black**, for non-functional interactions.
Additionally, if the user correctly (incorrectly) defined the sign of the interaction,
this will be represented in normal (increased) thickness.

Report
======

The interaction functionality report is saved to a XHTML file which contains:

* A **summary table**, where for every interaction, it shows the source and
  target node, the user defined sign and the computed sign.
* A **detailed table**, where for every interaction, and for all the valuations
  of the regulators of the target node, it shows the cases for which the
  specific interaction is functional.

{{<fig src="interactionfunctionality-context.png" title="Example of an functionality context of an interaction">}}
For all the valuations of all regulators of target node gB,
the cases for which the interaction gA -> gB is functional are shown.
{{</fig>}}

Availability
============

This feature was implemented in GINsim 3.0.

