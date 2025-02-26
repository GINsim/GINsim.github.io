---
title: "Reversal"
date: 2019-07-24T12:58:00Z
Summary: Compute a LRG generating the reversed asynchronous dynamics
---


The model reversal tool constructs a model in which the asynchronous successors of a state
correspond to it's predecessors in the original model.

Multivalued models are supported through model booleanization,
with some further transformations to prevent the introduction
of non-admissible successor states.


Usage
=====

The model reversal tool is available in the ``Actions`` menu.


Availability and further reading
=================================

This method was implemented in GINsim 3.0.
The backend is implemented in `BioLQM <http://colomoto.org/biolqm>`_,
enabling its programmatic use.

