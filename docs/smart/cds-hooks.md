---
layout: default
title: Reka Bentuk Seni Bina CDS Hooks
parent: SMART on FHIR
nav_order: 11
description: "Reka bentuk seni bina CDS Hooks untuk sokongan keputusan klinikal MyTxGNN"
permalink: /smart/cds-hooks/
---

# Reka Bentuk Seni Bina CDS Hooks

<p class="key-answer" data-question="Apakah CDS Hooks?">
<strong>CDS Hooks</strong> adalah spesifikasi HL7 untuk menyepadukan perkhidmatan sokongan keputusan klinikal (CDS) dengan aliran kerja EHR. Ia membolehkan sistem luaran memberikan cadangan semasa titik keputusan klinikal.
</p>

---

## Gambaran Keseluruhan Seni Bina

```
┌────────────────────────────────────────────────────────────────┐
│                        Sistem EHR                              │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                    Aliran Kerja Klinikal                 │ │
│  │                                                          │ │
│  │   [Lihat Pesakit] → [Preskripsi] → [Tandatangan Order]  │ │
│  │         │                │                │              │ │
│  │         ▼                ▼                ▼              │ │
│  │    patient-view    order-select    order-sign           │ │
│  │         │                │                │              │ │
│  └─────────┴────────────────┴────────────────┴──────────────┘ │
│                             │                                  │
│                     CDS Hooks Client                           │
└─────────────────────────────┬──────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌─────────────────────────┐    ┌─────────────────────────┐
│    MyTxGNN CDS Service  │    │   Perkhidmatan CDS Lain │
│                         │    │                         │
│  ┌───────────────────┐  │    │  ┌───────────────────┐  │
│  │ Discovery Endpoint│  │    │  │ Discovery Endpoint│  │
│  │ GET /cds-services │  │    │  │ GET /cds-services │  │
│  └───────────────────┘  │    │  └───────────────────┘  │
│                         │    │                         │
│  ┌───────────────────┐  │    │  ┌───────────────────┐  │
│  │ Service Endpoint  │  │    │  │ Service Endpoint  │  │
│  │POST /cds-services/│  │    │  │POST /cds-services/│  │
│  │    {service-id}   │  │    │  │    {service-id}   │  │
│  └───────────────────┘  │    │  └───────────────────┘  │
└─────────────────────────┘    └─────────────────────────┘
```

---

## Hooks yang Disokong

### 1. patient-view

Dicetuskan apabila doktor membuka rekod pesakit.

| Aspek | Nilai |
|-------|-------|
| **Titik Pencetus** | Buka carta pesakit |
| **Tujuan** | Amaran awal, ringkasan |
| **Konteks** | `patientId`, `userId` |

**Contoh MyTxGNN**:

```json
{
  "cards": [
    {
      "summary": "Calon Penggunaan Semula Dikesan",
      "detail": "3 ubat pesakit mempunyai ramalan penggunaan semula keyakinan tinggi",
      "indicator": "info",
      "source": {
        "label": "MyTxGNN"
      }
    }
  ]
}
```

### 2. order-select

Dicetuskan apabila doktor memilih ubat untuk preskripsi.

| Aspek | Nilai |
|-------|-------|
| **Titik Pencetus** | Pilih ubat |
| **Tujuan** | Cadangan, amaran awal |
| **Konteks** | `selections`, `draftOrders` |

### 3. order-sign

Dicetuskan sebelum doktor menandatangani pesanan.

| Aspek | Nilai |
|-------|-------|
| **Titik Pencetus** | Tandatangan pesanan |
| **Tujuan** | Amaran kritikal, pengesahan |
| **Konteks** | `draftOrders` |

---

## Reka Bentuk Perkhidmatan MyTxGNN

### Discovery Response

```json
{
  "services": [
    {
      "hook": "patient-view",
      "id": "mytxgnn-patient-summary",
      "title": "MyTxGNN Patient Summary",
      "description": "Shows drug repurposing opportunities for patient's current medications",
      "prefetch": {
        "medications": "MedicationRequest?patient={{context.patientId}}&status=active"
      }
    },
    {
      "hook": "order-select",
      "id": "mytxgnn-drug-info",
      "title": "MyTxGNN Drug Information",
      "description": "Shows repurposing predictions for selected drug",
      "prefetch": {
        "medications": "MedicationRequest?patient={{context.patientId}}&status=active"
      }
    }
  ]
}
```

### Prefetch

Prefetch membolehkan perkhidmatan CDS meminta data yang diperlukan dalam permintaan hook:

```json
{
  "prefetch": {
    "patient": "Patient/{{context.patientId}}",
    "medications": "MedicationRequest?patient={{context.patientId}}&status=active",
    "conditions": "Condition?patient={{context.patientId}}&clinical-status=active"
  }
}
```

---

## Aliran Permintaan

