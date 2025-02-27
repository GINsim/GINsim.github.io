---
title: "Documentation"
date: 2025-02-27T00:00:00Z
---

GINsim (Gene Interaction Network simulation) is a computer tool for the modeling and simulation of genetic regulatory networks.

Recent developments in functional genomics have generated large amounts of data on gene expression and on the underlying regulatory mechanisms. This has resulted in the progressive mapping of complex regulatory networks. As these networks usually include numerous intertwined feedback circuits, gaining an understanding of their spatio-temporal behaviour defies the intuition of the biologists. In this respect, formal modelling and simulation tools become a necessary complement to experimental tools. As precise information on molecular mechanisms and the value of kinetic parameters are currently difficult to establish, qualitative methods offer a highly attractive approach to model and analyse essential properties of genetic regulatory networks.
General information on modelling and analysis of genetic regulatory networks can be found in {{ <cite deJong2002> }}.

GINsim consists of a simulator of qualitative models of genetic regulatory networks based on a discrete, logical formalism.

GINsim allows the user to specify a model of a genetic regulatory network in term of asynchronous, multivalued logical functions, and to simulate and/or analyse its qualitative dynamical behaviour {{ <cite Chaouiya2012> }}.




### Install and Run GINsim

#### Availability and Requirements

GINsim 3.0 is freely available without guarantees.
Please contact us for training, other support or dedicated development.
The GINsim website (https://ginsim.github.io)[https://ginsim.github.io] provides the latest official version of the software, documentation, as well as a model library.

GINsim requires Java 8. 
You can obtain Java for Linux, Windows, Mac OSX, and Solaris at java.com.
Note that Apple used to provide its own Java version, newer versions are not supported on OSX 10.6 and older.
GINsim 2.9.10 is the last version supporting Java 6, and has the same features as GINsim 3.0.

Some features of GINsim rely on external tools, such as the NuSMV model checker.

#### Running GINsim
Once you have obtained GINsim, you can launch it by double-click or with the command `java -jar GINsim-#version.jar`.

The following options are available for GINsim:
    * file: open file on startup (skip the Welcome dialog).
    * -n: start with a new regulatory graph (skip the Welcome dialog).
    * -h: help message.
    * -s: run GINsim in script mode
    * -lm : Let the bioLQM library parse the command line arguments.
    * --dev : enables some experimental features still in under development.
    * -py : launch a server for the py4j python gateway (used for scripting in the Python Notebook).
    
The JAVA virtual machine provide many options, in particular GINsim can benefit from extending the amount of memory available, with the `-Xmx` option. For example, one can launch GINsim with 1000MB of memory using `java -Xmm1000M -jar GINsim-#version.jar`.


### Contact
Please send your comments, questions or suggestions to the public user group GINsim Users at ginsim-users@googlegroups.com, describing your problem and steps to reproduce it. 
As some problems are difficult to reproduce, you may be asked to provide log traces (using the GINsim/support/export log traces menu entry) and to launch GINsim from the command line to catch additional error messages.

Specific questions can also be adressed to the GINsim team at support@ginsim.org.
o


### Common quirks

#### Input nodes
In GINsim, some nodes can be defined as input nodes using a checkbox in the node property panel. These input nodes can not have any incoming interaction or dynamical rule as they have an implicit rule allowing them to always maintain their current activity level. Before setting a node as input, the modeller must thus remove all existing regulator or rule. Likewise, the input status must be removed before adding any new regulator or rule. To delete a logical formula, select it (without editing it) and use the delete key or the contextual menu.


#### Unexpected dynamical results
If you obtain unexpected dynamical results (stable states or simulations results), verify successively the structure of the regulatory graph, the maximal activity levels of all components, the thresholds of interactions coming out of multi-valued components and then the dynamical rules. GINsim further provides a tool to compute interaction functionality, which facilitates the identification of inconsistencies between the structure of the regulatory graph and the dynamical rules.


#### GUI refresh issues
Some refreshing problems may appear after long or complex modeling sessions, saving and restarting GINsim can solve some issues.


### GUI

#### Welcome dialog
Upon launch, GINsim will present the ``Welcome`` dialog box below.

{{<fig src="welcome.png" >}}{{</fig>}}

The ``New model`` action will create a new [Regulatory Graph](#regulatory-graph),       
while the ``Open`` and ``Import`` buttons allow to select an existing file      
in a [supported format](#formats).
The ``Recent files`` section allows the quick selection of a previously opened file.
For all these actions, the selected graph will be opened in a [Main Window](#main-window).


Closing this dialog or activating the ``quit`` button will stop GINsim.         


{{<notice>}}
This dialog is also shown after closing the last window (``Ctrl/Cmd-W``). Use the ``Quit`` (``Ctrl/Cmd-Q``) action to skip it.
{{</notice>}}

{{<notice>}}
When running GINsim on the command line, it is possible to provide a file to open or to
ask for a new model. In this case, the welcome dialog will not be shown. See the [run options](#install-and-run-ginsim).
{{</notice>}}

