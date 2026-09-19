---
layout: default
title: Articaine Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 90
evidence_level: L5
indication_count: 0
---

# Articaine Hydrochloride
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

# Articaine Hydrochloride: Anestesi Lokal Gigi — Penilaian Ubat Repurposing

## Ringkasan Satu Ayat

Articaine Hydrochloride ialah anestesi lokal jenis amida yang digunakan terutamanya dalam pergigian untuk anestesi infiltrasi dan blok saraf semasa prosedur pergigian.
Model TxGNN **tidak menghasilkan sebarang ramalan ubat baru** untuk sebatian ini dalam pakej bukti semasa, kemungkinan disebabkan oleh penghubungan DrugBank yang tidak mencukupi atau ketiadaan ubat ini dalam nod graf pengetahuan yang aktif.
Dengan **tiada bukti uji klinik** dan **tiada bukti sastera** yang diperoleh untuk petunjuk baru, penilaian ini berfungsi sebagai dokumentasi jurang data dan bukannya cadangan ubat baru.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Anestesi lokal pergigian (infiltrasi & blok saraf) |
| Petunjuk Baru Dijangka | — (Tiada ramalan dihasilkan) |
| Skor Ramalan TxGNN | — (Tiada ramalan dihasilkan) |
| Tahap Bukti | L5 — Ramalan model tidak tersedia; tiada kajian sokongan |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Masuk Akal?

Tiada ramalan ubat baru yang dihasilkan oleh TxGNN untuk Articaine Hydrochloride dalam pakej bukti ini. Sebab-sebab yang paling berkemungkinan ialah:

1. **DrugBank ID tidak diselesaikan**: Medan `drugbank_id` adalah nul dalam Pakej Bukti, bermakna ubat tidak dapat diletakkan pada nod dalam graf pengetahuan TxGNN (KG). Tanpa nod KG yang sah, tiada ramalan pautan dapat dilakukan.

2. **Profil farmakologi yang sempit**: Articaine ialah anestesi lokal khusus pergigian. Tidak seperti ubat sistemik dengan interaksi reseptor yang luas, mekanisme utamanya — penyekat saluran natrium bersara (Nav) pada terminal saraf tepi — mempunyai tapak tindakan yang sangat terlokalisasi, mengehadkan ruang kebolehpercayaan biologi untuk ubat baru sistemik.

3. **Jurang data hadir**: Kedua-dua mekanisme tindakan (MOA) dan butiran lesen NPRA tidak berjaya diekstrak daripada data sumber, seterusnya mengehadkan keupayaan model untuk menghasilkan ramalan yang bersandar pada konteks.

Sehingga DrugBank ID disahkan dan ubat dipetakan ke dalam KG, tiada penilaian ubat baru berasaskan bukti dapat disiapkan.

---

## Bukti Uji Klinik

Pada masa ini tiada uji klinik yang didaftarkan yang berkaitan untuk petunjuk baru (bukan pergigian) Articaine Hydrochloride.

---

## Bukti Sastera

Pada masa ini tiada sastera yang tersedia untuk ubat baru Articaine Hydrochloride selain petunjuk pergigian yang diluluskan.

---

## Maklumat Pasaran Malaysia

Pakej Bukti mengesahkan **3 pendaftaran yang aktif** di bawah NPRA, tetapi medan lesen butiran (nombor pendaftaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak berjaya diekstrak dalam tarikan data semasa. Jadual di bawah mencerminkan data yang tersedia:

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------------------|-------------|------------|-------------------|
| — | — | — | Butiran tidak diekstrak (pertanyaan NPRA mengembalikan 3 rekod; data mentah perlu diurai semula) |

**Tindakan diperlukan**: Jalankan semula saluran paip pengekstrakan data NPRA untuk mengisi medan aras lesen bagi ubat ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan bungkusan untuk maklumat keselamatan. Tiada amaran, kontraindikasi, atau data interaksi ubat tersedia dalam Pakej Bukti semasa.

> **Nota untuk apoteker klinikal**: Articaine secara amnya diketahui membawa risiko methemoglobinaemia dan toksisiti CNS/kardiovaskular pada dos tinggi, biasa untuk semua anestesi lokal amida. Ini harus disahkan dengan sisipan pakej berdaftar Malaysia sebelum sebarang penggunaan klinikal.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada ramalan ubat baru TxGNN dihasilkan kerana DrugBank ID yang tidak diselesaikan dan sambungan KG yang hilang; tanpa nod graf yang sah, tiada inferens ubat baru bermakna dapat dibuat untuk Articaine Hydrochloride pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **Selesaikan DrugBank ID**: Cari DrugBank untuk "Articaine" (berkemungkinan DB00348) dan sahkan pemetaan; jalankan semula ramalan KG dengan ID yang disahkan.
- **Ekstrak butiran lesen NPRA**: Urai semula respons NPRA mentah untuk mengisi nama produk, bentuk dos, dan teks petunjuk yang diluluskan bagi 3 produk berdaftar.
- **Peroleh data MOA**: Pertanyaan API DrugBank dengan ID yang disahkan untuk mendapatkan mekanisme tindakan dan sasaran farmakologi.
- **Muat turun sisipan pakej Malaysia**: Ambil daripada e-daftar NPRA untuk mengisi medan amaran keselamatan dan butiran kontraindikasi.
- **Jalankan semula penjanaan Pakej Bukti**: Selepas menyelesaikan jurang di atas (DG001, DG002), hasilkan semula Pakej Bukti pada v5 dan nilai semula untuk calon ubat baru.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

