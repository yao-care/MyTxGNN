---
layout: default
title: Betahistine Mesylate
parent: Low Evidence (L4-L5)
nav_order: 135
evidence_level: L5
indication_count: 0
---

# Betahistine Mesylate
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

# Betahistine Mesylate: Penilaian Ubat Guna Semula Pendahuluan (Tiada Indikasi Yang Diramalkan)

## Ringkasan Satu Ayat

Betahistine mesylate ialah analog histamin yang biasa digunakan untuk rawatan pening dan penyakit Ménière, pada masa kini dipasarkan di Malaysia dengan 1 pendaftaran. Model TxGNN telah **tidak menghasilkan sebarang indikasi guna semula yang diramalkan** untuk ubat ini, dan jurang data yang kritikal (mekanisme tindakan, profil keselamatan) tetap tidak terselesaikan, menghalang penilaian lanjutan pada masa ini.

## Tinjauan Pantas

| Item | Kandungan |
|------|------|
| Indikasi Asal | Tidak tersedia (data pendaftaran tidak lengkap) |
| Indikasi Guna Semula Yang Diramalkan | **Tiada** — TxGNN tidak menghasilkan sebarang ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan Yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

**Tiada ramalan telah dihasilkan oleh TxGNN untuk Betahistine Mesylate.** Bahagian ini oleh itu membincangkan farmakologi ubat yang diketahui untuk konteks.

Betahistine ialah analog struktur histamin yang bertindak sebagai agonis reseptor H₁ yang lemah dan antagonis reseptor H₃ yang kuat. Dengan menyekat autoresptor H₃ pra-sinapsis, ia meningkatkan turnover dan pelepasan histamin dalam sistem saraf pusat, dengan itu meningkatkan mikrosirkulasi dalam telinga dalam (stria vaskularis) dan memodulasi fungsi vestibular. Ia terutamanya ditetapkan untuk penyakit Ménière dan gejala pening yang berkaitan.

Ketiadaan ramalan TxGNN mungkin disebabkan oleh satu atau lebih faktor: (1) ID DrugBank tidak berjaya dipetakan (`drugbank_id: null`), menghalang ubat daripada ditempatkan dalam graf pengetahuan; (2) betahistine mesylate (bentuk garam tertentu) mungkin tidak hadir sebagai nod tersendiri dalam graf pengetahuan asas TxGNN (yang biasanya menggunakan bentuk asas INN); atau (3) profil farmakologi ubat tidak menghasilkan calon ubat guna semula yang signifikan dari segi statistik di atas ambang keyakinan model. Menyelesaikan pemetaan DrugBank adalah prasyarat untuk sebarang ramalan bermakna.

---

## Bukti Uji Klinis

Pada masa kini tiada uji klinis yang berkaitan dikenal pasti, kerana tiada indikasi yang diramalkan telah dihasilkan.

---

## Bukti Literatur

Pada masa kini tiada literatur yang berkaitan dikenal pasti, kerana tiada indikasi yang diramalkan telah dihasilkan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|------|------|------|------|
| *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* |

> **Nota:** Satu pendaftaran direkodkan dalam pangkalan data, tetapi butiran lesen (nombor kebenaran, nama produk, bentuk dos, dan indikasi yang diluluskan) tidak lengkap. Sila sahkan terus dengan pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk risalah ubat untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat pada masa kini tidak tersedia dalam pakej bukti ini (jurang data dikenal pasti sebagai keparahan yang menghalang).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
TxGNN tidak menghasilkan sebarang ramalan ubat guna semula untuk Betahistine Mesylate, kemungkinan besar disebabkan oleh pemetaan ID DrugBank yang gagal yang menghalang ubat daripada dipasukkan ke dalam graf pengetahuan. Tanpa ramalan yang sah, tiada penilaian ubat guna semula dapat diteruskan.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Selesaikan pemetaan DrugBank** — Cari dalam DrugBank menggunakan INN asas "betahistine" (DB06698) dan bukannya bentuk garam "betahistine mesylate" untuk memperoleh ID DrugBank yang sah dan menghubungkan ubat ke dalam graf pengetahuan
2. **Jalankan semula ramalan TxGNN** — Setelah ID DrugBank dipetakan, jalankan semula saluran paip ramalan KG dan DL untuk menghasilkan calon ubat guna semula
3. **Lengkapkan data pendaftaran NPRA** — Ambil butiran lesen penuh (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) daripada pangkalan data NPRA
4. **Dapatkan profil keselamatan** — Muat turun dan analisis risalah ubat untuk memperoleh amaran utama, kontraindikasi, dan maklumat interaksi ubat (pada masa kini dikenal pasti sebagai jurang data yang menghalang, DG001)
5. **Dapatkan data mekanisme tindakan** — Cari dalam API DrugBank untuk maklumat MOA yang terperinci (jurang data DG002)

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon ubat guna semula memerlukan pengesahan klinis sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

