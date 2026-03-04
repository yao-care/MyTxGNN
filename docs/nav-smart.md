---
layout: default
title: SMART on FHIR
nav_order: 2
has_children: true
description: "Integrasi SMART on FHIR untuk MyTxGNN - akses ramalan penggunaan semula ubat melalui standard interoperabiliti kesihatan."
permalink: /smart/
---

# SMART on FHIR

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Integrasikan MyTxGNN dengan sistem kesihatan menggunakan standard SMART on FHIR
</p>

---

## Apakah SMART on FHIR?

<p class="key-answer" data-question="Apakah SMART on FHIR?">
<strong>SMART on FHIR</strong> (Substitutable Medical Applications, Reusable Technologies on FHIR) adalah standard untuk aplikasi kesihatan yang membolehkan integrasi dengan sistem rekod perubatan elektronik (EHR) menggunakan protokol standard.
</p>

<div class="key-takeaway">
MyTxGNN menyokong SMART on FHIR untuk membolehkan integrasi lancar dengan sistem EHR hospital dan klinik, memberikan akses kepada ramalan penggunaan semula ubat dalam aliran kerja klinikal.
</div>

---

## Ciri-ciri Utama

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/smart/guide/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #1976D2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #1976D2;">Panduan Pengguna</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Pelajari cara menggunakan aplikasi SMART MyTxGNN</p>
</a>

<a href="{{ '/smart/technical/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #4CAF50;">
  <h3 style="margin: 0 0 0.5rem 0; color: #388E3C;">Dokumentasi Teknikal</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Spesifikasi teknikal dan panduan integrasi</p>
</a>

<a href="{{ '/smart/resources/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #F57C00;">Sumber Integrasi</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Alat dan sumber untuk integrasi sistem</p>
</a>

<a href="{{ '/fhir/metadata' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">Spesifikasi FHIR API</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Penyata keupayaan dan endpoint API</p>
</a>

</div>

---

## FHIR API Endpoints

| Endpoint | Penerangan | Contoh |
|----------|------------|--------|
| `/fhir/metadata` | Penyata keupayaan pelayan | [Lihat]({{ '/fhir/metadata' | relative_url }}) |
| `/fhir/MedicationKnowledge/{id}` | Maklumat ubat | [DB00860]({{ '/fhir/MedicationKnowledge/db00860.json' | relative_url }}) |
| `/fhir/ClinicalUseDefinition/{id}` | Data ramalan | [Contoh]({{ '/fhir/ClinicalUseDefinition/' | relative_url }}) |

### Contoh Permintaan

```bash
# Dapatkan maklumat ubat (Prednisolone)
curl https://mytxgnn.yao.care/fhir/MedicationKnowledge/db00860.json

# Dapatkan penyata keupayaan
curl https://mytxgnn.yao.care/fhir/metadata
```

---

## Sumber Teknikal

| Sumber | Penerangan | Pautan |
|--------|------------|--------|
| **CDS Hooks** | Perkhidmatan sokongan keputusan klinikal | [Lihat]({{ '/smart/cds-hooks/' | relative_url }}) |
| **CQL** | Bahasa Pertanyaan Klinikal | [Lihat]({{ '/smart/cql/' | relative_url }}) |
| **HL7 PDDI-CDS** | Interaksi ubat-ubat klinikal | [Lihat]({{ '/smart/pddi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Integrasi SMART on FHIR adalah untuk <strong>tujuan penyelidikan dan pendidikan</strong>. Sebelum penggunaan dalam persekitaran klinikal produksi, sila pastikan pematuhan dengan keperluan regulatori tempatan.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
