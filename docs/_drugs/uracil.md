---
layout: default
title: Uracil
parent: High Evidence (L1-L2)
nav_order: 677
evidence_level: L1
indication_count: 10
---

# Uracil
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
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

# Uracil: From Fluoropyrimidine-Based Chemotherapy Adjuvant to Colonic Neoplasm

## One-Sentence Summary

Uracil has no independent antitumour activity of its own — it is the DPD-inhibiting partner drug in the tegafur-uracil (UFT) combination, used to boost the efficacy of 5-fluorouracil (5-FU) chemotherapy. The TxGNN model flags **Colonic Neoplasm** as its top predicted indication (score 99.50%), and this is strongly supported by **3 completed Phase 3 RCTs** and **10 relevant publications** — though the evidence largely confirms an already-established, well-characterized mechanism rather than a genuinely novel hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not yet extractable — all 5 NPRA licence records in the current data pull have blank indication-text fields; based on known pharmacology, uracil is used as the DPD-inhibitor component of UFT (tegafur-uracil) combination chemotherapy |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data for uracil is currently a data gap (DG002). Based on the pharmacology evident in the collected trial and literature evidence, however, uracil's role is well characterized: it is combined with tegafur (a 5-FU prodrug) in a fixed ratio to form UFT. Uracil competitively inhibits dihydropyrimidine dehydrogenase (DPD), the enzyme responsible for degrading 5-FU, thereby raising and sustaining intratumoral 5-FU concentrations and enhancing cytotoxic effect.

Given that 5-FU-based chemotherapy (with or without DPD-inhibiting enhancers such as uracil) is a backbone treatment for colorectal cancer, the TxGNN prediction that uracil is relevant to "colonic neoplasm" is mechanistically unsurprising. Multiple Phase 3 trials in the evidence pack (e.g., ACTS-CC 02, NSABP C-06) directly compare UFT/leucovorin regimens against other fluoropyrimidine regimens in colon cancer, indicating this link reflects confirmation of an established, guideline-relevant use rather than a novel repurposing hypothesis.

