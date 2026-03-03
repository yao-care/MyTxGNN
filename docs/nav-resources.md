---
layout: default
title: Sumber
nav_order: 6
has_children: true
description: "Sumber data, muat turun, dan dokumentasi untuk MyTxGNN."
---

# Sumber

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Akses data, dokumentasi, dan sumber pembelajaran
</p>

---

## Muat Turun & Data

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/downloads/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #1976D2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #1565C0;">Muat Turun</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Muat turun data ramalan dan sumber dalam format CSV/JSON</p>
</a>

<a href="{{ '/sources/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #4CAF50;">
  <h3 style="margin: 0 0 0.5rem 0; color: #388E3C;">Sumber Data</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Dokumentasi sumber data yang digunakan dalam MyTxGNN</p>
</a>

<a href="{{ '/blog/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #F57C00;">Kajian Kes</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Tutorial dan kajian kes penggunaan MyTxGNN</p>
</a>

<a href="{{ '/fhir/metadata' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">FHIR API</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Akses data melalui API FHIR R4</p>
</a>

</div>

---

## Sumber Data Utama

| Sumber | Penerangan | Pautan |
|--------|------------|--------|
| **TxGNN** | Graf pengetahuan Harvard | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) |
| **NPRA** | Pendaftaran farmaseutikal Malaysia | [data.gov.my](https://data.gov.my/data-catalogue/pharmaceutical_products) |
| **DrugBank** | Pangkalan data ubat | [drugbank.com](https://go.drugbank.com/) |
| **ClinicalTrials.gov** | Ujian klinikal | [clinicaltrials.gov](https://clinicaltrials.gov/) |
| **PubMed** | Literatur bioperubatan | [pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/) |

---

## Format Data

### CSV

```
drug_name,drugbank_id,disease,prediction_score,evidence_level
Prednisolone,DB00860,Allergic Rhinitis,0.89,L2
Betamethasone,DB00443,Asthma,0.85,L3
...
```

### FHIR JSON

```json
{
  "resourceType": "MedicationKnowledge",
  "id": "db00860",
  "code": {
    "coding": [{
      "system": "https://go.drugbank.com/drugs/",
      "code": "DB00860",
      "display": "Prednisolone"
    }]
  }
}
```

---

## Sumber Pembelajaran

| Jenis | Penerangan | Pautan |
|-------|------------|--------|
| **Tutorial** | Panduan langkah demi langkah | [Kajian Kes]({{ '/blog/' | relative_url }}) |
| **Metodologi** | Penjelasan pendekatan | [Metodologi]({{ '/methodology/' | relative_url }}) |
| **SMART on FHIR** | Panduan integrasi | [SMART]({{ '/smart/guide/' | relative_url }}) |

---

## Petikan

Jika anda menggunakan dataset atau perisian ini, sila petik:

```bibtex
@misc{mytxgnn2026,
  title={MyTxGNN: Ramalan Penggunaan Semula Ubat untuk Ubat Diluluskan NPRA di Malaysia},
  url={https://mytxgnn.yao.care},
  year={2026}
}
```

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Sumber di halaman ini adalah untuk <strong>tujuan penyelidikan</strong>. Sila semak lesen individu sebelum penggunaan komersial.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
