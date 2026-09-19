---
layout: default
title: Bisacodyl
parent: Low Evidence (L4-L5)
nav_order: 148
evidence_level: L5
indication_count: 0
---

# Bisacodyl
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

# Bisacodyl: Laporan Penilaian Pengguna Semula Ubat

## Ringkasan Satu Ayat

Bisacodyl ialah pencahar perangsang yang digunakan secara meluas untuk melegakan sembelit dan penyediaan usus sebelum prosedur perubatan. Model TxGNN **tidak menjana sebarang petunjuk baharu yang dijangka** untuk ubat ini. Digabungkan dengan jurang data kritikal yang banyak (MOA, amaran keselamatan, teks petunjuk yang diluluskan), calon ini **tidak boleh meneruskan** ke penilaian lanjutan pada masa ini.

---

## Gambaran Pantas

| Perkara | Kandungan |
|------|------|
| Petunjuk Asal | Sembelit / Penyediaan usus (teks lesen tidak tersedia dalam pakej data) |
| Petunjuk Baharu yang Dijangka | **Tiada** — tiada ramalan yang dijana oleh TxGNN |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | **L5** (Tiada output ramalan model, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 13 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan Dijana?

Bisacodyl (DrugBank: DB09020) ialah terbitan difenilmetan yang bertindak sebagai pencahar perangsang. Ia berfungsi secara tempatan pada mukosa kolon dengan merangsang peristaltis dan menggalakkan pengumpulan air dan elektrolit dalam lumen usus. Tindakannya yang farmakologi adalah terutamanya tempatan dan sempit dari segi mekanik — terbatas kepada peningkatan motiliti usus.

Terdapat beberapa sebab yang mungkin mengapa graf pengetahuan TxGNN tidak menghasilkan calon pengguna semula untuk Bisacodyl:

1. **Aktiviti farmakologi sistemik yang terbatas.** Bisacodyl bertindak hampir eksklusif pada saluran gastrointestinal dan mempunyai penyerapan sistemik yang minimum. Ubat-ubatan dengan mekanisme bertindak secara tempatan yang sempit kurang berkemungkinan mempunyai sambungan yang munasabah kepada nod penyakit yang jauh dalam graf pengetahuan.

2. **Data interaksi molekul yang jarang.** Sebagai pencahar OTC dengan mekanisme yang telah dicirikan dengan baik dan mudah, Bisacodyl mempunyai lebih sedikit sasaran molekul yang direkodkan, interaksi protein, dan sambungan laluan dalam pangkalan data seperti DrugBank — mengakibatkan lebih sedikit tepi dalam graf pengetahuan untuk model melintasi.

3. **Data MOA yang hilang dalam pakej bukti ini.** Medan MOA ditandai sebagai jurang data, yang mungkin telah mengehadkan lagi keupayaan model untuk mengenal pasti pertindihan mekanik dengan petunjuk penyakit lain.

---

## Bukti Percubaan Klinikal

Tiada petunjuk yang dijangka dijana; oleh itu, tiada carian percubaan klinikal yang disasarkan dilakukan.

> Pada masa ini tiada percubaan klinikal yang berkaitan untuk dilaporkan bagi calon pengguna semula.

---

## Bukti Kesusasteraan

Tiada petunjuk yang dijangka dijana; oleh itu, tiada carian kesusasteraan yang disasarkan dilakukan.

> Pada masa ini tiada kesusasteraan yang berkaitan untuk dilaporkan bagi calon pengguna semula.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------|------|------|------|
| *(tidak tersedia)* | *(tidak tersedia)* | *(tidak tersedia)* | *(tidak tersedia)* |

> **Nota:** 13 pendaftaran telah dikenal pasti melalui pertanyaan NPRA (dipertanyakan 2026-03-27), tetapi maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak diisi dalam pakej bukti. Jurang data ini harus diperbaiki dengan membuat pertanyaan semula kepada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> Semua medan keselamatan (amaran utama, kontraindikasi, dan interaksi ubat-ubatan) dikembalikan sebagai jurang data atau tidak ditemui. Sebelum sebarang penilaian pengguna semula dapat diteruskan, perkara berikut mesti diperoleh:
> - Amaran dan langkah berjaga-jaga sisipan pakej
> - Senarai kontraindikasi
> - Profil interaksi ubat-ubatan

---

## Ringkasan Jurang Data

| ID Jurang | Perkara | Keseriusan | Kesan | Pemulihan |
|------|------|------|------|------|
| DG001 | Amaran Sisipan Pakej TFDA / Kontraindikasi | **Menghalang** | Tidak boleh memasuki penilaian awal keselamatan S1 | Muat turun dan analisis PDF sisipan pakej dari laman web TFDA |
| DG002 | Mekanisme Tindakan (MOA) | **Tinggi** | Mempengaruhi analisis keberkaitan mekanisme | Pertanyaan API DrugBank |
| — | Butiran lesen (semua 13 pendaftaran) | Tinggi | Tidak boleh mengesahkan teks petunjuk yang diluluskan atau bentuk dos | Pertanyaan semula NPRA dengan pengekstrakan medan penuh |
| — | Petunjuk yang dijangka | Kritikal | Tiada calon pengguna semula untuk dinilai | Sahkan pemetaan nod KG; sahkan nod Bisacodyl wujud dalam graf TxGNN |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Model TxGNN tidak menjana sebarang ramalan pengguna semula untuk Bisacodyl. Sebagai tambahan, jurang data kritikal yang banyak (MOA, profil keselamatan, butiran lesen) tetap tidak diselesaikan. Tiada isyarat pengguna semula yang boleh ditindaklanjuti untuk dinilai pada masa ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Sahkan bahawa Bisacodyl (DB09020) dipetakan dengan betul sebagai nod dalam graf pengetahuan TxGNN, dan sahkan sambungan tepi
- Pulihkan **DG001** (Menghalang): Dapatkan amaran sisipan pakej dan kontraindikasi
- Pulihkan **DG002** (Tinggi): Ambil data MOA dari API DrugBank
- Ekstrak semula butiran lesen penuh dari pangkalan data NPRA bagi semua 13 pendaftaran
- Jika nod ubat disahkan dalam KG dengan sambungan yang mencukupi, jalankan semula saluran pipa ramalan TxGNN dan nilai semula

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon ubat pengguna semula mesti menjalani pengesahan klinikal yang ketat sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

