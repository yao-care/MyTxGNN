---
layout: default
title: Lisinopril Dihydrate
parent: Low Evidence (L4-L5)
nav_order: 448
evidence_level: L5
indication_count: 0
---

# Lisinopril Dihydrate
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

# Lisinopril Dihydrate: Penilaian Ubat Baru dari Ubat Lama — Menunggu Data Lengkap

## Ringkasan Satu Ayat

Lisinopril dihydrate adalah produk farmaseutikal berdaftar di Malaysia dengan 3 kebenaran pemasaran aktif, disahkan oleh rekod NPRA.
Walau bagaimanapun, Evidence Pack semasa adalah **amat tidak lengkap**: tiada ramalan ubat baru dari ubat lama TxGNN telah dijana, dan kedua-dua mekanisme tindakan dan butiran indikasi yang diluluskan tidak ada.
Laporan ini mendokumentasikan keadaan data semasa dan menggariskan langkah-langkah wajib sebelum penilaian ubat baru dari ubat lama yang lengkap dapat diteruskan.

---

## Ikhtisar Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak diambil daripada data semasa |
| Indikasi Baru yang Diramalkan | Tiada ramalan yang dijana |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Tiada ramalan lagi — saluran paip model belum dijalankan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 3 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Masuk Akal?

Tiada ramalan ubat baru dari ubat lama TxGNN yang tersedia bagi lisinopril dihydrate. Log pertanyaan mengesahkan bahawa DrugBank telah dipertanyakan dengan berjaya dan mengembalikan 1 hasil, tetapi ID DrugBank tidak diisi dalam set data. Tanpa ID DrugBank yang sah, saluran paip ramalan graf pengetahuan (KG) dan pembelajaran mendalam (DL) tidak dapat mengenal pasti calon indikasi baru — ini adalah punca utama medan `predicted_indications` yang kosong.

Mekanisme tindakan (MOA) juga ditandai sebagai jurang data berat sebelah. Tanpa maklumat MOA, mustahil untuk menilai sama ada laluan farmakologi lisinopril relevan secara mekanis dengan sebarang indikasi calon, yang merupakan prasyarat untuk sebarang tuntutan ubat baru dari ubat lama yang dapat dipertahankan secara saintifik.

Selain itu, 3 rekod lesen NPRA telah diambil dari segi jumlah, tetapi semua medan berstruktur (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak diisi, menjadikan mustahil untuk mewujudkan bahkan skop terapeutik yang diluluskan semasa di Malaysia. Semua analisis yang lebih penting ditangguhkan sehingga jurang-jurang ini diselesaikan.

---

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan 3 pendaftaran aktif untuk lisinopril dihydrate di Malaysia. Maklumat lesen terperinci tidak ditangkap dalam tarik data semasa dan mesti diambil dalam kitaran berikutnya.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|------------|-----------|------------------------|
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |

---

## Pertimbangan Keselamatan

Sila rujuk risalah pakej untuk maklumat keselamatan yang lengkap. Data amaran risalah pakej, kontraindikasi, dan interaksi ubat tidak diambil dalam kitaran ini dan diperlukan sebelum sebarang saringan keselamatan pra dapat dilakukan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Evidence Pack kehilangan dua masukan paling penting untuk penilaian ubat baru dari ubat lama — ramalan TxGNN dan butiran indikasi yang diluluskan — menjadikan mustahil untuk menilai sama ada kebolehplausibilitasan saintifik mahupun landskap kawal selia untuk sebarang indikasi baru pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Menyekat — DG001]** Ambil risalah pakej NPRA/TFDA untuk lisinopril dihydrate: muat turun PDF monografi produk dan ekstrak amaran dan kontraindikasi untuk membolehkan saringan keselamatan pra
- **[Tinggi — DG002]** Petakan hasil pertanyaan DrugBank yang disahkan ke ID DrugBank dalam set data, kemudian ambil catatan MOA yang lengkap untuk menyokong analisis kebolehplausibilitasan mekanis
- **[Diperlukan]** Jalankan semula saluran paip ramalan KG dan DL TxGNN dengan ID DrugBank yang betul untuk mengisi `predicted_indications`
- **[Diperlukan]** Ambil butiran pendaftaran NPRA yang lengkap untuk semua 3 lesen — nombor kebenaran, nama produk, bentuk dos, dan indikasi yang diluluskan
- **[Langkah akhir]** Janakan semula Evidence Pack (v5+) dan keluarkan semula laporan penilaian ini setelah semua jurang data di atas diselesaikan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

