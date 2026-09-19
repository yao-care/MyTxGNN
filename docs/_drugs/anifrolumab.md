---
layout: default
title: Anifrolumab
parent: Low Evidence (L4-L5)
nav_order: 77
evidence_level: L5
indication_count: 0
---

# Anifrolumab
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

# Anifrolumab: Daripada Systemic Lupus Erythematosus kepada — (Tiada Data Ramalan TxGNN dalam Pakej Bukti Ini)

---

## Ringkasan Satu Ayat

Anifrolumab (SAPHNELO) ialah antibodi monoklonal manusia sepenuhnya yang menyasarkan reseptor interferon jenis I (IFNAR1), diluluskan untuk systemic lupus erythematosus (SLE) aktif sederhana hingga berat pada dewasa.
Pakej Bukti ini **tidak mengandungi sebarang petunjukan kegunaan baru yang diramalkan oleh TxGNN**, dan dua jurang data yang kritikal — maklumat keselamatan surat sisipan ubat yang hilang (Menghalang) dan data mekanisme tindakan yang hilang (Tinggi) — menghalang penilaian penggunaan semula yang lengkap.
**Tiada cadangan penggunaan semula boleh dikeluarkan** sehingga jurang-jurang ini diperbaiki dan saluran ramalan dijalankan semula.

---

## Ikhtisar Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asli | Systemic lupus erythematosus (SLE) aktif sederhana hingga berat |
| Petunjuk Kegunaan Baru yang Diramalkan | Tiada ramalan tersedia dalam Pakej Bukti ini |
| Skor Ramalan TxGNN | T/A |
| Aras Bukti | T/A |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disarankan | **Tangguh** |

---

## Sebab Tiada Ramalan yang Munasabah untuk Dinilai

Medan `predicted_indications` dalam Pakej Bukti ini adalah kosong. Tiga punca yang berkemungkinan:

1. **Saluran belum dilaksanakan** — Larian ramalan TxGNN untuk DB11976 mungkin belum tercetus atau selesai.
2. **Kegagalan pemetaan ID DrugBank** — Jika ANIFROLUMAB tidak berjaya dipadankan dengan nod dalam graf pengetahuan, tiada penyakit calon akan diberi skor.
3. **Isu peringkat data** — Keluaran ramalan mungkin wujud di hulu tetapi tidak digabungkan ke dalam Pakej Bukti v4 ini.

Selari dengan itu, dua jurang data menghalang penilaian walaupun jika ramalan tersedia:

| ID Jurang | Item | Tahap Keseriusan | Kesan |
|-----------|------|-----------------|-------|
| DG001 | Amaran surat sisipan ubat & kontraindikasi | **Menghalang** | Tidak dapat menyelesaikan saringan pra-keselamatan S1 |
| DG002 | Mekanisme tindakan (MOA) | Tinggi | Tidak dapat melakukan penilaian logik mekanik |

---

## Latar Belakang Ubat: Mekanisme Tindakan yang Diketahui

Walaupun medan MOA ditandakan sebagai jurang data dalam Pakej Bukti ini, mekanisme anifrolumab telah dicirikan dengan baik dalam literatur yang diterbitkan dan rekod DrugBank untuk DB11976.

Anifrolumab ialah antibodi monoklonal IgG1κ manusia sepenuhnya yang mengikat subunit 1 reseptor interferon jenis I (**IFNAR1**), menghalang isyarat daripada **semua interferon jenis I** (IFN-α, IFN-β, IFN-ω, dan subtaip yang berkaitan). Isyarat IFN Jenis I terlebih aktif secara patologi dalam kira-kira 60–80% pesakit SLE, mendorong pengeluaran sitokin keradangan, pengaktifan sel dendritik, dan autoreaktiviti sel B. Dengan menduduki IFNAR1, anifrolumab menyekat tandatangan gen interferon (IFNGS) dan mengurangkan transkrip yang dimediasi JAK1/TYK2 hiliran bagi gen pro-keradangan.

