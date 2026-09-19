---
layout: default
title: Fluvoxamine
parent: High Evidence (L1-L2)
nav_order: 358
evidence_level: L1
indication_count: 10
---

# Fluvoxamine
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
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

# Fluvoxamine: Daripada Gangguan Obsesif-Kompulsif kepada Gangguan Spektrum Kegelisahan yang Lebih Luas

## Ringkasan Satu Ayat

Fluvoxamine ialah penghambat pemasukan semula serotonin terpilih (SSRI) yang teks indikasi asal hilang daripada rekod sumber, walaupun pakej bukti sendiri secara berulang mendokumentasikan ia sebagai rawatan yang sudah diluluskan untuk **gangguan obsesif-kompulsif (OCD)**. Ramalan teratas TxGNN adalah, sebenarnya, OCD itu sendiri — nisbah TxGNN sendiri menandai ini sebagai berkemungkinan duplikat penggunaan yang sudah diluluskan dan bukannya indikasi baharu yang tulen. Isyarat pengguna semula yang lebih dipercayai dalam pakej ini ialah **gangguan kegelisahan** dan **agorafobia** (kedudukan 6–7), masing-masing disokong oleh pelbagai ujian klinis terkawal plasebo (bukti L2).

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tercatat dalam data berstruktur (teks indikasi lesen TFDA/NPRA dan `original_indications` DrugBank kedua-duanya kosong). Kesusasteraan dalam pakej ini secara konsisten mendokumentasikan fluvoxamine sebagai SSRI yang sudah dipasarkan untuk OCD. |
| Indikasi Baharu yang Diramal | Gangguan Obsesif-Kompulsif *(⚠ lihat kaveat di bawah — berkemungkinan bukan indikasi baharu yang tulen)* |
| Skor Ramalan TxGNN | 99.99% |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 6 |
| Keputusan Disyorkan | Teruskan dengan Pengawal |

**⚠ Kaveat kualiti data:** Ramalan kedudukan 1 (OCD) mempunyai tatasusunan `clinical_trials` yang *kosong* walaupun label bukti L1, dan nisbah TxGNN sendiri menyatakan ini "ialah salah satu indikasi yang sudah diluluskan fluvoxamine, bukan benar-benar penggunaan baharu; medan `original_indications` yang kosong berkemungkinan jurang data." Kedudukan 6 (**gangguan kegelisahan**, L2, S2/S3, Teruskan dengan Pengawal) dan 7 (**agorafobia**, L2, S2, Teruskan dengan Pengawal) disokong oleh pelbagai ujian klinis terkawal plasebo buta-dua dan mewakili calon pengguna semula yang lebih dipercayai daripada kedudukan 1.

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia dalam bentuk berstruktur (medan DrugBank MOA: jurang data). Berdasarkan farmakologi yang mantap yang tercermin di seluruh kesusasteraan dalam pakej bukti ini, fluvoxamine ialah penghambat pemasukan semula serotonin terpilih (SSRI). Dysregulasi serotonergik ialah hipotesis patofisiologi utama untuk OCD, dan SSRI termasuk fluvoxamine adalah farmakoterapi barisan pertama yang mantap untuk OCD — ini didokumentasikan secara langsung dalam pakej (contohnya, PMID 9184625: "tunjang rawatan farmakologi OCD ialah percubaan 10 hingga 12 minggu SRI yang kuat... salah satu SRI yang paling banyak dikaji ialah fluvoxamine").

Kerana medan `original_indications` kosong dan teks indikasi lesen TFDA/NPRA tidak ditangkap, saluran paip nampaknya telah menentukan kedudukan OCD sebagai "indikasi baharu yang diramal" teratas, padahal sebenarnya asas bukti menunjukkan OCD ialah penggunaan yang sudah diluluskan jangka panjang fluvoxamine (pelbagai ujian pasca-pemasaran dan Fasa 3/4, contohnya NCT01933919, NCT02022709). Ini ialah isu kelengkapan data huluan (DG001/DG002), bukan isyarat pengguna semula, dan harus diperbetulkan sebelum calon ini digunakan untuk membenarkan tuntutan "indikasi baharu".

Isyarat yang benar-benar lebih bermaklumat dalam pakej ini ialah mekanisme serotonergik bersama yang memanjangkan keberkesanan fluvoxamine daripada OCD kepada gangguan spektrum kegelisahan yang lain — gangguan kegelisahan sosial, gangguan panik, gangguan kegelisahan umum, dan agorafobia — semuanya disokong oleh ujian klinis terkawal plasebo buta-dua fluvoxamine langsung (contohnya, PMID 8927663, PMID 7726307, PMID 9754844, PMID 16573847). Ini adalah koheren dari segi mekanisme (laluan serotonergik yang sama, klasifikasi spektrum kegelisahan DSM yang bertindan) dan ini adalah tempat kes pengguna semula yang lebih kuat wujud.

---

## Bukti Ujian Klinis

