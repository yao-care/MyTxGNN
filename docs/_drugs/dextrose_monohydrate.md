---
layout: default
title: Dextrose Monohydrate
parent: Low Evidence (L4-L5)
nav_order: 272
evidence_level: L5
indication_count: 0
---

# Dextrose Monohydrate
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

# Dextrose Monohydrate: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu Ayat

Dextrose Monohydrate adalah monosakarida ringkas (glukosa) yang digunakan secara luas sebagai bahan eksipien farmasetik, suplemen kalori, dan terapi penggantian cairan. Model TxGNN **tidak menghasilkan sebarang indikasi baru yang diramalkan** untuk sebatian ini, dan jurang data yang kritikal kekal dalam mekanisme kerja dan dokumentasi keselamatan.

## Tinjauan Cepat

| Item | Kandungan |
|------|------|
| Indikasi Asal | Tidak tersedia (medan butiran lesen kosong) |
| Indikasi Baru yang Diramalkan | **Tiada** — TxGNN tidak mengembalikan sebarang ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 31 |
| Keputusan yang Dicadangkan | **Tahan** |

---

## Mengapa Tiada Ramalan?

Dextrose Monohydrate (glukosa monohidrat) adalah bentuk terhidrat D-glukosa, yang digunakan terutamanya dalam tetapan klinikal sebagai:
- Suplemen kalori intravena dan terapi penggantian cairan
- Kenderaan/bahan eksipien dalam formulasi farmasetik
- Rawatan untuk hipoglikemia

Tidak seperti molekul terapeutik konvensional yang berinteraksi dengan sasaran biologi tertentu, dextrose adalah metabolit endogen — substrat tenaga asas dalam fisiologi manusia. Ia tidak mempunyai mekanisme farmakologi yang sempit seperti agonis reseptor, perencat enzim, atau modulator saluran ion. Ciri ini menjadikannya kurang sesuai untuk pendekatan penggunaan semula ubat berasaskan graf pengetahuan seperti TxGNN.

Model TxGNN bergantung pada pemetaan ubat ke pengecam DrugBank dan kemudian melintasi hubungan ubat–penyakit dalam graf pengetahuan biomedis. Dalam kes ini, **ID DrugBank tidak diselesaikan** (`null`), yang bermaksud ubat tidak dapat dipanchor dalam graf pengetahuan. Tanpa nod yang sah dalam graf, tiada ramalan penyakit boleh dihasilkan. Tambahan pula, peranan dextrose sebagai metabolit asas daripada agen terapeutik yang disasarkan bermakna ia kekurangan profil interaksi molekul tertentu yang dimanfaatkan TxGNN untuk ramalan penggunaan semula.

---

## Bukti Ujian Klinikal

Tidak berkenaan — tiada indikasi yang diramalkan telah dihasilkan oleh TxGNN.

---

## Bukti Literatur

Tidak berkenaan — tiada indikasi yang diramalkan telah dihasilkan oleh TxGNN.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Sediaan | Indikasi yang Diluluskan |
|------|------|------|------|
| (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) |

> **Nota:** 31 pendaftaran telah diambil dari pangkalan data NPRA, tetapi maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk sediaan, dan teks indikasi yang diluluskan) tidak diisi dalam pakej bukti. Data mentah perlu diambil semula dengan pemetaan medan lengkap.

---

## Pertimbangan Keselamatan

> Sila rujuk risalah pakej untuk maklumat keselamatan.
>
> Data keselamatan utama (amaran, kontraindikasi, dan interaksi ubat) tidak dapat diambil. Ini telah dikenal pasti sebagai jurang data **Menyekat** (DG001) yang mesti diselesaikan sebelum sebarang penilaian lanjutan dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Dextrose Monohydrate adalah substrat metabolik asas (glukosa) tanpa sasaran farmakologi tertentu, menjadikannya calon yang tidak sesuai untuk penggunaan semula ubat berasaskan TxGNN. Model mengembalikan sifar ramalan indikasi, dan medan data yang kritikal — termasuk ID DrugBank, mekanisme kerja, butiran lesen, dan maklumat keselamatan — semua hilang.

**Untuk melanjutkan, yang berikut diperlukan:**
- **Selesaikan pemetaan DrugBank** — Sahkan sama ada entri DrugBank DB09341 (Glukosa) atau entri lain terpakai, dan jalankan semula saluran ramalan dengan ID DrugBank yang sah
- **Isikan butiran lesen** — Tanya semula NPRA dengan pengekstrakan medan lengkap untuk mengisi 31 rekod pendaftaran kosong
- **Dapatkan dokumentasi keselamatan** (DG001, Menyekat) — Muat turun dan parskan PDF risalah pakej dari pihak berkuasa pengawalseliaan untuk amaran dan kontraindikasi
- **Penilaian semula keselamatan** — Walaupun dengan ID DrugBank yang diselesaikan, dextrose sebagai metabolit endogen mungkin kekal pada asasnya tidak sesuai untuk penggunaan semula berasaskan graf pengetahuan; pertimbangkan untuk mengecualikan metabolit asas/eksipien daripada larian skrining masa hadapan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

