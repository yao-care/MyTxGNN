---
layout: default
title: Salicylic Acid
parent: Low Evidence (L4-L5)
nav_order: 608
evidence_level: L5
indication_count: 5
---

# Salicylic Acid
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

# Asid Salisilat: Dari Penggunaan Keratolik Topikal hingga Lima Indikasi Diprediksi TxGNN

## Ringkasan Satu Ayat

Asid salisilat (DrugBank DB00936) adalah agen beta-hidroksil asid (BHA) topikal yang telah lama dipasarkan dengan 71 lesen produk yang sedia ada di Malaysia, meskipun teks indikasi yang diluluskan asal yang khusus tidak ditangkap dalam penarikan data pendaftaran semasa. TxGNN menandai lima indikasi calon — **jerawat**, **mata ikan**, **keratosis yang diperoleh (aktinik)**, **penyakit keratinisasi**, dan **artritis degeneratif** — dengan kualiti bukti berkisar dari kuat, penggunaan klinikal yang sudah standard (jerawat dan mata ikan: **L1**, 34 dan 5 percubaan masing-masing) turun ke hipotesis kebanyakannya sejarah/praklinik (artritis degeneratif: **L3**). Ini terbaik dibaca sebagai portfolio lima soalan repurposing/sambungan label yang terpisah daripada satu indikasi baru tunggal.

---

## Gambaran Keseluruhan Cepat

*Nota: predicted_indications[0] mengikut pangkat TxGNN ("penyakit keratinisasi") membawa skor 0.0 dan bukti penyokong yang paling lemah (L3). Jadual di bawah menunjukkan entri tersebut ditambah perbandingan kesemua lima calon, kerana isyarat terkuat, paling boleh tindakan (jerawat, mata ikan) duduk pada pangkat 2–3, bukan pangkat 1.*

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak ditentukan dalam penarikan data pendaftaran (kesemua 5 rekod lesen sampel mempunyai `approved_indication_text` kosong); asid salisilat adalah agen keratolik/dermatologi topikal yang telah lama dipasarkan |
| Indikasi Baru Diprediksi (pangkat TxGNN 1) | Penyakit keratinisasi |
| Skor Prediksi TxGNN | Direkodkan sebagai 0.0 untuk kesemua 5 calon — nampaknya jurang populasi data daripada skor keyakinan yang tulen hampir sifar; **tidak boleh digunakan untuk pemeringkatan sebaik-baiknya** |
| Tahap Bukti (pangkat 1: penyakit keratinisasi) | L3 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 71 |
| Keputusan yang Disyorkan (pangkat 1: penyakit keratinisasi) | Soalan Penyelidikan |

### Kesemua Lima Indikasi Diprediksi, Disusun Mengikut Kekuatan Bukti

| Pangkat (TxGNN) | Penyakit | Tahap Bukti | Peringkat Keputusan | Cadangan | Kiraan CT / Lit |
|---|---|---|---|---|---|
| 2 | Jerawat | **L1** | S3 | Teruskan dengan Pengawasan | 34 CT / 19 Lit |
| 3 | Mata ikan | **L1** | S3 | Teruskan dengan Pengawasan | 5 CT / 20 Lit |
| 4 | Keratosis yang diperoleh (termasuk keratosis aktinik) | L2 | S3 | Teruskan dengan Pengawasan | 0 CT / 19 Lit |
| 1 | Penyakit keratinisasi | L3 | S2 | Soalan Penyelidikan | 1 CT / 19 Lit |
| 5 | Artritis degeneratif | L3 | S1 | Soalan Penyelidikan | 3 CT / 20 Lit |

---

## Mengapa Prediksi Ini Munasabah?

