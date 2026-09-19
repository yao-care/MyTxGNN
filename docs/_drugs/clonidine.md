---
layout: default
title: Clonidine
parent: High Evidence (L1-L2)
nav_order: 232
evidence_level: L1
indication_count: 10
---

# Clonidine
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

# Klonidina: Daripada Hipertensi kepada Gangguan Kurang Perhatian/Hiperaktiviti (ADHD)

## Ringkasan Satu Ayat

Klonidina adalah agonis α2-adrenergik yang bekerja sentral, secara klasik digunakan untuk mengobati hipertensi. Model TxGNN memprediksi bahawa ia juga mungkin berkesan untuk **Gangguan Kurang Perhatian/Hiperaktiviti (ADHD)** — suatu indikasi yang sudah disokong oleh **17 percobaan klinis** (termasuk empat RCT Fase 3 yang telah selesai) dan **19 publikasi**, dan sudah diluluskan di tempat lain sebagai Kapvay/CLONICEL (klonidina pelepasan lanjutan). Keluaran model yang berkaitan rapat, "ADHD, jenis kurang perhatian," menghasilkan skor hampir sama tetapi tidak mempunyai bukti independen — ini adalah subtipe DSM bagi entiti penyakit yang sama dan harus dibaca sebagai mewarisi bukti ADHD di bawah, bukan sebagai jurang data berasingan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Hipertensi (indikasi farmakologi yang telah ditetapkan; rekod pendaftaran NPRA Malaysia wujud tetapi teks labelnya tidak ditangkap dalam pakej data ini — lihat nota dalam Pertimbangan Keselamatan) |
| Indikasi Ramalan | Gangguan Kurang Perhatian/Hiperaktiviti (ADHD) |
| Skor Ramalan TxGNN | 99.9996% (pangkat model 25; entri subtipe "jenis kurang perhatian" menghasilkan skor 99.9997%, pangkat model 22) |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan Disyorkan | Teruskan dengan Penjaga |

---

## Mengapa Ramalan Ini Munasabah?

Klonidina adalah agonis reseptor α2A-adrenergik yang bekerja sentral. Agonisme α2A mengukuhkan penghantaran isyarat korteks prefrontal dengan mengurangkan ton noradrenergik di reseptor α2A postsinaptik — ini bukan mekanisme spekulatif tetapi mekanisme sebenar di sebalik Kapvay (klonidina pelepasan lanjutan) yang diluluskan FDA, diluluskan pada 2010 sebagai monoterapi atau terapi adjunktif untuk ADHD. Dengan kata lain, ini bukan isyarat penemuan semula yang eksploratori; ia mencerminkan indikasi yang sudah ditetapkan untuk molekul yang sama di bawah jenama/formulasi yang berbeza.

Dua keluaran TxGNN berpangkat tertinggi — "attention deficit-hyperactivity disorder" dan "attention deficit hyperactivity disorder, inattentive type" — adalah entiti penyakit asas yang sama. Subtipe kurang perhatian adalah deskriptor klinis DSM-5 ADHD dan bukannya keadaan yang berbeza secara biologis, dan pelabelan klonidina ER yang diluluskan tidak membezakan mengikut subtipe. Nod subtipe kurang perhatian oleh itu tidak mempunyai bukti percobaan atau sastera independen dalam pakej ini; bukti sokongannya harus dibaca sebagai diwarisi daripada entri ADHD umum di bawah.

Anotasi mekanisme formal terperinci (cth., data berstruktur DrugBank) dibenderakan sebagai jurang data dalam pakej bukti ini. Berdasarkan rasional mekanik yang ditangkap daripada bukti itu sendiri, aktiviti agonis α2A klonidina adalah konsisten dari segi farmakologi dengan peranannya yang ditetapkan dan diluluskan FDA dalam pengurusan ADHD bersama rangsangan dan agen bukan rangsangan lain (atomoksetin, guanfasin).

---

## Bukti Percobaan Klinis

