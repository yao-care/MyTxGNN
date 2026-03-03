---
layout: default
title: Low Evidence (L4-L5)
parent: Drug Reports
nav_order: 3
has_children: true
description: "L4-L5 drug repurposing candidates with limited clinical evidence, primarily AI predictions."
permalink: /evidence-low/
---

# Low Evidence Drugs

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Exploratory candidates requiring substantial validation
</p>

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L4** | Case reports or preclinical only | Very limited evidence, exploratory research |
| **L5** | AI prediction only, no clinical evidence | Hypothesis generation, needs validation |

---

## Drug List

{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}
{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L4 Level ({{ l4_drugs.size }} drugs)

| Drug Name | Predictions | Link |
|-----------|-------------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l4_drugs.size == 0 %}
*L4 drug reports are being prepared.*
{% endif %}

### L5 Level ({{ l5_drugs.size }} drugs)

| Drug Name | Predictions | Link |
|-----------|-------------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l5_drugs.size == 0 %}
*L5 drug reports are being prepared.*
{% endif %}

---

## Understanding L4-L5 Evidence

### L4: Case Reports & Preclinical

- Individual case reports in literature
- Animal model studies
- In vitro experiments
- Mechanism-based hypotheses

### L5: AI Prediction Only

- TxGNN model prediction without clinical validation
- Based on knowledge graph relationships
- High prediction score but no human studies
- Starting point for research hypothesis

---

## Value of L5 Predictions

While L5 represents the lowest evidence level, high-scoring L5 predictions can be valuable:

1. **Hypothesis Generation**: Identify novel drug-disease relationships
2. **Research Prioritization**: Focus resources on promising candidates
3. **Grant Applications**: Support funding requests for validation studies
4. **Literature Mining**: Guide systematic literature searches

---

## Pathway to Higher Evidence

L4-L5 candidates can advance through:

| Current | Next Step | Action Required |
|---------|-----------|-----------------|
| L5 | L4 | Publish case report or preclinical study |
| L4 | L3 | Complete Phase 1/2 trial or cohort study |
| L3 | L2 | Complete RCT or Phase 2 trial |
| L2 | L1 | Complete Phase 3 or systematic review |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
L4-L5 evidence levels indicate very limited or no clinical validation. These predictions are for research hypothesis generation only. Do not use for clinical decisions without substantial further research.
</div>
