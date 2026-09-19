---
layout: default
title: Bromhexine Hcl
parent: Low Evidence (L4-L5)
nav_order: 164
evidence_level: L5
indication_count: 0
---

# Bromhexine Hcl
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

# Bromheksina HCL: Agen Mukolotik — Tiada Indikasi Baru yang Diramalkan

## Ringkasan Satu Ayat

Bromheksina HCL adalah agen mukolotik yang telah terbukti dan luas digunakan untuk meredakan batuk produktif yang berkaitan dengan keadaan pernafasan. Model TxGNN **tidak menghasilkan sebarang ramalan penggunaan semula** untuk ubat ini. Dengan **37 pendaftaran** di Malaysia yang mengesahkan ketersediaan pasaran yang luas, pengayaan data lanjut (pemetaan DrugBank, MOA, profil keselamatan) diperlukan sebelum analisis penggunaan semula dapat dilakukan.

---

## Gambaran Umum Cepat

| Item | Kandungan |
|------|------|
| Indikasi Asal | Mukolotik — meredakan batuk produktif dalam gangguan pernafasan |
| Indikasi Baru yang Diramalkan | Tiada (tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 — Tiada ramalan dihasilkan |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 37 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Tidak Ada?

Bromheksina HCL adalah agen mukolotik yang berfungsi melalui depolimerisasi mukopolisakarida dan merangsang sekresi lendir serosa dalam saluran pernafasan, dengan itu mengurangkan kelikatan sputum dan memudahkan ekspektorasi. Ia telah digunakan secara klinikal secara global selama beberapa dekad untuk bronkitis, asma dengan sumbatan lendir, dan keadaan pernafasan lain dengan pengeluaran lendir yang berlebihan.

Model TxGNN tidak mengembalikan sebarang calon penggunaan semula untuk Bromheksina HCL. Ini mungkin disebabkan oleh satu atau lebih faktor berikut: (1) ID DrugBank ubat tidak berjaya dipetakan (`drugbank_id: null`), yang akan menghalang model daripada mencari ubat dalam graf pengetahuan; (2) data mekanisme tindakan Bromheksina tidak tersedia untuk digunakan oleh model; atau (3) profil farmakoloji ubat tidak menghasilkan persatuan penyakit novel berkeyakinan tinggi di atas ambang model.

Untuk memungkinkan analisis penggunaan semula yang bermakna, pemetaan DrugBank mesti diselesaikan terlebih dahulu. Bromheksina HCL disenaraikan dalam DrugBank (DB09015), dan membetulkan pautan ini akan membenarkan graf pengetahuan dan saluran pembelajaran mendalam untuk menjana ramalan yang diskor.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal yang berkaitan tersedia untuk penilaian, kerana tiada indikasi baru telah diramalkan.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan tersedia untuk penilaian, kerana tiada indikasi baru telah diramalkan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(Butiran tidak tersedia)* | — | — | — |

> **Nota:** Walaupun 37 pendaftaran NPRA telah diambil untuk Bromheksina HCL, butiran lesen individu (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak diisi dalam pakej bukti. Pertanyaan susulan ke pangkalan data NPRA diperlukan untuk melengkapkan bahagian ini.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Amaran utama, kontraindikasi, dan data interaksi ubat tidak tersedia dalam pakej bukti semasa.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan penggunaan semula TxGNN yang dihasilkan untuk Bromheksina HCL, kemungkinan besar disebabkan oleh pemetaan ID DrugBank yang hilang yang menghalang ubat daripada ditemui dalam graf pengetahuan. Tanpa indikasi yang diramalkan, tiada calon untuk dinilai.

**Untuk meneruskan, yang berikut diperlukan:**
- **Selesaikan pemetaan DrugBank**: Petakan Bromheksina HCL ke ID DrugBank-nya (DB09015) dan jalankan semula saluran ramalan TxGNN (kedua-dua kaedah KG dan DL)
- **Dapatkan data mekanisme tindakan**: Pertanyaan API DrugBank untuk mengisi medan MOA untuk penaakulan mekanis
- **Isi butiran lesen NPRA**: Pertanyaan semula pangkalan data NPRA untuk mendapatkan nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk 37 produk berdaftar
- **Dapatkan profil keselamatan**: Muat turun dan analisis sisipan pakej (PIL) untuk amaran utama, kontraindikasi, dan interaksi ubat
- **Jana semula pakej bukti**: Setelah jurang data di atas diisi, jalankan semula saluran penuh untuk menghasilkan penilaian penggunaan semula yang boleh ditindakkan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

