---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is an established second-generation antiseizure medication, already approved for a broad spectrum of epilepsy syndromes (partial-onset seizures, myoclonic seizures in juvenile myoclonic epilepsy, and primary generalized tonic-clonic seizures). The TxGNN model predicts it may also be effective for **Visual Epilepsy** (a reflex/photosensitive epilepsy phenotype), with **9 clinical trials** and **20 publications** retrieved — though, as detailed below, most of this evidence addresses seizure management broadly rather than visual epilepsy specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset seizures (adjunct/monotherapy), myoclonic seizures in JME, and primary generalized tonic-clonic seizures (per literature evidence in this pack; NPRA license indication text was not returned in this data pull — all 5 license records had empty `approved_indication_text` fields) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 44 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data for this drug is flagged as a data gap (DG002, High severity) in the evidence pack. However, literature retrieved within this same pack indicates Levetiracetam binds synaptic vesicle glycoprotein 2A (SV2A) and modulates presynaptic neurotransmitter release, an action believed to dampen the abnormal, hypersynchronous cortical firing that underlies seizure generation (PMID 34903423, PMID 21936590). This SV2A-mediated mechanism is considered broad-spectrum, acting across focal, generalized, and reflex seizure types rather than being restricted to a single epilepsy subtype.

Levetiracetam's original indications span multiple seizure phenotypes — partial-onset seizures, myoclonic seizures in juvenile myoclonic epilepsy, and primary generalized tonic-clonic seizures (PMID 21936590). Visual epilepsy (a reflex epilepsy triggered by visual stimuli, closely related to photosensitive epilepsy) sits within this same broader epilepsy spectrum and is thought to share the underlying cortical hyperexcitability mechanism that Levetiracetam already targets, which is the likely basis for the TxGNN model's near-100% prediction score.

That said, a close read of the retrieved evidence shows a gap between prediction and disease-specific validation: the 9 clinical trials and 20 publications returned for this candidate largely address seizure prophylaxis in traumatic brain injury, intracerebral haemorrhage, neonatal seizures, status epilepticus, and migraine — none directly enrolled or studied patients with visual/photosensitive epilepsy as the target condition. By contrast, related reflex-epilepsy phenotypes evaluated elsewhere in this evidence pack (e.g., reading epilepsy, startle epilepsy) do have direct clinical evidence for Levetiracetam or its analog seletracetam. This suggests plausible drug-class applicability but not yet a disease-specific evidence base for "visual epilepsy" itself — reflected in this candidate's own evidence-scoring fields being marked "pending" rather than assigned in the source data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | MAST trial — defines optimal duration and choice (phenytoin vs. levetiracetam) of antiepileptic drugs for seizure prevention after traumatic brain injury |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Liceo study — observational effectiveness of new AEDs (including levetiracetam) as first-choice bitherapy in focal epilepsy |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | RCT of prophylactic levetiracetam to improve functional outcome in acute intracerebral haemorrhage |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Efficacy of levetiracetam in control of neonatal seizures |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | AVASPA gene therapy study for Canavan disease; levetiracetam not the primary study drug — relevance to visual epilepsy unclear |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Cognitive/neuropsychological safety of levetiracetam as adjunctive therapy in children with refractory partial-onset seizures |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam's effect on hippocampal hyperactivity in patients with psychotic disorders (fMRI study) |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Same hippocampal-hyperactivity/psychosis study design, terminated early (enrollment n=1) |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label trial of levetiracetam for prophylactic treatment of migraine, with or without (visual) aura |

*Note: none of the above trials specifically enrolled or evaluated patients with visual/photosensitive epilepsy; they were returned via broad drug + seizure-related search terms.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3, PEACH) | The Lancet Neurology | Prophylactic levetiracetam did not clearly reduce acute seizure risk after intracerebral haemorrhage in this placebo-controlled trial |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs. phenobarbital for neonatal seizures; efficacy and safety compared head-to-head |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic review/meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in ICH, TBI, neurosurgery, and SAH; efficacy and optimal dosing remain unclear |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Clinical practice guideline | Neurocritical Care | Guideline on seizure prophylaxis in adults hospitalized with moderate-severe TBI |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic review/network meta-analysis | Journal of Neurology | Comparative efficacy/safety of antiseizure medications, including levetiracetam, for idiopathic generalized epilepsies |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic review/meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy, including juvenile myoclonic epilepsy |
| [35538830](https://pubmed.ncbi.nlm.nih.gov/35538830/) | 2023 | Meta-analysis | CNS & Neurological Disorders Drug Targets | Safety/effectiveness of levetiracetam vs. phenytoin in pediatric status epilepticus |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Medical Journal | Randomized comparison of phenobarbital and levetiracetam in childhood epilepsy |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | Open-label RCT | Seizure | Phenytoin vs. levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam's established indications: partial-onset seizures, myoclonic seizures in JME, and primary generalized tonic-clonic seizures |

*Note: as with the clinical trials, none of the retrieved literature specifically studies visual/photosensitive epilepsy; the body of evidence instead supports levetiracetam's broad, established role across other seizure types.*

---

## Malaysia Market Information

Levetiracetam is confirmed marketed in Malaysia with **44 total NPRA registrations**. However, product-level details (authorization numbers, product names, dosage forms, and approved indication text) were not populated in this evidence pull — all 5 sampled license records returned empty fields for these attributes. A follow-up NPRA data query is needed before a product-level table can be presented.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No structured warnings, contraindications, or drug-interaction data were returned for this candidate. Notably, this gap is flagged in the evidence pack as DG001 — "TFDA/NPRA label warnings/contraindications" — with Blocking severity, meaning it currently prevents a full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Levetiracetam has a strong, well-established evidence base across multiple seizure types, but none of the 9 clinical trials or 20 publications retrieved for this candidate specifically evaluate visual/photosensitive epilepsy — the evidence pack itself leaves this candidate's evidence level, decision stage, and recommendation marked as "pending." Combined with a Blocking-severity data gap on NPRA label warnings/contraindications (DG001), a defensible safety pre-assessment cannot yet be completed.

**To proceed, the following is needed:**
- NPRA label PDF (warnings, contraindications) to resolve DG001 (Blocking)
- DrugBank mechanism-of-action data to resolve DG002 (High)
- Targeted literature/trial search specifically for "visual epilepsy" / photosensitive reflex epilepsy (current results are drug + generic-seizure matches, not disease-specific)
- A completed drug-drug interaction (DDI) query — current status is `not_found` with 0 results
- NPRA product-level license data (authorization numbers, product names, dosage forms, indication text), since the current sample returned empty fields across all 5 records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

