---
layout: default
title: Rituximab
parent: Low Evidence (L4-L5)
nav_order: 599
evidence_level: L5
indication_count: 5
---

# Rituximab
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

# Rituximab: Daripada Keganasan Sel B CD20+ kepada Lima Indikasi Terjangka TxGNN (Satu Benar-benar Novel)

## Ringkasan Satu Ayat

Rituximab ialah antibodi monoklonal anti-CD20 kimaera yang asalnya digunakan untuk merawat keganasan sel B positif CD20. TxGNN mengembalikan lima indikasi terjangka untuk calon ini, tetapi empat daripadanya (limfoma bukan-Hodgkin, artritis reumatoid, limfoma sel mantel, dan "neoplasma sel B" secara keseluruhannya) adalah **penggunaan rituximab yang telah diluluskan secara global** — model ini sedang mengulang label yang diketahui daripada mencadangkan sesuatu yang baru — sementara hanya **Histiositosis Sel Langerhans (LCH)** mewakili calon pengguna semula yang benar-benar novel, dan ia kini disokong hanya oleh segelintir laporan kes (tiada percubaan klinikal yang khusus).

## Gambaran Pantas

| Pangkat | Indikasi Terjangka | Skor TxGNN | Tahap Bukti | Tahap Keputusan | Cadangan | Status berbanding Rituximab |
|--------|----------------------|------------|-------------|-----------------|----------|------------------------|
| 1 | Limfoma Bukan-Hodgkin (keluarga) | 0.00%* | L1 | S3 | Teruskan dengan Pengawal | Indikasi yang telah diluluskan (pengesahan model) |
| 2 | Artritis Reumatoid | 0.00%* | L1 | S3 | Teruskan dengan Pengawal | Indikasi yang telah diluluskan (pengesahan model) |
| 3 | Limfoma Sel Mantel | 0.00%* | L1 | S3 | Teruskan dengan Pengawal | Indikasi yang telah diluluskan (pengesahan model) |
| 4 | Neoplasma Sel B (umum) | 0.00%* | L1 | S3 | Teruskan dengan Pengawal | Kategori payung meliputi pelbagai penggunaan yang telah diluluskan |
| 5 | Histiositosis Sel Langerhans | 0.00%* | L4 | S1 | Soalan Penyelidikan | **Calon pengguna semula yang benar-benar novel** — bukti lemah |

\* Semua lima nilai `txgnn.score` dalam pak bukti adalah 0.0 — ini kelihatan seperti medan yang tidak diisi/tempat letak semula daripada skor keyakinan yang bermakna, dan harus diperlakukan sebagai jurang kualiti data dalam saluran ramalan daripada sebagai "tiada isyarat."

| Item | Kandungan |
|------|--------|
| Indikasi Asal | Limfoma Bukan-Hodgkin Sel B CD20-positif (indikasi asal yang ditubuhkan secara global; medan `drug.original_indications` dan lesen Malaysia `approved_indication_text` dalam pak bukti adalah kosong, jadi ini tidak disahkan terhadap teks label tempatan) |
| Status Pasaran Malaysia | Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 9 |

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pak bukti ini (`original_moa: [Data Gap]`, ditandai sebagai jurang data DG002/Keterukan tinggi). Berdasarkan maklumat umum yang ditubuhkan dengan baik, rituximab ialah antibodi monoklonal anti-CD20 kimaera murni/manusia yang mengikat CD20 pada permukaan limfosit B dan menghapuskan mereka melalui sitotoksisiti bergantung pelengkap, sitotoksisiti bergantung sel, dan apoptosis langsung. Kesan mujabarnya dalam keganasan sel B positif CD20 terbukti dengan baik, dan mekanisme pengurangan sel B yang sama boleh digunakan secara mekanik untuk keadaan autoimun yang didorong oleh aktiviti sel B/autobadi yang patogenik.

**Indikasi 1–4 (NHL, RA, MCL, neoplasma sel B)** bukan ramalan novel — ia adalah indikasi yang mana rituximab sudah memegang kelulusan kawal selia secara antarabangsa (NHL/CLL/MCL sejak akhir 1990-an–2000-an; RA dalam kombinasi dengan metotreksat sejak 2006). Medan `repurposing_rationale.mechanistic_link` pak bukti sendiri secara eksplisit menandai ini untuk setiap satu daripada empat entri ini, menerangkan mereka sebagai model "mengulang label yang diketahui" daripada mencadangkan sesuatu yang baru. Ini berguna sebagai **bukti pengesahan model** (TxGNN dengan betul memulihkan pasangan ubat–penyakit yang diketahui) tetapi tidak boleh diskor sebagai peluang pengguna semula.

