---
layout: default
title: Panduan Pengguna
parent: SMART on FHIR
nav_order: 1
description: "Panduan pengguna untuk aplikasi SMART on FHIR MyTxGNN"
permalink: /smart/guide/
---

# Panduan Pengguna SMART on FHIR

<p class="key-answer" data-question="Bagaimana menggunakan MyTxGNN SMART App?">
Panduan ini menerangkan cara mengakses dan menggunakan aplikasi SMART MyTxGNN untuk mencari ramalan penggunaan semula ubat dalam aliran kerja klinikal.
</p>

---

## Langkah 1: Lancarkan Aplikasi

### Dari Portal EHR

1. Log masuk ke sistem EHR anda
2. Navigasi ke bahagian "Aplikasi" atau "SMART Apps"
3. Cari "MyTxGNN Drug Repurposing"
4. Klik untuk melancarkan aplikasi

### Melalui SMART Launcher (Ujian)

Untuk ujian, gunakan [SMART App Launcher](https://launch.smarthealthit.org/):

1. Masukkan URL Launch: `https://mytxgnn.yao.care/smart/launch.html`
2. Pilih pelayan FHIR ujian
3. Pilih pesakit (jika berkaitan)
4. Klik "Launch"

---

## Langkah 2: Cari Ubat

Setelah aplikasi dilancarkan:

<ol class="actionable-steps">
<li>Masukkan nama ubat dalam kotak carian</li>
<li>Pilih ubat dari senarai cadangan</li>
<li>Lihat ramalan penggunaan semula untuk ubat tersebut</li>
</ol>

---

## Langkah 3: Semak Ramalan

Untuk setiap ubat, anda akan melihat:

| Bahagian | Penerangan |
|----------|------------|
| **Maklumat Ubat** | Nama, ID DrugBank, kelas terapeutik |
| **Ramalan KG** | Indikasi berpotensi dari graf pengetahuan |
| **Ramalan DL** | Indikasi dengan skor keyakinan tinggi |
| **Tahap Bukti** | L1-L5 berdasarkan bukti klinikal |

---

## Langkah 4: Lihat Bukti

Klik pada mana-mana ramalan untuk melihat:

- Ujian klinikal berkaitan dari ClinicalTrials.gov
- Artikel saintifik dari PubMed
- Maklumat NPRA Malaysia

---

## Keperluan Sistem

| Komponen | Keperluan |
|----------|-----------|
| **Pelayar** | Chrome, Firefox, Safari, Edge (terkini) |
| **FHIR** | R4 |
| **OAuth 2.0** | Diperlukan untuk integrasi EHR |

---

## Soalan Lazim

### Adakah aplikasi ini percuma?

Ya, MyTxGNN SMART App adalah percuma untuk kegunaan penyelidikan dan pendidikan.

### Adakah data pesakit dihantar?

Tidak. Aplikasi tidak menghantar atau menyimpan sebarang data pesakit. Semua ramalan adalah berasaskan ubat sahaja.

### Bolehkah saya menggunakan di hospital saya?

Ya, tetapi integrasi dengan EHR produksi memerlukan kelulusan IT hospital dan pematuhan keselamatan.

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Aplikasi ini adalah untuk <strong>tujuan penyelidikan sahaja</strong>. Ramalan penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
