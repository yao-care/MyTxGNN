---
layout: default
title: Bilastine
parent: Low Evidence (L4-L5)
nav_order: 145
evidence_level: L5
indication_count: 0
---

# Bilastine
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

# Bilastine: Penilaian Repurposing Ubat — Menunggu Ramalan

## Ringkasan Satu Ayat

Bilastine ialah antihistamin H1 generasi kedua yang didaftarkan di Malaysia dengan 5 kelulusan aktif, digunakan terutamanya untuk rawatan simptomatik rinitis alergik dan urtikaria. Model TxGNN **belum menjana sebarang ramalan petunjuk baharu** untuk ubat ini. **Tiada bukti percubaan klinikal atau literatur** telah dikumpulkan untuk calon repurposing, dan jurang data kritikal masih tinggal.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Tidak tersedia dalam data semasa |
| Petunjuk Baharu yang Diramalkan | Tiada (tiada ramalan TxGNN dijana) |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | L5 — Ramalan model belum tersedia |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 5 |
| Keputusan yang Disyorkan | **Tunggu** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan (MOA) terperinci tidak tersedia dalam pakej bukti. Berdasarkan maklumat farmakologi yang diketahui, Bilastine ialah antihistamin H1 generasi kedua, bukan penenang, yang menghalang secara selektif reseptor histamin H1 periferal. Ia digunakan secara klinikal untuk pelepasan simptomatik rinitis alergik konjunktivitis dan urtikaria (gatal-gatal).

Tiada ramalan TxGNN telah dijana untuk Bilastine pada masa ini. Ini mungkin disebabkan oleh pemetaan yang tidak lengkap antara ID DrugBank ubat (DB11591) dan nod dalam graf pengetahuan TxGNN, atau ubat mungkin tidak memenuhi ambang pemarkahan untuk sebarang petunjuk penyakit calon. Tanpa ramalan, tiada penilaian kebolehkepercayaan mekanik dapat dilakukan.

Sebelum penilaian repurposing dapat diteruskan, saluran paip ramalan TxGNN mesti dijalankan semula atau disahkan untuk menentukan mengapa tiada petunjuk calon telah dihasilkan untuk ubat ini.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan yang didaftarkan untuk calon repurposing, kerana tiada petunjuk baharu telah diramalkan.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan tersedia untuk calon repurposing, kerana tiada petunjuk baharu telah diramalkan.

---

## Maklumat Pasaran Malaysia

5 kelulusan dicatat dalam pangkalan data NPRA, tetapi maklumat produk terperinci belum diisi dalam pakej bukti.

| Nombor Kelulusan | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------|------|------|------|
| *(Data menunggu)* | *(Data menunggu)* | *(Data menunggu)* | *(Data menunggu)* |

> **Nota:** Medan butir lesen sedang kosong. Sila ambil maklumat produk penuh daripada [pangkalan data NPRA Quest3+](https://quest3plus.bpfk.gov.my/) untuk melengkapkan bahagian ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> **Jurang Data yang Dikenal Pasti:**
> - Amaran sisipan pakej TFDA/NPRA dan kontraindikasi belum dianalisis (Keterukan: **Menghalang** — tidak dapat meneruskan ke penilaian keselamatan Tahap 1)
> - Data interaksi ubat–ubat tidak ditemui dalam pertanyaan semasa

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Alasan:**
Tiada petunjuk yang diramalkan TxGNN wujud untuk Bilastine pada masa ini, dan pelbagai jurang data yang menghalang mencegah penilaian daripada diteruskan. Pakej bukti kekurangan data MOA, teks petunjuk yang diluluskan, maklumat keselamatan sisipan pakej, dan — yang paling kritikal — sebarang ramalan repurposing untuk dinilai.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Jalankan semula saluran paip ramalan TxGNN** — Sahkan bahawa Bilastine (DB11591) dipetakan dengan betul dalam graf pengetahuan (`node.csv` / `kg.csv`) dan jalankan semula `run_kg_prediction.py` untuk menjana petunjuk calon
2. **Isi butir lesen NPRA** — Ambil nama produk, bentuk dos, dan teks petunjuk yang diluluskan daripada pangkalan data NPRA Quest3+ untuk semua 5 pendaftaran
3. **Dapatkan data MOA** — Soal API DrugBank untuk mekanisme tindakan Bilastine, sasaran, dan farmakodinamik
4. **Analisis sisipan pakej** — Muat turun dan ekstrak amaran, kontraindikasi, dan tindak balas buruk daripada sisipan pakej rasmi (keterukan menghalang — diperlukan untuk penilaian keselamatan Tahap 1)
5. **Soal pangkalan data DDI** — Coba semula carian interaksi ubat–ubat apabila data DrugBank telah disepadukan sepenuhnya

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

