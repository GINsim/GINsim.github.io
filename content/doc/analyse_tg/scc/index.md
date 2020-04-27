---
title: "Strongly Connected Components"
date: 2019/07/24 12:58
Summary: Compute the Strongly Connected Components Graph
---


A [Strongly Connected Component (SCC)](http://en.wikipedia.org/wiki/Strongly_connected_component)
in a graph is a maximal subgraph such that all its components are strongly
connected. Each SCC can either a single node or a set of intertwined cycles
of the original graph.
The SCC graph is a derived graph in which each node represent one of the SCC
of the original graph.	This acyclic graph provides a simplified representation
of the organisation of the original graph. This graph is thus often much more compact.


In GINsim, the graph of the Strongly Connected Components (SCC graph) is often
used to provide a better understanding of the organisation of the attractors in
a [State Transition Graph](/doc/simulation/transition_graphs).
The computation of the SCC graph can be launched through the ``Construct SCC graph``
option of the ``Tools`` menu.
Note that GINsim also provides the [Hierarchical Transition Graph](/doc/simulation/transition_graphs)
dedicated to this problem.

{{<fig src="scc.png" title="Strongly Connected Components graph">}}

Example of Strongly Connected Component Graph (bottom right) and
the corresponding state transition graph (top left). 
The ``Selection Attribute`` tab in the bottom panel shows
the content of the selected SCC (i.e. the list of nodes
in the original graph).
{{</fig>}}


Note that while the ``Construct SCC Graph`` tool is often applied to
[State Transition Graph](/doc/simulation/transition_graphs), it can
also be applied to Regulatory Graphs (or more formally to any type of graphs).


Extract from SCC graph
======================


After computing the SCC graph, another tool enables to recover the subgraph
of the original graph corresponding to the selected nodes in the SCC graph.


To use it, select some nodes in a SCC graph and run the ``Extract subgraph``
action from the ``Graph`` menu.

This tool will open the original graph, and apply a filter to only keep the
selected parts. To work properly it thus requires that the original graph 
had been saved to a file, and that the association between the SCC graph 
and the original graph (maintained by GINsim transparently) is still valid.

