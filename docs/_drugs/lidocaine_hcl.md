---
layout: default
title: Lidocaine Hcl
parent: Low Evidence (L4-L5)
nav_order: 440
evidence_level: L5
indication_count: 0
---

# Lidocaine Hcl
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

# LIDOCAINE HCL: Anestetik Tempatan / Antiaritmik — Tiada Ramalan Ubat Semula Guna TxGNN Dijana

## Ringkasan Satu Ayat

Lidocaine HCl ialah agen anestetik tempatan dan antiaritmik yang digunakan secara meluas dengan **21 produk berdaftar** di Malaysia.
Larian analisis TxGNN semasa **tidak menjana sebarang ramalan ubat semula guna** untuk sebatian ini,
dan jurang data kritikal dalam mekanisme tindakan, indikasi yang diluluskan, dan maklumat keselamatan menghalang penilaian lengkap pada peringkat ini.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak diambil dalam set data semasa |
| Indikasi Baharu Ramalan | Tiada ramalan dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 – Tiada output ramalan model |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 21 |
| Keputusan Disyorkan | Tahan |

---

## Mengapa Tiada Ramalan Tersedia?

TxGNN memerlukan **DrugBank ID** yang sah untuk menolakinkan sebatian dalam graf pengetahuan dan menjana skor ubat semula guna. Dalam Pakej Bukti ini, `drugbank_id` ialah `null`, bermakna saluran paip tidak dapat memetakan Lidocaine HCl ke nod graf pengetahuan. Tanpa sauh ini, model tidak menghasilkan calon penyakit yang disusun.

Selain itu, susunan `original_indications` adalah kosong dan `original_moa` tidak tersedia, menghilangkan konteks biologi yang diperlukan untuk mengesahkan sebarang rasional mekanistik walaupun jika ramalan ada.

> Pada masa ini, data mekanisme tindakan terperinci tidak tersedia. Berdasarkan pengetahuan farmakologi am, Lidocaine HCl ialah penyekat saluran natrium yang digunakan sebagai agen anestetik tempatan dan ubat antiaritmik Kelas Ib; bagaimanapun, maklumat ini tidak disahkan dalam Pakej Bukti yang diberikan dan tidak boleh digunakan untuk penilaian rasmi tanpa sumber yang disahkan.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal terkait didaftarkan *(tiada indikasi ramalan untuk dicari)*.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan terkait tersedia *(tiada indikasi ramalan untuk dicari)*.

---

## Maklumat Pasaran Malaysia

Sejumlah **21 produk berdaftar** telah dikenal pasti melalui pertanyaan NPRA (tarikh pertanyaan: 2026-03-27). Bagaimanapun, butir lesen individu — termasuk nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan — tidak diambil dalam set data semasa.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|-----------------|-------------|-----------|------------------------|
| — | — | — | Rekod terperinci tidak tersedia; 21 pendaftaran disahkan oleh NPRA |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Penilaian ini tidak dapat diteruskan dengan bermakna kerana saluran paip TxGNN tidak menghasilkan calon ubat semula guna — akibat langsung daripada DrugBank ID yang hilang — dan semua medan data peringkat ubat (indikasi asal, mekanisme tindakan, amaran keselamatan, kontraindikasi, dan rekod lesen individu) adalah tidak hadir dalam Pakej Bukti semasa.

**Untuk diteruskan, yang berikut diperlukan:**

- **Selesaikan DrugBank ID**: Cari Lidocaine HCl di [DrugBank](https://www.drugbank.ca) (dijangka: DB00281) dan kemas kini medan `drugbank_id`, kemudian jalankan semula saluran paip ramalan TxGNN
- **Ambil butir lesen NPRA**: Pertanyaan daftar produk NPRA untuk semua 21 pendaftaran untuk mengisi nama produk, bentuk dos, dan teks indikasi yang diluluskan
- **Dapatkan data MOA dan keselamatan**: Tarik kemasukan DrugBank untuk farmakodinamik, mekanisme tindakan, amaran, kontraindikasi, dan interaksi ubat–ubat
- **Analisa sisipan pakej**: Muat turun PDF maklumat preskripsi yang diluluskan NPRA/pengilang untuk mengesahkan amaran dan kontraindikasi tempatan (Jurang Data DG001 — keterukan: Menyekat)
- **Jalankan semula pengumpulan bukti**: Setelah indikasi ramalan disahkan, picu pengumpul ClinicalTrials.gov dan PubMed untuk mengumpul kesusasteraan sokongan

> ⚠️ **Penafian YMYL**: Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon ubat semula guna mesti menjalani pengesahan klinikal sebelum aplikasi.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

