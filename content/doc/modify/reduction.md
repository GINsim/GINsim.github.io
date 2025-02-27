---
title: "Model reduction"
date: 2019-07-24T12:58:00Z
Summary: Removing components from a LRG, preserving dynamical properties
---


The reduction of regulatory graphs allows to extract a "simplified"
regulatory graph where a set of components are hidden. To keep a
consistent dynamical behaviour, the logical rules associated with the
targets of each hidden component account for the (indirect) effects
of its regulators. This construction of reduced models preserves
crucial dynamical properties of the original model, including stable
states and more complex attractors. Furthermore, the relationship
between the attractor configuration of the original model and those
of reduced models is formally established.

Usage
=====

The reduction tool is available in the ``Actions`` menu. It open a
configuration dialog in which the user can select the components
that will be hidden. Several configuration strategies can be defined.
Running the tool leads to the construction of a reduced model where
the selected components have been removed.


Some reductions are not possible (an auto-regulated component can not
be hidden using this method), if a reduction fails, GINsim will show
an error message, listing the components that could not be hidden and
proposing to continue with the result of the partial reduction.


Note that in some cases, the reduction may only be possible in a precise
order (but the result does not not change with the order). When blocked,
GINsim will try alternate orders for the remaining components, but not 
for the components which have already been succesfully reduced. In such
cases, it may be necessary to provide the list of components to reduce in
several steps to force the use of the correct order.


Output stripping
================

Outputs are components which do not regulate others. As such, these
components have no impact on the attractors that will be reached in
a simulation. These output components can be automatically removed
when performing a simulation or some other actions on a model.
To instruct GINsim to remove outputs, use the ``strip outputs`` 
checkbox next to the perturbation selection box.


Script mode
============

The reduction tool can also be used in script mode. It then relies on a previously defined reduction strategy.


Availability and further reading
=================================

This method was implemented in GINsim 2.4 {{<cite Naldi2011 >}}.
The support for output stripping was added in GINsim 3.0 {{<cite Naldi2012 >}}.


