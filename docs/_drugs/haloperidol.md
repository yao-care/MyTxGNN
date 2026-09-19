---
layout: default
title: Haloperidol
parent: High Evidence (L1-L2)
nav_order: 379
evidence_level: L1
indication_count: 10
---

# Haloperidol
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

# Haloperidol: Dari Petunjuk Diluluskan Tidak Tertentu kepada Skizofrenia

## Ringkasan Satu Ayat

Haloperidol adalah ubat yang dipasarkan di Malaysia (3 pendaftaran NPRA), tetapi teks petunjuk asal yang direkodkan secara rasmi adalah jurang data pada masa ini dalam pakej bukti ini. Ramalan teratas model TxGNN adalah **Skizofrenia** (skor 99.96%), disokong oleh **50 uji klinis** dan **20 penerbitan** — namun, nota rasional model sendiri menunjukkan ini sangat mungkin pengesahan penggunaan antipsikotik piawai sedia ada Haloperidol *yang wujud* dan bukannya isyarat pemindahan tujuan yang betul-betul baru.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak direkodkan dalam data pendaftaran sumber (jurang data — lihat DG001/DG002); Haloperidol adalah antipsikotik generasi pertama yang ditetapkan secara klinikal |
| Petunjuk Baru yang Diprediksi | Skizofrenia |
| Skor Ramalan TxGNN | 99.96% |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | Teruskan dengan Penjaga |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam medan `drug.original_moa` berstruktur. Walau bagaimanapun, rasional pemindahan tujuan pakej bukti sendiri menyediakan farmakologi yang berkaitan: Haloperidol adalah antipsikotik generasi pertama (tipikal) yang mekanismenya ialah antagonisme reseptor dopamin D2 pusat — mekanisme buku teks piawai untuk merawat skizofrenia.

Dengan penting, pakej bukti secara terang-terangan menandakan bahawa ini **bukan kes ketat pemindahan tujuan ubat**: Skizofrenia adalah petunjuk jangka panjang yang ditetapkan dan diluluskan Haloperidol dalam dunia sebenar, dan medan `original_indications` yang kosong mencerminkan jurang pengekstrakan data dan bukannya ketiadaan petunjuk itu. Dengan kata lain, model TxGNN telah mengenal pasti semula penggunaan utama Haloperidol yang diketahui — yang merupakan pemeriksaan kesahihan model yang berguna, tetapi tidak boleh dibentangkan kepada pihak berkepentingan sebagai peluang pemindahan tujuan baru.

Untuk perbandingan, calon pangkat 8 pakej ("gangguan psikotik," bukti L1) menunjukkan corak yang sama — antagonisme D2 secara langsung menyokong pengurusan psikosis akut dan merupakan amalan klinikal piawai, bukan penemuan baru. Sebaliknya, pangkat 3–7, 9, dan 10 (cth., gangguan sintesis glikoprotein bawaan, distrofi retina, hidranensefalus, miopia terikat-X, penyakit Charcot-Marie-Tooth) mempunyai **tiada uji klinis, tiada literatur, dan tiada pautan mekanistik yang munasabah** — pakej bukti sendiri melabelkan ini sebagai artifak positif palsu kemungkinan besar ruang pembenaman graf pengetahuan (L5, Tahan). Hanya pangkat 2 (gangguan skizofreniafom, L3, "Soalan Penyelidikan") mewakili isyarat yang betul-betul eksploratori patut dipantau.

---

## Bukti Uji Klinis

