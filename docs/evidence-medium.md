---
layout: default
title: Medium Evidence (L3)
parent: Laporan Ubat
nav_order: 2
has_children: true
description: "L3 drug repurposing candidates with moderate clinical evidence requiring further investigation."
permalink: /evidence-medium/
---

# Medium Evidence Drugs

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidates worth investigating with additional research
</p>

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L3** | Phase 1/2 trials or observational studies | Preliminary support, requires more research |

---

## Drug List

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}

### L3 Level ({{ l3_drugs.size }} drugs)

| Drug Name | Predictions | Link |
|-----------|-------------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [View Report]({{ drug.url | relative_url }}) |
{% endfor %}

{% if l3_drugs.size == 0 %}
*L3 drug reports are being prepared. Evidence collection in progress.*
{% endif %}

---

## What L3 Evidence Means

L3 level indicates:

- **Early-stage trials**: Phase 1 or Phase 2 studies exist
- **Observational data**: Cohort or case-control studies available
- **Mechanism support**: Preclinical evidence supports the hypothesis
- **Potential value**: Worth investigating but needs validation

### Recommended Actions for L3 Candidates

1. **Review existing literature** for mechanism of action
2. **Monitor ongoing trials** for results
3. **Consider pilot studies** if resources available
4. **Wait for Phase 3 data** before clinical implementation

---

## Transition to Higher Evidence

L3 drugs can be upgraded to L2 or L1 when:

- Phase 2/3 trial results are published
- Systematic reviews are completed
- Multiple independent studies confirm findings

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Drug repurposing predictions are for research purposes only. L3 evidence indicates preliminary support only. Clinical application requires further validation.
</div>
