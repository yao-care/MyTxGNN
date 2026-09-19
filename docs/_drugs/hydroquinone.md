---
layout: default
title: Hydroquinone
parent: Low Evidence (L4-L5)
nav_order: 386
evidence_level: L4
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **4** 
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

# HYDROQUINONE: Dari [Indikasi Tidak Ditentukan] ke Seborrheic Keratosis

## Ringkasan Satu Ayat

> Hydroquinone (DrugBank DB09526) adalah agen topikal yang telah dipasarkan dengan teks indikasi asli formal tidak ditangkap dalam paket bukti saat ini, meskipun bukti beranotasi menjelaskan hal itu sebagai penghambat tirosinase yang digunakan dalam kondisi kulit berpigmen.
> Model TxGNN memprediksi hal itu mungkin efektif untuk **Seborrheic Keratosis**, tetapi ini saat ini didukung oleh **0 uji klinis** dan hanya **2 publikasi**, keduanya terkait dengan subtipe berpigmen (dermatosis papulosa nigra) daripada seborrheic keratosis itu sendiri.

---

## Ikhtisar Cepat

| Kategori | Deskripsi |
|------|------|
| Original Indication | Tidak tersedia — TFDA/NPRA license `approved_indication_text` kosong dalam paket bukti ini |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Malaysia Market Status | ✓ Telah dipasarkan |
| Number of Registrations | 3 |
| Recommended Decision | Tunda |

---

## Mengapa Prediksi Ini Masuk Akal?

Data mekanisme kerja resmi tidak tersedia dalam paket bukti ini (Kesenjangan Data DG002, keparahan Tinggi). Berdasarkan anotasi yang tertanam dalam bukti, hydroquinone bertindak sebagai **penghambat tirosinase**, mengurangi sintesis melanin — mekanisme yang konsisten dengan peran terkenal dalam terapi topical pigmentasi/depigmentasi (hal ini juga tercermin secara tidak langsung dalam bukti uji klinis yang dikumpulkan untuk kandidat lain dalam paket ini, yang didominasi oleh uji klinis melasma).

Relevansi terhadap seborrheic keratosis adalah sempit dan tidak langsung. Seborrheic keratosis pada dasarnya adalah lesi jinak dengan proliferasi keratinosit, suatu proses yang tidak dipengaruhi oleh mekanisme penghambatan tirosinase hydroquinone. Hubungan yang mungkin adalah dengan **dermatosis papulosa nigra (DPN)** — varian seborrheic keratosis yang berpigmen dan tersebar di wajah, umum pada populasi dengan kulit berwarna — di mana pigmentasi berlebih (bukan proliferasi keratinosit) adalah ciri yang dapat diobati.

Oleh karena itu, rasionalisasi mekanisme paling banyak mendukung subset presentasi seborrheic keratosis (lesi wajah berpigmen pada pasien dengan kulit berwarna), bukan kategori penyakit secara keseluruhan. Skor TxGNN (99.73%) mencerminkan asosiasi tingkat grafik yang kuat tetapi belum dikonfirmasi oleh studi klinis atau mekanistik yang spesifik penyakit.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar.

---

## Bukti Literatur

| PMID | Tahun | Tipe | Jurnal | Temuan Utama |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Kohort | J Plast Reconstr Aesthet Surg | Studi observasi prospektif pada pasien Asia yang mengusulkan algoritma terapi kombinasi untuk gangguan pigmentasi wajah; tidak spesifik untuk seborrheic keratosis. |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Tinjauan | J Drugs Dermatol | Meninjau opsi pengobatan untuk dermatosis papulosa nigra (DPN), varian seborrheic keratosis berpigmen yang umum pada pasien Afrika-Amerika/Afrika-Karibia; mencatat bahwa histologi DPN sangat mirip dengan seborrheic keratosis. |

---

## Informasi Pasar Malaysia

Catatan NPRA menunjukkan **3 registrasi aktif** untuk hydroquinone, tetapi nomor lisensi, nama produk, bentuk sediaan, pabrikan, dan teks indikasi yang disetujui tidak diisi dalam ekstraksi paket bukti ini.

| Nomor Otorisasi | Nama Produk | Bentuk Sediaan | Indikasi yang Disetujui |
|---------|------|------|-----------|
| Tidak tersedia (3 lisensi pada file) | Tidak tersedia | Tidak tersedia | Tidak tersedia |

---

## Pertimbangan Keamanan

Silakan merujuk ke insert kemasan untuk informasi keamanan.

*(Catatan: pengambilan peringatan label TFDA/NPRA dan kontraindikasi adalah kesenjangan data Pemblokir — DG001 — dan diperlukan sebelum evaluasi keamanan apa pun dapat dilanjutkan; lihat Kesimpulan.)*

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tunda**

**Rasionalisasi:**
- Seborrheic keratosis tidak memiliki dukungan uji klinis langsung, dan kedua publikasi pendukung hanya terkait dengan subtipe berpigmen (DPN), bukan patologi proliferasi keratinosit yang mendasari penyakit.
- Peringatan/kontraindikasi insert kemasan hilang (DG001, keparahan Pemblokir) — menurut kebijakan paket bukti, hal ini sendiri memblokir masuk ke tahap tinjauan keamanan S1.

**Untuk melanjutkan, hal berikut diperlukan:**
- Ambil peringatan insert kemasan NPRA dan kontraindikasi (DG001)
- Peroleh catatan mekanisme kerja DrugBank formal (DG002)
- Isi detail lisensi Malaysia lengkap (nama produk, bentuk sediaan, teks indikasi) untuk 3 registrasi yang ada
- Jelaskan apakah indikasi yang diprediksi harus dipersempit khusus ke DPN/seborrheic keratosis berpigmen daripada kategori penyakit yang lebih luas
- Catatan: kandidat peringkat lain dalam paket ini (misalnya, "exanthem," peringkat 3) menunjukkan ketidaksesuaian label-penyakit yang jelas dalam bukti uji klinis mereka (uji klinis melasma dipetakan ke node penyakit yang tidak terkait) — perlu tinjauan pemetaan grafik pengetahuan sebelum penggunaan lebih lanjut dari set kandidat ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

