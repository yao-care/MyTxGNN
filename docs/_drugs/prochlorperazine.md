---
layout: default
title: Prochlorperazine
parent: High Evidence (L1-L2)
nav_order: 575
evidence_level: L2
indication_count: 10
---

# Prochlorperazine
{: .fs-9 }

Tahap bukti: **L2** | Indikasi diramal: **10** 
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

# Prochlorperazine: From Antiemetic Use to Schizophrenia

## One-Sentence Summary

> Prochlorperazine is a phenothiazine-class drug historically used as an antiemetic (nausea/vomiting) and antipsychotic agent. The TxGNN model predicts it may be effective for **Schizophrenia**, with **1 clinical trial** (low direct relevance) and **18 publications** — mostly historical studies from the 1950s–1970s — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from NPRA license text in this evidence pack (all `approved_indication_text` fields are blank); literature background describes prochlorperazine as "usually used to treat nausea, vomiting and schizophrenia" (PMID 29442053) |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 99.9992% (rank 43) |
| Evidence Level | L2 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA) is not available for prochlorperazine in this evidence pack. Based on known pharmacology, prochlorperazine is a **phenothiazine-class** drug, sharing its chemical family with chlorpromazine, butaperazine, and other classic antipsychotics. Phenothiazines act primarily as central **dopamine D2 receptor antagonists**, which is the pharmacological basis of antipsychotic activity. One mechanistic study in this evidence pack (PMID 23954492) further shows that prochlorperazine acts as a potent allosteric modulator of the human P2X7 receptor, a channel implicated in cytokine regulation and the pathophysiology of schizophrenia.

Notably, several older publications in the evidence pack (e.g., PMID 13785665, 1961; PMID 4396306, 1970; PMID 14278880, 1965; PMID 13878438, 1962) describe prochlorperazine already being used and comparatively tested for schizophrenia decades ago. This means the TxGNN "prediction" here largely reconfirms a historically documented use rather than identifying an entirely novel indication — the evidence gap is less about biological plausibility and more about the lack of modern, well-designed trials.

Given the direct mechanistic link (D2 antagonism → antipsychotic effect) and the historical clinical precedent, the prediction is mechanistically reasonable, but the supporting evidence is dated and of limited methodological rigor by current standards.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02600741](https://clinicaltrials.gov/study/NCT02600741) | N/A | Completed | 296 | Evaluated caregiver psycho-education and skills training for patients with schizophrenia, schizoaffective, or schizophreniform disorder receiving paliperidone palmitate or oral antipsychotics. Does not directly test prochlorperazine efficacy — graded **low relevance (C)** by evidence review. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13785665](https://pubmed.ncbi.nlm.nih.gov/13785665/) | 1961 | RCT | The Journal of Mental Science | Double-blind trial comparing chlorpromazine, prochlorperazine (Compazine), and trifluoperazine in paranoid schizophrenia. |
| [4396306](https://pubmed.ncbi.nlm.nih.gov/4396306/) | 1970 | RCT | L'union médicale du Canada | Comparative study of butaperazine vs. prochlorperazine in acute-phase schizophrenia. |
| [14278880](https://pubmed.ncbi.nlm.nih.gov/14278880/) | 1965 | RCT | Canadian Psychiatric Association Journal | Comparative study of butaperazine vs. prochlorperazine in chronic schizophrenia. |
| [13878438](https://pubmed.ncbi.nlm.nih.gov/13878438/) | 1962 | Clinical study | Journal of the Indian Medical Association | Reports on treatment of chronic schizophrenia with prochlorperazine. |
| [13868819](https://pubmed.ncbi.nlm.nih.gov/13868819/) | 1962 | Cohort | Journal of the Indian Medical Association | Clinical observation of prochlorperazine use in chronic schizophrenia. |
| [13664779](https://pubmed.ncbi.nlm.nih.gov/13664779/) | 1959 | Case report | Journal of Clinical and Experimental Psychopathology | Describes a synergistic effect of prochlorperazine and mepazine in two schizophrenia cases. |
| [23954492](https://pubmed.ncbi.nlm.nih.gov/23954492/) | 2013 | Mechanistic | Neuropharmacology | Identifies prochlorperazine as a potent allosteric modulator of the human P2X7 receptor, linked to schizophrenia pathophysiology. |
| [36165981](https://pubmed.ncbi.nlm.nih.gov/36165981/) | 2023 | Review | Journal of Applied Toxicology | Systematic review of phenothiazine derivatives' effects on autophagy, relevant to neuronal mechanisms in schizophrenia. |
| [30159761](https://pubmed.ncbi.nlm.nih.gov/30159761/) | 2018 | In vitro | Daru (Tehran Univ. Medical Sciences) | Notes prochlorperazine is "widely used to treat schizophrenia"; studies its effect on melanocyte viability/melanogenesis (off-target). |
| [29442053](https://pubmed.ncbi.nlm.nih.gov/29442053/) | 2017 | In vitro | Die Pharmazie | Background confirms prochlorperazine's clinical use for nausea, vomiting, and schizophrenia; studies its interaction with melanin (off-target). |

---

## Malaysia Market Information

Prochlorperazine holds **6 active registrations** in Malaysia (NPRA), and market status is confirmed as marketed. However, detailed license numbers, product names, dosage forms, and approved-indication text have not yet been retrieved into this evidence pack — all corresponding fields are currently blank (tracked as data gap DG001, "Blocking" severity). A formal NPRA label review is required before this information can be tabulated.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not yet available in this evidence pack — see data gap DG001.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical comparative trials and clinical observations (1959–1970) support prochlorperazine's use in schizophrenia, and its phenothiazine/D2-antagonist mechanism is directly consistent with antipsychotic activity — but this is effectively re-confirming an old, already-documented use rather than a novel repurposing signal, and the evidence base predates modern RCT standards. Critically, mandatory safety data (TFDA/NPRA label warnings and contraindications, DG001) is missing and is flagged as a **blocking** gap that prevents formal safety pre-assessment (S1).

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — required before any safety pre-assessment can begin (DG001, Blocking)
- DrugBank mechanism-of-action confirmation (DG002)
- Malaysia license details (license numbers, product names, approved indication text) currently blank in registry records
- Modern-era clinical evidence (post-1980s trials) to corroborate the historical findings, given the age and methodological limitations of the existing literature
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

