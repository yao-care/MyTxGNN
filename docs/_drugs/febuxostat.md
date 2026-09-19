---
layout: default
title: Febuxostat
parent: Low Evidence (L4-L5)
nav_order: 339
evidence_level: L5
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **3** 
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

# Febuxostat: Dari Hiperurisemia kepada Hipourisemia Renal, Defisiensi HPRT dan Sindrom Lesch-Nyhan

## Ringkasan Satu Ayat

Febuxostat adalah perencat xanthine oxidase (XO) yang digunakan secara mapan untuk menurunkan asid urik pada hiperurisemia/gaut. Model TxGNN mendedahkan tiga gangguan metabolisme purin yang berkaitan sebagai calon penyusunan semula ubat — **Hipourisemia Renal**, **Defisiensi HPRT Separa (sindrom Kelley-Seegmiller)**, dan **Sindrom Lesch-Nyhan** — namun kekuatan dan bahkan arah rasional berbeza dengan tajam di antara mereka: calon teratas (Hipourisemia Renal) adalah kontra-intuitif mekanik dan hanya disokong oleh satu uji kaji berkaitannya rendah dan dua artikel ulasan, manakala dua calon berperingkat lebih rendah sesuai dengan mekanisme ubat yang diketahui secara langsung tetapi bergantung pada bukti peringkat laporan kes sahaja, tanpa sebarang ujian klinikal berdaftar.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Hiperurisemia / Gaut (terapi penurun asid urik) — disimpulkan daripada teks mekanisme dalam pakej bukti; teks indikasi lesen TFDA itu sendiri tidak dipulangkan (jurang data) |
| Indikasi yang Diramalkan Dinilai | 3 (lihat jadual perbandingan di bawah) |
| Ramalan Teratas | Hipourisemia, Renal (skor 99.99%) — arah kesan adalah kontra-intuitif mekanik, lihat rasional |
| Ramalan Paling Koheren Mekanik | Defisiensi HPRT Separa / Sindrom Lesch-Nyhan |
| Tahap Bukti | L3 (peringkat 1) / L4 (peringkat 2, 3) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 11 |
| Cadangan Keputusan | **Tahan** (disekat — lihat rasional) |

### Perbandingan Indikasi yang Diramalkan

| Peringkat | Penyakit | Skor TxGNN | Tahap Bukti | Peringkat Keputusan | Cadangan |
|---|---|---|---|---|---|
| 1 | Hipourisemia, renal | 99.99% | L3 | S1 | Soalan Penyelidikan |
| 2 | Defisiensi hipoxanthine-guanine phosphoribosyltransferase (HPRT) separa | 99.98% | L4 | S2 | Teruskan dengan Penjaga |
| 3 | Sindrom Lesch-Nyhan | 99.68% | L4 | S2 | Teruskan dengan Penjaga |

---

## Mengapa Ramalan Ini Adalah Munasabah?

Medan `drug.original_moa` ditandakan sebagai jurang data, tetapi mekanisme boleh dibina semula daripada teks rasional pakej bukti itu sendiri: Febuxostat adalah **perencat xanthine oxidase (XO) yang terpilih** yang menyekat penukaran hipoxanthine/xanthine kepada asid urik — asas mekanik penggunaannya yang diluluskan dalam hiperurisemia dan gaut.

Untuk **Hipourisemia Renal (peringkat 1)**, hubungannya tidak mudah: ini adalah keadaan *rendah* urata serum, dan ubat *penurun* asid urik bukanlah rawatan langsung untuknya — merawat hipourisemia dengan febuxostat akan bercanggah mekanik. Hipotesis sebenar yang didedahkan dalam kesusasteraan (PMID 36754409) adalah lebih sempit dan berbeza: dalam pesakit hipourisemia renal yang mengalami kecederaan ginjal akut yang dipicu oleh senaman (EIAKI), aktiviti XO melonjak semasa senaman dan menjana spesies oksigen reaktif (ROS); perencat XO mungkin melindungi ginjal dengan menekan penjanaan ROS, bebas daripada sebarang kesan penurun urata yang lebih lanjut. Ini adalah laluan mekanik yang munasabah tetapi tidak langsung dan tidak disahkan, dan percubaan tunggal yang menyokong (NCT04398251) tidak memberikan perincian yang boleh digunakan mengenai populasi atau titik akhir (Gred Perkaitan C, status Tidak Diketahui).

Untuk **Defisiensi HPRT Separa (peringkat 2)** dan **Sindrom Lesch-Nyhan (peringkat 3)**, kesepadanan mekanik adalah langsung dan konvensional: kedua-duanya disebabkan oleh aktiviti enzim HPRT yang berkurangan/tiada, yang mengalihkan metabolisme purin melalui laluan XO dan menyebabkan hiperurisemia teruk, gaut, dan komplikasi renal. Mekanisme perencat-XO febuxostat bertindak terus pada patologi hiliran ini, dan ia sudah digunakan secara klinikal sebagai alternatif allopurinol dalam populasi pesakit yang sama persis — ini adalah kes pemulihan model terhadap corak penggunaan luar label yang diketahui dan mekanik yang wajar untuk gangguan metabolisme purin yang jarang berlaku daripada penemuan yang baru.

---

## Bukti Uji Kaji Klinikal

