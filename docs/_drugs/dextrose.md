---
layout: default
title: Dextrose
parent: Low Evidence (L4-L5)
nav_order: 270
evidence_level: L5
indication_count: 0
---

# Dextrose
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

# Dekstrosa: Laporan Penilaian Penggunaan Ulang Dadah

## Ringkasan Satu Ayat

Dekstrosa (glukosa) ialah agen farmasi pengisi dan terapi yang digunakan secara meluas, terutamanya diberikan sebagai cecair intravena untuk bekalan kalori dan hidrasi. Model TxGNN **tidak menghasilkan sebarang ramalan penggunaan ulang** untuk sebatian ini, dan pakej bukti mengandungi jurang data yang ketara di semua dimensi penilaian.

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Tidak tersedia (butiran lesen tidak lengkap) |
| Petunjuk Baru Diramalkan | Tiada — tidak ada ramalan yang dihasilkan |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | L5 (Tiada ramalan atau kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 69 |
| Keputusan yang Disyorkan | **Tahan** |

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan penggunaan ulang yang dijana oleh model TxGNN untuk Dekstrosa. Ini berkemungkinan disebabkan oleh sifat sebatian itu sendiri — Dekstrosa (D-glukosa) ialah monosakarida mudah yang digunakan terutamanya sebagai substrat tenaga dan kenderaan untuk pemberian ubat intravena, bukan ubat yang aktif secara farmakologi dengan sasaran molekular spesifik. Mekanisme tindakannya berdasarkan laluan metabolik asas (glikolisis, pengeluaran tenaga sel) dan bukannya mekanisme terapeutik khusus penyakit.

Oleh kerana Dekstrosa tidak mempunyai mekanisme farmakologi yang disasarkan, model graf pengetahuan TxGNN mungkin tidak mengenal pasti tepi penyakit-ubat yang bermakna di luar peranannya yang ditetapkan dalam penjagaan nutrisi dan sokongan. Sebatian yang mempunyai fungsi metabolik yang luas dan tidak khusus secara amnya adalah calon yang lemah untuk penggunaan ulang berdasarkan petunjuk, yang bergantung pada pengenalan hubungan sasaran-penyakit baru.

Selain itu, pakej bukti hilang data kritikal termasuk mekanisme tindakan terperinci (MOA), pemetaan ID DrugBank, dan teks petunjuk yang diluluskan daripada pemfailan kawal selia. Jurang data ini seterusnya mengehadkan sebarang analisis penggunaan ulang yang bermakna.

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal terkait didaftarkan — tiada petunjuk yang diramalkan dijana.

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan terkait tersedia — tiada petunjuk yang diramalkan dijana.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------|------|------|------|
| *(Butiran tidak tersedia)* | — | — | — |

> **Nota:** Walaupun 69 pendaftaran produk telah dikenal pasti dalam pangkalan data NPRA, butiran lesen yang terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak diisi dalam pakej bukti. Dekstrosa biasanya didaftarkan sebagai penyelaras intravena untuk penggantian cecair, bekalan kalori, dan sebagai kenderaan untuk ubat boleh suntik.

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti semasa.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan penggunaan ulang yang dijana oleh model TxGNN untuk Dekstrosa. Sebatian berfungsi sebagai substrat metabolik asas dan bukannya agen terapeutik yang disasarkan, menjadikannya calon yang tidak mungkin untuk penggunaan ulang ubat berdasarkan petunjuk. Selain itu, pakej bukti mengandungi pelbagai jurang data pemblokiran yang menghalang penilaian yang bermakna.

**Untuk meneruskan, yang berikut diperlukan:**
- Selesaikan pemetaan ID DrugBank (pertanyaan mengembalikan 1 hasil tetapi ID tidak ditangkap)
- Isikan butiran lesen NPRA (nombor kebenaran, nama produk, petunjuk yang diluluskan) untuk 69 produk berdaftar
- Perolehi amaran sisipan pakej TFDA dan kontraindikasi (keterukan: Pemblokiran — DG001)
- Perolehi data mekanisme tindakan daripada DrugBank (keterukan: Tinggi — DG002)
- Nilaikan semula sama ada Dekstrosa, sebagai sebatian metabolik tidak disasarkan, ialah calon yang sesuai untuk saluran penggunaan ulang TxGNN

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan ulang ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

