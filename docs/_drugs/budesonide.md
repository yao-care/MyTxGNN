---
layout: default
title: Budesonide
parent: High Evidence (L1-L2)
nav_order: 167
evidence_level: L1
indication_count: 5
---

# Budesonide
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

# Budesonide: Dari Terapi Kortikosteroid Inhalasi kepada Asma (Pengesahan Indikasi)

## Ringkasan Satu Ayat

Budesonide ialah glukokortikoid sintetik yang bertindak secara tempatan dan telah dipasarkan di Malaysia sebagai kortikosteroid inhalasi/oral. Persatuan berpangkat teratas model TxGNN menunjukkan **Asma**, namun bukti dan rasional yang disediakan menunjukkan bahawa ini adalah **indikasi teras yang sudah dilulus** untuk Budesonide daripada kandidat penggunaan semula yang benar-benar baru, disokong oleh kira-kira **50 ujian klinis** dan **20 penerbitan** dalam set data yang mendasarinya (10 teratas daripada setiap satu ditunjukkan di bawah). Kandidat ini sebaiknya dibaca sebagai **isyarat pengesahan validasi** — laporan juga menandakan tempat persatuan berpangkat lain model (IBD, asma alergik, asma intrinsik, penyakit Crohn) terletak pada spektrum kenovelaan.

