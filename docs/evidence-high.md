---
layout: default
title: High Evidence (L1-L2)
parent: Laporan Ubat
nav_order: 1
has_children: true
description: "39 ubat pada tahap bukti L1–L2 di laman ini (Malaysia), cth. Acetylcysteine, Bendamustine Hydrochloride, Bupropion, dengan indikasi ramalan utama, pendaftaran NPRA dan log semakan bagi setiap ubat."
permalink: /evidence-high/
---

# High Evidence Drugs

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Halaman ini menyenaraikan **{{ site.data.evidence_tier_facts.high.count }}** daripada **{{ site.data.drug_stats.total_drugs }}** ubat yang mempunyai laporan di laman ini ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Median bahagian L1–L2 di 30 laman TxGNN: {{ site.data.evidence_tier_facts.high.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Laman ini di atas median.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Laman ini di bawah median.{% else %}Laman ini sama dengan median.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
Dalam data tempatan (pendaftaran NPRA), **{{ site.data.evidence_tier_facts.high.with_current }}** daripada ubat ini mempunyai sekurang-kurangnya satu pendaftaran sah, **{{ site.data.evidence_tier_facts.high.none_current }}** mempunyai pendaftaran tetapi tiada yang sah, dan **{{ site.data.evidence_tier_facts.high.without_data }}** tiada dalam data tempatan. **{{ site.data.evidence_tier_facts.high.with_reviews }}** mempunyai catatan dalam log semakan (pembetulan maklumat pendaftaran di halaman ubat). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** mempunyai indikasi ramalan yang tidak disenaraikan oleh laman TxGNN lain untuk ubat yang sama.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Ada pendaftaran tetapi tiada yang sah: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Takrif semua tahap: [Metodologi]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Priority candidates for clinical evaluation
</p>

Ubat yang manakah mempunyai bukti ujian bagi indikasi baharu yang diramalkan, dan berapa banyak ujian berdaftar dipetik? Lihat [Ubat di Malaysia dengan bukti ujian klinikal untuk indikasi baharu]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Evidence Standards

| Level | Definition | Clinical Significance |
|-------|------------|----------------------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | Strong support, consider clinical use |
| **L2** | Single RCT or multiple Phase 2 trials | Moderate support, design validation trials |

---

## Drug List

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 Level ({{ site.data.evidence_tier_facts.high.by_level.L1 }} drugs)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Ubat | Tahap | Indikasi baharu utama diramal | pendaftaran NPRA: sah / jumlah | Log semakan | Hanya di laman ini |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ya ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

{% if l1_drugs.size == 0 %}
*L1 drug reports are being prepared. Evidence collection in progress.*
{% endif %}

### L2 Level ({{ site.data.evidence_tier_facts.high.by_level.L2 }} drugs)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Ubat | Tahap | Indikasi baharu utama diramal | pendaftaran NPRA: sah / jumlah | Log semakan | Hanya di laman ini |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ya ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

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