Mekanisme ini bukan eksklusif kepada SLE. Keadaan lain yang dicirikan oleh aktiviti IFN Jenis I yang meningkat — termasuk dermatomiositis, sindrom Sjögren primer, sklerosis sistematik, dan vaskulitis berkaitan ANCA — adalah sasaran yang munasabah secara biologi. Walau bagaimanapun, **tiada seorang pun disahkan melalui ramalan TxGNN dalam pakej data ini**, dan maklumat latar belakang ini disediakan semata-mata untuk konteks sambil menunggu jalan semula saluran ramalan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------------------|-------------|-----------|------------------------|
| (Tidak diisi) | Anifrolumab — SAPHNELO | (Tidak diisi) | SLE aktif sederhana hingga berat pada dewasa (butiran belum diambil ke dalam Pakej Bukti ini) |

> **Catatan:** Pakej Bukti mencatat 1 lesen berdaftar dengan status pasaran "Dipasarkan" (Dipasarkan), tetapi semua medan butiran lesen — termasuk nombor lesen, nama produk, bentuk dos, pengilang, dan teks petunjuk yang diluluskan — tidak diisi. Sila sahkan terus terhadap pendaftaran dalam talian NPRA atau ambil rekod lesen lengkap sebelum meneruskan.

---

## Pertimbangan Keselamatan

Sila rujuk surat sisipan ubat untuk maklumat keselamatan.

> **Amaran Jurang Data (DG001 — Menghalang):** Kedua-dua medan amaran utama dan kontraindikasi disenaraikan sebagai [Jurang Data] dalam Pakej Bukti ini. Penilaian keselamatan formal tidak dapat diselesaikan. Berdasarkan kelas ubat (biologi anti-IFNAR1), doktor harus sedar bahawa pertimbangan tipikal untuk kategori ini termasuk: jangkitan serius dan oportunistik (termasuk influenza dan herpes zoster), kontraindikasi vaksin yang dilemahkan secara langsung semasa rawatan, reaksi berkaitan infusi dan hipersensitiviti, dan potensi imunsupresi dalam kombinasi dengan biologi lain. **Ini adalah pertimbangan kelas umum sahaja dan mesti disahkan terhadap surat sisipan ubat Malaysia yang diluluskan sebelum sebarang keputusan klinikal.**

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguh**

**Alasan:**
Pakej Bukti ini tidak lengkap secara material — tiada ramalan penggunaan semula TxGNN hadir, data keselamatan kritikal tidak hadir pada aras keterhalangan, dan medan butiran lesen tidak diisi. Mengeluarkan cadangan penggunaan semula di bawah keadaan ini tidak akan dapat dipertahankan secara saintifik.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Menghalang — DG001]** Muat turun dan parse PDF surat sisipan ubat NPRA/TFDA untuk SAPHNELO (anifrolumab) untuk mengekstrak amaran yang diluluskan, kontraindikasi, panduan populasi istimewa, dan keperluan pengendalian; isi medan `safety.key_warnings` dan `safety.contraindications`
- **[Tinggi — DG002]** Soal API DrugBank untuk DB11976 untuk mendapatkan teks MOA lengkap dan isi medan `drug.original_moa`
- **[Saluran]** Jalankan semula saluran ramalan TxGNN KG + DL dengan ID DrugBank DB11976 yang disahkan untuk mengisi `predicted_indications`
- **[Kawal Selia]** Ambil rekod butiran lesen lengkap daripada NPRA (nombor lesen, nama produk, bentuk dos, teks petunjuk yang diluluskan) dan isi `taiwan_regulatory.licenses[0]`
- **[Penilaian Semula]** Setelah semua empat item di atas diselesaikan, serahkan semula Pakej Bukti (sasaran v5) untuk penilaian penggunaan semula aras bukti L1–L5 yang lengkap

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

