---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 6
---

# Etanercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Etanercept (DrugBank DB00005) is a TNF-α inhibiting biologic originally used to treat rheumatoid arthritis and related inflammatory arthritides.
> The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **6 clinical trials** and **20 publications** identified —
> however, the evidence is largely contradictory: most literature documents etanercept-*induced* vasculitis rather than therapeutic benefit, and the only direct interventional trial (in the related condition Wegener's granulomatosis/ANCA-associated vasculitis) was negative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (Malaysia licence indication text not returned in this data extract; based on internationally approved labeling for etanercept) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not returned for this drug in the current data pack. Based on known information, etanercept is a dimeric fusion protein combining the p75 TNF receptor with the Fc portion of human IgG1; it binds and neutralizes soluble TNF-α, and its efficacy in rheumatoid arthritis is well established. Because TNF-α is implicated in endothelial activation and immune-complex deposition in rheumatoid vasculitis (an extra-articular manifestation of RA), a TNF-blocking mechanism is theoretically plausible for this indication — which is presumably what drove the TxGNN score.

However, the evidence base does not support a straightforwardly positive relationship. Multiple case reports and a large registry cohort (BSRBR-RA) instead describe etanercept **triggering** cutaneous vasculitis, lupus-like/vasculitis-like events, and vasculitic nephropathy — a recognized paradoxical autoimmune phenomenon associated with anti-TNF therapy. The single direct interventional trial identified (NCT00001901, a Phase 1/2 trial of etanercept in Wegener's granulomatosis, a closely related ANCA-associated vasculitis) is the historically known WGET trial, which was terminated early after failing to meet its efficacy endpoint and showing an increased malignancy signal. Taken together, the mechanistic rationale exists but the directional evidence is mixed-to-negative, which is why this candidate is scored Hold rather than a positive recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 1/2 | Completed | 60 | The historical "WGET" trial testing etanercept in Wegener's granulomatosis (ANCA-associated vasculitis); terminated early — did not meet efficacy endpoint and showed increased malignancy risk. This is the only direct interventional evidence and it is negative. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional observational study of biologic DMARD treatment patterns in RA in China; not vasculitis-specific. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world treatment pathways comparing etanercept vs. non-biologic therapy in moderate RA; not a vasculitis endpoint study. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional study of tocilizumab (not etanercept) in RA; low direct relevance. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study of immune-mediated inflammatory disease (IMID) risk in patients on biologics/immunosuppressants; not RV-specific and status unknown. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; unrelated to vasculitis efficacy. |

---

## Literature Evidence

*Note: most items below document etanercept-induced (paradoxical) vasculitis or adverse renal/vascular events rather than therapeutic benefit — this pattern is central to the Hold recommendation.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological therapy (including TNF inhibitors) in rheumatoid vasculitis; the most directly relevant evidence source. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | Discusses the rationale and mixed evidence for TNF-α blockade in ANCA-associated vasculitis and glomerulonephritis. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort (adverse event) | RMD Open | BSRBR-RA registry analysis quantifying elevated risk of lupus-like and vasculitis-like events in TNF-inhibitor-treated vs. non-biologic-treated RA patients. |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case report | Case Reports in Medicine | Large-vessel vasculitis occurring in an RA patient during anti-TNF therapy — example of paradoxical vasculitis. |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case report | The Journal of Rheumatology | Proliferative lupus nephritis and leukocytoclastic vasculitis developing during etanercept treatment. |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case report | Rheumatology (Oxford) | Etanercept and infliximab associated with cutaneous vasculitis. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case report | Arthritis and Rheumatism | Accelerated nodulosis and vasculitis following etanercept therapy for RA. |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Commentary | The Journal of Rheumatology | Discusses TNF-α blockade and the risk of drug-induced vasculitis. |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Case report | Cureus | Etanercept-associated nephropathy, illustrating renal/vascular adverse effects of anti-TNF therapy. |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Case report | BMC Nephrology | RA patient who developed membranous nephropathy and ANCA-associated vasculitis successively during biologic treatment. |

---

## Malaysia Market Information

Etanercept holds 8 registered licences under NPRA and carries a "Marketed" status, but the data extraction for this drug did not return individual licence numbers, product names, dosage forms, manufacturers, or approved-indication text — these fields were blank in the source pack. This should be re-queried directly from the NPRA product registry before market-facing use of this report.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug–drug interaction data were returned for etanercept in this data pack; the label/warnings query is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale (TNF-α blockade reducing vascular inflammation) is plausible but the actual evidence base is contradictory: the only direct interventional trial (Wegener's granulomatosis/ANCA-associated vasculitis) was terminated early for lack of efficacy and an increased malignancy signal, and the majority of the literature instead documents etanercept **inducing** vasculitis as a paradoxical adverse effect rather than treating it.

**To proceed, the following is needed:**
- TFDA/NPRA package-insert warnings and contraindications (currently a blocking data gap — required before any S1 safety review)
- Verified mechanism-of-action documentation from DrugBank
- Malaysia licence-level detail (product names, indication text) re-queried from NPRA, since the current pack returned blank fields
- A dedicated, adequately powered trial specifically in rheumatoid vasculitis (not the related-but-distinct ANCA-vasculitis population) before this candidate could move beyond Hold
- Note: other candidates in this evidence pack — inflammatory spondylopathy and polyarticular juvenile rheumatoid arthritis — already carry L1 evidence and "Proceed with Guardrails" status, but these reflect etanercept's *existing* approved uses rather than novel repurposing signals, and are worth reviewing separately from this rheumatoid vasculitis candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

