---
layout: default
title: Digoxin
parent: Low Evidence (L4-L5)
nav_order: 280
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **6** 
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

# Digoxin: Daripada Kegagalan Jantung/Fibrilasi Atrium kepada Angina Prinzmetal

## Ringkasan Satu Ayat

Digoxin ialah glikosida jantung yang digunakan secara bersejarah untuk kegagalan jantung dan fibrilasi/flutter atrium, bertindak dengan menghambat pam Na⁺/K⁺-ATPase untuk meningkatkan kontraktiliti jantung dan memperlahankan penghantaran nod AV. Model TxGNN meramalkan ia mungkin berkesan untuk **Angina Prinzmetal** (angina vasospastik), tetapi analisis mekanistik mencadangkan ini mewakili **hubungan terbalik** — digoxin sebenarnya mungkin memburukkan vasospasma koroner. Pada masa ini, **0 uji klinikal** dan hanya **2 penerbitan yang terhubung secara tangensial** wujud, memberikan pada dasarnya tiada bukti sokongan.

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Kegagalan jantung, fibrilasi/flutter atrium (butiran lesen masih belum ada) |
| Indikasi Baru Diprediksi | Angina Prinzmetal |
| Skor Ramalan TxGNN | 99.81% |
| Tahap Bukti | L4 (Hanya analisis mekanistik — terang kontra-indikatif) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 4 |
| Keputusan yang Disyorkan | **Tahan** |

## Mengapa Ramalan Ini Munasabah?

Digoxin ialah glikosida jantung yang menghambat Na⁺/K⁺-ATPase pada sel miokard dan sel otot polos vaskular, membawa kepada peningkatan kalsium intrasel melalui pertukaran Na⁺/Ca²⁺. Dalam kegagalan jantung, ketersediaan kalsium yang ditingkatkan ini meningkatkan kontraktiliti jantung (kesan inotropik positif). Dalam fibrilasi atrium, tindakan vagotonik digoxin memperlahankan penghantaran nod AV, mengawal laju ventrikel.

Angina Prinzmetal (angina varian) disebabkan oleh vasospasma arteri koroner sementara, membawa kepada peningkatan ST dan nyeri dada biasanya semasa rehat. Rawatan standard — penyekat saluran kalsium dan nitrat — berfungsi dengan melonggarkan otot polos vaskular dan mengurangkan kalsium intrasel. **Mekanisme digoxin bertindak dalam arah bertentangan**: dengan menghambat Na⁺/K⁺-ATPase dalam otot polos vaskular, digoxin meningkatkan Ca²⁺ intrasel, yang secara teorinya akan **menggalakkan** vasospasma koroner daripada melegakan ia. Secara klinikal, penggunaan digoxin pada pesakit dengan vasospasma koroner dianggap kontraindikasi relatif.

Skor TxGNN yang tinggi (99.81%) mungkin mencerminkan proksimiti tahap graf yang kuat antara digoxin dan penyakit kardiovaskular dalam graf pengetahuan, daripada hubungan terapeutik tulen. Ini adalah batasan terkenal bagi model repurposing ubat berasaskan graf: ketersambungan tinggi dalam domain penyakit dapat menghasilkan ramalan 'rawatan' palsu yang sebenarnya adalah hubungan yang berbahaya. **Ramalan ini harus diperlakukan sebagai contoh peringatan terhadap keluaran model yang memerlukan semakan farmakologi pakar.**

## Bukti Uji Klinikal

Pada masa ini tiada uji klinikal berkaitan yang terdaftar untuk digoxin dalam angina Prinzmetal.

## Bukti Kesusasteraan

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|--------|----------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Ulasan | Acta Physiol Pharmacol Bulg | Ulasan farmakologi kronologi dan ritma sirkadian dalam rawatan antihipertensi; tidak mempertimbangkan digoxin untuk angina vasospastik secara langsung |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Ulasan | Chin Med Sci J | Penilaian semula mekanisme angina decubitus pada 30 pesakit; membincangkan pemantauan hemodinamik tetapi tidak menyokong digoxin sebagai rawatan untuk angina vasospastik |

> **Nota:** Tiada penerbitan memberikan bukti langsung untuk penggunaan digoxin dalam angina Prinzmetal. Kesusasteraan terhubung secara tangensial dengan farmakologi kardiovaskular tetapi tidak menyokong ubat indikasi baru.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|---------|------|------|-----------|
| (Butiran masih belum ada) | — | — | — |
| (Butiran masih belum ada) | — | — | — |
| (Butiran masih belum ada) | — | — | — |
| (Butiran masih belum ada) | — | — | — |

