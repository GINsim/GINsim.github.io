---
title: "Documentation"
date: 2025-02-27T00:00:00Z
---

GINsim (Gene Interaction Network simulation) is a computer tool for the modeling and simulation of genetic regulatory networks.

Recent developments in functional genomics have generated large amounts of data on gene expression and on the underlying regulatory mechanisms. This has resulted in the progressive mapping of complex regulatory networks. As these networks usually include numerous intertwined feedback circuits, gaining an understanding of their spatio-temporal behaviour defies the intuition of the biologists. In this respect, formal modelling and simulation tools become a necessary complement to experimental tools. As precise information on molecular mechanisms and the value of kinetic parameters are currently difficult to establish, qualitative methods offer a highly attractive approach to model and analyse essential properties of genetic regulatory networks.
General information on modelling and analysis of genetic regulatory networks can be found in {{ <cite deJong2002> }}.

GINsim consists of a simulator of qualitative models of genetic regulatory networks based on a discrete, logical formalism.

GINsim allows the user to specify a model of a genetic regulatory network in term of asynchronous, multivalued logical functions, and to simulate and/or analyse its qualitative dynamical behaviour {{ <cite Chaouiya2012> }}.




### Install and Run GINsim

#### Availability and Requirements

GINsim 3.0 is freely available without guarantees.
Please contact us for training, other support or dedicated development.
The GINsim website (https://ginsim.github.io)[https://ginsim.github.io] provides the latest official version of the software, documentation, as well as a model library.

GINsim requires Java 8. 
You can obtain Java for Linux, Windows, Mac OSX, and Solaris at java.com.
Note that Apple used to provide its own Java version, newer versions are not supported on OSX 10.6 and older.
GINsim 2.9.10 is the last version supporting Java 6, and has the same features as GINsim 3.0.

Some features of GINsim rely on external tools, such as the NuSMV model checker.

#### Running GINsim
Once you have obtained GINsim, you can launch it by double-click or with the command `java -jar GINsim-#version.jar`.

The following options are available for GINsim:
    * file: open file on startup (skip the Welcome dialog).
    * -n: start with a new regulatory graph (skip the Welcome dialog).
    * -h: help message.
    * -s: run GINsim in script mode
    * -lm : Let the bioLQM library parse the command line arguments.
    * --dev : enables some experimental features still in under development.
    * -py : launch a server for the py4j python gateway (used for scripting in the Python Notebook).
    
The JAVA virtual machine provide many options, in particular GINsim can benefit from extending the amount of memory available, with the `-Xmx` option. For example, one can launch GINsim with 1000MB of memory using `java -Xmm1000M -jar GINsim-#version.jar`.


### Contact
Please send your comments, questions or suggestions to the public user group GINsim Users at ginsim-users@googlegroups.com, describing your problem and steps to reproduce it. 
As some problems are difficult to reproduce, you may be asked to provide log traces (using the GINsim/support/export log traces menu entry) and to launch GINsim from the command line to catch additional error messages.

Specific questions can also be adressed to the GINsim team at support@ginsim.org.
o


### Common quirks

#### Input nodes
In GINsim, some nodes can be defined as input nodes using a checkbox in the node property panel. These input nodes can not have any incoming interaction or dynamical rule as they have an implicit rule allowing them to always maintain their current activity level. Before setting a node as input, the modeller must thus remove all existing regulator or rule. Likewise, the input status must be removed before adding any new regulator or rule. To delete a logical formula, select it (without editing it) and use the delete key or the contextual menu.


#### Unexpected dynamical results
If you obtain unexpected dynamical results (stable states or simulations results), verify successively the structure of the regulatory graph, the maximal activity levels of all components, the thresholds of interactions coming out of multi-valued components and then the dynamical rules. GINsim further provides a tool to compute interaction functionality, which facilitates the identification of inconsistencies between the structure of the regulatory graph and the dynamical rules.


#### GUI refresh issues
Some refreshing problems may appear after long or complex modeling sessions, saving and restarting GINsim can solve some issues.


### GUI

#### Welcome dialog
Upon launch, GINsim will present the ``Welcome`` dialog box below.

{{<fig src="welcome.png" >}}{{</fig>}}

The ``New model`` action will create a new [Regulatory Graph](#regulatory-graph),       
while the ``Open`` and ``Import`` buttons allow to select an existing file      
in a [supported format](#formats).
The ``Recent files`` section allows the quick selection of a previously opened file.
For all these actions, the selected graph will be opened in a [Main Window](#main-window).


Closing this dialog or activating the ``quit`` button will stop GINsim.         


{{<notice>}}
This dialog is also shown after closing the last window (``Ctrl/Cmd-W``). Use the ``Quit`` (``Ctrl/Cmd-Q``) action to skip it.
{{</notice>}}

{{<notice>}}
When running GINsim on the command line, it is possible to provide a file to open or to
ask for a new model. In this case, the welcome dialog will not be shown. See the [run options](#install-and-run-ginsim).
{{</notice>}}


### Logical Regulatory Graph

#### Definition
Informally, a Logical Regulatory Graph (LRG) is a directed labelled multigraph 
representing interactions (the edges) between genes (the nodes).               
Each interaction involves two genes, the source and the target, becoming active
whenever its source reaches a given level.                                     
                                                                               
The activation level of each component is defined by a regulatory function     
comprising parameters relative to all regulators of this component.            
                                                                               
For a more formal definition see {{< cite Naldi2011 >}} or {{< cite Thieffry2007 >}}.


#### Structure of the LRG
Regulatory graphs can be interactively modified: components and interactions
can be added, edited and removed. The interaction with the graph view is 
controled by an editing mode selected through the following buttons available
on the toolbar on the top:


Available editing modes for regulatory graphs:

* ![Edit button](/buttons/editmode.gif) Default editing mode: allows to select and move objects.
* ![Add Node button](/buttons/insertsquare.gif)  Component insertion mode: when selected, clicking on the graph panel adds a new component.

* ![Add positive interaction button](/buttons/insertpositiveedge.gif) ![Add negative interaction button](/buttons/insertnegativeedge.gif) ![Add dual interaction button](/buttons/insertdualedge.gif) ![Add unknown interaction button](/buttons/insertunknownedge.gif)  Interaction insertion mode: when selected, interactions are added by first
  selecting one component and dragging the selection to (the same or) another
  component. The interactions must be complemented by the definition of the logical
  parameters for the target variable (see below). The four buttons allow to add
  different types of interactions: activation, inhibition, dual or undefined.
* ![Delete button](/buttons/edit-delete.png) Deletion option: selected items (components or interactions) are deleted.


{{% notice %}}
The terms **component** and **interaction** are used throughout this document,
but some other terms are sometimes used in their place.
**Regulatory components** (also called nodes) can be of different types.
They often denote **genes** but also **proteins**, or yet global cellular
characteristics such as cell mass.
Similarly, **interactions** often denote transcriptional regulations but can
also denote protein phosphorylation, degradation, complex formation, ...
{{% /notice %}}


#### Component order

In GINsim, components are internally ordered. This order has no effect on the regulatory 
graph itself, but it has a direct effect on the internal representation of the logical 
parameters, with possible effects on (partial) simulation.
The default order follows the node addition chronology, which can be modified
by selecting a (set of) node(s) and using the ``Up/Down arrows`` on the left
side of the ``Modelling Attributes`` tab.
This change of order will have an effect throughout GINsim, e.g. in the 
state transition graph, since the same order is used in the states names.

{{< fig src="node_order.png" title="Changing component order" >}}
The left part of the ``Modelling Attributes`` tab of a
regulatory graph lists all components of the model and allows to modify their
order. The "up" and "down" buttons move selected components in the list.
{{< /fig >}}


{{< notice >}}
The selection of several components, can be achieved (like in all lists)
by using the ``Ctrl`` key (``apple/Cmd`` key on Mac OS X)
or ``Shift`` key, while selecting the nodes.
{{< /notice >}}


#### Component attributes

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


{{< fig src="geneConfig.png" title="Attributes of a component" >}}
Properties of the gene Cro, as defined in the **lambda4** model.
{{< /fig >}}


{{<notice>}}
The ``Modelling Attributes`` tab is divided into three parts.
The combobox selection list (bottom left) permits to select 
:doc:`annotations`, as well as :doc:`rules` .
{{</notice>}}


#### Interactions

When a single interaction arc is selected, the ``Modelling Attributes``
tab allows to define its properties.


{{< fig src="interactionConfig.png" title="Properties of an interaction arc" >}}
Properties of the Cro-N interaction in the **lambda4** model.
{{< /fig >}}


Depending on a component's activity level, different effects might occur on another
component. These different effects are controled by the definition of different 
ranges listed on the left.

* The "+" button creates an additional interaction range.
* The "-" button deletes the selected interaction range.
* Properties of the selected interaction range can be defined:

  * **Threshold** defines the lower bound of the selected interaction range.
    The interaction becomes **active** when
    the activity level of its source component is in this range.
  * **Sign**: each interaction range can be labelled with activation,
    inhibition, dual or unknown.
    However, this is only a visual hint, as the real effects of interactions are defined
    through :doc:`rules`.


#### Model integrity

GINsim keeps the definition of regulatory graphs consistent, which means that:

* When an interaction is deleted, all :doc:`rules` in which it was involved
  are also deleted.
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



### Dynamica rules

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

{{<fig src="configuredInteraction.png" title="Definition of non zero parameters for CI">}}
The logical parameter panel, showing all parameters for component CI.
{{</fig>}}

To **add** a new logical parameter, select the empty line in the list of parameters (the last line),
select a combination of active interactions on the right part, and click on the ``left arrow``.
The new logical parameter will be defined with the default value of 1, this value can be edited though.
The specification of logical parameters with target values set to 0 is not needed, since all non-specified logical parameters are implicitly considered to be 0.
Adding a parameter with a set of active interactions that is already defined is not permitted.


The ``Up/Down arrows`` enable the reordering the existing parameters.

To **remove** parameters from the list of active interactions, select them and click on the ``-`` button.

To **modify** the active interactions for an exiting parameter, select the corresponding line, then select the correct set of active interactions in the right part, and finally click on the ``left arrow`` button to apply the changes.

{{<notice warning>}}
It is not possible to select the ``Input`` checkbox
whenever a component has incoming interactions.

Similarly, if the ``Input`` checkbox is selected,
logical parameters can not be defined and the component
is considered to have an implicit self-activation.
{{</notice>}}



#### Logical functions


The dynamical behaviour of a given compoenent can also be specified through the use of logical functions. These function are, for certain cases, a more convenient manner to define complex behaviours with many regulators.
The definition of a logical function will generate the corresponding logical parameters automatically.

{{<notice warning>}}
  The automatically generated logical parameters may overlap with previously generated ones, automatically or manually.
{{</notice>}}


{{<fig src="logical-functions.png" title="Definition of a logical function for CI">}}
The logical function panel, showing the definition of one logical function at target 1.
{{</fig>}}


To define a new logical function, select the ``Down arrow``, specify a target value for the function, and select subsequent ``Down arrow``.
You can then press the ``E`` button to start editing the logical function (line color changes to green).
The after insertion of the logical function press ``Enter`` to validate the expression and automatically create the corresponding logical parameters.

The parser for logical functions accepts the logical AND and OR with the symbols ``&`` and ``|``, respectively. Additionally, you can add parentheses to prioritize logical operations.


