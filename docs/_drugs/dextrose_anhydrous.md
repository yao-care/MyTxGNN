---
layout: default
title: Dextrose Anhydrous
parent: Low Evidence (L4-L5)
nav_order: 271
evidence_level: L5
indication_count: 0
---

# Dextrose Anhydrous
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **0** 
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

# Dekstrosa Anhidrat: Penilaian Penggunaan Semula Dadah — Tiada Petunjuk Terapeutik Ramalan

## Ringkasan Satu Ayat

Dekstrosa Anhidrat (glukosa anhidrat) ialah agen nutrisi dan metabolik asas yang digunakan secara meluas untuk suplemen kalori, penggantian cecair, dan rawatan hipoglikemia. Model TxGNN telah **tidak menghasilkan sebarang ramalan penggunaan semula** untuk sebatian ini, dan jurang data kritikal (DrugBank ID, mekanisme tindakan, teks petunjuk yang diluluskan) tetap belum diselesaikan.

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak tersedia (teks petunjuk lesen tidak disediakan) |
| Petunjuk Terapeutik Ramalan | **Tiada** — TxGNN tidak mengembalikan sebarang ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 (Tiada ramalan, tiada kajian) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 15 |
| Keputusan Yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan?

Dekstrosa Anhidrat ialah bentuk anhidrat bagi D-glukosa, substrat tenaga utama tubuh. Ia dikelaskan sebagai agen nutrisi bukannya ubat terapeutik yang aktif secara farmakoloji. Peranan klinikal utamanya — terapi cecair intravena, suplemen kalori, pembetulan hipoglikemia, dan penggunaan sebagai bahan tambahan atau kenderaan — tidak melibatkan mekanisme farmakoloji khusus penyakit yang boleh dieksploitasi oleh grafik pengetahuan TxGNN untuk ramalan penggunaan semula.

Selain itu, DrugBank ID untuk sebatian ini tidak diselesaikan dalam saluran paip semasa (`drugbank_id: null`). Tanpa nod DrugBank yang sah, sebatian tidak dapat dipetakan ke dalam grafik pengetahuan TxGNN (yang bergantung pada tepi DrugBank–penyakit daripada `kg.csv`), dan oleh itu tiada skor ramalan dadah–penyakit boleh dikira.

Selain itu, data mekanisme tindakan (MOA) tidak tersedia. Dekstrosa bertindak sebagai sumber kalori yang dimetaboliskan melalui glikolisis dan kitaran asid sitrik; ia tidak memiliki MOA farmakoloji yang disasarkan dalam pengertian konvensional (cth., ikatan reseptor, perencatan enzim), yang seterusnya mengehadkan kecalonnya untuk penggunaan semula berasaskan petunjuk.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan untuk dipaparkan, kerana tiada petunjuk terapeutik baru yang diramalkan oleh TxGNN.

---

## Bukti Kesusasteraan

Pada masa ini tiada bukti kesusasteraan berkaitan untuk dipaparkan, kerana tiada petunjuk terapeutik baru yang diramalkan oleh TxGNN.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk Yang Diluluskan |
|------------------|-------------|-----------|------------------------|
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |

> **Nota:** 15 pendaftaran telah dikenal pasti dalam pangkalan data NPRA untuk Dekstrosa Anhidrat, tetapi rekod lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak diisi dalam bungkus bukti. Jurang data ini harus diperbetulkan dengan membuat pertanyaan semula kepada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, dan interaksi ubat) dikembalikan sebagai jurang data dalam bungkus bukti semasa.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Dekstrosa Anhidrat ialah sebatian nutrisi/metabolik asas tanpa mekanisme farmakoloji yang disasarkan. Model TxGNN menghasilkan sifar ramalan penggunaan semula, dan berbilang jurang data kritikal (DrugBank ID, MOA, teks petunjuk lesen, data keselamatan) tetap belum diselesaikan. Sebatian ini bukan calon yang berdaya maju untuk penilaian penggunaan semula ubat pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**
- **Selesaikan pemetaan DrugBank**: Sahkan sama ada Dekstrosa Anhidrat dipetakan kepada DrugBank ID [DB09341](https://go.drugbank.com/drugs/DB09341) (Glukosa) atau catatan berkaitan, dan jalankan semula saluran paip ramalan KG dengan nod yang betul
- **Isi butiran lesen NPRA**: Buat pertanyaan semula kepada pangkalan data NPRA untuk mendapatkan rekod pendaftaran lengkap (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan)
- **Ambil data keselamatan**: Muat turun dan huraikan sisipan pakej yang berkaitan untuk amaran, kontraindikasi, dan maklumat interaksi ubat
- **Nilai semula kecalonnya**: Jika pemetaan DrugBank berjaya diselesaikan dan sebatian diintegrasikan semula ke dalam grafik pengetahuan, jalankan semula ramalan TxGNN untuk menentukan sama ada sebarang skor petunjuk muncul

> ⚠️ *Laporan ini untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