| Nombor Percobaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT00641329](https://clinicaltrials.gov/study/NCT00641329) | Fasa 3 | Selesai | 198 | CLONICEL (klonidina HCl pelepasan berkelanjutan) sebagai tambahan kepada terapi psikostimulant vs. psikostimulant sahaja pada kanak-kanak/remaja dengan ADHD |
| [NCT00031395](https://clinicaltrials.gov/study/NCT00031395) | Fasa 3 | Selesai | 122 | Percobaan CAT — kajian terkawal klasik klonidina sahaja atau digabungkan dengan metilfenil pada kanak-kanak berusia 7–12 dengan ADHD |
| [NCT00556959](https://clinicaltrials.gov/study/NCT00556959) | Fasa 3 | Selesai | 236 | Penilaian dos-tindak balas CLONICEL vs. plasebo pada kanak-kanak/remaja dengan ADHD |
| [NCT00723190](https://clinicaltrials.gov/study/NCT00723190) | Fasa 3 | Selesai | 303 | Kajian keselamatan paparan kronik 12 bulan daripada CLONICEL, sebagai monoterapi atau digabungkan dengan rangsangan |
| [NCT01439126](https://clinicaltrials.gov/study/NCT01439126) | Fasa 4 | Selesai | 135 | Kajian penarikan semula rawak yang mengesahkan keberkesanan dan keselamatan jangka panjang KAPVAY (klonidina ER) pada kanak-kanak/remaja dengan ADHD |
| [NCT07044609](https://clinicaltrials.gov/study/NCT07044609) | Fasa 4 | Belum merekrut | 162 | Percobaan terkawal plasebo klonidina ER (Onyda XR) pada kanak-kanak berusia 6–12 dengan ADHD dan gangguan oposisi yang menentang seiring |
| [NCT00414921](https://clinicaltrials.gov/study/NCT00414921) | Fasa 2 | Selesai | 30 | Kajian tambahan prasekolah (berusia 4–6) klonidina dan metilfenil, sahaja atau digabungkan, untuk ADHD |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Fasa 4 | Merekrut | 500 | Percobaan rancangan SMART pragmatik membandingkan rangsangan dan agonis alfa-2 (termasuk klonidina) untuk ADHD pada remaja dengan gangguan spektrum autisme |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Fasa 4 | Tidak diketahui | 32 | Kesan klonidina pada tidur malam dan agresi siang hari pada kanak-kanak dengan sindrom Tourette dan ADHD yang seiring |
| [NCT06910605](https://clinicaltrials.gov/study/NCT06910605) | T/A | Merekrut | 26 | Kajian simulasi pemanduan yang meneliti cuti ubat pada dewasa dengan ADHD |

---

## Bukti Kesusasteraan

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Meta-analisis Rangkaian | The Lancet Psychiatry | Keberkesanan/tolerabiliti perbandingan ubat ADHD merentasi kanak-kanak, remaja, dan dewasa |
| [37166701](https://pubmed.ncbi.nlm.nih.gov/37166701/) | 2023 | Ulasan Sistematik | CNS Drugs | Ubat bukan rangsangan (termasuk klonidina) untuk ADHD dewasa, sebagai monoterapi atau adjunktif kepada rangsangan |
| [39760346](https://pubmed.ncbi.nlm.nih.gov/39760346/) | 2025 | Ulasan Sistematik | Pediatric Annals | Ubat ADHD bukan rangsangan sebagai alternatif bagi pesakit yang tidak dapat bertoleransi atau tidak bertindak balas kepada rangsangan |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Meta-analisis Rangkaian | The Lancet Psychiatry | Keselamatan kardiovaskular perbandingan ubat ADHD — kesan hemodinamik dan ECG merentasi kanak-kanak, remaja, dewasa |
| [28391425](https://pubmed.ncbi.nlm.nih.gov/28391425/) | 2017 | Ulasan Sistematik | Paediatric Drugs | Keselamatan, tolerabiliti, dan keberkesanan ubat (termasuk klonidina) untuk insomnia tingkah laku pada kanak-kanak dengan ADHD |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Ulasan | Current Pharmaceutical Design | Psikofarmakologi ADHD — kesan dan kesan sampingan kelas ubat utama |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Ulasan | The Annals of Pharmacotherapy | Gambaran patofisiologi, etiologi, dan rawatan ADHD |
| [28700715](https://pubmed.ncbi.nlm.nih.gov/28700715/) | 2017 | Meta-analisis Rangkaian | PLoS ONE | Keberkesanan dan keselamatan intervensi farmakologi, psikologi, dan CAM untuk ADHD pada kanak-kanak/remaja |
| [38506810](https://pubmed.ncbi.nlm.nih.gov/38506810/) | 2024 | Kohort | JAMA Network Open | Persatuan antara ubat ADHD khusus dan ketidakupayaan kerja / hasil kesihatan mental |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Kohort | Psychiatry Investigation | Keberkesanan dan keselamatan tampalan pelekat klonidina dalam pesakit sindrom Tourette dengan ADHD yang seiring |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan. Data amaran, kontraindikasi, dan data interaksi ubat bersumber NPRA pakej bukti ini dibenderakan sebagai jurang data yang menghalang (belum diambil semula), oleh itu tiada pernyataan keselamatan spesifik ubat boleh dibuat daripada set data semasa — ini mesti diselesaikan sebelum prosedur prapemeriksaan keselamatan S1 dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Penjaga**

**Rasional:**
Indikasi ADHD disokong oleh bukti tahap L1 — empat RCT Fase 3 yang telah selesai ditambah percobaan penarikan semula Fasa 4 yang telah selesai — dan mencerminkan mekanisme (agonisme α2A) yang sudah diluluskan untuk penggunaan yang sama dalam pasaran lain (Kapvay/CLONICEL). Bagaimanapun, data kawal selia dan keselamatan asas calon ini (amaran label NPRA, kontraindikasi, rekod MOA formal) kini menghalang jurang, jadi penjaga diperlukan sebelum sebarang tindakan klinis atau kawal selia.

**Untuk diteruskan, yang berikut diperlukan:**
- Ambil PDF label NPRA untuk pendaftaran Malaysia ini (nombor lesen, nama produk, teks indikasi yang diluluskan, bentuk dos) — kini kosong dalam set data
- Ambil amaran sisipan paket/kontraindikasi dan data DDI (kini "[Jurang Data]" / tidak ditemui)
- Sahkan rekod mekanisme formal/DrugBank untuk dokumentasi mekanisme α2A-adrenergik
- Jelaskan ketersediaan haluan/formulasi di Malaysia terhadap formulasi pelepasan lanjutan yang digunakan dalam percobaan ADHD pangsi (pelepasan segera vs. ER mungkin tidak boleh saling ganti untuk indikasi ini)

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

