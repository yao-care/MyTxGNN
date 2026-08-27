---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Cilastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cilastatin: From Severe Bacterial Infections (as Imipenem/Cilastatin) to Bacterial Arthritis

## One-Sentence Summary

Cilastatin is a dehydropeptidase-I (DHP-1) inhibitor co-formulated with imipenem to protect it from renal degradation; it has no independent antibacterial activity of its own. The TxGNN model predicts a top-ranked association with **Bacterial Arthritis**, but the supporting **17 publications** (no clinical trials) are almost entirely studies of the *imipenem/cilastatin combination* treating bone/joint infections — the efficacy signal is attributable to imipenem, not cilastatin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no NPRA license indication text captured); cilastatin is known to be marketed only as a fixed-dose combination with imipenem for severe bacterial infections |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for cilastatin is not available in the evidence pack. Based on known pharmacology, cilastatin is a renal dehydropeptidase-I (DHP-1) inhibitor whose sole clinical role is to prevent renal metabolism of imipenem, thereby maintaining adequate imipenem concentrations. Cilastatin itself has **no independent antibacterial activity** — it is never used as a standalone antibacterial agent.

The literature supporting the "bacterial arthritis" prediction consists of case series, cohort studies, and case reports of the imipenem/cilastatin *combination* treating osteomyelitis and septic/suppurative arthritis (e.g., PMID 3544811, 3904406, 3464787). While these confirm that imipenem/cilastatin is an effective regimen for bone and joint infections, the therapeutic effect should be attributed to imipenem's broad-spectrum beta-lactam activity, not to cilastatin. The same pattern repeats across all 10 TxGNN-predicted indications in this evidence pack (MRSA infection, pneumonia, sinusitis, bronchitis, etc.) — the model appears to be picking up on the fixed-dose combination's established antibacterial uses rather than identifying a genuinely novel mechanism-based repurposing signal for cilastatin.

For this reason, the mechanistic rationale for treating cilastatin as an independently repurposable drug for bacterial arthritis is weak, despite the high TxGNN prediction score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cilastatin + bacterial arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3544811](https://pubmed.ncbi.nlm.nih.gov/3544811/) | 1987 | Cohort | Am J Dis Child | 25 infants/children with acute osteomyelitis and/or suppurative arthritis treated with imipenem/cilastatin; needle aspiration/surgical drainage performed in a subset |
| [3904406](https://pubmed.ncbi.nlm.nih.gov/3904406/) | 1985 | Cohort | Am J Dis Child | 40 hospitalized children with proved/suspected bacterial infection (including bone/joint) treated with imipenem/cilastatin; efficacy and toxicity assessed |
| [3464787](https://pubmed.ncbi.nlm.nih.gov/3464787/) | 1986 | Case series | Jpn J Antibiot | 30 cases of bone and joint infection treated with imipenem/cilastatin sodium; overall cure rate 87% (96% acute, 50% chronic) |
| [7843815](https://pubmed.ncbi.nlm.nih.gov/7843815/) | 1994 | Case report | Infection | Hip septic arthritis due to *Bacteroides fragilis* in an alcoholic patient; recovery after imipenem/cilastatin + metronidazole plus surgical debridement |
| [16718934](https://pubmed.ncbi.nlm.nih.gov/16718934/) | 2006 | Case report | Scand J Infect Dis | Spondylodiscitis after facet joint steroid injection (*Pseudomonas aeruginosa*), treated with amikacin plus imipenem/cilastatin |
| [27826114](https://pubmed.ncbi.nlm.nih.gov/27826114/) | 2017 | Case report | Int J Infect Dis | Disseminated *Nocardia elegans* infection in a rheumatoid arthritis patient, switched to imipenem/cilastatin plus minocycline |
| [15335193](https://pubmed.ncbi.nlm.nih.gov/15335193/) | 2004 | Case report | Intern Med (Tokyo) | Pyothorax caused by *Nocardia otitidiscaviarum* in a rheumatoid vasculitis patient; poor initial response to IV imipenem/cilastatin |
| [26020393](https://pubmed.ncbi.nlm.nih.gov/26020393/) | 2015 | Case report/Review | Medicine | Disseminated *Mycobacterium abscessus* infection following septic arthritis; review of clinical characteristics, treatment, and prognosis |
| [37718611](https://pubmed.ncbi.nlm.nih.gov/37718611/) | 2023 | Case report/Review | Mod Rheumatol Case Rep | Disseminated *M. abscessus* complex with osteoarticular manifestations mimicking inflammatory arthritis in an immunocompromised patient |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Review of off-label vs. formally recommended antibiotics (including carbapenems) for MDR/XDR bacterial infections |

---

## Malaysia Market Information

The evidence pack confirms **5 NPRA registrations** for cilastatin-containing products (market status: Marketed), but the license number, product name, dosage form, and approved indication text fields were not populated in the source data, so a detailed authorization table cannot be produced here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 10 TxGNN-predicted indications in this evidence pack — including the top-ranked "bacterial arthritis" — are supported only by literature/trials describing the imipenem/cilastatin **combination**, not cilastatin acting independently; cilastatin has no antibacterial mechanism of its own, so the repurposing signal is not mechanistically attributable to this drug. No completed RCTs isolate cilastatin's contribution to any new indication.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings and contraindications (currently a blocking data gap)
- DrugBank-confirmed mechanism of action (currently a high-severity data gap)
- Complete NPRA license details (product name, dosage form, approved indication text) for the 5 existing registrations
- If pursuing this candidate further, a pharmacological assessment of whether cilastatin has *any* activity independent of DHP-1 inhibition, since current evidence cannot separate its contribution from imipenem's
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

