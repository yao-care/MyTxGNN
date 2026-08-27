---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 5
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Fenofibrate: From Hyperlipidemia to Hypoalphalipoproteinemia

## One-Sentence Summary

Fenofibrate is a fibrate-class PPAR-alpha agonist used for hyperlipidemia and hypertriglyceridemia (mixed dyslipidemia).
The TxGNN model predicts it may also be effective for **Hypoalphalipoproteinemia** (abnormally low HDL cholesterol),
with **1 clinical trial** and **11 publications** currently touching on this specific direction — evidence that is preliminary and mechanistically contested.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia / Hypertriglyceridemia (dyslipidemia) — specific NPRA-approved indication text not available in this evidence pack |
| Predicted New Indication | Hypoalphalipoproteinemia |
| TxGNN Prediction Score | 0.00% (as recorded in evidence pack) |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, fenofibrate belongs to the fibrate class and acts as a PPAR-alpha agonist — it activates lipoprotein lipase (LPL), lowers ApoC-III, reduces hepatic VLDL/triglyceride synthesis, and has been reported to raise ApoA-I expression and promote reverse cholesterol transport. This core mechanism is the basis for its established efficacy in hyperlipidemia and hypertriglyceridemia.

Hypoalphalipoproteinemia is defined by pathologically low HDL cholesterol, so in theory a drug that upregulates ApoA-I and reverse cholesterol transport could raise HDL levels in this population. However, the evidence pack's own rationale flags an important caveat: most hypoalphalipoproteinemia is caused by genetic defects (e.g., LCAT deficiency, ApoA-I mutations) that are not addressed by fenofibrate's mechanism, and multiple sources in the literature set (e.g., PMID 7567762, PMID 26667175) describe fenofibrate/fibrate combinations *causing* iatrogenic HDL reduction rather than correcting it. The mechanistic direction is therefore ambiguous and requires careful interpretation rather than straightforward extrapolation from the original indication.

It is also worth noting that three of the other four predicted indications in this evidence pack — familial hyperlipidemia, hypertriglyceridemia, and hyperlipidemia — substantially overlap with fenofibrate's already-established core indications rather than representing genuinely novel repurposing opportunities; the evidence pack's own rationale text for hypertriglyceridemia explicitly notes this ("already an approved indication, not strictly repurposing"). A fifth candidate, "obsolete familial combined hyperlipidemia," has no supporting trial or literature data and is flagged as a likely duplicate/obsolete disease-mapping artifact.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00458055](https://clinicaltrials.gov/study/NCT00458055) | NA | Completed | 19 | Treatment study for severe HDL deficiency; examines reverse cholesterol transport in a small, non-randomized, directly relevant population, but without a comparator arm. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26667175](https://pubmed.ncbi.nlm.nih.gov/26667175/) | 2016 | Mechanistic/Biomarker | Molecular & Cellular Proteomics | Identifies PON1 and ApoC proteins as risk factors for hypoalphalipoproteinemia in diabetic patients on fenofibrate + rosiglitazone — describes a paradoxical HDL/ApoA-I reduction as a treatment complication. |
| [23557750](https://pubmed.ncbi.nlm.nih.gov/23557750/) | 2013 | Case-Control/Mechanistic | J Am Heart Assoc | Links low-HDL phenotype to enhanced lipid peroxidation and platelet activation, supporting the biological rationale for HDL-targeted intervention. |
| [19230892](https://pubmed.ncbi.nlm.nih.gov/19230892/) | 2009 | Cohort | Atherosclerosis | Fenofibrate (with nicotinic acid) used in familial LCAT deficiency; reports lipoprotein and renal changes after 6 weeks — a genetic hypoalphalipoproteinemia subtype. |
| [24362356](https://pubmed.ncbi.nlm.nih.gov/24362356/) | 2014 | Review | Current Opinion in Lipidology | Reviews reverse cholesterol transport flux methodology relevant to HDL-raising mechanisms. |
| [21107758](https://pubmed.ncbi.nlm.nih.gov/21107758/) | 2011 | Expert Opinion/Review | Current Atherosclerosis Reports | Discusses combination lipid therapy, noting isolated hypoalphalipoproteinemia as an exception to statin-first treatment algorithms. |
| [23415437](https://pubmed.ncbi.nlm.nih.gov/23415437/) | 2013 | Case Report/Review | J Clin Lipidology | Describes a patient with marked HDL deficiency on a regimen including fenofibrate 145 mg/day; reviews genetic HDL-deficiency literature. |
| [30201532](https://pubmed.ncbi.nlm.nih.gov/30201532/) | 2018 | Case Report | J Clin Lipidology | LCAT-deficient patient case; not fenofibrate-specific but relevant to the target disease's natural history. |
| [10349128](https://pubmed.ncbi.nlm.nih.gov/10349128/) | 1999 | Review | Medicina | Describes partial LCAT deficiency syndrome, a genetic cause of hypoalphalipoproteinemia. |
| [23023895](https://pubmed.ncbi.nlm.nih.gov/23023895/) | 2012 | Review | Singapore Med J | General review on low-HDL management strategies beyond LDL-lowering. |
| [7567762](https://pubmed.ncbi.nlm.nih.gov/7567762/) | 1995 | Case Report | Postgrad Med J | Reports iatrogenic profound hypoalphalipoproteinemia from probucol + fibrate combination — evidence of a mechanism working in the *opposite* direction. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial directly studying this population is a small (n=19), non-randomized, single-arm study, and none of the 10 supporting publications are RCTs — evidence level is L3 with the decision at an early "Research Question" stage. More importantly, the mechanistic case is internally contradictory: several of the retrieved sources describe fenofibrate (alone or in combination) *causing* iatrogenic HDL reduction rather than correcting it, and most hypoalphalipoproteinemia is driven by genetic defects (LCAT deficiency, ApoA-I mutations) that fenofibrate's PPAR-alpha mechanism does not directly address.

**To proceed, the following is needed:**
- Malaysia/NPRA package insert data — warnings, contraindications, and DDI (currently a Blocking data gap)
- Verified mechanism of action from DrugBank (currently a High-severity data gap)
- Confirmed original approved indication text (all 13 Malaysia license records currently have blank indication fields)
- A controlled study in a defined, non-iatrogenic hypoalphalipoproteinemia population to resolve the conflicting directionality seen in the literature
- Clarification of whether "obsolete familial combined hyperlipidemia" (rank 3, no evidence) is a disease-mapping duplicate before it is carried forward as a separate candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

