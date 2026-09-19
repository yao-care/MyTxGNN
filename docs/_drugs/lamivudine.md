---
layout: default
title: Lamivudine
parent: High Evidence (L1-L2)
nav_order: 423
evidence_level: L1
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **5** 
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

# Lamivudine: Dari Indikasi Asal yang Tidak Terdokumentasikan kepada Jangkitan Penyakit Berjangkit HIV

## Ringkasan Satu Ayat

Lamivudine (3TC, DrugBank DB00709) adalah penghambat reverse transcriptase analog sitidina; rekod lesen NPRA Malaysia dalam pakej bukti ini tidak mengandungi teks indikasi asal yang boleh digunakan (jurang data), jadi penggunaan berlesen sebenarnya tidak dapat dipetik terus daripada set data ini. Ramalan model TxGNN teratas — **jangkitan penyakit berjangkit HIV** — disokong oleh **50 percubaan klinikal** dan **20 penerbitan**, tetapi bukti itu sendiri menunjukkan ini kemungkinan besar adalah indikasi antiretroviral lamivudine yang telah lama wujud dan telah diluluskan, bukan isyarat pengguna semula yang benar-benar baru (lihat kaveat di bawah). Isyarat kedua yang sama-sama disokong, jangkitan virus hepatitis B kronik, menunjukkan corak yang sama.

> **Kaveat penting:** Medan rasional pakej bukti sendiri menyatakan bahawa kedua-dua "jangkitan penyakit berjangkit HIV" dan "jangkitan virus hepatitis B kronik" adalah indikasi bersejarah lamivudine yang telah diluluskan (Epivir® untuk HIV; Epivir-HBV® / Zeffix® untuk HBV), dan bahawa medan `original_indications` yang kosong harus dibaca sebagai jurang data, bukan sebagai bukti ini adalah kegunaan baharu. Pangkat 3–5 dalam set ramalan asas adalah hampir-duplikat pangkat 1–2 (AIDS adalah peringkat klinikal jangkitan HIV, dan pangkat 4–5 mengulangi pangkat 1–2), konsisten dengan artifak saluran data bukan lima isyarat bebas. Laporan ini harus dibaca sebagai kes **kelengkapan data / pengesahan**, bukan kes penemuan.

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak didokumentasikan dalam ekstrak lesen NPRA semasa (jurang data — DG001/DG002). Mengikut nota mekanik pakej bukti itu sendiri, kegunaan sebenar lamivudine yang diluluskan ialah jangkitan HIV-1 dan hepatitis B kronik. |
| Indikasi Baru Diramalkan | Jangkitan penyakit berjangkit HIV |
| Skor Ramalan TxGNN | 0.00% (seperti yang tercatat dalam pakej bukti — lihat nota di bawah) |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 30 |
| Keputusan Yang Disyorkan | Teruskan dengan Penjaga |

*Nota mengenai skor:* pakej bukti merekod skor TxGNN sebanyak 0.0 untuk setiap indikasi berpangkat, yang tidak tipikal untuk calon berpangkat teratas dan mungkin sendiri adalah artifak dari jurang data yang sama menjejaskan `original_indications`. Ini harus disahkan terhadap keluaran model mentah sebelum skor digunakan dalam sebarang pemeringkatan hiliran.

## Mengapa Ramalan Ini Munasabah?

Pada masa kini, rekod mekanisme-tindakan berstruktur tidak tersedia dalam medan DrugBank bagi pakej bukti ini ([Jurang Data] / DG002). Bagaimanapun, rasional pengguna semula yang dilampirkan pada setiap calon berpangkat memang menerangkan mekanisme: Lamivudine (3TC) ialah analog nukleosida sitidina yang, selepas pemfosforilan intraseluler kepada lamivudine trifosfat, secara kompetitif menghalang reverse transcriptase HIV-1 dan dipasukkan ke dalam rantaian DNA viral yang sedang berkembang, menyebabkan penamatan rantaian. Trifosfat yang sama juga menghalang polimerase DNA HBV (yang mempunyai aktiviti reverse-transcriptase), menghalang reverse transcription RNA pregenomic HBV.

Kedua-duanya digambarkan dalam data sumber sebagai **indikasi sedia ada lamivudine yang telah diluluskan** (jangkitan HIV-1 sebagai ejen tulang belakang NRTI, dan hepatitis B kronik di bawah nama jenama Epivir-HBV/Zeffix), bukan sebagai farmakologi yang baru ditemui. AIDS (pangkat 3) adalah mudah-mudahan hanya peringkat klinikal lanjutan jangkitan HIV bukan entiti penyakit yang berbeza, dan ia mengambil dari asas bukti yang sama seperti pangkat 1.

