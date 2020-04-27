---
title: "Dynamical rules"
date: 2019/07/24 12:58
summary: Logical rules control changes of activity for model components
weight: 4
---


The dynamical behaviour of regulatory components depends on their regulators,
but the precise rules governing them must be explicitly defined.
In GINsim, these rules can be defined either as **logical parameters**, or
as **logical functions**. These two alternatives are described below.


Logical parameters
==================

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



Logical functions
=================


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