Data mekanisme-tindakan terperinci tidak dipenuhi dalam pak bukti ini (ditandai sebagai jurang data DG002, keterukan Tinggi). Berdasarkan farmakoloji yang ditubuhkan, asid salisilat adalah beta-hidroksil asid (BHA) lipofil yang, apabila digunakan secara topikal, bertindak sebagai **agen keratolik/desmolitik**: ia mengganggu perekat desmosomal antara sel dalam stratum korneum, menggalakkan pelepasan keratin yang tidak normal tebal atau kohesif. Mekanisme tunggal ini munasabah menjelaskan empat daripada lima indikasi diprediksi — **jerawat** (hiperkeratosis folikuler + penyumbatan sebum), **mata ikan** (epidermis hiperkeratotik yang dijangkiti HPV), **keratosis aktinik/yang diperoleh** (epidermis hiperkeratotik displastik, di mana asid salisilat meningkatkan penetrasi produk co-formulasi 5-fluorourasil), dan kategori **penyakit keratinisasi** yang lebih luas (keratodermas palmoplantar, penyakit Darier, iktiosis) — semua yang berkongsi hiperkeratosis sebagai patologi inti.

Calon kelima, **artritis degeneratif**, bergantung pada laluan mekanistik yang berbeza: garam salisilat (cth., natrium salisilat) mempunyai aktiviti anti-inflamasi/analgesik perencatan siklo-oksigenase (COX) sistemik, yang telah dikaji secara sejarah untuk sakit sendi sebelum disalahi oleh NSAID moden. Ini berkaitan secara farmakoloji dengan asid salisilat tetapi adalah soalan laluan/formulasi yang berbeza (sistemik vs. topikal) dan disokong kebanyakannya oleh literatur 1950–1980an ditambah satu kajian nanozarah praklinik 2025 — sambungan yang jauh lebih lemah dan lebih spekulatif daripada indikasi keratolik.

Kerana tiada satu pun daripada empat indikasi laluan keratolik mewakili mekanisme benar-benar baru, soalan praktikal untuk set calon ini kurang "adakah repurposing biologi munasabah" dan lebih "berapa banyak daripada ini adalah standard penjagaan/sambungan label sudah ada (jerawat, mata ikan) berbanding tulen kurang bukti (gangguan keratinisasi jarang, artritis degeneratif)."

---

## Bukti Percubaan Klinikal