> 4 pendaftaran terdapat dalam rekod di Malaysia, tetapi maklumat lesen terperinci (nama produk, bentuk dos, indikasi yang diluluskan) tidak tersedia pada potong data. Sila rujuk pangkalan data NPRA untuk butiran pendaftaran lengkap.

## Pertimbangan Keselamatan

> Sila rujuk risalah ubat untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti ini.
>
> **Nota farmakovigilans penting untuk calon ubat indikasi baru khusus ini:** Digoxin diketahui mempunyai indeks terapeutik yang sempit. Dalam konteks angina Prinzmetal, mekanisme digoxin yang meningkatkan Ca²⁺ intrasel dalam otot polos vaskular menimbulkan **risiko berpotensi memperburukkan vasospasma koroner**. Ini mewakili isyarat keselamatan terhadap, bukannya memihak, arah ubat indikasi baru ini.

## Indikasi Diprediksi Tambahan (Kedudukan 2–6)

Semua ramalan TxGNN tambahan untuk digoxin telah dinilai dan menerima cadangan **Tahan** kerana kekurangan rasional mekanistik dan ketiadaan bukti klinikal:

| Kedudukan | Indikasi Diprediksi | Skor TxGNN | Tahap Bukti | Kebimbangan Utama |
|------|--------|----------|--------|---------|
| 2 | Halangan duodenum | 99.70% | L5 | Patalogi mekanikal; tiada rasional farmakoloji. Hanya 1 laporan kes yang tidak berkaitan. |
| 3 | Ulser duodenum | 99.59% | L5 | Penyakit berasaskan asid/H. pylori; toksisiti GI digoxin mungkin memburukkan simptom. Kesusasteraan menerangkan interaksi ubat/toksisiti, bukan penggunaan terapeutik. |
| 4 | Refluk duodenogastrik | 99.53% | L5 | Gangguan motiliti GI; kesan GI vagotonik digoxin adalah buruk, bukan terapeutik. Tiada kesusasteraan. |
| 5 | Kerentanan kepada strok iskemik (istilah usang) | 99.29% | L5 | Istilah ontologi usang; bukti mencadangkan digoxin **meningkatkan** risiko strok (OR 1.2–1.6). |
| 6 | Hipoalfalipoproteinemia | 99.20% | L5 | Gangguan metabolisme lipid; tiada persilangan terkenal dengan perencatan Na⁺/K⁺-ATPase. Tiada bukti. |

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tahan**

**Rasional:**
Ramalan teratas (angina Prinzmetal) mewakili **kontraindikasi farmakologi** daripada peluang terapeutik — mekanisme digoxin yang meningkatkan kalsium intrasel dalam otot polos vaskular secara teorinya akan memperburukkan vasospasma koroner. Kesemua enam indikasi yang diprediksi tidak mempunyai sokongan uji klinikal, dan kesusasteraan sedia ada tidak mengesahkan sebarang aplikasi terapeutik. Skor TxGNN yang seragam tinggi merentasi domain penyakit yang tidak berkaitan (jantung, GI, serebrovaskular, metabolik) mencadangkan model menangkap jejak farmakologi digoxin yang luas dalam graf pengetahuan daripada mengenal pasti calon ubat indikasi baru tulen.

**Untuk meneruskan, perkara berikut diperlukan:**
- Kajian mekanisme tindakan terperinci daripada DrugBank untuk mengesahkan atau menyangkal sebarang kesan sasaran luar yang boleh relevan secara terapeutik
- Data keselamatan risalah ubat (amaran utama, kontraindikasi, DDI) untuk penilaian risiko komprehensif
- Butiran pendaftaran Malaysia lengkap (data lesen NPRA)
- Jika sebarang indikasi maju, bukti praklinik mekanisme terapeutik yang munasabah diperlukan sebelum pertimbangan klinikal

---

> *Penafian: Laporan ini hanya untuk rujukan penyelidikan dan tidak merupakan nasihat perubatan. Calon ubat indikasi baru memerlukan pengesahan klinikal yang ketat sebelum sebarang aplikasi terapeutik. Ramalan model TxGNN harus ditafsirkan bersama-sama dengan ulasan pakar farmakologi dan klinikal.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

