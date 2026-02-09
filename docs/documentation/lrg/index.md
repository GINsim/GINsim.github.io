
### Definition
Informally, a Logical Regulatory Graph (LRG) is a directed labelled multigraph
representing interactions (the edges) between genes (the nodes).
Each interaction involves two genes, the source and the target, becoming active
whenever its source reaches a given level.

The activation level of each component is defined by a regulatory function
comprising parameters relative to all regulators of this component.

For a more formal definition see [@Naldi2011] or [@Thieffry2007].


### Structure of the LRG
Regulatory graphs can be interactively modified: components and interactions
can be added, edited and removed. The interaction with the graph view is 
controlled by an editing mode selected through the following buttons available
on the toolbar on the top:


Available editing modes for regulatory graphs:

* ![Edit button](/documentation/lrg/editmode.gif) Default editing mode: allows to select and move objects.
* ![Add Node button](/documentation/lrg/insertsquare.gif)  Component insertion mode: when selected, clicking on the graph panel adds a new component.

* ![Add positive interaction button](/documentation/lrg/insertpositiveedge.gif) ![Add negative interaction button](/documentation/lrg/insertnegativeedge.gif) ![Add dual interaction button](/documentation/lrg/insertdualedge.gif) ![Add unknown interaction button](/documentation/lrg/insertunknownedge.gif)  Interaction insertion mode: when selected, interactions are added by first
  selecting one component and dragging the selection to (the same or) another
  component. The interactions must be complemented by the definition of the logical
  parameters for the target variable (see below). The four buttons allow to add
  different types of interactions: activation, inhibition, dual or undefined.
* ![Delete button](/documentation/lrg/edit-delete.png) Deletion option: selected items (components or interactions) are deleted.


!!! info
    The terms **component** and **interaction** are used throughout this document, but some other terms are sometimes used in their place.
    **Regulatory components** (also called nodes) can be of different types.
    They often denote **genes** but also **proteins**, or yet global cellular characteristics such as cell mass.
    Similarly, **interactions** often denote transcriptional regulations but can also denote protein phosphorylation, degradation, complex formation, ...


### Component order

In GINsim, components are internally ordered. This order has no effect on the regulatory 
graph itself, but it has a direct effect on the internal representation of the logical 
parameters, with possible effects on (partial) simulation.
The default order follows the node addition chronology, which can be modified
by selecting a (set of) node(s) and using the ``Up/Down arrows`` on the left
side of the ``Modelling Attributes`` tab.
This change of order will have an effect throughout GINsim, e.g. in the 
state transition graph, since the same order is used in the states names.

!!! example "Changing component order"
    ![Changing component order](/documentation/lrg/node_order2026.png)

    The left part of the ``Modelling Attributes`` tab of a regulatory graph lists all components of the model and allows to modify their order. The "up" and "down" buttons move selected components in the list.


!!! info
    The selection of several components, can be achieved (like in all lists) by using the ``Ctrl`` key (``apple/Cmd`` key on Mac OS X) or ``Shift`` key, while selecting the nodes.


### Component attributes

When a single component is selected, the ``Modelling Attributes``
tab allows to define its properties:

* ``Id``: component's identifier. It appears in the graph	and it must be unique.
* ``Name``: component's long name (optional).
* ``Input``: mark a component as an input node, i.e., cannot have regulators.
* ``Max``: the maximal expression level of the component.
  The default value is 1 (Boolean case).
  It can be augmented to generate multi-valued components.
* ``Logical parameters``: define the rules controlling the dynamical evolution
  of the expression level depending on the active incoming interactions.


!!! example "Attributes of a component"
    ![Attributes of a component](/documentation/lrg/geneConfig2026.png)
    
    Properties of the gene Cro, as defined in the **lambda4** model.


