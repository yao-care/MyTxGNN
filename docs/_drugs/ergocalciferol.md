---
layout: default
title: Ergocalciferol
parent: Low Evidence (L4-L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Ergocalciferol: Dari Indikasi Asal yang Tidak Tercatat hingga Kekurangan Vitamin D yang Sudah Ketinggalan Zaman

## Ringkasan Satu Kalimat

Ergocalciferol (vitamin D2) adalah produk yang telah lama dipasarkan di Malaysia (10 pendaftaran NPRA yang aktif), tetapi paket bukti ini tidak mengandung catatan yang dapat digunakan mengenai teks indikasi yang resmi disetujui. Prediksi peringkat teratas model TxGNN — **kekurangan vitamin D yang sudah ketinggalan zaman** — didukung oleh **nol uji klinis dan nol kutipan literatur**, dan teks rasional model sendiri menandainya sebagai kemungkinan besar re-identifikasi penggunaan yang sudah dikenal dan sudah disetujui dari obat itu sendiri daripada indikasi repurposing yang benar-benar baru.

---

## Gambaran Umum Cepat

| Item | Konten |
|------|--------|
| Indikasi Asal | Tidak ada di file — semua kolom teks indikasi lisensi NPRA dan kolom tingkat obat `original_indications` kosong dalam paket bukti ini |
| Indikasi Baru yang Diprediksi | Kekurangan Vitamin D yang Sudah Ketinggalan Zaman* |
| Skor Prediksi TxGNN | 99.99% |
| Tingkat Bukti | L5 (nol uji klinis, nol literatur — lihat catatan di bawah) |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 10 |
| Keputusan yang Direkomendasikan | Tunda |

*"Ketinggalan zaman" di sini adalah istilah ontologi penyakit itu sendiri (MONDO/OMIM menandainya sebagai konsep yang tidak digunakan lagi), dan `repurposing_rationale` model sendiri menyatakan bahwa ini kemungkinan besar adalah re-deteksi indikasi ergocalciferol yang dikenal daripada kandidat repurposing yang sebenarnya.

**Catatan tentang Tingkat Bukti:** kolom penilaian internal paket bukti ini memberi label kandidat ini "L1," tetapi sesuai dengan aturan penentuan (L1 memerlukan ≥2 RCT Phase 3 yang diselesaikan) dan fakta bahwa kedua array `clinical_trials` dan `literature` kosong untuk kandidat ini, tingkat yang benar menurut kriteria yang dinyatakan adalah **L5**. Perbedaan ini harus diperbaiki di hulu dalam saluran penilaian.

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme aksi yang terperinci tidak tersedia (ditandai sebagai celah data berkeparahan Tinggi, DG002). Berdasarkan pengetahuan farmakologis umum, ergocalciferol (vitamin D2) adalah prekursor vitamin D yang larut dalam lemak yang menjalani hidroksilasi hepatik 25 dan hidroksilasi renal 1α menjadi metabolitnya yang aktif, calcitriol, yang mengatur absorpsi kalsium/fosfat usus dan mineralisasi tulang. Jalur ini sudah mapan dan merupakan dasar farmakologis untuk pada dasarnya semua kandidat yang muncul dalam paket ini.

Kandidat peringkat teratas, bagaimanapun, bukanlah sinyal repurposing yang berguna: istilah penyakit "kekurangan vitamin D yang sudah ketinggalan zaman" itu sendiri adalah indikasi asli ergocalciferol yang terkenal di buku teks, dan rasional model sendiri secara eksplisit menyatakan bahwa skor tinggi kemungkinan besar mencerminkan "fakta farmakologis yang sudah dikenal, bukan penemuan baru" — sebuah artefak yang kemungkinan besar disebabkan oleh hilangnya data `original_indications`, yang membuat TxGNN tidak mampu membedakan kandidat ini dari penggunaan ergocalciferol yang dikenal.

Melampaui peringkat 1, beberapa kandidat peringkat lebih rendah menunjukkan pola repurposing yang lebih sejati dan didukung bukti — ergocalciferol digunakan sebagai adjuvan dalam gangguan tulang metabolisme kalsium/fosfat yang berdekatan dengan indikasi intinya: **osteodistrofi renal** (peringkat 9, L2, satu uji Phase 4 ditambah studi klinis perbandingan langsung 1985 tentang ergocalciferol vs. calcitriol), **rakitis hipofosfatemik herediter** (peringkat 7, L3, termasuk studi klinis NEJM 1980 yang menggunakan ergocalciferol secara langsung), dan **hipofosfatemia** (peringkat 8, L3, termasuk uji dosis ergocalciferol yang sedang direncanakan, NCT07366450). Ini adalah koherensi mekanistik dan layak untuk evaluasi terpisah, meskipun praktik modern sebagian besar telah beralih ke analog vitamin D aktif (calcitriol/doxercalciferol) untuk kondisi ini.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar.

---

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia.

---

## Pertimbangan Keselamatan

Silakan merujuk ke risalah obat untuk informasi keselamatan.

(Peringatan/kontraindikasi TFDA/NPRA tidak tersedia dalam paket bukti ini — ini ditandai sebagai celah data berkeparahan **Pemblokiran**, DG001, dan mencegah kandidat ini memasuki tahap tinjauan keselamatan S1 terlepas dari bukti efikasi.)

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tunda**

**Rasional:**
Kandidat peringkat teratas tidak memiliki dukungan uji klinis atau literatur, dan rasional paket bukti sendiri menunjukkan bahwa ini kemungkinan besar menduplikasi penggunaan ergocalciferol yang sudah disetujui yang sudah ada daripada mewakili indikasi baru. Terpisah, celah data keselamatan Pemblokiran (tidak ada label peringatan/kontraindikasi TFDA/NPRA di file) mencegah kandidat apa pun untuk obat ini dari menghapus skrining keselamatan awal.

**Untuk melanjutkan, hal berikut diperlukan:**
- Selesaikan DG001 (Pemblokiran): ambil dan urai risalah obat NPRA untuk peringatan/kontraindikasi
- Selesaikan DG002 (Tinggi): kueri DrugBank untuk mekanisme aksi yang dikonfirmasi
- Dapatkan teks indikasi yang disetujui obat sebenarnya — semua 10 catatan lisensi NPRA saat ini dalam paket ini memiliki nama produk, bentuk dosis, dan kolom indikasi yang kosong
- Jika peluang repurposing yang sebenarnya masih diinginkan, alihkan upaya tinjauan ke peringkat 7–9 (rakitis hipofosfatemik herediter, hipofosfatemia, osteodistrofi renal), yang memiliki bukti nyata — meskipun sudah ketinggalan zaman — daripada peringkat 1

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

