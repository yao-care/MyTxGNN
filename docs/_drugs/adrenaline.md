---
layout: default
title: Adrenaline
parent: Low Evidence (L4-L5)
nav_order: 30
evidence_level: L5
indication_count: 0
---

# Adrenaline
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

# Adrenalin (Epinefrin): Profil Ubat — Ramalan Ubat Berulang TxGNN Tergantung

## Ringkasan Satu Ayat

Adrenalin (Epinefrin) adalah katekolamin yang telah terbukti digunakan dalam perubatan kecemasan, terutamanya untuk anafilaksis, henti jantung, dan bronkospasma teruk.
**Tiada ramalan ubat berulang TxGNN tersedia** untuk calon ini — saluran ramalan belum selesai, dan jurang data kritikal masih tidak dapat diselesaikan.
Laporan ini mendokumentasikan status kawal selia semasa di Malaysia dan menggariskan langkah-langkah yang diperlukan sebelum penilaian ubat berulang dapat diteruskan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak diisi dalam Pakej Bukti semasa |
| Petunjuk Baru yang Diramalkan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 — Ramalan model belum dijalankan; tiada kajian sokongan dalam pakej |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 17 |
| Keputusan yang Disyorkan | **Tungguh** |

---

## Mengapa Ramalan Belum Tersedia?

Tatasusunan `predicted_indications` dalam Pakej Bukti semasa adalah kosong. Dua jurang data hulu menyekat penilaian ubat berulang:

- **DG001 (Menyekat)** — Amaran sisipan pakej dan kontraindikasi belum diambil daripada pihak berkuasa kawal selia. Tanpa ini, langkah pra-saringan keselamatan (S1) tidak dapat diselesaikan.
- **DG002 (Tinggi)** — Data mekanisme tindakan (MOA) belum dimuatkan daripada DrugBank. Ini menghalang analisis kebolehpercayaan mekanik untuk sebarang petunjuk yang diramalkan.

Daripada farmakoloji yang ditetapkan, Adrenalin bertindak sebagai agonis adrenergik bukan-pilih pada reseptor α₁, α₂, β₁, dan β₂, menghasilkan vasokonstriksi, bronkodilatasi, kronotrpi positif, dan kesan inotropik. Petunjuknya yang klasikal termasuk anafilaksis, henti jantung tanpa denyut nadi, asma teruk, dan croup. Sama ada TxGNN mengenalpasti peluang ubat berulang yang baru di luar penggunaan yang telah ditetapkan ini tetap akan ditentukan setelah saluran ramalan dilaksanakan dengan data input yang lengkap.

---

## Maklumat Pasaran Malaysia

17 pendaftaran aktif telah dikenalpasti dalam pangkalan data NPRA untuk Adrenalin (Epinefrin). Walau bagaimanapun, butiran produk individu tidak diisi dalam Pakej Bukti semasa dan memerlukan langkah pengambilan data susulan.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|-----------------|------------|-----------|----------------------|
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |
| — | — | — | — |

> **Nota**: 17 rekod disahkan dalam daftar NPRA. Butiran produk lengkap (nombor lesen, nama jenama, bentuk dos, teks petunjuk yang diluluskan) mesti diambil daripada pangkalan data NPRA untuk melengkapkan bahagian ini.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.

Data keselamatan untuk Adrenalin tidak tersedia dalam Pakej Bukti semasa (Jurang Data DG001, keterukan: **Menyekat**). Tiada amaran utama, kontraindikasi, atau data interaksi ubat-ubat telah diisi. Ini adalah item pemulihan keutamaan tertinggi sebelum sebarang penilaian ubat berulang dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tungguh**

**Rasional:**
Pakej Bukti untuk Adrenalin tidak lengkap pada tahap asas — tiada ramalan TxGNN telah dijana, data MOA hilang, dan data keselamatan belum diambil. Keputusan Tungguh diperlukan sehingga jurang data yang menyekat dan berseveriti tinggi diselesaikan.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Menyekat]** Muat turun dan huraikan PDF sisipan pakej NPRA/TFDA untuk mengekstrak amaran, kontraindikasi, dan data populasi khas (pemulihan untuk DG001)
- **[Tinggi]** Soal API DrugBank untuk mendapatkan data MOA, farmakodinamik, dan ketoksikan untuk Adrenalin (pemulihan untuk DG002)
- Ambil rekod butiran lesen penuh untuk 17 pendaftaran NPRA yang disahkan (nama produk, bentuk dos, teks petunjuk yang diluluskan)
- Jalankan semula saluran ramalan TxGNN untuk Adrenalin setelah data input lengkap, untuk menjana `predicted_indications`
- Janakan semula Pakej Bukti dan teruskan ke penilaian penuh setelah semua jurang data diselesaikan

---

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon ubat berulang yang dikenalpasti oleh TxGNN memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

