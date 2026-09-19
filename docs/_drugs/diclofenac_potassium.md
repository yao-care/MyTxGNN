---
layout: default
title: Diclofenac Potassium
parent: Low Evidence (L4-L5)
nav_order: 276
evidence_level: L5
indication_count: 0
---

# Diclofenac Potassium
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

# Diclofenac potassium: Penilaian Awal Penolokan Semula Ubat

## Ringkasan Satu Ayat

Diclofenac potassium (Diklofenac kalium) adalah ubat anti-inflamasi tanpa steroid (NSAID) yang sedang dipasarkan di Malaysia dengan 6 produk terdaftar. Model TxGNN telah **belum menjana petunjuk indikasi baru** untuk ubat ini, dan pakej bukti mengandungi jurang data yang ketara yang mesti ditangani sebelum penilaian penolokan semula ubat yang penuh boleh diteruskan.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|------|
| Indikasi Asal | NSAID — teks indikasi yang diluluskan khusus tidak tersedia dalam data semasa |
| Indikasi Baru yang Dijangkakan | — (Tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Data tidak mencukupi untuk penilaian) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 6 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pakej bukti. Berdasarkan pengetahuan farmakologi yang telah ditubuhkan dengan baik, Diclofenac potassium adalah penyekat siklooksigenase (COX-1/COX-2) yang tidak-selektif yang termasuk dalam kelas NSAID. Ia menghasilkan kesan terapeutiknya dengan menghalang sintesis prostaglandin, dengan itu mengurangkan keradangan, kesakitan, dan demam. Formulasi garam kalium menyediakan penyerapan yang lebih pantas berbanding dengan garam natrium.

Walau bagaimanapun, **tiada ramalan TxGNN telah dijana** untuk ubat ini. Susunan `predicted_indications` adalah kosong, bermaksud model sama ada belum dijalankan untuk Diclofenac potassium, atau ubat tidak berjaya dipetakan ke grafik pengetahuan. Tanpa indikasi yang dijangkakan, analisis kebolehplausibilan mekanistik tidak dapat diselesaikan.

Patut diambil perhatian bahawa Diclofenac dan kelas NSAID secara keseluruhan telah menjadi subjek penyelidikan penolokan semula ubat yang luas di seluruh dunia — khususnya dalam bidang seperti onkologi (pencegahan kanser kolorektal), penyakit Alzheimer, dan keadaan dermatologi tertentu — menunjukkan bahawa apabila saluran paip TxGNN dikonfigurasi dengan betul untuk ubat ini, ramalan yang bermakna mungkin muncul.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang berdaftar (tiada indikasi yang dijangkakan tersedia untuk carian bukti).

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia (tiada indikasi yang dijangkakan tersedia untuk carian bukti).

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* |

> **Nota:** Walaupun 6 pendaftaran produk telah dikenal pasti melalui pertanyaan NPRA (bertanya 2026-03-27), maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak ditangkap dalam pakej bukti semasa. Data ini perlu dikumpul semula daripada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Pakej bukti semasa tidak mengandungi data keselamatan yang diselesaikan (amaran, kontraindikasi, atau interaksi ubat-ubatan). Sebagai NSAID yang digunakan secara meluas, kebimbangan keselamatan utama secara umum termasuk risiko pendarahan gastrointestinal, peristiwa trombotik kardiovaskular, kemerosotan fungsi buah pinggang, dan reaksi hipersensitiviti — tetapi ini harus disahkan daripada sisipan pakej rasmi Malaysia.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pakej bukti jauh daripada lengkap — tiada indikasi yang dijangkakan TxGNN, tiada ID DrugBank yang diselesaikan, tiada data mekanisme tindakan, tiada maklumat keselamatan, dan tiada rekod lesen terperinci. Penilaian penolokan semula ubat yang bermakna tidak dapat dijalankan sehingga jurang data asas ini diisi.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Pemetaan DrugBank** — Selesaikan ID DrugBank untuk Diclofenac potassium (mungkin DB00586 untuk diklofenac; garam kalium harus dipetakan ke sebatian induk). Ini penting untuk ramalan berasaskan KG.
2. **Jalankan semula ramalan TxGNN** — Sebaik sahaja pemetaan DrugBank selesai, laksanakan saluran paip ramalan grafik pengetahuan dan pembelajaran mendalam untuk menghasilkan indikasi calon.
3. **Kumpul butir-butir lesen NPRA** — Bertanya semula pangkalan data NPRA untuk melengkapkan nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk kesemua 6 pendaftaran.
4. **Dapatkan data MOA** — Pertanyaan API DrugBank untuk maklumat mekanisme tindakan penuh, farmakodinamik, dan sasaran.
5. **Selesaikan data keselamatan** — Muat turun dan parsekan sisipan pakej Malaysia untuk mengekstrak maklumat amaran utama, kontraindikasi, dan interaksi ubat-ubatan.
6. **Pengumpulan bukti** — Sebaik sahaja indikasi yang dijangkakan tersedia, jalankan kolektor ClinicalTrials.gov, PubMed, dan ICTRP untuk mengumpul bukti sokongan.

---

*Penafian: Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Calon penolokan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

