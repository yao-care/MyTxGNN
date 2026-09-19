---
layout: default
title: Benserazide Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 127
evidence_level: L5
indication_count: 0
---

# Benserazide Hydrochloride
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

# Benserazide Hydrochloride: Laporan Penilaian Repurposing Ubat

## Ringkasan Satu Ayat

Benserazide hydrochloride ialah perencat dekarboxilase DOPA periferal, biasanya digunakan dalam kombinasi dengan levodopa untuk rawatan penyakit Parkinson. Model TxGNN **belum menghasilkan sebarang petunjuk baru yang diramalkan** untuk sebatian ini, dan pakej bukti mengandungi jurang data yang ketara merentas pelbagai kategori, menghalang penilaian repurposing yang bermakna pada masa ini.

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Penyakit Parkinson (kombinasi dengan levodopa) |
| Petunjuk Baru yang Diramalkan | — (Tiada ramalan dijana) |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Tiada kajian; tiada ramalan model tersedia) |
| Status Pasaran Malaysia | ✓ Tersedia di pasaran (Tersedia di pasaran) |
| Bilangan Pendaftaran | 3 |
| Keputusan Disyorkan | **Tunggu** |

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan TxGNN yang dijana untuk benserazide hydrochloride. Susunan `predicted_indications` adalah kosong, bermaksud model tidak mengenal pasti sebarang calon repurposing yang memenuhi ambang pemarkahan.

Benserazide ialah perencat aromatic L-amino acid decarboxylase (AADC) periferal. Ia tidak melintas penghalang darah-otak dan bertindak dengan menyekat penukaran levodopa ke dopamin yang bersifat periferal, dengan itu meningkatkan ketersediaan hayati levodopa dalam sistem saraf pusat. Ia sentiasa digunakan sebagai produk kombinasi (levodopa/benserazide, dipasarkan sebagai Madopar®) dan mempunyai aktiviti farmakoloji mandiri yang terbatas.

Ketiadaan ramalan mungkin boleh dikaitkan dengan beberapa faktor: (1) benserazide berfungsi terutamanya sebagai penambah farmakokinetik dan bukannya agen terapeutik langsung, menjadikan potensi repurposing mandirinya terbatas; (2) ID DrugBank tidak diselesaikan (`drugbank_id: null`), yang mungkin telah menghalang pemetaan yang sepatutnya ke dalam graf pengetahuan TxGNN; dan (3) data mekanisme tindakan tidak tersedia dalam pakej bukti, seterusnya mengehadkan keupayaan model untuk membuat kaitan mekanik.

## Bukti Percubaan Klinikal

Pada masa ini tiada petunjuk yang diramalkan telah dijana, oleh itu tiada carian percubaan klinikal yang disasarkan telah dilakukan.

## Bukti Kesusasteraan

Pada masa ini tiada petunjuk yang diramalkan telah dijana, oleh itu tiada carian kesusasteraan yang disasarkan telah dilakukan.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------|------|------|-----------|
| *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* |

> **Nota:** Tiga pendaftaran telah dikenalpasti dalam pangkalan data NPRA, tetapi maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak diisi dalam pakej bukti. Ini mewakili jurang data yang perlu diperbetulkan dengan membuat pertanyaan ke pangkalan data NPRA secara langsung.

## Pertimbangan Keselamatan

> Sila rujuk risalah produk untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, dan interaksi ubat–ubat) pada masa ini tidak tersedia dalam pakej bukti ini.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Alasan:**
Tiada calon repurposing yang diramalkan oleh TxGNN untuk benserazide hydrochloride. Sebagai tambahan, jurang data kritikal wujud merentas pemetaan DrugBank, mekanisme tindakan, butiran lesen pengawalan, dan maklumat keselamatan, menjadikan sebarang penilaian repurposing prematur.

**Untuk meneruskan, yang berikut diperlukan:**
- **Selesaikan pemetaan ID DrugBank** — Soal DrugBank untuk "benserazide" (DB00190) bagi membolehkan integrasi graf pengetahuan yang sepatutnya
- **Isi butiran lesen NPRA** — Ambil rekod pendaftaran lengkap (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) dari pangkalan data NPRA
- **Dapatkan data mekanisme tindakan** — Ambil MOA dari DrugBank untuk menyokong penaakulan mekanik
- **Dapatkan data keselamatan** — Muat turun dan analisis risalah produk (PIL) untuk amaran utama, kontraindikasi, dan interaksi ubat
- **Jalankan semula ramalan TxGNN** — Sebaik sahaja ID DrugBank diselesaikan dan ubat itu dipetakan dengan sepatutnya ke dalam graf pengetahuan, laksanakan semula saluran ramalan untuk menentukan sama ada sebarang calon repurposing muncul
- **Pertimbangkan konteks kombinasi** — Memandangkan benserazide hampir eksklusif digunakan dalam kombinasi dengan levodopa, nilaikan sama ada model ramalan perlu menilai kombinasi levodopa/benserazide dan bukannya benserazide sahaja

---

*Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon repurposing ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

