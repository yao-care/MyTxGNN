---
layout: default
title: Aspirin
parent: Low Evidence (L4-L5)
nav_order: 95
evidence_level: L5
indication_count: 0
---

# Aspirin
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

# ASPIRIN: Penilaian Penggunaan Semula Ubat (Tiada Ramalan Tersedia)

## Ringkasan Satu Ayat

Aspirin (asid asetilsalilik) adalah agen analgesik, antipiretik, dan anti-inflamasi yang digunakan secara meluas dengan aplikasi kardiovaskular yang terbukti, disahkan sebagai dipasarkan di Malaysia dengan 22 produk terdaftar.
Walau bagaimanapun, **tiada petunjuk ramalan TxGNN** terdapat dalam bungkus bukti ini, dan data kritikal termasuk mekanisme tindakan, butiran lesen individu, dan profil keselamatan adalah tidak ada.
**Laporan ini mencerminkan penilaian yang tidak lengkap; pengambilan data tambahan diperlukan sebelum sebarang keputusan penggunaan semula boleh dibuat.**

---

## Gambaran Pantas

| Perkara | Kandungan |
|---------|-----------|
| Petunjuk Asal | Tidak dinyatakan dalam data pendaftaran |
| Petunjuk Baharu Ramalan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A — tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 22 |
| Keputusan Disyorkan | **Tahan** |

---

## Sebab Tiada Ramalan Tersedia

Saluran paip ramalan TxGNN tidak mengembalikan sebarang cadangan petunjuk untuk Aspirin dalam bungkus bukti ini. Ini kemungkinan besar disebabkan oleh satu atau lebih daripada kegagalan hiliran berikut:

1. **DrugBank ID hilang** — Tanpa DrugBank ID yang disahkan, ubat tidak boleh dipetakan ke nod dalam graf pengetahuan TxGNN, menghalang semua penilaian berbasis KG dan DL seterusnya.
2. **Pemetaan penyakit mungkin tidak lengkap** — Jika medan teks petunjuk yang diluluskan kosong (seperti yang ada di sini), langkah normalisasi penyakit tidak dapat menghasilkan nod benih untuk traversal graf penggunaan semula.
3. **Pengambilan data adalah separa** — Log pertanyaan mengesahkan bahawa NPRA mengembalikan 22 rekod dan DrugBank mengembalikan 1 hasil, tetapi medan berstruktur tidak diisi ke dalam bungkus bukti, mencadangkan jurang penghuraian atau integrasi.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia. Berdasarkan farmakologi yang diterbitkan secara meluas, Aspirin menghalang secara tidak boleh balik enzim COX-1 dan COX-2, mengurangkan sintesis prostaglandin. Ini menjadikannya secara mekanis munasabah untuk penggunaan semula ke dalam konteks inflamasi, trombotik, dan berpotensi onkologi. Walau bagaimanapun, maklumat ini belum ditangkap secara formal dalam bungkus bukti semasa dan tidak boleh digunakan untuk penilaian berstruktur sehingga rekod DrugBank diintegrasikan.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal yang berkaitan didaftarkan.

*(Tiada ramalan petunjuk tersedia dalam bungkus bukti ini, jadi tiada bukti ujian khusus petunjuk boleh dipaparkan.)*

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan tersedia.

*(Tiada ramalan petunjuk tersedia dalam bungkus bukti ini, jadi tiada bukti kesusasteraan khusus petunjuk boleh dipaparkan.)*

---

## Maklumat Pasaran Malaysia

22 kebenaran produk disahkan untuk Aspirin di Malaysia melalui pertanyaan NPRA. Walau bagaimanapun, butiran lesen individu (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) tidak diambil dalam bungkus bukti ini dan oleh itu tidak tersedia untuk tabulasi.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------------------|------------|-----------|------------------------|
| — | Tidak diambil | Tidak diambil | Tidak diambil |

> **Nota:** Pertanyaan NPRA mengembalikan 22 rekod (ID pertanyaan 1, status: berjaya), tetapi medan berstruktur dalam semua 22 catatan lesen adalah kosong. Satu tarikan data tambahan diperlukan untuk mengisi jadual ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Bungkus bukti ini tidak mengandungi sebarang petunjuk ramalan TxGNN dan hilang semua medan data kritikal — mekanisme tindakan, butiran lesen individu, amaran keselamatan, dan kontraindikasi — menjadikannya mustahil untuk menjalankan penilaian penggunaan semula ubat yang bermakna pada tahap ini.

**Untuk meneruskan, berikut diperlukan:**

- **Jalankan semula saluran paip TxGNN** selepas menyelesaikan isu pemetaan DrugBank ID, supaya cadangan petunjuk dapat dijana
- **Ambil rekod DrugBank** (log pertanyaan mengesahkan 1 hasil ditemui) untuk mengisi DrugBank ID, MOA, kategori farmakologi, dan data keselamatan
- **Huraikan PDF NPRA/sisipan pakej** untuk mengisi 22 catatan lesen dengan nama produk, bentuk dos, dan teks petunjuk yang diluluskan (menangani jurang data DG001)
- **Selesaikan jurang data MOA** (DG002) melalui API DrugBank untuk memungkinkan analisis plausibiliti mekanis
- **Jalankan penapisan DDI** setelah DrugBank ID disahkan dan medan keselamatan diisi
- **Menilai semula tahap bukti** setelah petunjuk ramalan dan bukti sokongan tersedia

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

