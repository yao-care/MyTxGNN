---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 3
---

# Nitrazepam
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

# Nitrazepam: From Insomnia to Insomnia (Sleep Disorder, Initiating and Maintaining Sleep)

## One-Sentence Summary

Nitrazepam is a classic benzodiazepine hypnotic used for insomnia. The TxGNN model's top prediction — **Sleep Disorder, Initiating and Maintaining Sleep** — is essentially a re-identification of this drug's own established indication rather than a novel repurposing target, supported by **20 publications** (including 1 RCT) but **0 registered clinical trials**. Two additional, much lower-confidence candidates (acute encephalopathy with biphasic seizures, Wernicke-Korsakoff syndrome) were also flagged by the model but have no supporting evidence at all.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in NPRA license text (blank in registry extract); internationally, nitrazepam is indicated for short-term treatment of insomnia |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep (Insomnia) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (1 RCT-level publication; no registered clinical trials) |
| Malaysia Market Status | Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nitrazepam is a classic benzodiazepine that acts on the α-subunits of the GABA-A receptor, increasing the frequency of chloride-channel opening. This produces sedative, anxiolytic, muscle-relaxant, and anticonvulsant effects — a well-characterized mechanism directly relevant to sleep induction and maintenance.

Importantly, the model's top-ranked prediction is not a genuinely new indication: it reflects nitrazepam's own long-established, primary clinical use as a hypnotic. This should be read as TxGNN correctly recovering a known drug-disease relationship rather than surfacing a novel repurposing hypothesis — useful as a validation signal for the model, but not as new commercial or clinical opportunity.

TxGNN also surfaced two lower-ranked, much weaker candidates: acute encephalopathy with biphasic seizures and late reduced diffusion (AESD), and Wernicke-Korsakoff syndrome (WKS). Both share a superficial pharmacological rationale (GABA-A agonism could theoretically help control seizures or agitation in these conditions), but neither has any supporting clinical trial or literature evidence, and the core pathology of each (neuroinflammation/cytotoxic edema in AESD; thiamine-deficiency-driven neurodegeneration in WKS) is not addressed by nitrazepam's mechanism. Both are scored L5 and recommended **Hold**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatr Scand | Double-blind crossover trial (n=26 geriatric inpatients): nitrazepam 5mg vs. triazolam 0.25mg produced similar sleep quantity/quality and psychomotor performance, no significant difference |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Up to 40% of adults have insomnia; prevalence rises with age; reviews risk factors and hypnotic treatment evidence |
| [32724021](https://pubmed.ncbi.nlm.nih.gov/32724021/) | 2020 | Review | Med Lett Drugs Ther | Review of lemborexant (Dayvigo), a newer orexin-antagonist hypnotic, contextualizing older benzodiazepine hypnotics such as nitrazepam |
| [20467592](https://pubmed.ncbi.nlm.nih.gov/20467592/) | 2010 | Review | Drugs of Today | Reviews serotonin 5-HT2A antagonists for insomnia; notes benzodiazepines (incl. nitrazepam) reduce slow-wave and REM sleep versus non-BZD hypnotics |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskr Nor Laegeforen | Reviews classification, diagnosis, and treatment developments in insomnia for general practitioners |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Reviews hypnotic drug efficacy in relation to sleep physiology (REM/NREM cycling) |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Review | British Medical Journal | Correspondence/commentary on nitrazepam's reported subjective and dream-related effects |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Review/Case | British Medical Journal | 27 patients took nitrazepam overdose (up to 80 tablets) with only drowsiness, no serious harm; double-blind trial found it as effective as butobarbitone — concluded "a safe hypnotic" |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | PK study | Clin Pharmacokinet | Reviews nitrazepam's clinical pharmacokinetics (absorption, half-life, metabolism) |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case report/Cohort | Br J Psychiatry | Case series on nitrazepam (Mogadon) dependence risk with prolonged use |

---

## Malaysia Market Information

Nitrazepam is marketed in Malaysia with 1 NPRA registration; detailed license number, product name, dosage form, and approved-indication text are not populated in the current data extract and would need to be pulled directly from the NPRA product register.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (insomnia) is pharmacologically coherent and supported by one RCT-level publication plus a substantial historical literature base, but it reconfirms nitrazepam's already-known indication rather than identifying a new one — so there is no true "repurposing" upside here, only a validation signal. The two other TxGNN-flagged indications (AESD, WKS) have no supporting evidence and are separately recommended Hold.

**To proceed, the following is needed:**
- TFDA/NPRA product label (key warnings, contraindications) — currently a blocking data gap (DG001)
- Formal MOA confirmation via DrugBank API (currently a data gap, DG002)
- Drug-drug interaction (DDI) data — current query returned no results
- Complete NPRA license/product details (license number, product name, dosage form, approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

