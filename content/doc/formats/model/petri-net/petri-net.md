---
title: "Petri net Export"
summary: Export LRG as Petri net
date: 2019-07-24T00:00:00Z
---


Regulatory graphs can be exported into discrete <!-- TODO: check nomenclature with claudine -->
Petri net using the rewriting method described in {{<cite Chaouiya2006 >}}.

In the "File -> Export" menu, a "Petri Net" submenu permits to choose one of three supported Petri net representations: INA, PNML and APNN.
Choosing any of these representations, opens a configuration dialog box which presents a list of options to be considered in the export.
These include modifications such as model perturbations or reductions, or the definition of a set of initial states.


{{<fig src="pnexport.png" title="The Petri Net export dialog">}}
The Petri Net export dialog box allows to select the export format, the initial markup and the 
mutant to apply before exporting. The initial markup can be generated from an existing initial state
of the model  (modifications made in this dialog are also applied to the simulation settings); only the 
first selected state is used.
{{</fig>}}

TODO: update figure!


