---
title: "Welcome dialog"
date: 2019-07-24T12:58:00Z
summary: The welcome dialog
---


Upon launch, GINsim will present the ``Welcome`` dialog box below.

{{<fig src="welcome.png" title="The Welcome dialog shown on startup">}}{{</fig>}}

The ``New model`` action will create a new [Regulatory Graph](../../lrg),
while the ``Open`` and ``Import`` buttons allow to select an existing file
in a [supported format](../../formats).
The ``Recent files`` section allows the quick selection of a previously opened file.
For all these actions, the selected graph will be opened in a [Main Window](../main-window).


Closing this dialog or activating the ``quit`` button will stop GINsim.


{{<notice>}}
This dialog is also shown after closing the last window (``Ctrl/Cmd-W``). Use the ``Quit`` (``Ctrl/Cmd-Q``) action to skip it.
{{</notice>}}

{{<notice>}}
When running GINsim on the command line, it is possible to provide a file to open or to
ask for a new model. In this case, the welcome dialog will not be shown. See the [run options](../../installation).
{{</notice>}}

