---
title: "Initial states"
date: 2019-07-18T12:58:00Z
summary: Define initial states for regulatory graph
---

Named groups of states can be defined for the regulatory graph and used
for example as starting point for the :doc:`simulation`.

{{<fig src="initial_states.png" title="Initial state definition panel">}}
Each line in the table of intial states has a name and provides a value or a range for
one or more components. Components which are not restricted are denoted by stars ("*")
in the table.
{{</fig>}}

Each row of the table corresponds to a set of states, where activity
levels are specified for each component in the corresponding table cell.
Each component can use all of its possible levels (denoted by a star ("*")),
a single level or any subset of levels, separated by semicolons (;).
Intervals can also be defined using a dash ("0-2" denotes all levels from 0 to 2, included).
The special value "m" denotes the maximal level of the component.
For example, "0;2-4" means "0 or values between 2 and 4" and is identical to "0;2;3;4".
"1-m" means "any activity (from 1 to the max)".
The default, denoted by a "*", covers all possible values (it is thus the same as "0-m").


Initial states can be reordered, deleted and duplicated using the buttons on top of the table.

{{<notice tip>}}
A value can be entered in many cells at once using multiple selection.
{{</notice>}}