| Indikasi | Nombor Ujian | Fasa | Status | Pendaftaran | Penemuan Utama |
|---|---------|------|------|------|---------|
| Hipourisemia, renal | [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fasa 4 | Tidak Diketahui | 100 | Kajian pusat tunggal (Shanghai Xu-hui Central Hospital, Urology) mengenai kawalan asid urik pada pengulangan batu dan fungsi renal dalam pesakit batu kalkuli hiperuremik; tajuk/ringkasan tidak mengesahkan kaitan kepada hipourisemia renal secara khusus (Gred Perkaitan C) |

Defisiensi HPRT Separa dan Sindrom Lesch-Nyhan: **Tiada ujian klinikal berkaitan yang berdaftar pada masa ini.**

---

## Bukti Kesusasteraan

| Indikasi | PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|---|------|-----|------|------|---------|
| Hipourisemia, renal | [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Ulasan | Clinical Rheumatology | Ulasan naratif etiologi hipourisemia dan perkaitan klinikal untuk ahli reumatologi |
| Hipourisemia, renal | [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Ulasan/Kes | Internal Medicine (Tokyo) | Kes hipourisemia renal keluarga (mutasi URAT1) dengan EIAKI berulang; mencadangkan perencat XO bukan purin (termasuk febuxostat) sebagai profilaksis melalui penindasaan ROS |
| Defisiensi HPRT separa | [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Laporan kes | CEN Case Reports | Mutasi HPRT1 p.V35M novel yang menyebabkan defisiensi HPRT separa yang mempersembahkan sebagai gaut remaja keluarga |
| Defisiensi HPRT separa | [26073243](https://pubmed.ncbi.nlm.nih.gov/26073243/) | 2015 | Laporan kes | Internal Medicine (Tokyo) | Mutasi gen HPRT novel digabungkan dengan varian yang diketahui, mempersembahkan sebagai hiperurisemia/gaut dalam seorang berusia 15 tahun |
| Sindrom Lesch-Nyhan | [40763966](https://pubmed.ncbi.nlm.nih.gov/40763966/) | 2025 | Laporan kes/siri | Zhonghua Yi Xue Yi Chuan Xue Za Zhi | Ciri klinikal, genetik, dan rawatan dua kes sindrom Lesch-Nyhan pediatrik |
| Sindrom Lesch-Nyhan | [32128695](https://pubmed.ncbi.nlm.nih.gov/32128695/) | 2020 | Laporan kes | CEN Case Reports | Kes mutasi HPRT1 yang sama seperti di atas, berkaitan dengan spektrum defisiensi HPRT yang lebih luas termasuk sindrom Lesch-Nyhan |

---

## Maklumat Pasaran Malaysia

Pakej bukti mengesahkan Febuxostat adalah **Dipasarkan** di Malaysia dengan **11 jumlah pendaftaran**, tetapi rekod lesen individu (nombor lesen, nama produk, bentuk dos, teks indikasi yang diluluskan) semuanya dipulangkan kosong dalam cabutan data ini — jurang data yang memerlukan pertanyaan semula NPRA/TFDA secara langsung sebelum ini boleh digunakan untuk semakan kawal selia.

---

## Pertimbangan Keselamatan

Sila rujuk risalah penghimpaun untuk maklumat keselamatan.

*(Nota: `key_warnings`, `contraindications`, dan `ddi` semuanya ditandakan sebagai jurang data dalam pakej bukti ini. Ini ditandakan sebagai jurang **Sekatan** (DG001) — ia menghalang secara langsung penyelesaian peringkat saringan keselamatan awal S1 untuk mana-mana tiga indikasi calon, bebas daripada kekuatan bukti individu mereka.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tidak kira seberapa menjanjikan kes mekanik untuk Defisiensi HPRT Separa dan Sindrom Lesch-Nyhan, log jurang data pakej sendiri menandakan amaran label TFDA yang hilang/kontraidikasi (DG001) sebagai **Keparahan Sekatan** — ia secara eksplisit menghalang kemasukan ke dalam peringkat saringan keselamatan awal S1. Tiada indikasi boleh dimajukan melepasi pintu gerbang ini sehingga data itu disediakan. Secara berasingan, calon teratas (Hipourisemia Renal) mempunyai rasional yang tidak langsung mekanik dan hanya bukti ujian Gred C, dan tidak boleh diprioritaskan walaupun pintu gerbang keselamatan dibersihkan.

**Untuk meneruskan, yang berikut diperlukan:**
- Label produk TFDA/NPRA (amaran, kontraidikasi, DDI) — diperlukan untuk membersihkan pintu gerbang keselamatan S1 yang Sekatan
- Dokumentasi MOA asal terperinci daripada DrugBank (pada masa ini jurang data Keparahan Tinggi)
- Perincian peringkat lesen NPRA penuh (nama produk, bentuk dos, teks indikasi) untuk 11 pendaftaran
- Penjelasan populasi/titik akhir sebenar ujian NCT04398251 untuk mengesahkan atau menolak perkaitan kepada hipourisemia renal
- Memandangkan kelangkaan defisiensi HPRT dan sindrom Lesch-Nyhan, bukti dunia nyata/daftar harus dicari untuk menambah asas kesusasteraan kes-saja sebelum sebarang penggunaan berpenjaga dimuktamadkan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

