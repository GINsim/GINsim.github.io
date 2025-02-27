---
title: "Drosophila EGF Signalling pathway"
aliases:
- /node/96
taxon: 
- D. melanogaster
process: 
- Signalling
submitter: Abibatou MBODJ and Denis THIEFFRY
supporting_paper: "88"
files: 
- EGF__Pathway_12Jun2013.zginml
- EGF_Pathway_Documentation_11May2013.pdf
file_descriptions: 
- GINsim file for Drosophila EGF Signalling pathway
- Drosophila EGF Signalling pathway model documentation
---


Four activating ligands, Spitz, Keren, Gurken and Vein have been identified
for drosophila EGF receptors, called DER. Spitz (SPI) is the major ligand and
is involved in most situations where the pathway is activated. Keren plays a
minor, redundant role, while Gurken is used exclusively during oogenesis.
These ligands are produced as inactive transmembrane precursors, which are
retained in the endoplasmic reticulum and needed to processed by the chaperone
protein Star. Processed ligands are directed into another compartment where
they encounter Rhomboid (RHO) serine proteases, which cleave the ligand
precursors within the transmembrane domain to release the active, secreted
ligand form. RHO also cleaves and inactivates Star, attenuating the level of
cleaved ligand that is produced. The fourth ligand, Vein, is produced as a
secreted molecule, which is a weaker activating ligand used either to enhance
signalling by other ligands or in specific situations such as muscle
patterning. Binding of ligands to DER leads to dimerization and triggering of
the canonical DRK/SOS/RAS/RAF/DSOR1/Rolled pathway. DRK (SH2-domain-containing
protein) recruits SOS (Son of sevenless, a guanine nucleotide exchange factor)
to catalyze the exchange of RAS bound GDP for GTP exchange, thereby activating
RAS. RAS then promotes the activation of RAF, leading to DSOR1 activation, and
eventually to Rolled (RL) activation. RL inactivates transcriptional co-
repressors, such as Aop, and activates transcription factors, such as Pointed
(PNT) ({{<cite "models/90" >}}).
The transcriptional activator PNT is the major effector of the pathway.
The protein Anterior open (AOP) is a constitutive repressor,
which competes for PNT binding sites and can be removed from the nucleus and
degraded upon phosphorylation by MAP kinases. AOS (Argos), STY (Sprouty) and
KEK (Kekkon) are inducible repressive elements involved in negative feedbacks.
AOS is a secreted molecule, which sequesters the ligand SPI (Spitz). STY acts
downstream of DER, but upstream of RAS and RAF, by recruiting GAP1 and
blocking the ability of DRK to bind to its positive effector. KEK is a
transmembrane protein forming a non-functional heterodimer with the receptor.
Constitutively expressed, CBL (E3 ligase) modulates DER signalling by
recognizing activated, internalized receptor molecules and inducing their
ubiquitination and degradation. CBL may also enhance the endocytosis of DER,
following ligand binding. Modulation of DER signalling by CBL has been
reported only in the follicle cells, which receive the Gurken signal from the
oocyte ({{<cite "models/92" "models/93" "models/94" "models/95" >}}).

Our logical model represents a cell receiving different
combinations of ligands binding (SPI or Vein or both) and express/receive
different levels of inhibitory inputs (Aos, Sty, Cbl, Kek).
The signalling pathway is characterized by no signalling, medium or high
signalling process designed by multi-valued nodes. We consider five main wild-
type cellular situations:

1. Cells secreting ligands but lacking Der activation (inhibition of Der),
   leading to no signalling.
2. Cells receiving medium signal with SPI expressed at level 1 and/or Vein
   expressed also at level 1, leading to medium signalling.
3. Cells receiving SPI at level of expression 1 (and/or Vein expressed at level 1)
   and in presence of an inhibitor (e.g. STY, AOS, or KEK), leading to no signalling.
4. Cells receiving SPI at level of expression 2 in the absence of inhibitors,
   leading to high signalling.
5. Cells receiving SPI at level of expression 2 (and/or Vein expressed at level 1) in
   presence of an inhibitor (e.g. STY, AOS, or KEK,...), leading only to medium signalling.

