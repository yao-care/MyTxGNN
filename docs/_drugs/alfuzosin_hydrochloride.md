---
layout: default
title: Alfuzosin Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 42
evidence_level: L5
indication_count: 0
---

# Alfuzosin Hydrochloride
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

# Alfuzosin Hydrochloride: Laporan Penilaian — Ramalan Ubat Berubah Tujuan Tidak Tersedia

## Ringkasan Satu Ayat

Alfuzosin Hydrochloride ialah antagonis reseptor adrenergi alfa-1 selektif yang digunakan terutamanya untuk merawat hiperplasia prostat jinak (BPH) dan gejala saluran air kencing bawah (LUTS). Model TxGNN tidak menjana sebarang ramalan ubat berubah tujuan untuk ubat ini dalam perlaksanaan semasa, berkemungkinan disebabkan oleh jurang data hilir dalam pemetaan DrugBank atau resolusi nod KG. Penilaian ubat berubah tujuan sepenuhnya tidak dapat dijalankan sehingga jurang data utama — amaran sisipan pakej, MOA, dan rekod lesen lengkap — diselesaikan.

---

## Gambaran Pantas

| Perkara | Kandungan |
|------|---------|
| Petunjuk Asal | Hiperplasia Prostat Jinak (BPH) / Gejala Saluran Air Kencing Bawah |
| Indikasi Baru Dijangka | Tidak tersedia |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | Tidak Berkenaan — Tiada ramalan dijana |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan Disyorkan | **Tahan** |

---

## Latar Belakang Mekanisme Ubat

Pada masa kini, data mekanisme tindakan terperinci tidak tersedia daripada pakej bukti. Berdasarkan maklumat farmakologi yang tersedia secara umum, Alfuzosin Hydrochloride termasuk dalam kelas quinazoline bagi antagonis reseptor adrenergi alfa-1. Ia secara selektif menghalang reseptor alfa-1 dalam otot licin prostat, leher vesika urinaria, dan uretra, dengan itu mengurangkan rintangan aliran air kencing dan mengurangkan gejala obstruksi yang berkaitan dengan BPH.

Sebagai suatu kelas, penyekat alfa-1 berkongsi mekanisme yang ditentukan dengan baik yang telah diterokai di luar BPH. Keadaan seperti kolik ureter (memudahkan keluaran batu), hipertensi, dan disfungsi kencing tertentu telah disiasat dengan ubat-ubatan dalam kelas ini. Bagaimanapun, tanpa skor ramalan TxGNN yang disahkan dan nod penyakit yang berkaitan, adalah tidak mungkin untuk mengenal pasti atau menilai calon ubat berubah tujuan tertentu pada masa ini.

Ketiadaan ID DrugBank dalam pakej bukti ini (`drugbank_id: null`) dengan kuat mencadangkan bahawa langkah pemetaan nod ubat gagal, yang akan menjelaskan mengapa model TxGNN tidak menghasilkan output. Menyelesaikan pemetaan DrugBank adalah langkah pemulihan paling kritikal sebelum menjalankan semula saluran paip ramalan.

---

## Maklumat Pasaran Malaysia

> **Nota:** Pertanyaan NPRA mengembalikan **3 lesen berdaftar** untuk Alfuzosin Hydrochloride (tarikh pertanyaan: 2026-03-27, status: berjaya). Bagaimanapun, bidang rekod lesen berstruktur — nama produk, bentuk dos, pengeluar, dan teks petunjuk yang diluluskan — tidak diisi dalam pakej bukti ini. Sila pertanyakan portal [Pendaftaran Produk NPRA](https://www.npra.gov.my/) secara langsung untuk mendapatkan butiran pendaftaran lengkap bagi ketiga-tiga produk ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> **Jurang Data DG001 (Menyekat):** Amaran sisipan pakej NPRA/TFDA dan kontraindikasi belum diambil. Ini menghalang penyiapan pemeriksaan keselamatan S1. Pemulihan: muat turun dan parskan PDF sisipan pakej daripada laman web rasmi NPRA.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Model TxGNN tidak menghasilkan sebarang ramalan ubat berubah tujuan untuk ubat ini, dan dua jurang data kritikal — MOA yang hilang dan data keselamatan sisipan pakej yang hilang — menghalang penilaian ubat berubah tujuan yang bermakna. Punca akar kemungkinan besar ialah kegagalan pemetaan nod DrugBank (`drugbank_id: null`), yang mesti diselesaikan sebelum menjalankan semula saluran paip ramalan.

**Untuk meneruskan, yang berikut diperlukan:**

- **[DG002 — Keutamaan Tinggi]** Pertanyakan API DrugBank untuk menyelesaikan ID DrugBank bagi Alfuzosin Hydrochloride dan dapatkan mekanisme tindakan. Ini adalah punca akar yang paling mungkin bagi ramalan TxGNN yang hilang.
- **[DG001 — Menyekat]** Muat turun dan parskan PDF sisipan pakej NPRA untuk mengeluarkan amaran dan kontraindikasi utama, membolehkan langkah pemeriksaan keselamatan S1.
- **Perolehan rekod lesen lengkap:** Pertanyakan semula pangkalan data NPRA untuk mengisi nama produk, bentuk dos, pengeluar, dan teks petunjuk yang diluluskan bagi semua 3 lesen berdaftar.
- **Jalankan semula saluran paip ramalan TxGNN** selepas pemetaan DrugBank diselesaikan untuk menjana calon ubat berubah tujuan dengan skor ramalan dan nod penyakit yang berkaitan.
- **Jana semula laporan ini** setelah jurang di atas diselesaikan; templat lengkap (bukti percubaan klinikal, bukti literatur, penilaian sitotoksisiti) akan diisi dengan sewajarnya.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

