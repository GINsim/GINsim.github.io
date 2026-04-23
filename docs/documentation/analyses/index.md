
### Strongly Connected Components graph

A [Strongly Connected Component (SCC)](http://en.wikipedia.org/wiki/Strongly_connected_component)
in a graph is a maximal subgraph such that all its components are strongly
connected. Each SCC can be either a single node or a set of intertwined cycles
of the original graph.
The SCC graph is a derived graph in which each node represents one of the SCC
of the original graph.	This acyclic graph provides a simplified representation
of the organisation of the original graph. This graph is thus often much more compact.

In GINsim, the graph of the Strongly Connected Components (SCC graph) is often
used to provide a better understanding of the organisation of the attractors in
a [State Transition Graph](#state-transition-graphs).

#### Construct an SCC graph
The computation of the SCC graph can be launched through the ``Construct SCC graph``
option of the ``Tools`` menu.
Note that GINsim also provides the [Hierarchical Transition Graph](#hierarchical-transition-graphs) dedicated to this problem.


!!! example "Strongly Connected Components graph"
    ![Strongly Connected Components graph](/documentation/analyses/scc.png)

    Example of Strongly Connected Component Graph (bottom right) and the corresponding state transition graph (top left).
    The ``Selection Attribute`` tab in the bottom panel shows the content of the selected SCC (i.e. the list of nodes in the original graph).


Note that while the ``Construct SCC graph`` tool is often applied to [State Transition Graph](#state-transition-graphs), it can
also be applied to Regulatory Graphs (or more formally to any type of graphs).


#### Extract from SCC graph

After computing the SCC graph, another tool allows to recover the subgraph
of the original graph corresponding to the selected nodes in the SCC graph.

To use it, select some nodes in a SCC graph and run the ``Extract subgraph``
action from the ``Graph`` menu.

This tool will open the original graph, and apply a filter to only keep the
selected parts. To work properly it thus requires that the original graph
had been saved to a file, and that the association between the SCC graph
and the original graph (maintained by GINsim transparently) is still valid.

### Attractors reachability

!!! example "Attractors reachability"
    ![](/documentation/analyses/attractorsReachability2026.png)

    The attractors'reachbility dialog box, showing the configuration of the analysis.


### Stable state search

This tool allows the analytic (i.e. without running a simulation) determination
of stable states of the model. All stable states are determined, regardless of
their reachability[@Naldi2007].

This tool allows the analytic (i.e. without running a simulation) determination of
trapspaces of the model. These trapspaces contain the stable states, as well as an
approximation for complex attractors.


#### Usage

The stable state identification tool is available from the ``Compute stable states`` option of the ``Tools`` menu.
The stable states dialog box allows to run the analysis after the optional
selection of a perturbation. The result is shown in a table in the same dialog box, allowing to launch a novel analysis for another perturbation.
A "\*" in the table denotes that each of the values of this component gives rise to a stable state (or several if another "\*" appears in the same row).


!!! example "Stable states search"
    ![](/documentation/analyses/fixedPoints2026.png)

    The stable states dialog box, showing the result of the analysis.


#### Availability

Stable state search was first implemented in GINsim 2.3.
The implementation is now part of the
[bioLQM toolkit](https://colomoto.org/biolqm).


### Trapspace search


This tool allows the analytic (i.e. without running a simulation) determination of
trapspaces of the model. These trapspaces contain the stable states, as well as an
approximation for complex attractors **cite Klarner2014**.


#### Usage

This tool is available from the ``Trapspace identification`` option of the ``Tools`` menu.


!!! example "The trapspace dialog box"
    ![](/documentation/analyses/trapspaces.png)

    The trapspace dialog box, showing the result of the analysis.


#### Availability

Trapspace identification was first implemented in GINsim 3.0, relying on
the [bioLQM toolkit](http://www.colomoto.org/biolqm).


### Circuit analysis

Regulatory circuits play crucial roles in the dynamical behaviour of a system.
Indeed, positive circuits are required for the existence of several attractors,
whereas negative circuits may generate cyclic attractors[@Thieffry2007].


Many regulatory graphs currently under study contain a large number of circuits,
but a relatively small number of them often plays a more important role.
In [@Naldi2007], we describe a method to compute a **functionality context**
for all circuits, to determine which circuits are more likely to affect the
attractor configuration of the system.


Note that the functionality contexts identified here give the conditions on the
immediate regulators of the circuits under which it is fully effective. These
conditions may be impossible to maintain according to the dynamical rules of
the model, especially in the case of model perturbations.


#### Usage

The ``Circuits Functionality`` entry of the ``Action`` menu opens the circuit
analysis dialog. This dialog provides an interface to lookup all circuits in the
regulatory graph or a subset of circuits matching some filtering rules (length,
involved components).


!!! example "Select regulatory circuits for analysis"
    ![Select regulatory circuits for analysis](/documentation/analyses/circuitsConfig.png)

    A first dialog allows to select which circuits will be analysed, by specifying constraints on the length of the circuits or on the involved actors. By default all circuits are considered.


The dialog then allows to analyse the selected circuits, it will then show the circuit for which a **functionality context** was found.
The analysis can be repeated for various perturbations.


!!! example "Result of the functionality analysis"
    ![Result of the functionality analysis](/documentation/analyses/circuits.png)

    When the analysis is completed, the dialog classifies the selected circuits, according to their computed sign.
    When a circuit is selected, its functionality context is shown at the bottom of the dialog box.



#### Availability

Circuit analysis was implemented in GINsim 2.3.


