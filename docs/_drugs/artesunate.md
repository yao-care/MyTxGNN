---
layout: default
title: Artesunate
parent: Low Evidence (L4-L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Artesunate
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

# Artesunate: Ubat Antimalaria — Penilaian Tujuan Semula (Awal)

## Ringkasan Satu Ayat

Artesunate (DrugBank: DB09274) ialah ejen antimalaria terbitan artemisinin yang sudah mantap, kini memegang satu kebenaran pasaran aktif di Malaysia.
Walau bagaimanapun, Pakej Bukti ini mengandungi jurang data yang kritikal — **tiada ramalan TxGNN dikembalikan**, dan mekanisme kerja, teks indikasi kawal selia, serta data keselamatan semuanya tidak ada — bermakna penilaian tujuan semula ubat yang lengkap **tidak dapat diselesaikan pada peringkat ini**.
Pemulihan data segera diperlukan sebelum meneruskan ke sintesis bukti.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Malaria (disimpulkan daripada kelas ubat; teks indikasi diluluskan tidak tersedia dalam pakej semasa) |
| Indikasi Baru yang Diramalkan | Tiada ramalan tersedia dalam data semasa |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A — data tidak mencukupi untuk menetapkan tahap |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Wajar?

Buat masa sekarang, data mekanisme kerja yang terperinci tidak tersedia dalam Pakej Bukti ini, dan model TxGNN tidak mengembalikan calon ubat tujuan semula untuk sebatian ini.

Artesunate tergolong dalam kelas antimalaria artemisinin. Peranan klinikal utamanya adalah dalam merawat jangkitan *Plasmodium* yang teruk dan tanpa komplikasi. Penyelidikan terdahulu telah mencadangkan bahawa artemisinin mungkin menjalankan aktiviti sitotoksik melalui penjanaan radikal bebas bergantung besi, yang telah mendorong penyiasatan eksploratori ke dalam aplikasi onkologi — namun, asas bukti ini **tidak tercermin dalam Pakej Bukti semasa** dan tidak boleh dinilai secara formal di sini.

Tanpa indikasi ramalan yang disahkan, analisis jambatan mekanisme-ke-indikasi tidak berkenaan pada masa ini. Sebaik sahaja ramalan TxGNN berjaya dijana, bahagian ini harus disemak semula untuk menilai sama ada mekanisme antimalaria yang diketahui dapat dibenarkan secara mekanistik untuk indikasi baru yang diramalkan.

---

## Bukti Ujian Klinik

Tiada indikasi ramalan tersedia dalam Pakej Bukti semasa. Bukti ujian klinik tidak boleh diekstrak atau disimpulkan.

Sebaik sahaja indikasi sasaran dikenal pasti daripada keluaran TxGNN, ujian yang relevan harus diambil semula daripada `predicted_indications[0].evidence.clinical_trials`.

---

## Bukti Literatur

Tiada indikasi ramalan tersedia dalam Pakej Bukti semasa. Bukti literatur tidak boleh diekstrak atau disimpulkan.

Sebaik sahaja indikasi sasaran dikenal pasti, penerbitan yang relevan harus diambil semula daripada `predicted_indications[0].evidence.literature`.

---

## Maklumat Pasaran Malaysia

Pakej Bukti mengesahkan **1 kebenaran pasaran aktif** di Malaysia; walau bagaimanapun, semua medan terperinci pendaftaran kini kosong.

| Nombor Kebenaran | Nama Produk | Bentuk Ubatan | Indikasi yang Diluluskan |
|---------------------|--------------|-------------|---------------------|
| *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia)* | *(Tidak tersedia — memerlukan pengambilan rekod NPRA)* |

Untuk mengisi jadual ini, rekod pendaftaran NPRA lengkap untuk Artesunate mesti diambil semula dan dianalisis.

---

## Pertimbangan Keselamatan

Sila rujuk lembaran penyisipan pakej untuk maklumat keselamatan.

> **Nota:** Semua medan keselamatan dalam Pakej Bukti ini — termasuk amaran utama, kontraindikasi, dan interaksi ubat-ubat — sama ada ditandai sebagai jurang data atau tidak mengembalikan hasil. Ini diklasifikasikan sebagai jurang data **Penghalang** (DG001) yang menghalang sebarang langkah penilaian bergantung keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Pakej Bukti ini tidak lengkap dalam dua dimensi penghalang: (1) saluran ramalan TxGNN tidak mengembalikan calon ubat tujuan semula untuk Artesunate, dan (2) data keselamatan dan kawal selia yang kritikal tidak ada. Tiada cadangan tujuan semula berasaskan bukti boleh dibuat dalam keadaan semasa.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Penghalang — DG001]** Ambil semula dan analisis PDF lembaran penyisipan pakej NPRA/TFDA untuk mengeluarkan indikasi diluluskan, amaran utama, dan kontraindikasi
- **[Tinggi — DG002]** Soal API DrugBank untuk Artesunate (DB09274) untuk mengambil semula mekanisme kerja, farmakodinamik, dan kategori ubat
- **[Penghalang — Ramalan]** Diagnosis mengapa `predicted_indications` kosong — sahkan bahawa ID DrugBank Artesunate ada dalam senarai nod graf pengetahuan TxGNN (`data/node.csv`) dan jalankan semula saluran ramalan (`scripts/run_kg_prediction.py`)
- **[Sederhana]** Isi terperinci lesen NPRA (nama produk, bentuk ubatan, nombor kebenaran) daripada rekod kawal selia yang disahkan ada (1 pendaftaran ditemui)
- **[Selepas pemulihan]** Sebaik sahaja ramalan dan MOA tersedia, jalankan semula penjanaan Pakej Bukti lengkap untuk membolehkan penilaian tahap bukti L1–L5 yang lengkap dan keputusan Go / Teruskan dengan Keadaan Keselamatan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

