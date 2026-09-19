---
layout: default
title: Alverine Citrate
parent: Low Evidence (L4-L5)
nav_order: 49
evidence_level: L5
indication_count: 0
---

# Alverine Citrate
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

# ALVERINE CITRATE: Penilaian Ubah Guna Ubat — Data Tidak Mencukupi untuk Prediksi

## Ringkasan Satu Ayat

Alverine Citrate adalah penenang otot licin (antispasmodik) yang berdaftar di Malaysia, biasanya ditunjukkan untuk keram gastrointestinal dan sindrom usus terrangsang (IBS). Namun, Paket Bukti semasa **tidak mengandungi indikasi baru yang diramalkan oleh TxGNN**, dan medan data kritikal — termasuk mekanisme tindakan dan teks indikasi yang diluluskan — tidak tersedia. **Laporan ini tidak dapat diteruskan ke penilaian ubah guna penuh sehingga jurang data kritikal diselesaikan.**

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak tersedia dalam Paket Bukti semasa |
| Indikasi Baru yang Diramalkan | Tiada — prediksi TxGNN belum disiapkan |
| Skor Prediksi TxGNN | Tidak Terpakai |
| Tahap Bukti | L5 (ramalan model sahaja — belum dijalankan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Dicadangkan | **Tunggu** |

---

## Mengapa Prediksi Ini Munasabah?

Pada masa ini, tiada indikasi yang diramalkan oleh TxGNN yang tersedia untuk Alverine Citrate dalam Paket Bukti ini. Tatasusunan `predicted_indications` adalah kosong, yang bermaksud saluran paip prediksi graf pengetahuan dan pembelajaran mendalam belum menghasilkan keluaran untuk sebatian ini.

Selain itu, data mekanisme tindakan terperinci (MOA) tidak ada. Berdasarkan pengetahuan farmakologi am, Alverine Citrate adalah penenang otot licin kelas antispasmodik, bertindak pada otot licin viseral untuk menghilangkan kejang. Kegunaannya yang terbukti dalam keadaan kejang gastrointestinal dan ginekologi memberikan asas mekanistik untuk ubah guna berpotensi ke dalam gangguan motilitas yang berkaitan atau kesakitan — tetapi analisis ini tidak dapat dijalankan secara formal tanpa melengkapkan saluran paip prediksi.

**Tiada analisis mekanistik atau berkaitan indikasi lanjut boleh dilakukan sehingga Paket Bukti dilengkapkan.**

---

## Bukti Uji Klinis

Pada masa ini tiada uji klinis berkaitan yang berdaftar dalam Paket Bukti ini.

*(Sebab: Tiada indikasi yang diramalkan tersedia untuk mendasarkan carian uji.)*

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia dalam Paket Bukti ini.

*(Sebab: Tiada indikasi yang diramalkan tersedia untuk mendasarkan carian literatur.)*

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|-------------|-----------|-------------------------|
| — | — | — | — |
| — | — | — | — |

> **Nota:** 2 pendaftaran disahkan dalam pangkalan data pengawal selia Malaysia (status pasaran: Dipasarkan), tetapi nama produk, bentuk dos, dan teks indikasi yang diluluskan tidak diambil dalam tarik data ini. Pertanyaan semula pangkalan data NPRA atau mengakses rekod produk individu diperlukan.

---

## Pertimbangan Keselamatan

Sila rujuk kepada lembaran maklumat produk untuk maklumat keselamatan.

> **Notis Jurang Data:** Kedua-dua amaran utama dan kontraindikasi mengembalikan `[Jurang Data]` dalam Paket Bukti ini (diklasifikasikan sebagai keterukan **Halangan**). Tiada rekod interaksi ubat-ubat ditemui. Penilaian keselamatan tidak dapat diteruskan sehingga lembaran maklumat produk TFDA/NPRA diambil dan dianalisis.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Rasional:**
Paket Bukti untuk Alverine Citrate sangat tidak lengkap — tiada indikasi yang diramalkan oleh TxGNN, tiada data MOA, tiada teks indikasi yang diluluskan, dan tiada maklumat keselamatan. Penilaian ubah guna yang bermakna tidak dapat dijalankan dalam keadaan ini.

**Untuk meneruskan, yang berikut diperlukan:**

- [ ] **[Halangan — DG001]** Muat turun dan analisis PDF lembaran maklumat produk TFDA/NPRA untuk mengeluarkan indikasi yang diluluskan, amaran utama, dan kontraindikasi
- [ ] **[Tinggi — DG002]** Pertanyaan API DrugBank menggunakan INN "alverine citrate" untuk mendapatkan DrugBank ID, MOA, farmakodinamik, dan kategori ubat
- [ ] **[Diperlukan]** Jalankan semula saluran paip prediksi KG dan DL TxGNN dengan DrugBank ID yang dipetakan dengan betul untuk melengkapkan `predicted_indications`
- [ ] **[Diperlukan]** Pertanyaan semula rekod produk NPRA untuk mengisi nombor lesen, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk 2 pendaftaran yang disahkan
- [ ] **[Pilihan]** Sahkan ejaan INN dan nama alternatif (cth., "Alverine", "Alverin sitrat") untuk meningkatkan liputan pemetaan merentas semua pengumpul

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

