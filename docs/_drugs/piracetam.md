---
layout: default
title: Piracetam
parent: Low Evidence (L4-L5)
nav_order: 551
evidence_level: L5
indication_count: 0
---

# Piracetam
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

# Piracetam: Penilaian Penyusunan Semula Ubat — Ramalan TxGNN Ditangguhkan

## Ringkasan Satu Ayat

Piracetam (DrugBank: DB09210) ialah agen nootropik yang kini memegang **9 kelulusan pemasaran** di Malaysia.
Pakej Bukti mengandungi **tiada ramalan penyusunan semula TxGNN**, dan data peringkat ubat yang kritikal — termasuk mekanisme kerja, teks petunjuk yang diluluskan, dan amaran keselamatan — tetap menjadi jurang data yang tertunggak.
Penilaian penyusunan semula yang lengkap **tidak dapat dilakukan** sehingga jurang-jurang ini diselesaikan.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak tersedia dalam data semasa |
| Petunjuk Baharu yang Diramalkan | Tiada (ramalan TxGNN belum dijana) |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A — tiada data ramalan tersedia |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Dicadangkan | **Tangguh** |

---

## Mengapa Tiada Ramalan Kini Tersedia

Medan `predicted_indications` dalam Pakej Bukti ini adalah kosong, bermakna saluran pemprosesan pengetahuan graf TxGNN dan pembelajaran dalam telah menghasilkan tiada petunjuk baharu calon untuk Piracetam. Tanpa petunjuk sasaran, penalaran mekanistik teras, semakan ujian klinikal, dan analisis kesusasteraan yang membentuk tulang belakang laporan penyusunan semula tidak dapat dijalankan.

Selain itu, data mekanisme kerja yang terperinci (MOA) ditandai sebagai jurang data berseveriti tinggi (DG002). Tanpa memahami cara Piracetam bertindak di peringkat molekul, tidak mungkin untuk menilai sama ada sebarang petunjuk yang diramalkan adalah munasabah dari segi farmakologi.

Setelah ramalan TxGNN dijana dan data MOA diambil daripada DrugBank, bahagian ini akan digantikan dengan nisbah mekanistik penuh yang menghubungkan petunjuk asal dan baharu.

---

## Maklumat Pasaran Malaysia

Sembilan kelulusan pemasaran telah disahkan melalui pertanyaan NPRA pada 2026-03-27. Walau bagaimanapun, rekod lesen individu — termasuk nama produk, bentuk dos, dan teks petunjuk yang diluluskan — tidak diisi dalam versi Pakej Bukti ini.

| Status | Perincian |
|--------|-----------|
| Lesen yang disahkan | 9 (sumber: NPRA, ditanya 2026-03-27) |
| Nama produk | Tidak diambil |
| Bentuk dos | Tidak diambil |
| Teks petunjuk yang diluluskan | Tidak diambil |

> **Tindakan diperlukan:** Ambil rekod lesen penuh daripada portal NPRA untuk mengisi perincian peringkat produk sebelum meneruskan.

---

## Pertimbangan Keselamatan

Sila rujuk risalah pakej untuk maklumat keselamatan. Amaran utama dan kontraindikasi belum diambil daripada PDF risalah pakej (jurang data DG001, keterukan: Halangan). Tiada interaksi ubat–ubat ditemui dalam pertanyaan semasa (kiraan DDI: 0), tetapi hasil ini harus ditafsirkan dengan berhati-hati sehingga risalah pakej penuh disemak.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguh**

**Alasan:**
Dua prasyarat untuk penilaian penyusunan semula — petunjuk sasaran yang diramalkan TxGNN dan data keselamatan/MOA ubat asas — kedua-duanya tidak hadir. Meneruskan tanpanya akan menghasilkan analisis tanpa asas bukti atau mekanistik.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Jalankan saluran pemprosesan ramalan TxGNN** untuk Piracetam (kaedah KG + DL) untuk menjana calon penyusunan semula dengan skor keyakinan
2. **Ambil MOA daripada API DrugBank** (DG002 — Keterukan Tinggi): pertanyaan DrugBank untuk mekanisme kerja, farmakoinamik, dan sasaran ubat
3. **Muat turun dan urai PDF risalah pakej TFDA/NPRA** (DG001 — Keterukan Halangan): ekstrak amaran utama, kontraindikasi, dan panduan penduduk khas
4. **Ambil rekod lesen NPRA penuh**: nama produk, bentuk dos, pengilang, dan teks petunjuk yang diluluskan untuk semua 9 kelulusan
5. **Jalankan semula penjanaan Pakej Bukti** (v5 atau lebih baru) dengan data di atas, kemudian janakan semula laporan ini

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penyusunan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

