
## Availability and Requirements

GINsim 3.0 is freely available without guarantees.
Please contact us for training, other support or dedicated development.
The GINsim website [https://ginsim.github.io](https://ginsim.github.io) provides the latest official version of the software, [documentation](../documentation/index.md), as well as a [model library](../models/index.md).

!!! tip "Download versions"
    - **Latest version 3.0 beta2** on GitHub: [GINsim-3.0-beta2.jar](https://github.com/GINsim/GINsim/releases/download/V3.0-beta2/GINsim-3.0-beta2.jar)
    - **Development version** on GitHub: [GINsim-SNAPSHOT-jar-with-dependencies.jar](https://github.com/GINsim/GINsim/releases/tag/latest)
    - **All releases** on GitHub: [https://github.com/GINsim/GINsim/releases](https://github.com/GINsim/GINsim/releases)


GINsim requires Java >=8.
You can obtain Java for Linux, Windows, Mac OSX, and Solaris at java.com.
Note that Apple used to provide its own Java version, newer versions are not supported on OSX 10.6 and older.
GINsim 2.9.10 is the last version supporting Java 6, and has the same features as GINsim 3.0.

Some features of GINsim rely on external tools, such as the NuSMV model checker.

### Running GINsim
Once you have obtained GINsim, you can launch it by double-click or with the command:

```bash
$ java -jar GINsim-#version.jar
```


The following options are available for GINsim:

    file: open file on startup (skip the Welcome dialog).
    -n: start with a new regulatory graph (skip the Welcome dialog).
    -h: help message.
    -s: run GINsim in script mode
    -lm : Let the bioLQM library parse the command line arguments.
    --dev : enables some experimental features still in under development.
    -py : launch a server for the py4j python gateway (used for scripting in the Python Notebook).

The JAVA virtual machine provide many options, in particular GINsim can benefit from extending the amount of memory available, with the `-Xmx` option. For example, one can launch GINsim with 1000MB of memory using `java -Xmm1000M -jar GINsim-#version.jar`.

## Terms of use

By browsing this web site, you acknowledge and accept its general terms of use described below.

**Personal data**: GINsim and this web site do not collect any personal data beyond access logs.

**Content**: The content of this website is available under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International, unless stated otherwise on specific pages.

**Hyperlinks**: The editors do not take responsibility for the content of external web sites accessible by hyperlinks from this web site. Hyperlinks by third parties to pages of this web site are authorized as long as this web site can be duly identified.

**Modification**: The editors might change these terms of use without prior warning.

## License

This software is licensed under the [GNU General Public License v3.0](https://github.com/GINsim/GINsim/blob/main/LICENSE).