!!! info
    The ``Modelling Attributes`` tab is divided into three parts.
    The combobox selection list (bottom left) permits to select :doc:`annotations`, as well as [Dynamical rules](#dynamical-rules).


## Interactions

When a single interaction arc is selected, the ``Modelling Attributes`` tab allows to define its properties.


!!! example "Properties of an interaction arc"
    ![Properties of an interaction arc](/documentation/lrg/interactionConfig2026.png)

    Properties of the Cro-N interaction in the **lambda4** model.


Depending on a component's activity level, different effects might occur on another
component. These different effects are controlled by the definition of different 
ranges listed on the left.

* The "+" button creates an additional interaction range.
* The "-" button deletes the selected interaction range.
* Properties of the selected interaction range can be defined:
* **Threshold** defines the lower bound of the selected interaction range.
The interaction becomes **active** when the activity level of its source component is in this range.
* **Sign**: each interaction range can be labelled with activation, inhibition, dual or unknown.
However, this is only a visual hint, as the real effects of interactions are defined through [Dynamical rules](#dynamical-rules).


### Model integrity

GINsim keeps the definition of regulatory graphs consistent, which means that:

* When an interaction is deleted, all [Dynamical rules](#dynamical-rules) in which it was involved are also deleted.
* When the ``max value`` of a node is decreased, interactions and logical
  parameters are checked and, if necessary, updated accordingly and silently
  to avoid inconsistencies.


Since such changes have automatic repercussions on the model parameters
and interaction ranges to keep the model valid, keep in mind that you
need to double-check parameters after performing such changes.

Checking activation intervals of interactions and the correctness
of logical parameters is left to the user as adding more controls generates more
annoyances than real help. Invalid logical parameters are highlighted to ease their
detection. Keep in mind that a change in the activation-range of one of the
interactions can turn a valid logical parameter into an ill-defined one. Parameters
involving interactions from the same source with disjoint activity ranges 
are also ill-defined and thus highlighted for correction.



-------------------------------------------
### Dynamical rules

The dynamical behaviour of regulatory components depends on their regulators,
but the precise rules governing them must be explicitly defined.
In GINsim, these rules can be defined either as **logical parameters**, or
as **logical functions**. These two alternatives are described below.


#### Logical parameters

A logical parameter corresponds to a single entry (line) in the truthtable of a component.
It is defined by a target activity level and a list of active interactions.
By default, interactions not present on the list are implicitly considered to be inactive.
This means that in order to a given parameter to be effective,
all interactions present on the list must be active, and all interactions not
present on the list must be inactive.

When a component is selected, **logical parameters** for this component can be
defined in the right part of the ``Modelling Attribute`` tab. The panel dedicated
to the definition of logical parameters is divided into three parts:

* On the left, a table lists all defined logical parameters,
  showing their values and related interactions.
* A central part containing buttons to edit the list of parameters.
* On the right, a list of all incoming interactions of the selected component.


!!! example "Definition of non zero parameters for CI"
    ![Definition of non zero parameters for CI](/documentation/lrg/configuredInteraction2026.png)

    The logical parameter panel, showing all parameters for component CI.

To **add** a new logical parameter, select the empty line in the list of parameters (the last line),
select a combination of active interactions on the right part, and click on the ``left arrow``.
The new logical parameter will be defined with the default value of 1, this value can be edited though.
The specification of logical parameters with target values set to 0 is not needed, since all non-specified logical parameters are implicitly considered to be 0.
Adding a parameter with a set of active interactions that is already defined is not permitted.


The ``Up/Down arrows`` enable the reordering the existing parameters.

To **remove** parameters from the list of active interactions, select them and click on the ``-`` button.

To **modify** the active interactions for an exiting parameter, select the corresponding line, then select the correct set of active interactions in the right part, and finally click on the ``left arrow`` button to apply the changes.

!!! info
    It is not possible to select the ``Input`` checkbox whenever a component has incoming interactions.
    
    Similarly, if the ``Input`` checkbox is selected, logical parameters cannot be defined and the component is considered to have an implicit self-activation.



#### Logical functions


The dynamical behaviour of a given component can also be specified through the use of logical functions. These function are, for certain cases, a more convenient manner to define complex behaviours with many regulators.
The definition of a logical function will generate the corresponding logical parameters automatically.

!!! info
    The automatically generated logical parameters may overlap with previously generated ones, automatically or manually.


!!! example "Definition of a logical function for CI"
    ![Definition of a logical function for CI](/documentation/lrg/logical-functions2026.png)

    The logical function panel, showing the definition of one logical function at target 1.


To define a new logical function, select the ``Down arrow``, specify a target value for the function, and select subsequent ``Down arrow``.
You can then press the ``E`` button to start editing the logical function (line color changes to green).
After insertion of the logical function press ``Enter`` to validate the expression and automatically create the corresponding logical parameters.

The parser for logical functions accepts the logical AND and OR with the symbols ``&`` and ``|``, respectively. Additionally, you can add parentheses to prioritize logical operations.


#### Annotations

Annotations can be attached to the different components of the regulatory graph:

* the graph itself,
* components,
* interactions.

An annotation is composed of a textual comment and a numbered list of URIs,
which can be opened using the ``[i]`` buttons on the left side.

!!! example "The annotation panel"
    ![The annotation panel](/documentation/lrg/annotation2026.png)
    
    The same **Annotation panel** is used for all elements
supporting notes. This screenshot shows the graph annotations,
available when the selection is empty.



Some shortcuts are provided for linking to entries in online databases.
For example, ``pubmed:19426782`` will open http://www.ncbi.nlm.nih.gov/pubmed/19426782.
This relies on the [identifiers.org webservice](http://identifiers.org).


-------------------------------------------
### LRG modifications

#### Perturbations

GINsim facilitates the definition of **perturbations** to define small changes to
the regulation of components in regulatory graphs. A perturbation is a set of
restrictions on the evolution of the activity level of one or several components.


##### Using Perturbations

Some tools, notably Simulation and Stable state search, include a
perturbation selection panel to apply a perturbation before running.


##### Definition of Perturbations

Perturbation can be defined using the following configuration panel.
The panel appears upon activation of the ``configure`` button in the
perturbation selection panel.


!!! example "Perturbation definition panel"
    ![Perturbation definition panel](/documentation/lrg/perturbations2026.png)

    This edition panel considers two types of perturbations: **simple perturbations** which only affect the activity of a single component, and **multiple perturbations** which group together a list of simple perturbations.


##### Simple Perturbations

The perturbation definition panel appears on the top-right part of the dialog above
when no simple perturbation is selected, or when clicking the ``+`` button.
To create a perturbation, one must first select the affected component using the combobox.
The restriction configuration panel will then appear, and the perturbation can be added using the ``create`` button.

The activity level of Boolean components can be fixed at ``0`` or at ``1``,
corresponding to the definition of a knockdown or ectopic activity respectively.
Radio buttons allows to choose between these two possibilities.

Multi-valued components offer more possibilities, that can be configured using
a range slider. Their activity level will be restricted in the selected range,
or completely fixed if the range corresponds to a single value.


!!! example "Perturbation creation panels"
    ![Perturbation creation panels](/documentation/lrg/booleanperturbation2026.png)

    TODO: add multivalued figure figures/mvaluedperturbation.png


This enables the definition of simple perturbations where the activity level of a component is restricted to the selected value(s).

!!! info
    The definition of more subtle perturbations (conditional knockouts...) still requires the modifications of the logical parameters. We plan to add convenient means to define other types of perturbations in the future.

!!! info
    Simple perturbations cannot be duplicated: when trying to add a simple perturbation that is already defined, nothing will happen.



##### Multiple Perturbations

The bottom part of the panel lists multiple perturbations.
Multiple perturbations can be created by selecting several
simple perturbation and clicking the button which appears
in the information panel.
These perturbations can then be ordered and deleted using 
the buttons on the right side.


!!! warning
    Deleting a simple perturbation will also remove all the multiple perturbations using it.


#### Booleanization


GINsim enables the definition of multi-valued models where some components can
have several increasing activity levels. However, some other analysis tools only
consider Boolean (on/off) models.
Model booleanization allows to convert multi-valued models into Boolean models
by mapping each multivalued component on a group of Boolean variables. The
resulting Boolean model generates the same dynamical behaviour as the original
multivalued model.

bioLQM uses the mapping originally proposed by van Ham, in which a component
associated with the maximal value ``m`` will be mapped on ``m`` Boolean components.
For example, a component taking the values ``0`, ``1``, ``2``, and ``3`` will be
encoded as ``000``, ``100``, ``110``, and ``111``.

The booleanization introduces many non-admissible states, which may require special
care depending on the analysis applied on the booleanized model. This modifier makes
sure that a simulation which start with an admissible state will not explore 
non-admissible states. It also prevents the introduction of non-admissible attractors
by making sure that at least one admissible state is reachable from any non-admissible.


##### Usage

Exporting a multivalued model to a format limited to Boolean components triggers an implicit Booleanization step.
This booleanization step can also be performed explicitely using the booleanization tool in the ``Actions`` menu.

##### Availability and further reading

This method was implemented in GINsim 3.0.
The backend is implemented in the 
[bioLQM toolkit](http://colomoto.org/biolqm),
enabling its programmatic use.


#### Model reversal

The model reversal tool constructs a model in which the asynchronous successors of a state
correspond to its predecessors in the original model.

Multivalued models are supported through model booleanization,
with some further transformations to prevent the introduction
of non-admissible successor states.


##### Usage

The model reversal tool is available in the ``Actions`` menu.


##### Availability and further reading

This method was implemented in GINsim 3.0.
The backend is implemented in `BioLQM <http://colomoto.org/biolqm>`_,
enabling its programmatic use.


#### Model reduction


The reduction of regulatory graphs allows to extract a "simplified"
regulatory graph where a set of components are hidden. To keep a
consistent dynamical behaviour, the logical rules associated with the
targets of each hidden component account for the (indirect) effects
of its regulators. This construction of reduced models preserves
crucial dynamical properties of the original model, including stable
states and more complex attractors. Furthermore, the relationship
between the attractor configuration of the original model and those
of reduced models is formally established.

##### Usage

The reduction tool is available in the ``Actions`` menu. It open a
configuration dialog in which the user can select the components
that will be hidden. Several configuration strategies can be defined.
Running the tool leads to the construction of a reduced model where
the selected components have been removed.


Some reductions are not possible (an auto-regulated component cannot
be hidden using this method), if a reduction fails, GINsim will show
an error message, listing the components that could not be hidden and
proposing to continue with the result of the partial reduction.


Note that in some cases, the reduction may only be possible in a precise
order (but the result does not change with the order). When blocked,
GINsim will try alternate orders for the remaining components, but not 
for the components which have already been succesfully reduced. In such
cases, it may be necessary to provide the list of components to reduce in
several steps to force the use of the correct order.


##### Output stripping

Outputs are components which do not regulate others. As such, these
components have no impact on the attractors that will be reached in
a simulation. These output components can be automatically removed
when performing a simulation or some other actions on a model.
To instruct GINsim to remove outputs, use the ``strip outputs`` 
checkbox next to the perturbation selection box.


##### Script mode


The reduction tool can also be used in script mode. It then relies on a previously defined reduction strategy.


##### Availability and further reading

This method was implemented in GINsim 2.4 (see [@Naldi2011]).
The support for output stripping was added in GINsim 3.0 (see [@Naldi2012]).


