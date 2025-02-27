---
title: "Composition"
date: 2019-07-24T12:58:00Z
Summary: Composing multiple instances of an LRG, based on neighbour integration functions
---


Models of inter-cellular regulation can be viewed as the coordination
between logical modules governing the intracellular regulatory interactions.
This coordination is achieved by inter-cellular communication which is made
operational by having external regulators influence the state of components
in each intracellular module. By making the inter-cellular regulatory relations
explicit, it is possible to obtain a global logical model describing the whole
system. This tool provides a generic method to obtain this global model from
the composition of identical individual logical modules {{<cite Mendes2013 >}}.

Usage
=====

The composition tool is available in the ``Actions`` menu. It opens a
composition specification dialog in which the user can specify the
parameters of the composition.

The LRG currently loaded will be used as the intracellular module of the composition. In order for the composition to be meaningful, it is necessary that the LRG contains at least one input component, which will integrate the signals originating from external modules.

In this composition specification dialog the user indicates:

* The number of instances of the composition, which refers to the number of logical modules to be composed
* The neighbourhood relation between instances, which is a non-reflexive relation establishing which instances are in the vicinity and, consequently, can influence each instance. In general, this relation is not symmetrical meaning that if module 1 has module 2 as its neighbour, the former is influenced by the latter, but the reverse is not true unless otherwise specified. The ``Symmetry`` option makes all neighbourhood relations symmetrical automatically.
* The logical integration function for each input the user wishes to map.
  
  The available logical integration functions are ``OR``, ``AND`` (for components taking Boolean values), ``MAX``, ``MIN`` and ``THRESHOLD2`` (for components taking other values). The ``THRESHOLD2`` function has multi-valued arguments and produces a Boolean result, being <code>true</code> only if at least one argument takes value 2 or above. The arguments of the logical integration function can be specified as any subset of proper components. Depending on the type of input component being mapped and the proper components selected as arguments, the list of available logical integration functions is automatically updated.
  
  By selecting a logical integration function and a subset of proper components as arguments, the value of the mapped input component will be governed by the value of the integration function applied to the corresponding arguments in all the neighbouring instances. For example, if an input component ``U0`` is mapped to an ``OR`` of the proper components ``G1`` and ``G2``, then, for the first instance ``1`` (which, suppose,  has instances ``2`` and ``3`` as neighbours), the input component will be the disjunction of the values of ``G1`` and ``G2`` in instance ``2`` and the values of the same components in instance ``3``. Consequently, all mapped input components rely on the same neighbouring relation.
* Whether the composed model should be reduced with respect to the mapped input components.
  
  The reduction option will remove the mapped input components from the composed model and reflect the regulatory effects of components external to each module onto the components regulated by the mapped input component. The reduced composed model corresponds to the most natural dynamics expected from the composition, since the mapped input components in the composed model are "dummy" components for which no delays are associated to the corresponding value updates.
  
  The option not to reduce the resulting composed model should only be used to elicit fine tuning of the integration functions for particular modules.



Availability and further reading
=================================

This method was implemented in GINsim 3.0.


