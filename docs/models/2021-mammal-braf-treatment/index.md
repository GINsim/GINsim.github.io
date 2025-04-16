---
title: "Response to BRAF treatment in melanoma and colorectal cancer"
taxon: 
- Mammal
- Human
process: 
- Cancer
submitter: Aurelien Naldi
supporting_paper: "247"
files: 
- BRAF_Model.zginml
file_descriptions: 
- BRAF model
---

The study of response to cancer treatments has benefited greatly from the contribution of different
omics data but their interpretation is sometimes difficult. Some mathematical models based on
prior biological knowledge of signaling pathways, facilitate this interpretation but often require
fitting of their parameters using perturbation data. We propose a more qualitative mechanistic
approach, based on logical formalism and on the sole mapping and interpretation of omics data,
and able to recover differences in sensitivity to gene inhibition without model training. This
approach is showcased by the study of BRAF inhibition in patients with melanomas and colorectal
cancers who experience significant differences in sensitivity despite similar omics profiles.

We first gather information from literature and build a logical model summarizing the regulatory
network of the mitogen-activated protein kinase (MAPK) pathway surrounding BRAF, with factors
involved in the BRAF inhibition resistance mechanisms. The relevance of this model is verified by
automatically assessing that it qualitatively reproduces response or resistance behaviors identified
in the literature. Data from over 100 melanoma and colorectal cancer cell lines are then used to
validate the model’s ability to explain differences in sensitivity. This generic model is transformed
into personalized cell line-specific logical models by integrating the omics information of the cell
lines as constraints of the model. The use of mutations alone allows personalized models to
correlate significantly with experimental sensitivities to BRAF inhibition, both from drug and
CRISPR targeting, and even better with the joint use of mutations and RNA, supporting
multi-omics mechanistic models. A comparison of these untrained models with learning approaches
highlights similarities in interpretation and complementarity depending on the size of the datasets.



