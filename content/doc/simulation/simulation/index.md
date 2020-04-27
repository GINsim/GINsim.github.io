---
title: "The simulation"
date: 2019/07/18 12:58
summary: Generate Transition Graphs
---



Once a regulatory model has been defined, a simulation can be launched
through the ``Run Simulation`` option of the ``Action`` menu.
This option triggers a dialog box allowing to choose simulation settings.

{{<fig src="simulation_config.png" title="Simulation settings">}}
This dialog box allows to configure and run the simulation.
{{</fig>}}


This dialog box allows to define simulation settings.
The top part of the dialog box enables the definition of transformations to apply to
the regulatory graph before the simulation.
The left part of the dialog box enables to manage (select, add or remove) simulations settings.
The right part of the dialog box enables the definition of the current simulation setting.


Configure the simulation
=========================

The top part of the simulation dialog enables the selection of a perturbation
to be applied to the regulatory graph before running the simulation. The associated ``Configure``
button will show the :doc:`perturbation definition panel </modify/perturbation>`.

The bottom part of the dialog box is dedicated to the definition of
:doc:`initial_states` of the simulation.
Each row defines a single state or a group of states, and the checkboxes allow
to select the states used for the simulation. If no row is selected, all possible
states are considered, generating a complete state transition graph.


In a given state of the system, one or several genes are called to update their
values. When several changes are pending, different construction strategies lead to
different successor states and thus to different state transition graphs.
GINsim implements the classical <em>synchronous</em> and <em>asynchronous</em>
updating, and enables the definition of ad hoc strategies using <em>priority classes</em>.
These updating modes are described in detail in <link xref="tool-simulation-updating-mode">their documentation</link>.


Simulation settings are saved and restored as associated data in <link xref="format-zginml">ZGINML files</link>.

Running simulations with perturbation
=====================================

{{<fig src="blocking.png" title="Perturbation simulation result">}}
Result of an asynchronous simulation, where the expression level for
Cro has been blocked at 1.
The state transition graph is the same as the original asynchronous one,
but all transitions where Cro leaves this value have been suppressed.
This state transition graph is now composed of two disconnected parts,
with a new stable state.
{{</fig>}}

The "strip output" checkbox next to the perturbation selector enables to
activate automatic removal of all output components from the simulation.
Their value can be retrieved on demand when browsing the resulting 
State Transition Graph. See the <link xref="lrg-modifier-reduction">reduction</link> section for more details.


The "Construction Strategy" panel enables the selection of the type of graph computed
by the simulation (the classical <link xref="transition-graphs#stg">State Transition Graph</link>,
or the more compact <link xref="transition-graphs#htg">Hierarchical Transition Graph</link>).

State Transition Graphs can be computed breadth-first or depth-first.
Both options lead to the same result, unless the simulation is interrupted by
a <link xref="#dslimit">size limit</link> (see below).



Depth and size limitations
==========================

An option is also offered to limit the search depth and/or the total number of
states generated in a simulation.

{{<notice warning>}}
When considering several initial states (or the full STG), some of 
them can be reached while running the simulation from an other state.
In this case, no new search will be triggered for them and the depth
counter will not be reinitialised (i.e. the depth limit for these 
initial states will be shorter).
{{</notice>}}

{{<fig src="stg_depth_limit.png" title="Limitation of the depth in the case of a depth first construction">}}
State transition graph with all reachable states from the state "0111".
The same simulation with a depth limit set to 2 keeps only the initial state
and the nodes at a distance of two or less (i.e. the six white states).
{{</fig>}}

The limit on the total number of states apply to all simulation modes. Under the
asynchronous assumption, this limit has slightly different effects on depth first
and breadth first search.

{{<fig src="stg_size_limit.png">}}
Limitation of the size (depth first and breadth first search construction)
The limit on the total number of nodes has different effects on depth
first and breadth first state transition graphs. These examples show the
graph of the figure above [TODO: figure link] limited to 6
states. The first state transition graph was obtained using the depth
first construction, whereas the second results from the breadth first
one.
{{</fig>}}


Running the simulation
======================

While the simulation is running, the bottom left corner indicates
the size of the generated state transition graph. The simulation
can be interrupted, using the ``Cancel`` button, without loosing
the calculated part of the state transition graph.

At the end of a simulation, several options are available to save,
display or analyse the resulting state transition graph
(see <link xref="gui-whattodo" />).

