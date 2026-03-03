---
layout: default
title: Spesifikasi FHIR API
parent: SMART on FHIR
nav_order: 6
description: "Spesifikasi lengkap FHIR R4 API untuk MyTxGNN"
permalink: /smart/fhir-api/
---

# Spesifikasi FHIR API

<p class="key-answer" data-question="Apakah endpoint FHIR yang tersedia?">
MyTxGNN menyediakan API FHIR R4 untuk mengakses data ubat dan ramalan penggunaan semula. Halaman ini mendokumentasikan semua endpoint yang tersedia.
</p>

---

## Maklumat Asas

| Item | Nilai |
|------|-------|
| **Base URL** | `https://mytxgnn.yao.care/fhir` |
| **Versi FHIR** | R4 (4.0.1) |
| **Format** | JSON (application/fhir+json) |
| **Pengesahan** | Tidak diperlukan untuk akses baca |

---

## Endpoint

### CapabilityStatement

Dapatkan keupayaan pelayan FHIR.

```
GET /fhir/metadata
```

**Respons**: `CapabilityStatement` yang mendokumentasikan sumber dan operasi yang disokong.

[Lihat Contoh]({{ '/fhir/metadata' | relative_url }}){: .btn .btn-primary }

---

### MedicationKnowledge

Maklumat ubat termasuk ID DrugBank, nama, dan indikasi.

#### Dapatkan Ubat Tunggal

```
GET /fhir/MedicationKnowledge/{id}
```

**Parameter**:
- `id`: ID DrugBank (cth. db00860)

**Contoh**:
```bash
curl https://mytxgnn.yao.care/fhir/MedicationKnowledge/db00860.json
```

**Respons**:
```json
{
  "resourceType": "MedicationKnowledge",
  "id": "db00860",
  "meta": {
    "profile": ["http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"]
  },
  "code": {
    "coding": [{
      "system": "https://go.drugbank.com/drugs/",
      "code": "DB00860",
      "display": "Prednisolone"
    }]
  },
  "status": "active",
  "indicationGuideline": [
    {
      "indication": [{
        "reference": {
          "reference": "ClinicalUseDefinition/db00860-allergic-rhinitis"
        }
      }]
    }
  ]
}
```

---

### ClinicalUseDefinition

Ramalan penggunaan semula ubat.

#### Dapatkan Ramalan Tunggal

```
GET /fhir/ClinicalUseDefinition/{id}
```

**Parameter**:
- `id`: Format `{drugbank_id}-{disease_slug}` (cth. db00860-allergic-rhinitis)

**Contoh**:
```bash
curl https://mytxgnn.yao.care/fhir/ClinicalUseDefinition/db00860-allergic-rhinitis.json
```

**Respons**:
```json
{
  "resourceType": "ClinicalUseDefinition",
  "id": "db00860-allergic-rhinitis",
  "type": "indication",
  "subject": [{
    "reference": "MedicationKnowledge/db00860"
  }],
  "indication": {
    "diseaseSymptomProcedure": {
      "concept": {
        "text": "Allergic Rhinitis"
      }
    }
  },
  "extension": [{
    "url": "https://mytxgnn.yao.care/fhir/StructureDefinition/prediction-score",
    "valueDecimal": 0.85
  }]
}
```

---

## Struktur Data

### MedicationKnowledge

| Medan | Jenis | Penerangan |
|-------|-------|------------|
| `id` | string | ID DrugBank (huruf kecil) |
| `code.coding[0].code` | string | ID DrugBank (huruf besar) |
| `code.coding[0].display` | string | Nama ubat |
| `status` | code | Sentiasa "active" |
| `indicationGuideline` | array | Senarai indikasi |

### ClinicalUseDefinition

| Medan | Jenis | Penerangan |
|-------|-------|------------|
| `id` | string | Format: `{drug}-{disease}` |
| `type` | code | Sentiasa "indication" |
| `subject[0].reference` | string | Rujukan ke MedicationKnowledge |
| `indication.diseaseSymptomProcedure.concept.text` | string | Nama penyakit |

---

## Kod Status HTTP

| Kod | Maksud |
|-----|--------|
| 200 | Berjaya |
| 404 | Sumber tidak dijumpai |
| 500 | Ralat pelayan |

---

## Had Kadar

| Jenis | Had |
|-------|-----|
| Per minit | 60 permintaan |
| Per jam | 1,000 permintaan |
| Per hari | 10,000 permintaan |

---

## Contoh Kod

### JavaScript

```javascript
async function getDrugInfo(drugId) {
  const response = await fetch(
    `https://mytxgnn.yao.care/fhir/MedicationKnowledge/${drugId}.json`
  );
  return response.json();
}

// Penggunaan
const prednisolone = await getDrugInfo('db00860');
console.log(prednisolone.code.coding[0].display);
```

### Python

```python
import requests

def get_drug_info(drug_id):
    url = f"https://mytxgnn.yao.care/fhir/MedicationKnowledge/{drug_id}.json"
    response = requests.get(url)
    return response.json()

# Penggunaan
prednisolone = get_drug_info('db00860')
print(prednisolone['code']['coding'][0]['display'])
```

---

<div class="disclaimer">
<strong>Penafian</strong><br>
API ini adalah untuk <strong>tujuan penyelidikan sahaja</strong>. Jangan gunakan untuk keputusan klinikal tanpa pengesahan lanjut.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
