---
title: "Drosophila VEGF Signalling pathway"
aliases:
- /node/160
taxon: 
- D. melanogaster
process: 
- Signalling
submitter: Abibatou MBODJ and Denis THIEFFRY
supporting_paper: "88"
files: 
- VEGF_Pathway_12Jun2013.zginml
- VEGF_Pathway_Documentation_11May2013.pdf
file_descriptions: 
- GINsim file for Drosophila VEGF Signalling pathway
- Drosophila VEGF Signalling pathway model documentation
---


VEGF (also called PDGF or PVF) pathway participates in different developmental
processes, including border cell migration, hemocyte migration and survival,
thorax closure during metamorphosis, the rotation and dorsal closure of the
male terminalia. and embryonic salivary gland tissue migration. The ability of
PVR to activate the MAP-kinase pathway is important for control of cell growth
and differentiation in other tissues. Three genes in the Drosophila genome
code for PVR ligands: PVF1, PVF2, and PVF3. Binding of one of the ligands
(PVF1, 2 or 3) to the receptor PVR triggers the canonical DRK/SOS/RAS/RAF/DSOR1/RL
pathway {{<cite "models/155" "models/159" "models/158" "models/156" "models/157" />}}.
DOF is needed to assemble the PVR receptor and allow it to auto-phosphorylate,
likely as an adaptor that links the receptor to RAS pathway. DOF is a cytoplasmic
protein which is expressed ubiquitously only in cells that express the FGF receptors.
It contains an ankyrin repeat, a coiled-coil structure and many tyrosines
within environments that suggest that if phosphorylated they act as binding
sites for the SH2 domains of proteins such as DRK or CSW {{<cite "models/101" />}}.
The SH2-domain-containing protein DRK recruits the guanine nucleotide exchange
factor, Son of sevenless (SOS), to catalyze the exchange of GDP bound to RAS
for GTP, thereby activating RAS with the help of activated KSR. RAS promotes
the activation of RAF, leading to the activation of DSOR1, and ultimately to
that of the MAP kinase Rolled (RL ). Rolled can activate transcription, both
through inactivation of transcriptional co-repressors such as AOP, as well as
through the activation of transcription factors such as the ETS-domain-containing
protein Pointed (PNT) {{<cite "models/154" "models/90" />}}. The activation of PNT
is a major output of the pathway. It is either phosphorylated by MAP kinase to
produce an active transcriptional activator (PointedP2), or transcriptionally
induced by MAP kinase to produce a constitutive transcriptional activator (PointedP1).
Sprouty (STY) acts downstream of the receptor, but upstream of RAS1 and RAF,
by recruiting GAP1 and blocking the ability of DRK to bind to its positive
effector. We have considered three typical initial states corresponding to i.
ligands binding in wild-type signalling enabling situation (VEGF_signalling),
ii. ligand binding in the presence of the inhibitor Sprouty
(Sprouty_inhibition), iii. absence of ligand (No_signalling).

