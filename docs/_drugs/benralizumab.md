---
layout: default
title: Benralizumab
parent: Low Evidence (L4-L5)
nav_order: 126
evidence_level: L5
indication_count: 5
---

# Benralizumab
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

# Benralizumab: Daripada Asma Eosinofilik Teruk kepada Dermatitis

## Ringkasan Satu Ayat

Benralizumab ialah antibodi monoklonal anti-IL-5Rα yang asalnya diluluskan untuk rawatan penyelenggaraan tambahan bagi asma eosinofilik teruk. Model TxGNN meramalkan ia mungkin berkesan untuk **Dermatitis** (berpangkat ke-2 daripada 5 ramalan), dengan **6 percubaan klinikal** dan **20 penerbitan** tersedia — bagaimanapun, percubaan HILLIER Fasa 2 yang utama menunjukkan **kekurangan kesan klinikal**, menjadikan ini contoh berhati-hati bagi ramalan model yang bertentangan dengan bukti klinikal.

---

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Asma eosinofilik teruk (rawatan penyelenggaraan tambahan) |
| Petunjuk Ramalan Baru | Dermatitis (Pangkat 2); Trombositopenia disebabkan oleh kemusnahan imun (Pangkat 1) |
| Skor Ramalan TxGNN (Pangkat 1) | 99.34% (trombositopenia — tiada bukti sokongan) |
| Skor Ramalan TxGNN (Pangkat 2) | 99.16% (dermatitis — RCT Fasa 2 negatif) |
| Tahap Bukti | **L2** (dermatitis: 1 RCT Fasa 2 selesai); **L5** (semua petunjuk lain) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Cadangan Keputusan | **Tahan** — RCT Fasa 2 utama menghasilkan keputusan negatif yang pasti |

---

## Gambaran Keseluruhan Semua Petunjuk Ramalan

| Pangkat | Petunjuk Ramalan | Skor TxGNN | Tahap Bukti | Cadangan |
|------|---------------------|-------------|---------------|---------------|
| 1 | Trombositopenia disebabkan oleh kemusnahan imun | 99.34% | L5 | Tahan |
| 2 | Dermatitis | 99.16% | L2 | Tahan (RCT negatif) |
| 3 | Acne keloid | 99.13% | L5 | Tahan |
| 4 | Dermatomyositis neonatal | 99.05% | L5 | Tahan |
| 5 | Dermatomyositis amyopatik | 99.03% | L5 | Tahan |

> **Nota:** Daripada 5 ramalan TxGNN, hanya **dermatitis** (Pangkat 2) mempunyai bukti klinikal atau kesusasteraan. 4 ramalan yang tinggal bergantung semata-mata pada model tanpa kajian sokongan. Laporan ini memfokus pada dermatitis sebagai petunjuk paling bermaklumat untuk penilaian.

---

## Mengapa Ramalan Ini Munasabah?

Benralizumab ialah antibodi monoklonal anti-IL-5Rα yang dimanusiakan yang menghapuskan eosinofil dan sel bakul melalui sitotoksisitas dimediasi sel bergantung pada antibodi (ADCC). Ia asalnya dibangunkan dan diluluskan untuk asma eosinofilik teruk, di mana inflamasi didorong oleh eosinofil memainkan peranan patogenik pusat. Model TxGNN memberikan skor tinggi kepada pelbagai keadaan dimediasi imun, kemungkinan mencerminkan kedekatan graf antara nod penyakit berkaitan eosinofil dalam graf pengetahuan.

Untuk **dermatitis** (khususnya dermatitis atopik, AD), alasan mekanik adalah sederhana tetapi akhirnya tidak mencukupi. Eosinofil memang terdapat dalam lesi kulit AD, dan benralizumab telah terbukti berkesan menghapuskan sel pembawa IL-5Rα dalam kulit pesakit AD (PMID 40781582). Bagaimanapun, pemacu teras AD ialah paksi Th2-terpolarisasi IL-4/IL-13, yang membawa kepada gangguan halangan epidermal dan kitaran gatal-calar. Penyingkiran eosinofil sahaja tidak mengganggu gelung patogenik pusat ini — kesimpulan yang disahkan oleh keputusan negatif percubaan HILLIER.

