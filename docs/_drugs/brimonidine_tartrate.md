---
layout: default
title: Brimonidine Tartrate
parent: Low Evidence (L4-L5)
nav_order: 160
evidence_level: L5
indication_count: 0
---

# Brimonidine Tartrate
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

# Brimonidine Tartrate: Penilaian Pengunaan Semula Ubat — Data Tidak Mencukupi untuk Ramalan

## Ringkasan Satu Ayat

Brimonidine tartrate ialah agonis adrenergik alfa-2 yang digunakan secara meluas untuk merawat glaukoma dan hipertensi okular. Model TxGNN **tidak menghasilkan sebarang indikasi baru yang diramal** untuk ubat ini, dan medan data utama (DrugBank ID, MOA, teks indikasi yang diluluskan, data keselamatan) kekal kosong. Laporan ini berfungsi sebagai **penilaian jurang data** untuk membimbing langkah seterusnya dalam melengkapkan pakej bukti.

---

## Ringkasan Cepat

| Item | Kandungan |
|------|------|
| Indikasi Asal | *(Data tidak disediakan dalam pakej bukti — diketahui secara klinikal untuk glaukoma / hipertensi okular)* |
| Indikasi Baru yang Diramal | **Tiada** — TxGNN mengembalikan tiada ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **L5** (Tiada ramalan, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan Dihasilkan?

Brimonidine tartrate ialah agonis reseptor adrenergik alfa-2 terpilih. Ia mengurangkan pengeluaran humor akueus dan meningkatkan aliran uveosklerа, dengan itu menurunkan tekanan intraokular. Ia juga tersedia dalam formulasi derma topikal untuk merawat eritema wajah yang berterusan yang berkaitan dengan rosasea.

Model TxGNN mengembalikan tatasusunan `predicted_indications` yang kosong, yang biasanya menunjukkan satu atau lebih isu berikut:

1. **Pemetaan DrugBank ID yang hilang** — Pakej bukti menunjukkan `drugbank_id: null`. Tanpa pengenalan DrugBank yang sah, ubat tidak boleh ditemui dalam graf pengetahuan TxGNN (`node.csv`), dan tiada calon pengunaan semula boleh diberi skor. Log pertanyaan menunjukkan pertanyaan DrugBank mengembalikan 1 hasil, tetapi ID tidak diisi ke dalam pakej bukti.

2. **Data hulu yang tidak lengkap** — Tatasusunan `original_indications` adalah kosong dan semua rekod lesen mempunyai medan kosong, menunjukkan bahawa pengekstrakan data NPRA tidak berjaya menghuraikan medan berstruktur untuk ubat ini.

3. **Batasan laluan topikal/oftalmik** — Brimonidine digunakan terutamanya sebagai agen oftalmik atau topikal. Graf pengetahuan TxGNN mungkin mempunyai perwakilan terbatas bagi ubat yang bertindak secara setempat berbanding terapeutik sistemik.

Sehingga DrugBank ID diselesaikan dan ubat berjaya dipetakan ke dalam graf pengetahuan, tiada ramalan pengunaan semula boleh dihasilkan.

---

## Bukti Ujian Klinikal

Tiada indikasi yang diramal tersedia; oleh itu, tiada carian ujian klinikal yang bertujuan dijalankan.

---

## Bukti Kesusasteraan

Tiada indikasi yang diramal tersedia; oleh itu, tiada carian kesusasteraan yang bertujuan dijalankan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Nota:** 9 pendaftaran telah dikenalpasti oleh pertanyaan NPRA, tetapi butiran lesen berstruktur (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak diisi dalam pakej bukti. Data NPRA mentah perlu diekstrak semula dan diurai.

---

## Pertimbangan Keselamatan

> Sila rujuk pamflet pakej untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) sedang tidak diisi dalam pakej bukti.

---

## Ringkasan Jurang Data

Jurang kritikal berikut mesti diselesaikan sebelum calon ini boleh maju:

| ID Jurang | Item | Tahap Keterukan | Kesan | Pemulihan |
|--------|------|----------|--------|-------------|
| DG001 | Amaran pamflet pakej & kontraindikasi | **Menghalang** | Tidak boleh memasuki saringan keselamatan S1 | Muat turun PDF pamflet pakej daripada NPRA/TFDA dan urai |
| DG002 | Mekanisme Tindakan (MOA) | Tinggi | Mempengaruhi analisis keberkaitan mekanistik | Pertanyaan API DrugBank (1 hasil sudah ditemui) |
| — | DrugBank ID | **Menghalang** | Tidak boleh menjalankan ramalan TxGNN tanpa nod KG | Petakan daripada hasil pertanyaan DrugBank (DB00484) |
| — | Butiran lesen NPRA | Tinggi | Bahagian maklumat pasaran adalah kosong | Ekstrak semula medan berstruktur daripada medan indikasi yang diluluskan NPRA |
| — | Teks indikasi asal | Tinggi | Tidak boleh menetapkan garis asas untuk logik pengunaan semula | Urai daripada medan indikasi yang diluluskan NPRA |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pakej bukti tidak lengkap secara kritikal — tiada pemetaan DrugBank ID, tiada butiran lesen yang diurai, tiada data keselamatan, dan akibatnya tiada ramalan TxGNN dihasilkan. Maklumat tidak mencukupi untuk menilai sebarang peluang pengunaan semula pada ketika ini.

**Untuk meneruskan, berikut diperlukan:**
- **Selesaikan pemetaan DrugBank ID** — Log pertanyaan menunjukkan 1 hasil DrugBank ditemui; isi `drugbank_id` (mungkin **DB00484** untuk brimonidine) dan jalankan semula ramalan TxGNN
- **Ekstrak semula data lesen NPRA** — Urai nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk semua 9 pendaftaran
- **Perolehi pamflet pakej** — Muat turun dan urai amaran, kontraindikasi, dan maklumat interaksi ubat
- **Pertanyaan API DrugBank untuk MOA** — Perolehi mekanisme tindakan, farmakodinamik, dan data toksisiti
- **Jalankan semula saluran paip TxGNN** — Selepas DrugBank ID dipetakan, jalankan `run_kg_prediction.py` untuk menghasilkan calon pengunaan semula

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

