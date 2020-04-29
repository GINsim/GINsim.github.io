---
title: TCR signalisation
aliases:
- /node/78
taxon: 
- Mammal
process: 
- Differentiation
submitter: Claudine Chaouiya
supporting_paper: Klamt2006
files: 
- TCRsig40.zginml
file_descriptions: 
- Regulatory Model
---


This Boolean model of the TCR signalling pathway, encompassing 40 regulatory
components, is based on the work of Klamt et al..
In this version of the model, an auto-regulation has been added on each input.


This model has been studied in {{<cite "models/58">}}, using novel algorithms
for the analysis of feedback circuits and the determination of stable states.
The stable state analysis shows seven stable states, listed bellow.
Each stable state corresponds to a different input combination, except "111".
Indeed, the systems shows an oscilatory behaviour under full activation.


The feedback circuit analysis shows nine circuits, besides the three auto-
activation on the inputs. Only one of these circuits is functional: (ZAP70,
cCbl). This negative circuit is functional in presence of LCK and TCRphos
which can only be maintained in presence of the three inputs. This circuit
drives the oscillatory behaviour observed under full activation.

