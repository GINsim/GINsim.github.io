---
title: TCR signalisation
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


Klamt et al. proposed in [@Klamt2006] a Boolean model of the TCR signalling pathway.
The model encompasses 40 regulatory components.
In this version of the model, an auto-regulation has been added on each input.


This model has been studied in [@Naldi2007], using novel algorithms
for the analysis of feedback circuits and the determination of stable states.
The stable state analysis shows seven stable states, listed bellow.
Each stable state corresponds to a different input combination, except "111".
Indeed, the systems shows an oscilatory behaviour under full activation.

!!! example "7 stable states of the model. A "*" means "all possible expression levels (i.e. 0 or 1). The expression level of all other variables is 0."
    | CD45 | CD8 | TCRlig | TCRbind | PAGCsk | Fyn | TCRphos | Ikb |
    |------|-----|--------|---------|--------|-----|---------|-----|
    | 0    | *   | 0      | 0       | 1      | 0   | 0       | 1   |
    | 0    | *   | 1      | 1       | 0      | 0   | 0       | 1   |
    | 1    | 0   | 0      | 0       | 1      | 0   | 0       | 1   |
    | 1    | 0   | 1      | 1       | 0      | 1   | 1       | 1   |
    | 1    | 1   | 0      | 0       | 1      | 0   | 0       | 1   |

The feedback circuit analysis shows nine circuits, besides the three auto-
activation on the inputs. Only one of these circuits is functional: (ZAP70,
cCbl). This negative circuit is functional in presence of LCK and TCRphos
which can only be maintained in presence of the three inputs. This circuit
drives the oscillatory behaviour observed under full activation.

