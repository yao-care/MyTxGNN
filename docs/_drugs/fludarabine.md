---
layout: default
title: Fludarabine
parent: Low Evidence (L4-L5)
nav_order: 348
evidence_level: L4
indication_count: 10
---

# Fludarabine
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **10** 
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

# Fludarabine: Dari B-Cell Chronic Lymphocytic Leukemia ke Plasma Cell Myeloma

## Ringkasan Satu Ayat

Fludarabine adalah analog nukleosida purin yang secara historis digunakan melawan B-cell chronic lymphocytic leukemia (CLL) dan keganasan B-cell indolen terkait (teks indikasi khusus regulasi tidak dikembalikan dalam pengambilan data ini; framing ini diambil dari literatur sekitarnya).
Model TxGNN memprediksi bahwa ini mungkin efektif untuk **Plasma Cell Myeloma**, dengan **0 uji klinis** dan **20 publikasi** yang saat ini terkait dengan pasangan ini — tetapi sebagian besar literatur tersebut menggambarkan peran fludarabine sebagai agen lymphodepleting/transplant-conditioning daripada pengobatan antimyeloma langsung.

---

## Tinjauan Cepat

| Item | Isi |
|------|-----|
| Indikasi Asli | Tidak ditentukan dalam data regulasi yang disediakan; konteks literatur menunjukkan B-cell chronic lymphocytic leukemia (CLL) dan keganasan limfoid indolen terkait |
| Indikasi Baru yang Diprediksi | Plasma Cell Myeloma |
| Skor Prediksi TxGNN | 99.82% |
| Tingkat Bukti | L4 |
| Status Pasar Malaysia | Dipasarkan (Marketed) |
| Jumlah Registrasi | 2 |
| Keputusan yang Direkomendasikan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme tindakan terperinci tidak tersedia untuk Fludarabine dalam paket bukti ini (`original_moa: [Data Gap]`). Berdasarkan literatur sekitarnya, fludarabine adalah analog nukleosida purin yang menghambat DNA polymerase dan ribonucleotide reductase, menghasilkan efek sitostatik dan imunosupresif/lymphodepleting yang mendalam. Properti ganda ini adalah yang menghubungkannya dengan plasma cell myeloma dalam grafik pengetahuan TxGNN: fludarabine adalah komponen inti regimen reduced-intensity conditioning (RIC) sebelum transplantasi stem sel allogenik dan regimen lymphodepletion sebelum infusi CAR-T BCMA/CD19 — keduanya digunakan pada multiple myeloma relapsed/refractory.

