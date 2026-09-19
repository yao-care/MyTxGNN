---
layout: default
title: Benazepril Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 124
evidence_level: L5
indication_count: 0
---

# Benazepril Hydrochloride
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

# Benazepril Hydrochloride: Penilaian Penggunaan Semula Ubat — Laporan Awal

## Ringkasan Satu Ayat

Benazepril Hydrochloride ialah penghambat ACE yang sedang dipasarkan di Malaysia dengan 2 produk terdaftar. **Tiada petunjuk penggunaan baru telah diramalkan oleh TxGNN pada masa ini**, dan jurang data penting (ID DrugBank, MOA, teks petunjuk yang diluluskan, dan maklumat keselamatan) mesti diselesaikan sebelum penilaian penuh dapat diteruskan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Asal | *(Data tidak tersedia — teks petunjuk lesen kosong)* |
| Petunjuk Penggunaan Baru yang Diramalkan | **Tiada** — tiada ramalan TxGNN dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **L5** (Tiada ramalan, tiada kajian untuk dinilai) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini **tiada ramalan TxGNN** tersedia untuk Benazepril Hydrochloride. Tatasusunan `predicted_indications` kosong, bermakna model sama ada belum dilaksanakan untuk ubat ini atau tiada calon memenuhi ambang skor.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pakej bukti ini. Berdasarkan maklumat yang diketahui umum, Benazepril ialah penghambat enzim angiotensin-menukar (ACE) yang menghalang penukaran angiotensin I kepada angiotensin II, dengan itu mengurangkan vasopengerutan dan sekresi aldosteron. Ia digunakan secara meluas untuk rawatan hipertensi dan kegagalan jantung kongestif. Kelas ubat ini juga telah disiasat untuk kesan nefroprotektif dalam nefropati berdiabetes dan keadaan lain.

Sebelum penilaian penggunaan semula ubat dapat diteruskan, saluran paip ramalan TxGNN mesti dilaksanakan dengan pemetaan DrugBank yang sah untuk Benazepril (ID DrugBank: **DB00542**, berdasarkan data umum yang diketahui) untuk menjana petunjuk calon.

---

## Bukti Uji Klinikal

Pada masa ini tiada petunjuk ramalan untuk dicari. Bukti uji klinikal akan dikumpulkan sebaik sahaja ramalan TxGNN tersedia.

---

## Bukti Literatur

Pada masa ini tiada petunjuk ramalan untuk dicari. Bukti literatur akan dikumpulkan sebaik sahaja ramalan TxGNN tersedia.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------|------|------|-----------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Nota:** Dua pendaftaran telah ditemui oleh pertanyaan NPRA (tarikh pertanyaan: 2026-03-27), tetapi medan terperinci lesen (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) semuanya kosong dalam pakej bukti ini. Ini perlu diekstrak semula daripada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk surat kapsul untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini hilang daripada pakej bukti ini.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Penilaian ini tidak dapat diteruskan kerana tiada petunjuk ramalan TxGNN dan pelbagai jurang data kritikal tetap tidak diselesaikan. Pakej bukti tidak lengkap pada peringkat paling asas — tanpa petunjuk ramalan, tiada penilaian penggunaan semula boleh dilakukan.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Pemetaan ID DrugBank** — Sahkan ID DrugBank (berkemungkinan DB00542) dan sepadukan ke dalam pakej bukti
2. **Jalankan semula ramalan TxGNN** — Laksanakan saluran paip ramalan KG dan DL dengan pemetaan DrugBank yang betul untuk menjana petunjuk calon
3. **Isi terperinci lesen NPRA** — Pertanyaan semula pangkalan data NPRA untuk mengisi nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan untuk 2 produk terdaftar
4. **Dapatkan data MOA** — Pertanyaan API DrugBank untuk mendapatkan mekanisme tindakan (laluan penghambatan ACE)
5. **Dapatkan data keselamatan** — Muat turun dan parse PDF surat kapsul (仿單) daripada NPRA/pengeluar untuk mengekstrak amaran, kontraindikasi, dan maklumat interaksi ubat
6. **Pengumpulan bukti** — Sebaik sahaja petunjuk ramalan tersedia, jalankan pengumpul ClinicalTrials.gov, PubMed, dan ICTRP untuk bukti sokongan

---

### Ringkasan Jurang Data

| ID | Item | Keterukan | Remediasi |
|----|------|----------|-------------|
| DG001 | Amaran/kontraindikasi surat kapsul | **Menghalang** | Muat turun PDF surat kapsul daripada NPRA dan parse |
| DG002 | Mekanisme Tindakan (MOA) | Tinggi | Pertanyaan API DrugBank |
| — | ID DrugBank | Tinggi | Peta BENAZEPRIL HYDROCHLORIDE → DB00542 |
| — | Petunjuk ramalan TxGNN | **Menghalang** | Jalankan semula saluran paip ramalan |
| — | Terperinci lesen NPRA | Sederhana | Pertanyaan semula NPRA dengan ekstraksi medan lengkap |

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

