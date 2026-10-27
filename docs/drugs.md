---
layout: default
title: Senarai Ubat
parent: Laporan Ubat
nav_order: 4
description: "Browse all drugs with drug repurposing predictions from MyTxGNN"
permalink: /drugs/
---
{%- comment -%}2026-10-27 build gate：站上各頁的藥物數讀 site.data.drug_stats；它和實際公開藥物頁數／等級分布不一致時，
故意 include 不存在的檔讓 Jekyll 建置失敗，錯誤訊息即修法。{%- endcomment -%}
{%- assign gate_listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign gate_ds = site.data.drug_stats -%}
{%- assign gate_l1 = gate_listed | where: "evidence_level", "L1" | size -%}
{%- assign gate_l2 = gate_listed | where: "evidence_level", "L2" | size -%}
{%- assign gate_l3 = gate_listed | where: "evidence_level", "L3" | size -%}
{%- assign gate_l4 = gate_listed | where: "evidence_level", "L4" | size -%}
{%- assign gate_l5 = gate_listed | where: "evidence_level", "L5" | size -%}
{%- if gate_listed.size != gate_ds.total_drugs or gate_l1 != gate_ds.level_counts.L1 or gate_l2 != gate_ds.level_counts.L2 or gate_l3 != gate_ds.level_counts.L3 or gate_l4 != gate_ds.level_counts.L4 or gate_l5 != gate_ds.level_counts.L5 -%}
{% include ERROR-docs-data-drug_stats-json-out-of-sync--run-python3-scripts-generate_drug_stats-py.html %}
{%- endif %}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" %}

# Drug Predictions

Browse drugs analyzed by MyTxGNN with their predicted new indications.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Drugs Analyzed | {{ site.data.drug_stats.total_drugs }} |
| Predictions listed on this site (score ≥0.99, up to 10 per drug) | {{ site.data.site_stats.indications }} |
| Unique Diseases | 17,041 |

---

## Top Drugs by Prediction Count

The following drugs have the most predicted new indications from the TxGNN deep learning model:

| Rank | Drug | DrugBank ID | Predictions | Sample Brand |
|------|------|-------------|-------------|--------------|
| 1 | **Prednisolone** | DB00860 | 3,650 | Predsone Syrup |
| 2 | **Betamethasone** | DB00443 | 3,198 | Betamethasone-G Tablet |
| 3 | **Fusidic Acid** | DB02703 | 3,008 | Defuzin Cream |
| 4 | **Hydrocortisone Acetate** | DB14539 | 2,880 | Hydrosone Cream |
| 5 | **Hydrocortisone** | DB00741 | 2,780 | Proctosedyl Ointment |
| 6 | **Dexamethasone** | DB01234 | 2,736 | SW-Dexasone Tablet |
| 7 | **Ketoconazole** | DB01026 | 759 | Funginox Tablet |
| 8 | **Ofloxacin** | DB01165 | 690 | Oflicin-100 Tablet |
| 9 | **Triamcinolone** | DB00620 | 645 | Trinolone Cream |
| 10 | **Mometasone Furoate** | DB14512 | 640 | Vizomet Ointment |
| 11 | **Salicylic Acid** | DB00936 | 567 | Sebitar Scalp Treatment |
| 12 | **Clotrimazole** | DB00257 | 549 | Mycoril Spray |
| 13 | **Fluticasone Propionate** | DB00588 | 540 | Flutinide Nasal Spray |
| 14 | **Simvastatin** | DB00641 | 528 | SimvaHEXAL Tablet |
| 15 | **Zinc Oxide** | DB09321 | 504 | Polylab Zinc Paste |
| 16 | **Metronidazole** | DB00916 | 425 | B. Braun Metronidazole |
| 17 | **Paclitaxel** | DB01229 | 370 | Paxus PM Injection |
| 18 | **Ibuprofen** | DB01050 | 360 | Nurofen for Children |
| 19 | **Telmisartan** | DB00966 | 348 | Telmidip Tablets |
| 20 | **Cyanocobalamin** | DB00115 | 320 | Hovid Neurovit Injection |

---

## Drug Categories

### Corticosteroids (High Prediction Count)

Corticosteroids dominate the prediction list due to their broad anti-inflammatory mechanisms:

- Prednisolone (3,650 predictions)
- Betamethasone (3,198 predictions)
- Hydrocortisone Acetate (2,880 predictions)
- Hydrocortisone (2,780 predictions)
- Dexamethasone (2,736 predictions)
- Triamcinolone (645 predictions)
- Mometasone Furoate (640 predictions)

### Antifungals

- Fusidic Acid (3,008 predictions)
- Ketoconazole (759 predictions)
- Clotrimazole (549 predictions)

### Antibiotics

- Ofloxacin (690 predictions)
- Metronidazole (425 predictions)

### Cardiovascular

- Simvastatin (528 predictions)
- Telmisartan (348 predictions)

### Oncology

- Paclitaxel (370 predictions)

---

## Data Access

### FHIR API

Access drug and prediction data via FHIR R4 API:

- **Capability Statement**: [`/fhir/metadata`]({{ '/fhir/metadata' | relative_url }})
- **MedicationKnowledge**: `/fhir/MedicationKnowledge/{drugbank_id}`
- **ClinicalUseDefinition**: `/fhir/ClinicalUseDefinition/{drug}-{indication}`

### Downloads

Full prediction data available for download:

- [DrugBank Mapping CSV]({{ '/downloads/' | relative_url }}) - Drug ID mappings

---

## Search Tips

1. **By Drug Name**: Search for the generic drug name (e.g., "Metformin")
2. **By DrugBank ID**: Use the DrugBank identifier (e.g., "DB00331")
3. **By Disease**: Search for disease name to find drugs with predictions for that condition

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Drug repurposing predictions are for research purposes only. These predictions have not been validated clinically and do not constitute medical recommendations. Always consult healthcare professionals for medical decisions.
</div>

---

## Senarai Penuh Ubat

{{ listed_drugs.size }} laporan ubat

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Ubat | Tahap bukti | Indikasi |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}
