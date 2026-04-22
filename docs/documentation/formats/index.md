
### GINsim format

The Z-GINML format (also denoted **extended save**), is a zip archive containing a ginml file along with companion files to store associated data,
especially initial states, perturbations, and simulation parameters. More generally,
each plugin can provide a parser and file writer to store its associated data in a Z-GINML file.

The **GINML** format is an extension of the [GXL (Graph eXchange Language)](http://www.gupro.de/GXL) format.
This extension comprises new attributes and sub-elements for elements `node` and `edge`, and an additional element called `parameter`.

- Element `node`:
	- attribute `id`: node identifier (name of the component);
	- attribute `basevalue`: "base level of expression" of the corresponding component (default value `0`); 
	In other words, it is the value of the logical parameter corresponding to the case where none of the incoming interactions is functional;
	- attribute `maxvalue`: "maximum level of expression" of the corresponding component (default value `1`);
	- attribute `input`: is this node an input of the system? (default value `false`).

Sub-elements within a node:
	- a list of elements `parameter` corresponding to the user defined logical parameters for this node.
  
- Element `edge`:
	- attribute `id`: edge identifier (usual format "source_node_id:target_node_id");
	- attributes `from` and `to`: source and target nodes of this edge;
	- attribute `sign`: gives the sign of the interaction (positive for an activation, negative for a repression, otherwise unknown);
	- one or two sub-elements `int` (level or interval letting the interaction functional) 
	
Element `parameter`:
	- attribute `idActiveInteractions`: list of the `edge` IDs which are the functional interactions exerted upon the considered node.
	- attribute `val`: value of the logical parameter.

See the GINML's dtd or in pdf format. More information on [CoLoMoto web site](https://colomoto.github.io/formats/ginml/).

See also the GINML description of the gap-gene network case A, or in PDF format.

(TODO: described stored associated data)

Some companion data can be associated to the graphs to store the configuration of various tools.
Some of this extra data can be shared between several tools.
This extra data is stored in its own entry inside ZGINML files.



### Export graph view

The graph view can be exported as an image in the PNG format.
This export considers only the visual appearance of the graph,
and can thus be applied to all types of graph in GINsim.

The view can also be exported in the
[Scalable Vector Graphic (SVG)](http://www.w3.org/Graphics/SVG/) format.
Tools like [Inkscape](http://inkscape.org), can then be used to display,
modify and export SVG files to virtually any image format.


### Export graph structure

The following exports consider only the graph structure, and
can thus be applied to all types of graph in GINsim.

The graph structure can be exported for use in dedicated graph visualization software,
which can handle some graphs considered as too large for viewing in GINsim directly.
These exports only consider the graph structure (graphical attributes are lost).
The following formats are supported:

#### Graphviz

Files in the [DOT language](http://www.graphviz.org/content/dot-language)
can be opened using the graph visualization software
[Graphviz](http://www.graphviz.org).


#### BioLayout

[Biolayout](http://www.biolayout.org), is a graph visualization software focussing
on biological networks.

#### Cytoscape

[Cytoscape](http://www.cytoscape.org),
is also used for the analysis of biological networks. While GINsim can export
regulatory graphs for cytoscape, this format is not yet available for other types of graphs.


#### NuSMV export

The dynamics of logical regulatory graphs can be described using a NuSMV specification.
In GINsim, this specification is created through an export functionality capable of
generating a symbolic description of the logical model specified in GINsim.

Additionally, it is capable of describing different updating policies for the
generation of the successors, such as synchronous, asynchronous and priority classes.

Finally, it tries to address the space problem of the state representation by
annotating the information regarding the input variables on edges instead of states
(making use of ARCTL),
and by (optionally) defining output variables as simple macro functions.


###### Symbolic representation

Each variable is declared under the <code>VAR</code> section together with
the corresponding range of values (domain). The order of the declaration of
variables is of extreme importance since it influences the construction of the
internal BDD representing the whole dynamics.

The initialization of a set of variables is performed by using the
<code>INIT</code> keyword followed by an assignment of a value to a given variable.
Alternatively, a macro can be defined with a conjunction of variable valuations
and simply use the macro name with the <code>INIT</code> keyword.

The rules concerning the computation of the target value of a given variable
are described under the <code>ASSIGN</code> section, using the
<code>next(Var) := ...;</code> form.

The computation of the focal point is declared under the <code>DEFINE</code>
section, where the actual logical rules referencing all the regulatory
components are declared.

In this section it is also declared all the macros to be used in the property
specifications, such as weak and strong stable states, the list of initial
conditions defined by the user, or the output variables which (if specified)
do not participate in the state characterization.


##### Updating policies
In this export, all of the possible updating policies synchronous/asynchronous are considered as being special cases of the priority classes:

* Asynchronous updating is represented as having one
    priority class per variable ([VarA] [VarB] ... [VarZ]), with
    the restriction of a single class update per successor.
* Synchronous updating is represented as having one
    single priority class containing all of the variables
    ([VarA VarB ... VarZ]), where all of the variables in the
    class are called to change their value in the (single)
    successor.



##### State representation

There are three main types of variables characterizing a state:
state variables, which are declared under the <code>VAR</code> section;
output variables, which (if specified by the "Strip outputs" option) are declared
as macros under the <code>DEFINE</code> section;
and the input variables, which are declared under the <code>IVAR</code> section.

State variables are the ones characterizing an internal state in NuSMV, so,
whenever one of the state variables is called to change, a new successor is
(might be) created.
Output variables are the ones that are not critical for the state characterization,
and whose values can be computed through state variables alone.
Output variables can still be referenced with a temporal operator in a property
specification though.
Input variables are always projected over transitions rather then the state.
Between a state and its successor, a transition contains all the valid input
valuations, i.e., if a given input valuation does not permit to follow a given
transition is will be not represented over that transition.


###### Macros representing state restrictions

The NuSMV export will always automatically compute the model stable states and
insert them in the NuSMV model description.
Every <em>stableState</em> is either a <em>weakSS</em> or a <em>strongSS</em>,
and each one of these can be composed by several ones, depending on the model.
The user, can then use each of these macro names for the specification of
properties, from a general one <em>stableState</em> to a more specific one
<em>strongSS</em>.

Additionally, when exporting a model, the user can define and select state
restrictions on the internal components or on the input components.
Only the ones that are checked will be written on the NuSMV specification.
Similarly, the names given to each of these state restrictions will correspond to
macro names which can be used in the specification of properties.


###### Temporal logic property specification

This NuSMV specification of the logical model, does not include any
property specifications.
It is <em>up to the user</em> to encode them at the end of the NuSMV specification file.
Again, in any given property, the user can always use the <em>stableState</em>
or the <em>initialStateList</em> macros previously defined.
In order to aid the user in such task, the following example reachability
properties are added, as comments, at the end of each file.


```
--------------------------------------------------
-- Reachability Properties using VARYING INPUTS --
-- i.e. there is NO CONTROL on the input change at each transition
--
-- 1. Between an initial state (pattern) and a stable state (pattern)
--   a. Existence of at least one path connecting two state patterns
-- INIT initState;
-- SPEC EF ( stableState );
--   b. Existence of all the paths connecting two state patterns
-- INIT initState;
-- SPEC AF ( stableState );
--
-- 2. Between all the weak/strong stable states
-- INIT weakSS1;
--  SPEC EF ( weakSS2 );
--  ...
--  SPEC EF ( weakSSn );
--------------------------------------------------
-- Reachability Properties using FIXED INPUTS --
-- i.e. a VALUE RESTRICTION can be forced at each transition
--
-- 1. Between an initial state (pattern) and a stable state (pattern)
--   a. Existence of at least one path connecting two state patterns
-- INIT initState; SPEC EAF ( inpVar1=0 &amp; inpVar3=1 )( stableState );
--   b. Existence of all the paths
-- INIT initState; SPEC AAF ( inpVar1=0 &amp; inpVar3=1 )( stableState );
--
-- 2. Testing input combinations
-- INIT weakSS1;
--  SPEC EAF ( inpVar1=0 &amp; inpVar2=0 )( weakSS2 );
--  SPEC EAF ( inpVar1=0 &amp; inpVar2=1 )( weakSS2 );
--  SPEC EAF ( inpVar1=1 &amp; inpVar2=0 )( weakSS2 );
--  SPEC EAF ( inpVar1=1 &amp; inpVar2=1 )( weakSS2 );
--  ...
```


##### Availability and further reading

This export was implemented in GINsim 3.0. Further information is available in [@Monteiro2012].


#### Petri net export
Regulatory graphs can be exported into discrete <!-- TODO: check nomenclature with claudine -->
Petri net using the rewriting method described in [@Chaouiya2006].

In the "File -> Export" menu, a "Petri Net" submenu allows to choose one of three supported Petri net representations: INA, PNML and APNN.
Choosing any of these representations, opens a configuration dialog box which presents a list of options to be considered in the export.
These include modifications such as model perturbations or reductions, or the definition of a set of initial states.


!!! example "The Petri Net export dialog"
    ![The Petri Net export dialog](/documentation/formats/pnexport.png)

    The Petri Net export dialog box allows to select the export format, the initial markup and the mutant to apply before exporting. The initial markup can be generated from an existing initial state of the model  (modifications made in this dialog are also applied to the simulation settings); only the first selected state is used.

TODO: update figure!