## Gambaran Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak dapat diekstrak daripada data lesen NPRA semasa (kesemua 5 rekod lesen sampel mempunyai medan `approved_indication_text` kosong). Budesonide ialah glukokortikoid yang dicirikan dengan baik dipasarkan untuk indikasi pernafasan (asma) dan gastrointestinal (IBD) secara global. |
| Indikasi Baru Yang Diramalkan | Asma |
| Skor Ramalan TxGNN | 0.00% *(lihat kaveat di bawah — nilai ini kelihatan sebagai pemegang tempat data daripada skor keyakinan sebenar, kerana ia dilaporkan sebagai 0.0 walaupun berada di kedudukan #1)* |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 34 |
| Keputusan Yang Disyorkan | Teruskan dengan Syarat Keselamatan |

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci untuk Budesonide tidak tersedia dalam suapan DrugBank berstruktur (Jurang Data DG002). Berdasarkan farmakoloji yang diketahui, Budesonide ialah glukokortikoid sintetik tidak-terhalogen dengan potensi anti-radang tempatan yang tinggi dan metabolisme hepatik pelepasan pertama yang meluas, yang memberikan nisbah aktiviti tempatan-ke-sistemik yang menguntungkan. Sifat ini mendasari dua aplikasi klinis utamanya: penggunaan inhalasi/nebulasi untuk radang saluran udara (asma) dan formulasi oral atau rektal pelepasan pH/masa untuk radang gastrointestinal (penyakit Crohn, kolitis ulseratif, kolitis mikroskopik).

Untuk kandidat berpangkat teratas dalam pak bukti ini, rasional mekanistik yang disediakan secara eksplisit menyatakan: *"Budesonide ialah ICS yang kuat dan bertindak secara tempatan yang menekan penyusupan eosinofil saluran udara, edema mukosa, dan pelepasan sitokin melalui reseptor glukokortikoid — ini adalah mekanisme anti-radang bersama untuk asma. Ini adalah indikasi teras Budesonide yang sudah dilulus, bukan kandidat ramalan baru; pautan mekanistik adalah langsung dan telah disahkan secara klinis."* Dalam erti kata lain, keluaran TxGNN tertentu ini mengesahkan penggunaan yang telah ditetapkan daripada membuka hipotesis terapeutik baru — badan bukti Fasa 3 yang besar di bawah mencerminkan puluhan tahun penyelidikan indikasi yang dilulus, bukan data penggunaan semula eksploratori.

Untuk konteks, persatuan berpangkat lain pak bukti yang sama berbeza-beza dalam kenovelaan: penyakit usus radang (kedudukan 2) dan penyakit Crohn (kedudukan 5) juga merupakan penggunaan yang sudah dilulus bagi formulasi pelepasan ileum Budesonide (Entocort EC); asma alergik (kedudukan 3) bertindih dengan besar kepada indikasi asma yang dilulus; hanya asma intrinsik (bukan alergik) (kedudukan 4) mencerminkan soalan fenotip khusus yang benar-benar kurang dikaji, disokong terutamanya oleh literatur yang lebih lama dan berskala kecil (tahap bukti L3, peringkat keputusan "Soalan Penyelidikan"). Perbezaan ini penting untuk memprioritaskan sebarang kerja susulan.

## Bukti Ujian Klinis

| Nombor Ujian | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Fasa 3 | Selesai | 1,600 | Symbicort (budesonide/formoterol) rejim SMART vs. rawatan amalan terbaik konvensional untuk asma berterusan selama 26 minggu |
| [NCT05202262](https://clinicaltrials.gov/study/NCT05202262) | Fasa 3 | Selesai | 645 | VATHOS: ujian 24 minggu budesonide/formoterol MDI vs. MDI budesonide dan Symbicort Turbuhaler berlabel terbuka dalam asma yang tidak tersusun dengan baik |
| [NCT00509028](https://clinicaltrials.gov/study/NCT00509028) | Fasa 3 | Selesai | 241 | Keselamatan/keberkesanan jangka panjang (48 minggu) budesonide Turbuhaler dalam kanak-kanak Jepun dengan asma bronkial |
| [NCT00646529](https://clinicaltrials.gov/study/NCT00646529) | Fasa 3 | Selesai | 175 | SAPLING: perbandingan keselamatan 6 bulan Symbicort vs. Pulmicort Turbuhaler dalam kanak-kanak asmatik berusia 6–11 |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Fasa 3 | Selesai | 2,091 | Ujian pelbagai negara 12 bulan membandingkan Symbicort SMART vs. Symbicort + terbutaline mengikut keperluan dalam pesakit ≥16 tahun |
| [NCT04609904](https://clinicaltrials.gov/study/NCT04609904) | Fasa 3 | Selesai | 2,187 | Keberkesanan/keselamatan budesonide/glicopirroniun/formoterol vs. Symbicort dalam orang dewasa/remaja dengan asma yang sangat tidak tersusun dengan baik |
| [NCT00646594](https://clinicaltrials.gov/study/NCT00646594) | Fasa 3 | Selesai | 1,200 | Perbandingan 7 bulan Symbicort pMDI (tetap/dapat disesuaikan) vs. Advair dalam subjek ≥12 tahun dengan asma |
| [NCT00252824](https://clinicaltrials.gov/study/NCT00252824) | Fasa 3 | Selesai | 1,000 | Perbandingan 26 minggu terapi inhalasi tunggal Symbicort vs. rawatan bertingkat konvensional dalam remaja/orang dewasa dengan asma berterusan |
| [NCT01803555](https://clinicaltrials.gov/study/NCT01803555) | Fasa 3 | Selesai | 605 | Keberkesanan/keselamatan 12 minggu budesonide/formoterol Spiromax vs. Symbicort Turbohaler dalam asma berterusan |
| [NCT01360021](https://clinicaltrials.gov/study/NCT01360021) | Fasa 3 | Selesai | 214 | Perbandingan 12 minggu Symbicort MDI yang diaktifkan nafas vs. formulasi pMDI bertekan dalam astmatik dewasa/remaja |

*Nota: set data yang mendasarinya mengandungi ~50 ujian yang berkaitan dengan asma secara keseluruhan; 10 di atas diprioritaskan untuk relevansi berpangkat ("A"), status Fasa 3 yang selesai, dan saiz pendaftaran.*

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | Budesonide-formoterol inhalasi mengikut keperluan sebagai alternatif kepada strategi penyelenggaraan konvensional dalam asma ringan |
| [37003355](https://pubmed.ncbi.nlm.nih.gov/37003355/) | 2023 | RCT | Chest | Ujian DENALI: pMDI albuterol-budesonide dalam asma ringan hingga sederhana, mengesahkan sumbangan setiap komponen kepada keberkesanan |
| [11687183](https://pubmed.ncbi.nlm.nih.gov/11687183/) | 2001 | Ulasan Cochrane/Meta-analisis | Cochrane Database Syst Rev | Ulasan sistematik budesonide inhalasi untuk asma kronik dalam kanak-kanak dan orang dewasa |
| [32237004](https://pubmed.ncbi.nlm.nih.gov/32237004/) | 2020 | Ulasan | Respirology | Sintesis data kawalan asma daripada ujian penyelenggaraan-dan-pelepas budesonide/formoterol |
| [38527278](https://pubmed.ncbi.nlm.nih.gov/38527278/) | 2024 | Konsensus Pakar/Ulasan | J Asthma | Konsensus pakar Thailand tentang penggunaan budesonide nebulasi untuk asma dan KOPD, peringkat stabil dan eksaserbasi |
| [16162021](https://pubmed.ncbi.nlm.nih.gov/16162021/) | 2005 | Ulasan | Drugs | Ulasan suspens inhalasi budesonide untuk rawatan asma dalam bayi dan kanak-kanak |
| [38889078](https://pubmed.ncbi.nlm.nih.gov/38889078/) | 2024 | Meta-analisis | J Asthma | Meta-analisis kesan inhalasi budesonide terhembus pada gejala pernafasan dan penanda radang dalam asma |
| [27381656](https://pubmed.ncbi.nlm.nih.gov/27381656/) | 2016 | Ulasan Mekanistik | Pulm Pharmacol Ther | Mekanisme molekul dan selular yang mendasari kesan terapeutik budesonide dalam asma |
| [17983258](https://pubmed.ncbi.nlm.nih.gov/17983258/) | 2007 | Ulasan | Drugs | Ulasan budesonide/formoterol sebagai terapi inhalasi penyelenggaraan-dan-pelepas gabungan dalam asma |
| [19032229](https://pubmed.ncbi.nlm.nih.gov/19032229/) | 2008 | Ulasan | Allergy | Ulasan terapi penyelenggaraan-dan-pelepas budesonide/formoterol dalam asma sederhana hingga teruk mengikut garis panduan GINA |

*Nota: set data yang mendasarinya mengandungi 20 penerbitan yang berkaitan dengan asma secara keseluruhan; 10 di atas diprioritaskan sebagai RCT dan meta-analisis terlebih dahulu, kemudian ulasan mengikut ketermukaan dan relevansi.*

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan bahawa Budesonide **dipasarkan di Malaysia dengan 34 lesen jumlah**, namun medan peringkat lesen yang dikembalikan dalam pertanyaan semasa (nombor lesen, nama produk, bentuk dos, pengilang, teks indikasi yang dilulus) semuanya kosong untuk 5 rekod sampel. Tiada jadual kebenaran yang boleh digunakan boleh dibentangkan daripada set data ini pada masa ini. Pertanyaan semula ke daftar produk NPRA (atau pencarian terus pada pangkalan data NPRA QUEST) diperlukan untuk mengisi nombor kebenaran, nama produk/jenama, bentuk dos, dan teks indikasi label sebelum bahagian ini boleh diselesaikan.

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

*(Data amaran utama, kontraindikasi, dan interaksi ubat dicari tetapi tidak mengembalikan hasil yang boleh digunakan — status pertanyaan DDI: tidak ditemui, 0 interaksi dalam fail. Ini ditandakan sebagai jurang data bloking (DG001) untuk penilaian keselamatan penuh; lihat Kesimpulan di bawah.)*

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Syarat Keselamatan**

**Rasional:**
Asas ujian klinis dan literatur untuk Budesonide dalam asma adalah luas dan matang (tahap bukti L1, pelbagai RCT Fasa 3 yang selesai), namun ini mencerminkan pengesahan indikasi yang sudah dilulus daripada peluang penggunaan semula yang baru — rasional mekanistik yang disediakan sendiri menyatakan bahawa ini bukan kandidat ramalan baru. Penetapan "syarat keselamatan" oleh itu didorong kurang oleh ketidakpastian keberkesanan dan lebih banyak oleh dua jurang data Bloking/Keterukan Tinggi yang menghalang tanda-tangan keselamatan dan peraturan yang lengkap: amaran label NPRA yang hilang/kontraindikasi (DG001, Bloking) dan data mekanisme tindakan berstruktur yang hilang (DG002, Prioriti Tinggi).

**Untuk teruskan, yang berikut diperlukan:**
- Sisipan pakej TFDA/NPRA (amaran, berjaga-jaga, kontraindikasi) — diperlukan sebelum pemeriksaan keselamatan Peringkat 1 boleh diselesaikan (Bloking)
- Data mekanisme tindakan berstruktur melalui pertanyaan API DrugBank (Prioriti Tinggi)
- Butiran peringkat lesen NPRA yang lengkap (nombor kebenaran, nama produk, bentuk dos, teks indikasi yang dilulus) untuk 34 produk berdaftar — ekstrak semasa mengembalikan medan kosong
- Penjelasan medan skor TxGNN, yang membaca 0.00% walaupun berada di kedudukan #1-berpangkat — kemungkinan artifak saluran/eksport daripada nilai keyakinan sebenar
- Jika penyelidikan penggunaan semula selanjutnya diingini, utamakan fenotip asma intrinsik (bukan alergik) (kedudukan 4, tahap bukti L3, peringkat keputusan "Soalan Penyelidikan") sebagai kandidat yang lebih benar-benar eksploratori dalam set ini, daripada persatuan asma/IBD/penyakit Crohn yang sudah dilulus

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