Berdasarkan ini, "ramalan" paling baik ditafsirkan sebagai model yang menerbitkan semula kegunaan yang mantap daripada graf pengetahuan, kemungkinan besar kerana medan `original_indications` kosong apabila model dijalankan (jurang kemasukan data bukan ketiadaan indikasi sebenar). Bukti klinikal dan kesusasteraan di bawah adalah oleh itu sangat matang — percubaan merentangi hampir tiga dekad (1996–2028) — yang adalah sendirinya konsisten dengan indikasi yang ditubuhkan bukan indikasi yang baru muncul.

## Bukti Percubaan Klinikal

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Kunci |
|---------|------|------|------|---------|
| [NCT00038506](https://clinicaltrials.gov/study/NCT00038506) | Fasa 4 | Selesai | 100 | Kajian labelan terbuka TRIZIVIR (abacavir/lamivudine/zidovudine) ditambah intensifikasi tenofovir dalam pesakit HIV dengan kegagalan virologik awal |
| [NCT00053638](https://clinicaltrials.gov/study/NCT00053638) | Fasa 3 | Selesai | 345 | Efavirenz lawan tenofovir, masing-masing ditambah dosis tetap abacavir/lamivudine, dalam pesakit HIV-1 naif antiretroviral |
| [NCT03205566](https://clinicaltrials.gov/study/NCT03205566) | Fasa 4 | Selesai | 38 | Raltegravir dengan atau tanpa lamivudine untuk perlindungan terhadap jangkitan HIV tisu genital; profil PK/PD pereputan |
| [NCT01449929](https://clinicaltrials.gov/study/NCT01449929) | Fasa 3 | Selesai | 488 | Dolutegravir lawan darunavir/ritonavir, masing-masing dengan tulang belakang NRTI ganda (abacavir/lamivudine atau tenofovir/emtricitabine), selama 96 minggu dalam dewasa naif ART |
| [NCT00197613](https://clinicaltrials.gov/study/NCT00197613) | Fasa 3 | Selesai | 650 | Kajian Tshepo — kajian pertama berskala besar rintangan antiretroviral dan hasil rawatan di Botswana |
| [NCT00001083](https://clinicaltrials.gov/study/NCT00001083) | Fasa 2 | Selesai | 240 | PRAM-1: zidovudine+lamivudine lawan stavudine+ritonavir lawan kombinasi tiga kali dalam kanak-kanak terinfeksi HIV yang berpengalaman antiretroviral |
| [NCT00002411](https://clinicaltrials.gov/study/NCT00002411) | T/A | Selesai | T/A | Penindasan jangka panjang RNA HIV plasma oleh rejimen kombinasi tiga kali (termasuk zidovudine+lamivudine+nelfinavir) dalam subjek naif rawatan |
| [NCT00000887](https://clinicaltrials.gov/study/NCT00000887) | Fasa 1 | Selesai | 24 | Keselamatan/PK nelfinavir + zidovudine + lamivudine dalam wanita hamil terinfeksi HIV dan bayi |
| [NCT00000865](https://clinicaltrials.gov/study/NCT00000865) | Fasa 1 | Selesai | 32 | PK keadaan mantap, toleransi dan keselamatan 1592U89 (abacavir) sahaja atau dengan agen antiretroviral lain, termasuk rejimen yang mengandungi lamivudine, dalam kanak-kanak terinfeksi HIV |

## Bukti Kesusasteraan

| PMID | Tahun | Jenis | Jurnal | Penemuan Kunci |
|------|-----|------|------|---------|
| [32504574](https://pubmed.ncbi.nlm.nih.gov/32504574/) | 2020 | RCT | The Lancet HIV | Keputusan minggu-144: bictegravir/emtricitabine/TAF tidak inferior kepada rejimen yang mengandungi dolutegravir dalam pesakit naif rawatan HIV |
| [39826566](https://pubmed.ncbi.nlm.nih.gov/39826566/) | 2025 | RCT | The Lancet HIV | Percubaan D2ARLING: keberkesanan dolutegravir + lamivudine dalam pesakit naif rawatan HIV tanpa ujian rintangan asas |
| [40874763](https://pubmed.ncbi.nlm.nih.gov/40874763/) | 2026 | RCT | Clinical Infectious Diseases | Kajian DOLCE: terapi ganda dolutegravir/lamivudine dalam pesakit naif rawatan dengan CD4 <200/mm³ |
| [36094514](https://pubmed.ncbi.nlm.nih.gov/36094514/) | 2022 | RCT | J Acquir Immune Defic Syndr | Kohort pelbagai pusat China mengesahkan keberkesanan virologik dan keselamatan terapi ganda lamivudine + dolutegravir yang dipermudahkan |
| [29474268](https://pubmed.ncbi.nlm.nih.gov/29474268/) | 2018 | Ulasan | J Acquir Immune Defic Syndr | Tinjauan retrospektif 25 tahun tentang peranan lamivudine dan relevansinya yang berterusan dalam rawatan HIV-1 |
| [24754315](https://pubmed.ncbi.nlm.nih.gov/24754315/) | 2014 | Ulasan | Expert Opin Pharmacother | Ulasan sifat rejimen tablet tunggal dolutegravir/abacavir/lamivudine |
| [37832567](https://pubmed.ncbi.nlm.nih.gov/37832567/) | 2023 | Kohort | The Lancet HIV | Analisis kohort DTG RESIST kolaboratif pada corak mutasi rintangan di bawah ART berasaskan dolutegravir |
| [31503008](https://pubmed.ncbi.nlm.nih.gov/31503008/) | 2019 | Kohort | Antiviral Therapy | Ulasan sistematik pada mutasi rintangan pra-rawatan/diperoleh kepada lamivudine atau rilpivirine |
| [11996639](https://pubmed.ncbi.nlm.nih.gov/11996639/) | 2002 | Ulasan | Expert Opin Pharmacother | Gambaran keseluruhan tablet gabungan Trizivir (zidovudine/lamivudine/abacavir) |
| [26517111](https://pubmed.ncbi.nlm.nih.gov/26517111/) | 2015 | Ulasan | Expert Rev Clin Pharmacol | Ulasan kombinasi dos tetap Dutrebis (lamivudine/raltegravir) untuk rawatan HIV-1 |

## Maklumat Pasaran Malaysia

Pakej bukti melaporkan **30 pendaftaran NPRA jumlah keseluruhan** dengan status pasaran "Dipasarkan," tetapi lima rekod lesen yang disertakan dalam eksport ini tidak mengandungi medan yang diisi (nombor lesen, nama produk, bentuk dos, pengeluar, dan teks indikasi semuanya kosong). Ini adalah jurang kelengkapan data dalam ekstrak semasa, bukan bukti daftar kosong — bilangan agregat (30) mengesahkan kehadiran pasaran yang aktif, tetapi butiran lesen individu perlu ditarik semula daripada sumber NPRA sebelum ia boleh dilaporkan.

## Pertimbangan Keselamatan

Sila rujuk pada sisipan pakej untuk maklumat keselamatan.

*Bendera untuk pengulas:* pakej bukti asas menandakan amaran dan kontraindikasi sisipan pakej TFDA/NPRA yang hilang (DG001) sebagai jurang data keterukan **Menghalang**, secara jelas dicatat sebagai menghalang kemasukan ke dalam peringkat pra-penilaian keselamatan S1. Ini harus diselesaikan sebelum calon ini maju melepasi peringkat semasa, tanpa mengira kekuatan bukti klinikal/kesusasteraan di atas.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Penjaga**

**Rasional:**
Asas percubaan klinikal dan kesusasteraan untuk lamivudine dalam jangkitan HIV adalah luas dan matang (L1), tetapi pakej bukti sendiri menunjukkan ini kemungkinan besar adalah pengenalan semula indikasi antiretroviral lamivudine yang diketahui dan telah diluluskan bukan penemuan pengguna semula baru — jurang "indikasi asal" dalam data sumber harus ditutup sebelum ini dianggap sebagai calon pengguna semula yang tulen. Secara berasingan, jurang data keselamatan keterukan Menghalang (amaran TFDA/NPRA dan kontraindikasi) bermakna pra-penilaian keselamatan S1 belum dapat disiapkan.

**Untuk meneruskan, berikut diperlukan:**
- Selesaikan DG001: ambil dan parse sisipan pakej TFDA/NPRA (amaran, kontraindikasi) — pada masa kini menghalang pra-penilaian keselamatan
- Selesaikan DG002: dapatkan rekod mekanisme-tindakan berstruktur daripada DrugBank
- Tarik semula rekod lesen NPRA dengan medan yang diisi (nombor lesen, nama produk, bentuk dos, pengeluar, teks indikasi) — lima entri semasa kosong
- Sahkan sama ada `original_indications` benar-benar kosong pada masa ramalan, atau sama ada ini adalah kecacatan saluran data yang menyebabkan indikasi yang diketahui (HIV, HBV) dipermukaan sebagai "ramalan"
- Singkirkan duplikat set ramalan — pangkat 1/4 (HIV) dan pangkat 2/5 (HBV) nampaknya berulang, dan pangkat 3 (AIDS) bertindih dengan pangkat 1; jelaskan sama ada ini mencerminkan lima keluaran model bebas atau artifak saluran sebelum menggunakan bilangan pangkat dalam pemarkahan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