By contrast, the model's lower-ranked candidates (rectosigmoid junction neoplasm, lipoma of colon, colonic lymphangioma, cecum villous adenoma, cecum neuroendocrine tumor G1, cavernous hemangioma of colon, colon leiomyoma) have little to no supporting evidence and largely reflect anatomical proximity in the knowledge graph rather than genuine pharmacological relevance — these are assessed separately below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant tegafur-uracil (UFT) vs. observation in curatively resected Stage II colon cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 (tegafur-based) vs. capecitabine, first-line metastatic colorectal cancer; same fluoropyrimidine-enhancer class as UFT |
| [NCT00677443](https://clinicaltrials.gov/study/NCT00677443) | Phase 3 | Completed | 344 | SOX (S-1 + oxaliplatin) vs. COX (capecitabine + oxaliplatin) in advanced colorectal cancer |
| [NCT00749450](https://clinicaltrials.gov/study/NCT00749450) | Phase 3 | Completed | 6088 | Large adjuvant chemotherapy comparison (oxaliplatin, fluorouracil, capecitabine) after high-risk colorectal surgery |
| [NCT00002551](https://clinicaltrials.gov/study/NCT00002551) | Phase 3 | Completed | 1917 | Postoperative 5-FU regimen comparisons plus pelvic radiotherapy in rectal cancer |
| [NCT00069108](https://clinicaltrials.gov/study/NCT00069108) | Phase 3 | Completed | 627 | XELOX vs. FOLFOX4 in metastatic colorectal cancer previously treated with irinotecan/5-FU |
| [NCT01097018](https://clinicaltrials.gov/study/NCT01097018) | Phase 3 | Completed | 468 | Perifosine + capecitabine vs. placebo + capecitabine in refractory advanced colorectal cancer |
| [NCT04607421](https://clinicaltrials.gov/study/NCT04607421) | Phase 3 | Active, not recruiting | 831 | Encorafenib + cetuximab ± chemotherapy in BRAF V600E-mutant metastatic colorectal cancer (same disease area, no direct uracil/UFT link) |
| [NCT04230187](https://clinicaltrials.gov/study/NCT04230187) | Phase 3 | Recruiting | 528 | Bevacizumab + mFOLFOXIRI/mFOLFOX-6 as first-line therapy in unresectable metastatic colorectal cancer |
| [NCT00967616](https://clinicaltrials.gov/study/NCT00967616) | Phase 2 | Completed | 100 | CS-7017 + FOLFIRI in metastatic colorectal cancer after first-line failure (non-fluoropyrimidine-enhancer, low direct relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clinical Colorectal Cancer | ACTS-CC 02 Phase III trial: S-1+oxaliplatin vs. tegafur-uracil+leucovorin (UFT/LV) as adjuvant therapy in high-risk Stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 updated 5-year survival analysis, UFT/LV as comparator arm |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT/Cohort | Medicine | Nationwide Taiwan NHIRD cohort study + meta-analysis: UFT vs. 5-FU as postoperative adjuvant therapy in Stage II/III colon cancer |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP Protocol C-06: oral UFT + leucovorin vs. IV fluorouracil + leucovorin in Stage II/III colon carcinoma |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT (tegafur+uracil) as postoperative adjuvant chemotherapy for solid tumors — clinical evidence, MOA, and future directions |
| [11177740](https://pubmed.ncbi.nlm.nih.gov/11177740/) | 2001 | Review | Current Oncology Reports | Adjuvant chemotherapy for colon cancer, including oral fluoropyrimidine options |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Observational | BMC Cancer | JFMC46-1201: prospective propensity-matched study of UFT/LV for high-risk Stage II colon cancer |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Observational | International Journal of Clinical Oncology | JFMC46-1201 final analysis: updated 5-year OS and risk-factor outcomes for UFT/LV |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case Report | Cancer Chemotherapy and Pharmacology | UFT-induced haemolytic anaemia in a metastatic colon cancer patient |
| [17033240](https://pubmed.ncbi.nlm.nih.gov/17033240/) | 2006 | Case Report | Gan To Kagaku Ryoho | Two metastatic colonic cancer patients successfully treated with UFT + oral leucovorin |

---

## Malaysia Market Information

Uracil-containing products are recorded as marketed with 5 total NPRA registrations, but licence-level detail (licence number, product name, dosage form, manufacturer, approved indication text) has not yet been extracted from source records for any of the 5 entries. This is tracked as data gap DG001 (Blocking) and needs to be resolved before a full S1 safety assessment can proceed.

---

## Cytotoxicity

Uracil is classified here as antineoplastic because it functions exclusively as the DPD-inhibiting component of a known fluoropyrimidine-class cytotoxic combination (tegafur-uracil/UFT).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine-potentiator; uracil itself has no direct antitumour activity — it inhibits DPD to raise 5-FU exposure) |
| Myelosuppression Risk | Low to Moderate — review evidence (PMID 17952521) reports UFT has a comparatively mild toxicity profile versus IV 5-FU; a rare case of UFT-induced haemolytic anaemia has been reported (PMID 11320674) |
| Emetogenicity Classification | Low to Moderate (consistent with oral fluoropyrimidine class) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; watch for diarrhea, mucositis, and hand-foot syndrome typical of fluoropyrimidine regimens |
| Handling Protection | Must follow cytotoxic drug handling regulations as a component of an antineoplastic combination regimen |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (ACTS-CC 02, NSABP C-06, and related trials) support tegafur-uracil (UFT)'s established role in colon cancer adjuvant and first-line therapy, giving an L1 evidence level. However, this largely confirms an already-known mechanism (DPD inhibition potentiating 5-FU) rather than a novel therapeutic hypothesis, and critical safety/regulatory data remain incomplete.

**To proceed, the following is needed:**
- TFDA/NPRA package insert — warnings, contraindications, and DDI data (DG001, Blocking)
- Confirmed DrugBank mechanism-of-action record for uracil (DG002, High)
- Full extraction of the 5 NPRA licence records (product name, dosage form, indication text) to confirm whether colorectal cancer is already an approved indication for uracil-containing products in Malaysia, which would reframe this from "new indication" to "existing indication confirmation"
- Clarification of DPD-deficiency screening requirements given known fluoropyrimidine toxicity risk in poor metabolizers
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

