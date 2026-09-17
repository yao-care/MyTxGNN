---
layout: default
title: Potassium Citrate
parent: Medium Evidence (L3)
nav_order: 566
evidence_level: L3
indication_count: 10
---

# Potassium Citrate
{: .fs-9 }

Tahap bukti: **L3** | Indikasi diramal: **10** 
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

Using no additional tools — this is a direct content-generation task; I'll follow the report template exactly against the supplied Evidence Pack.

# Potassium Citrate: From Urinary Alkalinization to Renal Tubular Acidosis

## One-Sentence Summary

Potassium citrate is a urinary alkalinizing agent long used to correct hypocitraturia and prevent recurrent calcium/uric-acid kidney stones, and it is currently marketed in Malaysia under 31 NPRA registrations. The TxGNN model predicts it may be effective for **Renal Tubular Acidosis**, a direction supported by **3 clinical trials** and **16 publications**, though none of the trials reached a successful, adequately powered completion. The evidence base is dominated by decades-old dosing/observational studies and reviews rather than confirmatory RCTs, reflecting the fact that potassium citrate is already established off-label/adjunct practice for this condition rather than a truly novel hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary alkalinization / prevention of kidney stones (specific NPRA registration indication text not returned in this dataset) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L3 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 31 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, potassium citrate is an alkalinizing salt that dissociates to provide citrate and bicarbonate-equivalent buffering capacity; it is an established agent for correcting urinary/metabolic acidification abnormalities and for raising urinary citrate to inhibit calcium salt crystallization. Its efficacy in urinary alkalinization and stone prevention is well established, and mechanistically this extends directly to renal tubular acidosis (RTA), where the core pathophysiology is impaired renal acid excretion leading to metabolic acidosis, hypocitraturia, and hypokalemia — precisely the abnormalities potassium citrate is designed to correct.

Distal RTA and hypocitraturic nephrolithiasis are clinically intertwined: patients with dRTA frequently develop calcium phosphate stones as a direct consequence of chronic acidosis and low urinary citrate, and potassium citrate has been used as a mainstay alkali/citrate replacement therapy in this population for over 30 years. This is reflected in the literature base — several of the oldest and most directly relevant studies are dose-finding/effectiveness studies of potassium citrate specifically in dRTA patients (e.g., Preminger 1985, Tapaneya-Olarn 2002, Domrongkitchaiporn 2002) — rather than being purely a novel algorithmic association.

The main limitation is that no randomized controlled trial has actually confirmed clinical outcome benefit (e.g., stone recurrence or renal function preservation) specifically for potassium citrate in RTA; the one Phase 3 RCT designed to do so (NCT03644706) was terminated with only 3 patients enrolled.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | Randomized, double-blind, placebo-controlled withdrawal study of ADV7103 vs. placebo for preventing metabolic acidosis in pediatric/adult distal RTA; terminated with only 3 subjects enrolled — severely underpowered, no usable efficacy data produced |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Intended to study urinary chemistry and acid-base effects of potassium citrate in children with idiopathic hypercalciuria and urolithiasis; withdrawn before enrollment |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Unknown | 40 | Pilot study of oral sodium bicarbonate (not potassium citrate) to alkalinize serum/urine in pediatric patients with topiramate-induced RTA; drug mismatch, only indirectly relevant |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4009822](https://pubmed.ncbi.nlm.nih.gov/4009822/) | 1985 | Clinical study | The Journal of Urology | In 9 patients with incomplete distal RTA, potassium citrate (60–80 mEq/day) significantly increased urinary pH and citrate and decreased calcium excretion after 3 months |
| [12549788](https://pubmed.ncbi.nlm.nih.gov/12549788/) | 2002 | Clinical study | J Med Assoc Thailand | Determined the optimal potassium citrate dose to correct metabolic acidosis and reduce calcium stone risk in children with distal RTA |
| [11840381](https://pubmed.ncbi.nlm.nih.gov/11840381/) | 2002 | Clinical study | Am J Kidney Diseases | Evaluated effectiveness and optimal dosing of potassium citrate for correcting urinary abnormalities and preventing nephrolithiasis in pediatric distal RTA |
| [39325135](https://pubmed.ncbi.nlm.nih.gov/39325135/) | 2024 | Review | Paediatric Drugs | Reviews recent treatment developments for pediatric distal RTA, including alkali/citrate replacement therapy |
| [35357683](https://pubmed.ncbi.nlm.nih.gov/35357683/) | 2022 | Case Report | Journal of Nephrology | Growth improvement in a child with primary distal RTA after switching from conventional alkalizing treatment to a prolonged-release potassium citrate/potassium bicarbonate formulation |
| [39274272](https://pubmed.ncbi.nlm.nih.gov/39274272/) | 2024 | Cohort | Journal of Clinical Medicine | Evaluated phytate as an adjunct in adults with incomplete distal RTA who could not tolerate standard oral potassium citrate |
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos Españoles de Urología | Reviews diagnosis and management of RTA-associated nephrolithiasis, including citrate/alkalinizing therapy |
| [23924538](https://pubmed.ncbi.nlm.nih.gov/23924538/) | 2013 | Review | Medicina (Buenos Aires) | Reviews citrate's role as an inhibitor of calcium salt crystallization, including in distal RTA and hypokalemia-related hypocitraturia |
| [3306318](https://pubmed.ncbi.nlm.nih.gov/3306318/) | 1987 | Cohort | Mineral and Electrolyte Metabolism | Summarizes data supporting potassium citrate in managing RTA-associated calcium stones, hypocitraturic calcium oxalate nephrolithiasis, and uric acid lithiasis |
| [30454739](https://pubmed.ncbi.nlm.nih.gov/30454739/) | 2019 | Review | Pediatric Clinics of North America | General review of RTA diagnosis, classification, and treatment approach in children |

## Malaysia Market Information

31 NPRA registrations are on file for potassium citrate (market status: Marketed), but this evidence pack did not return populated product name, dosage form, manufacturer, or indication text for individual license entries — only the aggregate count is available. Detailed per-license data needs to be pulled directly from the NPRA registry before this can be tabulated.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong and long-standing clinical dosing/effectiveness studies (dating to 1985) directly support potassium citrate's use in correcting the acid-base and hypocitraturic abnormalities of RTA, but no completed RCT confirms outcome-level benefit — the one designed trial was terminated after enrolling only 3 subjects — so this remains L3 (observational/review-level) evidence rather than confirmatory.

**To proceed, the following is needed:**
- TFDA/NPRA package insert warnings, precautions, and contraindications (currently a Blocking data gap)
- Confirmed DrugBank mechanism-of-action data
- Complete Malaysia license-level detail (product name, dosage form, approved indication text) for the 31 registrations
- A safety monitoring plan (e.g., serum potassium, renal function) specific to RTA populations, given the drug's core potassium-loading effect
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

