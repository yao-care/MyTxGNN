---
layout: default
title: Ampicillin Trihydrate
parent: Low Evidence (L4-L5)
nav_order: 72
evidence_level: L5
indication_count: 0
---

# Ampicillin Trihydrate
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

# Ampicillin Trihydrate: Penilaian Kegunaan Semula (Tiada Ramalan TxGNN Tersedia)

## Ringkasan Satu Baris

Ampicillin Trihydrate adalah antibiotik aminopenicillin spektrum luas yang digunakan secara meluas untuk merawat jangkitan bakteria termasuk jangkitan saluran pernafasan, jangkitan saluran kencing, dan meningitis.
Bungkusan Bukti semasa mengandungi **tiada indikasi kegunaan semula yang diramalkan oleh TxGNN** untuk ubat ini — paip saluran ramalan belum dijalankan atau mengembalikan hasil untuk calon ini.
Tanpa indikasi kegunaan semula yang diramalkan, penilaian kegunaan semula yang formal tidak boleh diselesaikan pada masa ini; **laporan ini mendokumenkan ketersediaan data semasa dan mengenalpasti jurang yang mesti diselesaikan sebelum meneruskan.**

---

## Tinjauan Ringkas

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Jangkitan bakteria (antibiotik spektrum luas: pernafasan, saluran kencing, CNS, GI) |
| Indikasi Kegunaan Semula yang Diramalkan | Tidak tersedia — tiada ramalan TxGNN dikembalikan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A (paip saluran ramalan tidak dilaksanakan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Disyorkan | **Tahan** — jurang data kritikal mesti diselesaikan terlebih dahulu |

---

## Latar Belakang Ubat

Ampicillin Trihydrate adalah bentuk garam trihidrat yang stabil bagi ampicillin, antibiotik beta-laktam spektrum luas dalam subkelas aminopenicillin. Ia telah digunakan secara klinikal sejak tahun 1960-an dan masih berada dalam Senarai Ubat-Ubatan Penting WHO.

**Mekanisme Tindakan (daripada pengetahuan umum — pertanyaan DrugBank belum selesai):**
Ampicillin menggunakan aktiviti bakterisida dengan mengikat secara tak boleh balik kepada protein pengikat penicillin (PBPs) yang terletak pada membran dalam dinding sel bakteria. Ini menghalang enzim transpeptidase yang bertanggungjawab untuk sambungan silang peptidoglikan, dengan itu mengganggu sintesis dinding sel dan akhirnya menyebabkan lisis sel bakteria. Sisi rantai aminobenzil memberikan liputan gram-negatif yang dipanjangkan berbanding dengan penicillin awal.

> ⚠️ **Jurang Data DG002 (Tinggi):** Data MOA formal belum diambil daripada DrugBank untuk Bungkusan Bukti ini. Penerangan di atas adalah berdasarkan pengetahuan farmakologi yang ditetapkan dan harus disahkan terhadap rekod API DrugBank sebelum pelaporan formal.

**Indikasi yang Ditetapkan:**
Ampicillin diluluskan untuk jangkitan yang disebabkan oleh organisma yang peka, termasuk:
- Jangkitan saluran pernafasan atas dan bawah (*Haemophilus influenzae*, *Streptococcus pneumoniae*)
- Jangkitan saluran kencing (*E. coli*, *Enterococcus faecalis*)
- Jangkitan gastrointestinal (*Salmonella*, *Shigella*)
- Meningitis bakteria, endokarditis, dan septicemia

---

## Status Ramalan TxGNN

Medan `predicted_indications` dalam Bungkusan Bukti adalah **kosong**. Ini bermakna salah satu senario berikut telah berlaku:

| Kemungkinan Penyebab | Tindakan yang Disyorkan |
|---|---|
| Paip saluran ramalan tidak dilaksanakan untuk ubat ini | Jalankan `scripts/run_kg_prediction.py` dengan Ampicillin Trihydrate sebagai input |
| Pemetaan ID DrugBank gagal (ID DrugBank adalah `null`) | Selesaikan pemetaan ID DrugBank; ID kanonik adalah **DB00415** (ampicillin) |
| Ketidaksesuaian penyeragaman nama ubat | Periksa sama ada "AMPICILLIN TRIHYDRATE" menyeragamkan dengan betul kepada nod KG |
| Tiada isyarat kegunaan semula yang ketara di atas ambang | Tinjau tetapan ambang ramalan |

Sehingga indikasi kegunaan semula yang diramalkan oleh TxGNN tersedia, bahagian inti laporan ini (bukti ujian klinikal, bukti kesusasteraan, nisbah mekanisme) tidak boleh dipenuhi.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal yang berkaitan berdaftar untuk sasaran indikasi kegunaan semula — tiada indikasi kegunaan semula yang diramalkan tersedia.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan tersedia — tiada sasaran indikasi kegunaan semula yang diramalkan untuk dicari.

---

## Maklumat Pasaran Malaysia

Bungkusan Bukti mengesahkan **9 pendaftaran aktif** di Malaysia; bagaimanapun, semua medan terperinci lesen individu (nombor lesen, nama produk, bentuk dos, pengilang, indikasi yang diluluskan) dikembalikan sebagai rentetan kosong dalam seret data semasa.

> ⚠️ Rekod lesen terperinci mesti diambil daripada portal NPRA sebelum bahagian ini boleh diselesaikan.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---|---|---|---|
| (9 lesen disahkan) | Terperinci tidak tersedia dalam bungkusan data semasa | — | — |

**Tindakan yang disyorkan:** Soal semula NPRA dengan julat nombor lesen `MAL` atau ambil rekod pendaftaran penuh melalui API carian produk NPRA untuk mengisi jadual ini.

---

## Pertimbangan Keselamatan

> ⚠️ **Jurang Data DG001 (Menyekat):** Amaran paket sisipan TFDA/NPRA dan kontraindikasi belum diambil. Jurang ini diklasifikasikan sebagai **Menyekat** dan menghalang penyelesaian peringkat penyaringan keselamatan pra-S1.

Sila rujuk sisipan paket yang diluluskan untuk maklumat keselamatan lengkap. Bidang utama untuk diambil termasuk:
- Amaran hipersensitiviti / anaphylaxis (reaktiviti silang dengan cephalosporin)
- Kontraindikasi dalam pesakit yang alergi kepada penicillin
- Keperluan pelarasan dos renal
- Interaksi ubat (antikoagulan, ubat kontraseptif oral, allopurinol, antibiotik bacteriostatic)

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Nisbah:**
Paip saluran ramalan TxGNN belum mengembalikan sebarang calon kegunaan semula untuk Ampicillin Trihydrate, dan dua jurang data kritikal (data keselamatan sisipan paket dan MOA DrugBank) masih tidak diselesaikan. Penilaian kegunaan semula yang formal tidak boleh dijalankan tanpa sasaran indikasi kegunaan semula yang diramalkan.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Selesaikan pemetaan ID DrugBank** — Sahkan ID DrugBank kanonik (`DB00415` untuk ampicillin) dan jalankan semula paip saluran ramalan KG untuk menjana `predicted_indications`.
2. **Ambil data sisipan paket (DG001 — Menyekat)** — Muat turun NPRA/TFDA PDF sisipan paket dan huraikan amaran, kontraindikasi, dan data interaksi ubat.
3. **Ambil MOA daripada DrugBank (DG002 — Tinggi)** — Pertanyaan API DrugBank untuk mendapatkan data farmakologi berstruktur dan mekanisme.
4. **Isi perincian lesen NPRA** — Soal semula NPRA untuk mengambil rekod lesen penuh (nama produk, bentuk dos, indikasi yang diluluskan) untuk semua 9 pendaftaran.
5. **Jalankan semula pengumpulan bukti** — Setelah indikasi kegunaan semula yang diramalkan tersedia, laksanakan pengumpul ClinicalTrials.gov dan PubMed untuk mengisi jadual bukti.
6. **Keluarkan semula laporan ini** — Selepas langkah-langkah di atas, janakan semula Bungkusan Bukti (versi sasaran v5) dan hasilkan laporan penilaian yang lengkap.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

