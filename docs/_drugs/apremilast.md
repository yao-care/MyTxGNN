---
layout: default
title: Apremilast
parent: Low Evidence (L4-L5)
nav_order: 81
evidence_level: L5
indication_count: 0
---

# Apremilast
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

# Apremilast: Penilaian Penggunaan Semula Ubat — Ramalan TxGNN Ditangguhkan

## Ringkasan Satu Ayat

Apremilast (DrugBank: DB05676) ialah penghambat fosfodiestaraz 4 (PDE4) yang selektif dengan kegunaan yang telah terbukti dalam keadaan radang seperti artritis psoriatik dan psoriasis plak, dan disahkan dipasarkan di Malaysia dengan 3 produk berdaftar. Walau bagaimanapun, Pakej Bukti semasa tidak mengandungi **ramalan indikasi baru yang dijana oleh TxGNN**, dan data kritikal — termasuk butiran label kawal selia, amaran keselamatan, dan mekanisme tindakan — tidak diambil dalam kitaran pengumpulan ini. Penilaian ubat penggunaan semula yang lengkap tidak boleh dikeluarkan sehingga jurang-jurang ini diselesaikan; keputusan **Tunda** disyorkan sambil menunggu pengumpulan semula.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak diambil — teks label kawal selia tidak hadir dalam Pakej Bukti ini |
| Indikasi Baru Diramalkan | **Ditangguhkan** — tiada ramalan TxGNN yang hadir dalam Pakej Bukti ini |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | **Tunda** |

---

## Mengapa Ramalan Ini Munasabah?

Bahagian ini tidak dapat diselesaikan dalam bentuk piawai kerana tiada indikasi sasaran yang diramalkan oleh TxGNN yang tersedia dalam Pakej Bukti semasa (`predicted_indications: []`).

Daripada pengetahuan farmakologi yang tersedia secara umum, Apremilast ialah penghambat PDE4 molekul kecil yang meningkatkan tahap cAMP intrasel, secara meluas mengawal pengeluaran pengantara radang dan anti-radang (contohnya, mengurangkan TNF-α, IL-17, IL-23 sambil meningkatkan IL-10). Mekanisme tindakan ini mempunyai potensi kaitan merentas spektrum luas penyakit radang kronik di luar kegunaannya yang diluluskan semasa.

Setelah ramalan TxGNN dijana, bahagian ini akan menilai kesetaraan mekanik dari indikasi calon teratas yang disenaraikan dan hubungannya dengan kelompok indikasi radang yang diluluskan.

---

## Maklumat Pasaran Malaysia

Pakej Bukti merekodkan **3 produk berdaftar** di Malaysia (status pertanyaan NPRA: berjaya), tetapi semua medan peringkat produk — nombor kebenaran, nama produk, bentuk dos, pengilang, dan teks indikasi yang diluluskan — dikembalikan sebagai kosong dalam larian pengumpulan ini. Jadual di bawah tidak dapat diisi sehingga butiran pendaftaran NPRA dipertanyakan semula.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|-------------|-----------|--------------------------|
| *(tidak diambil)* | *(tidak diambil)* | *(tidak diambil)* | *(tidak diambil)* |

**Tindakan diperlukan:** Pertanyaan semula NPRA dengan nama ubat "APREMILAST" dan ambil rekod butiran produk penuh untuk semua 3 lesen.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. Amaran utama dan kontraindikasi telah dikenal pasti sebagai jurang data **Menyekat** (DG001) dan tidak diambil dalam kitaran penilaian ini. Tiada rekod interaksi ubat-ubat yang ditemui dalam pertanyaan DDI (hasil: `not_found`, 0 interaksi).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunda**

**Rasional:**
Pakej Bukti kehilangan tiga keperluan minimum untuk penilaian penggunaan semula — ramalan indikasi sasaran TxGNN, data label kawal selia yang diisi, dan maklumat keselamatan — menjadikan mustahil untuk menilai potensi terapeutik, kesetaraan mekanik, atau profil risiko pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Menyekat — DG001]** Muat turun dan analisis PDF sisipan pakej NPRA / TFDA untuk Apremilast untuk mengekstrak amaran utama dan kontraindikasi; ini mesti diselesaikan sebelum sebarang penilaian keselamatan dapat dimulai
- **[Tinggi — DG002]** Pertanyaan API DrugBank untuk DB05676 untuk mengambil penerangan mekanisme tindakan (MOA) penuh
- **[Diperlukan]** Jalankan saluran paip model TxGNN untuk Apremilast (DB05676) untuk menjana ramalan indikasi baru yang beringkat; tanpa ramalan, tiada sasaran penggunaan semula yang wujud untuk dinilai
- **[Diperlukan]** Pertanyaan semula pangkalan data pendaftaran NPRA untuk mengambil butiran produk lengkap (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) untuk semua 3 lesen Malaysia
- **[Susulan]** Setelah indikasi sasaran dikenal pasti, jalankan pengumpul bukti ClinicalTrials.gov dan PubMed terhadap pasangan ubat–penyakit untuk mengisi bahagian bukti ujian klinikal dan sastera
- **[Susulan]** Tetapkan semula Tahap Bukti (L1–L5) dan naik taraf cadangan keputusan (Pergi / Teruskan dengan Perlindungan) setelah semua jurang di atas ditutup

---

> ⚠️ **Penafian:** Laporan ini hanya untuk rujukan penyelidikan dan bukan merupakan nasihat perubatan. Calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum sebarang aplikasi terapeutik.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

