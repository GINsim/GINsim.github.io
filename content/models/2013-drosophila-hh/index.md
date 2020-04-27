---
title: "Drosophila Hh Signalling pathway"
aliases:
- /node/144
taxon: 
- D. melanogaster
process: 
- Signalling
submitter: Abibatou MBODJ and Denis THIEFFRY
supporting_paper: "88"
files: 
- Hh__Pathway_11Jun2013.zginml
- Hh_Pathway_Documentation_11May013.pdf
file_descriptions: 
- GINsim file for Drosophila Hh Signalling pathway
- Drosophila Hh Signalling pathway model documentation
---


Processing of HH ligand The precursor of HH is auto-catalytically cleaved to produce an
N-terminal (HH-N) and a C- terminal (HH-C) fragments {{<cite "models/128" "models/133">}}.
A cholesterol moiety is covalently attached to the last amino acid of HH-N to create HH-Np,
that is responsible for the biological activities of HH proteins
{{<cite "models/128" "models/133" "models/129">}}. The N-terminal region of HH-Np
is further modified by addition of palmitate that is essential for its signalling activity
{{<cite "models/134" "models/135" "models/136" "models/137" "models/130" "models/138">}}.
We model these aspects by an AND rule (combining inputs
from DLP, IHOG, Rasp, DISP, SHF, Lipophorin, BOI and DALLY) attached to the
component representing the secreted HH molecule, denoted Hh in our model. HH
Signalling Two integral membrane proteins are involved in HH signal reception:
Patched and Smoothened. HH binding to its receptor Patched (PTC) relieves PTC-
mediated repression of Smoothened (SMO), a serpentine-like membrane protein
required for HH signalling {{<cite "models/139" "models/140">}}. This allows
SMO stabilisation, activation, and phosphorylation by Shaggy (SGG), and downstream
signalling through the formation of a protein complex including the serine threonine
kinase Fused (FU), the kinesin-like protein Costa (COS), and the protein
Suppressor of Fused (SUFU), ultimately controlling the post-translational
processing of the protein Cubitus interruptus (CI) {{<cite "models/141">}}.
In the absence of HH, COS binds CI directly and sequesters it in the cytoplasm
with the help of SUFU. The recruitment of different kinases (Casein kinase 1 alpha,
Shaggy, Protein kinase A) then leads to the phosphorylation of CI and to its
proteolysis by SLMB. The resulting truncated protein (CI_rep) is released and
enters the nucleus, where it has a transcriptional repressing activity. Recent
evidence further indicates that SMO is inhibited by TOW, which tentatively
mediates the effect of PTC on SMO {{<cite "models/142" "models/143">}}.
Following SMO activation, the transcription factor CI is phosphorylated and
translocated into the nucleus in its entire form, which plays a transcriptional
activatory role (CI_act). In the model, a cascade of inhibitions, from HH on PTC,
and from PTC on SMO, implements the indirect positive action of HH on SMO. A protein
complex including CI, COS, and FU, phosphorylates and thereby inhibits SU(FU),
ultimately favouring the CI activatory form and its translocation into the
nucleus. We model the roles of the kinases (SGG, PKA, and CK1a), COS and
SU(FU) (both needed to recruit the kinases) in the processing of CI in terms
of inhibitory interactions on CI_act and activatory interactions on CI_rep
{{<cite "models/131" "models/127">}}. Complexes are represented implicitly
(they are formed as soon as the components are synthesised or activated), while
logical rules define component activity requirements to form CI_act versus CI_rep
forms. To explore the dynamic of the pathway, we define two initial states to
simulate the presence and the absence of signalling. On one hand, the non binding
of HH (level expression 0) triggers a series of signalling cascades that lead to
the activation of several kinases (for example SGG, PKA, CK1a, ...) at level of
expression 1, which will permit the formation of CI repressor (expressed at
level 1), which in turn will inhibit the targets. On the other hand, the
presence of HH (level of expression 1) leads to a stable state corresponding
to the signalling conditions leading to the formation of CI activator that
will activate the targets node (level of expression 1).

