---
layout: default
title: Gliclazide
parent: Low Evidence (L4-L5)
nav_order: 369
evidence_level: L5
indication_count: 5
---

# Gliclazide
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
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

# Gliclazide: Daripada Type 2 Diabetes Mellitus kepada Type 2 Diabetes Mellitus (Tiada Isyarat Indikasi Baru yang Sah)

## Ringkasan Satu Ayat

Gliclazide adalah sulfonilurea generasi kedua yang telah diluluskan dan dipasarkan untuk type 2 diabetes mellitus (T2DM). Kesemua lima "indikasi yang diramal" yang dikembalikan oleh TxGNN untuk calon ini adalah varian penyakit yang sama (T2DM / diabetes mellitus) dengan **skor TxGNN 0.0**, menunjukkan ini bukan isyarat penggunaan semula yang tulin tetapi artifak data yang disebabkan oleh medan `original_indications` yang hilang di hulu. **35 uji klinis dan 20 penerbitan** telah diambil, tetapi mereka menyokong indikasi sedia ada yang telah diluluskan untuk gliclazide — bukan yang baru.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|------|
| Indikasi Asal | Type 2 Diabetes Mellitus (berdasarkan farmakoloji yang telah terbukti; teks indikasi lesen NPRA tidak diambil dalam penarikan data ini) |
| "Indikasi Baru" yang Diramal | Type 2 Diabetes Mellitus (pendua indikasi asal — lihat rasional di bawah) |
| Skor Ramalan TxGNN | 0.00% |
| Tahap Bukti | L1 (kualiti bukti tinggi, tetapi ini menyokong indikasi yang *sedia ada*, bukan hipotesis penggunaan semula) |
| Status Pasaran Malaysia | ✓ Dipasarkan (NPRA) |
| Bilangan Pendaftaran | 36 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, rekod mekanisme tindakan (MOA) yang berstruktur tidak tersedia dalam DrugBank untuk calon ini (ditandai sebagai jurang data berketerukan tinggi, DG002). Berdasarkan farmakoloji yang diketahui yang ditangkap dalam rasional penggunaan semula paket bukti itu sendiri: gliclazide adalah sulfonilurea generasi kedua yang bertindak langsung pada saluran SUR1/Kir6.2 (K_ATP) sel β pankreas. Penutupan saluran mencetuskan depolarisasi membran, membuka saluran kalsium berfungsi voltan, dan merangsang sekresi insulin — ini adalah mekanisme penurun glukosa asal gliclazide yang **telah diluluskan**, bukan lintasan yang baru ditemui.

Kesemua lima indikasi "diramal" yang disenaraikan kedudukan dalam paket bukti ini adalah "type 2 diabetes mellitus" atau "diabetes mellitus" pada granulariti yang berbeza. Ini bukan hipotesis penggunaan semula: ia adalah ubatan sendiri muncul semula kerana medan `drug.original_indications` di hulu kosong, jadi langkah deduplikasi yang sepatutnya mengecualikan indikasi yang sudah diketahui daripada senarai calon penggunaan semula tidak berlaku. `txgnn.score = 0.0` merentasi kesemua lima pangkat mengesahkan ini — TxGNN sebenarnya tidak memberikan keyakinan kepada ini sebagai tepi ubatan–penyakit novel.

**Kesimpulan: tiada hipotesis saintifik yang bermakna "ubatan lama, kegunaan baru" untuk dinilai di sini.** Tindakan yang betul adalah pembaikan saluran paip data, bukan penilaian klinis.

---

## Bukti Ujian Klinis

*(Bukti di bawah mendokumenkan prestasi gliclazide dalam indikasi sedia adanya, T2DM — bukan indikasi baru.)*

