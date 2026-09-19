---
layout: default
title: Bismuth Subgallate
parent: Low Evidence (L4-L5)
nav_order: 149
evidence_level: L5
indication_count: 0
---

# Bismuth Subgallate
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

# Bismuth Subgallate: Laporan Penilaian Penambahan Kegunaan Ubat

## Ringkasan Satu Ayat

Bismuth Subgallate (DrugBank: DB13909) adalah sebatian bismut yang sedang dipasarkan di Malaysia dengan 1 produk berdaftar. Tiada petunjuk kegunaan baru yang telah dijangka oleh model TxGNN pada masa ini, dan jurang data kritikal — termasuk mekanisme tindakan, teks petunjuk kegunaan yang diluluskan, dan maklumat keselamatan — menghalang penilaian penambahan kegunaan yang bermakna.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Kegunaan Asal | Tidak tersedia (medan petunjuk kegunaan lesen adalah kosong) |
| Petunjuk Kegunaan yang Dijangka | Tiada (tiada ramalan TxGNN dihasilkan) |
| Skor Ramalan TxGNN | N/A |
| Aras Bukti | N/A — Tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan (Marketed) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Buat masa ini **tiada ramalan TxGNN** tersedia untuk Bismuth Subgallate. Tatasusunan `predicted_indications` adalah kosong, bermakna model sama ada tidak menghasilkan calon penambahan kegunaan untuk ubat ini atau saluran paip ramalan belum dijalankan untuknya.

Selain itu, data mekanisme tindakan (MOA) yang terperinci tidak tersedia. Bismuth subgallate adalah garam bismut yang diketahui dalam farmakologi am untuk sifat astringent dan haemostatic, tetapi tanpa entri MOA yang disahkan dalam pakej bukti, penalaran mekanik untuk sebarang petunjuk kegunaan baru yang berpotensi tidak dapat ditubuhkan.

Sebelum sebarang penilaian penambahan kegunaan dapat diteruskan, ubat mesti terlebih dahulu lulus melalui saluran paip ramalan TxGNN dengan pemetaan nod KG-ke-DrugBank yang berjaya, dan jurang data asas (MOA, petunjuk kegunaan yang diluluskan, profil keselamatan) mesti diselesaikan.

---

## Bukti Uji Kaji Klinikal

Buat masa ini tiada uji kaji klinikal yang berkaitan berdaftar — tiada petunjuk kegunaan yang dijangka tersedia untuk dicari.

---

## Bukti Literatur

Buat masa ini tiada literatur yang berkaitan tersedia — tiada petunjuk kegunaan yang dijangka tersedia untuk dicari.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk Kegunaan yang Diluluskan |
|------|------|------|------|
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |

> **Nota:** Satu lesen dicatat dalam pangkalan data NPRA, tetapi semua medan perincian (nombor lesen, nama produk, bentuk dos, petunjuk kegunaan yang diluluskan) adalah kosong dalam pakej bukti semasa. Ini perlu diambil daripada portal NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat-ubat) buat masa ini tidak tersedia. Pertanyaan DrugBank DDI tidak mengembalikan hasil apa pun. Profil keselamatan lengkap mesti diperolehi daripada sisipan pakej produk atau pangkalan data NPRA sebelum sebarang penilaian penambahan kegunaan dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan penambahan kegunaan TxGNN telah dihasilkan untuk Bismuth Subgallate, dan beberapa jurang data penyekat wujud. Tanpa petunjuk kegunaan yang dijangka, tiada apa pun untuk dinilai bagi kemasukakalan klinikal atau sokongan bukti.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Jalankan saluran paip ramalan TxGNN** — Sahkan bahawa DB13909 dipetakan ke nod yang sah dalam graf pengetahuan; jika pemetaan gagal, siasat ID DrugBank alternatif atau bentuk garam
2. **Ambil data MOA** (Jurang Data DG002, keseriusan: Tinggi) — Pertanyaan DrugBank API untuk farmakodinamik dan mekanisme tindakan
3. **Ambil butiran lesen NPRA** — Perolehi maklumat pendaftaran lengkap (nombor lesen, nama produk, bentuk dos, teks petunjuk kegunaan yang diluluskan) daripada portal NPRA
4. **Ambil maklumat keselamatan** (Jurang Data DG001, keseriusan: Menyekat) — Muat turun dan huraikan PDF sisipan pakej daripada pihak berkuasa kawal selia untuk amaran, kontraindikasi, dan tindakan berjaga-jaga
5. **Nilai semula** setelah hasil ramalan dan data asas tersedia

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penambahan kegunaan ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

