---
layout: default
title: Amoxicillin Sodium
parent: Low Evidence (L4-L5)
nav_order: 64
evidence_level: L5
indication_count: 0
---

# Amoxicillin Sodium
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

# Amoxicillin Sodium: Antibiotik — Penilaian Ubah Guna Tidak Lengkap

## Ringkasan Satu Ayat

Amoxicillin Sodium ialah antibiotik β-laktam spektrum luas yang digunakan secara meluas dan didaftarkan di Malaysia di bawah 5 lesen produk.
Pakej Bukti semasa tidak menghasilkan sebarang ramalan ubah guna TxGNN kerana input data kritikal yang hilang — jurang data utama termasuk amaran dalam risalah kemasan dan mekanisme tindakan mesti diselesaikan sebelum penilaian bermakna boleh diteruskan.
Sehingga jurang-jurang ini ditangani, tiada tahap bukti yang boleh diberikan dan keputusan **Tahan** disyorkan.

---

## Ikhtisar Pantas

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Tidak Tersedia (teks lesen tidak diisi dalam Pakej Bukti) |
| Indikasi Baru yang Diramalkan | Tiada — tiada ramalan dihasilkan |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A — di bawah L5 (tiada ramalan dihasilkan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 5 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada indikasi ubah guna yang diramalkan telah dihasilkan dalam Pakej Bukti ini — tatasusunan `predicted_indications` adalah kosong. Ini bermakna saluran TxGNN tidak menghasilkan sebarang calon ubah guna untuk Amoxicillin Sodium di bawah konfigurasi data semasa, dan analisis mekanisme-ke-indikasi-baru yang standard tidak boleh dilakukan.

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia. Berdasarkan pengetahuan farmakologi yang ditegakkan, Amoxicillin Sodium tergolong dalam subkumpulan aminopenisilin antibiotik β-laktam, dengan mekanisme utamanya melibatkan perencatan sintesis dinding sel bakteria melalui pengikatan kepada protein pengikat penisilin (PBPs). Bagaimanapun, maklumat ini tidak disahkan melalui DrugBank dalam Pakej Bukti semasa, dan oleh itu tidak boleh dipercayai secara formal untuk pemetaan mekanisme-tindakan dalam rangka kerja TxGNN.

Untuk membuka calon ubah guna, tiga input mesti berada di tempat terlebih dahulu: DrugBank ID yang disahkan dipautkan kepada Amoxicillin Sodium, teks indikasi yang diluluskan daripada rekod lesen NPRA yang diisi, dan data risalah kemasan yang diselesaikan untuk melewati pra-pemeriksaan keselamatan. Setelah ini tersedia, menjalankan semula langkah ramalan Graf Pengetahuan dan Pembelajaran Dalam harus menghasilkan calon bermakna.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan berdaftar dalam Pakej Bukti ini.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan tersedia dalam Pakej Bukti ini.

---

## Maklumat Pasaran Malaysia

Lima pendaftaran produk telah dikenal pasti melalui pertanyaan NPRA (tarikh pertanyaan: 2026-03-27) dan pertanyaan telah dicatat sebagai berjaya (`result_count: 5`). Bagaimanapun, semua medan lesen terperinci — nombor lesen, nama produk, bentuk dos, pengilang, dan teks indikasi yang diluluskan — telah dikembalikan sebagai rentetan kosong, mencadangkan isu penghuraian data atau pemetaan medan pada hulu panggilan API daripada ketiadaan pendaftaran yang sebenarnya.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------------------|--------------|-------------|---------------------|
| (Tidak diisi) | (Tidak diisi) | (Tidak diisi) | (Tidak diisi) |
| (Tidak diisi) | (Tidak diisi) | (Tidak diisi) | (Tidak diisi) |
| (Tidak diisi) | (Tidak diisi) | (Tidak diisi) | (Tidak diisi) |
| (Tidak diisi) | (Tidak diisi) | (Tidak diisi) | (Tidak diisi) |
| (Tidak diisi) | (Tidak diisi) | (Tidak diisi) | (Tidak diisi) |

> **Tindakan diperlukan:** NPRA mengembalikan 5 rekod tetapi pemetaan medan gagal. Jalankan semula saluran penghuraian data terhadap tindak balas NPRA mentah untuk mengisi semula baris ini sebelum analisis hiliran.

---

## Pertimbangan Keselamatan

Sila rujuk risalah kemasan untuk maklumat keselamatan.

> **Nota:** Kedua-dua amaran utama dan kontraindikasi membawa jurang data luar biasa pada keterukan **Menyekat** (DG001), yang menghalang pra-pemeriksaan keselamatan daripada diteruskan. Tiada rekod interaksi ubat-ubat dikenal pasti (pertanyaan DDI mengembalikan 0 hasil). Penilaian keselamatan sepenuhnya disekat sehingga data risalah kemasan diambil daripada sumber rasmi NPRA dan diuraikan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada ramalan ubah guna TxGNN telah dihasilkan dan dua jurang data kritikal — jurang keterukan Menyekat pada amaran risalah kemasan dan jurang keterukan Tinggi pada mekanisme tindakan — menghalang kedua-dua pra-pemeriksaan keselamatan dan analisis mekanisme-tindakan. Penilaian ini tidak boleh maju sehingga jurang-jurang di bawah diselesaikan.

**Untuk meneruskan, yang berikut diperlukan:**

- **[DG001 — Menyekat]** Muat turun dan uraikan PDF risalah kemasan daripada tapak web rasmi NPRA untuk mengekstrak amaran, tindakan berjaga-jaga, dan kontraindikasi untuk Amoxicillin Sodium
- **[DG002 — Tinggi]** Pertanyakan API DrugBank untuk mengesahkan DrugBank ID dan mendapatkan data MOA penuh; ID yang disahkan adalah prasyarat untuk ramalan berasaskan KG
- **[Pengisian semula data lesen]** Selidiki mengapa 5 rekod produk berdaftar NPRA dikembalikan dengan semua medan kosong; periksa tindak balas API mentah dan betulkan logik pemetaan medan dalam saluran pemprosesan data
- **[Jalankan semula saluran TxGNN]** Setelah DrugBank ID disahkan dan teks indikasi tersedia, jalankan semula `run_kg_prediction.py` dan `txgnn_model.py` untuk menghasilkan calon ubah guna
- **[Pengumpulan bukti]** Selepas ramalan dihasilkan, jalankan pengumpul ClinicalTrials.gov dan PubMed terhadap indikasi yang diramalkan teratas untuk membina jadual bukti dan memberikan tahap bukti formal (L1–L5)

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

