---
layout: default
title: Atovaquone
parent: Low Evidence (L4-L5)
nav_order: 102
evidence_level: L5
indication_count: 0
---

# Atovaquone
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

# Atovaquone: Penilaian Penggunaan Semula Ubat Tertangguh — Data Tidak Mencukupi, Analisis Lengkap Tidak Dapat Dilakukan

---

## Ringkasan Satu Ayat

Atovaquone adalah ubat antiparasit yang digunakan secara meluas untuk rawatan dan pencegahan pneumonia *Pneumocystis jirovecii* (PCP), serta penyakit toksoplasma dan pencegahan malaria (digunakan bersama proguanil).
Walau bagaimanapun, dalam Evidence Pack ini, **medan indikasi yang diprediksi oleh TxGNN kosong**, dan rekod indikasi asal, mekanisme tindakan dan maklumat keselamatan semuanya mempunyai jurang kritis, **penilaian penggunaan semula ubat yang lengkap tidak dapat dilakukan**.
Disyorkan untuk melengkapkan data dan melaksanakan semula proses ramalan, kemudian melakukan penilaian rasmi.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak dicatat dalam Evidence Pack (berdasarkan pengetahuan umum: rawatan/pencegahan PCP, penyakit toksoplasma, pencegahan malaria) |
| Indikasi Baru yang Diprediksi | **Tiada** (`predicted_indications` ialah tatasusunan kosong) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A (Tiada hasil ramalan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Maklumat Pasaran Malaysia

Pertanyaan NPRA mengembalikan 1 pendaftaran Dipasarkan, tetapi Evidence Pack ini belum mendapatkan medan pendaftaran terperinci (nama produk, bentuk dos, indikasi yang diluluskan, dll.).

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|------------|-----------|------------------------|
| (Belum diperoleh) | (Belum diperoleh) | (Belum diperoleh) | (Belum diperoleh) |

> **Langkah Pemulihan**: Melalui antara muka pertanyaan rasmi NPRA, dapatkan maklumat produk lengkap menggunakan nombor pendaftaran dan isikan jadual di atas.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan bungkusan untuk maklumat keselamatan.

> Medan keselamatan Evidence Pack ini (amaran, kontraindikasi, interaksi ubat) semuanya merupakan jurang data, belum diperoleh daripada sisipan produk atau DrugBank.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Evidence Pack Atovaquone ini mempunyai beberapa jurang kritis — hasil ramalan TxGNN hilang, indikasi asal tidak dicatat, mekanisme tindakan belum diperoleh, amaran keselamatan dan kontraindikasi belum diisi, proses penilaian tidak dapat diteruskan.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Blocking — DG001]** Muat turun dan analisis PDF sisipan produk NPRA/TFDA, dapatkan amaran keselamatan dan kontraindikasi, untuk menghapuskan sekatan penilaian keselamatan awal S1
- **[High — DG002]** Pertanyaan API DrugBank untuk mekanisme tindakan (MOA) DB01117, untuk menyokong analisis kaitan mekanisme
- **Laksanakan semula proses ramalan TxGNN**, hasilkan senarai calon indikasi baru untuk Atovaquone (DB01117) (`predicted_indications`)
- **Lengkapkan maklumat pendaftaran NPRA terperinci**: Dapatkan nama produk, bentuk dos, teks penuh indikasi yang diluluskan
- Setelah data dilengkapkan, janakan semula laporan mengikut spesifikasi Evidence Pack v4, jalankan penarafan bukti L1–L5 lengkap dan analisis keputusan

---

> ⚠️ **Penafian YMYL**: Hasil laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan sebarang nasihat perubatan. Ubat calon penggunaan semula ubat mesti melalui pengesahan klinikal rasmi sebelum dapat digunakan dalam keputusan penjagaan kesihatan sebenarnya.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

