---
layout: default
title: Amorolfine
parent: Low Evidence (L4-L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Amorolfine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Amorolfine: Daripada Onychomycosis Kepada Drug-Induced Osteoporosis

## Ringkasan Satu Ayat

Amorolfine ialah ejen antijamur topikal dari kelas morfolin, yang terutamanya digunakan untuk rawatan onychomycosis (jangkitan kulat kuku) dengan mengganggu membran sel kulat melalui penghambatan biosintesis ergosterol.
Model TxGNN meramalkan bahawa ia mungkin berkesan untuk **Drug-Induced Osteoporosis**, dengan **0 ujian klinikal** dan **0 penerbitan** yang pada masa ini menyokong arah ini.
Ramalan ini sepenuhnya bergantung pada hasil model, meletakkannya pada Tahap Bukti **L5** — tahap paling rendah.

---

## Ikhtisar Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Onychomycosis (jangkitan kulat kuku) |
| Indikasi Baru yang Diramalkan | Drug-Induced Osteoporosis |
| Skor Ramalan TxGNN | 99.998% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | **Tangguhkan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia dalam Evidence Pack ini. Berdasarkan farmakologi yang telah ditegakkan, Amorolfine termasuk dalam kelas morfolin antijamur. Cara kerjanya adalah dengan menghambat dua enzim kulat utama — Δ14-reductase dan Δ7-Δ8-isomerase — dalam laluan biosintesis ergosterol. Ini menyebabkan sterol perantara beracun menumpuk dalam membran sel kulat, yang akhirnya mengakibatkan kematian sel. Penting sekali, laluan ini spesifik kepada kulat dan tidak wujud dalam sel mamalia.

Kaitan yang dicadangkan dengan osteoporosis yang diinduksi ubat sangat lemah secara mekanis. Metabolisme tulang pada manusia dikawal oleh keseimbangan antara osteoblas (pembentukan tulang) dan osteoklas (resorpsi tulang), suatu proses yang tidak mempunyai hubungan yang diketahui dengan biosintesis ergosterol. Analogi dangkal boleh diambil kepada antijamur azol tertentu (contohnya vorikonazol), yang telah dikaitkan dengan periostitis dan anomali tulang — bagaimanapun, kesan tersebut dimediasi oleh perencatan CYP450 sistemik dan pengumpulan fluorida, suatu mekanisme yang sama sekali tidak terpakai kepada amorolfine. Amorolfine diberikan secara eksklusif sebagai pernis kuku topikal dengan penyerapan sistemik yang boleh diabaikan, bermaksud ia tidak boleh menjalankan kesan farmakologi sistemik pada tisu tulang.

Ringkasnya, meskipun model TxGNN memberikan skor ramalan tinggi (mungkin mencerminkan kedekatan struktur atau graph-embedding dalam knowledge graph), tiada laluan biologi yang boleh dipercayai pada masa ini yang menghubungkan mekanisme antijamur amorolfine dengan osteoporosis yang diinduksi ubat. Ramalan ini tidak boleh dimajukan tanpa terlebih dahulu mengenal pasti hipotesis mekanis yang munasabah.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang terdaftar.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

Amorolfine mempunyai **3 produk berdaftar** dengan NPRA di Malaysia (status pasaran: Dipasarkan). Maklumat produk terperinci — termasuk nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan — belum diisi dalam Evidence Pack ini. Data ini harus diambil terus daripada portal pencarian produk NPRA.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|-------------|-----------|-------------------------|
| *(Menunggu pengambilan)* | *(Menunggu pengambilan)* | *(Menunggu pengambilan)* | *(Menunggu pengambilan)* |

---

## Pertimbangan Keselamatan

Sila rujuk lembaran maklumat produk untuk maklumat keselamatan.

> **Nota:** Kedua-dua amaran utama dan kontraindikasi telah ditandai sebagai jurang data dalam Evidence Pack ini (keterukan: Blocking dan High masing-masing). Semakan keselamatan lengkap tidak boleh diteruskan sehingga lembaran maklumat produk NPRA (Ringkasan Ciri-ciri Produk) telah dimuat turun dan dihuraikan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguhkan**

**Alasan:**
Calon ini disokong semata-mata oleh ramalan model TxGNN (Tahap Bukti L5) tanpa ujian klinikal terdaftar dan tanpa literatur yang diterbitkan. Tambahan pula, kaitan mekanis antara perencatan ergosterol spesifik kulat amorolfine dan osteoporosis yang diinduksi ubat tidak munasabah secara biologi — ubat ini mempunyai pendedahan sistemik yang boleh diabaikan, dan laluan sasaran yang dicadangkan tidak wujud dalam tisu tulang mamalia.

**Untuk meneruskan, yang berikut diperlukan:**
- Ambil butiran pendaftaran NPRA lengkap (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) untuk semua 3 produk berdaftar
- Muat turun dan huraikan PDF lembaran maklumat produk NPRA untuk mengisi data keselamatan (amaran utama, kontraindikasi) — pada masa ini merupakan jurang data **Blocking**
- Soal API DrugBank (DB09056) untuk mendapatkan mekanisme tindakan lengkap (MOA) — pada masa ini merupakan jurang data **High** severity
- Lakukan carian literatur praklinikal yang lebih luas untuk menentukan sama ada sebarang sebatian kelas morfolin (selain antijamur) telah menunjukkan aktiviti metabolisme tulang
- Jika sebarang isyarat praklinikal muncul, rancang kajian in vitro yang tersasaran sebelum mempertimbangkan kemajuan klinikal
- Nilaikan semula justifikasi ramalan: jika tiada kaitan mekanis yang boleh ditegakkan selepas langkah-langkah di atas, tutup calon ini secara rasmi

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

