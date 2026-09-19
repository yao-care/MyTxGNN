---
layout: default
title: Abemaciclib
parent: Low Evidence (L4-L5)
nav_order: 12
evidence_level: L5
indication_count: 0
---

# Abemaciclib
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

# Abemaciclib (DB12001): Penilaian Repurposing Ubat — Ramalan TxGNN Tertunda

---

## Ringkasan Satu Ayat

Abemaciclib adalah penghambat CDK4/6 selektif yang sedang dipasarkan di Malaysia untuk rawatan kanser payudara. Evidence Pack semasa mengandungi **tiada petunjukan baru yang diramalkan oleh TxGNN**, dan data kritikal termasuk mekanisme tindakan, teks petunjuk yang diluluskan, dan amaran keselamatan semuanya disenaraikan sebagai jurang data yang belum diselesaikan. Penilaian repurposing lengkap **tidak dapat dilakukan** sehingga jurang ini diselesaikan.

---

## Gambaran Ringkas

| Perkara | Kandungan |
|------|----------|
| Petunjuk Asal | Butiran menunggu (teks lesen tidak dikembalikan dalam cabutan data semasa) |
| Petunjukan Baru yang Diramalkan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | — |
| Paras Bukti | L5 (ramalan model belum dijana) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini **tiada petunjukan baru yang diramalkan oleh TxGNN** untuk Abemaciclib dalam Evidence Pack ini. Tanpa petunjukan sasaran, alasan mekanik untuk repurposing tidak dapat dibina.

Abemaciclib diketahui berfungsi sebagai penghambat selektif kinase bergantung siklin 4 dan 6 (CDK4/6), yang merupakan pengawal utama transisi kitaran sel G1-to-S. Perencatan CDK4/6 menghasilkan penghentian kitaran sel dalam sel kanser yang mengekalkan laluan Rb (protein retinoblastoma) yang utuh. Walau bagaimanapun, data MOA terperinci telah ditandai sebagai jurang data (DG002) dalam bungkusan semasa, dan tanpa petunjukan sasaran yang diramalkan, tiada analisis jambatan mekanik yang dapat dilakukan.

Apabila ramalan TxGNN dijana, biologi laluan yang dikongsi antara petunjukan kanser payudara asal dan mana-mana petunjukan baru yang diramalkan boleh dinilai secara sistematik. Memandangkan penglibatan CDK4/6 yang luas dalam isyarat proliferatif merentasi pelbagai jenis tumor, peluang repurposing merentasi tumor pepejal lain atau keganasan hematologi adalah hipotesis yang munasabah untuk diterokai.

---

## Bukti Ujian Klinikal

Tiada petunjukan yang diramalkan tersedia dalam Evidence Pack semasa. Bukti ujian klinikal khusus petunjukan tidak dapat dibentangkan pada peringkat ini.

---

## Bukti Literatur

Tiada petunjukan yang diramalkan tersedia dalam Evidence Pack semasa. Bukti literatur khusus petunjukan tidak dapat dibentangkan pada peringkat ini.

---

## Maklumat Pasaran Malaysia

Pertanyaan NPRA (2026-03-27) mengesahkan **3 pendaftaran aktif**. Walau bagaimanapun, cabutan data semasa tidak mengembalikan rekod produk terperinci (nombor kebenaran, nama produk, bentuk dos, atau teks petunjukan yang diluluskan). Cabutan data NPRA susulan diperlukan.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjukan yang Diluluskan |
|-----------------|------------|-----------|--------------------------|
| — | — | — | Butiran menunggu |

> **Catatan:** 3 pendaftaran disahkan melalui pertanyaan NPRA. Butiran penuh memerlukan re-pertanyaan atau pengambilan manual dari portal NPRA.

---

## Sitotoksisiti

Abemaciclib adalah terapi antineoplastik yang disasarkan (kelas penghambat CDK4/6), dan berikut merangkum profil sitotoksisiti berdasarkan ciri-ciri kelas ubat.

| Perkara | Kandungan |
|------|----------|
| Klasifikasi Sitotoksisiti | Terapi yang disasarkan — penghambat CDK4/6 selektif (bukan sitotoksik konvensional) |
| Risiko Myelosuppression | Sederhana — neutropenia adalah peristiwa keburukan hematologi yang paling biasa dilaporkan untuk kelas ubat ini |
| Klasifikasi Emetogenisiti | Rendah |
| Item Pemantauan | CBC dengan kiraan pembezaan, ujian fungsi hati (ALT/AST), fungsi buah pinggang, kreatinin serum; pantau untuk diare dan tromboembolisme vena |
| Perlindungan Pengendalian | Ikuti garis panduan institusional untuk agen onkologi lisan yang disasarkan; amalan piawai berlaku |

---

## Pertimbangan Keselamatan

Data keselamatan (amaran utama dan kontraindikasi) tidak tersedia dalam Evidence Pack semasa dan ditandai sebagai jurang data yang menghalang (DG001). Tiada interaksi ubat-ubat dikenal pasti dalam pertanyaan DDI.

> Sila rujuk sisipan bungkus NPRA yang diluluskan untuk maklumat keselamatan lengkap.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Evidence Pack untuk Abemaciclib (DB12001) sangat tidak lengkap — ramalan TxGNN belum dijana, dan dua jurang data yang belum diselesaikan (DG001: amaran/kontraindikasi bungkus NPRA; DG002: mekanisme tindakan) menghalang kedua-dua pra-saringan keselamatan dan analisis kebolehpercayaan mekanik. Tiada penilaian repurposing boleh diselesaikan dalam keadaan ini.

**Untuk meneruskan, berikut diperlukan:**

- **[DG001 — Menghalang]** Muat turun dan analisis PDF sisipan bungkus NPRA untuk mengekstrak teks petunjukan yang diluluskan, amaran utama, dan kontraindikasi
- **[DG002 — Tinggi]** Pertanyaan API DrugBank (DB12001) untuk mendapatkan data mekanisme tindakan terperinci
- **[Ramalan TxGNN]** Jalankan ramalan TxGNN untuk Abemaciclib dan isikan `predicted_indications`
- **[Butiran Lesen]** Jalankan semula cabutan data NPRA untuk mendapatkan nama produk penuh, bentuk dos, dan nombor kebenaran untuk semua 3 produk yang didaftarkan
- **Re-isu Evidence Pack** selepas menyelesaikan DG001 dan DG002 untuk membolehkan penilaian penuh

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

