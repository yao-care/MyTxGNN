---
layout: default
title: Docusate Sodium
parent: Low Evidence (L4-L5)
nav_order: 294
evidence_level: L5
indication_count: 0
---

# Docusate Sodium
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

# Docusate Sodium: Penilaian Ubah Tujuan Ubat — Tiada Indikasi Baharu yang Diramalkan

## Ringkasan Satu Ayat

Docusate sodium adalah surfaktant anionik yang terkenal sebagai pelembut najis, kini dipasarkan di Malaysia dengan 1 pendaftaran. Model TxGNN **tidak meramalkan sebarang indikasi ubah tujuan ubat yang baharu** untuk ubat ini, dan tiada penyakit calon yang dikenal pasti untuk penilaian lanjutan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Indikasi Asal | (Tidak tercatat dalam set data semasa) |
| Indikasi Baharu yang Diramalkan | **Tiada** — tiada ramalan yang dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Jumlah Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan yang Dijana?

Docusate sodium (dioctyl sodium sulfosuccinate) adalah surfaktant anionik yang bertindak sebagai pelembut najis. Ia mengurangkan ketegangan permukaan najis, membenarkan air dan lipid menembusi jisim najis, dengan itu memudahkan pergerakan usus. Ia digunakan secara meluas sebagai ubat pencahar tanpa resepi.

Terdapat beberapa kemungkinan sebab mengapa TxGNN tidak menjana calon ubah tujuan ubat untuk ubat ini:

1. **DrugBank ID yang hilang**: Pek Bukti tidak mengandungi pemetaan DrugBank ID untuk Docusate sodium. Tanpa pengenalpastian ini, ubat tidak dapat ditempatkan dalam graf pengetahuan TxGNN, menjadikannya mustahil untuk mengira skor ramalan penyakit–ubat.

2. **Keterhubungan graf pengetahuan terbatas**: Walaupun dipetakan, docusate sodium adalah surfaktant mudah dengan mekanisme tindakan fizikal bukan spesifik (bukan mekanisme farmakologi bertarget reseptor atau enzim). Ubat dengan MOA bukan spesifik cenderung mempunyai lebih sedikit tepi dalam graf pengetahuan, mengurangkan kemungkinan ramalan ubah tujuan ubat yang bermakna.

3. **Profil terapeutik sempit**: Sebagai pelembut najis dengan tindakan gastrointestinal setempat dan penyerapan sistemik minimal, asas farmakologi untuk ubah tujuan ubat lintas indikasi secara intrinsik terhad.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| (Tidak tercatat) | (Tidak tercatat) | (Tidak tercatat) | (Tidak tercatat) |

> **Nota:** Satu pendaftaran telah dikenal pasti dalam pangkalan data NPRA, tetapi bidang lesen terperinci (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak ditangkap dalam pek bukti semasa. Pengesahan manual di [portal NPRA Quest3+](https://quest3plus.bpfk.gov.my/) adalah disyorkan.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan paket untuk maklumat keselamatan. Tiada amaran, kontraindikasi, atau data interaksi ubat tersedia dalam pek bukti semasa.

---

## Jurang Data yang Dikenal Pasti

| ID Jurang | Item | Keterukan | Kesan | Penyelesaian |
|--------|------|----------|--------|-------------|
| DG001 | Amaran Label TFDA / Kontraindikasi | Menghalang | Tidak dapat melakukan penskrinan keselamatan S1 | Muat turun dan analisis PDF label dari laman web TFDA |
| DG002 | Mekanisme Tindakan (MOA) | Tinggi | Menjejaskan analisis relevansi mekanistik | Pertanyaan API DrugBank |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada calon ubah tujuan ubat yang diramalkan oleh TxGNN untuk Docusate sodium. Punca utama yang paling mungkin adalah pemetaan DrugBank ID yang hilang, yang menghalang ubat daripada ditempatkan dalam graf pengetahuan. Selain itu, sebagai ubat pencahar surfaktant bukan spesifik dengan pendedahan sistemik minimal, Docusate sodium mempunyai rasional farmakologi terbatas untuk ubah tujuan ubat lintas indikasi.

**Untuk meneruskan, yang berikut diperlukan:**
- **Selesaikan pemetaan DrugBank**: Docusate sodium sepadan dengan DrugBank ID **DB11089** (atau **DB04352** untuk bentuk garam dioctyl sulfosuccinate). Jalankan semula saluran pemetaan dengan pengenalpastian yang dibetulkan.
- **Jalankan semula ramalan TxGNN** selepas DrugBank ID berjaya dipetakan ke graf pengetahuan.
- **Isi jurang data**: Dapatkan amaran label (DG001) dan maklumat MOA (DG002) untuk membolehkan penskrinan keselamatan S1 jika ramalan kemudiannya dijana.
- **Jika tiada ramalan muncul selepas pemetaan semula**, kelaskan ubat ini sebagai **keutamaan rendah untuk ubah tujuan ubat** dan arkibkan.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

