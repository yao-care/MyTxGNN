---
layout: default
title: Betaxolol Hcl
parent: Low Evidence (L4-L5)
nav_order: 139
evidence_level: L5
indication_count: 0
---

# Betaxolol Hcl
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

# BETAXOLOL HCL: Penilaian Ubah Guna Ubat — Menunggu Data Ramalan

## Ringkasan Satu Ayat

Betaxolol HCl adalah penghambat reseptor adrenergik beta-1 selektif, tersedia di Malaysia dengan 2 produk berdaftar.
Model TxGNN **belum menghasilkan indikasi yang diramalkan** untuk ubat ini,
dan jurang data kritikal (MOA, profil keselamatan, butiran lesen) tetap perlu ditangani sebelum penilaian boleh diteruskan.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Indikasi Asal | *(Butiran lesen tertunda — medan data pendaftaran kosong)* |
| Indikasi Baharu Diramalkan | **Tiada** — tiada ramalan TxGNN tersedia |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | L5 (Tiada ramalan atau bukti sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 2 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini **tiada ramalan TxGNN** untuk dinilai bagi Betaxolol HCl. Tatasusunan `predicted_indications` adalah kosong, bermaksud model belum mengenal pasti indikasi kandidat baharu untuk ubat ini.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pakej bukti ini. Berdasarkan klasifikasi farmakoloji yang diketahui, Betaxolol HCl adalah antagonis reseptor adrenergik beta-1 selektif (beta-blocker). Ia biasanya digunakan dalam bentuk oral untuk pengurusan tekanan darah tinggi, dan dalam bentuk oftalmik untuk pengurangan tekanan intra-okular dalam glukoma sudut terbuka atau hipertensi okular. Selektivitasnya untuk reseptor beta-1 berbanding reseptor beta-2 adalah ciri pembeza berbanding beta-blocker bukan selektif.

Sebelum penilaian ubah guna boleh dijalankan, saluran paip ramalan TxGNN mesti dijalankan untuk sebatian ini, dan indikasi kandidat yang terhasil mesti diisi ke dalam pakej bukti. Selain itu, pemetaan ID DrugBank (pada masa ini null) perlu diselesaikan untuk membolehkan pengumpulan bukti automatik.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan didaftarkan — tiada indikasi yang diramalkan tersedia untuk dicari.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan tersedia — tiada indikasi yang diramalkan tersedia untuk dicari.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Terluluskan |
|------|------|------|------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Nota:** 2 pendaftaran direkodkan dalam pangkalan data kawal selia, tetapi semua medan butiran lesen (nombor kebenaran, nama produk, bentuk dos, indikasi terluluskan) adalah kosong. Ini perlu diambil daripada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan bungkusan untuk maklumat keselamatan.
>
> Semua medan data keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini tidak tersedia. Ini mesti diambil sebelum sebarang penilaian ubah guna boleh diteruskan — ini ditandai sebagai jurang data **Menyekat** (DG001).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Pakej bukti ini hilang data kritikal di setiap tahap: tiada indikasi yang diramalkan TxGNN, tiada pemetaan ID DrugBank, tiada data MOA, butiran lesen kosong, dan tiada maklumat keselamatan. Penilaian ubah guna yang bermakna tidak boleh dijalankan sehingga jurang ini diselesaikan.

**Untuk meneruskan, berikut diperlukan:**

1. **Pemetaan ID DrugBank** — Selesaikan ID DrugBank untuk Betaxolol HCl (pertanyaan mengembalikan 1 hasil setiap log, tetapi ID tidak dipopulasi; berkemungkinan `DB00195`)
2. **Ramalan TxGNN** — Jalankan saluran paip ramalan KG dan/atau DL untuk menghasilkan indikasi kandidat baharu
3. **Butiran lesen NPRA** — Populatkan nombor kebenaran, nama produk, bentuk dos, dan teks indikasi terluluskan untuk 2 produk berdaftar
4. **Data keselamatan (Menyekat)** — Muat turun dan analisis PDF sisipan bungkusan daripada laman web NPRA untuk mengekstrak amaran, kontraindikasi, dan interaksi ubat
5. **Data MOA** — Pertanyaan API DrugBank untuk mendapatkan butiran mekanisme tindakan
6. **Pengumpulan bukti** — Apabila indikasi yang diramalkan tersedia, jalankan pengumpul ClinicalTrials.gov, PubMed, dan ICTRP

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

