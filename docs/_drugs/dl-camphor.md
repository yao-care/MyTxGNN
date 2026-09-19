---
layout: default
title: Dl-Camphor
parent: Low Evidence (L4-L5)
nav_order: 290
evidence_level: L5
indication_count: 0
---

# Dl-Camphor
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

# DL-Camphor: Laporan Penilaian Penentuan Semula Ubat

## Ringkasan Satu Ayat

DL-Camphor ialah agen topical yang dipasarkan di Malaysia dengan 9 produk berdaftar, biasa digunakan sebagai penggorengan balas dan analgesia ringan. Model TxGNN **tidak mempunyai petunjuk baru yang diramalkan** untuk sebatian ini, dan jurang data kritikal wujud dalam mekanisme tindakan, teks petunjuk yang diluluskan, dan maklumat keselamatan.

---

## Ikhtisar Cepat

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak tersedia (teks petunjuk lesen hilang) |
| Petunjuk Baru yang Diramalkan | Tiada — TxGNN tidak mengembalikan prediksi |
| Skor Prediksi TxGNN | N/A |
| Tahap Bukti | N/A — Tiada prediksi untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Prediksi Ini Munasabah?

**Tiada prediksi TxGNN untuk dinilai** bagi DL-Camphor. Model mengembalikan senarai petunjuk yang diramalkan kosong, yang mungkin boleh dikaitkan dengan satu atau lebih faktor berikut:

1. **DrugBank ID Hilang**: DL-Camphor tidak dapat dipetakan ke pengenal DrugBank (`drugbank_id: null`). Graf pengetahuan TxGNN bergantung pada nod DrugBank untuk menambat entiti ubat; tanpa pemetaan yang sah, model tidak dapat menghasilkan prediksi. Ini adalah punca utama yang paling berkemungkinan.

2. **Liputan graf pengetahuan terhad**: DL-Camphor ialah campuran racemik d-camphor dan l-camphor. Ia terutamanya digunakan sebagai eksipien atau dalam persediaan topical bebas preskripsi. Sebatian tersebut mungkin mempunyai perwakilan terhad dalam graf pengetahuan TxGNN, yang berat ke arah terapeutik preskripsi dengan sasaran molekul yang dicirikan dengan baik.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pakej bukti ini. Berdasarkan pengetahuan farmakologi umum, DL-Camphor ialah ketone monoterpena siklik yang bertindak pada reseptor TRPV1 dan TRPV3, menghasilkan sensasi kesejukan dan analgesia tempatan ringan. Profil terapeutiknya adalah terutamanya topical, yang seterusnya mengehadkan peluang penentuan semula sistematik.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan berdaftar — tiada prediksi TxGNN yang dihasilkan untuk dicari.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan tersedia — tiada prediksi TxGNN yang dihasilkan untuk dicari.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------|------|------|------|
| (tidak disediakan) | (tidak disediakan) | (tidak disediakan) | (tidak disediakan) |
| (tidak disediakan) | (tidak disediakan) | (tidak disediakan) | (tidak disediakan) |
| (tidak disediakan) | (tidak disediakan) | (tidak disediakan) | (tidak disediakan) |
| (tidak disediakan) | (tidak disediakan) | (tidak disediakan) | (tidak disediakan) |
| (tidak disediakan) | (tidak disediakan) | (tidak disediakan) | (tidak disediakan) |

> **Nota:** 9 pendaftaran dikenal pasti oleh pertanyaan NPRA, tetapi butiran lesen (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk) tidak diisi dalam pakej bukti. Jurang data ini mesti diselesaikan sebelum penilaian seterusnya.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini hilang. Tiada interaksi ubat-ubatan ditemui dalam pertanyaan DrugBank.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada prediksi penentuan semula TxGNN yang dihasilkan bagi DL-Camphor, kemungkinan besar kerana sebatian ini tidak mempunyai pemetaan DrugBank ID. Tanpa prediksi, tiada petunjuk calon untuk dinilai. Selain itu, pelbagai jurang data kritikal (MOA, teks petunjuk, profil keselamatan) menghalang penilaian yang bermakna.

**Untuk meneruskan, perkara berikut diperlukan:**
- **Selesaikan pemetaan DrugBank** — Siasat sama ada DL-Camphor (atau enantiomer individunya d-camphor / l-camphor) mempunyai entri DrugBank (cth. DB01744 untuk Camphor) dan jalankan semula saluran pemetaan
- **Isi butiran lesen NPRA** — Perolehi nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan bagi semua 9 produk berdaftar
- **Dapatkan data keselamatan** — Muat turun dan huraikan sisipan pakej daripada pangkalan data NPRA untuk mengisi amaran, kontraindikasi, dan profil interaksi
- **Dapatkan data MOA** — Pertanyakan API DrugBank atau PubChem untuk butiran mekanisme farmakologi
- **Jalankan semula prediksi TxGNN** — Setelah DrugBank ID diselesaikan, laksanakan semula saluran prediksi graf pengetahuan dan pembelajaran mendalam

---

### Ringkasan Jurang Data

| ID Jurang | Item | Keterukan | Sumber yang Disyorkan |
|--------|------|----------|--------------------|
| DG001 | Amaran/kontraindikasi sisipan pakej NPRA | **Menghalang** | Laman web NPRA — muat turun dan huraikan PDF |
| DG002 | Mekanisme Tindakan (MOA) | Tinggi | Pertanyaan API DrugBank |
| — | Medan butiran lesen (semua kosong) | Tinggi | Pertanyaan pangkalan data NPRA semula |
| — | Pemetaan DrugBank ID | **Menghalang** | Carian DrugBank untuk "Camphor" (DB01744) |

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

