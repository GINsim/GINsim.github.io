---
title: "Drosophila eggshell patterning"
summary: Prototype software for the analysis of epithelial patterning
aliases:
- /node/176
---

{{<notice>}}
As of 2019, the prototype software described on this page has been
superseded by the [Epilog tool](http://epilog-tool.org).
{{</notice>}}


This prototype software has been developed mainly by Adrien Fauré (with some help from Oltman de Wiljes)
to create and simulate logical models of epithelia, in the context of a research project on Drosophila
oogenesis (project supported by the FCT, PTDC/EIA-CCO/099229/2008).
It is made available to facilitate reproduction of all results described in the manuscript mentioned below.
A user-friendly software is currently under development, based on the principles of this prototype.

Adrien Fauré, 2013-12-12


Reference:
    Adrien Fauré, Barbara M.I. Vreede, Elio Sucena, Claudine Chaouiya. A comprehensive model of EGF and BMP pathways reveals cell-autonomous and juxtacrine effects patterning the Drosophila eggshell. 


# EPITHELIAL MODELS

An epithelial model is defined as a grid of hexagonal cells.
Each cell has six direct neighbors, except along the left and
right borders: the grid forms a cylinder.

Cells are assigned the same set of variables and associated logical rules,
thus defining a cellular logical model. Rules specify each component's target
level, depending on the levels of its regulators, including regulators from
other cells within a radius specified by the user.

The values of the variables can be visualised on the grid according to a user-defined color code.


# LOGICAL RULES

Rules are written with each cell as the reference point.
One rule has to be specified for each non-0 value of each variable.
The syntax used for logical rules is based on python code that is
interpreted by the programme.

* To check the value of a cellular variable:
  self.parentcell.getspecies('species').value returns the value of the variable "species".
* To check the value of an extracellular variable:
  self.parentcell.haswith(species, distance, value) returns the number of cells within
  the distance = (min, max) interval where the specified variable (species) has the
  specified value. If distance is omitted, default is "(1,1)"; if value is omitted,
  default is "1".
* Logical operators ("and", "or" and "not") can be used, as well as relational
  operators ("==", "<",">","<=", ">=", "!=").

## Example:

self.parentcell.getspecies('X').value==1 or self.parentcell.haswith('Y', value=2, distance=(0,3))>=10

will return true if variable X equals 1 in the cell, or if the cell has at least 10 neighbours having Y at level 2 within a [0,3] radius (thus including the cell itself in this case).


# STATES

A "state" corresponds to the levels of all variables, in all cells of the model.
In practice, a state can be saved as a list of cells where variables have a non-zero
value (level 0 being treated as the default). The current state can be visualised on
the grid, and specific states can be saved to be loaded later.


# SIMULATION

Simulations are carried out synchronously, step by step, from the current state, 
for all variables in all cells. Whenever needed, some variables may be assigned
a priority in the form of an integer, with 1 being the highest priority.

For example, in the Drosophila eggshell patterning mechanistic model, inputs 
(and the gene Midline that is downstream to only inputs) are given priority 1;
integration variables that count the number of cells expressing Rho, Aos and Br
in the neighbouring cells are given priority 2; EGFR, which rapidly integrates
these signals, is given priority 3; other components are given priority 4.


# HANDLING MUTATIONS

There is no explicit way to define mutant cells.
The simplest possibility is to define a "mutant" variable as a self-maintaining
input to the component to be mutated. That component's rule can then be adjusted
to define its behaviour in presence or absence of the mutation.


# GUI

* File menu: 
  * New: create a new grid. Specify the grid's dimensions and click "Create".
  * Open: open an existing model
  * Save: save the current model. Model are saved as text files that include
    the list of species and their logical rules, and a list of states.
* Edit menu:
  Select or unselect all cells to visualise and change their parameters
  (the value of their variables) through the right panel.
  ("Unselect" actually selects all cells, only not showing the dark line around them, used for screen shots)
* States menu: Save, load or delete states.
* Simulation panel:
  Click to update the model, by one or up to ten steps. Upon the second choice, the simulation 
  will stop either after ten steps or when a stable state is reached, in which case the number
  of steps will be displayed in the panel. The panel also displays the list of genes components
  that have been updated.
* canvas:
  Displays the grid that represents the epithelial model.
  Click (left mouse button) on a cell to select it.
  Hold to select several cells.
  (For simplicity, clicks around the top to bottom parts of the cell are not taken into account.
  This actually permits to select discontinuous regions...)
* right column:
  Top part shows the list of the variables along with their values in the selected cells.
  Select one or several variables and click "Show" to display their values on the grid in
  the user-defined color code.
  Lower part allows the user to select one variable and modify its value in the selected cells.
* bottom panel:
  Left part lets the user select one variable (independently from the right column parameter panel)
  and visualise or modify its parameters (name, maximum value and color), along with the logical rules.
  To modify the name, max level or color, simply click on the corresponding field and enter a new value,
  then set the focus elsewhere (e.g. by clicking on an other field) to validate. White background 
  indicates the value displayed in the field is the one stored in the model; yellow, that it's been
  modified but not yet validated; red, that the value entered is not acceptable (e.g., entering a
  variable name that already exists, or a negative max value, etc.).
  To modify the logical rule, click on the rule for one level and then click the "edit rule" button.
  Then in the new panel, edit the rule and click the set button to validate.


# Download

All files in a [single archive](AllFiles.zip) containing:

* Python prototype implementing the simulation of the epithelial models.
* Phenomenological cellular model: phenomenological_cellular.zginml (GINsim file)
* Mechanistic cellular model: mechanistic_cellular.zginml(GINsim file)
* Phenomenological epithelial model: phenomenologic_epithelium.txt (text file to be loaded from the python prototype)
* Mechanistic epithelial model: mechanistic_epithelium.txt (text file to be loaded from the python prototype) 