| Nombor Uji | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT01052389](https://clinicaltrials.gov/study/NCT01052389) | Fasa 4 | Selesai | 300 | Uji GiSAS — aripiprazol, olanzapin, dan haloperidol dibandingkan selama 12 bulan pada pesakit ambulatori skizofrenia |
| [NCT00203775](https://clinicaltrials.gov/study/NCT00203775) | N/A | Ditamatkan | N/A | Risperidon lawan haloperidol untuk kekerasan/permusuhan dalam narapidana psikotik |
| [NCT00485901](https://clinicaltrials.gov/study/NCT00485901) | Fasa 3 | Selesai | 50 | Olanzapin IM lawan haloperidol IM dalam pesakit skizofrenia yang teruja secara akut |
| [NCT00455234](https://clinicaltrials.gov/study/NCT00455234) | Fasa 3 | Selesai | 300 | Olanzapin IM lawan haloperidol IM + prometazin untuk tranquilisasi cepat |
| [NCT00249119](https://clinicaltrials.gov/study/NCT00249119) | Fasa 3 | Selesai | 1579 | Risperidon lawan haloperidol tetap 10mg dalam skizofrenia kronik |
| [NCT00191555](https://clinicaltrials.gov/study/NCT00191555) | Fasa 4 | Selesai | 360 | Olanzapin jangka panjang lawan haloperidol dalam pesakit skizofrenia yang stabil |
| [NCT00866645](https://clinicaltrials.gov/study/NCT00866645) | Fasa 2/3 | Selesai | 240 | Levosulpirid IM lawan haloperidol IM untuk pengagitan dalam pesakit skizofrenia Cina |
| [NCT00631722](https://clinicaltrials.gov/study/NCT00631722) | N/A | Selesai | 80 | Ketiapin lawan haloperidol untuk gejala yang teruja dalam skizofrenia akut |
| [NCT01164059](https://clinicaltrials.gov/study/NCT01164059) | Fasa 4 | Selesai | 149 | Antipsikotik lebih baru lawan haloperidol/flupentiksol dos rendah dalam skizofrenia |
| [NCT00723606](https://clinicaltrials.gov/study/NCT00723606) | Fasa 3 | Selesai | 376 | Ziprasidone IM lawan haloperidol IM untuk pengagitan dalam skizofrenia (kajian pendaftaran China) |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [11777998](https://pubmed.ncbi.nlm.nih.gov/11777998/) | 2002 | RCT | The New England Journal of Medicine | Perbandingan jangka panjang risperidon lawan haloperidol untuk pencegahan relaps dalam gangguan skizofrenia/skizofaektif |
| [31006114](https://pubmed.ncbi.nlm.nih.gov/31006114/) | 2019 | Ulasan (Cochrane) | Cochrane Database of Systematic Reviews | Ulasan sistematik pemutusan haloperidol dalam pesakit skizofrenia stabil |
| [18254045](https://pubmed.ncbi.nlm.nih.gov/18254045/) | 2008 | Ulasan (Cochrane) | Cochrane Database of Systematic Reviews | Haloperidol lawan klorpromazin — perbandingan antipsikotik penanda aras |
| [11552769](https://pubmed.ncbi.nlm.nih.gov/11552769/) | 2001 | Analisis berkumpul | International Clinical Psychopharmacology | Analisis bersatu 12 uji buta ganda, risperidon lawan haloperidol dan antipsikotik lain |
| [15342619](https://pubmed.ncbi.nlm.nih.gov/15342619/) | 2004 | RCT | Journal of Clinical Pharmacology | Kesan haloperidol/lorazepam IM pada selang QT dalam skizofrenia |
| [27516021](https://pubmed.ncbi.nlm.nih.gov/27516021/) | 2016 | Kohort | Romanian Journal of Morphology and Embryology | Hasil klinikal/biologi rawatan haloperidol lanjutan |
| [33472389](https://pubmed.ncbi.nlm.nih.gov/33472389/) | 2021 | Kajian perbandingan | The American Journal of Psychiatry | Klozapin lawan olanzapin lawan haloperidol untuk kekerasan dalam skizofrenia dengan gangguan kondu |
| [10200746](https://pubmed.ncbi.nlm.nih.gov/10200746/) | 1999 | Kajian | The American Journal of Psychiatry | Gangguan seksual semasa rawatan klozapin lawan haloperidol |
| [35887056](https://pubmed.ncbi.nlm.nih.gov/35887056/) | 2022 | Praklinikal | International Journal of Molecular Sciences | Kesan haloperidol/olanzapin pada proliferasi sel hipokampal (model haiwan) |
| [37635268](https://pubmed.ncbi.nlm.nih.gov/37635268/) | 2023 | Praklinikal | International Journal of Developmental Neuroscience | Kesan haloperidol pada faktor neurotrofik/epigenetik dalam model skizofrenia teraruh ketamin |

---

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan 3 pendaftaran aktif (status pasaran: Dipasarkan), tetapi nombor lesen individu, nama produk, bentuk dos, dan medan teks petunjuk kelulusan tidak diisi dalam cabutan data ini — jurang pengekstrakan data, bukan ketiadaan pendaftaran. Pertanyaan semula pangkalan data produk NPRA diperlukan untuk melengkapkan jadual ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. **Nota:** amaran label TFDA/NPRA dan kontraindikasi (DG001) dan data interaksi ubat pada masa ini tidak tersedia dan ditandakan sebagai jurang data *Pemblokiran* — ini mesti diselesaikan sebelum sebarang penilaian peringkat keselamatan (S1) dapat diselesaikan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Penjaga**

**Rasional:**
Ramalan pangkat 1 (skizofrenia) disokong oleh bukti RCT Fasa 3/4 yang luas dan ulasan sistematik (L1), tetapi ini sebahagian besarnya mengesahkan penggunaan yang sudah ditetapkan Haloperidol dan bukannya mengenal pasti peluang pemindahan tujuan baru — jadi nilai praktikalnya di sini ialah sebagai pemeriksaan kesahihan model, bukan calon baru untuk memajukan. Jurang data pemblokiran (amaran label TFDA/NPRA dan kontraindikasi yang hilang) menghalang penyiapan saringan keselamatan awal untuk sebarang petunjuk, termasuk yang ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Ambil dan urai sisipan pakej TFDA/NPRA (amaran, kontraindikasi) — jurang pemblokiran DG001
- Perolehi data MOA DrugBank untuk mendokumentasikan mekanisme secara rasmi (jurang peringkat ubat semasa DG002)
- Pertanyaan semula NPRA untuk nama produk lengkap setiap lesen, bentuk dos, dan teks petunjuk kelulusan
- Jelaskan dengan kakitangan kawal selia/klinikal sama ada skizofrenia harus diperlakukan sebagai kes "pengesahan" dan bukannya calon pemindahan tujuan sebelum pelaburan lanjutan
- Pangkat 3, 5, 6, 7, 9, 10 (L5, tiada uji/literatur, tiada kebolehpercayaan mekanistik) harus diprioritaskan semula sebagai positif palsu kemungkinan; pangkat 2 (gangguan skizofreniafom, L3) mungkin wajar pemantauan ringan sahaja

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

