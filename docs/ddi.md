---
layout: default
title: Drug-Drug Interactions
parent: Safety Data
nav_order: 1
description: "MyTxGNN drug-drug interaction database for assessing drug repurposing safety."
permalink: /ddi/
---

# Drug-Drug Interactions (DDI)

<p class="key-answer" data-question="What DDI data does MyTxGNN have?">
This platform integrates drug interaction data from <strong>DDInter 2.0</strong> and <strong>Guide to PHARMACOLOGY</strong> to help researchers consider safety factors when evaluating drug repurposing candidates.
</p>

<div class="key-takeaway">
Drug interactions are a critical consideration for drug repurposing. When a drug is used for a new indication, it may need to be combined with standard treatments for that disease. Understanding potential DDI risks is essential.
</div>

---

## Data Sources

<table class="comparison-table">
<thead>
<tr><th>Data Source</th><th>DDI Records</th><th>Drugs Covered</th><th>Update</th></tr>
</thead>
<tbody>
<tr>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
  <td>222,391</td>
  <td>2,310</td>
  <td>2026-02</td>
</tr>
<tr>
  <td><a href="https://www.guidetopharmacology.org/" target="_blank" rel="noopener">Guide to PHARMACOLOGY</a></td>
  <td>4,636</td>
  <td>2,156</td>
  <td>2026-02 (v2025.4)</td>
</tr>
</tbody>
</table>

---

## DDI Severity Levels

<p class="key-answer" data-question="What are the drug interaction severity levels?">
Drug interactions are classified into three levels based on severity, from Major to Minor, each with different clinical management recommendations.
</p>

| Level | English | Description | Recommended Action |
|-------|---------|-------------|-------------------|
| **Severe** | Major | May be life-threatening or cause permanent harm | Avoid combination, find alternatives |
| **Moderate** | Moderate | May require dose adjustment or close monitoring | Use with caution, monitor adverse reactions |
| **Mild** | Minor | Low clinical significance | Generally safe to combine, monitor if needed |

---

## How to Use DDI Data

### In Drug Reports

Each drug report's "Safety Considerations" section includes important drug interaction information.

<ol class="actionable-steps">
<li>Go to the <a href="{{ '/drugs/' | relative_url }}">Drug List</a> and find your target drug</li>
<li>Scroll to the "Safety Considerations" section in the report</li>
<li>Review the drug's DDI alerts and contraindications</li>
</ol>

### Download Full Dataset

Need large-scale analysis? Download the raw DDI data from GitHub:

| Data | Description | Link |
|------|-------------|------|
| DDInter Data | Complete DDI reference table | [GitHub](https://github.com/yao-care/MyTxGNN/tree/main/data/external/ddi) |
| Pharmacology Data | Approved drug interactions | [GitHub](https://github.com/yao-care/MyTxGNN/tree/main/data/external/ddi) |

---

## Why DDI Matters for Drug Repurposing

<blockquote class="expert-quote">
"Drug repurposing research must evaluate not only efficacy but also drug interactions in the new indication context. Many drug repurposing failures occur precisely because interactions with standard treatment drugs are overlooked."
<cite>— Drug Safety Assessment Principles</cite>
</blockquote>

### DDI Considerations in Drug Repurposing

1. **Standard Treatment Drugs**: New indications typically have existing standard treatments; assess combination risks
2. **Patient Population Differences**: Different diseases have different comorbidities and medication habits
3. **Dose Adjustment Needs**: Some DDIs can be managed through dose adjustment rather than complete avoidance

---

## Common DDI Scenarios

### Corticosteroids (e.g., Prednisolone)

| Interaction | Drug Class | Severity | Note |
|-------------|------------|----------|------|
| NSAIDs | Anti-inflammatory | Moderate | Increased GI bleeding risk |
| Warfarin | Anticoagulant | Moderate | May alter INR |
| Diuretics | Cardiovascular | Moderate | Enhanced hypokalemia |

### Statins (e.g., Simvastatin)

| Interaction | Drug Class | Severity | Note |
|-------------|------------|----------|------|
| CYP3A4 Inhibitors | Various | Major | Increased myopathy risk |
| Fibrates | Lipid-lowering | Moderate | Enhanced myopathy risk |
| Grapefruit juice | Food | Moderate | Increased drug levels |

---

## Related Resources

| Resource | Description | Link |
|----------|-------------|------|
| Drug List | View individual drug reports | [Go]({{ '/drugs/' | relative_url }}) |
| Methodology | Understanding evidence levels | [Go]({{ '/methodology/' | relative_url }}) |
| Data Sources | Complete data source information | [Go]({{ '/sources/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
DDI data on this page is for research reference only and <strong>does not constitute medication advice</strong>. Actual medication decisions should consult professional pharmacists or physicians. The clinical impact of drug interactions varies by individual factors.
<br><br>
<small>Last reviewed: 2026-03-03 | Reviewer: MyTxGNN Research Team</small>
</div>
