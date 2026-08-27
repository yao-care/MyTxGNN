---
layout: default
title: Methylene Blue
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 3
---

# Methylene Blue
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

# Methylene Blue: From Undocumented Original Indication to Bronchitis

## One-Sentence Summary

> Methylene Blue (DrugBank DB09241) is marketed in Malaysia, but the source registry entry currently contains no documented original indication text or mechanism-of-action data.
> The TxGNN model assigns a very high score to **Bronchitis** as a candidate new indication, but the supporting literature is dominated by incidental co-occurrence (e.g., methylene blue used as a bronchoscopy stain) rather than genuine treatment evidence — **0 clinical trials** and **10 publications**, none of which describe therapeutic use of methylene blue in bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current NPRA license record (pending retrieval) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methylene blue is not currently available from the queried sources (DrugBank query pending — see data gap DG002). Based on well-established pharmacology, methylene blue is a phenothiazine-class redox dye best known for accepting electrons from NADPH via methemoglobin reductase and non-enzymatically reducing ferric (Fe³⁺) iron back to ferrous (Fe²⁺) iron — the basis of its classic use as an antidote in methemoglobinemia (see the Additional Predicted Indications section below). No comparable redox, anti-inflammatory, bronchodilatory, or antimicrobial mechanism linking methylene blue to chronic or acute bronchitis is described in the retrieved evidence.

