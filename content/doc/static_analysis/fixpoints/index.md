---
title: Fixed points
date: 2019-07-18T12:58:00Z
summary: Identify fixed points (stable states)
weight: 40
---


This tool allows the analytic (i.e. without running a simulation) determination
of stable states of the model. All stable states are determined, regardless of
their reachability {{<cite Naldi2007 >}}.

This tool allows the analytic (i.e. without running a simulation) determination of
trapspaces of the model. These trapspaces contain the stable states, as well as an
approximation for complex attractors.

Usage
=====

The stable state identification tool is available from the ``Compute stable states``
option of the ``Tools`` menu.
The stable states dialog box allows to run the analysis after the optional
selection of a perturbation. The result is shown in a table in the same dialog box, allowing
to launch a novel analysis for another perturbation. A "*" in the table denotes that
each of the values of this component gives rise to a stable state (or several if another
"*" appears in the same row).

{{<fig src="fixedpoints.png">}}
The stable states dialog box, showing the result of the analysis
{{</fig>}}


Availability
============

Stable state search was first implemented in GINsim 2.3.
The implementation is now part of the 
[bioLQM toolkit](https://colomoto.org/biolqm).


