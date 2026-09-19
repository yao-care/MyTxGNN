---
layout: default
title: Dextromethorphan Hydrobromide
parent: Low Evidence (L4-L5)
nav_order: 269
evidence_level: L5
indication_count: 0
---

# Dextromethorphan Hydrobromide
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

# Dextromethorphan Hydrobromide: Laporan Penilaian Penurunan Ubatan Tujuan

## Ringkasan Satu Ayat

Dextromethorphan hydrobromide ialah ubatan penekan batuk (antitussive) yang digunakan secara meluas dengan 35 pendaftaran di Malaysia.
Walau bagaimanapun, model TxGNN **tidak menghasilkan sebarang ramalan petunjuk baru** untuk ubatan ini dalam kitaran analisis semasa,
dan jurang data penting (MOA, pelabelan keselamatan, pemetaan DrugBank) kekal tidak diselesaikan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-------|
| Petunjuk Asal | Antitussive (penekan batuk) — *teks petunjuk peringkat lesen belum ditangkap* |
| Ramalan Petunjuk Baru | **Tiada** (tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 35 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

### Tiada Ramalan yang Dijana

Model TxGNN tidak mengembalikan sebarang calon penurunan tujuan untuk dextromethorphan hydrobromide. Ini mungkin disebabkan oleh satu atau lebih sebab berikut:

1. **Pemetaan ID DrugBank yang hilang** — Pakej bukti menunjukkan `drugbank_id: null`. Tanpa pengenalpasti DrugBank yang sah (ID yang dijangka ialah DB00514), ubatan tidak dapat ditemukan dalam graf pengetahuan TxGNN, dan oleh itu tiada ramalan tepi ubatan-penyakit dapat dikira.

2. **Data huluan yang tidak lengkap** — Tatasusunan petunjuk asal kosong dan mekanisme tindakan disenaraikan sebagai jurang data. Input yang hilang ini mungkin telah menghalang saluran paip ramalan daripada dilaksanakan untuk sebatian ini.

### Farmakologi Terkenal (Pengetahuan Umum)

Dextromethorphan ialah terbitan morphinan sintetik yang bertindak terutamanya sebagai **antagonis reseptor NMDA** dan **agonis reseptor sigma-1**. Ia adalah isomer-d bagi metil eter levorphanol dan, tidak seperti isomer-l, tidak mempunyai aktiviti analgesik opioid pada dos terapeutik. Penggunaannya yang diluluskan terutamanya di seluruh dunia ialah sebagai antitussive bukan narkotik untuk pelepasan batuk sementara. Baru-baru ini, dextromethorphan (dalam kombinasi dengan quinidine sebagai Nuedexta®) telah diluluskan untuk **pseudobulbar affect (PBA)**, menunjukkan bahawa molekul ini mempunyai aktiviti CNS yang terbukti di luar penindasan batuk — satu fakta yang boleh, pada dasarnya, menyokong hipotesis penurunan tujuan masa depan dalam petunjuk neurologi atau psikiatri.

---

## Bukti Percubaan Klinis

Tiada ramalan petunjuk yang dijana; oleh itu, tiada carian percubaan klinis yang disasarkan telah dilakukan.

> Pada masa ini tiada percubaan klinis yang berkaitan untuk dipaparkan.

---

## Bukti Kesusasteraan

Tiada ramalan petunjuk yang dijana; oleh itu, tiada carian kesusasteraan yang disasarkan telah dilakukan.

> Pada masa ini tiada kesusasteraan yang berkaitan tersedia.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------|------|------|-----------|
| *(tidak ditangkap)* | *(tidak ditangkap)* | *(tidak ditangkap)* | *(tidak ditangkap)* |

> **Nota:** 35 pendaftaran produk telah dikenal pasti dalam pangkalan data NPRA, tetapi data peringkat lesen yang terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) belum ditangkap ke dalam pakej bukti. Semua lima slot lesen pada masa ini kosong.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> Data keselamatan utama (amaran, kontraindikasi, dan interaksi ubat) tidak dapat diperolehi dalam kitaran pengumpulan bukti ini. Ini diklasifikasikan sebagai jurang data **Menyekat** (DG001) yang mesti diselesaikan sebelum meneruskan ke penilaian keselamatan Peringkat 1.

---

## Ringkasan Jurang Data

Jurang data yang tidak diselesaikan berikut telah dikenal pasti dan mesti ditangani sebelum calon ini dapat dinilai semula:

| ID Jurang | Kategori | Item | Keterukan | Pemulihan |
|--------|----------|------|----------|-------------|
| DG001 | Tahap Ubatan | Amaran sisipan pakej & kontraindikasi | **Menyekat** | Muat turun dan susuli PDF sisipan pakej dari laman web TFDA |
| DG002 | Tahap Ubatan | Mekanisme tindakan (MOA) | Tinggi | Pertanyaan API DrugBank (ID yang dijangka: DB00514) |
| — | Tahap Ubatan | Pemetaan ID DrugBank | Tinggi | Sahkan pemetaan ke DB00514 dan jalankan semula saluran paip ramalan |
| — | Tahap Ubatan | Teks petunjuk asal | Sederhana | Ekstrak daripada rekod lesen |
| — | Kawal Selia | Butiran lesen (semua 35 rekod) | Sederhana | Pertanyaan semula pangkalan data NPRA dengan pengekstrakan medan penuh |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan penurunan tujuan yang dijana oleh TxGNN, kemungkinan besar kerana pemetaan ID DrugBank hilang (`null`), yang menghalang ubatan daripada ditemukan dalam graf pengetahuan. Selain itu, jurang data penyekat dalam pelabelan keselamatan menjadikan mustahil untuk meneruskan ke penilaian keselamatan. Calon ini tidak dapat dinilai sehingga isu data huluan diselesaikan.

**Untuk meneruskan, perkara berikut diperlukan:**
- **Selesaikan pemetaan ID DrugBank** — Sahkan bahawa dextromethorphan hydrobromide memetakan ke ID DrugBank `DB00514` dan suntik semula ke dalam saluran paip ramalan
- **Jalankan semula ramalan TxGNN** — Apabila ID DrugBank dipetakan, jalankan semula kedua-dua kaedah ramalan KG dan DL
- **Ambil data keselamatan sisipan pakej** (DG001) — Muat turun PDF sisipan pakej Malaysia/Taiwan dan ekstrak amaran, kontraindikasi, dan data interaksi
- **Pertanyaan API DrugBank untuk MOA** (DG002) — Isi medan mekanisme tindakan untuk membolehkan analisis kebolehpercayaan mekanik
- **Selesaikan pengekstrakan data peringkat lesen** — Tangkap nombor kebenaran, nama produk, bentuk dos, dan petunjuk yang diluluskan untuk 35 produk berdaftar

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

