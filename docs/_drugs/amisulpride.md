---
layout: default
title: Amisulpride
parent: Low Evidence (L4-L5)
nav_order: 57
evidence_level: L5
indication_count: 0
---

# Amisulpride
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

# Amisulpride: Penilaian Penggunaan Semula — Tiada Ramalan TxGNN Tersedia

## Ringkasan Satu Ayat

Amisulpride (DB06288) ialah antipsikotik atipikal dengan 4 produk berdaftar di pasaran Malaysia.
Evidence Pack semasa tidak mengandungi **ramalan penggunaan semula TxGNN**, dan medan data kritikal — termasuk mekanisme tindakan, indikasi yang diluluskan, dan amaran keselamatan — tidak hadir.
Penilaian ini tidak dapat diteruskan melebihi penilaian status awal sehingga pengumpulan data selesai.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Tidak diambil daripada data semasa |
| Indikasi Baru yang Diramalkan | Tidak tersedia |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | — (Tiada ramalan dijana) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 4 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan Tersedia?

Amisulpride tidak dapat menjana ramalan TxGNN dalam kitaran ini kerana dua jurang data yang tidak diselesaikan yang menyekat saluran:

**1. Mekanisme tindakan (MOA) yang hilang:** Pertanyaan API DrugBank mengembalikan hasil (query log ID 2, 2026-03-27), tetapi medan MOA tidak diisi dalam Evidence Pack. Tanpa data mekanistik yang disahkan, graf pengetahuan tidak dapat mewujudkan laluan pautan penyakit kepada sasaran penggunaan semula calon.

**2. Medan indikasi yang diluluskan kosong:** Kesemua 4 lesen berdaftar NPRA mengembalikan teks indikasi kosong. Tanpa sauh penyakit asas, sistem tidak dapat menjalankan pemarkahan persamaan penyakit atau menapis ramalan calon.

Daripada literatur perubatan terbitan, amisulpride dikenali sebagai **antagonis reseptor dopamin D2/D3 yang selektif**. Pada dos antipsikotik standard (400–800 mg/hari), ia mengurangkan gejala positif dan negatif skizofrenia dengan menyekat reseptor dopamin postsinaptik. Pada dos ultra-rendah (5–25 mg), ia bertindak secara pilihan pada autorreseptor pra-sinaptik, yang mendasari sifat antiemetiknya yang terdokumentasi dengan baik — mekanisme yang menghasilkan kelulusan FDA AS untuk mual dan muntah selepas operasi (PONV) pada 2020 (nama jenama: Barhemsys®). Setelah data MOA dan indikasi ditangkap secara rasmi, dijangka larian ramalan TxGNN yang bermakna boleh dilaksanakan.

---

## Maklumat Pasaran Malaysia

Pertanyaan NPRA (2026-03-27) mengesahkan 4 produk berdaftar, tetapi butiran aras produk tidak dipulangkan dalam kitaran data ini. Jadual di bawah tidak dapat diisi sehingga penarikan data NPRA sekunder selesai.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------------------|-------------|-------------|---------------------|
| (data tidak diambil) | (data tidak diambil) | (data tidak diambil) | (data tidak diambil) |

> **Nota:** NPRA mengembalikan pertanyaan yang berjaya dengan 4 hasil, tetapi semua medan rekod lesen (nama produk, bentuk dos, pengeluar, indikasi yang diluluskan) adalah rentetan kosong. Pertanyaan semula yang menyasarkan monograf produk individu atau PDF sisipan pakej diperlukan.

---

## Pertimbangan Keselamatan

Sila merujuk kepada sisipan pakej untuk maklumat keselamatan.

> Amaran kunci, kontraindikasi, dan data interaksi ubat tidak tersedia dalam Evidence Pack ini. Sisipan pakej NPRA harus dimuat turun dan dianalisis sebagai langkah remediasi utama.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada ramalan TxGNN dijana, dan ketiga-tiga input penilaian teras — indikasi yang diluluskan, mekanisme tindakan, dan profil keselamatan — hilang. Tiada bukti yang mencukupi untuk menilai potensi penggunaan semula atau kebolehlaksanaan keselamatan pada peringkat ini.

**Untuk diteruskan, yang berikut diperlukan:**

- **Pengambilan sisipan pakej NPRA**: Muat turun monograf PDF untuk kesemua 4 produk berdaftar untuk mengekstrak indikasi yang diluluskan, amaran kunci, dan kontraindikasi (Data Gap DG001 — Keterukan yang menyekat)
- **Pertanyaan semula API DrugBank**: Ambil data mekanisme tindakan, farmakodinamik, dan interaksi ubat untuk DB06288 (Data Gap DG002 — Keterukan tinggi)
- **Larian semula saluran TxGNN**: Setelah menyelesaikan DG001 dan DG002, jalankan semula saluran ramalan KG dan ramalan DL untuk menjana indikasi penggunaan semula calon
- **Pengesahan butiran produk NPRA**: Sahkan sama ada kesemua 4 pendaftaran berkongsi indikasi yang sama (cth, skizofrenia sahaja) atau sama ada indikasi antiemetik dos rendah (PONV) didaftarkan secara berasingan di Malaysia

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

