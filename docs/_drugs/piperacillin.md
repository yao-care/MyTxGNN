---
layout: default
title: Piperacillin
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 9
---

# Piperacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a broad-spectrum beta-lactam antibiotic widely used to treat serious bacterial infections caused by both gram-positive and gram-negative organisms, most commonly administered as the piperacillin/tazobactam (Pip-Tazo) combination. The TxGNN model assigns it the highest prediction score of **99.94%** for **Rheumatoid Arthritis (RA)**, yet the 18 retrieved publications contain no direct evidence for piperacillin as an RA treatment — they uniformly describe its antibiotic use for *managing infections in* RA patients, pointing to a confounding signal rather than a genuine therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (gram-positive and gram-negative pathogens) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only; no directly supportive studies exist) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Piperacillin is a penicillin-type beta-lactam antibiotic that exerts its action by covalently binding to penicillin-binding proteins (PBPs) on the bacterial cell surface, thereby inhibiting the final cross-linking step of peptidoglycan biosynthesis and causing cell wall disruption and bacterial lysis. It covers a broad range of clinically important pathogens including *Pseudomonas aeruginosa*, *Enterobacteriaceae*, and many streptococci. Detailed mechanistic data from DrugBank is not currently available for this report; however, its mechanism as a cell-wall synthesis inhibitor is well established in the pharmacological literature.

The apparent TxGNN association between piperacillin and rheumatoid arthritis almost certainly reflects a **comorbidity confounding bias** baked into the knowledge graph. RA patients on methotrexate, JAK inhibitors, or biologics such as etanercept are systemically immunocompromised and frequently develop serious bacterial infections requiring empirical broad-spectrum antibiotic cover — for which piperacillin/tazobactam is a standard first-line choice. The model appears to have interpreted this frequent "RA patient ↔ piperacillin" co-occurrence in the biomedical literature as a therapeutic signal, when in reality piperacillin is treating infectious *complications of immunosuppression*, not RA itself.

Some beta-lactam antibiotics have been reported in preclinical settings to possess modest immunomodulatory properties, including partial NF-κB pathway suppression and Toll-like receptor modulation. However, no direct mechanistic or clinical evidence exists for such effects with piperacillin in the context of autoimmune synovitis. Paradoxically, prolonged broad-spectrum antibiotic use disrupts gut microbiota homeostasis, which may worsen immune dysregulation in autoimmune conditions such as RA — making long-term use in this indication biologically counterproductive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for piperacillin in rheumatoid arthritis.

---

## Literature Evidence

The 18 publications were retrieved by combining "piperacillin" with "rheumatoid arthritis" in a PubMed search. **None of these papers study piperacillin as a treatment for RA.** They document piperacillin used as an antibiotic to manage infections arising in immunosuppressed RA patients, or methotrexate-related complications in which piperacillin does not even appear. The 10 most informative entries are presented below for transparency:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case Report | Orthopädie | RA patient on JAK1 inhibitor (upadacitinib) developed prosthetic knee infection; IV piperacillin/tazobactam initiated for concurrent pneumonia — antibiotic use, not RA therapy |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case Report | BMJ Case Reports | RA patient on etanercept + methotrexate developed purulent pericarditis; empirical piperacillin/tazobactam started for suspected infection — drug used as antibiotic, not RA modifier |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Retrospective Cohort | Br J Clin Pharmacol | Machine-learning risk-scoring model for antibiotic-induced eosinophilia in hospitalised patients receiving piperacillin/tazobactam or ampicillin/sulbactam — safety pharmacology study, no RA relevance |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Retrospective Cohort | Ann Transl Med | Prevalence and clinical characteristics of antibiotic-associated drug-induced liver injury (DILI); piperacillin listed among causative agents — DILI surveillance study |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case Report | Cureus | RA patient in 9-year remission on sulfasalazine developed isolated recurrent pleural effusion; piperacillin not involved |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case Report | Proc Baylor Univ Med Ctr | Low-dose methotrexate toxicity causing pancytopenia and stomatitis in RA; leucovorin rescue — piperacillin not involved |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case Report | Cureus | Pancytopenia as a diagnostic challenge in RA patient on low-dose methotrexate — piperacillin not mentioned |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Case Report | Orthopedics | Bilateral femoral emphysematous osteomyelitis caused by *E. coli* in RA patient on long-term prednisone; treated with IV antibiotics and intramedullary antibiotic cement |
| [19621776](https://pubmed.ncbi.nlm.nih.gov/19621776/) | 2009 | Case Report | No Shinkei Geka | Hypertrophic pachymeningitis treated with a regimen including piperacillin; minocycline reduced CRP — piperacillin used as an antibiotic, no autoimmune/RA relevance |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case Report | Med J Australia | Near-fatal pancytopenia following accidental methotrexate overdose in RA — piperacillin not involved |

> ⚠️ **Critical Interpretation Note**: Not a single retrieved publication provides evidence that piperacillin treats, modifies, or ameliorates rheumatoid arthritis. The co-occurrence of piperacillin and RA in these papers reflects the antibiotic's role in managing infectious complications in immunosuppressed RA patients — a classic confounding scenario in knowledge-graph-based predictions.

---

## Malaysia Market Information

Eight product licenses are registered in Malaysia under Marketed status. Detailed registration records (product names, dosage forms, manufacturers, approved indication texts) were not returned by the NPRA data query for this candidate. Please consult the [NPRA Product Registration database](https://www.npra.gov.my) directly for current license details.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Full warning text, contraindications, and drug–drug interaction data were not available in the data source at the time of this report. Clinically, piperacillin/tazobactam is known to carry risks of hypersensitivity reactions (including anaphylaxis), antibiotic-associated DILI, and eosinophilia with prolonged use. Dose adjustment is required in renal impairment (reduced CrCl) — a particularly relevant consideration if this drug were ever evaluated in RA patients with comorbid diabetic or inflammatory nephropathy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked score of 99.94% for piperacillin in rheumatoid arthritis is almost certainly a **confounding artifact** driven by the high frequency with which immunosuppressed RA patients receive piperacillin for bacterial infections; zero clinical trials and zero directly supportive publications confirm that no genuine repurposing signal exists. There is no mechanistic basis — and some theoretical harm (gut dysbiosis worsening autoimmunity) — to justify further development of this candidate.

**To move beyond Hold, the following would be required:**

- **Mechanism validation**: Preclinical evidence demonstrating piperacillin's direct anti-inflammatory effect on RA-relevant pathways (e.g., synovial fibroblast invasion, Th17/Treg balance, NF-κB or NLRP3 inhibition) in *in vitro* or animal arthritis models
- **Knowledge graph debiasing**: Re-analysis of the TxGNN graph to correct for the "infection-in-immunosuppressed-patient" confounding structure before re-scoring
- **MOA data retrieval**: Full DrugBank pharmacological profile (currently unavailable — data gap DG002) to identify any secondary immunomodulatory targets
- **Regulatory safety profile**: Retrieval and parsing of Malaysian product insert PDFs (currently unavailable — data gap DG001) to complete the safety assessment required for S1-stage evaluation
- **Microbiome impact assessment**: Literature review on beta-lactam effects on gut microbiota composition in autoimmune disease models, given the theoretical risk of worsening RA through dysbiosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

