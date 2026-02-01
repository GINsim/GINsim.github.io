
### Welcome dialog
Upon launch, GINsim will present the ``Welcome`` dialog box below.

![Welcome](gui/welcome2026.png)


The ``New model`` action will create a new [Regulatory Graph](index.md#logical-regulatory-graph),
while the ``Open`` and ``Import`` buttons allow to select an existing file
in a [supported format](index.md#formats-importsexports).
The ``Recent files`` section allows the quick selection of a previously opened file.
For all these actions, the selected graph will be opened in a [Main Window](index.md#main-window).


Closing this dialog or activating the ``quit`` button will stop GINsim.


!!! info

    This dialog is also shown after closing the last window (``Ctrl/Cmd-W``). Use the ``Quit`` (``Ctrl/Cmd-Q``) action to skip it.

!!! info

    When running GINsim on the command line, it is possible to provide a file to open or to ask for a new model. In this case, the welcome dialog will not be shown. See the [run options](../install/index.md).



### Common quirks

#### Input nodes
In GINsim, some nodes can be defined as input nodes using a checkbox in the node property panel. These input nodes cannot have any incoming interaction or dynamical rule as they have an implicit rule allowing them to always maintain their current activity level. Before setting a node as input, the modeller must thus remove all existing regulators or rules. Likewise, the input status must be removed before adding any new regulator or rule. To delete a logical formula, select it (without editing it) and use the delete key or the contextual menu.


#### Unexpected dynamical results
If you obtain unexpected dynamical results (stable states or simulations results), verify successively the structure of the regulatory graph, the maximal activity levels of all components, the thresholds of interactions coming out of multi-valued components and then the dynamical rules. GINsim further provides a tool to compute interaction functionality, which facilitates the identification of inconsistencies between the structure of the regulatory graph and the dynamical rules.


#### GUI refresh issues
Some refreshing problems may appear after long or complex modeling sessions, saving and restarting GINsim can solve some issues.


### Main window

#### The GINsim window
The main window allows to view a graph, edit its appearance and access to GINsim's main features. This window is divided into three parts:

- the menu and toolbar on the top;
- the graph panel, as the main central part; 
- the secondary panel on the bottom.

!!! example "The main window of GINsim"
	![The main window of GINsim](gui/mainWindow.png)

	The main window of GINsim, featuring an empty model.

#### Graph view

see the [graph page](index.md#state-transition-graphs) or merge its content here?


#### File menu

!!! example "File menu"
	![File menu](gui/fileMenu.png)

	The File menu offers all the classical options to open/save a file, to open/close a window, and to quit the application.

The File menu provides the following options:

- **New** to create a new graph. This opens a new window unless the current graph is empty.
- **Open** to load a graph from a file. This opens a new window unless the current graph is empty.
- **Recent Files** to open a recently used graph. This submenu lists the last opened graphs.
- **Merge graph** to open a graph and merge it with the current one. This option works only for regulatory graphs.
- **Close** to close the current graph. If other windows are opened, it will simply close the current one, otherwise it will leave you with an empty window.
- **Save/Save as** to save the current graph. If the file is new or if the **Save as** option has been selected, a file selection dialog appears which allows to choose the graphical attributes to save: it is possible to save only the structure of the graph, ignoring all graphical attributes, or to save only the position of nodes. The default is to save all graphical attributes (position, size, color, shape...). The graph is saved in the (XML-based) [GINML](index.md#ginsim-format).
- **Save Subgraph** to save the current selection as a new graph.
- **Export** to save the current graph in another format. GINsim can export regulatory and state transition graphs using several generic visualisation formats. These exports only retain the graph structure and visual appearance. The following export formats are available under the File/export submenu: TODO
The regulatory graph can additionally be exported into different formats.
- **Quit** to close all graphs and exit the GINsim application.

Some of these actions **New**, **Open** and **Save** are also available from the toolbar.


!!! example "The Save dialog"
	![The save dialog](gui/saving.png)

	The Java **Save** dialog allows to browse and create folders, as well as to choose their location.
	By default, only folders and GINML files are shown; other files can be seen by removing the **GINML Files** filter.
	The drop-down list on the right side allows to select the graphical attributes to save. The **ExtendedSave** checkbox allows to enable or disable extended save (which generates an archive containing the graph and related data).

!!! info
	If the **extended save** option is selected, the file is saved in an archive (zip file with a .zginml extension) instead of a XML file (with a .ginml extension). This allows to save related data, such as simulation parameters or mutant definitions, along with the model. These files need GINsim 2.3 or later to be opened.


#### Edit menu

!!! example "The Edit menu"
	![The Edit menu](gui/editMenu.png)

	The Edit menu allows the selection of some editing options. It is composed of three sections: copy/paste, graph editing tools and selection management.

##### Copy/paste

The edit menu offers classical **Copy**/**Paste** entries.

- Regulatory graph elements can be copied and pasted from one GINsim window to another.
- Pasted elements are automatically selected to ease their movement.
- The **Copy** action does not test selected interactions, it will automatically select ALL interactions between selected genes.
- The identifiers of pasted genes are postfixed to avoid naming conflicts.
- Logical parameters are also copied and cleaned up: logical parameters involving non-copied nodes are suppressed. The resulting graph is consistent but the new parameters may need to be checked.

!!! warning
	**Copy**/**Paste** actions are specific to GINsim: copying the graph and pasting it into an external application is not supported. These actions are only available for regulatory graphs.


#### Actions menu

!!! warning
	TODO: replace this all with a short note and point to the relevant index pages?

!!! example "The Actions menu"
	![The Actions menu](gui/actionMenu.png)

	The Action menu for a regulatory graph.

	
Different actions can be performed from this menu, depending on the type of graph.
Individual actions are detailed in the relevant part of this manual.
Currently available actions are:

- for all graphs:
	- [Graph layouts](index.md#graph-layouts);
	- determination of the [Strongly Connected Components (SCC)](index.md#strongly-connected-components-graph) of a graph;
- for regulatory graphs:
	- [The simulation](index.md#simulation) (i.e., computation of a state transition graph);
	- analysis of the [Circuit analysis](index.md#circuit-analysis);
	- determination of [Stable states](index.md#stable-state-search);
- for state transition graphs:
	- [path search](index.md#find-path);
	- [stg animator](index.md#the-stg-animator) graphical path construction (animation);


#### The secondary panel

The bottom panel allows to edit the items selected in the graph view. It contains two tabs:

- The first tab (called `Modelling Attributes` for regulatory graphs) will change with the type of graph.
Panels for the various graph types are described in the corresponding sections.
- The `Graphical Attributes` tab allows to edit the appareance of the selected items.
It is described in the [graph view page](index.md#graph-view).

