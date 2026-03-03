---
layout: default
title: Drug-Disease Safety
parent: Safety Data
nav_order: 2
description: "MyTxGNN Drug-Disease Safety Information database for evaluating drug safety risks in specific patient populations."
permalink: /ddsi/
---

# Drug-Disease Safety Information (DDSI)

<p class="key-answer" data-question="What is DDSI?">
<strong>Drug-Disease Safety Information (DDSI)</strong> refers to warnings about drugs that may worsen conditions or cause adverse reactions in patients with specific diseases. This helps researchers consider patient comorbidities when evaluating drug repurposing candidates.
</p>

<div class="key-takeaway">
When repurposing drugs, it's essential to consider the common comorbidities of the target patient population. For example, when using a drug for cancer patients, consider their common liver and kidney function abnormalities.
</div>

---

## What is DDSI?

When drugs are used in patients with certain diseases, they may:

| Situation | Description | Example |
|-----------|-------------|---------|
| **Disease Worsening** | Drug may aggravate existing condition | NSAIDs worsening kidney function |
| **Altered Efficacy** | Disease state affects drug metabolism | Cirrhosis affecting drug clearance |
| **Increased Toxicity** | Disease makes organs more susceptible | Heart failure patients more sensitive to digoxin |
| **Symptom Masking** | Drug may hide disease signs | Beta-blockers masking hypoglycemia symptoms |

---

## Data Source

<table class="comparison-table">
<thead>
<tr><th>Item</th><th>Information</th></tr>
</thead>
<tbody>
<tr>
  <td>Data Source</td>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
</tr>
<tr>
  <td>DDSI Records</td>
  <td>8,359</td>
</tr>
<tr>
  <td>Drugs Covered</td>
  <td>115</td>
</tr>
<tr>
  <td>License</td>
  <td>CC BY-NC-SA 4.0</td>
</tr>
</tbody>
</table>

---

## DDSI Severity Levels

| Level | English | Description | Recommended Action |
|-------|---------|-------------|-------------------|
| **Severe** | Major | Absolute contraindication or life-threatening | Avoid use, find alternatives |
| **Moderate** | Moderate | May require dose adjustment or monitoring | Use with caution, monitor closely |
| **Mild** | Minor | Low clinical significance | Generally safe, monitor if needed |

---

## Common Drug-Disease Considerations

### Liver Disease

<ol class="actionable-steps">
<li><strong>Hepatotoxic drugs contraindicated</strong>: Avoid in severe liver impairment</li>
<li><strong>Dose adjustment needed</strong>: Reduce doses for hepatically metabolized drugs</li>
<li><strong>Coagulation concerns</strong>: Increased risk with anticoagulants in cirrhosis</li>
</ol>

### Kidney Disease

- Adjust doses for renally excreted drugs
- Avoid or use nephrotoxic drugs cautiously
- Monitor electrolyte changes

### Cardiovascular Disease

- Heart failure patients more sensitive to certain drugs
- QT prolongation risk drugs need arrhythmia history review
- Hypotension risk drugs need cardiovascular status assessment

---

## Application in Drug Repurposing

<blockquote class="expert-quote">
"When evaluating drug repurposing, we must consider not only whether the drug is effective for the new indication, but also the comorbidity characteristics of the target patient population to avoid safety issues."
<cite>— Drug Safety Assessment Principles</cite>
</blockquote>

### Evaluation Process

1. **Identify Target Population**: Understand common comorbidities
2. **Cross-reference DDSI Data**: Check for contraindications
3. **Risk-Benefit Assessment**: Weigh efficacy against potential risks
4. **Monitoring Plan**: Design surveillance for high-risk groups

---

## Related Resources

| Resource | Description | Link |
|----------|-------------|------|
| Drug-Drug Interactions | DDI database | [Go]({{ '/ddi/' | relative_url }}) |
| Drug-Food Interactions | DFI database | [Go]({{ '/dfi/' | relative_url }}) |
| Drug-Herb Interactions | DHI database | [Go]({{ '/dhi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
DDSI data on this page is for research reference only and <strong>does not constitute medication advice</strong>. Actual medication decisions should consult professional pharmacists or physicians. Drug effects on specific diseases vary by individual factors.
<br><br>
<small>Last reviewed: 2026-03-03 | Reviewer: MyTxGNN Research Team</small>
</div>