Namun, peringkat relevansi paket bukti itu sendiri jujur tentang keterbatasan: dalam hampir semua 20 publikasi terkait, fludarabine muncul sebagai agen imunosupresif/conditioning adjunktif yang memungkinkan engraftment transplantasi atau CAR-T, bukan sebagai terapi antimyeloma langsung dalam haknya sendiri. Hanya satu studi — laporan in vitro/in vivo tahun 2007 (PMID 17976186) — secara langsung menguji aktivitas sitostatik fludarabine terhadap sel myeloma, menunjukkan hambatan pertumbuhan sel myeloma RPMI8226 melalui pensinyalan Akt/NF-κB yang berkurang. Tidak ada uji klinis dalam dataset ini yang dirancang untuk menguji fludarabine sebagai agen antimyeloma mandiri atau kombinasi. Hubungan mekanistik oleh karena itu masuk akal tetapi tidak langsung, dan skor kesamaan tinggi model kemungkinan mencerminkan co-occurrence padat fludarabine dengan myeloma dalam konteks transplantasi/CAR-T daripada efek farmakologis langsung yang divalidasi.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar (0 uji klinis dikembalikan untuk kueri Fludarabine × Plasma Cell Myeloma; lihat id `query_log` 3–4).

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Temuan Kunci |
|------|-------|------|--------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preklinik (in vitro/in vivo) | European Journal of Haematology | Fludarabine secara langsung menghambat pertumbuhan sel myeloma RPMI8226, dengan fosforilasi Akt yang berkurang — satu-satunya bukti langsung sitostatik antimyeloma intrinsik dalam dataset ini |
| [7781758](https://pubmed.ncbi.nlm.nih.gov/7781758/) | 1995 | Laporan awal | European Journal of Haematology | Deskripsi klinis awal aktivitas fludarabine dalam plasma cell leukemia, entitas yang terkait dengan myeloma |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 (Cohort) | American Journal of Clinical Oncology | Bortezomib + fludarabine + melphalan (± total marrow irradiation) sebagai conditioning allogeneic HSCT untuk myeloma berisiko tinggi/relapsed — fludarabine digunakan sebagai conditioning imunosupresif, bukan agen antitumor mandiri |
| [37833271](https://pubmed.ncbi.nlm.nih.gov/37833271/) | 2023 | Cohort | Blood Cancer Journal | Dibandingkan bendamustine vs. fludarabine/cyclophosphamide lymphodepletion sebelum BCMA CAR-T pada multiple myeloma — peran fludarabine terbatas pada lymphodepletion pre-CAR-T |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 (cohort kecil) | Leukemia Research Reports | Split-dose busulfan/fludarabine/cyclophosphamide sebagai conditioning allogeneic SCT untuk myeloma dan myelofibrosis (2 pasien MM terdaftar) |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Cohort retrospektif | Bone Marrow Transplantation | Fludarabine + treosulfan reduced-toxicity conditioning sebelum allogeneic SCT pada 34 pasien myeloma |
| [33784005](https://pubmed.ncbi.nlm.nih.gov/33784005/) | 2021 | Phase 1 | Clinical and Translational Medicine | Anti-BCMA CAR-T pada MM relapsed/refractory dan plasma cell leukemia; fludarabine/cyclophosphamide digunakan untuk lymphodepletion sebelum infusi CAR-T |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Hasil standar perawatan dengan ciltacabtagene autoleucel (cilta-cel) pada R/R MM di 16 pusat AS; conditioning berbasis fludarabine biasanya mendahului infusi CAR-T |
| [36690811](https://pubmed.ncbi.nlm.nih.gov/36690811/) | 2023 | Phase 1 | Nature Medicine | Uji klinis first-in-human Phase 1 UNIVERSAL dari anti-BCMA CAR-T allogeneic (ALLO-715) pada R/R MM mengikuti conditioning lymphodepletion |
| [31058154](https://pubmed.ncbi.nlm.nih.gov/31058154/) | 2019 | Tinjauan | Frontiers in Medicine | Tinjauan pencitraan [18F]-fludarabine PET untuk pementasan keganasan hematologi — aplikasi pencitraan diagnostik, bukan terapi |

---

## Informasi Pasar Malaysia

Catatan NPRA Malaysia mengkonfirmasi **2 registrasi dipasarkan** untuk Fludarabine (status pasar: Marketed/Marketed), tetapi nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui untuk registrasi ini tidak dikembalikan dalam pengambilan data ini — kedua catatan lisensi dalam paket bukti berisi bidang kosong.

---

## Sitotoksisitas

Fludarabine adalah agen kemoterapi sitotoksik konvensional (antimetabolit analog nukleosida purin), sehingga bagian ini berlaku.

| Item | Isi |
|------|-----|
| Klasifikasi Sitotoksisitas | Sitotoksik konvensional (analog nukleosida purin / antimetabolit) |
| Risiko Myelosuppression | Silakan lihat peringatan dan tindakan pencegahan dalam leaflet kemasan |
| Klasifikasi Emetogenisitas | Silakan lihat peringatan dan tindakan pencegahan dalam leaflet kemasan |
| Item Pemantauan | Silakan lihat peringatan dan tindakan pencegahan dalam leaflet kemasan |
| Perlindungan Penanganan | Harus ditangani sesuai protokol penanganan obat sitotoksik/berbahaya institusional |

---

## Pertimbangan Keselamatan

Silakan lihat leaflet kemasan untuk informasi keselamatan. Data peringatan kunci, kontraindikasi, dan interaksi obat tidak tersedia dalam paket bukti ini (kueri DDI mengembalikan tidak ada hasil), dan peringatan label TFDA/NPRA ditandai sebagai **Blocking** kesenjangan data (DG001) yang harus diselesaikan sebelum evaluasi keselamatan apa pun (S1) dapat dilanjutkan.

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Prediksi plasma cell myeloma didukung hanya oleh bukti tidak langsung — peran fludarabine yang sudah ditetapkan sebagai agen lymphodepletion/conditioning untuk prosedur transplantasi dan CAR-T pada myeloma, ditambah satu studi preklinik tahun 2007 yang menunjukkan aktivitas antitumor langsung. Tidak ada uji klinis dalam dataset ini yang menguji fludarabine sebagai terapi antimyeloma, dan kesenjangan data keselamatan pemblokiran (DG001 — peringatan label TFDA/NPRA dan kontraindikasi) mencegah kemajuan apa pun ke tinjauan keselamatan.

**Untuk melanjutkan, berikut ini diperlukan:**
- Label produk TFDA/NPRA (peringatan, kontraindikasi) untuk menyelesaikan DG001 sebelum evaluasi S1 keselamatan apa pun
- Data mekanisme tindakan yang dikonfirmasi (DG002) melalui DrugBank untuk mengklarifikasi apakah aktivitas antimyeloma fludarabine adalah efek farmakologis asli atau artefak dari co-occurrence agen conditioning-nya
- Studi yang secara khusus menguji fludarabine (sendiri atau dalam kombinasi) sebagai agen antimyeloma, daripada sebagai conditioning transplantasi/CAR-T
- Catatan lisensi Malaysia lengkap (nomor otorisasi, nama produk, bentuk dosis, teks indikasi yang disetujui) untuk 2 produk terdaftar

**Catatan:** dalam set prediksi obat yang sama, dua kandidat lainnya membawa bukti yang secara material lebih kuat — myelodysplastic syndrome (peringkat 7: L1, tahap keputusan S3, "Lanjutkan dengan Safeguards") dan indolent plasma cell myeloma (peringkat 4: L2, tahap keputusan S2, "Lanjutkan dengan Safeguards") — dan dapat memerlukan evaluasi terpisah dan khusus.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

