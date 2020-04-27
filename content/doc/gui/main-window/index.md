---
title: "The main window"
date: 2019/07/24 12:58
summary: View and edit graphs, launch actions
---


<section id="mainWindow">
<title>The GINsim window</title>
<p>The main window allows to view a graph, edit its appareance and access to GINsim's main features. This window is divided into three parts:</p>
<list>
	<item><p>the menu and toolbar on the top;</p></item>
	<item><p>the graph panel, as the main central part;</p></item>
	<item><p>the secondary panel on the bottom.</p></item>
</list>

<figure>
	<title>The main window of GINsim</title>
	<desc>The main window of GINsim, featuring an empty model.</desc>
	<media type="image" src="figures/mainWindow.png"/>
</figure>

</section>

<section id="view">
<title>Graph view</title>

<p>see the <link xref="gui-graph">graph page</link> or merge its content here?</p>
</section>

<section id="fileMenu">
<title>File menu</title>
<figure>
	<title>File menu</title>
	<desc>The File menu offers all the classical options to open/save a file, to
		open/close a window, and to quit the application.</desc>
	<media type="image" src="figures/fileMenu.png"/>
</figure>

<p> The File menu provides the following options:</p>
<terms>
	<item><title>New</title><p>to create a new graph. This opens a new window unless the
			current graph is empty.</p></item>
	<item><title>Open</title><p>to load a graph from a file. This opens a new window
			unless the current graph is empty.</p></item>
	<item><title>Recent Files</title><p>to open a recently used graph. This submenu lists the
			last opened graphs.</p></item>
	<item><title>Merge graph</title><p>to open a graph and merge it with the current one.
			This option works only for regulatory graphs.</p></item>
	<item><title>Close</title><p>to close the current graph. If other windows are opened, it
			will simply close the current one, otherwise it will last with an empty
			window.</p></item>
	<item><title>Save</title><title>Save as</title>
		<p>to save the current graph. If the file is new orif the <em>Save as</em> option has
		been selected, a file selection dialog appears which allows to choose the graphical
		attributes to save: it is possible to save only the structure of
		the graph, ignoring all graphical attributes, or to save only the
		position of nodes. The default is to save all graphical attributes
		(position, size, color, shape...). The graph is saved in the (XML-based)
		<link href="http://gin.univ-mrs.fr/GINsim/ginml.html"><em>GINML</em></link> format.
			<!--
			<list>
			<item>extended save: if this option is selected, the resulting file will be a zip file containing the model itself along with additionnal data (simulation parameters, definition of mutants...) that is associated to it. If the option is not selected, the file will be a text file containing only the model.</item>
		</list>
			-->
		</p></item>
		<item><title>Save Subgraph</title><p>save the current selection as a new graph.</p></item>
		<item><title>Export</title><p>save the current graph in another format. GINsim
			can export regulatory and state transition graphs using several generic visualisation formats.
			These exports only retain the graph structure and
			visual appearance. The following export formats are available under the
			File/export submenu: </p>
			
			<p>The regulatory graph can additionally be exported into different formats.</p>
		</item>
		<item><title>Quit</title><p>close all graphs and exit the GINsim application.</p></item>
	</terms>

	<p>Some of these actions (<em>New</em>, <em>Open</em> and <em>Save</em>) are also available from
	the toolbar. </p>

<figure>
	<title>The save dialog</title>
	<desc>
		The Java <em>Save</em> dialog allows to browse and create folders, as well as to choose their location.
		By default, only folders and GINML files are shown; other files can be seen by removing the <em>GINML Files</em> filter.
		The drop-down list on the right side allows to select the graphical attributes to save. The	<em>ExtendedSave</em> checkbox
		allows to enable or disable extended save (which generates an archive containing the graph and related data).
	</desc>
	<media type="image" src="figures/saving.png"/>
</figure>

<note style="tip">
	<p>If the <em>Extended Save</em> option is selected, the file is
		saved in an archive (zip file with a .zginml extension) instead of a xml file
		(with a .ginml extension). This allows to save related data, such as simulation
		parameters or mutant definitions, along with the model. These files need GINsim
		2.3 or later  to be opened.</p>