Pada masa ini tiada ujian klinis berkaitan yang didaftar (predicted_indications[0].evidence.clinical_trials kosong untuk gangguan obsesif-kompulsif; ambil perhatian bahawa pelbagai ujian fluvoxamine/OCD seperti [NCT01933919](https://clinicaltrials.gov/study/NCT01933919) dan [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) memang muncul di bawah entri ramalan "gangguan kegelisahan" dalam pakej bukti ini, mencadangkan kemungkinan ketidakkonsistenan peletak teg penyakit huluan).

---

## Bukti Kesusasteraan

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-------|------|--------|----------------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | RCT/Meta-analisis | Journal of Psychiatric Research | Meta-analisis rangkaian rawatan farmakologi vs. psikologi (sahaja dan digabung) untuk OCD kanak-kanak/remaja, termasuk SRI seperti fluvoxamine. |
| [19198698](https://pubmed.ncbi.nlm.nih.gov/19198698/) | 2008 | RCT | Drugs of Today | Tiga ujian 12 minggu buta-dua, berbilang pusat, terkawal plasebo bagi fluvoxamine pelepasan terkawal dalam OCD dan fobia sosial menunjukkan keberkesanan. |
| [9184625](https://pubmed.ncbi.nlm.nih.gov/9184625/) | 1997 | Ulasan | The Journal of Clinical Psychiatry | Ulasan komprehensif yang menetapkan keberkesanan anti-obsesif fluvoxamine daripada ujian buta-dua terkawal plasebo; salah satu SRI yang paling banyak dikaji untuk OCD. |
| [40143130](https://pubmed.ncbi.nlm.nih.gov/40143130/) | 2025 | Ulasan (gambaran keseluruhan ulasan sistemik) | Pharmaceuticals (Basel) | Mensintesis ulasan sistemik/meta-analisis mengenai keberkesanan fluvoxamine merentas GAD, gangguan kegelisahan sosial, gangguan panik, dan OCD. |
| [27318812](https://pubmed.ncbi.nlm.nih.gov/27318812/) | 2016 | Ulasan Sistemik/Meta-analisis Rangkaian | The Lancet Psychiatry | Membandingkan keberkesanan langsung dan tidak langsung semua campur tangan OCD farmakologi dan psikoterapi utama dalam satu analisis. |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Ulasan | Comprehensive Psychiatry | Keselamatan dan kebolehterimaan jangka panjang SRI dos tinggi luar label (termasuk fluvoxamine) dalam rawatan OCD. |
| [31040685](https://pubmed.ncbi.nlm.nih.gov/31040685/) | 2019 | Kajian penggalian peraturan persatuan | Neuropsychiatric Disease and Treatment | Meramalkan tindak balas rawatan fluvoxamine dalam kohort OCD Iran menggunakan penggalian peraturan persatuan; mencatat 40–60% pesakit tidak bertindak balas memadai terhadap SRI. |
| [34880926](https://pubmed.ncbi.nlm.nih.gov/34880926/) | 2021 | Analisis statistik/kohort | Clinical Practice and Epidemiology in Mental Health | Pemodelan regresi kuantil ordinal Bayesian bagi respons fluvoxamine dalam pesakit OCD. |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Ulasan bukti klinis | BMJ Clinical Evidence | Epidemiologi umum dan ringkasan pilihan rawatan untuk OCD (prevalens ~1–2.7% bergantung kepada kumpulan umur). |
| [1806635](https://pubmed.ncbi.nlm.nih.gov/1806635/) | 1991 | Ulasan | International Clinical Psychopharmacology | Ulasan naratif awal OCD sebagai sindrom neuropsikiatrik dan pendekatan rawatannya secara bersejarah. |

---

## Maklumat Pasaran Malaysia

Rekod NPRA menunjukkan **6 lesen produk berdaftar** untuk fluvoxamine (status pasaran: ✓ Dipasarkan), tetapi nombor lesen, nama produk, bentuk dos, pengeluar, dan medan teks indikasi yang diluluskan tidak diisi dalam pakej bukti ini (jurang data) — butiran label lengkap harus diambil terus daripada surat penyisipan pakej NPRA/produk sebelum data ini digunakan untuk keputusan kawal selia atau klinis.

---

## Pertimbangan Keselamatan

Sila rujuk surat penyisipan pakej untuk maklumat keselamatan. Semua medan keselamatan berstruktur dalam pakej bukti ini (amaran utama, kontraindikasi, interaksi ubat-ubat) ditandai sebagai jurang data — terutamanya, **DG001 (amaran surat penyisipan pakej TFDA/NPRA/kontraindikasi) ditandai sebagai Penyekat**, bermaksud calon ini belum dapat melengkapkan penilaian keselamatan awal S1.

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Teruskan dengan Pengawal**

**Nisbah:**
- Mekanisme serotonergik asas didukung dengan baik untuk fluvoxamine merentas spektrum gangguan OCD/kegelisahan, dan pelbagai ujian klinis langsung menyokong penggunaan dalam gangguan kegelisahan dan agorafobia (bukti L2, kedudukan 6–7).
- Walau bagaimanapun, ramalan "indikasi baharu" kedudukan 1 (OCD) nampaknya menduplikasi penggunaan yang sudah diluluskan kerana jurang data huluan (medan `original_indications` kosong), dan jurang data keselamatan Penyekat (DG001) menghalang ulasan keselamatan awal yang lengkap — pengawal, bukan Go penuh, adalah sesuai pada peringkat ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Surat penyisipan pakej PDF TFDA/NPRA (amaran, kontraindikasi, DDI) untuk menyelesaikan DG001 (Penyekat)
- Data mekanisme tindakan DrugBank untuk menyelesaikan DG002 dan memperkuat analisis pautan mekanisme
- Penyelarasan medan `original_indications` yang kosong supaya OCD diklasifikasikan dengan betul sebagai penggunaan yang sudah diluluskan dan bukannya ramalan "baharu"
- Butiran lesen yang lengkap (nama produk, bentuk dos, teks indikasi) untuk 6 pendaftaran Malaysia
- Jika mengejar pengguna semula khusus, utamakan ulasan pengesahan calon gangguan kegelisahan / agorafobia (kedudukan 6–7), yang membawa kes bukti langsung yang lebih kuat

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

