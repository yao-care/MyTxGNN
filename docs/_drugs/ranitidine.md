---
layout: default
title: Ranitidine
parent: High Evidence (L1-L2)
nav_order: 585
evidence_level: L1
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer / GERD Therapy to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist historically used to suppress gastric acid secretion in peptic ulcer disease and GERD. The TxGNN model's top prediction for this drug is **Active Peptic Ulcer Disease** (score 99.89%), which is not a truly novel indication but a re-confirmation of ranitidine's own classic, decades-established use — supported by **1 clinical trial record** and **20 publications**, including multiple head-to-head RCTs against ranitidine as an active comparator. Note: ranitidine was withdrawn/recalled in several major markets in 2019–2020 due to NDMA contamination concerns, which must be factored into any go-forward decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in source data (DG001: TFDA/NPRA label text not extracted — all 6 license records have empty indication fields). Ranitidine's classic pharmacological use is gastric acid suppression in peptic ulcer disease/GERD, per the evidence pack's own mechanistic rationale text. |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap (DG002) in this evidence pack. However, the pack's own repurposing rationale for this candidate states the mechanism directly: ranitidine is a competitive H2-receptor antagonist that blocks histamine-driven acid secretion at gastric parietal cells, reducing both basal and stimulated gastric acid output and thereby promoting ulcer healing — a classic, well-established mode of action for this drug class.

The key nuance here is that "active peptic ulcer disease" is **not a new therapeutic frontier** for ranitidine — it is the drug's own core, long-established indication. The pack explicitly notes (for the closely related candidate "peptic ulcer disease," rank 7, same evidence level L1 and same recommendation) that this reflects a data-gap artifact in the original-indication field rather than genuine lack of efficacy evidence. In other words, TxGNN's high score here is best read as validating known pharmacology rather than surfacing a genuinely novel repurposing opportunity.

That said, the underlying mechanistic logic is sound and well supported: multiple historical RCTs directly compared ranitidine against cimetidine, famotidine, and omeprazole in duodenal/gastric ulcer healing, consistently confirming efficacy. A closely related candidate in the same pack ("peptic ulcer disease," rank 7) carries substantially richer clinical trial documentation (11 trials, including completed Phase 3 studies such as NCT00633672 and NCT00401752 using ranitidine as an active comparator), reinforcing confidence in this mechanistic class for this disease area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated effects of various PPIs and statins on clopidogrel antiplatelet activity in PCI patients — study focus is drug–drug interaction, not direct ranitidine efficacy in active PUD (relevance grade C, per pack annotation). |

