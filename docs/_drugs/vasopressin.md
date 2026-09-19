---
layout: default
title: Vasopressin
parent: Low Evidence (L4-L5)
nav_order: 685
evidence_level: L4
indication_count: 2
---

# Vasopressin
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **2** 
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

# Vasopressin: Dari Indikasi Asal yang Tidak Terdokumentasi hingga Kekurangan Protrombin Bawaan (Ramalan Kepercayaan Rendah)

## Ringkasan Satu Kalimat

Vasopressin (DrugBank DB00067) dipasarkan di Malaysia di bawah 2 pendaftaran, tetapi teks indikasi asal yang disetujui dan mekanisme kerja saat ini tidak tersedia dalam set data ini. Model TxGNN memprediksi kemungkinan hubungan dengan **Kekurangan Protrombin Bawaan**, tetapi 3 publikasi pendukung utama adalah laporan kasus/ulasan tentang gangguan yang berbeda (hemofilia A didapat dan kekurangan Faktor V/VIII gabungan), tanpa **uji klinis** dan kekhawatiran mekanistik yang terdokumentasi bahwa model mungkin telah mengacaukan vasopressin dengan analogue-nya desmopressin (DDAVP).

---

## Tinjauan Cepat

| Item | Konten |
|------|--------|
| Indikasi Asal | Tidak tersedia dalam set data saat ini |
| Indikasi Baru yang Diprediksi | Kekurangan Protrombin Bawaan |
| Skor Prediksi TxGNN | 99.63% |
| Tingkat Bukti | L4 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 2 |
| Keputusan yang Direkomendasikan | Tunda |

---

## Mengapa Prediksi Ini Wajar?

Saat ini, data mekanisme kerja terperinci untuk vasopressin tidak tersedia dalam set data ini. Berdasarkan farmakologi umum, vasopressin (AVP) bertindak terutama pada reseptor V1/V2 dan digunakan secara klinis untuk diabetes insipidus, perdarahan varises gastrointestinal, dan syok vasodilatasi (septik).

Paket bukti sendiri meningkatkan kekhawatiran signifikan daripada mengkonfirmasi kelayakan: literatur pendukung sebenarnya menyangkut **desmopressin (DDAVP)**, analogue sintetis vasopressin yang bekerja pada reseptor V2 untuk memicu pelepasan von Willebrand Factor dan Faktor VIII dari endotel — mekanisme yang digunakan dalam keadaan kekurangan Faktor VIII/vWF, bukan kekurangan protrombin (Faktor II). Protrombin tidak disimpan di badan Weibel-Palade dan tidak dilepaskan oleh stimulasi DDAVP. Rasionalisasi secara eksplisit mencatat bahwa link yang diprediksi ini mungkin mencerminkan grafik pengetahuan yang mengacaukan vasopressin dengan analogue-nya DDAVP, atau kedekatan antar node faktor koagulasi, daripada hubungan farmakologis yang sebenarnya.

Mengingat hal ini, prediksi harus diperlakukan sebagai hipotesis yang dihasilkan oleh kedekatan grafik daripada sinyal yang berdasarkan mekanisme.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar

---

## Bukti Literatur

| PMID | Tahun | Tipe | Jurnal | Temuan Utama |
|------|------|------|--------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Ulasan | Autoimmunity reviews | Mengulas hemofilia A didapat (autoantibodi terhadap Faktor VIII), gangguan yang berbeda dari kekurangan protrombin bawaan; tidak membahas peran vasopressin dalam kekurangan protrombin. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Laporan Kasus | Rinsho Ketsueki (Jpn J Clin Hematol) | Kasus pemberian DDAVP pada kekurangan Faktor V dan Faktor VIII bawaan gabungan — bukan kekurangan protrombin. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Laporan Kasus | Rinsho Ketsueki (Jpn J Clin Hematol) | Pengiriman sesar yang dikelola dengan penggantian Faktor VIII dalam pasien dengan kekurangan Faktor V/VIII gabungan — sekali lagi bukan kekurangan protrombin. |

**Catatan:** Tidak ada literatur yang diidentifikasi langsung mempelajari vasopressin (atau DDAVP) dalam kekurangan protrombin bawaan; ketiga referensi menyangkut gangguan faktor koagulasi yang berbeda (Faktor V/VIII), yang merupakan dasar untuk kekhawatiran mekanistik yang dikemukakan di atas.

---

## Informasi Pasar Malaysia

Malaysia memiliki 2 pendaftaran vasopressin aktif (status pasar: ✓ Dipasarkan), tetapi nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui saat ini tidak tersedia dalam set data ini.

---

## Pertimbangan Keselamatan

Silakan lihat paket sisipan untuk informasi keselamatan.

*(Catatan: Peringatan label TFDA/NPRA dan kontraindikasi ditandai dalam paket bukti ini sebagai kesenjangan data **Pemblokiran** — lihat Kesimpulan di bawah.)*

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tunda**

**Rasionalisasi:**
- Indikasi yang diprediksi (kekurangan protrombin bawaan) kekurangan dukungan uji klinis apa pun, dan literatur pendukung sebenarnya membahas gangguan yang berbeda dan secara mekanistik berbeda (kekurangan Faktor V/VIII yang dirawat dengan DDAVP, bukan vasopressin itu sendiri). Analisis paket bukti sendiri menunjukkan prediksi mungkin berasal dari kebingungan grafik pengetahuan antara vasopressin dan analogue-nya desmopressin daripada relevansi obat-penyakit yang sebenarnya.
- Secara terpisah, kesenjangan data **Pemblokiran** (peringatan label TFDA/NPRA dan kontraindikasi yang hilang) mencegah kandidat ini memasuki tahap pra-penilaian keselamatan S1 terlepas dari bukti kemanjuran apa pun.

**Untuk melanjutkan, yang berikut ini diperlukan:**
- Peringatan label asli/kontraindikasi dari NPRA/TFDA (saat ini kesenjangan data Pemblokiran)
- Data mekanisme kerja yang dikonfirmasi melalui DrugBank (saat ini kesenjangan data dengan tingkat keparahan Tinggi)
- Klarifikasi apakah rasionalisasi mekanistik sebaiknya mengarah ke desmopressin (DDAVP) daripada vasopressin, mengingat dasar literaturnya
- Jika ditindaklanjuti, farmakologi primer/bukti praklinik yang langsung menghubungkan vasopressin (bukan DDAVP) dengan sintesis atau aktivitas protrombin

**Kandidat tambahan (prioritas lebih rendah):** Prediksi kedua, *osteoporosis yang diinduksi obat* (skor TxGNN 99.62%), juga ditandai tetapi tidak memiliki uji klinis atau dukungan literatur sama sekali (Tingkat Bukti L5) dan sama-sama direkomendasikan untuk **Tunda**.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

