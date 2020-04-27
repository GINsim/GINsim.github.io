---
title: "The Z-GINML format"
summary: The native file format in GINsim
date: 2019/07/24
---

The Z-GINML format (also denoted **extended save**), is a zip archive containing a ginml file along with
companion files to store associated data, especially initial states, perturbations, and simulation parameters.
More generally, each plugin can provide a parser and file writer to store its associated data in a Z-GINML file.


The **GINML** format is an extension of the [GXL (Graph eXchange Language)](http://www.gupro.de/GXL) format.
This extension comprises new attributes and subelements for elements node and edge, and an additional element called parameter.


<terms>
<item><title>element node</title>
    <p>a new attribute basevalue corresponds to the "based level of expression" of the corresponding component (default value 0).
        In other words, it is the value of the logical parameter corresponding to the case where none of the incoming interactions if functional.
        New subelements within a node:
    </p>
    <list>
        <item><p>a list of elements parameter corresponding to the user defined logical parameters for this node</p></item>
        <item><p>an element intdefining the maximum level of expression of this node</p></item>
    </list>
</item>
<item><title>element edge</title>
<p>a new attribute sign which gives the sign of the interaction (positive for an activation, negative for a repression, otherwise unknown)
one or two subelements int (level or interval letting the interaction functional)
element parameter, is empty and has two attributes :
attribute idActiveInteractions gives the "name" of the parameter. It is the list of the functional interactions exerted upon the considered node,
attribute val is the value of the logical parameter.</p>
</item>
</terms>


See the GINML's dtd or in pdf format 
See also the GINML description of the gap-gene network case A, or in pdf format.


# TODO: described stored associated data

Some companion data can be associated to the graphs to store the configuration of various tools.
Some of this extra data can be shared between several tools.
This extra data is stored in its own entry inside ZGINML files.


