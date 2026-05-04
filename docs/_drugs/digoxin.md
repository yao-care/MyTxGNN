---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 6
---

# Digoxin
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

# Digoxin: From Heart Failure/Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside historically used for heart failure and atrial fibrillation/flutter, acting by inhibiting the Na⁺/K⁺-ATPase pump to increase cardiac contractility and slow AV nodal conduction. The TxGNN model predicts it may be effective for **Prinzmetal Angina** (vasospastic angina), but mechanistic analysis suggests this represents a **reverse association** — digoxin may actually worsen coronary vasospasm. Currently, **0 clinical trials** and only **2 tangentially related publications** exist, providing essentially no supportive evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure, atrial fibrillation/flutter (licence details pending) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 (Mechanistic analysis only — notably contra-indicative) |
| Malaysia Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase on myocardial and vascular smooth muscle cells, leading to increased intracellular calcium via the Na⁺/Ca²⁺ exchanger. In heart failure, this enhanced calcium availability augments cardiac contractility (positive inotropic effect). In atrial fibrillation, digoxin's vagotonic actions slow AV nodal conduction, controlling ventricular rate.

Prinzmetal angina (variant angina) is caused by transient coronary artery vasospasm, leading to ST-elevation and chest pain typically at rest. The standard treatments — calcium channel blockers and nitrates — work by relaxing vascular smooth muscle and reducing intracellular calcium. **Digoxin's mechanism acts in the opposite direction**: by inhibiting Na⁺/K⁺-ATPase in vascular smooth muscle, digoxin increases intracellular Ca²⁺, which would theoretically **promote** coronary vasospasm rather than relieve it. Clinically, digoxin use in patients with coronary vasospasm is considered a relative contraindication.

The high TxGNN score (99.81%) likely reflects the strong graph-level proximity between digoxin and cardiovascular diseases in the knowledge graph, rather than a genuine therapeutic relationship. This is a well-known limitation of graph-based drug repurposing models: high connectivity within a disease domain can produce spurious "treatment" predictions that are actually harmful associations. **This prediction should be treated as a cautionary example of model output requiring expert pharmacological review.**

## Clinical Trial Evidence

Currently no related clinical trials registered for digoxin in Prinzmetal angina.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Review of chronopharmacology and circadian rhythms in antihypertensive treatment; does not directly address digoxin for vasospastic angina |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chin Med Sci J | Re-evaluation of angina decubitus mechanism in 30 patients; discusses hemodynamic monitoring but does not support digoxin as treatment for vasospastic angina |

> **Note:** Neither publication provides direct evidence for the use of digoxin in Prinzmetal angina. The literature is tangentially related to cardiovascular pharmacology but does not support repurposing.

## Malaysia Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| (Details pending) | — | — | — |
| (Details pending) | — | — | — |
| (Details pending) | — | — | — |
| (Details pending) | — | — | — |

> 4 registrations are on record in Malaysia, but detailed licence information (product names, dosage forms, approved indications) was not available at data cutoff. Please consult the NPRA database for complete registration details.

## Safety Considerations

> Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack.
>
> **Important pharmacovigilance note for this specific repurposing candidate:** Digoxin is known to have a narrow therapeutic index. In the context of Prinzmetal angina, digoxin's mechanism of increasing intracellular Ca²⁺ in vascular smooth muscle poses a **potential risk of exacerbating coronary vasospasm**. This represents a safety signal against, rather than in favour of, this repurposing direction.

## Additional Predicted Indications (Ranked 2–6)

All additional TxGNN predictions for digoxin were assessed and received **Hold** recommendations due to lack of mechanistic rationale and absence of clinical evidence:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Key Concern |
|------|---------------------|-------------|----------------|-------------|
| 2 | Duodenal obstruction | 99.70% | L5 | Mechanical pathology; no pharmacological rationale. Only 1 unrelated case report. |
| 3 | Duodenal ulcer | 99.59% | L5 | Acid/H. pylori-mediated disease; digoxin GI toxicity may worsen symptoms. Literature describes drug interactions/toxicity, not therapeutic use. |
| 4 | Duodenogastric reflux | 99.53% | L5 | GI motility disorder; digoxin's vagotonic GI effects are adverse, not therapeutic. No literature. |
| 5 | Susceptibility to ischaemic stroke (obsolete term) | 99.29% | L5 | Obsolete ontology term; evidence suggests digoxin **increases** stroke risk (OR 1.2–1.6). |
| 6 | Hypoalphalipoproteinaemia | 99.20% | L5 | Lipid metabolism disorder; no known intersection with Na⁺/K⁺-ATPase inhibition. No evidence. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) represents a **pharmacological contra-indication** rather than a therapeutic opportunity — digoxin's mechanism of increasing intracellular calcium in vascular smooth muscle would theoretically exacerbate coronary vasospasm. All six predicted indications lack clinical trial support, and the existing literature does not substantiate any therapeutic application. The uniformly high TxGNN scores across unrelated disease domains (cardiac, GI, cerebrovascular, metabolic) suggest the model is capturing digoxin's broad pharmacological footprint in the knowledge graph rather than identifying genuine repurposing candidates.

**To proceed, the following would be needed:**
- Detailed mechanism of action review from DrugBank to confirm or refute any off-target effects that could be therapeutically relevant
- Package insert safety data (key warnings, contraindications, DDIs) for comprehensive risk assessment
- Complete Malaysia registration details (NPRA licence data)
- If any indication were to advance, preclinical evidence of a plausible therapeutic mechanism would be required before clinical consideration

---

> *Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before any therapeutic application. TxGNN model predictions should be interpreted in conjunction with expert pharmacological and clinical review.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

