---
layout: default
title: Nota Teknikal ClinicalTrials.gov API v2
parent: SMART on FHIR
nav_order: 8
description: "Nota teknikal untuk menggunakan ClinicalTrials.gov API v2 dalam MyTxGNN"
permalink: /smart/clinicaltrials-api/
---

# Nota Teknikal ClinicalTrials.gov API v2

<p class="key-answer" data-question="Apakah ClinicalTrials.gov API v2?">
<strong>ClinicalTrials.gov API v2</strong> adalah API terkini dari NIH untuk mengakses data ujian klinikal. MyTxGNN menggunakan API ini untuk mengumpul bukti ujian klinikal bagi ramalan penggunaan semula ubat.
</p>

---

## Maklumat Asas API

| Item | Nilai |
|------|-------|
| **Base URL** | `https://clinicaltrials.gov/api/v2` |
| **Format** | JSON |
| **Pengesahan** | Tidak diperlukan |
| **Dokumentasi** | [clinicaltrials.gov/data-api](https://clinicaltrials.gov/data-api/api) |

---

## Endpoint Utama

### 1. Carian Kajian

```
GET /studies
```

**Parameter Utama**:

| Parameter | Penerangan | Contoh |
|-----------|------------|--------|
| `query.cond` | Keadaan/penyakit | `diabetes` |
| `query.intr` | Intervensi/ubat | `metformin` |
| `query.term` | Carian umum | `cancer treatment` |
| `filter.overallStatus` | Status kajian | `RECRUITING` |
| `pageSize` | Saiz halaman | `100` |

**Contoh Permintaan**:

```bash
curl "https://clinicaltrials.gov/api/v2/studies?query.intr=prednisolone&query.cond=allergic%20rhinitis&pageSize=10"
```

---

### 2. Kajian Tunggal

```
GET /studies/{nctId}
```

**Contoh**:

```bash
curl "https://clinicaltrials.gov/api/v2/studies/NCT01234567"
```

---

## Struktur Respons

```json
{
  "studies": [
    {
      "protocolSection": {
        "identificationModule": {
          "nctId": "NCT01234567",
          "briefTitle": "Study of Drug X for Condition Y"
        },
        "statusModule": {
          "overallStatus": "COMPLETED",
          "startDateStruct": {
            "date": "2020-01-15"
          }
        },
        "conditionsModule": {
          "conditions": ["Allergic Rhinitis"]
        },
        "armsInterventionsModule": {
          "interventions": [
            {
              "type": "DRUG",
              "name": "Prednisolone"
            }
          ]
        }
      }
    }
  ],
  "nextPageToken": "..."
}
```

---

## Penggunaan dalam MyTxGNN

### Pengumpul Bukti

MyTxGNN menggunakan `ClinicalTrialsCollector` untuk mencari ujian klinikal yang berkaitan:

```python
from txgnn.collectors.clinicaltrials import ClinicalTrialsCollector

collector = ClinicalTrialsCollector()

# Cari ujian untuk ubat dan penyakit
results = collector.search(
    drug="Prednisolone",
    disease="Allergic Rhinitis"
)

for trial in results.results:
    print(f"{trial.nct_id}: {trial.title}")
```

---

## Penapisan Status

| Status | Penerangan |
|--------|------------|
| `RECRUITING` | Sedang merekrut peserta |
| `ACTIVE_NOT_RECRUITING` | Aktif tetapi tidak merekrut |
| `COMPLETED` | Selesai |
| `TERMINATED` | Ditamatkan |
| `WITHDRAWN` | Ditarik balik |

---

## Had dan Pertimbangan

### Had Kadar

- **Tanpa API Key**: 3 permintaan/saat
- **Dengan API Key**: 10 permintaan/saat

### Amalan Terbaik

<ol class="actionable-steps">
<li>Gunakan paging untuk senarai besar (`pageToken`)</li>
<li>Cache respons untuk mengurangkan permintaan</li>
<li>Gunakan medan tertentu (`fields`) untuk respons lebih kecil</li>
<li>Tangani ralat dengan retry dan exponential backoff</li>
</ol>

---

## Perubahan dari API v1

| Aspek | v1 (Legacy) | v2 (Terkini) |
|-------|-------------|--------------|
| **Format** | XML/JSON | JSON sahaja |
| **Pagination** | offset/count | pageToken |
| **Naming** | CamelCase | Konsisten |
| **Fields** | Terhad | Komprehensif |

---

## Contoh Kod Lengkap

```python
import requests
from typing import List, Optional

class ClinicalTrialsAPI:
    BASE_URL = "https://clinicaltrials.gov/api/v2"

    def search_studies(
        self,
        drug: str,
        condition: Optional[str] = None,
        status: Optional[List[str]] = None,
        page_size: int = 20
    ) -> dict:
        params = {
            "query.intr": drug,
            "pageSize": page_size,
            "format": "json"
        }

        if condition:
            params["query.cond"] = condition

        if status:
            params["filter.overallStatus"] = ",".join(status)

        response = requests.get(
            f"{self.BASE_URL}/studies",
            params=params
        )
        response.raise_for_status()
        return response.json()

# Penggunaan
api = ClinicalTrialsAPI()
results = api.search_studies(
    drug="Prednisolone",
    condition="Asthma",
    status=["COMPLETED", "RECRUITING"]
)

for study in results.get("studies", []):
    protocol = study["protocolSection"]
    ident = protocol["identificationModule"]
    print(f"{ident['nctId']}: {ident['briefTitle']}")
```

---

## Sumber Rujukan

| Sumber | Pautan |
|--------|--------|
| Dokumentasi Rasmi | [clinicaltrials.gov/data-api](https://clinicaltrials.gov/data-api/api) |
| Panduan Migrasi v1→v2 | [clinicaltrials.gov/data-api/migration](https://clinicaltrials.gov/data-api/about-api/v1-migration) |
| GitHub Issues | [github.com/ctti-clinicaltrials](https://github.com/ctti-clinicaltrials) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Nota teknikal ini adalah untuk <strong>rujukan pembangunan</strong>. ClinicalTrials.gov API boleh berubah. Sila rujuk dokumentasi rasmi untuk maklumat terkini.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
