---
title: "Find path"
date: 2019/07/24 12:58
summary: Define and search for paths in LRGs and STGs
---

The "Find path" action enable the determination of paths between pairs of nodes in a Logical Regulatory Graph or between pairs of states in a Transition Graph.

For both graph types, selecting the "Find path" action in the "Graph" menu, opens a configuration dialog box which allows for the specification of the starting node/state, the target node/state, and optional intermediate nodes/states (using the "+" and "-" buttons to add and remove them, respectively).
Once the set of nodes/states is defined, selecting "Run" will make GINsim compute the shortest path and highlight it on the corresponding LRG/STG.
If several paths exist between these states, the first encountered shortest path is returned.
Additionally, a button is available to alternate between the original LRG/STG colors and the computed path.

{{<fig src="find_path.png" title="Search for a path in the state transition graph">}}
The search tool has found a path from the state <em>0110</em> to <em>0311</em>, involving four steps.
{{</fig>}}

TODO: figure to find path in a LRG

