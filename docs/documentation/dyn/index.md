### State transition graphs


A State Transition Graph (STG) is a directed graph representing the
dynamical behaviour of a [Logical Regulatory Graph](index.md#logical-regulatory-graph).
Nodes of this graph represent possible states of the model, assigning
a value to each component. Arcs of the STG represent transitions from
one state to another (i.e. change of value for one or several components).

For a more formal definition see [@Naldi2011].


### Simulation

Once a regulatory model has been defined, a simulation can be launched
through the ``Run Simulation`` option of the ``Tools`` menu.
This option triggers a dialog box allowing to choose simulation settings.


!!! example "Simulation settings"
    ![Simulation settings](/documentation/dyn/simulation_config2026.png)

    This dialog box allows to configure and run the simulation.

This dialog box allows to define simulation settings.
The top part of the dialog box enables the definition of transformations to apply to
the regulatory graph before the simulation.
The left part of the dialog box enables to manage (select, add or remove) simulations settings.
The right part of the dialog box enables the definition of the current simulation setting.


### Initial states

Named groups of states can be defined for the regulatory graph and used
for example as starting point for the [Simulation](index.md#simulation).

Each row of the table corresponds to a set of states, where activity
levels are specified for each component in the corresponding table cell.
Each component can use all of its possible levels (denoted by a star ("\*")), a single level or any subset of levels, separated by semicolons (;).
Intervals can also be defined using a dash ("0-2" denotes all levels from 0 to 2, included).
The special value "m" denotes the maximal level of the component.
For example, "0;2-4" means "0 or values between 2 and 4" and is identical to "0;2;3;4".
"1-m" means "any activity (from 1 to the max)".
The default, denoted by a "\*", covers all possible values (it is thus the same as "0-m").


Initial states can be reordered, deleted and duplicated using the buttons on top of the table.

!!! hint
    A value can be entered in many cells at once using multiple selection.


##### Configure the simulation

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

##### Running simulations with perturbation


!!! warning
    I cannot reproduce the same graphics. The legend of the figure below seems not sufficient for me to reproduce. 


!!! example "Perturbation simulation result"
    ![Perturbation simulation result](/documentation/dyn/blocking.png)

    Result of an asynchronous simulation, where the expression level for Cro has been blocked at 1.
    The state transition graph is the same as the original asynchronous one, but all transitions where Cro leaves this value have been suppressed.
    This state transition graph is now composed of two disconnected parts, with a new stable state.


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



##### Depth and size limitations

An option is also offered to limit the search depth and/or the total number of
states generated in a simulation.


!!! warning
    When considering several initial states (or the full STG), some of them can be reached while running the simulation from an other state.
    In this case, no new search will be triggered for them and the depth counter will not be reinitialised (i.e. the depth limit for these initial states will be shorter).


!!! example "Limitation of the depth in the case of a depth first construction"
    ![Limitation of the depth in the case of a depth first construction](/documentation/dyn/stg_depth_limit.png)

    State transition graph with all reachable states from the state "0111".
    The same simulation with a depth limit set to 2 keeps only the initial state and the nodes at a distance of two or less (i.e. the six white states).



The limit on the total number of states apply to all simulation modes. Under the asynchronous assumption, this limit has slightly different effects on depth first and breadth first search.


!!! example "Limitation of STG size"
    ![Limitation of STG size](/documentation/dyn/stg_size_limit.png)

    Limitation of the size (depth first and breadth first search construction).
    The limit on the total number of nodes has different effects on depth first and breadth first state transition graphs. These examples show the graph of the figure above [TODO: figure link] limited to 6 states. The first state transition graph was obtained using the depth first construction, whereas the second results from the breadth first one.


##### Running the simulation

While the simulation is running, the bottom left corner indicates
the size of the generated state transition graph. The simulation
can be interrupted, using the ``Cancel`` button, without loosing
the calculated part of the state transition graph.

At the end of a simulation, several options are available to save,
display or analyse the resulting state transition graph
(see <link xref="gui-whattodo" />).


#### Updating modes

In a given state of the system, one or several genes are called to update their
values. When several changes are pending, different construction strategies lead to
different successor states and thus to different state transition graphs.

##### Synchronous mode

In this mode, all updating calls are performed simultaneously.
This simplification may generate artefacts in the state transition graph.

Each state has then at most one successor state, which encompasses fully
updated gene levels.


##### Asynchronous mode

In this mode, all changes are performed independantly. It will generate a
state transition graph taking into account any possible trajectories. This mode
is chosen by default.

A given state may have several successor states, each of them corresponding to a
single updating of one gene level.

In this mode, the graph transition state can be generated "depth first" or
"breadth first". The same state transition graph will be built, except if
interrupted (for illustration, see :doc:`depth and size limitation <simulation>`).


!!! example "Construction strategy: synchronous versus asynchronous"
    ![Construction strategy: synchronous versus asynchronous](/documentation/dyn/a-sync.png)

    Samples of simulation results for the lambda4 model, applying asynchronous and synchronous strategies to the same initial states (all states where C1=0 and Cro&gt;0). Dotted arcs denote multiple, simultaneous transitions.


##### Priority classes

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


!!! example "Definition of Priority classes"
    ![Definition of Priority classes](/documentation/dyn/priorityClass.png)


!!! example "Priority Class: example result"
    ![Priority Class: example result](/documentation/dyn/dyn_pclass.png)

    Example of simulation by priority classes.
    Two priority classes have been created.
    The highest ranked one is synchronous and contains C1, C2 and Cro.
    The other class contains only N.
    The resulting state transition graph is splited into two parts: N expressed *versus* N not expressed.



#### Hierarchical Transition Graphs

The Hierarchical Transition Graphs (HTG) is an acyclic graph, which provides
a compact representation of the State Transition Graph. It improves on
the [graph of the Strongly Connected Components](index.md#strongly-connected-components-graph) by merging
linear chains of states (in addition to cycles) into single nodes.

More information on this graph is available in Berenguier _et al_[@Berenguier2013].


