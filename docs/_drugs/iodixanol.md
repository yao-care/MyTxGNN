---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Iodixanol: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is a non-ionic, iso-osmolar radiographic contrast agent, primarily used as an imaging aid rather than a therapeutic drug. The TxGNN model predicts possible relevance to three joint-disease phenotypes — **osteoarthritis susceptibility** (top-ranked), osteoarthritis, and rheumatoid arthritis — all with ~99% network scores, but **no clinical trials exist for any of the three**, and the available literature (8 papers total) uses iodixanol exclusively as a research/imaging tool in osteoarthritis studies rather than as a treatment, suggesting the high scores likely reflect a co-occurrence artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available NPRA license records; per the evidence pack's own literature, iodixanol is identified as "a neutral diffusing computed tomography (CT) contrast agent" — i.e., a diagnostic imaging agent, not a treatment |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for iodixanol (flagged as a High-severity data gap). Based on the information available, iodixanol is a radiographic contrast medium — its established pharmacological role is to enhance X-ray/CT visualization of tissue, not to modify disease biology. It has no known anti-inflammatory, chondroprotective, or immunomodulatory mechanism that would plausibly treat osteoarthritis or rheumatoid arthritis.

The literature actually retrieved in this evidence pack supports this concern rather than resolving it: all 7 osteoarthritis-related papers and the 1 rheumatoid-arthritis-related paper use iodixanol (or the related agent iohexol) as a **research or diagnostic tool** — e.g., a CT tracer to study cartilage/subchondral-bone solute transport, a contrast agent in photon-counting CT cartilage imaging, or a radiocontrast agent requiring desensitization in an RA patient — not as a therapeutic intervention being tested against these diseases.

This pattern is consistent with a TxGNN false-positive: because iodixanol frequently co-occurs with osteoarthritis in the literature (as an imaging tool used *to study* OA), the knowledge-graph embedding may register a strong drug–disease association without any underlying treatment relationship. The evidence pack's own rationale field for the osteoarthritis candidate makes this explicit, and the same concern applies to the top-ranked "osteoarthritis susceptibility" candidate, which has zero supporting literature or trials at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis susceptibility, osteoarthritis, or rheumatoid arthritis (0 results across ClinicalTrials.gov and ICTRP for all three candidates).

---

## Literature Evidence

No literature was found for the top-ranked candidate (osteoarthritis susceptibility). The table below lists the literature found for the other two candidates evaluated in this evidence pack, none of which constitutes therapeutic evidence.

**For osteoarthritis:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imaging/Methodology | Ann Biomed Eng | Uses a dual-contrast (nanoparticle + molecular) approach in photon-counting CT to assess articular cartilage health — a diagnostic imaging technique, not a treatment |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imaging/Methodology | Ann Biomed Eng | Nanoparticle diffusion CT + finite element study of cartilage function |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Basic Science (transport model) | J Biomech | Uses iodixanol (~1550 Da) as a neutral CT contrast tracer to study solute permeability across the cartilage/subchondral-bone interface in OA models |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Basic Science (finite element model) | J Biomech | Finite-element modeling of neutral solute transport across the osteochondral interface using CT contrast tracing |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Basic Science (finite element model) | J Vis Exp | Experimental/FEM protocol for tracking neutral and charged solute transport across cartilage |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Basic Science (ex vivo) | Osteoarthritis Cartilage | Aging effects on mandibular condylar cartilage stiffness (diffusion-based methodology) |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | J Exp Orthop | Iodine contrast agents do not affect Platelet-Rich Plasma function used for intra-articular injection guidance |

**For rheumatoid arthritis:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Case report | Cureus | Successful desensitization to radiocontrast iohexol in an RA patient with amyloidosis needing repeat angioplasty imaging — an allergy-management case, unrelated to RA treatment |

---

## Malaysia Market Information

NPRA records confirm iodixanol is marketed in Malaysia with **4 active registrations**. However, detailed license records (registration numbers, product names, dosage forms, and approved indication text) were not returned in this data pull and cannot be tabulated at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (osteoarthritis susceptibility) has no supporting clinical trials or literature whatsoever — a pure model score. The next two candidates (osteoarthritis, rheumatoid arthritis) have literature, but every paper uses iodixanol as an imaging/research tool rather than a therapeutic agent, matching the profile of a TxGNN co-occurrence artifact rather than a real repurposing signal. Separately, the TFDA/NPRA labeling data (warnings and contraindications) is a Blocking-severity gap, which on its own prevents this candidate from entering the S1 safety screening stage.

**To proceed, the following is needed:**
- TFDA/NPRA package insert: key warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data (High-priority gap, DG002)
- An independent assessment of whether the TxGNN score reflects a genuine pharmacological hypothesis or a literature co-occurrence artifact, before committing further evaluation resources
- If pursued, a preclinical/pharmacological rationale for any anti-arthritic activity of iodixanol, which does not currently exist in the evidence reviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

