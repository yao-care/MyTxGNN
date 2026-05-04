---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: From Bacterial Infections to Monoclonal Gammopathy

## One-Sentence Summary

Amoxicillin is a broad-spectrum aminopenicillin antibiotic widely used for treating bacterial infections of the respiratory, urinary, and gastrointestinal tracts, including *Helicobacter pylori* eradication regimens.
The TxGNN model predicts it may be effective for **Monoclonal Gammopathy** — most specifically Immunoproliferative Small Intestinal Disease (IPSID), where antibiotic eradication of the bacterial antigenic driver produces disease remission.
This direction is supported by **1 clinical trial** and **11 publications**, with the most compelling biological rationale concentrated in IPSID case series.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory, urinary, gastrointestinal tract; *H. pylori* eradication) |
| Predicted New Indication | Monoclonal Gammopathy — specifically IPSID (Alpha-chain disease / Mediterranean lymphoma) |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 100 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved in this Evidence Pack. Based on established pharmacological knowledge, amoxicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by binding irreversibly to penicillin-binding proteins (PBPs), preventing peptidoglycan cross-linking and causing bactericidal activity against a broad range of gram-positive and gram-negative organisms. This mechanism is the essential foundation for its potential role in antigen-driven lymphoproliferative disease.

The biological bridge to monoclonal gammopathy centres on a specific subtype: **Immunoproliferative Small Intestinal Disease (IPSID)**, also known as Alpha-chain disease or Mediterranean lymphoma. In IPSID, persistent intestinal bacterial infection — particularly *Campylobacter jejuni* and related gram-negative organisms — drives abnormal clonal proliferation of IgA α-heavy-chain-secreting B cells, generating a detectable monoclonal immunoglobulin. When this bacterial antigenic driver is eradicated with antibiotics (tetracycline, amoxicillin ± metronidazole), early-stage disease (Stage A) can achieve durable complete remission without chemotherapy.

This mechanism closely parallels the well-validated *H. pylori* eradication model for gastric MALT lymphoma, and multiple published case series have documented full or partial regression of IPSID following antibiotic therapy alone (PMID 9030995, 8988128, 20300878), making this one of the few repurposing opportunities in this class that is already partially clinically validated. **Critical caveat**: this biological rationale applies exclusively to early-stage IPSID and does **not** extend to MGUS, multiple myeloma, Waldenström's macroglobulinemia, or other monoclonal gammopathies, where amoxicillin has no established mechanistic role.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | N/A | Terminated | 351 | Prospective double-blind RCT comparing moxifloxacin monotherapy vs. ciprofloxacin + amoxicillin/clavulanate as oral empirical therapy for febrile neutropenia in low-risk cancer patients; terminated early without a definitive conclusion. Amoxicillin used as part of the comparator combination — not as a treatment for monoclonal gammopathy directly. |

