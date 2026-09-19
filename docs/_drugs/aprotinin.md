---
layout: default
title: Aprotinin
parent: Low Evidence (L4-L5)
nav_order: 83
evidence_level: L5
indication_count: 0
---

# Aprotinin
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

# Aprotinin: Penilaian Kembali Guna Ubat — Tiada Ramalan TxGNN Tersedia

## Ringkasan Satu Ayat

Aprotinin (DrugBank: DB06692) adalah penyekat protease serin yang secara klasik digunakan sebagai ejen antifibrinolitik untuk mengurangkan kehilangan darah perioperatif dalam pembedahan jantung.
Walau bagaimanapun, **pakej bukti semasa tidak mengandungi sebarang petunjuk baru yang diramalkan oleh TxGNN**, dan medan data kritikal termasuk mekanisme tindakan, amaran sisipan pakej, dan teks petunjuk yang diluluskan semuanya hilang.
Laporan ini berfungsi sebagai **penilaian jurang data** daripada penilaian kembali guna penuh; tiada cadangan boleh dibuat sehingga jurang yang dikenal pasti diselesaikan.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak tersedia dalam Pakej Bukti semasa |
| Petunjuk Baru yang Diramalkan | Tiada — ramalan TxGNN belum selesai |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 (Ramalan model sahaja — tetapi tiada ramalan wujud) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan Tersedia

Tatasusunan `predicted_indications` dalam Pakej Bukti ini adalah **kosong**, bermakna TxGNN sama ada belum memproses calon ini, atau kemasukan DrugBank Aprotinin (DB06692) tidak dapat berjaya dipautkan ke graf pengetahuan untuk pemeringkatan.

Dua jurang data hulu kritikal menyekat aliran kerja kembali guna penuh:

1. **Mekanisme Tindakan (MOA)** — diklasifikasikan sebagai keterukan **Tinggi**. Tanpa data MOA, graf pengetahuan tidak dapat dengan betul menambat profil farmakologi Aprotinin ke nod penyakit, yang secara langsung merosot kualiti sebarang pemeringkatan TxGNN.

2. **Amaran Sisipan Pakej TFDA dan Kontaindikasi** — diklasifikasikan sebagai keterukan **Menyekat**. Ini menghalang pula penyaringan keselamatan asas (peringkat S1), bermakna calon tidak boleh diteruskan ke semakan kebolehlaksanaan klinikal.

Sehingga dua jurang ini diselesaikan, tiada nisbah mekanis, jadual bukti ujikaji klinikal, atau jadual bukti kesusasteraan boleh dijana dengan bermakna untuk sasaran kembali guna.

---

## Maklumat Pasaran Malaysia

Butiran pendaftaran dalam Pakej Bukti adalah tidak lengkap — semua medan (nombor lesen, nama produk, bentuk dos, pengeluar, teks petunjuk yang diluluskan) kosong walaupun 2 lesen berdaftar direkodkan.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------------------|-------------|-----------|--------------------------|
| (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) |
| (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) |

> **Tindakan Diperlukan:** Ambil butiran lesen penuh daripada daftar produk NPRA Malaysia untuk mengisi jadual ini.

---

## Pertimbangan Keselamatan

Semua medan keselamatan dalam Pakej Bukti semasa tidak mengandungi data yang boleh digunakan:

- Amaran utama: tidak diambil
- Kontaindikasi: tidak diambil
- Interaksi ubat-ubatan: pertanyaan mengembalikan 0 keputusan (`not_found`)

> Sila rujuk sisipan pakej yang diluluskan untuk maklumat keselamatan. Ambil perhatian bahawa Aprotinin mempunyai sejarah keselamatan pasca-pasaran yang ketara di bidang kuasa lain (termasuk penarikan pasaran di beberapa negara disebabkan peristiwa buruk kardiovaskular dan ginjal) — sejarah pengawalseliaan ini mesti dikaji sebelum sebarang penilaian kembali guna diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pakej Bukti secara keseluruhan tidak lengkap — tiada ramalan TxGNN, tiada MOA, tiada data keselamatan, dan tiada teks petunjuk yang diluluskan — menjadikan mustahil untuk menilai potensi kembali guna Aprotinin pada masa ini.

**Untuk diteruskan, perkara berikut diperlukan:**

- **[Menyekat — DG001]** Muat turun dan urai PDF sisipan pakej TFDA untuk mengekstrak amaran, kontaindikasi, dan teks petunjuk yang diluluskan; jalankan semula pintu penurasan keselamatan peringkat S1
- **[Tinggi — DG002]** Pertanyaan API DrugBank untuk DB06692 untuk mendapatkan mekanisme tindakan, kategori ubat, dan profil ketoksikan; gunakan ini untuk menjalankan semula pemetaan KG TxGNN
- **[Diperlukan]** Sahkan sama ada nod DrugBank Aprotinin dengan betul hadir dalam `data/node.csv` dan `data/kg.csv`; jika hilang atau salah dikenal pasti, langkah ramalan KG akan tidak menghasilkan keluaran
- **[Diperlukan]** Ambil butiran lesen NPRA penuh (nombor lesen, nama produk, bentuk dos, teks petunjuk) untuk kedua-dua produk berdaftar
- **[Diperlukan]** Siasat status pengawalseliaan Aprotinin di peringkat antarabangsa (ditangguhkan/ditarik di EU dan Canada sejak 2007–2008 disebabkan penemuan percubaan BART) dan nilai sama ada pendaftaran Malaysia 2 tetap aktif dan sesuai secara klinikal
- **[Pilihan]** Setelah MOA disahkan, sahkan secara manual sama ada Aprotinin muncul dalam sebarang kesusasteraan kembali guna (cth., anti-radang, angioedema herediter, pankreatitis) untuk melengkapi saluran paip TxGNN

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

