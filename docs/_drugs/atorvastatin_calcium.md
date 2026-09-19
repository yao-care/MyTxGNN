---
layout: default
title: Atorvastatin Calcium
parent: Low Evidence (L4-L5)
nav_order: 99
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium
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

# Atorvastatin Calcium: Penilaian Tujuan Ulang Ubat — Data Ramalan TxGNN Tertangguh

## Ringkasan Satu Ayat

Atorvastatin Calcium adalah ubat statin yang digunakan secara meluas dan asal-mulanya ditunjukkan untuk hiperlipidemik dan pengurangan risiko kardiovaskular melalui perencatan reductase HMG-CoA.
Paket Bukti semasa tidak mengandungi **output ramalan TxGNN** — array `predicted_indications` kosong — bermakna tiada indikasi tujuan ulang baharu boleh dinilai pada masa ini.
Dengan **71 produk berdaftar** di Malaysia dan data keselamatan serta MOA penting masih belum lengkap, penilaian tujuan ulang ubat adalah **tersekat** sehingga jurang data hulu diselesaikan.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Hiperlipidemik / Pengurangan risiko kardiovaskular (telah ditubuh; teks indikasi TFDA belum diambil) |
| Indikasi Baru Ramalan | — *(Tiada output TxGNN tersedia)* |
| Skor Ramalan TxGNN | — *(Tertangguh)* |
| Tahap Bukti | — *(Tidak dapat ditentukan)* |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 71 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Data ramalan TxGNN tidak tersedia dalam Paket Bukti semasa (`predicted_indications: []`), jadi analisis pontian mekanisme-ke-indikasi tidak boleh dilakukan pada peringkat ini.

Daripada pengetahuan farmaseutikal yang telah ditubuh, atorvastatin adalah perencat reductase HMG-CoA (statin). Selain daripada pengurangan lipid, statin telah dikaji secara meluas untuk kesan pleiotropik — termasuk sifat anti-radang, anti-proliferatif, dan neuroprotektif — yang telah mendorong hipotesis tujuan ulang dalam bidang seperti penyakit neurodegeneratif, sepsis, dan kanser tertentu. Walau bagaimanapun, hipotesis-hipotesis ini **tidak dapat disahkan atau diskor** tanpa output model TxGNN.

Analisis mekanisme-ke-indikasi formal akan diselesaikan apabila paip ramalan TxGNN dilaksanakan dan data MOA DrugBank diambil.

---

## Bukti Uji Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan dalam Paket Bukti ini.

*Nota: Ini mencerminkan data `predicted_indications` yang hilang — bukan ketiadaan aktiviti ujian dunia sebenar untuk atorvastatin. Apabila indikasi sasaran dikenal pasti oleh TxGNN, pencarian ClinicalTrials.gov harus dijalankan.*

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia dalam Paket Bukti ini.

*Nota: Alasan yang sama seperti di atas — pengambilan bukti literatur terikat kepada indikasi ramalan khusus, yang belum tersedia lagi.*

---

## Maklumat Pasaran Malaysia

Paket Bukti mengesahkan **71 produk berdaftar** untuk ATORVASTATIN CALCIUM di Malaysia. Walau bagaimanapun, butiran produk individu (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak dikembalikan dalam penarikan data semasa.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------------------|-------------|-------------|---------------------|
| *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* |

> **Tindakan Diperlukan:** Jalankan semula pertanyaan NPRA/BPFK dengan pengambilan butiran peringkat lesen penuh. Dengan 71 pendaftaran disahkan, data ini harus dapat diakses.

---

## Pertimbangan Keselamatan

Sila rujuk selebaran maklumat produk untuk maklumat keselamatan.

> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat-ubat) dikembalikan sebagai jurang data atau tidak ditemui dalam pertanyaan semasa. Pengambilan selebaran maklumat TFDA/NPRA (PIL/SmPC) diperlukan sebelum sebarang keputusan berpagar keselamatan boleh dibuat.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Analisis tujuan ulang utama tidak dapat diteruskan kerana paip ramalan TxGNN belum mengembalikan output untuk calon ini, dan dua jurang data yang menghalang (keselamatan/MOA) kekal belum diselesaikan. Ubat ini telah ditubuh dengan baik dalam pasaran (71 pendaftaran Malaysia), jadi keberlakuan kawal selia kuat apabila sasaran ramalan disahkan.

**Untuk meneruskan, yang berikut diperlukan:**

- [ ] **[DG001 — Menghalang]** Ambil selebaran maklumat TFDA/NPRA: muat turun SmPC/PIL PDF daripada portal rasmi NPRA dan analisis amaran utama serta kontraindikasi
- [ ] **[DG002 — Tinggi]** Ambil MOA DrugBank: pertanyaan API DrugBank menggunakan ID DrugBank yang diselesaikan (pemetaan TFDA → ID DrugBank dicuba; pastikan hasil pemetaan ditulis kepada `drug.drugbank_id`)
- [ ] **[Kritikal]** Jalankan paip ramalan TxGNN untuk ATORVASTATIN CALCIUM untuk mengisi `predicted_indications` — ini adalah prasyarat untuk seluruh penilaian tujuan ulang
- [ ] Ambil butiran peringkat lesen NPRA penuh (nama produk, bentuk dos, teks indikasi) untuk 71 produk berdaftar
- [ ] Jalankan semula pertanyaan DDI setelah ID DrugBank disahkan (status `query_status: not_found` semasa kemungkinan disebabkan oleh paut ID DrugBank yang hilang)

Apabila yang di atas diselesaikan, laporan ini harus dijana semula dengan Paket Bukti v5.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