### 1. Permintaan Hook

```http
POST /cds-services/mytxgnn-drug-info
Content-Type: application/json

{
  "hook": "order-select",
  "hookInstance": "abc-123",
  "context": {
    "userId": "Practitioner/dr-smith",
    "patientId": "Patient/john-doe",
    "selections": ["MedicationRequest/draft-1"]
  },
  "prefetch": {
    "medications": {
      "resourceType": "Bundle",
      "entry": [...]
    }
  }
}
```

### 2. Pemprosesan

```python
def process_hook(request):
    # 1. Ekstrak konteks
    patient_id = request['context']['patientId']
    selections = request['context']['selections']

    # 2. Dapatkan ubat dari prefetch atau query
    medications = request.get('prefetch', {}).get('medications')
    if not medications:
        medications = fetch_medications(patient_id)

    # 3. Cari ramalan MyTxGNN
    predictions = get_repurposing_predictions(medications)

    # 4. Jana kad
    cards = generate_cards(predictions)

    return {"cards": cards}
```

### 3. Respons

```json
{
  "cards": [
    {
      "uuid": "card-1",
      "summary": "Prednisolone: 15 ramalan penggunaan semula",
      "detail": "Prednisolone mempunyai 15 indikasi berpotensi dengan skor ≥0.7, termasuk rinitis alahan dan asma.",
      "indicator": "info",
      "source": {
        "label": "MyTxGNN",
        "url": "https://mytxgnn.yao.care"
      },
      "links": [
        {
          "label": "Lihat laporan penuh",
          "url": "https://mytxgnn.yao.care/drugs/prednisolone/",
          "type": "absolute"
        }
      ]
    }
  ]
}
```

---

## Struktur Kad

| Medan | Jenis | Penerangan |
|-------|-------|------------|
| `uuid` | string | Pengenalan unik kad |
| `summary` | string | Tajuk ringkas (< 140 aksara) |
| `detail` | string | Penerangan terperinci (markdown) |
| `indicator` | code | `info`, `warning`, `critical` |
| `source` | object | Sumber maklumat |
| `suggestions` | array | Cadangan tindakan |
| `links` | array | Pautan luaran |

---

## Pelaksanaan

### Teknologi

| Komponen | Pilihan |
|----------|---------|
| **Pelayan** | Flask, FastAPI, Express |
| **Pangkalan Data** | PostgreSQL, Redis (cache) |
| **FHIR Client** | fhirclient, hapi-fhir |

### Contoh Pelayan (FastAPI)

```python
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class CDSRequest(BaseModel):
    hook: str
    hookInstance: str
    context: dict
    prefetch: dict = None

@app.get("/cds-services")
async def discovery():
    return {
        "services": [
            {
                "hook": "patient-view",
                "id": "mytxgnn-summary",
                "title": "MyTxGNN Summary"
            }
        ]
    }

@app.post("/cds-services/mytxgnn-summary")
async def patient_summary(request: CDSRequest):
    patient_id = request.context.get("patientId")
    # Logik pemprosesan...
    return {
        "cards": [
            {
                "summary": "Ringkasan MyTxGNN",
                "detail": "...",
                "indicator": "info",
                "source": {"label": "MyTxGNN"}
            }
        ]
    }
```

---

## Pengujian

### CDS Hooks Sandbox

Gunakan [sandbox.cds-hooks.org](https://sandbox.cds-hooks.org/) untuk menguji perkhidmatan:

1. Masukkan URL discovery: `https://mytxgnn.yao.care/cds-services`
2. Pilih hook (cth. patient-view)
3. Konfigurasi konteks
4. Lihat respons kad

---

## Amalan Terbaik

<ol class="actionable-steps">
<li><strong>Prestasi</strong>: Respons dalam < 500ms</li>
<li><strong>Relevansi</strong>: Hanya papar kad yang bermakna</li>
<li><strong>Kejelasan</strong>: Gunakan bahasa mudah difahami</li>
<li><strong>Tindakan</strong>: Sertakan cadangan yang boleh dilaksanakan</li>
<li><strong>Pengendalian Ralat</strong>: Kembalikan senarai kad kosong jika tiada amaran</li>
</ol>

---

## Sumber Rujukan

| Sumber | Pautan |
|--------|--------|
| CDS Hooks Spec | [cds-hooks.org](https://cds-hooks.org/) |
| CDS Hooks Sandbox | [sandbox.cds-hooks.org](https://sandbox.cds-hooks.org/) |
| HL7 CDS Hooks IG | [hl7.org/fhir/cds-hooks](https://hl7.org/fhir/cds-hooks/) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Dokumentasi seni bina ini adalah untuk <strong>rujukan reka bentuk</strong>. Pelaksanaan CDS untuk kegunaan klinikal memerlukan pengujian dan pengesahan yang teliti.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
