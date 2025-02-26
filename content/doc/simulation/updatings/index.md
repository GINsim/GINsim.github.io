---
title: "Updating modes"
date: 2019-07-18T12:58:00Z
summary: Updating modes for the simulation
---


In a given state of the system, one or several genes are called to update their
values. When several changes are pending, different construction strategies lead to
different successor states and thus to different state transition graphs.

Synchronous mode
=================

In this mode, all updating calls are performed simultaneously.
This simplification may generate artefacts in the state transition graph.

Each state has then at most one successor state, which encompasses fully
updated gene levels.


Asynchronous mode
=================

In this mode, all changes are performed independantly. It will generate a
state transition graph taking into account any possible trajectories. This mode
is chosen by default.

A given state may have several successor states, each of them corresponding to a
single updating of one gene level.

In this mode, the graph transition state can be generated "depth first" or
"breadth first". The same state transition graph will be built, except if
interrupted (for illustration, see :doc:`depth and size limitation <simulation>`).


{{<fig src="a-sync.png" title="Construction strategy: synchronous versus asynchronous">}}
Samples of simulation results for the lambda4 model, applying
asynchronous and synchronous strategies to the same initial states (all
states where C1=0 and Cro&gt;0). Dotted arcs denote multiple,
simultaneous transitions.
{{</fig>}}


Priority classes
================

This strategy allows the user to group components into different classes, and
to assign a priority level to each of these classes. In case of concurrent
transition calls, GINsim first updates the gene(s) belonging to the class with
the highest ranking. For each class, the user can further specify the desired
updating assumption, which then determines the treatment of concurrent
transition calls inside that class. When several classes have the same ranking,
concurrent transitions are treated under an asynchronous assumption (no
priority).

The creation of a new configuration, using the leftmost "+" button, starts wth some predefined settings:

* The definition of a single class contaning all components, equivalent to the (a)synchronous updating.
* The definition of a fully-ordered updating using a separate class for each component.
* The separation of the increasing and decreasing transition of each components for more fine-grained configurations.


The left part of the configuration dialog box shows a list of priority classes
(see figure below). The name of a class
can be edited and a checkbox allows to change its internal mode from
asynchronous (unchecked) to synchronous (checked). Buttons enable to add (+),
delete (X), order (using the arrows) and group/ungroup priority classes.

The central column lists transitions that belong to the currently selected
class, while the column on the right displays all other transitions (i.e. belonging to
other classes). To add transitions to the selected class, choose them in the
right list an click on the "&lt;&lt;" button. The ``>>`` button removes the
transition selected in the central list from the current class and add them to
the next class in the list (to the first class when the last one is selected).

When multiple classes are selected, they can be assigned the same rank.
Multiple classes with the same rank are treated asynchronously: if all classes
are asynchronous, it is thus equivalent to a single larger class, but it allows
the definition of asynchronous update of multiple synchronous classes as well.

{{<fig src="priorityClass.png" title="Definition of Priority classes" />}}


{{<fig src="dyn_pclass.png" title="Priority Class: example result">}}
Example of simulation by priority classes. Two priority classes
have been created. The highest ranked one is synchronous and
contains C1, C2 and Cro. The other class contains only N. The
resulting state transition graph is splited into two parts: N
expressed *versus* N not expressed.
{{</fig>}}

