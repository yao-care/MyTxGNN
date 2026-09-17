---
layout: default
title: Propylene Glycol
parent: Low Evidence (L4-L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Propylene Glycol
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

Using the report template above directly (this is a fully-specified content-generation task, not a coding task, so no additional skill applies) — drafting the evaluation report from the evidence pack.

# Propylene Glycol: From Pharmaceutical Excipient to Bronchitis

## One-Sentence Summary

Propylene glycol (PG) is a pharmaceutical excipient/solvent with no independently registered therapeutic indication and no documented mechanism of action. The TxGNN model's top prediction is **Bronchitis**, but the **4 clinical trials** and **3 publications** retrieved for this pairing all involve other active substances (cyclosporine inhalation solution, e-cigarette liquid constituents) in which PG appears only as a formulation vehicle — none provide direct evidence of PG's therapeutic efficacy in bronchitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — PG has no independently registered therapeutic indication (used as a pharmaceutical excipient/solvent); no approved-indication text or original indication data was returned by any source |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 (per evidence-pack scoring; underlying trials/literature are indirect — none study PG as the active agent) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for propylene glycol is not available. PG is a small-molecule diol used almost exclusively as a pharmaceutical excipient, solvent, and humectant — it does not have an independently proven therapeutic indication, which is why no original indication could be extracted from the regulatory record.

Because PG lacks a known pharmacodynamic mechanism, the biological rationale linking it to bronchitis is weak. The four retrieved clinical trials all evaluate **Cyclosporine Inhalation Solution (CIS)** for bronchiolitis obliterans following lung/stem-cell transplant — PG may appear only as an inhalation-formulation vehicle, not as the tested active ingredient. Similarly, the retrieved literature examines e-cigarette liquid constituents (PG is a common e-liquid base) and their association with chronic bronchitis/COPD from a toxicological/irritant perspective, not a therapeutic one — if anything, this literature points toward airway irritation rather than a treatment effect.

Taken together, the high TxGNN score most likely reflects a structural artifact in the knowledge graph — PG co-occurring with respiratory-disease nodes because it is a common inhalation-formulation excipient — rather than a genuine pharmacological signal for treating bronchitis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Completed | 25 | Cyclosporine Inhalation Solution (CIS) for bronchiolitis obliterans syndrome post lung/HSC transplant; PG is a possible formulation excipient, not the tested agent |
| [NCT00938236](https://clinicaltrials.gov/study/NCT00938236) | Phase 3 | Terminated | 17 | Long-term extension of inhaled cyclosporine for chronic rejection prevention post lung transplant; trial terminated |
| [NCT00755781](https://clinicaltrials.gov/study/NCT00755781) | Phase 3 | Completed | 284 | Randomized controlled study of CIS for improving BOS-free survival after lung transplant; PG not the active study drug |
| [NCT01273207](https://clinicaltrials.gov/study/NCT01273207) | Phase 2 | Completed | 7 | Extended-access CIS study for bronchiolitis obliterans; small sample, PG unrelated to treatment mechanism |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | Reviews chronic e-cigarette use (PG-containing e-liquids) and potential lung disease risk, including chronic bronchitis |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | E-cigarette constituents (including PG) as airway irritants potentially worsening pre-existing respiratory disease |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | Preclinical (animal model) | Respiratory Research | Quercetin, not PG, reduces lung inflammation in an elastase/LPS COPD mouse model; unrelated to PG's mechanism |

## Malaysia Market Information

Propylene glycol has 3 active market authorizations in Malaysia, but authorization number, product name, dosage form, and approved indication text were not returned by the regulatory data source for any of the 3 records, so a detailed authorization table cannot be produced at this time.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The clinical trials and literature retrieved for the top-ranked prediction (bronchitis) do not directly evidence PG's efficacy — they involve other active agents (cyclosporine) or examine PG only as an incidental e-liquid/irritant component. Combined with the absence of a known mechanism of action, the evidence does not support advancing this candidate.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings and contraindications) — currently a blocking data gap (DG001)
- DrugBank mechanism-of-action data for propylene glycol (DG002)
- Complete Malaysia licence details (authorization number, product name, dosage form, approved indication text) for the 3 registered products
- Direct pharmacological or clinical evidence isolating PG's effect from formulation/vehicle roles
- Note: among the 10 TxGNN-predicted indications in this evidence pack, rank 3 ("diabetic retinopathy") carries a comparatively stronger evidence tier (L3, decision stage S1, "Research Question") and may warrant separate evaluation, though it also lacks direct PG-specific clinical evidence.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

