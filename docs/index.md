# Welcome to GINsim

![GINsim logo](ginsim.svg){: style="width: 120px; float: left; margin-right: 10px;"}

GINsim (Gene Interaction Network simulation) is a software tool for the design and analysis of qualitative dynamical models of genetic regulatory networks.

Recent developments in functional genomics have generated large amounts of data on gene expression and on the underlying regulatory mechanisms. 
This has resulted in the progressive mapping of complex regulatory networks. As these networks usually include numerous intertwined feedback circuits, gaining an understanding of their spatio-temporal behaviour defies the intuition. 
Formal modelling approaches become a necessary complement to experimental tools. 
As precise information on molecular mechanisms and the value of kinetic parameters are currently difficult to establish, qualitative methods offer a highly attractive approach to model and analyse essential properties of genetic regulatory networks.


## Logical modelling formalism

GINsim consists of a simulator of qualitative models of genetic regulatory networks based on a discrete, logical formalism.

GINsim allows the user to specify a model of a genetic regulatory network in term of asynchronous, multivalued logical functions, and to simulate and/or analyse its qualitative dynamical behaviour.

## Citing GINsim

!!! info "If you use GINsim, please cite it using the following publication"
    Aurélien Naldi, Céline Hernandez, Wassim Abou-Jaoudé, Pedro T. Monteiro, Claudine Chaouiya, and Denis Thieffry. **Logical modeling and analysis of cellular regulatory networks with GINsim 3.0**. _Frontiers in Physiology_, June 2018. [doi:10.3389/fphys.2018.00646](https://doi.org/10.3389/fphys.2018.00646)


## Main features

!!! example "Model editor"
    ![GINsim](edit.svg){: style="float: left; margin-right: 10px;"}

    - Build qualitative models in a graphical interface.
    - The [regulatory graph](documentation/index.md#logical-regulatory-graph) represent interactions between biological entities.
    - [Logical rules](documentation/index.md#dynamical-rules) define the dynamical behaviour of each component.
    - [Annotations](documentation/index.md#annotations) keep track of the underlying knowledge.
    - Apply [perturbations](documentation/index.md#perturbations) to account for mutants or alternative hypothesis.
    - [Reduce](documentation/index.md#model-reduction) complex models by hiding intermediate components.



!!! example "Dynamical analysis"
    ![STG](simulation.svg){: style="float: left; margin-right: 10px;"}

    - Visualize simulation results as [state transition graphs](documentation/index.md#state-transition-graphs).
    - The non-deterministic trajectories represent alternative cell fates.
    - Efficient identification of some dynamical properties, up to complex models.
    - [Fixed points](documentation/index.md#stable-state-search) and [trap spaces](documentation/index.md#trapspace-search) are attractors of the system.
    - [Functional circuits](documentation/index.md#circuit-analysis) highlight key interactions in the model.



!!! example "Interoperability"
    ![CoLoMoTo](colomoto.png){: style="float: left; margin-right: 10px;"}

    GINsim can load and export models from the [SBML qual](https://sbml.org/documents/specifications/level-3/version-1/qual/) format, enabling to share them with other software tools. Its integration in the [CoLoMoTo notebook](https://colomoto.github.io/colomoto-docker/) enables the definition of complex, reproducible anlysis workflows.

    - Efficient reachability analysis using [pint](http://loicpauleve.name/pint);
    - Complex reachability analysis using the [NuSMV model checker](https://nusmv.fbk.eu);
    - Quantification of reachability probabilities using [MaBoSS](https://maboss.curie.fr);
    - 2D modelling of a cellular tissue using [Epilog](http://epilog-tool.org). 