> **Note**: No clinical trials specifically investigating amoxicillin for IPSID or monoclonal gammopathy are currently registered. The trial above (Relevance Grade C) provides only contextual background on amoxicillin use in a haematology-oncology setting.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1997 | Case Series | *Lancet* | Mediterranean lymphoma (IPSID) treated with antibiotics alone; documents complete regression of monoclonal B-cell disease after eradication therapy, establishing the antibiotic-treatment paradigm for early-stage IPSID |
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Series | *Lancet* | Regression of immunoproliferative small intestinal disease following *H. pylori* eradication; directly supports the infection-driven clonal B-cell proliferation model |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Series | *J Gastrointest Cancer* | 20-year-old male with alpha-heavy-chain IPSID achieved complete clinical and endoscopic regression following *H. pylori* eradication antibiotic therapy, with resolution of mesenteric lymphadenopathy on CT |
| [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) | 2005 | Case Report | *Arch Pathol Lab Med* | Non-secretory IPSID variant (extranodal marginal zone B-cell lymphoma) of the distal small bowel; highlights diagnostic spectrum and histopathological subtypes relevant to defining antibiotic-responsive candidates |
| [21908119](https://pubmed.ncbi.nlm.nih.gov/21908119/) | 2011 | Case Report | *Med Mal Infect* | *Rothia dentocariosa* pneumonia in an immunocompromised patient with plasma cell dyscrasia; amoxicillin used for infectious complication management in a monoclonal gammopathy context |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case Report | *Front Public Health* | Disseminated nocardiosis caused by *Nocardia vulneris* in a patient with macroglobulinemia; amoxicillin/clavulanate identified as one of the susceptible antibiotic options |
| [22092390](https://pubmed.ncbi.nlm.nih.gov/22092390/) | 2012 | Retrospective Comparative Study | *J Oral Pathol Med* | Comparative analysis of bisphosphonate-related ONJ in multiple myeloma vs. breast cancer; amoxicillin used as supportive antibiotic in standardised wound care protocol |
| [20015614](https://pubmed.ncbi.nlm.nih.gov/20015614/) | 2010 | Case Series | *Int J Oral Maxillofac Surg* | Surgical management of bisphosphonate-induced ONJ in myeloma patients unresponsive to conservative therapy; amoxicillin used as prophylactic/supportive antibiotic |
| [20513124](https://pubmed.ncbi.nlm.nih.gov/20513124/) | 2010 | Diagnostic Accuracy Study | *Am J Hematol* | High false-positive rate of Aspergillus galactomannan test in multiple myeloma patients; amoxicillin/clavulanate implicated as a cause of assay interference — clinically relevant for infection monitoring in this population |
| [18639371](https://pubmed.ncbi.nlm.nih.gov/18639371/) | 2009 | Retrospective Study | *Br J Oral Maxillofac Surg* | Bisphosphonate-associated ONJ in myeloma: therapy discontinuation does not alter clinical course and may allow recurrence of bone pain and osteolytic progression |

> **Evidence Assessment**: The three IPSID/Mediterranean lymphoma papers (PMID 9030995, 8988128, 20300878) provide the most directly relevant and mechanistically compelling evidence. The remaining publications reflect amoxicillin use in secondary infection management or supportive care within haematological malignancy contexts, and do not constitute primary repurposing evidence.

---

## Malaysia Market Information

Amoxicillin is confirmed as marketed in Malaysia with 100 registered products. However, individual product registration details — including authorization numbers, product names, dosage forms, and approved indications — were not returned in this Evidence Pack.

> **Action Required**: Retrieve full product listing from the Malaysia NPRA e-Search portal to confirm available formulations (oral, injectable, suspension), dosing strengths, and currently approved indications before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings and contraindications data were not available in this Evidence Pack and should be retrieved directly from the NPRA-approved product labelling.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amoxicillin has a biologically plausible, partially validated mechanism for treating early-stage IPSID (Stage A) through eradication of the bacterial antigenic driver sustaining clonal B-cell proliferation — a paradigm directly analogous to *H. pylori* eradication for gastric MALT lymphoma, supported by published case series demonstrating durable disease regression. The scope is deliberately narrow: this recommendation applies to **IPSID only** and must not be extrapolated to other monoclonal gammopathies.

**To proceed, the following is needed:**
- Retrieve MOA data from DrugBank API (DB01060) to formally document the mechanistic basis and confirm absence of direct anti-lymphoproliferative activity
- Retrieve NPRA product label PDF to extract full warnings, contraindications, and currently approved indications for Malaysia-specific labelling
- Define strict patient selection criteria: **early-stage IPSID (Stage A only)** — explicitly excluding MGUS, multiple myeloma, and Waldenström's macroglobulinemia from any expanded use proposal
- Commission a focused systematic review of IPSID antibiotic therapy outcomes (amoxicillin vs. tetracycline vs. amoxicillin + metronidazole) to characterise the optimal regimen, dosing duration, and remission rates
- Investigate regional epidemiology: IPSID / Mediterranean lymphoma has higher reported prevalence in Middle Eastern and some Southeast Asian populations, which may increase clinical relevance in the Malaysian context
- Clarify TxGNN false-positive rate for the higher-ranked predictions (Ranks 1–5, all L5/Hold), as these appear to reflect knowledge-graph noise rather than genuine repurposing candidates, and refine the prediction pipeline accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

