---
title: "Graph selection"
date: 2019/07/24 12:58
summary: Handle the selected items in a graph
---

The [interactive graph view](../graph) lets the user select one or multiple
components (nodes or edges). The selection affects the surrounding graphical interface (properties for
the selected element(s) is shown), as well as some actions which use the selected components as input.


# Interactive selection

Components can be selected directly on the graph view: clicking on a component selects it.
Note that a simple click will first clear the current selection. Maintaining the
``control`` key allows to add or remove components to the selection.


# Selection tools

The ``Graph`` menu contains submenus to update the selection.
The classical ``Select all`` and ``Invert selection`` are provided and can be
restricted to nodes or edges. The ``Extend selection`` submenu allows to add
neighbour items to the current selection.

