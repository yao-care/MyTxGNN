---
layout: default
title: Amoxycillin Sodium
parent: Low Evidence (L4-L5)
nav_order: 67
evidence_level: L5
indication_count: 0
---

# Amoxycillin Sodium
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

# Amoxycillin Sodium: Kajian Status Kawal Selia — Tiada Ramalan Ubah Tujuan Rawatan Tersedia

## Ringkasan Satu Ayat

Amoxycillin Sodium adalah antibiotik spektrum luas kelas penisilin yang digunakan secara meluas untuk infeksi bakteria termasuk infeksi saluran pernafasan, saluran kencing, dan infeksi kulit.
Model TxGNN **tidak menghasilkan sebarang ramalan ubah tujuan rawatan** untuk ubat ini dalam larian semasa — laporan ini mendokumenkan status kawal selia Malaysia dan menggariskan jurang data yang mesti diselesaikan sebelum analisis ubah tujuan rawatan dapat diselesaikan.
**Tiada bukti ujian klinikal atau literatur untuk petunjuk baru tersedia pada masa ini.**

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Infeksi bakteria (antibiotik spektrum luas; butiran surat paket belum diambil) |
| Petunjuk Ubah Tujuan Ramalan | Tiada — tiada ramalan TxGNN dihasilkan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A (tiada ramalan tersedia) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan ubah tujuan rawatan yang dihasilkan oleh TxGNN untuk Amoxycillin Sodium dalam larian ini. Oleh itu, pautan mekanistik antara petunjuk baru dan penggunaan asal ubat tidak boleh ditetapkan pada peringkat ini.

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia dalam sistem. Berdasarkan pengetahuan farmakologi umum, Amoxycillin Sodium adalah antibiotik beta-laktam spektrum luas yang tergolong dalam kelas penisilin. Ia memberikan kesannya yang antibakteria dengan menghalang sintesis dinding sel bakteria melalui pengikatan kepada protein pengikat penisilin (PBP), yang akhirnya membawa kepada lisis sel. Petunjuk yang ditetapkan termasuk infeksi saluran pernafasan, saluran kencing, kulit, dan tisu lembut, antara lain.

Sebelum analisis ubah tujuan rawatan dapat diteruskan, rekod DrugBank mesti dipautkan (ID DrugBank pada masa ini hilang), MOA mesti ditangkap secara rasmi dalam sistem, dan saluran paip TxGNN mesti dijalankan semula dengan pemetaan entiti ubat yang betul untuk menghasilkan petunjuk calon.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|-----------------|------------|----------|----------------------|
| — | — | — | — |

> **Nota:** Walaupun 1 pendaftaran aktif dicatat dalam sistem, semua butiran peringkat produk (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) tidak diambil dalam penghausan data semasa. Sila kueri portal pencarian produk NPRA secara langsung (https://www.npra.gov.my/) untuk mendapatkan rekod lesen penuh.

---

## Pertimbangan Keselamatan

Sila rujuk surat paket untuk maklumat keselamatan yang lengkap. Tiada data DDI, amaran utama, atau kontraindikasi yang tersedia dalam paket bukti semasa.

Sebagai nota umum, Amoxycillin dikontraindikasikan pada pesakit dengan kepekaan yang diketahui kepada antibiotik beta-laktam (penisilin, sefalosporin). Interaksi yang relevan secara klinikal termasuk kesan antibiotik yang berkurangan bagi ubat pencegah kehamilan oral dan risiko pendarahan yang meningkat dengan antikoagulan — ini harus disahkan terhadap surat paket yang berdaftar secara rasmi di Malaysia.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Nisbah:**
Saluran paip TxGNN tidak menghasilkan sebarang calon ubah tujuan rawatan untuk Amoxycillin Sodium, dan input data yang penting (pautaan ID DrugBank, MOA, butiran surat paket, rekod lesen) hilang. Laporan tidak boleh diteruskan ke peringkat sintesis bukti tanpa asas-asas ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Pemblokiran]** Ambil rekod lesen penuh NPRA — muat turun PDF surat paket produk untuk mengeluarkan petunjuk yang diluluskan, amaran, dan kontraindikasi
- **[Pemblokiran]** Selesaikan pemetaan ID DrugBank — Amoxycillin Sodium harus dipetakan ke DB01060 (Amoxicillin) DrugBank; sahkan melalui API DrugBank dan kemas kini `drugbank_id` dalam paket bukti
- **[Tinggi]** Tangkap MOA secara rasmi — isi medan `original_moa` dengan mekanisme PBP-binding / perencat sintesis dinding sel selepas pautaan DrugBank disahkan
- **[Tinggi]** Jalankan semula saluran paip ramalan TxGNN — setelah pemetaan DrugBank diselesaikan, jalankan semula langkah ramalan KG dan DL untuk menghasilkan calon ubah tujuan rawatan
- **[Sederhana]** Isi semua medan lesen — nama produk, bentuk dos, pengeluar, dan teks petunjuk yang diluluskan harus dikeluarkan dari rekod NPRA dan disimpan untuk versi laporan seterusnya

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Semua calon ubah tujuan rawatan memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

