---
layout: default
title: Dokumentasi Teknikal
parent: SMART on FHIR
nav_order: 2
description: "Dokumentasi teknikal untuk integrasi SMART on FHIR MyTxGNN"
permalink: /smart/technical/
---

# Dokumentasi Teknikal

<p class="key-answer" data-question="Apakah keperluan teknikal untuk integrasi?">
Halaman ini menyediakan dokumentasi teknikal terperinci untuk pembangun yang ingin mengintegrasikan MyTxGNN dengan sistem EHR menggunakan standard SMART on FHIR.
</p>

---

## Seni Bina Sistem

```
┌─────────────────────────────────────────────────────────┐
│                    Sistem EHR                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Pelayan    │  │   Pelayan    │  │   Aplikasi   │  │
│  │   FHIR R4    │  │   OAuth 2.0  │  │     EHR      │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │
└─────────┼─────────────────┼─────────────────┼──────────┘
          │                 │                 │
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────┐
│              MyTxGNN SMART App                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Antara     │  │   Modul      │  │   Paparan    │  │
│  │   muka FHIR  │  │   Ramalan    │  │   Hasil      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## Aliran OAuth 2.0

### Permintaan Kebenaran

```
GET {authorization_endpoint}
  ?response_type=code
  &client_id=mytxgnn-client
  &redirect_uri=https://mytxgnn.yao.care/smart/callback
  &scope=launch openid fhirUser patient/*.read
  &state={state}
  &aud={fhir_server}
```

### Pertukaran Token

```bash
POST {token_endpoint}
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code={authorization_code}
&redirect_uri=https://mytxgnn.yao.care/smart/callback
&client_id=mytxgnn-client
```

---

## Profil FHIR

### MedicationKnowledge

MyTxGNN menggunakan sumber `MedicationKnowledge` untuk menyimpan maklumat ubat:

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
  },
  "status": "active",
  "indicationGuideline": [...]
}
```

### ClinicalUseDefinition

Ramalan disimpan dalam sumber `ClinicalUseDefinition`:

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
      "text": "Allergic Rhinitis"
    }
  }
}
```

---

## Endpoint API

| Method | Endpoint | Penerangan |
|--------|----------|------------|
| GET | `/fhir/metadata` | Penyata keupayaan |
| GET | `/fhir/MedicationKnowledge/{id}` | Dapatkan ubat |
| GET | `/fhir/MedicationKnowledge?code={drugbank_id}` | Cari ubat |
| GET | `/fhir/ClinicalUseDefinition?subject=MedicationKnowledge/{id}` | Dapatkan ramalan |

---

## Kod Contoh

### JavaScript (fhir.js)

```javascript
const client = FHIR.client({
  serverUrl: "https://mytxgnn.yao.care/fhir"
});

// Dapatkan maklumat ubat
const medication = await client.read({
  resourceType: "MedicationKnowledge",
  id: "db00860"
});

// Cari ramalan
const predictions = await client.search({
  resourceType: "ClinicalUseDefinition",
  searchParams: {
    subject: "MedicationKnowledge/db00860"
  }
});
```

### Python

```python
from fhirclient import client
from fhirclient.models import medicationknowledge

settings = {
    'app_id': 'mytxgnn',
    'api_base': 'https://mytxgnn.yao.care/fhir'
}

smart = client.FHIRClient(settings=settings)

# Dapatkan ubat
med = medicationknowledge.MedicationKnowledge.read('db00860', smart.server)
print(med.code.coding[0].display)
```

---

## Pengendalian Ralat

| Kod HTTP | Maksud | Penyelesaian |
|----------|--------|--------------|
| 400 | Permintaan tidak sah | Semak parameter |
| 401 | Tidak dibenarkan | Dapatkan semula token |
| 404 | Tidak dijumpai | Semak ID sumber |
| 429 | Terlalu banyak permintaan | Tunggu dan cuba semula |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Dokumentasi teknikal ini adalah untuk <strong>tujuan pembangunan dan integrasi</strong>. Sila rujuk pasukan IT anda untuk keperluan keselamatan dan pematuhan khusus.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
