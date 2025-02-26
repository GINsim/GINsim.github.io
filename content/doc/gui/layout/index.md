---
title: "Graph layouts"
date: 2019-07-24T12:58:00Z
summary: Automatic positionning of graph elements
---


The "layout submenu of the "view" menu provides some tools to place graph components automatically.
These layout tools are mostly useful for graphs computed by GINsim, such as  state transition graphs.
Note that GINsim only offers very simple layout tools. For complex cases,
dedicated tools such as graphviz or cytoscape can provide much better results.
The following layouts are available:


## Level layout

Nodes are placed on rows, nodes without any incoming
arc being placed at the top and nodes without any outgoing arc at the bottom.

{{<fig src="levelLayout.png" title="Level layout example">}}{{</fig>}}


## Ring layout

Nodes are placed on three concentric rings, source
nodes at the center, terminal nodes at the periphery.

{{<fig src="ringLayout.png" title="Ring layout example">}}{{</fig>}}


## STG layouts

State transition graphs have additional layout methods which place
components on a grid based on the activity levels.