| Nombor Ujian | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT01709305](https://clinicaltrials.gov/study/NCT01709305) | Fasa 4 | Selesai | 5,570 | Ujian rawak terkawal berbilang pusat China yang besar membandingkan gliclazide, glimepiride, repaglinide, atau acarbose sebagai tambahan lini ketiga kepada sitagliptin+metformin dalam T2DM |
| [NCT00102388](https://clinicaltrials.gov/study/NCT00102388) | Fasa 3 | Selesai | 1,092 | Vildagliptin berbanding gliclazide dalam pesakit T2DM yang naif dadah — perbandingan keberkesanan/keselamatan langsung |
| [NCT01758380](https://clinicaltrials.gov/study/NCT01758380) | Fasa 4 | Selesai | 557 | Ujian rawak terkawal buta ganda, dummy buta ganda membandingkan vildagliptin berbanding gliclazide sebagai terapi dwi dengan metformin semasa puasa Ramadan |
| [NCT01420692](https://clinicaltrials.gov/study/NCT01420692) | N/A | Selesai | 64 | Insulin detemir berbanding gliclazide-MR ditambahkan kepada pengubahsuaian gaya hidup + metformin — kesan pada fungsi endotel |
| [NCT00738088](https://clinicaltrials.gov/study/NCT00738088) | Fasa 4 | Dibatalkan | 14 | Kajian mekanis respons glikemik sulfonilurea dan patofisiologi T2DM |
| [NCT02092597](https://clinicaltrials.gov/study/NCT02092597) | Fasa 4 | Selesai | 42 | Penilaian keselamatan terapi berasaskan incretin pada sistem kardiovaskular, GI, dan buah pinggang |
| [NCT01195259](https://clinicaltrials.gov/study/NCT01195259) | N/A | Selesai | 1 | Meta-analisis kesan buruk keganasan ADOPT/RECORD (metformin versus rosiglitazone) — tidak berkaitan langsung dengan gliclazide; kemungkinan artifak pautan pangkalan data |
| [NCT06704802](https://clinicaltrials.gov/study/NCT06704802) | N/A | Selesai | 678 | Kohort pemerhatian menilai program pendidikan digabungkan dengan gliclazide MR pada HbA1c dalam T2DM yang tidak terkawal |
| [NCT02475499](https://clinicaltrials.gov/study/NCT02475499) | N/A | Selesai | 886,172 | Kajian farmakoepidemiologi ubat berasaskan incretin dan risiko kanser pankreas, menggunakan sulfonilurea sebagai pembanding |
| [NCT03246828](https://clinicaltrials.gov/study/NCT03246828) | N/A | Selesai | 10 | Kesan gliclazide pada sekresi glukagon dalam HNF1A/HNF4A-MODY (subtip diabetes atipik, bukan T2DM) |

---

## Bukti Kesusasteraan

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [18539916](https://pubmed.ncbi.nlm.nih.gov/18539916/) | 2008 | Ujian RCT | New England Journal of Medicine | Ujian ADVANCE: kawalan glukosa intensif (berasaskan gliclazide MR) dan hasil pembuluh darah dalam T2DM |
| [39792745](https://pubmed.ncbi.nlm.nih.gov/39792745/) | 2025 | Ujian RCT | Medicine | Sitagliptin berbanding gliclazide + metformin dalam T2DM rawat pertama dengan glukotoksisiti |
| [40326063](https://pubmed.ncbi.nlm.nih.gov/40326063/) | 2025 | Ujian RCT (silih ganti) | Diabetes, Obesity & Metabolism | RACELINES: kesan hemiodinamik buah pinggang empagliflozin/linagliptin berbanding gliclazide |
| [36300277](https://pubmed.ncbi.nlm.nih.gov/36300277/) | 2022 | Ulasan | Expert Opinion on Pharmacotherapy | Gambaran keseluruhan peranan gliclazide dalam pengurusan T2DM berbanding agen yang lebih baru |
| [29802958](https://pubmed.ncbi.nlm.nih.gov/29802958/) | 2018 | Ulasan | Diabetes Research and Clinical Practice | Kedudukan gliclazide MR di kalangan sulfonilurea dan antihiperglikemik yang lebih baru |
| [24533045](https://pubmed.ncbi.nlm.nih.gov/24533045/) | 2014 | Ulasan Sistematik/Meta-analisis | PLoS ONE | Keselamatan dan keberkesanan gliclazide berbanding agen penurun glukosa lain |
| [35398820](https://pubmed.ncbi.nlm.nih.gov/35398820/) | 2022 | Pemerhatian | Acta Medica Indonesiana | Kajian DIA-RAMADAN di dunia sebenar tentang keselamatan/keberkesanan gliclazide MR semasa Ramadan |
| [32516291](https://pubmed.ncbi.nlm.nih.gov/32516291/) | 2020 | Ujian RCT/Kohort | Journal of Hypertension | Kesan kardio-buah pinggang dapagliflozin berbanding gliclazide dalam T2DM |
| [29558784](https://pubmed.ncbi.nlm.nih.gov/29558784/) | 2019 | Ujian RCT | Exp Clin Endocrinol Diabetes | Alogliptin dan gliclazide sama-sama meningkatkan sel progenitor endotel beredar |
| [30119196](https://pubmed.ncbi.nlm.nih.gov/30119196/) | 2018 | Kajian PK | Biomedicine & Pharmacotherapy | Kepekatan gliclazide keadaan stabil minimum dalam pesakit T2DM pada tablet MR |

---

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan gliclazide sedang dipasarkan di Malaysia dengan **36 lesen produk yang didaftarkan**. Walau bagaimanapun, penarikan data ini tidak mengambil semula nombor lesen individu, nama produk, bentuk dos, atau teks indikasi (semua medan terperinci lesen dikembalikan kosong), jadi jadual setiap produk tidak dapat dibentangkan. Jurang ini harus diperbetulkan dengan menanyakan semula daftar produk NPRA untuk penyenaraian lesen lengkap.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan.

*(Amaran sisipan paket TFDA/NPRA dan kontraindikasi ditandai sebagai jurang data berketerukan Pemblokiran (DG001) dalam paket bukti ini — tiada data amaran utama, kontraindikasi, atau interaksi ubat yang dapat diambil semula.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
- Kesemua lima indikasi "baru" yang diramal adalah indikasi sedia ada ubatan itu sendiri (T2DM) pada granulariti penamaan yang berbeza, dengan skor TxGNN 0.0 — ini adalah artifak penduplikatan saluran paip data (medan `original_indications` yang hilang), bukan hipotesis penggunaan semula. Tiada apa-apa di sini untuk dinilai sebagai "ubatan lama, kegunaan baru."
- Secara berasingan, jurang berketerukan Pemblokiran (amaran sisipan paket/kontraindikasi yang hilang) bermakna calon ini tidak dapat lulus walaupun skrin keselamatan asas (S1) tanpa mengira soalan indikasi.

**Untuk meneruskan, perkara berikut diperlukan:**
- Baiki saluran paip data hulu untuk memenuhi `drug.original_indications` untuk gliclazide dan jalankan semula deduplikasi supaya indikasi yang telah diluluskan dikecualikan daripada senarai calon penggunaan semula
- Ambil amaran sisipan paket TFDA/NPRA, kontraindikasi, dan data DDI (DG001, Pemblokiran)
- Ambil data MOA berstruktur daripada DrugBank (DG002, Tinggi)
- Tanya semula NPRA untuk terperinci produk lesen setiap satu lengkap (nombor lesen, nama produk, bentuk dos, teks indikasi)
- Jika TxGNN dijalankan semula selepas pembaikan data dan permukaan indikasi yang berbeza secara tulin dan bukan skor sifar untuk gliclazide, penilaian semula sebagai calon baru

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

