---
layout: default
title: High Evidence (L1-L2)
parent: Laporan Ubat
nav_order: 1
has_children: true
description: "L1-L2 drug repurposing candidates with strong clinical trial or systematic review evidence."
permalink: /evidence-high/
---

# High Evidence Drugs

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Priority candidates for clinical evaluation
</p>

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | Strong support, consider clinical use |
| **L2** | Single RCT or multiple Phase 2 trials | Moderate support, design validation trials |

---

## Drug List

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 Level ({{ l1_drugs.size }} drugs)

| Drug Name | Predictions | Link |
|-----------|-------------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l1_drugs.size == 0 %}
*L1 drug reports are being prepared. Evidence collection in progress.*
{% endif %}

### L2 Level ({{ l2_drugs.size }} drugs)

| Drug Name | Predictions | Link |
|-----------|-------------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l2_drugs.size == 0 %}
*L2 drug reports are being prepared. Evidence collection in progress.*
{% endif %}

---

## How Evidence Levels Are Determined

Evidence levels are assigned based on the quality and quantity of clinical evidence:

1. **Clinical Trials**: Phase 3 RCTs carry the highest weight
2. **Systematic Reviews**: Meta-analyses of multiple studies
3. **Study Design**: Randomized controlled trials > observational studies
4. **Sample Size**: Larger studies provide stronger evidence

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Drug repurposing predictions are for research purposes only. These predictions have not been clinically validated and should not be used for medical decisions. Always consult healthcare professionals.
</div>
