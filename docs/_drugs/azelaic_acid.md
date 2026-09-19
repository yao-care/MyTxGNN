---
layout: default
title: Azelaic Acid
parent: Low Evidence (L4-L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Azelaic Acid
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

# Azelaic Acid: Agen Dermatologi — Tiada Petunjuk Baru Diramal

## Ringkasan Satu Ayat

Azelaic Acid adalah asid dikarboksilik yang berlaku semula jadi yang biasa digunakan dalam dermatologi untuk rawatan jerawat vulgaris dan rosacea. Model TxGNN **tidak menghasilkan sebarang petunjuk penggunaan semula** untuk ubat ini, bermakna pada masa ini tiada petunjuk baru yang dicadangkan secara pengiraan. Pengkayaan data yang lebih lanjut (mekanisme tindakan, butir-butir kawal selia) diperlukan sebelum penilaian semula.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Penggunaan dermatologi (jerawat, rosacea — berdasarkan farmakologi yang diketahui; teks petunjuk yang diluluskan khusus tidak tersedia dalam set data) |
| Petunjuk Baru yang Diramal | **Tiada** — tiada ramalan TxGNN yang dijana |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | **T/A** — tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tangguh** |

---

## Mengapa Tiada Ramalan yang Dijana?

Azelaic Acid (DrugBank ID: DB00548) ialah asid dikarboksilik dengan sifat antibakteria, keratolitik, anti-radang, dan perencat tirosinase yang diketahui. Ia digunakan terutamanya sebagai agen topikal untuk jerawat vulgaris, rosacea, dan gangguan hiperpigmentasi.

Model TxGNN tidak menghasilkan sebarang calon penggunaan semula untuk ubat ini. Beberapa faktor mungkin menjelaskan perkara ini:

1. **Profil penggunaan topikal sahaja**: Azelaic Acid digunakan terutamanya secara topikal, yang menghadkan interaksi farmakologi sistemik yang ditangkap oleh graf pengetahuan. Rangkaian hubungan ubat-penyakit TxGNN mungkin tidak memadai mewakili kesan terapeutik khusus laluan topikal.

2. **Data mekanisme tindakan yang hilang**: Medan MOA adalah hilang daripada set data semasa. Tanpa anotasi sasaran-laluan eksplisit dalam graf pengetahuan, keupayaan model untuk menginferkan persatuan penyakit baru berkurangan.

3. **Keterhubungan graf pengetahuan yang terhad**: Jika Azelaic Acid mempunyai beberapa tepi sahaja (ubat-sasaran, ubat-penyakit, ubat-ubat) dalam rangkaian graf asas, rangkaian saraf graf mempunyai isyarat yang tidak mencukupi untuk menghasilkan ramalan keyakinan tinggi.

---

## Bukti Uji Klinis

Tiada petunjuk yang diramal; oleh itu, tiada carian uji klinis yang disasarkan telah dilakukan.

---

## Bukti Kesusasteraan

Tiada petunjuk yang diramal; oleh itu, tiada carian kesusasteraan yang disasarkan telah dilakukan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk Diluluskan |
|------|------|------|------|
| *(Tidak tersedia dalam set data)* | *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* |

> **Nota:** Pertanyaan NPRA mengesahkan 2 pendaftaran untuk Azelaic Acid di Malaysia, tetapi maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) tidak ditangkap dalam set data semasa. Sila semak [Carian Produk NPRA](https://quest3plus.bpfk.gov.my/pmo/index.php) untuk butir-butir pendaftaran yang lengkap.

---

## Pertimbangan Keselamatan

> Sila rujuk lembaran maklumat paket untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat-ubatan tidak tersedia dalam set data semasa.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguh**

**Alasan:**
Model TxGNN tidak menghasilkan sebarang petunjuk penggunaan semula untuk Azelaic Acid. Tanpa petunjuk calon, tiada hipotesis penggunaan semula yang boleh ditindaklanjuti untuk dinilai pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **Data mekanisme tindakan (MOA)** — Tanya API DrugBank untuk mendapatkan anotasi sasaran dan laluan, yang akan memperkaya perwakilan Azelaic Acid dalam graf pengetahuan
- **Butir-butir kawal selia Malaysia yang lengkap** — Ambil maklumat lesen NPRA penuh termasuk nama produk, bentuk dos, dan teks petunjuk yang diluluskan
- **Data keselamatan lembaran maklumat paket** — Dapatkan amaran utama, kontraindikasi, dan berhati-hati daripada pelabelan produk yang diluluskan
- **Semakan keterhubungan graf pengetahuan** — Sahkan bahawa Azelaic Acid (DB00548) wujud sebagai nod dalam graf pengetahuan TxGNN (`data/kg.csv`) dan menilai jumlah tepinya; jika tiada atau tidak berkaitan dengan baik, ubat tidak dapat dinilai dengan berkesan oleh model
- **Jalankan semula ramalan TxGNN** selepas pengkayaan data untuk menentukan sama ada petunjuk baru muncul

---

*Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan semula ubat memerlukan pengesahan klinis sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