</note>
<!--
	<p>In addition to these generic export format, regulatory graphs can be exported into <link href="http://www.sbml.org/">SBML</link>. <note style="warning">MORE EXPLANATIONS ARE NEEDED</note></p>
	-->
</section>


<section id="editMenu">
<title>Edit menu</title>

<figure>
	<title>The Edit menu</title>
	<desc>The Edit menu allows the selection of some editing options. It is
		composed of three sections: copy/paste, graph editing tools and selection
		management.</desc>
	<media type="image" src="figures/editMenu.png"/>
</figure>

<section id="copyPaste">
	<title>Copy/paste</title>
	<p>The edit menu offers classical <em>Copy</em> / <em>Paste</em> entries.</p>
	<note>
		<p><em>Copy</em> and <em>Paste</em> actions are
			specific to GINsim: copying the graph and pasting it into an external
			application is not supported. These actions are only available for
			regulatory graphs.</p>
	</note>
	<list>
		<item>
			<p>Regulatory graph elements can be copied and pasted from one GINsim window to
				another.</p>
		</item>
		<item>
			<p>Pasted elements are automatically selected to ease their move.</p>
		</item>
		<item>
			<p>The <em>Copy</em> action does not test selected
				interactions, it will automatically select ALL interactions between
				selected genes.</p>
		</item>
		<item>
			<p>The identifiers of pasted genes are postfixed to avoid naming conflicts</p>
		</item>
		<item>
			<p>Logical parameters are also copied and cleaned up: logical
				parameters involving not-copied nodes are suppressed. The resulting graph
				is consistent but the new parameters may need to be checked.</p>
		</item>
	</list>
</section>
</section>


<section id="actionMenu">
<title>Actions menu</title>

<note><p>TODO: replace this all with a short note and point to the relevant index pages?</p></note>

<figure>
	<title>The Actions menu</title>
	<desc>The Action menu for a regulatory graph.</desc>
	<media type="image" src="figures/actionMenu.png"/>
</figure>
<p>Different actions can be performed from this menu, depending on the type of graph.
	Individual actions are detailed in the relevant part of this manual. Currently
	available actions are:</p>
<list>
	<item>
		<p>for all graphs:</p>
		<list>
			<item>
				<p><link xref="gui-layouts"/>;</p>
			</item>
			<item>
				<p>determination of the <link xref="tool-scc">Strongly
					Connected Components (SCC)</link> of a graph;</p>
			</item>
		</list>
	</item>
	<item>
		<p>for regulatory graphs:</p>
		<list>
			<item>
				<p><link xref="tool-simulation"/> (<em>i.e.</em> computation of a state transition graph);</p>
			</item>
			<item><p>analyse of the <link xref="tool-circuits"/>;</p></item>
			<item><p>determination of <link xref="tool-stable"/>;</p></item>
			<!--
			<item><p>running a <xref linkend="modelChecker"/>;</p></item>
			-->
		</list>
	</item>
	<item>
		<p>for state transition graphs:</p>
		<list>
			<item>
				<p><link xref="tool-find-path">path search</link>;</p>
			</item>
			<item>
				<p><link xref="tool-stg-animator">graphical path construction
				(animation)</link>.</p>
			</item>
	</list>
	</item>
</list>

</section>

<section id="secWindow">
<title>The secondary panel</title>
<p>The bottom panel allows to edit the items selected in the graph view. It contains two tabs: </p>
<list type="numbered">
	<item>
		<p>The first tab (called <em>Modelling Attributes</em> for regulatory graphs)
		will change with the type of graph. Panels for the various graph types are described
		in the corresponding sections.</p>
	</item>
	<item>
		<p>The <em>Graphical Attributes</em> tab allows to edit the appareance of the selected items.
		It is described in the <link xref="gui-graph">graph view page</link>.</p>
	</item>
</list>

</section>

