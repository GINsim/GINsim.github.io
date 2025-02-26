---
title: "Troubleshooting"
date: 2019-07-24T12:58:00Z
summary: Debug problems
---

# Get in touch
Some common issues are listed below, if you can not find a solution, please contact the GINsim team
or send a message to the [user support forum](http://ginsim.org/contact),
describing your problem and steps to reproduce it.
As some problems are difficult to reproduce, you may be asked to provide log traces (using the
``GINsim/support/export log traces`` menu entry) and to launch GINsim from the command
line to catch additional error messages.


# Common quirks

## Input nodes

In GINsim, some nodes can be defined as input nodes using a checkbox in the node property panel.
These input nodes can not have any incoming interaction or dynamical rule as they have an implicit rule
allowing them to always maintain their current activity level.
Before setting a node as input, the modeller must thus remove all existing regulator or rule.
Likewise, the input status must be removed before adding any new regulator or rule.
To delete a logical formula, select it (without editing it) and use the delete key or the contextual menu.


## Unexpected dynamical results

If you obtain unexpected dynamical results (stable states or simulations results), 
verify successively the structure of the regulatory graph, the maximal activity levels of all components,
the thresholds of interactions coming out of multi-valued components and then the dynamical rules.
GINsim further provides a tool to <gui>compute interaction functionality</gui>, which facilitates the
identification of inconsistencies between the structure of the regulatory graph and the dynamical rules.



## GUI refresh issues
Some refreshing problems may appear after long or complex modeling sessions, saving and restarting
GINsim can solve some issues.

