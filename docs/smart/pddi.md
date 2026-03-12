---
layout: default
title: Nota Teknikal HL7 PDDI-CDS IG
parent: SMART on FHIR
nav_order: 10
description: "Nota teknikal untuk HL7 Potential Drug-Drug Interaction Clinical Decision Support Implementation Guide"
permalink: /smart/pddi/
---

# Nota Teknikal HL7 PDDI-CDS IG

<p class="key-answer" data-question="Apakah PDDI-CDS IG?">
<strong>PDDI-CDS IG</strong> (Potential Drug-Drug Interaction Clinical Decision Support Implementation Guide) adalah panduan pelaksanaan HL7 FHIR untuk sokongan keputusan klinikal berkaitan interaksi ubat-ubat berpotensi.
</p>

---

## Gambaran Keseluruhan

### Tujuan PDDI-CDS

| Aspek | Penerangan |
|-------|------------|
| **Masalah** | Interaksi ubat-ubat (DDI) berbahaya |
| **Penyelesaian** | Amaran CDS yang diseragamkan |
| **Standard** | HL7 FHIR + CDS Hooks |
| **Sasaran** | Sistem EHR dan farmasi |

---

## Seni Bina

```
┌─────────────────────────────────────────────────────────┐
│                    Sistem EHR                           │
│                                                         │
│  ┌─────────────┐        ┌─────────────┐                │
│  │ Preskripsi  │───────▶│ CDS Hooks   │                │
│  │   Ubat      │        │   Client    │                │
│  └─────────────┘        └──────┬──────┘                │
└────────────────────────────────┼────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────┐
│              Perkhidmatan PDDI-CDS                      │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Pangkalan  │  │   Enjin     │  │  Penjana    │     │
│  │  Data DDI   │──│   Peraturan │──│   Kad CDS   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

---

## CDS Hooks untuk PDDI

### Hook: order-select

Dicetuskan apabila doktor memilih ubat untuk preskripsi.

**Konteks**:

```json
{
  "hook": "order-select",
  "hookInstance": "d1577c69-dfbe-44ad-ba6d-3e05e953b2ea",
  "context": {
    "userId": "Practitioner/123",
    "patientId": "Patient/456",
    "selections": ["MedicationRequest/789"],
    "draftOrders": {
      "resourceType": "Bundle",
      "entry": [
        {
          "resource": {
            "resourceType": "MedicationRequest",
            "id": "789",
            "medication": {
              "coding": [{
                "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                "code": "197361"
              }]
            }
          }
        }
      ]
    }
  }
}
```

### Respons: Kad Amaran

```json
{
  "cards": [
    {
      "uuid": "card-1",
      "summary": "Interaksi Ubat-Ubat Berpotensi",
      "detail": "Warfarin + Aspirin: Risiko pendarahan meningkat",
      "indicator": "warning",
      "source": {
        "label": "PDDI-CDS",
        "url": "https://example.org/pddi"
      },
      "suggestions": [
        {
          "label": "Pertimbangkan alternatif",
          "actions": [
            {
              "type": "delete",
              "description": "Batalkan preskripsi aspirin",
              "resourceId": "MedicationRequest/789"
            }
          ]
        }
      ],
      "links": [
        {
          "label": "Maklumat lanjut",
          "url": "https://example.org/ddi/warfarin-aspirin",
          "type": "absolute"
        }
      ]
    }
  ]
}
```

---

## Penunjuk Keterukan

| Penunjuk | Penerangan | Tindakan |
|----------|------------|----------|
| `critical` | Berbahaya, jangan teruskan | Sekat preskripsi |
| `warning` | Risiko signifikan | Amaran dengan pilihan |
| `info` | Maklumat sahaja | Paparkan nota |

---

## Aplikasi dalam MyTxGNN

### Senario: Penggunaan Semula dengan DDI

Apabila ubat yang dicadangkan untuk penggunaan semula mempunyai interaksi dengan ubat sedia ada pesakit:

```json
{
  "cards": [
    {
      "uuid": "repurposing-ddi-1",
      "summary": "Pertimbangan Penggunaan Semula: Interaksi Ubat",
      "detail": "Prednisolone (ramalan untuk rinitis alahan) mungkin berinteraksi dengan warfarin yang sedang diambil pesakit. Pantau INR dengan teliti.",
      "indicator": "warning",
      "source": {
        "label": "MyTxGNN PDDI",
        "url": "https://mytxgnn.yao.care"
      },
      "suggestions": [
        {
          "label": "Lihat laporan penuh",
          "actions": [
            {
              "type": "create",
              "description": "Buka laporan MyTxGNN",
              "resource": {
                "resourceType": "Task",
                "status": "requested",
                "intent": "proposal",
                "code": {
                  "text": "Review MyTxGNN Report"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Pelaksanaan

### Langkah-langkah

<ol class="actionable-steps">
<li><strong>Daftar perkhidmatan CDS</strong>: Konfigurasi endpoint CDS Hooks</li>
<li><strong>Integrasikan pangkalan data DDI</strong>: DrugBank, DDInter, atau sumber lain</li>
<li><strong>Laksanakan logik peraturan</strong>: Tentukan bila dan bagaimana amaran dipaparkan</li>
<li><strong>Uji dengan sandbox</strong>: Gunakan CDS Hooks Sandbox untuk pengujian</li>
<li><strong>Sesuaikan dengan EHR</strong>: Integrasikan dengan sistem produksi</li>
</ol>

---

## Sumber Data DDI

| Sumber | Penerangan | Liputan |
|--------|------------|---------|
| **DDInter 2.0** | Pangkalan data DDI komprehensif | 200,000+ DDI |
| **DrugBank** | Maklumat interaksi ubat | 16,000+ ubat |
| **RxNorm** | Istilah ubat standard | Liputan luas |

---

## Contoh Kod

### Pelayan CDS Hooks (Python)

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/cds-services', methods=['GET'])
def discovery():
    return jsonify({
        "services": [
            {
                "hook": "order-select",
                "id": "pddi-check",
                "title": "PDDI Check Service",
                "description": "Check for potential drug-drug interactions"
            }
        ]
    })

@app.route('/cds-services/pddi-check', methods=['POST'])
def pddi_check():
    context = request.json.get('context', {})
    draft_orders = context.get('draftOrders', {})

    # Analisis interaksi
    cards = analyze_interactions(draft_orders)

    return jsonify({"cards": cards})

def analyze_interactions(orders):
    # Logik analisis DDI
    cards = []
    # ... implementasi ...
    return cards
```

---

## Sumber Rujukan

| Sumber | Pautan |
|--------|--------|
| PDDI-CDS IG | [hl7.org/fhir/uv/pddi](https://hl7.org/fhir/uv/pddi/) |
| CDS Hooks | [cds-hooks.org](https://cds-hooks.org/) |
| DDInter 2.0 | [ddinter2.scbdd.com](https://ddinter2.scbdd.com/) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Nota teknikal ini adalah untuk <strong>rujukan pembangunan</strong>. Sistem sokongan keputusan klinikal memerlukan pengesahan yang teliti sebelum penggunaan dalam persekitaran klinikal.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
