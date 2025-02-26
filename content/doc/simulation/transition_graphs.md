---
title: Transition graphs
date: 2019-07-18T12:58:00Z
summary: Graphs representing the dynamical behaviour
---


State Transition Graphs
=======================

A State Transition Graph (STG) is a directed graph representing the
dynamical behaviour of a [Logical Regulatory Graph]({{< relref "../lrg/_index.md" >}}).
Nodes of this graph represent possible states of the model, assigning
a value to each component. Arcs of the STG represent transitions from
one state to another (i.e. change of value for one or several components).

For a more formal definition see {{<cite Naldi2011 />}}.



Hierarchical Transition Graphs
==============================

The Hierarchical Transition Graphs (HTG) is an acyclic graph, which provides
a compact representation of the State Transition Graph. It improves on
the [graph of the Strongly Connected Components](TODO/../tools/scc) by merging
linear chains of states (in addition to cycles) into single nodes.

More information on this graph is available in
{{<cite Berenguier2013 />}}.


