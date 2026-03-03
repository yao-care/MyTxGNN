---
layout: default
title: Rujukan SMART App Gallery
parent: SMART on FHIR
nav_order: 4
description: "Rujukan galeri aplikasi SMART on FHIR untuk inspirasi dan pembelajaran"
permalink: /smart/gallery/
---

# Rujukan SMART App Gallery

<p class="key-answer" data-question="Apakah SMART App Gallery?">
SMART App Gallery adalah koleksi aplikasi kesihatan yang dibina menggunakan standard SMART on FHIR. Halaman ini menyenaraikan contoh aplikasi yang boleh menjadi rujukan untuk pembangunan dan integrasi.
</p>

---

## Kategori Aplikasi

### Sokongan Keputusan Klinikal

| Aplikasi | Penerangan | Pautan |
|----------|------------|--------|
| **CDS Hooks Sandbox** | Ujian perkhidmatan CDS | [sandbox.cds-hooks.org](https://sandbox.cds-hooks.org/) |
| **Rx Refill** | Pengurusan preskripsi | [apps.smarthealthit.org](https://apps.smarthealthit.org/) |

### Pengurusan Ubat

| Aplikasi | Penerangan | Pautan |
|----------|------------|--------|
| **MedMinder** | Peringatan ubat | Contoh |
| **Drug Interactions** | Semak interaksi | Contoh |

### Kesihatan Pesakit

| Aplikasi | Penerangan | Pautan |
|----------|------------|--------|
| **Growth Chart** | Carta pertumbuhan pediatrik | [github.com/smart-on-fhir](https://github.com/smart-on-fhir/growth-chart-app) |
| **BP Centiles** | Persentil tekanan darah | [apps.smarthealthit.org](https://apps.smarthealthit.org/) |

---

## Galeri Rasmi SMART

<div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; margin: 1.5rem 0;">
  <strong>SMART App Gallery</strong><br>
  <a href="https://apps.smarthealthit.org/" target="_blank" rel="noopener">apps.smarthealthit.org</a><br>
  <small>Koleksi rasmi aplikasi SMART on FHIR yang dibangunkan oleh komuniti</small>
</div>

---

## Ciri-ciri Aplikasi Berkualiti

Berdasarkan aplikasi dalam galeri, berikut adalah ciri-ciri aplikasi SMART yang baik:

<ol class="actionable-steps">
<li><strong>Fokus Tunggal</strong>: Selesaikan satu masalah dengan baik</li>
<li><strong>Responsif</strong>: Berfungsi pada pelbagai saiz skrin</li>
<li><strong>Pantas</strong>: Masa muat kurang dari 3 saat</li>
<li><strong>Selamat</strong>: Pematuhan HIPAA/GDPR</li>
<li><strong>Mesra Pengguna</strong>: Antara muka intuitif</li>
</ol>

---

## Contoh Seni Bina

### Aplikasi Paparan Ubat

```
┌─────────────────────────────────────────┐
│           SMART App Launch              │
│  ┌─────────────────────────────────────┐│
│  │  OAuth 2.0 Authorization            ││
│  └─────────────────────────────────────┘│
│                    ▼                    │
│  ┌─────────────────────────────────────┐│
│  │  Fetch MedicationRequest            ││
│  │  GET /MedicationRequest?patient=X   ││
│  └─────────────────────────────────────┘│
│                    ▼                    │
│  ┌─────────────────────────────────────┐│
│  │  Query MyTxGNN API                  ││
│  │  GET /fhir/ClinicalUseDefinition    ││
│  └─────────────────────────────────────┘│
│                    ▼                    │
│  ┌─────────────────────────────────────┐│
│  │  Display Repurposing Predictions    ││
│  └─────────────────────────────────────┘│
└─────────────────────────────────────────┘
```

---

## Pelajaran dari Galeri

| Aspek | Amalan Terbaik |
|-------|----------------|
| **Kebenaran** | Minta skop minimum yang diperlukan |
| **Data** | Cache respons FHIR secara bijak |
| **UI** | Gunakan reka bentuk konsisten dengan EHR |
| **Ralat** | Paparkan mesej ralat yang bermakna |
| **Prestasi** | Gunakan paging untuk senarai besar |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Aplikasi yang disenaraikan adalah untuk <strong>rujukan dan pembelajaran</strong>. Semak lesen dan syarat penggunaan sebelum mengadaptasi kod.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
