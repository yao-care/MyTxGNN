---
layout: default
title: Low Evidence (L4-L5)
parent: Laporan Ubat
nav_order: 3
has_children: true
description: "523 ubat pada tahap bukti L5 di laman ini (Malaysia), cth. Ascorbic Acid, Cholecalciferol, Folic Acid, dengan indikasi ramalan utama, pendaftaran NPRA dan log semakan bagi setiap ubat."
permalink: /evidence-low/
---

# Low Evidence Drugs

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Halaman ini menyenaraikan **{{ site.data.evidence_tier_facts.low.count }}** daripada **{{ site.data.drug_stats.total_drugs }}** ubat yang mempunyai laporan di laman ini ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Median bahagian L5 di 30 laman TxGNN: {{ site.data.evidence_tier_facts.low.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Laman ini di atas median.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Laman ini di bawah median.{% else %}Laman ini sama dengan median.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
Dalam data tempatan (pendaftaran NPRA), **{{ site.data.evidence_tier_facts.low.with_current }}** daripada ubat ini mempunyai sekurang-kurangnya satu pendaftaran sah, **{{ site.data.evidence_tier_facts.low.none_current }}** mempunyai pendaftaran tetapi tiada yang sah, dan **{{ site.data.evidence_tier_facts.low.without_data }}** tiada dalam data tempatan. **{{ site.data.evidence_tier_facts.low.with_reviews }}** mempunyai catatan dalam log semakan (pembetulan maklumat pendaftaran di halaman ubat). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** mempunyai indikasi ramalan yang tidak disenaraikan oleh laman TxGNN lain untuk ubat yang sama.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Ada pendaftaran tetapi tiada yang sah: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Ubat dengan pendaftaran tempatan yang sah disenaraikan dahulu.
{% endif %}

Takrif semua tahap: [Metodologi]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L4 Level ({{ l4_drugs.size }} drugs)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Ubat | Tahap | Indikasi baharu utama diramal | pendaftaran NPRA: sah / jumlah | Log semakan | Hanya di laman ini |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ya ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

{% if l4_drugs.size == 0 %}
*L4 drug reports are being prepared.*
{% endif %}

### L5 Level ({{ site.data.evidence_tier_facts.low.by_level.L5 }} drugs)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Ubat | Tahap | Indikasi baharu utama diramal | pendaftaran NPRA: sah / jumlah | Log semakan | Hanya di laman ini |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ya ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

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
- Graph neural network prediction (score ≥ 0.99), not a relation already recorded in the knowledge graph
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
