---
layout: default
title: Abiraterone Acetate
parent: Low Evidence (L4-L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# Abiraterone Acetate
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **0** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Abiraterone Acetate: Daripada Kanser Prostat kepada [Menunggu Ramalan TxGNN]

## Ringkasan Satu Ayat

Abiraterone Acetate adalah perencat CYP17A1 yang diindikasikan untuk kanser prostat yang tahan ketua metastatik (mCRPC), didaftarkan di Malaysia di bawah 11 kebenaran.
Bagaimanapun, **saluran paip ramalan TxGNN belum menghasilkan calon petunjuk baru** untuk ubat ini — `predicted_indications` kosong.
Tanpa output ramalan, laporan ini berfungsi sebagai **audit kelengkapan data** sebelum penilaian penjumlahan semula yang penuh.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Kanser prostat yang tahan ketua metastatik (mCRPC) *(daripada pengetahuan umum; teks indikasi NPRA tidak diambil)* |
| Indikasi Ramalan Baru | Belum dijana |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | Tidak boleh dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 11 |
| Keputusan yang Disyorkan | **Tahan** — jurang data penting menghalang penilaian |

---

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan TxGNN yang tersedia pada masa ini untuk Abiraterone Acetate (`predicted_indications: []`). Rasional mekanistik untuk penjumlahan semula tidak dapat dibina tanpa indikasi sasaran.

Pada masa ini, data mekanisme tindakan terperinci belum diambil daripada DrugBank. Berdasarkan pengetahuan yang tersedia secara terbuka, Abiraterone Acetate secara tidak boleh balik merencat **CYP17A1** (17α-hidroksilase/C17,20-liase), enzim utama dalam biosintesis androgen di testis, kelenjar adrenal, dan dalam tisu tumor prostat itu sendiri. Mekanisme penipisan androgen ini mendorong keupayaannya dalam kanser prostat yang peka hormon dan tahan ketua.

Sebaik sahaja saluran paip ramalan TxGNN dilaksanakan dan calon indikasi baru dikenal pasti, jambatan mekanistik antara perencatan CYP17A1 dan penyakit yang diramalkan dapat dinilai di sini.

---

## Bukti Ujian Klinikal

Pada masa ini tiada indikasi yang diramalkan oleh TxGNN tersedia. Bukti ujian klinikal tidak dapat dipaparkan.

---

## Bukti Kesusasteraan

Pada masa ini tiada indikasi yang diramalkan oleh TxGNN tersedia. Bukti kesusasteraan tidak dapat dipaparkan.

---

## Maklumat Pasaran Malaysia

Pertanyaan NPRA mengembalikan **11 lesen terdaftar**, tetapi butiran lesen individu (nombor kebenaran, nama produk, bentuk dos, teks indikasi yang diluluskan) tidak diisi dalam Pakej Bukti ini. Sila jalankan semula pengekstrakan data dengan pengambilan medan penuh.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------------------|-------------|-------------|-------------------|
| *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* |

> ⚠️ **11 pendaftaran disahkan** melalui pertanyaan NPRA (2026-03-27), tetapi butiran rekod individu memerlukan lintasan pengekstrakan susulan.

---

## Ketoksikan

Abiraterone Acetate adalah agen antineoplastik (perencat biosintesis androgen untuk kanser prostat).

| Item | Kandungan |
|------|----------|
| Klasifikasi Ketoksikan | Terapi tersasaran — Hormonal / perencat CYP17A1 (bukan sitotoksik konvensional) |
| Risiko Supresi Sumsum Tulang | Rendah (mekanisme bukan sitotoksik; supresi sumsum tulang bukan kebimbangan utama) |
| Klasifikasi Emetogenisiti | Rendah |
| Item Pemantauan | Fungsi hati (ALT/AST/bilirubin), kalium serum, tekanan darah, retensi bendalir, testosteron serum dan PSA |
| Perlindungan Pengendalian | Langkah-langkah pengendalian onkologi standard; biasanya tidak memerlukan protokol pengendalian ubat sitotoksik di bawah kebanyakan garis panduan institusional, tetapi sahkan mengikut SOP setempat |

---

## Pertimbangan Keselamatan

Sila rujuk risalah pakej untuk maklumat keselamatan.

> Pakej Bukti membawa **DG001 (Menyekat)**: Amaran dan kontraindikasi risalah pakej NPRA/TFDA belum diambil. Jurang ini mesti diselesaikan sebelum sebarang keputusan yang tergantung keselamatan dapat dibuat.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Dua input paling penting untuk penilaian penjumlahan semula — indikasi yang diramalkan TxGNN dan data keselamatan/MOA — kedua-duanya tidak hadir. Meneruskan tanpanya akan menghasilkan penilaian risiko yang tidak bermaklumat.

**Untuk meneruskan, yang berikut diperlukan:**

- [ ] **\[DG001 — Menyekat\]** Ambil risalah pakej NPRA/TFDA: muat turun PDF dan parskan amaran, kontraindikasi, dan data populasi istimewa
- [ ] **\[DG002 — Tinggi\]** Tanyakan API DrugBank untuk `ABIRATERONE ACETATE` untuk mendapatkan ID DrugBank, MOA yang disahkan, kategori ubat, dan data ketoksikan
- [ ] **Jalankan semula saluran paip ramalan TxGNN** — `predicted_indications` kosong; laksanakan langkah ramalan KG + DL dan isi Pakej Bukti
- [ ] **Ekstrak semula butiran lesen NPRA** — 11 pendaftaran wujud tetapi medan rekod individu (nama produk, bentuk dos, teks indikasi) tidak ditangkap; tanyakan semula dengan pemetaan medan penuh
- [ ] Sebaik sahaja ramalan tersedia, janakan semula laporan ini dengan indikasi sasaran dan jadual bukti

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

