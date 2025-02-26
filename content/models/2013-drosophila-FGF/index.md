---
title: "Drosophila FGF Signalling pathway"
aliases:
- /node/102
taxon: 
- D. melanogaster
process: 
- Signalling
submitter: Abibatou MBODJ and Denis THIEFFRY
supporting_paper: "88"
files: 
- FGF_Pathway_12Jun2013.zginml
- FGF_Pathway_Documentation_11May2013.pdf
file_descriptions: 
- GINsim file for Drosophila FGF Signalling pathway
- Drosophila FGF Signalling pathway model documentation
---


Drosophila genome encodes two FGF receptors, HTL (Heartless) and BTL
(Breathless), which are required for the morphogenesis of different tissues.
BTL is expressed in the tracheae, while HTL is expressed in embryonic mesoderm
and was first identified because of its essential role in heart development.
BTL ligand, BNL is encoded by the branchless gene {{<cite "models/98" />}}.
THS (Thisbe) and PYR (Pyramus) function in a partially redundant fashion to
activate heartless (htl).
Upon ligand binding receptor dimerization triggers the canonical
DRK/SOS/RAS/RAF/DSOR1/RL pathway. In contrast with other RTKs, Stumps is
needed to trigger signal transduction {{<cite "models/99" "models/153" />}}.
Stumps is a cytoplasmic protein expressed in cells also expressing the
FGF receptors. The presence of an ankyrin repeat, a coiled-coil structure
and many tyrosines suggests that Stumps could bind SH2 domains of proteins
such as DRK or CSW {{<cite "models/101" />}}. As a
result, DRK recruits the guanine nucleotide exchange factor SOS (Son of
sevenless), which catalyzes the exchange of GDP bound to RAS for GTP.
Activated RAS then promotes the activation of RAF (Pole hole), DSOR1, and
eventually that of RL (Rolled). RL can activate transcription through the
inactivation of transcriptional co-repressors such as Anterior Open (AOP), as
well as through the activation of transcriptional activators such as PNT
(Pointed, with two forms denote by suffixes P1 and P2) {{<cite "models/154" "models/90" />}}.
The negative regulator STY (Sprouty) acts downstream of SOS but upstream of RAS
and RAF, by recruiting GAP1 and blocking the ability of DRK to bind to its
positive effector. Our model enables the simulation of pathway responses to
different ligand combinations. In this regard, we define four initial states
to simulate different behavior of the pathway. The first initial state
reproduces the signalling through the receptor HTL (bound by Pyr and Ths), the
second initial state corresponds to the signalling through the receptor BTL,
the third initial state corresponds to the involvement of the inhibitor
Sprouty during signalling conditions and the fourth initial state corresponds
to the absence of signalling (no ligands binding). Each of these initial
states lead to a specific stable state representative of in vivo conditions.


