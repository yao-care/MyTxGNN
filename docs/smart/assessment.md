---
layout: default
title: Penilaian Aplikasi Boleh Integrasi
parent: SMART on FHIR
nav_order: 5
description: "Panduan penilaian untuk menentukan kesesuaian aplikasi SMART on FHIR untuk integrasi"
permalink: /smart/assessment/
---

# Penilaian Aplikasi Boleh Integrasi

<p class="key-answer" data-question="Bagaimana menilai aplikasi SMART?">
Halaman ini menyediakan rangka kerja untuk menilai sama ada aplikasi SMART on FHIR sesuai untuk diintegrasikan dengan sistem EHR organisasi anda.
</p>

---

## Kriteria Penilaian

### 1. Keselamatan

| Kriteria | Perincian | Skor (1-5) |
|----------|-----------|------------|
| **Pengesahan** | Menyokong OAuth 2.0? | |
| **Penyulitan** | HTTPS sahaja? | |
| **Data Minimal** | Minta skop minimum? | |
| **Audit** | Log akses tersedia? | |

### 2. Pematuhan

| Kriteria | Perincian | Skor (1-5) |
|----------|-----------|------------|
| **HIPAA** | Pematuhan privasi AS | |
| **PDPA** | Pematuhan privasi Malaysia | |
| **GDPR** | Pematuhan privasi EU | |
| **Tempatan** | Keperluan regulatori tempatan | |

### 3. Teknikal

| Kriteria | Perincian | Skor (1-5) |
|----------|-----------|------------|
| **FHIR R4** | Menyokong versi terkini? | |
| **Prestasi** | Masa respons < 3s? | |
| **Ketersediaan** | SLA 99.9%? | |
| **Dokumentasi** | API didokumentasikan? | |

### 4. Klinikal

| Kriteria | Perincian | Skor (1-5) |
|----------|-----------|------------|
| **Keperluan** | Menyelesaikan masalah sebenar? | |
| **Aliran Kerja** | Sesuai dengan aliran kerja? | |
| **Bukti** | Disokong bukti klinikal? | |
| **Latihan** | Memerlukan latihan minimal? | |

---

## Senarai Semak Penilaian MyTxGNN

### Keselamatan

- [x] OAuth 2.0 Authorization Code Flow
- [x] HTTPS untuk semua komunikasi
- [x] Tiada data pesakit disimpan
- [x] Skop baca sahaja (`patient/*.read`)

### Pematuhan

- [x] Tiada data pesakit dipindahkan keluar
- [x] Ramalan adalah rujukan penyelidikan sahaja
- [x] Penafian dipaparkan dengan jelas

### Teknikal

- [x] FHIR R4 sepenuhnya
- [x] Masa respons API < 500ms
- [x] Dokumentasi API lengkap
- [x] Kod sumber terbuka (GitHub)

### Klinikal

- [x] Menyediakan maklumat penggunaan semula ubat
- [x] Tidak mengganggu aliran kerja preskripsi
- [x] Bukti tahap disertakan (L1-L5)
- [ ] Latihan pengguna (dalam pembangunan)

---

## Proses Penilaian

<ol class="actionable-steps">
<li><strong>Semakan Awal</strong>: Semak dokumentasi dan demo</li>
<li><strong>Penilaian Teknikal</strong>: Pasukan IT menilai keselamatan dan integrasi</li>
<li><strong>Penilaian Klinikal</strong>: Doktor menilai kegunaan dan aliran kerja</li>
<li><strong>Ujian Sandbox</strong>: Uji dalam persekitaran bukan produksi</li>
<li><strong>Penilaian Risiko</strong>: Dokumentasikan risiko dan mitigasi</li>
<li><strong>Kelulusan</strong>: Dapatkan kelulusan dari pihak berkuasa</li>
</ol>

---

## Borang Keputusan

| Aspek | Skor Purata | Lulus? |
|-------|-------------|--------|
| Keselamatan | _/5 | Ya/Tidak |
| Pematuhan | _/5 | Ya/Tidak |
| Teknikal | _/5 | Ya/Tidak |
| Klinikal | _/5 | Ya/Tidak |
| **Keseluruhan** | **_/5** | **Ya/Tidak** |

**Skor minimum untuk kelulusan**: 3.5/5 untuk setiap aspek

---

## Sumber Rujukan

| Dokumen | Penerangan |
|---------|------------|
| [SMART App Launch IG](https://hl7.org/fhir/smart-app-launch/) | Standard pelancaran aplikasi |
| [ONC Cures Act](https://www.healthit.gov/curesrule/) | Keperluan interoperabiliti AS |
| [PDPA Malaysia](https://www.pdp.gov.my/) | Akta Perlindungan Data Peribadi |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Kriteria penilaian ini adalah <strong>panduan umum</strong>. Organisasi anda mungkin mempunyai keperluan tambahan berdasarkan polisi dalaman dan keperluan regulatori.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
