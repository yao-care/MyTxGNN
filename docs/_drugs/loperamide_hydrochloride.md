---
layout: default
title: Loperamide Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 453
evidence_level: L5
indication_count: 0
---

# Loperamide Hydrochloride
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

# Loperamide Hydrochloride: Agen Antidiarrhea — Penilaian Pengeluaran Semula Ubat Ditangguhkan

## Ringkasan Satu Ayat

Loperamide Hydrochloride adalah agonis reseptor opioid yang bekerja secara persifer, yang digunakan secara luas sebagai agen antidiarrhea untuk diare akut dan kronik.
Pakej Bukti semasa mengandungi **tiada petunjuk indikasi yang diramalkan oleh TxGNN**, yang bermakna analisis pengeluaran semula ubat yang formal tidak dapat diselesaikan pada masa ini.
Sebelum meneruskan, jurang data kritikal — termasuk maklumat keselamatan sisipan pakej dan MOA DrugBank — mesti diselesaikan.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Antidiarrhea (diare akut, diare kronik, diare pengembara) |
| Indikasi Baru yang Diramalkan | Tidak tersedia — tiada output TxGNN dalam Pakej Bukti ini |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | T/A (data ramalan hilang) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Penilaian Ini Tidak Dapat Diteruskan?

Pakej Bukti untuk Loperamide Hydrochloride kekurangan dua kategori data yang merupakan prasyarat untuk laporan pengeluaran semula ubat yang lengkap:

**1. Tiada Indikasi yang Diramalkan oleh TxGNN**
Tatasusunan `predicted_indications` adalah kosong. Tanpa output model TxGNN, tiada target pengeluaran semula calon untuk dinilai, tiada jejak bukti untuk ditaksir, dan tiada pautan percubaan klinikal atau kesusasteraan untuk disemak. Ini adalah jurang paling asas — enjin keseluruhan laporan.

**2. Jurang Data Mekanisme Tindakan (MOA)**
Loperamide bertindak sebagai agonis **reseptor μ-opioid** dalam plexa myenterik dinding usus, mengurangkan peristaltik dan sekresi usus tanpa kesan sistem saraf pusat yang ketara pada dos terapeutik. Walau bagaimanapun, maklumat ini belum disahkan secara formal melalui DrugBank atau sisipan pakej dalam Pakej Bukti ini (ditandai sebagai DG002, keterukan: Tinggi). Sehingga MOA disahkan dari sumber data berstruktur, analisis kebolehpercayaan mekanistik untuk sebarang indikasi baru tidak dapat didokumentasikan secara formal.

**3. Jurang Data Keselamatan Sisipan Pakej**
Amaran dan kontraindikasi ditandai sebagai DG001 (keterukan: Sekatan). Tanpa ini, bahagian keselamatan laporan ini tidak dapat diselesaikan, dan sebarang calon pengeluaran semula ubat tidak dapat lulus langkah pra-pemeriksaan keselamatan S1 standard.

---

## Maklumat Pasaran Malaysia

Medan butiran lesen tidak dipenuhi dalam Pakej Bukti semasa (semua entri kosong). Berdasarkan hasil pertanyaan kawal selia, **9 pendaftaran produk** disahkan dipasarkan di Malaysia. Jadual di bawah mencerminkan data berstruktur yang tersedia:

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|------------------|-------------|-----------|-------------------|
| — | — | — | *(Butiran lesen tidak dipenuhi dalam Pakej Bukti)* |

> **Tindakan Diperlukan**: Ambil rekod lesen penuh dari pangkalan data NPRA untuk memenuhi nama produk, bentuk dos, dan indikasi yang diluluskan bagi semua 9 pendaftaran.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Pakej Bukti ini kekurangan indikasi yang diramalkan oleh TxGNN sepenuhnya, menjadikannya mustahil untuk mengenal pasti, menilai, atau melaporkan sebarang calon pengeluaran semula ubat. Selain itu, dua jurang data yang menyekat atau berketerukan tinggi menghalang analisis keselamatan dan mekanistik daripada diteruskan.

**Untuk meneruskan, yang berikut diperlukan:**

- [ ] **[Kritikal]** Jalankan semula model TxGNN untuk Loperamide Hydrochloride dan isi `predicted_indications` dengan sekurang-kurangnya satu indikasi calon, termasuk percubaan klinikal dan kesusasteraan yang berkaitan
- [ ] **[Sekatan — DG001]** Muat turun dan analisis PDF sisipan pakej TFDA/NPRA untuk mengekstrak amaran utama dan kontraindikasi, membolehkan pra-pemeriksaan keselamatan S1
- [ ] **[Tinggi — DG002]** Pertanyakan API DrugBank menggunakan INN "loperamide" untuk mendapatkan data MOA, kategori ubat, dan ketoksikan yang berstruktur; sahkan DrugBank ID
- [ ] **[Standard]** Isi semua 9 rekod lesen dalam `taiwan_regulatory.licenses` dengan nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan dari NPRA
- [ ] **[Standard]** Hantar semula Pakej Bukti yang lengkap untuk laporan pengeluaran semula ubat penuh setelah semua jurang kritikal diselesaikan

---

> ⚠️ **Penafian**: Laporan ini hanya untuk rujukan penyelidikan dan tidak membentuk nasihat perubatan. Calon pengeluaran semula ubat memerlukan pengesahan klinikal sebelum sebarang aplikasi.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

