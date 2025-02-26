---
title: "Booleanize models"
date: 2019-07-24T12:58:00Z
Summary: Boolean mapping for multivalued models
---


GINsim enables the definition of multi-valued models where some components can
have several increasing activity levels. However, some other analysis tools only
consider Boolean (on/off) models.
Model booleanization allows to convert multi-valued models into Boolean models
by mapping each multivalued component on a group of Boolean variables. The
resulting Boolean model generates the same dynamical behaviour as the original
multivalued model.

bioLQM uses the mapping originaly proposed by van Ham, in which a component
associated with the maximal value ``m`` will be mapped on ``m`` Boolean components.
For example, a component taking the values ``0`, ``1``, ``2``, and ``3`` will be
encoded as ``000``, ``100``, ``110``, and ``111``.

The booleanization introduces many non-admissible states, which may require special
care depending on the analysis applied on the booleanized model. This modifier makes
sure that a simulation which start with an admissible state will not explore 
non-admissible states. It also prevents the introduction of non-admissible attractors
by making sure that at least one admissible state is reachable from any non-admissible.


Usage
=====

Exporting a multivalued model to a format limited to Boolean components triggers an implicit Booleanization step.
This booleanization step can also be performed explicitely using the booleanization tool in the ``Actions`` menu.

Availability and further reading
=================================

This method was implemented in GINsim 3.0.
The backend is implemented in the 
[bioLQM toolkit](http://colomoto.org/biolqm),
enabling its programmatic use.

