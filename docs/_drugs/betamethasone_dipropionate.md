---
layout: default
title: Betamethasone Dipropionate
parent: Low Evidence (L4-L5)
nav_order: 137
evidence_level: L5
indication_count: 0
---

# Betamethasone Dipropionate
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

# Betamethasone Dipropionate: Laporan Penilaian Ubat Repurposing

## Ringkasan Satu Ayat

Betamethasone Dipropionate ialah kortikosteroid sintetik yang kuat digunakan secara meluas untuk keadaan dermatologi yang meradang dan gatal. Model TxGNN telah **tidak menghasilkan sebarang petunjukan baru yang diramalkan** untuk ubat ini pada masa ini. Pada masa ini **tiada ujian klinikal atau penerbitan** yang terpaut kepada calon repurposing, dan beberapa jurang data kritikal tetap perlu diselesaikan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Petunjukan Asal | *(Data tidak tersedia dalam paket bukti semasa — lihat nota di bawah)* |
| Petunjukan Baru yang Diramalkan | **Tiada** (tiada ramalan TxGNN dijana) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **L5** — Ramalan model sahaja; tiada calon dikenal pasti |
| Status Pasaran Malaysia | ✓ Dalam Pasaran (Marketed) |
| Jumlah Pendaftaran | 41 |
| Keputusan yang Disyorkan | **Tahan** |

> **Nota tentang Petunjukan Asal:** Kesemua 41 rekod lesen yang dikembalikan oleh NPRA semuanya mempunyai medan teks petunjukan kosong. Berdasarkan pengetahuan farmakologi yang ditubuhkan, Betamethasone Dipropionate ialah kortikosteroid topikal berkuasa tinggi yang ditunjukkan untuk pelepasan manifestasi radang dan gatal bagi dermatosis yang responsif kepada kortikosteroid (cth: eksema, psoriasis, dermatitis).

---

## Mengapa Ramalan Ini Munasabah?

**Tiada ramalan TxGNN untuk dinilai** pada masa ini. Tatasusunan `predicted_indications` kosong, bermakna model tidak mengembalikan sebarang calon repurposing ubat untuk Betamethasone Dipropionate.

Ini mungkin disebabkan oleh satu atau lebih sebab berikut:
- **Pemetaan ID DrugBank yang hilang**: Paket bukti menunjukkan `drugbank_id: null`. Tanpa pengenal DrugBank yang sah, graf pengetahuan TxGNN tidak dapat mengangkur nod ubat dan oleh itu tidak dapat menghasilkan ramalan repurposing.
- **Had kortikosteroid topikal**: Betamethasone Dipropionate terutamanya digunakan sebagai agen topikal. Ubat dengan mekanisme terutamanya tempatan (bukan sistemik) mungkin mempunyai lebih sedikit sambungan graf pengetahuan kepada nod penyakit sistemik, mengurangkan kemungkinan ramalan berskor tinggi.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam paket bukti ini. Berdasarkan pengetahuan farmakologi umum, Betamethasone Dipropionate ialah kortikosteroid sintetik yang difluorina yang mengeluarkan kesan anti-radang, antipruritus, dan vasokonstriktif dengan mengikat reseptor glukokortikoid intraseluler, menekan pelepasan sitokin pro-radang, dan menghalang aktiviti fosfolipase A2. Mekanisme ini dicirikan dengan baik tetapi medan MOA harus diisi daripada DrugBank untuk membolehkan analisis mekanistik yang betul.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang terdaftar (tiada petunjukan yang diramalkan untuk soalan).

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia (tiada petunjukan yang diramalkan untuk soalan).

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjukan yang Diluluskan |
|------|------|------|------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Isu Kualiti Data:** Kesemua 41 rekod lesen NPRA telah dikembalikan dengan medan kosong (nombor lesen, nama produk, bentuk dos, dan teks petunjukan yang diluluskan semuanya kosong). Soalan NPRA mentah adalah berjaya (`result_count: 41`), tetapi data berstruktur tidak diuraikan ke dalam paket bukti. Ini mesti diperbaiki sebelum laporan dapat diselesaikan.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan paket untuk maklumat keselamatan.
>
> Semua medan data keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini tidak tersedia. Soalan DDI mengembalikan sifar interaksi. Jurang data ini diklasifikasikan sebagai keterukan **Sekatan** — penilaian tidak dapat meneruskan ke saringan keselamatan Tahap 1 tanpa data ini.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Calon ini tidak dapat dinilai kerana (1) tiada ramalan repurposing TxGNN dijana, berkemungkinan disebabkan oleh pemetaan ID DrugBank yang hilang, dan (2) data lesen NPRA, amaran keselamatan, dan mekanisme tindakan semuanya hilang atau kosong. Tiada petunjukan yang diramalkan untuk dinilai.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Selesaikan pemetaan ID DrugBank** — Soal DrugBank untuk "Betamethasone Dipropionate" (log soalan menunjukkan hit DrugBank yang berjaya dengan `result_count: 1`; ID harus ditangkap dan diisi sebagai `drugbank_id` — dijangka: [DB04315](https://go.drugbank.com/drugs/DB04315) atau sebatian induk [DB00443](https://go.drugbank.com/drugs/DB00443) untuk Betamethasone)
2. **Urai semula rekod lesen NPRA** — 41 pendaftaran ditemui tetapi semua medan kosong; muat semula dan urai data berstruktur
3. **Isi MOA daripada DrugBank** — Apabila ID DrugBank diselesaikan, ambil mekanisme tindakan
4. **Ambil data keselamatan** — Muat turun dan urai PDF sisipan paket daripada laman NPRA/TFDA untuk amaran, kontraindikasi, dan interaksi ubat
5. **Jalankan semula ramalan TxGNN** — Dengan ID DrugBank sah yang dipetakan ke dalam graf pengetahuan, jalankan semula saluran ramalan KG dan DL untuk menghasilkan calon repurposing
6. **Hasilkan semula paket bukti** — Apabila jurang di atas diisi, hasilkan paket bukti v5 dan jalankan semula laporan ini

---

*Laporan ini dijana pada 2026-04-09 berdasarkan Paket Bukti v4 (ID calon: TW-UNKNOWN-multi). Hasil adalah untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon repurposing ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