### Jerawat (pangkat TxGNN 2, L1)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---|---|---|---|---|
| [NCT02052752](https://clinicaltrials.gov/study/NCT02052752) | Fasa 4 | Selesai | 90 | Kajian berubah dua-buta rawakan menilai betapa cepatnya produk asid salisilat topikal jerawat menghasilkan peningkatan lesi yang kelihatan dalam 5 hari |
| [NCT05821296](https://clinicaltrials.gov/study/NCT05821296) | N/A | Selesai | 42 | "Crystal Peel," pembusukan berasaskan asid salisilat, dinilai untuk keberkesanan kiraan lesi dalam jerawat vulgaris ringan di wajah |
| [NCT06179056](https://clinicaltrials.gov/study/NCT06179056) | N/A | Selesai | 48 | Dibandingkan aktiviti anti-biofilm asid salisilat, isotretinoin, dan N-asetilsistein terhadap C. acnes, dan kesan pada kerentanan antibiotik |
| [NCT03071549](https://clinicaltrials.gov/study/NCT03071549) | Fasa 3 | Selesai | 34 | Rawakan bebas-belah: asid salisilat + kombinasi asid azelat vs. pembusukan TCA 25% untuk jerawat ringan hingga sederhana |
| [NCT00624676](https://clinicaltrials.gov/study/NCT00624676) | N/A | Selesai | 80 | Kajian perbandingan rawakan: terbitan asid salisilat lipofilik (LHA) dengan benzoil peroksida 5% untuk jerawat vulgaris wajah |
| [NCT01446237](https://clinicaltrials.gov/study/NCT01446237) | N/A | Selesai | 125 | Kajian serbuka 12 minggu sistem kombinasi benzoil peroksida 2.5% + asid salisilat 0.5% untuk jerawat sederhana hingga teruk |
| [NCT02755545](https://clinicaltrials.gov/study/NCT02755545) | Fasa 4 | Selesai | 127 | Percubaan berbilang pusat 24 minggu membandingkan dua rawatan jerawat pada orang dewasa dengan jerawat wajah ringan hingga sederhana |
| [NCT03832647](https://clinicaltrials.gov/study/NCT03832647) | Fasa 4 | Selesai | 200 | Rawakan dua-buta produk dermo-kosmetik ditambah adapalen/benzoil peroksida vs. adapalen/BPO ditambah pelembap standard |
| [NCT05712837](https://clinicaltrials.gov/study/NCT05712837) | N/A | Selesai | 60 | Rawakan: pembusukan TCA 25% vs. pembusukan asid salisilat 30% dalam jerawat vulgaris ringan hingga sederhana |
| [NCT05497323](https://clinicaltrials.gov/study/NCT05497323) | Fasa 1 | Tidak diketahui | 284 | Krim kombinasi yang mengandungi asid salisilat + niasida + zat aktif lain sebagai terapi tambahan untuk jerawat ringan hingga sederhana |

### Mata Ikan (pangkat TxGNN 3, L1) — kesemua 5 percubaan berdaftar ditunjukkan

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---|---|---|---|---|
| [NCT05617950](https://clinicaltrials.gov/study/NCT05617950) | N/A | Tidak diketahui | 174 | Kajian rawakan kepala-ke-kepala: asid salisilat vs. krioterapi untuk mata ikan akibat HPV-1 |
| [NCT06958237](https://clinicaltrials.gov/study/NCT06958237) | N/A | Selesai | 30 | Penilaian prestasi/keselamatan pasca-pasaran tampalan mata ikan berasaskan asid salisilat (peranti perubatan) untuk mata ikan umum dan mata ikan |
| [NCT01712295](https://clinicaltrials.gov/study/NCT01712295) | Fasa 4 | Tidak diketahui | 100 | Formulasi salisilat baru (dengan etil piruvat) vs. salisilat 17% standard penjagaan untuk mata ikan |
| [NCT05588999](https://clinicaltrials.gov/study/NCT05588999) | Fasa 1 | Selesai | 70 | Krioterapi sahaja vs. krioterapi + pembalut asid salisilat untuk mata ikan |
| [NCT02151630](https://clinicaltrials.gov/study/NCT02151630) | Fasa 2/3 | Tidak diketahui | 60 | Dibandingkan asid piruvat 70% vs. larutan asid salisilat kompaun (16.7% SA + asid laktat) untuk mata ikan |

### Keratosis yang Diperoleh (pangkat TxGNN 4, L2)

Pada masa kini tiada percubaan klinikal yang berkaitan didaftarkan untuk istilah penyakit yang tepat ini. (Bukti percubaan RCT penyokong untuk produk kombinasi 5-FU/asid salisilat yang khusus wujud dalam jadual literatur di bawah.)

### Penyakit Keratinisasi (pangkat TxGNN 1, L3)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---|---|---|---|---|
| [NCT05536193](https://clinicaltrials.gov/study/NCT05536193) | Fasa 4 | Tidak diketahui | 34 | Kajian belah-muka topikan metformin emulgel vs. pembusukan asid salisilat untuk jerawat vulgaris — kaitan kepada "penyakit keratinisasi" yang luas adalah tidak langsung (percubaan spesifik jerawat, disusun C) |

### Artritis Degeneratif (pangkat TxGNN 5, L3)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---|---|---|---|---|
| [NCT03277573](https://clinicaltrials.gov/study/NCT03277573) | Fasa 1 | Selesai | 40 | Kajian keselamatan/ketoleransian/PK salsalat (salisilat) dalam penyakit Alzheimer ringan hingga sederhana — bukan percubaan OA; termasuk hanya untuk kaitan kelas salisilat, memerlukan pengesahan manual |
| [NCT04066426](https://clinicaltrials.gov/study/NCT04066426) | Fasa 4 | Selesai | 200 | Perbandingan analgesik berasaskan naproksena untuk sakit miofasial/TMD — naproksena adalah campur tangan, bukan asid salisilat; kaitan kelas NSAID tidak langsung sahaja |
| [NCT07350239](https://clinicaltrials.gov/study/NCT07350239) | N/A | Belum merekrut | 20 | Pencirian pemerhatian patologi TMJ yang teruk — tiada campur tangan asid salisilat |

Tiada satu pun daripada tiga percubaan "artritis degeneratif" yang terdaftar adalah percubaan keberkesanan asid salisilat langsung dalam OA; indikasi ini bergantung hampir sepenuhnya pada literatur kelas salisilat yang lebih lama dan satu kajian praklinik 2025 (lihat di bawah).

---

## Bukti Literatur

### Jerawat

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [38300170](https://pubmed.ncbi.nlm.nih.gov/38300170/) | 2024 | Garis Panduan | J Am Acad Dermatol | Garis panduan penjagaan AAD untuk pengurusan jerawat vulgaris |
| [35789996](https://pubmed.ncbi.nlm.nih.gov/35789996/) | 2022 | Ulasan Sistematik/NMA | Br J Dermatol | Meta-analisis rangkaian rawatan jerawat topikal/lisan/fizikal/digabungkan |
| [40682377](https://pubmed.ncbi.nlm.nih.gov/40682377/) | 2025 | Rawakan | J Cosmet Dermatol | Kajian prospektif 21 hari: gel asid salisilat meningkatkan lesi jerawat sambil mengekalkan fungsi penghalang kulit |
| [30972839](https://pubmed.ncbi.nlm.nih.gov/30972839/) | 2019 | Mekanistik | Exp Dermatol | Asid salisilat menindas laluan AMPK/SREBP1 dalam sebasit, mengurangkan pengeluaran sebum |
| [26347269](https://pubmed.ncbi.nlm.nih.gov/26347269/) | 2015 | Ulasan | Clin Cosmet Investig Dermatol | Ulasan komprehensif asid salisilat sebagai agen pembusukan/komedolitik |
| [34812859](https://pubmed.ncbi.nlm.nih.gov/34812859/) | 2021 | Ulasan | JAMA | Ulasan umum pengurusan jerawat vulgaris, termasuk terapi BHA topikal |
| [33034949](https://pubmed.ncbi.nlm.nih.gov/33034949/) | 2020 | Ulasan Cochrane (ringkas) | J Evid Based Med | Ulasan berasaskan bukti asid azelat/salisilat, niasida, sulfur, seng, asid buah untuk jerawat |
| [32356369](https://pubmed.ncbi.nlm.nih.gov/32356369/) | 2020 | Ulasan Sistematik Cochrane | Cochrane Database Syst Rev | Ulasan Cochrane penuh asid azelat topikal, asid salisilat, dan agen berkaitan untuk jerawat |
| [39420562](https://pubmed.ncbi.nlm.nih.gov/39420562/) | 2024 | Ulasan | Expert Opin Pharmacother | Pembaruan pengurusan farmakoloji jerawat vulgaris |
| [30550830](https://pubmed.ncbi.nlm.nih.gov/30550830/) | 2019 | Ulasan | J Am Acad Dermatol | Ulasan pembusukan kimia kedalaman dangkal dan sederhana, termasuk pembusukan asid salisilat |

### Mata Ikan

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [33263934](https://pubmed.ncbi.nlm.nih.gov/33263934/) | 2021 | Ulasan Sistematik | Dermatol Ther | Ulasan sistematik rawatan topikal untuk mata ikan |
| [40743833](https://pubmed.ncbi.nlm.nih.gov/40743833/) | 2025 | Rawakan Pragmatik Berbilang-pusat | Ann Dermatol Venereol | Dibandingkan asid salisilat 50%, krioterapi, krim 5-FU, dan imiquimod dalam mata ikan yang pernah dirawat sebelumnya |
| [21652750](https://pubmed.ncbi.nlm.nih.gov/21652750/) | 2011 | Rawakan | BMJ | Percubaan rawakan: krioterapi vs. asid salisilat untuk mata ikan |
| [3377974](https://pubmed.ncbi.nlm.nih.gov/3377974/) | 1988 | Rawakan Dua-buta | Br J Dermatol | Asam monokloroasetik + asid salisilat 60% lebih baik daripada plasebo untuk mata ikan sederhana (66% vs 18% penyembuhan) |
| [16281635](https://pubmed.ncbi.nlm.nih.gov/16281635/) | 2004 | Ulasan Sistematik/Meta-analisis | J Dtsch Dermatol Ges | Keberkesanan persediaan 5-FU/asid salisilat untuk mata ikan umum dan mata ikan |
| [29379975](https://pubmed.ncbi.nlm.nih.gov/29379975/) | 2018 | Ulasan | J Am Osteopath Assoc | Epidemiologi, patofisiologi, dan pengurusan klinikal mata ikan |
| [39295250](https://pubmed.ncbi.nlm.nih.gov/39295250/) | 2024 | Siri kes retrospektif (n=48) | J Med Virol | Formulasi kantaridin/podofil/asid salisilat (CPS) dalam mata ikan yang sukar dilawan |
| [27072919](https://pubmed.ncbi.nlm.nih.gov/27072919/) | 2016 | Retrospektif (n=75) | Dermatol Ther | Keselamatan/keberkesanan rawatan CPS untuk mata ikan yang sukar dilawan |
| [12852385](https://pubmed.ncbi.nlm.nih.gov/12852385/) | 2003 | Kohort/laporan kes | J Drugs Dermatol | Imiquimod kombinasi + tampalan asid salisilat untuk mata ikan |
| [40526950](https://pubmed.ncbi.nlm.nih.gov/40526950/) | 2024 | Ulasan | Dermatol Online J | Ulasan terkini penggunaan kantaridin topikal, termasuk formulasi CPS untuk mata ikan |

### Keratosis yang Diperoleh (termasuk Keratosis Aktinik)

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [27995485](https://pubmed.ncbi.nlm.nih.gov/27995485/) | 2017 | Rawakan Fasa III | Dermatol Ther | 5-FU 0.5%/asid salisilat 10% lebih baik daripada kenderaan untuk rawatan keratosis aktinik yang bertujuan bidang |
| [32478958](https://pubmed.ncbi.nlm.nih.gov/32478958/) | 2020 | Kohort | Dermatol Ther | Pemantauan dermoskopi/RCM terapi rawatan 5-FU/SA yang bertujuan lesi untuk keratosis aktinik |
| [27223248](https://pubmed.ncbi.nlm.nih.gov/27223248/) | 2016 | Ulasan produk | Skin Therapy Lett | Ulasan Actikerall (5-FU 0.5%/SA 10%) untuk rawatan AK yang bertujuan pesakit |
| [35435128](https://pubmed.ncbi.nlm.nih.gov/35435128/) | 2022 | Kohort pemerhatian | J Dermatolog Treat | Tindak balas klinikal awal kepada larutan topikal 5-FU/SA untuk keratosis aktinik kepala/leher |
| [36902419](https://pubmed.ncbi.nlm.nih.gov/36902419/) | 2023 | Ulasan | Int J Mol Sci | Ulasan agen farmakoloji (termasuk 5-FU/SA) untuk pencegahan/rawatan keratosis aktinik |
| [38351246](https://pubmed.ncbi.nlm.nih.gov/38351246/) | 2024 | Ulasan | Am J Clin Dermatol | Terapi pemerbersihan bidang untuk pengurusan keratosis aktinik |
| [25495775](https://pubmed.ncbi.nlm.nih.gov/25495775/) | 2015 | Analisis keberkesanan kos | Expert Rev Pharmacoecon Outcomes Res | Keberkesanan kos 5-FU/SA untuk keratosis aktinik di Sepanyol |
| [24472429](https://pubmed.ncbi.nlm.nih.gov/24472429/) | 2014 | Ulasan (keselamatan) | J Am Acad Dermatol | Ulasan risiko ketoksikan/salisilisme daripada persediaan asid salisilat topikal |
| [32886029](https://pubmed.ncbi.nlm.nih.gov/32886029/) | 2022 | Ulasan Sistematik | J Dermatolog Treat | Pilihan rawatan (termasuk keratolik) untuk keratosis pilar dan varian |
| [17298101](https://pubmed.ncbi.nlm.nih.gov/17298101/) | 2007 | Ulasan | Am J Clin Dermatol | Ulasan pengurusan keratoderma palmoplantar yang diperoleh |

### Penyakit Keratinisasi (kategori luas — kebanyakan bukti berasaskan kes)

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [23986157](https://pubmed.ncbi.nlm.nih.gov/23986157/) | 2013 | Rawakan Dua-buta | J Drugs Dermatol | Krim asid alfa/poli-hidroksil 20% mengurangkan pengelupasan dalam psoriasis plak kronik |
| [30972839](https://pubmed.ncbi.nlm.nih.gov/30972839/) | 2019 | Mekanistik | Exp Dermatol | Kesan asid salisilat pada laluan hiperkeratinisasi folikuler (AMPK/SREBP1) |
| [41231204](https://pubmed.ncbi.nlm.nih.gov/41231204/) | 2025 | Praklinik (tikus) | J Drug Target | Komponen gel asid salisilat dalam nanoemulsi untuk model psoriasis teraruh imiquimod |
| [29077501](https://pubmed.ncbi.nlm.nih.gov/29077501/) | 2017 | Ulasan (berasaskan kes) | J Am Podiatr Med Assoc | Pengurusan keratodermas palmoplantar, pelajaran daripada Pachyonychia congenita |
| [11976541](https://pubmed.ncbi.nlm.nih.gov/11976541/) | 2002 | Ulasan | Ann Dermatol Venereol | Ulasan patofisiologi xerosis dan keratinisasi yang tidak teratur |
| [29500825](https://pubmed.ncbi.nlm.nih.gov/29500825/) | 2018 | Laporan kes | J Dermatol | Keratoderma palmoplantar bergaris jenis I dirawat dengan akretin + asid salisilat topikal |
| [36812285](https://pubmed.ncbi.nlm.nih.gov/36812285/) | 2022 | Laporan kes | Acta Dermatovenerol Croat | Kes penyakit Darier segmental |
| [17511940](https://pubmed.ncbi.nlm.nih.gov/17511940/) | 2007 | Laporan kes | Dermatol Online J | Keratosis folikularis (penyakit Darier-White) dengan keratoderma palmoplantar yang luar biasa |
| [31364784](https://pubmed.ncbi.nlm.nih.gov/31364784/) | 2019 | Laporan kes | Dermatol Ther | Pachyonychia congenita bertindak balas terhadap terapi gabungan pembedahan/perubatan (termasuk topikal) |
| [28223752](https://pubmed.ncbi.nlm.nih.gov/28223752/) | 2017 | Laporan kes | Ann Dermatol | Dermatosis terra firma-forme dirawat dengan pengelupasan alkohol asid salisilat |

### Artritis Degeneratif

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [14592543](https://pubmed.ncbi.nlm.nih.gov/14592543/) | 2003 | Ulasan Mekanistik | Thromb Res | Ulasan sejarah mekanisme tindakan aspirin/salisilat |
| [20547600](https://pubmed.ncbi.nlm.nih.gov/20547600/) | 2010 | Rawakan | Postgrad Med J | Injeksi natrium salisilat subkutan untuk sakit artritis degeneratif ibu jari |
| [41394718](https://pubmed.ncbi.nlm.nih.gov/41394718/) | 2025 | Praklinik (haiwan) | bioRxiv (prapencetak) | Zarah asid poli-salisilat mengurangkan sakit dan kerosakan struktur dalam model OA pasca-trauma |
| [38785813](https://pubmed.ncbi.nlm.nih.gov/38785813/) | 2024 | Praklinik (tikus) | Biology | Zarah nano asid salisilat-ferum-oksida mengurangkan lesi histologi dalam OA lutut teraruh MIA |
| [7361087](https://pubmed.ncbi.nlm.nih.gov/7361087/) | 1980 | Perbandingan Dua-buta | Schweiz Med Wochenschr | Diflunisal vs. asid asetilsalisilik dalam artritis degeneratif pinggul/lutut (perbandingan 12 minggu) |
| [331427](https://pubmed.ncbi.nlm.nih.gov/331427/) | 1977 | Rawakan (sejarah) | Rev Med Chile | Fenbufen vs. asid asetilsalisilik dalam rawatan artritis degeneratif |
| [17688170](https://pubmed.ncbi.nlm.nih.gov/17688170/) | 2007 | Rawakan kecil | Niger Q J Hosp Med | TENS vs. iontofisis natrium salisilat untuk artritis degeneratif lutut |
| [6988202](https://pubmed.ncbi.nlm.nih.gov/6988202/) | 1980 | Ulasan | Drugs | Farmakoloji diflunisal (terbitan salisilat) dan penggunaan dalam sakit OA |
| [2754669](https://pubmed.ncbi.nlm.nih.gov/2754669/) | 1989 | In vitro | J Rheumatol | Kesan natrium salisilat pada metabolisme proteoglikan tulang rawan artritis degeneratif |
| [12244878](https://pubmed.ncbi.nlm.nih.gov/12244878/) | 2002 | Ulasan | Wien Med Wochenschr | Ekstrak kulit willow (sumber salisilat semulajadi) ulasan farmakoloji/penggunaan klinikal |

*Bukti praklinik/mekanistik yang dicatat (peringkat "belum selesai"/tidak diklasifikasi dalam sumber) harus disahkan secara bebas sebelum petikan dalam sebarang penyerahan peraturan.*

---

## Maklumat Pasaran Malaysia

Jumlah pendaftaran: **71 lesen**, status pasaran **Dipasarkan**. Rekod otorisasi individu (nombor lesen, nama produk, bentuk dos, teks indikasi diluluskan) dikembalikan sebagai medan kosong dalam penarikan data ini dan tidak tersedia untuk jadual — ini harus diselesaikan dengan menanyakan semula data pendaftaran NPMB sebelum sebarang keputusan penjajaran label dibuat.

---

## Pertimbangan Keselamatan

Tiada medan keselamatan yang dipenuhi (amaran utama, kontraindikasi, atau interaksi ubat-ubatan) dikembalikan dalam penarikan data ini — ditandai sebagai jurang data DG001 (**Keterukan Penutupan**: "tidak dapat meneruskan prapenilaian keselamatan S1"). Sila rujuk sisipan pek untuk maklumat keselamatan.

Satu titik yang relevan dengan keselamatan memang muncul daripada bukti literatur itu sendiri dan patut ditandai secara bebas daripada medan keselamatan yang hilang: asid salisilat topikal membawa risiko terdokumen, jika tidak biasa, daripada **salisilisme (ketoksikan salisilat)** dengan penggunaan kepekatan tinggi atau luas permukaan besar/lama (PMID [24472429](https://pubmed.ncbi.nlm.nih.gov/24472429/)) — berkaitan dengan sebarang indikasi yang diperluaskan melibatkan kawasan rawatan yang lebih besar (cth., jerawat trunkus, keratoderma yang luas) atau populasi kanak-kanak/gangguan fungsi ginjal.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Pengawasan (jerawat, mata ikan, keratosis aktinik/yang diperoleh) / Tahan (penyakit keratinisasi, artritis degeneratif)**

**Alasan:**
- Jerawat dan mata ikan sudah mempunyai bukti L1 (34 dan 5 percubaan masing-masing, termasuk RCT kepala-ke-kepala) dan mencerminkan penggunaan klinikal/OTC yang mantap — kerja utama yang tinggal adalah penjajaran label peraturan, bukan penyelidikan keberkesanan baru.
- Keratosis aktinik/yang diperoleh (L2) disokong oleh produk kombinasi yang telah diluluskan sedia ada (5-FU 0.5%/SA 10%, cth., Actikerall) dalam pasaran lain — calon sambungan label Malaysia yang berdaya hayat dengan menunggu data keselamatan setempat.
- Penyakit keratinisasi (L3, pangkat 1 mengikut skor TxGNN) dan artritis degeneratif (L3) bergantung pada laporan kes, percubaan kecil/sudah lama, atau kerja praklinik 2024–2025 sahaja — hipotesis repurposing yang nyata, tetapi belum boleh tindakan tanpa kajian khusus.
- Medan skor TxGNN itu sendiri (0.0 merentasi kesemua lima calon) nampaknya cacat populasi data dan tidak boleh digunakan untuk memprioritaskan di antara lima indikasi ini sehingga diperbetulkan.

**Untuk meneruskan, yang berikut diperlukan:**
- Selesaikan DG001 (Penutupan): dapatkan amaran label NPMB sebenar/kontraindikasi sebelum sebarang penilaian keselamatan S1
- Selesaikan DG002 (Tinggi): dapatkan pernyataan MOA yang disahkan DrugBank/sumber literatur
- Tanyakan semula data pendaftaran NPMB untuk mengisi rekod lesen individu (nama produk, bentuk dos, teks indikasi diluluskan) — rekod semasa kosong
- Sahkan/betulkan medan skor TxGNN (pada masa ini 0.0 untuk kesemua calon, berkemungkinan cacat saluran paip)
- Untuk artritis degeneratif khususnya: sahkan secara manual NCT03277573 dan NCT04066426, kerana campur tangan yang disenaraikan bagi tidak satu pun percubaan itu adalah asid salisilat itu sendiri yang jelas

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

