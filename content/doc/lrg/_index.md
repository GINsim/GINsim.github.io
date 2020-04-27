---
title: "Logical Regulatory Graphs"
date: 2019/07/24 12:58
summary: Define regulatory graphs
weight: 2
---

Informally, a Logical Regulatory Graph (LRG) is a directed labelled multigraph 
representing interactions (the edges) between genes (the nodes).
Each interaction involves two genes, the source and the target, becoming active
whenever its source reaches a given level.

The activation level of each component is defined by a regulatory function
comprising parameters relative to all regulators of this component.

For a more formal definition see {{< cite Naldi2011 >}} or {{< cite Thieffry2007 >}}.