Untuk **trombositopenia disebabkan oleh kemusnahan imun** (Pangkat 1, skor TxGNN tertinggi), pautan mekanik adalah lemah. ITP didorong oleh autoantibodi anti-platelet (anti-GPIIb/IIIa, anti-GPIb/IX) dan kemusnahan platelet dimediasi sel T. Eosinofil bukan pemain utama dalam patogenesis ITP. Skor TxGNN yang tinggi kemungkinan mencerminkan kedekatan nod penyakit imun dalam graf pengetahuan dan bukannya potensi terapeutik tulin. Ramalan yang tinggal (acne keloid, dermatomyositis neonatal, dermatomyositis amyopatik) berkongsi alasan mekanik yang sama lemah — pemacu patogenik (pengaktifan fibroblast/TGF-β untuk keloid; interferon jenis I/komplemen untuk dermatomyositis) tidak berkaitan dengan biologi eosinofil.

---

## Bukti Percubaan Klinikal (Dermatitis)

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Fasa 2 | **Ditamatkan** | 194 | **Kajian HILLIER**: Percubaan multinasional, rawak, buta ganda, terkawal plasebo dalam AD sederhana hingga teruk. **Ditamatkan disebabkan kekurangan keberkesanan.** Keputusan yang diterbitkan (PMID 37178404) secara eksplisit melaporkan "Kekurangan kesan" benralizumab pada tanda dan gejala AD. |
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Fasa 2 | Selesai | 20 | Kajian mekanik: Benralizumab berjaya menghapuskan sel pembawa IL-5Rα (eosinofil, sel bakul, ILC2s) dalam lesi kulit AD, tetapi kesan biologi ini **tidak diterjemahkan ke dalam peningkatan klinikal**. |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Fasa 2 | Belum lagi merekrut | 96 | Sasaran DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms), entiti yang berbeza daripada AD biasa. Eosinofil memainkan peranan yang lebih menonjol dalam DRESS. Patut dipantau tetapi tidak secara langsung terpakai pada AD. |
| [NCT06477653](https://clinicaltrials.gov/study/NCT06477653) | Fasa 2 | Merekrut | 30 | Mengkaji **dupilumab** (bukan benralizumab) sebagai tambahan untuk HES. Kaitan tidak langsung sahaja. |
| [NCT04126499](https://clinicaltrials.gov/study/NCT04126499) | T/A | Selesai | 28 | Kajian retrospektif pemerhatian benralizumab dalam pesakit asma eosinofilik teruk di Sepanyol. Tidak dirancang untuk penilaian dermatitis. |
| [NCT04763447](https://clinicaltrials.gov/study/NCT04763447) | Fasa 4 | Merekrut | 234 | Mengkaji penarikan balik **omalizumab** dalam asma. Tiada kaitan langsung pada benralizumab atau dermatitis. |

> ⚠️ **Penemuan kritikal:** Dua-dua percubaan yang secara langsung relevan (HILLIER dan NCT03563066) menunjukkan bahawa walaupun benralizumab mencapai sasaran biologinya (penyingkiran eosinofil dalam kulit), ini **tidak** menghasilkan faedah klinikal untuk dermatitis atopik.

---

## Bukti Percubaan Klinikal (Petunjuk Ramalan Lain)

Pada masa ini tiada percubaan klinikal berkaitan yang didaftarkan untuk:
- Trombositopenia disebabkan oleh kemusnahan imun
- Acne keloid
- Dermatomyositis neonatal
- Dermatomyositis amyopatik

---

## Bukti Kesusasteraan (Dermatitis)

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [37178404](https://pubmed.ncbi.nlm.nih.gov/37178404/) | 2023 | **RCT Fasa 2** | JEADV | **Keputusan percubaan HILLIER: "Kekurangan kesan benralizumab pada tanda dan gejala dermatitis atopik sederhana hingga teruk."** Bukti negatif pasti. |
| [38695680](https://pubmed.ncbi.nlm.nih.gov/38695680/) | 2024 | RCT Fasa 2 (sekunder) | Immunotherapy | Ringkasan bahasa biasa kajian HILLIER, mengesahkan benralizumab tidak meningkatkan hasil AD. |
| [40781582](https://pubmed.ncbi.nlm.nih.gov/40781582/) | 2025 | Kajian translasi | Clin Transl Allergy | Benralizumab menghapuskan sel pembawa IL-5Rα dalam lesi kulit AD, tetapi kesan biologi tidak berkorelasi dengan peningkatan klinikal. |
| [39234416](https://pubmed.ncbi.nlm.nih.gov/39234416/) | 2024 | Kajian translasi | JACI Global | Menilai kesan benralizumab pada inflamasi kulit selepas cabaran alergen intraderma dalam pesakit AD. |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Ulasan | Allergologie select | Kemas kini komprehensif tentang biologi untuk penyakit atopik; meletakkan benralizumab antara agen penyasaran IL-5 yang lain. |
| [37201737](https://pubmed.ncbi.nlm.nih.gov/37201737/) | 2023 | Ulasan sains asas | Pharmacol Ther | Mengulas sel Th2 patogenik sebagai sasaran terapeutik; menerangkan mengapa penyekat IL-4/IL-13 (bukan IL-5Rα) ialah laluan berkesan untuk AD. |
| [36355314](https://pubmed.ncbi.nlm.nih.gov/36355314/) | 2023 | Ulasan | Dermatol Ther | Membincangkan gabungan dupilumab dengan biologi lain; benralizumab disebut dalam konteks komorbidit atopik. |
| [36270814](https://pubmed.ncbi.nlm.nih.gov/36270814/) | 2023 | Laporan kes (AE) | Therapie | **Laporan peristiwa buruk**: Dermatitis granulomatosa antargranular teraruh benralizumab — reaksi kulit paradoks. |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Ulasan keselamatan | JACI In Practice | Keselamatan biologi (termasuk benralizumab) untuk penyakit atopik semasa kehamilan. |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Ulasan keselamatan | Immunol Allergy Clin N Am | Biologi untuk rinitis alergik, asma, dan AD semasa kehamilan dan laktasi. |

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk Diluluskan |
|---------|------|------|-----------|
| (Butiran pendaftaran belum selesai) | Benralizumab | — | Asma eosinofilik teruk |

> Pendaftaran NPRA mengesahkan 1 pendaftaran aktif. Maklumat lesen terperinci (nama produk, bentuk dos, teks petunjuk penuh) tidak tersedia dalam pakej bukti pada masa laporan ini.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> **Nota:** Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti semasa (Jurang Data DG001). Untuk terus ke penilaian keselamatan (Tahap S1), PDF sisipan pakej harus diperolehi daripada laman web NPRA dan dianalisis untuk amaran, kontraindikasi, dan tindakan berjaga-jaga.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Walaupun skor ramalan TxGNN yang tinggi (>99%) merentasi semua 5 petunjuk ramalan, bukti klinikal secara langsung bercanggah dengan ramalan yang paling tersokong bukti. Percubaan HILLIER (Fasa 2, n=194, rawak, buta ganda, terkawal plasebo) secara pasti menunjukkan **kekurangan kesan** benralizumab dalam dermatitis atopik sederhana hingga teruk. Kajian translasi mengesahkan bahawa walaupun benralizumab mencapai sasaran biologinya (penyingkiran eosinofil dalam kulit), ini tidak diterjemahkan ke dalam peningkatan klinikal — menunjukkan bahawa eosinofil bukan faktor patogenik penghad kadar dalam AD. 4 ramalan yang tinggal (trombositopenia, acne keloid, dermatomyositis neonatal/amyopatik) tidak mempunyai bukti sokongan dan alasan mekanik lemah.

**Kes ini berfungsi sebagai contoh pengesahan penting:** skor berdekatan graf TxGNN yang tinggi tidak menjamin keberkesanan terapeutik. Model mungkin memberikan skor tinggi berdasarkan pengelompokan nod penyakit dimediasi imun, dan bukannya menangkap keperluan mekanik tertentu bagi setiap penyakit.

**Untuk terus, yang berikut diperlukan:**
- ❌ **Dermatitis**: Tiada pembangunan lanjut dijustifikasi — bukti Fasa 2 negatif pasti
- ⏸️ **Trombositopenia (ITP)**: Memerlukan bukti pra-klinikal bagi penglibatan eosinofil dalam patogenesis ITP sebelum sebarang penerokaan klinikal dapat dijustifikasi
- ⏸️ **Acne keloid / Dermatomyositis**: Memerlukan sains asas menetapkan peranan eosinofil/IL-5Rα dalam patogenesis
- 📋 **Umum**: Perolehi sisipan pakej NPRA untuk profil keselamatan lengkap (Jurang Data DG001); perolehi data MOA terperinci daripada DrugBank (Jurang Data DG002)
- 👁️ **Pantau**: NCT06734884 (benralizumab dalam DRESS) — jika positif, mungkin buka semula perbincangan bagi keadaan dermatologi didorong eosinofil yang berbeza daripada AD

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

