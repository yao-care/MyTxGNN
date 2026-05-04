---
layout: default
title: Arginine
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Arginine: From Nutritional Amino Acid to Gastroparesis

## One-Sentence Summary

L-Arginine is a semi-essential amino acid widely used as a nutritional supplement and in metabolic support therapies, including urea cycle disorder management. The TxGNN model predicts it may be effective for **Gastroparesis**, with **1 registered clinical trial** (indirect relevance only) and **10 preclinical publications** currently supporting this direction. Overall, the mechanistic rationale is scientifically compelling, but human clinical evidence remains absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional supplementation; amino acid/metabolic support (regulatory label data unavailable) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 138 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

L-Arginine is the obligate endogenous substrate for all three isoforms of nitric oxide synthase (NOS). In the gastrointestinal tract, the neuronal isoform (nNOS) resides in the inhibitory motor neurons of the myenteric plexus and uses L-Arginine to synthesise nitric oxide (NO). This NO signal drives two critical motor events that are disrupted in gastroparesis: pyloric sphincter relaxation and fundic (gastric accommodation) relaxation. When either L-Arginine availability or nNOS activity is reduced, gastric outflow is impaired — the defining pathophysiology of gastroparesis.

Direct preclinical support for this mechanism was provided by Reichardt et al. (PMID: 25057793), who demonstrated that glucocorticoid-induced gastroparesis in mice is mechanistically mediated by tissue depletion of L-Arginine; replenishing L-Arginine restored NO production and normalised gastric emptying. A parallel line of evidence from Welsh et al. (PMID: 23639814) showed that tetrahydrobiopterin (BH4) deficiency — which incapacitates NOS without touching its substrate — also causes gastroparesis in newborn mice, pointing to the Arginine → NOS → NO axis as a shared bottleneck across multiple gastroparesis aetiologies.

Although L-Arginine itself has no formally approved gastric motility indication, its role as the rate-limiting substrate for nitrergic neurotransmission in the gut places it at the mechanistic centre of gastroparesis pathology. The TxGNN knowledge-graph model appears to have captured this Arginine–NO–gastroparesis axis through its network topology, producing a high prediction score of 99.42%. The prediction is biologically coherent, even though human clinical validation is still required.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Unknown | 150 | Observational study of autologous pancreatic islet cell transplantation after pancreatectomy for glycaemic control. Arginine stimulation test is used as an islet function assessment tool; gastroparesis is not a primary or secondary endpoint. Relevance to Arginine treatment of gastroparesis is indirect (Grade C). |

> **Note:** No clinical trials directly testing L-Arginine supplementation as a treatment for gastroparesis are currently registered. The single trial identified above uses an arginine stimulation test as a functional assay, not as a therapeutic intervention.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Animal Study | *Endocrinology* | Dexamethasone induced gastroparesis in mice through depletion of tissue L-Arginine; effect was abolished in GR(dim) mutant mice. Directly demonstrates the Arginine–NO–gastroparesis mechanistic link. |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | BH4 deficiency (NOS cofactor) caused gastroparesis in newborn mice. Converges on the Arginine → NOS → NO axis as the critical pathway for pyloric relaxation. |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | 6-OHDA Parkinson's disease rat model exhibited impaired nitrergic relaxation of the pyloric sphincter, with altered nNOS expression causing delayed gastric emptying. Supports nitrergic pathway as a target. |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Animal Study | *Neurogastroenterol Motil* | Diabetic BB-rats showed decreased nNOS expression and impaired inhibitory neurotransmission in the jejunum, identifying nNOS downregulation as a mechanism of diabetic gastroparesis. |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Animal Study | *World J Gastroenterol* | Ghrelin and GHRP-6 improved gastric motility in diabetic mice with gastroparesis, providing therapeutic context for gastric motility modulation. |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | Synchronized gastric electrical stimulation improved impaired gastric accommodation via the nitrergic pathway in dogs; further implicates the NO system in gastric relaxation. |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | Hyperglycaemia-induced inhibition of gastric motility was mediated by vagal nodose ganglia K(ATP) channels; provides mechanistic context for diabetic gastroparesis. |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Animal Study | *Am J Physiol Gastrointest Liver Physiol* | Sacral nerve stimulation improved impaired gastric accommodation in rats via spinal afferent and vagal efferent pathways. Demonstrates modifiability of NO-mediated gastric accommodation. |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case Report | *Am J Case Rep* | MELAS patient (m.3243A>G) with gastroparesis; lifestyle changes normalised lactate. L-Arginine is a known adjunct therapy in MELAS, providing a real-world human precedent for Arginine use in a gastroparesis-associated mitochondrial condition. |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Animal Study | *Gastroenterology* | Antigen challenge in sensitised rats caused delayed gastric emptying; mechanism (gastroparesis vs. prolonged trituration) and mediators under investigation. Background context for gastroparesis pathophysiology. |

---

## Malaysia Market Information

> Detailed product-level registration data (product name, dosage form, approved indication) is not available in the current dataset. The NPRA query confirmed **138 active registrations** for Arginine-containing products in Malaysia as of 2026-03-27. Full registration details can be retrieved from the [NPRA product search portal](https://www.npra.gov.my/).

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were identified in the current query (DDI query status: not found). Formal warnings and contraindications data require retrieval from the NPRA package insert PDF (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence is preclinical (animal studies, Tier 3); no human clinical trials have directly evaluated L-Arginine supplementation as a treatment for gastroparesis. Despite a high TxGNN prediction score and a well-defined mechanistic pathway (Arginine → nNOS → NO → pyloric/fundic relaxation), the absence of Phase 1/2 human data prevents advancement beyond a research question at this stage.

**To proceed, the following is needed:**

- **Human pharmacodynamic proof-of-concept study**: A small-scale pilot trial measuring gastric emptying time (e.g., scintigraphy or breath test) before and after oral/IV L-Arginine supplementation in gastroparesis patients.
- **Optimal dose and route characterisation**: Identify the dose required to meaningfully restore gastric mucosal and myenteric NO levels in humans (oral vs. IV; acute vs. chronic supplementation).
- **Safety and contraindication review**: Retrieve and parse NPRA/manufacturer package insert to identify relevant warnings (Data Gap DG001), particularly for patients with renal impairment, sepsis, or herpes simplex infection where Arginine use may be restricted.
- **MOA documentation**: Formal DrugBank API query to complete Arginine's mechanism of action record (Data Gap DG002).
- **NPRA license detail extraction**: Retrieve the 138 Malaysian product registrations to confirm available dosage forms and any existing approved indications that could inform labelling strategy.
- **Subgroup hypothesis**: Define whether the primary target population is diabetic gastroparesis, post-surgical gastroparesis, or idiopathic gastroparesis, as the mechanistic evidence (PMID: 25057793; 18312542) is strongest in glucocorticoid- and diabetes-associated subtypes.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