Reviewing the 10 literature records tied to this prediction, the great majority use methylene blue only as a diagnostic **stain** (e.g., in fiberoptic bronchoscopy to differentiate malignant from benign bronchial tissue, or in bronchoalveolar lavage fluid quantitation) rather than as a therapeutic agent for bronchitis. Several other records are unrelated compounds (a beta-blocker, plant essential oils, a biosensor) that merely mention "bronchitis" in their background text, alongside methylene blue appearing elsewhere in the same corpus. The repurposing rationale supplied with this candidate explicitly flags this as **textual co-occurrence noise** rather than a treatment signal, which is consistent with the L5 evidence level and Hold recommendation below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic Cohort | Zhonghua wai ke za zhi | Methylene blue used as a bronchoscopy stain to distinguish central lung cancer from bronchitis (diagnostic use, not treatment) |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Case Report/Other | Terapevticheskii arkhiv | Methylene blue chromoendofibroscopy for differentiating benign/malignant GI and bronchial neoplasms (diagnostic staining) |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Other | Am Rev Respir Dis | Methylene blue used as one of five tracer markers to quantify intra-alveolar fluid in lavage studies (methodological use) |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case Report | Mikrobiyoloji bulteni | Case of *Moraxella catarrhalis* endocarditis; bronchitis mentioned only as a typical presentation of this organism, unrelated to methylene blue |
| [17120034](https://pubmed.ncbi.nlm.nih.gov/17120034/) | 2007 | Case Report | Eur J Pediatr | Tracheoesophageal fistula case report; no methylene blue-bronchitis treatment link |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical (unrelated compound) | J Ethnopharmacol | *Lippia alnifolia* essential oil relaxes guinea-pig trachea; bronchitis mentioned only as background, not methylene blue |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical (unrelated compound) | J Ethnopharmacol | *Aloysia gratissima* antidepressant/neuroprotective study; bronchitis mentioned only in traditional-use background |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Other (unrelated) | Anal Chim Acta | Gold-nanoparticle aptasensor for theophylline detection; bronchitis mentioned only as a theophylline indication, unrelated to methylene blue |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Other (unrelated drug) | Int J Clin Pharmacol Ther Toxicol | Beta-blocker "Tobanum" cardiovascular study; methylene blue used only as a circulation-time indicator dye |
| [2749902](https://pubmed.ncbi.nlm.nih.gov/2749902/) | 1989 | Other | Tsitologiia | Cytospectrophotometric study of methemoglobin in erythrocytes using methylene blue-related dyes; unrelated to bronchitis |

---

## Additional Predicted Indications (Higher Evidence Confidence)

The evidence pack includes two further TxGNN-ranked candidates for methylene blue that are considerably better supported mechanistically than bronchitis and warrant separate tracking:

### Methemoglobinemia, alpha type (drug/chemical-induced) — Rank 2

TxGNN score 99.36% · **Evidence Level L3** · Decision Stage S2 · **Recommendation: Proceed with Guardrails**

Methylene blue is reduced by NADPH-methemoglobin reductase to leucomethylene blue, which non-enzymatically converts ferric (Fe³⁺) methemoglobin back to normal ferrous (Fe²⁺) hemoglobin — a textbook-established mechanism and methylene blue's classic role as the standard antidote for acquired/drug-induced methemoglobinemia.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/) | 1986 | Review | Medical Toxicology | Clinical features and management of drug- and chemical-induced methemoglobinemia, including methylene blue treatment |
| [26950891](https://pubmed.ncbi.nlm.nih.gov/26950891/) | 2016 | Basic Science/Other | J Photochem Photobiol B | Molecular/photochemical study of methylene blue; notes FDA-documented toxicities including methemoglobinemia |

No clinical trials currently registered for this indication.

### Methemoglobinemia due to methemoglobin reductase deficiency (congenital/hereditary) — Rank 3

TxGNN score 99.36% · **Evidence Level L4** · Decision Stage S1 · **Recommendation: Research Question**

Same underlying redox mechanism as above, but in patients with hereditary cytochrome b5 reductase (diaphorase I) deficiency. Individual response varies, and methylene blue is contraindicated/risky in patients with concurrent G6PD deficiency (hemolysis risk), so this population needs separate safety evaluation from the acquired form.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36638001](https://pubmed.ncbi.nlm.nih.gov/36638001/) | 2023 | Cohort (Animal) | Am J Vet Res | Long-term oral methylene blue in dogs with hereditary CYB5R deficiency; effects on methemoglobin levels and inflammatory markers |
| [29845943](https://pubmed.ncbi.nlm.nih.gov/29845943/) | 2018 | Case Report | Neth J Med | 61-year-old with congenital methemoglobinemia (novel CYB5R3 variant); brief recurrence after methylene blue suggested congenital cause |
| [35202847](https://pubmed.ncbi.nlm.nih.gov/35202847/) | 2022 | Case Report (Animal) | Top Companion Anim Med | Oral methylene blue in a dog with CYB5R deficiency and disorder of sex development |
| [14109019](https://pubmed.ncbi.nlm.nih.gov/14109019/) | 1964 | Case Report | Arch Intern Med | Early description of hereditary diaphorase deficiency and methemoglobinemia |
| [14248326](https://pubmed.ncbi.nlm.nih.gov/14248326/) | 1964 | Case Report | Arch Fr Pediatr | New case of recessive congenital methemoglobinemia linked to diaphorase I deficiency |

No clinical trials currently registered for this indication.

---

## Malaysia Market Information

NPRA records list methylene blue as **Marketed** with **1 registration on file**; the license number, product name, dosage form, and approved indication text for this registration have not yet been retrieved from the source registry (data gap DG001, blocking).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision (Bronchitis): Hold**

**Rationale:**
- TxGNN's 99.97% score for bronchitis is not supported by any clinical trial or genuine mechanistic literature — the 10 retrieved publications reflect co-occurrence noise (methylene blue as a diagnostic stain, or unrelated compounds mentioning bronchitis), consistent with the pack's own L5/Hold assessment.

**To proceed, the following is needed:**
- TFDA/NPRA label data — warnings, contraindications (DG001, blocking)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- A specific pharmacological hypothesis (anti-inflammatory, antimicrobial, or mucolytic) connecting methylene blue to bronchitis before this candidate can advance past S0

**Separately noted:** the methemoglobinemia candidates (Rank 2 & 3) are mechanistically well-supported and already carry "Proceed with Guardrails" / "Research Question" recommendations in this pack — these represent methylene blue's known, established pharmacology rather than novel repurposing, and should be tracked on their own evaluation path rather than folded into the bronchitis assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