No trial in this record directly tests ranitidine as an intervention for active peptic ulcer disease specifically; the single retrieved trial is only indirectly related (PPI/statin–clopidogrel interaction). Stronger direct trial evidence for the closely related "peptic ulcer disease" candidate exists elsewhere in this pack (see rank 7) but falls outside the scope of this specific disease-term entry.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Nocturnal rioprostil vs. ranitidine in duodenal ulcer healing; ranitidine used as active comparator with established efficacy. |
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Ranitidine 300 mg/day in 151 patients with duodenal/prepyloric/gastric corporeal ulcer; 4-week healing rates 68–91%; ranitidine also effective in relapse-prevention maintenance therapy. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clinical Therapeutics | 160-patient multicenter trial: famotidine 40 mg vs. ranitidine 300 mg nightly for active duodenal ulcer; ranitidine achieved 80% endoscopic healing at 8 weeks, incl. NSAID/aspirin-related ulcers. |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | Journal of Gastroenterology and Hepatology | Double-blind, double-dummy trial (270 patients): omeprazole vs. ranitidine 150 mg bid for duodenal ulcer healing and relapse, with weekly endoscopic assessment. |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | The American Journal of Medicine | Multicenter, double-blind, randomized international study (1,031 patients, 19 countries): famotidine vs. ranitidine for active duodenal ulcer. |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT | Journal of the Association of Physicians of India | Double-blind randomized trial: famotidine 40 mg vs. ranitidine 300 mg nocturnal dosing for gastric/duodenal ulcer, 4–8 week endoscopic follow-up. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intelligence & Clinical Pharmacy | Overview confirming ranitidine's FDA approval for active duodenal ulcer and gastric hypersecretory states; 4–10x more potent than cimetidine. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-Gastroenterology | Reviews acid suppression as central mechanism in peptic ulcer healing across H2-antagonists including ranitidine. |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | Controlled study | Hepato-Gastroenterology | Prospective controlled study: ranitidine + ecabet vs. ranitidine alone for inhibition of peptic ulcer relapse, independent of H. pylori eradication. |
| [6317740](https://pubmed.ncbi.nlm.nih.gov/6317740/) | 1983 | Review | Journal of Clinical Gastroenterology | Comparative pharmacodynamics/pharmacokinetics of cimetidine and ranitidine, both established H2-antagonists for peptic ulcer disease. |

---

## Malaysia Market Information

The NPRA registry shows **6 active licenses** for ranitidine in Malaysia (market status: Marketed), but the detailed license fields (authorization number, product name, dosage form, approved indication text) are not populated in this data extract — this is tracked as data gap DG001 and is flagged as **Blocking** for safety evaluation, since it also prevents retrieval of label warnings/contraindications. These fields need to be sourced from NPRA/label PDFs before market-level claims can be made.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) is currently available for this candidate — all fields are marked as data gaps in the source pack (DG001, Blocking severity).

One critical safety signal surfaced directly within the evidence pack's own rationale must be flagged: **ranitidine was withdrawn/recalled in multiple countries in 2019–2020 due to N-nitrosodimethylamine (NDMA) impurity concerns** (see PMID 31848148, "Ranitidine in short supply: why now, and where next?"). Given Malaysia's market status here is listed as "Marketed," current supply status and any NPRA safety communications on this issue should be verified before any guardrail decision is finalized.

Please refer to the package insert for full safety information once retrieved.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and historical clinical-trial/literature evidence for ranitidine in acid-suppression-responsive ulcer disease is strong (Evidence Level L1), but this is essentially confirmation of an already-established use rather than a novel repurposing signal, and a Blocking-severity safety data gap (label warnings/contraindications) prevents a full safety evaluation at this time.

**To proceed, the following is needed:**
- Retrieve TFDA/NPRA label PDF content to resolve DG001 (warnings, contraindications) — currently Blocking for safety review
- Retrieve DrugBank MOA data to resolve DG002 and support formal mechanistic-linkage documentation
- Populate the 6 Malaysia license records (product name, dosage form, approved indication text) — currently all empty
- Confirm current Malaysia market/supply status in light of the global 2019–2020 NDMA-related ranitidine recalls
- Clarify whether this candidate should be treated as a genuine repurposing opportunity or reclassified as label-consistent use, given the overlap with rank #7 ("peptic ulcer disease") in this same evidence pack

---

### Other Candidate Indications in This Pack (Lower Priority, for Reference Only)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------|------|------|
| 2 | Peptic ulcer perforation | 99.88% | L4 | Hold |
| 3 | Gastrojejunal ulcer | 99.88% | L3 | Research Question |
| 4 | Duodenogastric reflux | 99.84% | L4 | Hold |
| 5 | Duodenal obstruction | 99.83% | L4 | Hold |
| 6 | Gastroduodenitis | 99.73% | L3 | Proceed with Guardrails |
| 7 | Peptic ulcer disease | 99.58% | L1 | Proceed with Guardrails |
| 8 | Smouldering systemic mastocytosis | 99.53% | L4 | Research Question |
| 9 | Abnormality of glucagon secretion | 99.50% | L5 | Hold |
| 10 | Lymphoadenopathic mastocytosis with eosinophilia | 99.43% | L5 | Hold |

*This report focuses on the top-ranked candidate per the specified evidence pack structure; candidates 2–10 would require separate individual evaluation if pursued further.*
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

