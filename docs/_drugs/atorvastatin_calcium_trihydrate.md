---
layout: default
title: Atorvastatin Calcium Trihydrate
parent: Low Evidence (L4-L5)
nav_order: 100
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium Trihydrate
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

# Atorvastatin Calcium Trihydrate: Penilaian Penghantaran Semula Ubat (Tiada Ramalan Tersedia dalam Paket Bukti Semasa)

## Ringkasan Satu Ayat

Atorvastatin Calcium Trihydrate adalah statin yang telah terbukti keberkesanannya, awalnya digunakan untuk merawat hiperkolesterolaemia dan mengurangkan risiko kardiovaskular dengan menghambat HMG-CoA reductase. Paket Bukti semasa mengandungi **tiada indikasi yang diramalkan oleh TxGNN** untuk ubat ini, bermakna keluaran pemodelan penghantaran semula belum tersedia untuk penilaian. Sehingga data ramalan dihasilkan, adalah tidak mungkin untuk menilai kekuatan bukti atau memberikan satu rekomendasi.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Hiperkolesterolaemia / Pengurangan risiko kardiovaskular (kelas statin; disahkan daripada pengetahuan kelas ubat — teks indikasi NPRA rasmi tidak diperoleh) |
| Indikasi Baru yang Diramalkan | — Tidak tersedia (predicted_indications adalah kosong) |
| Skor Ramalan TxGNN | — Tidak tersedia |
| Tahap Bukti | L5 (data ramalan model tidak ada; tiada kajian sokongan boleh dinilai pada masa ini) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 32 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Satu Ramalan Adalah Munasabah?

Pada peringkat ini, tiada sasaran penghantaran semula telah dijana oleh model TxGNN untuk ubat ini, jadi tiada pautan mekanik kepada satu indikasi baru boleh dinilai secara rasmi.

Untuk rujukan, Atorvastatin termasuk dalam kelas statin dan bertindak sebagai penghambat kompetitif bagi 3-hydroxy-3-methylglutaryl-coenzyme A (HMG-CoA) reductase, enzim penentu kadar dalam laluan biosintesis kolesterol. Di luar penurunan lipid, statin menunjukkan kesan pleiotropik — termasuk sifat anti-inflamasi, imunomodulatori, dan anti-proliferatif — yang telah mendorong hipotesis penghantaran semula merentasi pelbagai kawasan penyakit (cth., penyakit Alzheimer, sklerosis berganda, kanser tertentu). Walau bagaimanapun, tiada arah ini boleh dinilai secara rasmi atau disenaraikan pangkat tanpa keluaran ramalan TxGNN.

Data mekanisme tindakan terperinci juga direkodkan sebagai jurang data (DG002) dalam paket semasa. Setelah data DrugBank diambil dan saluran ramalan TxGNN dijalankan, bahagian ini akan dipenuhi dengan indikasi calon yang disenaraikan pangkat.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan — sasaran ramalan belum ditentukan; bahagian akan dipenuhi setelah keluaran TxGNN tersedia.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia — sasaran ramalan belum ditentukan; bahagian akan dipenuhi setelah keluaran TxGNN tersedia.

---

## Maklumat Pasaran Malaysia

Ubat ini memegang **32 pendaftaran** dengan NPRA (Malaysia) dan disahkan sebagai dipasarkan. Walau bagaimanapun, rekod lesen individu yang diperoleh dalam Paket Bukti ini tidak mengandungi sebarang medan yang dipenuhi (nombor lesen, nama produk, bentuk dos, teks indikasi yang diluluskan semuanya kosong). Jadual di bawah mencerminkan keadaan data semasa:

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|-----------------|-----------|----------|----------------------|
| — | — | — | — |

> **Nota:** Butiran peringkat lesen (nama produk, bentuk dos, teks indikasi yang diluluskan) mesti diperoleh daripada portal NPRA untuk melengkapkan bahagian ini. 32 pendaftaran mengesahkan satu kehadiran pasaran yang mantap selaras dengan Atorvastatin menjadi ubat kardiovaskular barisan pertama.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Jurang data keselamatan telah dicatat untuk calon ini:
> - **DG001 (Sekatan):** Amaran dan kontraindikasi sisipan pakej NPRA/TFDA belum diperoleh. Ini menyekat langkah pra-pemeriksaan keselamatan S1. Pemulihan: muat turun dan parsing PDF sisipan pakej daripada sumber rasmi.
> - Tiada rekod interaksi ubat-ubat dikembalikan dalam paket bukti ini (status pertanyaan: tidak ditemui).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan Munasabah:**
Saluran ramalan TxGNN belum menghasilkan keluaran untuk Atorvastatin Calcium Trihydrate, menjadikannya mustahil untuk mengenal pasti, menilai, atau melakukan penilaian terhadap sebarang indikasi calon penghantaran semula. Tanpa indikasi sasaran, tiada langkah penilaian lanjutan (kebolehpercayaan mekanik, bukti ujian klinikal, bukti kesusasteraan, pemprofilan keselamatan) boleh disempurnakan.

**Untuk meneruskan, perkara berikut diperlukan:**

- [ ] **Jalankan ramalan TxGNN** — jalankan saluran ramalan KG + DL dengan ID DrugBank Atorvastatin untuk menjana indikasi calon yang disenaraikan pangkat
- [ ] **Ambil ID DrugBank** — medan `drugbank_id` adalah nol; petakan "ATORVASTATIN CALCIUM TRIHYDRATE" kepada entri DrugBank kanoniknya (DB01076) untuk membolehkan input model (Jurang Data DG002)
- [ ] **Ambil data MOA** — pertanyaan API DrugBank untuk memenuhi mekanisme tindakan (Jurang Data DG002)
- [ ] **Ambil butiran sisipan pakej NPRA** — muat turun dan parsing teks indikasi yang diluluskan, amaran, dan kontraindikasi untuk 32 produk terdaftar (Jurang Data DG001; ketertiban: Sekatan)
- [ ] **Isi data peringkat lesen** — pastikan 32 rekod pendaftaran NPRA termasuk nama produk, bentuk dos, dan teks indikasi yang diluluskan
- [ ] **Jalankan semula pengumpulan bukti** — setelah indikasi yang diramalkan tersedia, kumpulkan bukti ClinicalTrials.gov, PubMed, dan ICTRP untuk pasangan ubat-penyakit tertentu itu

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

