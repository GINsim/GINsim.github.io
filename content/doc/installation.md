---
title: "Install and Run GINsim"
date: 2019/07/24 12:58
summary: Availability, requirements, first run
weight: 1
---


GINsim 3.0 is freely available without guarantees. Please contact us for training,
other support or dedicated development.
The [GINsim website](http://www.ginsim.org) provides the latest official
version of the software, documentation, as well as a model library.


GINsim 3.0 requires Java 8. You can obtain Java for Linux, Windows, Mac OSX,
and Solaris at http://www.java.com. Note that Apple used to
provide its own Java version, newer versions are not supported on OSX 10.6
and older.


Some features of GINsim rely on external tools, such as the NuSMV model checker.


Running GINsim
==============

Once you have obtained GINsim, you can launch it by double-click
or with the command ``java -jar GINsim.jar``.


The following options are available for GINsim:

* ``file``: open ``file`` on startup (skip the <link xref="starting-welcome" />).
* ``-n``: start with a new regulatory graph (skip the <link xref="starting-welcome" />).
* ``-h``: help message.
* ``-s``: run GINsim in <link xref="advanced-script">script mode</link>
* ``-lm`` : Let the bioLQM library parse the command line arguments.
* ``--dev`` : enables some experimental features still in under development.
* ``-py`` : launch a server for the py4j python gateway (used for scripting in the Python Notebook).

Furthermore, [the JAVA virtual machine provides many options](http://docs.oracle.com/javase/6/docs/technotes/tools),
in particular GINsim can benefit from extending the amount of memory available, with the ``-Xmx`` option.
For example, one can launch GINsim with 1000MB of memory using ``java -Xmm1000M -jar GINsim.jar``.