**Indikasi 5 (Histiositosis Sel Langerhans)** adalah calon novel yang benar-benar. LCH ialah proliferasi klonal sel mieloid dendriti/histiositik daripada keganasan sel B, jadi CD20 bukan sasaran terapi utama dalam lesi itu sendiri — pautan mekanik adalah tidak langsung, terduga untuk bertindak melalui pengurangan penghimpunan sel B/limfoid yang reaktif di sekitar lesi atau melalui kesan pada komplikasi yang berkaitan LCH/seperti autoimun yang merosot saraf. Ini ditunjukkan dalam tahap bukti yang lebih rendah (L4) dan tahap keputusan (S1, "Soalan Penyelidikan").

## Bukti Percubaan Klinikal

### Indikasi 1: Limfoma Bukan-Hodgkin (keluarga)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Fasa 3 | Aktif, tidak merekrut | 650 | B-NHL 2013: protokol piawai NHL-BFM/NOPHO menilai peranan rituximab dalam limfoma/leukemia sel B agresif matang NHL dalam kanak-kanak dan remaja |
| [NCT06230224](https://clinicaltrials.gov/study/NCT06230224) | Fasa 3 | Merekrut | 216 | OLYMPIA-4: odronextamab vs. penjagaan piawai yang mengandungi rituximab dalam limfoma B agresif yang dikembalikan/tahan sebarang rawatan |
| [NCT04680052](https://clinicaltrials.gov/study/NCT04680052) | Fasa 3 | Aktif, tidak merekrut | 654 | Tafasitamab + lenalidomida + rituximab vs. lenalidomida + rituximab dalam limfoma folikular/zon marginal R/R |
| [NCT05171647](https://clinicaltrials.gov/study/NCT05171647) | Fasa 3 | Aktif, tidak merekrut | 208 | Mosunetuzumab + polatuzumab vs. rituximab + gemitabin/oksaliplatin (R-GemOx) dalam limfoma B agresif R/R |
| [NCT03570892](https://clinicaltrials.gov/study/NCT03570892) | Fasa 3 | Aktif, tidak merekrut | 331 | BELINDA: tisagenlecleucel vs. penjagaan piawai (selepas kegagalan rituximab/antrasiklin) dalam limfoma B agresif R/R |
| [NCT02285062](https://clinicaltrials.gov/study/NCT02285062) | Fasa 3 | Selesai | 570 | Lenalidomida + R-CHOP (R2-CHOP) vs. plasebo + R-CHOP dalam DLBCL jenis ABC yang tidak dirawat |
| [NCT01200589](https://clinicaltrials.gov/study/NCT01200589) | Fasa 3 | Dihentikan | 438 | Ofatumumab vs. monoterapi rituximab dalam limfoma B indolen yang dikembalikan selepas terapi yang mengandungi rituximab |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Fasa 3 | Aktif, tidak merekrut | 510 | Zanubrutinib + rituximab vs. bendamustina + rituximab dalam limfoma sel mantel yang tidak dirawat (tidak layak untuk transplantasi) |
| [NCT04745832](https://clinicaltrials.gov/study/NCT04745832) | Fasa 3 | Dihentikan | 82 | COASTAL: zandelisib + rituximab vs. imunokhemioterapi piawai dalam NHL indolen yang dikembalikan |
| [NCT00072449](https://clinicaltrials.gov/study/NCT00072449) | Fasa 2 | Dihentikan | 12 | Monoterapi rituximab untuk limfoma CNS primer yang tahan/dikembalikan |

### Indikasi 2: Artritis Reumatoid

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT00422383](https://clinicaltrials.gov/study/NCT00422383) | Fasa 3 | Selesai | 378 | Kajian dwi-buta rawak bagi rejim rawatan semula MabThera + metotreksat dalam RA dengan respons inadekuat kepada MTX |
| [NCT00299104](https://clinicaltrials.gov/study/NCT00299104) | Fasa 3 | Selesai | 755 | Rituximab + MTX vs. MTX sahaja dalam RA aktif yang tidak pernah dirawat dengan MTX (kajian pendaftaran antarabangsa) |
| [NCT00443651](https://clinicaltrials.gov/study/NCT00443651) | Fasa 3 | Selesai | 578 | Kajian keselamatan atas label terbuka rituximab + ubat DMARD lain dalam RA aktif dengan respons DMARD yang inadekuat |
| [NCT01272908](https://clinicaltrials.gov/study/NCT01272908) | Fasa 3 | Selesai | 120 | RESET: keselamatan/keberkesanan rituximab dalam RA selepas respons inadekuat kepada satu agen penghambat TNF terdahulu |
| [NCT00299130](https://clinicaltrials.gov/study/NCT00299130) | Fasa 3 | Selesai | 511 | Kajian kawalan plasebo rituximab + MTX vs. monoterapi MTX dalam RA aktif |
| [NCT01332994](https://clinicaltrials.gov/study/NCT01332994) | Fasa 3 | Selesai | 519 | MIRAI: toksilizumab berurutan kemudian rituximab dalam RA yang tidak membalas DMARD |
| [NCT01382940](https://clinicaltrials.gov/study/NCT01382940) | Fasa 4 | Selesai | 351 | Keselamatan kadar infusi rituximab yang lebih cepat dalam RA sederhana hingga teruk |
| [NCT03853746](https://clinicaltrials.gov/study/NCT03853746) | Fasa 4 | Selesai | 10 | Pengurangan sel B jangka pendek dan aktiviti penyakit jangka panjang/toleransi imun (juga dikaji dalam MS) |
| [NCT01640548](https://clinicaltrials.gov/study/NCT01640548) | N/A | Selesai | 320 | Ulasan carta retrospektif bagi monoterapi biologi (termasuk rituximab) dalam RA |
| [NCT01557348](https://clinicaltrials.gov/study/NCT01557348) | N/A | Selesai | 1239 | Kajian pemerhatian global rituximab/penghambat TNF alternatif dalam bukan responden RA kepada satu penghambat TNF |

### Indikasi 3: Limfoma Sel Mantel

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT04566887](https://clinicaltrials.gov/study/NCT04566887) | Fasa 2 | Merekrut | 105 | Akalabrutin + R-CHOP dalam limfoma sel mantel yang tidak pernah dirawat sebelum transplantasi autolog |
| [NCT05245656](https://clinicaltrials.gov/study/NCT05245656) | Fasa 2 | Merekrut | 90 | Perbandingan rawak rituximab/bendamustina (RB) bergantian dengan RB/sitarabin (RBAC) vs. RB sahaja dalam limfoma sel mantel tidak layak transplantasi yang lebih tua |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Fasa 3 | Merekrut | 182 | Monoterapi glofitamab vs. pilihan penyiasat (rituximab + bendamustina, atau lenalidomida + rituximab) dalam limfoma sel mantel R/R |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Fasa 3 | Aktif, tidak merekrut | 510 | Zanubrutinib + rituximab vs. bendamustina + rituximab dalam limfoma sel mantel tidak dirawat, tidak layak transplantasi |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Fasa 2 | Selesai | 141 | Penambahan venetoclax kepada rituximab/bendamustina/sitarabin (V-RBAC) dalam limfoma sel mantel berisiko tinggi yang lebih tua |
| [NCT04849715](https://clinicaltrials.gov/study/NCT04849715) | Fasa 3 | Ditarik balik | 0 | Parsaclisib + bendamustina/rituximab vs. plasebo + BR sebagai terapi baris pertama limfoma sel mantel |
| [NCT06482684](https://clinicaltrials.gov/study/NCT06482684) | Fasa 2 | Merekrut | 150 | Rituximab + ibrutinib induksi diikuti penyatuan CAR-T vs. penjagaan piawai dalam limfoma sel mantel berisiko tinggi |
| [NCT00376961](https://clinicaltrials.gov/study/NCT00376961) | Fasa 2 | Selesai | 68 | Induksi R-CHOP + bortezomib diikuti pemeliharaan bortezomib dalam limfoma sel mantel yang baru didiagnosis |
| [NCT00114738](https://clinicaltrials.gov/study/NCT00114738) | Fasa 2 | Selesai | 53 | Induksi EPOCH-rituximab-bortezomib dengan pemeliharaan bortezomib vs. pemerhatian dalam limfoma sel mantel yang tidak dirawat |
| [NCT01389427](https://clinicaltrials.gov/study/NCT01389427) | Fasa 1/2 | Selesai | 41 | Temsirolimus + rejimen berbasis rituximab (R-CHOP/R-FC/R-DHA) dalam limfoma sel mantel yang dikembalikan/tahan |

### Indikasi 4: Neoplasma Sel B (umum)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT02005471](https://clinicaltrials.gov/study/NCT02005471) | Fasa 3 | Selesai | 389 | Venetoclax + rituximab vs. bendamustina + rituximab dalam CLL yang dikembalikan/tahan (percubaan pendaftaran utama) |
| [NCT01808599](https://clinicaltrials.gov/study/NCT01808599) | Fasa 2 | Aktif, tidak merekrut | 112 | Klorambuil + rituximab subkutan, kemudian pemeliharaan rituximab, dalam limfoma MALT |
| [NCT03391466](https://clinicaltrials.gov/study/NCT03391466) | Fasa 3 | Selesai | 359 | ZUMA-7: aksikabajen silolusol vs. penjagaan piawai (berbasis rituximab) dalam DLBCL R/R |
| [NCT04361279](https://clinicaltrials.gov/study/NCT04361279) | Fasa 3 | Selesai | 421 | Biosimilar rituximab (SIBP-02) + CHOP vs. rituximab + CHOP dalam DLBCL CD20+ yang tidak dirawat |
| [NCT00312845](https://clinicaltrials.gov/study/NCT00312845) | Fasa 3 | Selesai | 676 | Bortezomib + rituximab vs. rituximab sahaja dalam limfoma B indolen yang dikembalikan/tahan |
| [NCT04212013](https://clinicaltrials.gov/study/NCT04212013) | Fasa 3 | Aktif, tidak merekrut | 23 | Ibrutinib + rituximab vs. plasebo + rituximab dalam limfoma zon marginal yang tidak pernah dirawat |
| [NCT03777085](https://clinicaltrials.gov/study/NCT03777085) | Fasa 3 | Tidak diketahui | 230 | TQB2303 + CHOP vs. rituximab + CHOP dalam DLBCL CD20+ yang tidak dirawat |
| [NCT04623541](https://clinicaltrials.gov/study/NCT04623541) | Fasa 1/2 | Aktif, tidak merekrut | 195 | Epcoritamab (± venetoclax/pirtobrutinib) dalam CLL dan sindrom Richter yang R/R |
| [NCT02158091](https://clinicaltrials.gov/study/NCT02158091) | Fasa 1/2 | Aktif, tidak merekrut | 32 | IPI-145 + fludarabin/siklofosfamida/rituximab (FCR) dalam CLL muda yang tidak dirawat |
| [NCT04980859](https://clinicaltrials.gov/study/NCT04980859) | Fasa 3 | Tidak diketahui | 45 | Zanubrutinib + imunokhemioterapi kursus terbatas dalam CLL yang baru dirawat tanpa 17p- |

### Indikasi 5: Histiositosis Sel Langerhans

Liputan percubaan adalah jarang dan sebahagian besar luar sasaran — tiada satu daripada empat percubaan yang dikembalikan ialah percubaan rituximab-dalam-LCH yang berdedikasi:

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama / Kaveat Perkaitan |
|---------|------|------|------|---------|
| [NCT07270835](https://clinicaltrials.gov/study/NCT07270835) | Fasa 4 | Merekrut | 40 | Zanubrutinib + rituximab untuk **limfositosis hemofagositik sekunder (HLH) dalam limfoma sel B** — ketangential kepada LCH itu sendiri (HLH boleh berlaku sebagai komplikasi LCH, tetapi populasi percubaan ini ialah limfoma sel B, bukan LCH) |
| [NCT01818908](https://clinicaltrials.gov/study/NCT01818908) | Fasa 2 | Tidak diketahui | 50 | DA-EPOCH untuk HLH yang berkaitan NHL — dinilai "C" (perkaitan rendah), populasi adalah NHL, bukan LCH |
| [NCT03096782](https://clinicaltrials.gov/study/NCT03096782) | Fasa 2 | Selesai | 6 | Kejuruteraan pemindahan darah umbilikus untuk leukemia/limfoma — dinilai "C", tidak berkaitan dengan soalan rituximab-LCH |
| [NCT01471067](https://clinicaltrials.gov/study/NCT01471067) | Fasa 1 | Selesai | 33 | Fukosylation darah umbilikus untuk keganasan hematologi — tidak berkaitan dengan LCH |

**Tiada percubaan dalam pak bukti ini secara langsung menguji rituximab dalam LCH.**

## Bukti Kesusasteraan

### Indikasi 1: Limfoma Bukan-Hodgkin (keluarga)

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [27345636](https://pubmed.ncbi.nlm.nih.gov/27345636/) | 2016 | RCT (Tahap 1) | Lancet Oncology | GADOLIN: obinutuzumab + bendamustina vs. bendamustina sahaja dalam limfoma indolen yang tahan rituximab |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Ulasan (Tahap 1) | Advances in Therapy | Pengalaman klinikal 20 tahun ulasan rituximab merentasi keganasan hematologi sel B |
| [38010876](https://pubmed.ncbi.nlm.nih.gov/38010876/) | 2023 | Ulasan Sistematik (Tahap 1) | Hematology | Meta-analisis keberkesanan/keselamatan rituximab subkutan dalam NHL |
| [39234863](https://pubmed.ncbi.nlm.nih.gov/39234863/) | 2025 | RCT (Tahap 2) | Haematologica | Pengalaman nyata dengan rituximab + lenalidomida dalam limfoma indolen yang dikembalikan/tahan |
| [32135128](https://pubmed.ncbi.nlm.nih.gov/32135128/) | 2020 | Ulasan Sistematik | Lancet Haematology | Peristiwa buruk kardiovaskular dengan CHOP vs. R-CHOP dalam NHL — meta-analisis |
| [25499449](https://pubmed.ncbi.nlm.nih.gov/25499449/) | 2015 | Ulasan | Blood | Limfoma folikular yang berubah — sejarah semula jadi dan hasil |
| [37860948](https://pubmed.ncbi.nlm.nih.gov/37860948/) | 2024 | Retrospektif | J Chemotherapy | Ciri-ciri/peramal tindak balas yang berkaitan infusi kepada rituximab dalam B-NHL |
| [21958083](https://pubmed.ncbi.nlm.nih.gov/21958083/) | 2012 | Ulasan | Leukemia & Lymphoma | Pemeliharaan rituximab dalam limfoma folikular — fakta dan kontroversi |
| [32303486](https://pubmed.ncbi.nlm.nih.gov/32303486/) | 2020 | Ulasan | Clin Lymphoma Myeloma Leuk | Pengurusan peristiwa buruk daripada rituximab + lenalidomida dalam limfoma indolen/darjah rendah NHL |
| [40749164](https://pubmed.ncbi.nlm.nih.gov/40749164/) | 2025 | Praklinik | Blood | Kombinasi glofitamab (CD20×CD3 T-sel engager) — model NHL praklinik |

### Indikasi 2: Artritis Reumatoid

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [31099191](https://pubmed.ncbi.nlm.nih.gov/31099191/) | 2019 | Ulasan Sistematik (Tahap 1) | Int J Rheum Dis | Risiko jangkitan rituximab vs. rawatan bukan-rituximab dalam RA |
| [41004196](https://pubmed.ncbi.nlm.nih.gov/41004196/) | 2025 | Ulasan Sistematik (Tahap 1) | Expert Opin Biol Ther | Keberkesanan/keselamatan rituximab dalam penyakit paru antara yang berkaitan RA |
| [31446557](https://pubmed.ncbi.nlm.nih.gov/31446557/) | 2019 | Ulasan Sistematik/Meta-analisis (Tahap 1) | BioDrugs | Keberkesanan/keselamatan komparatif biosimilar vs. rituximab asal dalam RA dan NHL |
| [19758217](https://pubmed.ncbi.nlm.nih.gov/19758217/) | 2009 | Kohort (Tahap 2) | Ann NY Acad Sci | Kesan klinikal, biologi, dan farmakogenetik jangka panjang rituximab dalam RA |
| [33638167](https://pubmed.ncbi.nlm.nih.gov/33638167/) | 2021 | Kajian Farmakokinetik | Fundam Clin Pharmacol | Kebolehubahan kepekatan palung rituximab dan toksilizumab dalam RA |
| [16920570](https://pubmed.ncbi.nlm.nih.gov/16920570/) | 2006 | Ulasan | Autoimmunity Reviews | Rawatan RA dengan rituximab — kemas kini awal dan indikasi kemungkinan |
| [17896839](https://pubmed.ncbi.nlm.nih.gov/17896839/) | 2007 | Ulasan | BioDrugs | Rituximab dalam RA — ringkasan percubaan kawalan plasebo utama |
| [26692536](https://pubmed.ncbi.nlm.nih.gov/26692536/) | 2016 | Meta-analisis Rangkaian | Int J Rheum Dis | NMA Bayesian membandingkan toksilizumab, rituximab, abatacept, tofacitinib dalam RA yang tidak membalas TNF |
| [21925447](https://pubmed.ncbi.nlm.nih.gov/21925447/) | 2011 | Ulasan Sistematik | Reumatologia Clinica | Ulasan sistematik keberkesanan dan keselamatan rituximab dalam RA |
| [38693680](https://pubmed.ncbi.nlm.nih.gov/38693680/) | 2024 | Kajian | Musculoskeletal Care | Persepsi pesakit/rheumatologi pada pengurangan dos rituximab dalam RA |

### Indikasi 3: Limfoma Sel Mantel

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [38669626](https://pubmed.ncbi.nlm.nih.gov/38669626/) | 2024 | RCT (Tahap 1) | Blood | LyMa-101: obinutuzumab vs. rituximab dalam limfoma sel mantel yang layak transplantasi, hasil jangka panjang |
| [30348538](https://pubmed.ncbi.nlm.nih.gov/30348538/) | 2018 | RCT Fasa 3 (Tahap 1) | Lancet Oncology | VR-CAP vs. R-CHOP dalam limfoma sel mantel yang tidak dirawat, tidak layak transplantasi — hasil OS terakhir |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | RCT (Tahap 1) | Lancet | ENRICH: ibrutinib + rituximab vs. imunokhemioterapi piawai dalam limfoma sel mantel yang tidak dirawat (usia 60+) |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | RCT Fasa 3 (Tahap 1) | Future Oncology | Zanubrutinib + rituximab vs. bendamustina + rituximab dalam limfoma sel mantel yang tidak layak transplantasi |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Analisis Terkumpul | Blood Advances | Induksi rituximab/bendamustina dan rituximab/sitarabin untuk limfoma sel mantel yang layak transplantasi |
| [36469833](https://pubmed.ncbi.nlm.nih.gov/36469833/) | 2023 | Susulan RCT jangka panjang | J Clin Oncol | Percubaan Rangkaian Limfoma Sel Mantel Eropah — sitarabin dos tinggi + ASCT, susulan jangka panjang |
| [30033656](https://pubmed.ncbi.nlm.nih.gov/30033656/) | 2018 | Ulasan Sistematik/Meta-analisis | Am J Hematol | Terapi pemeliharaan rituximab untuk limfoma sel mantel — ulasan sistematik dan meta-analisis |
| [39023870](https://pubmed.ncbi.nlm.nih.gov/39023870/) | 2024 | Ulasan | Blood | "Adakah rituximab retro dalam limfoma sel mantel?" — perspektif pada standard of care yang berkembang |
| [38678093](https://pubmed.ncbi.nlm.nih.gov/38678093/) | 2024 | RCT Fasa 3 | Leukemia | Penambahan bortezomib kepada rituximab/sitarabin/deksametason dalam limfoma sel mantel R/R |
| [28988912](https://pubmed.ncbi.nlm.nih.gov/28988912/) | 2017 | Ulasan | Lancet Oncology | Pemeliharaan rituximab dalam limfoma sel mantel |

### Indikasi 4: Neoplasma Sel B (umum)

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [20647199](https://pubmed.ncbi.nlm.nih.gov/20647199/) | 2010 | RCT (Tahap 1) | NEJM | Percubaan RAVE: rituximab vs. siklofosfamida untuk vaskulitis yang berkaitan ANCA |
| [33661537](https://pubmed.ncbi.nlm.nih.gov/33661537/) | 2021 | Ulasan (Tahap 1) | Am J Hematol | Kemas kini 2021 tentang DLBCL — stratifikasi risiko dan pengurusan, R-CHOP sebagai tonggak |
| [32482755](https://pubmed.ncbi.nlm.nih.gov/32482755/) | 2020 | Ulasan (Tahap 2, mekanik) | Haematologica | Peraturan dan fungsi CD20 — biologi yang mendasari terapi anti-CD20 |
| [32933335](https://pubmed.ncbi.nlm.nih.gov/32933335/) | 2021 | Ulasan | Expert Opin Biol Ther | Rawatan anti-CD20 untuk keganasan sel B — status semasa dan arah hadapan masa depan |
| [28983819](https://pubmed.ncbi.nlm.nih.gov/28983819/) | 2017 | Ulasan | Advances in Therapy | Rituximab subkutan untuk keganasan hematologi sel B — rasional saintifik |
| [18240027](https://pubmed.ncbi.nlm.nih.gov/18240027/) | 2008 | Ulasan | Clin Rev Allergy Immunol | Rituximab di luar penghapusan sel B yang mudah — perkaitan untuk gangguan autoimun sel B |
| [12710588](https://pubmed.ncbi.nlm.nih.gov/12710588/) | 2002 | Ulasan | Anti-Cancer Drugs | Rituximab dalam gangguan sel B selain daripada NHL |
| [20194898](https://pubmed.ncbi.nlm.nih.gov/20194898/) | 2010 | Praklinik | Blood | Kejuruteraan GA101 (obinutuzumab) sebagai antibodi anti-CD20 generasi seterusnya yang ditingkatkan vs. rituximab |
| [25499448](https://pubmed.ncbi.nlm.nih.gov/25499448/) | 2015 | Ulasan | Blood | DLBCL — mengoptimalkan hasil dalam konteks heterogenitas klinikal/biologi |
| [33171490](https://pubmed.ncbi.nlm.nih.gov/33171490/) | 2021 | Ulasan | Blood | Rawatan limfoma Burkitt dalam dewasa |

### Indikasi 5: Histiositosis Sel Langerhans

Kesusasteraan khusus kepada rituximab dalam LCH adalah sangat terbatas; kebanyakan item yang dikembalikan oleh pencarian "histiositosis" yang lebih luas adalah tentang gangguan bukan-Langerhans yang tidak berkaitan (penyakit Rosai-Dorfman, xanthogranuloma nekrobiotik, penyakit Erdheim-Chester) dan hanya ketangential yang berkaitan:

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [30596314](https://pubmed.ncbi.nlm.nih.gov/30596314/) | 2018 | Siri kes (Tahap 3) | Pediatr Hematol Oncol | **Satu-satunya kertas yang langsung relevan-topik**: terapi rituximab untuk disfungsi neurologi yang berkaitan LCH |
| [18351339](https://pubmed.ncbi.nlm.nih.gov/18351339/) | 2008 | Laporan kes | Ann Hematol | LCH meniru relaps dalam pesakit limfoma folikular — pertindihan diagnostik, bukan bukti rawatan |
| [23256832](https://pubmed.ncbi.nlm.nih.gov/23256832/) | 2012 | Siri kes | Vnitrni Lekarstvi | Lenalidomida (bukan rituximab) dalam gangguan darah yang jarang termasuk LCH — latar belakang sahaja |
| [22681714](https://pubmed.ncbi.nlm.nih.gov/22681714/) | 2013 | Laporan kes | Actas Dermosifiliogr | Xanthogranuloma remaja (bukan-Langerhans) + limfoma folikular dirawat dengan kimia + rituximab |
| [15561688](https://pubmed.ncbi.nlm.nih.gov/15561688/) | 2004 | Ulasan | Hematology Am Soc Hematol Educ Program | Gambaran keseluruhan gangguan seluler/histiositik atipik termasuk LCH |

## Maklumat Pasaran Malaysia

Menurut data NPRA, rituximab mempunyai **9 jumlah pendaftaran** dan kini **dipasarkan** di Malaysia. Walau bagaimanapun, medan tahap lesen yang dikembalikan dalam pak bukti ini (nombor kebenaran, nama produk, bentuk dos, pengeluar, teks indikasi yang diluluskan) semuanya kosong — ini kelihatan sebagai jurang ekstraksi dalam sumber data NPRA daripada ketiadaan pendaftaran, dan harus ditarik semula sebelum calon ini bergerak lebih jauh.

## Sitotoksisiti

Penggunaan terjangka/yang ditubuhkan rituximab merangkau kedua-dua onkologi (NHL, CLL, MCL) dan penyakit autoimun bukan-onkologi (RA), jadi profil sitotoksisiti dimasukkan memandangkan kes penggunaan onkologi.

| Item | Kandungan |
|------|--------|
| Klasifikasi Sitotoksisiti | Terapi tersasaran / Imunoterapi (antibodi monoklonal anti-CD20) — bukan kemioterapi sitotoksik konvensional |
| Risiko Pengurangan Sumsum | Rendah hingga sederhana; kesan hematologi utama ialah pengurangan limfosit B daripada pengurangan sumsum yang luas, meskipun neutropenia (termasuk permulaan yang ditangguhkan) dilaporkan, khususnya dalam rejimen kombinasi (cth., R-CHOP, R-bendamustina) |
| Klasifikasi Emetogenisiti | Rendah (sebagai monoterapi); tindak balas yang berkaitan infusi (demam, menggigil, hipotensi) adalah risiko pentadbiran akut yang lebih bermakna secara klinikal — lihat PMID 37860948 di atas |
| Item Pemantauan | CBC dengan pembezaan, tahap imunoglobulin, status hepatitis B/risiko reaktivasi (menurut risiko kelas anti-CD20 yang diketahui), pemantauan tindak balas yang berkaitan infusi semasa pentadbiran |
| Perlindungan Pengendalian | Sebagai antibodi monoklonal biologi, langkah berjaga-jaga pengendalian ubat berbahaya/biologi piawai digunakan; tidak memerlukan protokol pengendalian kemioterapi sitotoksik konvensional |

Data toksisiti terperinci khusus kepada pak bukti ini tidak tersedia — sila rujuk amaran dan sesaat sisipan paket untuk panduan yang definitif.

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan. Medan keselamatan pak bukti ini (`key_warnings`, `contraindications`, `ddi.interactions`) tidak diisi (jurang data DG001, ditandai sebagai **keterukan Pemblokiran** — "tidak dapat memasuki pra-skrin keselamatan S1" — remediasi: ambil dan huraikan PDF sisipan paket TFDA/NPRA).

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Bercampur — lihat pecahan setiap indikasi**

**Rasional:**
- Indikasi 1–4 (NHL, RA, MCL, neoplasma sel B) adalah **penggunaan rituximab yang telah diluluskan**, bukan calon pengguna semula yang novel — TxGNN sedang mengesahkan pasangan ubat–penyakit yang diketahui di sini, yang merupakan pengesahan kebolehan model yang berguna tetapi tidak seharusnya dikira sebagai peluang saluran baharu. Ini membawa bukti L1 dan label "Teruskan dengan Pengawal" hanya dalam erti pengesahan amalan klinikal sedia ada, bukan meneroka sesuatu yang baru.
- Indikasi 5 (Histiositosis Sel Langerhans) adalah satu-satunya calon novel yang benar-benar, tetapi bukti kini terhad kepada siri kes kanak-kanak tunggal (L4, tahap "Soalan Penyelidikan") tanpa percubaan klinikal yang menyokong secara langsung menguji rituximab dalam LCH.

**Untuk meneruskan, perkara berikut diperlukan:**
- Selesaikan jurang data keselamatan yang Keterukan Pemblokiran (DG001): ambil dan huraikan sisipan paket TFDA/NPRA untuk amaran, percanggahan, dan data DDI sebelum sebarang pra-skrin keselamatan S1 boleh berlaku.
- Selesaikan jurang data MOA (DG002) melalui pertanyaan API DrugBank untuk mengesahkan klasifikasi mekanisme-tindakan.
- Tarik semula maklumat terperinci lesen NPRA Malaysia (nombor kebenaran, nama produk, teks indikasi) — semua 9 pendaftaran kini mempunyai rekod kosong.
- Siasat anomali `txgnn.score = 0.0` merentasi semua lima ramalan — medan ini kelihatan tidak diisi dan tidak seharusnya ditafsirkan sebagai skor keyakinan yang sebenar.
- Jika meneruskan LCH khususnya: telah menugaskan pencarian kesusasteraan/percubaan tersasaran yang terbatas kepada "histiositosis sel Langerhans" + "rituximab" (pertanyaan "histiositosis" luas semasa mengembalikan kebanyakan hasil luar sasaran untuk gangguan bukan-Langerhans yang tidak berkaitan) dan pertimbangkan sama ada kajian percontohan yang berdedikasi adalah wajar memandangkan asas bukti kes-laporan sahaja.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

