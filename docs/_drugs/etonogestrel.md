---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 5
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is the progestin active ingredient of subdermal contraceptive implants, used to prevent pregnancy by suppressing ovulation and thinning the endometrium.
The TxGNN model predicts it may also be relevant to **Amenorrhea**,
with **1 clinical trial** and **2 publications** currently linked to this prediction — though none directly tests etonogestrel as an amenorrhea *treatment*.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in the current Malaysia registration record; based on known drug identity, etonogestrel is used as a subdermal contraceptive implant |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, etonogestrel is a synthetic progestin that suppresses ovulation and induces endometrial atrophy — the basis of its use in long-acting contraceptive implants.

Amenorrhea (absence of menstruation) is a well-documented **pharmacological consequence** of progestin-only contraceptives, and progestin implants are sometimes used off-label specifically to induce therapeutic amenorrhea in conditions such as heavy menstrual bleeding or endometriosis-related pain. This gives the prediction plausible mechanistic grounding.

However, an important caveat: the supporting clinical trial and the 1999 literature reference are both contraceptive-efficacy studies, where amenorrhea/bleeding pattern is reported as a **side effect or secondary outcome**, not as a treatment target. This evidence pack does not currently demonstrate that etonogestrel is being studied *for* amenorrhea as a therapeutic indication — the link should be read as mechanistic association rather than confirmed repurposing evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Assessed contraceptive efficacy and safety of the etonogestrel implant during extended use (years 4–5 after insertion); not designed to evaluate amenorrhea as a treatment endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomized comparison of Implanon (etonogestrel) vs. Norplant contraceptive implants; reports bleeding pattern (including amenorrhea) as a secondary outcome, no pregnancies in either arm |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Study Protocol | Trials | COVID-19 pneumonia treatment protocol (BIO101) — content is unrelated to etonogestrel or amenorrhea; likely a spurious match and should be disregarded |

---

## Malaysia Market Information

Malaysia (NPRA) records show **1 active registration** with market status "Marketed," but the license number, product name, dosage form, and approved indication text were not captured in the current data extraction and require follow-up retrieval from NPRA before regulatory review can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA label warnings/contraindications and drug interaction data are currently unavailable (flagged as a **Blocking** data gap — DG001), which prevents completion of the initial safety screen for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for etonogestrel–amenorrhea is plausible, but the cited trial and literature support contraceptive efficacy, not amenorrhea treatment, and a Blocking data gap in TFDA safety labeling prevents any preliminary safety evaluation.

**To proceed, the following is needed:**
- TFDA/NPRA package insert (warnings, contraindications) — required to clear the Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Complete Malaysia license record (license number, product name, dosage form, approved indication text)
- Clarification of whether the intended repurposing use is *therapeutic induction of amenorrhea* (e.g., for menorrhagia/endometriosis) rather than amenorrhea as an incidental contraceptive side effect, ideally supported by trials with amenorrhea as a primary endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

