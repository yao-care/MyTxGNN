---
layout: default
title: Medium Evidence (L3)
parent: Laporan Ubat
nav_order: 2
has_children: true
description: "48 ubat pada tahap bukti L3–L4 di laman ini (Malaysia), cth. Acitretin, Alprazolam, Calcipotriol, dengan indikasi ramalan utama, pendaftaran NPRA dan log semakan bagi setiap ubat."
permalink: /evidence-medium/
---

# Medium Evidence Drugs

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Halaman ini menyenaraikan **{{ site.data.evidence_tier_facts.medium.count }}** daripada **{{ site.data.drug_stats.total_drugs }}** ubat yang mempunyai laporan di laman ini ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Median bahagian L3–L4 di 30 laman TxGNN: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Laman ini di atas median.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Laman ini di bawah median.{% else %}Laman ini sama dengan median.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
Dalam data tempatan (pendaftaran NPRA), **{{ site.data.evidence_tier_facts.medium.with_current }}** daripada ubat ini mempunyai sekurang-kurangnya satu pendaftaran sah, **{{ site.data.evidence_tier_facts.medium.none_current }}** mempunyai pendaftaran tetapi tiada yang sah, dan **{{ site.data.evidence_tier_facts.medium.without_data }}** tiada dalam data tempatan. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** mempunyai catatan dalam log semakan (pembetulan maklumat pendaftaran di halaman ubat). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** mempunyai indikasi ramalan yang tidak disenaraikan oleh laman TxGNN lain untuk ubat yang sama.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Ada pendaftaran tetapi tiada yang sah: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Takrif semua tahap: [Metodologi]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 Level ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} drugs)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Ubat | Tahap | Indikasi baharu utama diramal | pendaftaran NPRA: sah / jumlah | Log semakan | Hanya di laman ini |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ya ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

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
