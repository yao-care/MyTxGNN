---
layout: default
title: Linagliptin
parent: Low Evidence (L4-L5)
nav_order: 443
evidence_level: L5
indication_count: 0
---

# Linagliptin
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

# Linagliptin: Dari Diabetes Mellitus Jenis 2 — Tiada Ramalan Tujuan Baru Tersedia

## Ringkasan Satu Ayat

Linagliptin ialah inhibitor DPP-4 (dipeptidyl peptidase-4) yang telah diluluskan untuk pengurusan Diabetes Mellitus Jenis 2.
Evidence Pack ini mengandungi **tiada ramalan tujuan baru TxGNN** — medan `predicted_indications` adalah kosong, menunjukkan saluran ramalan belum dijalankan atau mengembalikan hasil.
Dua jurang data yang menghalang (MOA dan sisipan pakej) mesti diselesaikan sebelum penilaian tujuan baru boleh diteruskan.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Diabetes Mellitus Jenis 2 |
| Petunjuk Baru yang Diramalkan | Tidak tersedia — `predicted_indications` adalah kosong |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A — tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan Disyorkan | **Tahan** |

---

## Maklumat Pasaran Malaysia

9 pendaftaran NPRA telah disahkan, tetapi semua rekod lesen individu dalam Evidence Pack ini tidak dipenuhi (rentetan kosong). Maklumat peringkat produk yang terperinci tidak tersedia sehingga data lesen diambil dari pangkalan data NPRA.

| Item | Status |
|------|--------|
| Jumlah pendaftaran (NPRA) | 9 |
| Butiran lesen | Tidak tersedia dalam Evidence Pack ini |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> **Nota:** Kedua-dua amaran utama dan kontraindikasi ditandai sebagai jurang data (DG001, keterukan: Menghalang). Tiada rekod interaksi ubat-ubatan dikembalikan oleh pertanyaan DDI. Penilaian keselamatan tidak boleh diteruskan sehingga sisipan pakej diperoleh.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tatasusunan `predicted_indications` adalah kosong, bermakna tiada calon tujuan baru telah dikenal pasti oleh TxGNN untuk ubat ini. Digabungkan dengan dua jurang data yang tidak diselesaikan meliputi maklumat keselamatan MOA dan sisipan pakej, pada masa ini tidak ada asas untuk menjalankan penilaian tujuan baru.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Selesaikan DG001 (Menghalang)** — Muat turun dan hurai PDF sisipan pakej TFDA/NPRA untuk mengekstrak petunjuk yang diluluskan, amaran, dan kontraindikasi; ini adalah prasyarat untuk langkah penyaringan keselamatan.
2. **Selesaikan DG002 (Tinggi)** — Pertanyaan API DrugBank untuk mekanisme tindakan Linagliptin (DB08882); data MOA diperlukan oleh saluran TxGNN untuk pemarkahan kesamaan mekanik.
3. **Jalankan semula saluran ramalan TxGNN** dengan input lengkap untuk mengisi `predicted_indications`; hanya kemudian boleh sasaran penyakit dan tahap bukti diberikan.
4. **Ambil butiran lesen NPRA** untuk 9 produk berdaftar (nama produk, bentuk dos, teks petunjuk yang diluluskan) untuk melengkapkan bahagian Maklumat Pasaran Malaysia.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

