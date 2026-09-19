---
layout: default
title: Clofazimine
parent: Low Evidence (L4-L5)
nav_order: 229
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **3** 
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

# Clofazimine: Dari Kusta (Penyakit Hansen) ke Pneumocystosis

## Ringkasan Satu Kalimat

Clofazimine adalah agen antimikobarteri riminofenazin yang telah mapan dalam terapi multidrug kusta dan rejimen tuberkulosis resistan multidrug.
Model TxGNN meramalkan bahwa ia mungkin efektif untuk **Pneumocystosis**, dengan skor prediksi **99.90%**, tetapi **0 uji klinis** dan **0 publikasi** saat ini mendukung arah ini, dan penjelasan mekanis model sendiri menandai prediksi ini sebagai kemungkinan artefak ko-kemunculan grafik pengetahuan daripada tautan farmakologis sejati.

---

## Gambaran Singkat

| Item | Konten |
|------|--------|
| Indikasi Asli | Kusta (Penyakit Hansen) / MDR-TB — berdasarkan pengetahuan farmakologis yang mapan tentang clofazimine; tidak dikonfirmasi oleh teks lisensi NPRA dalam Evidence Pack ini (semua 4 catatan lisensi memiliki kolom indikasi kosong — lihat Data Gap DG001) |
| Indikasi Baru yang Diprediksi | Pneumocystosis |
| Skor Prediksi TxGNN | 99.90% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Registrasi | 4 |
| Rekomendasi Keputusan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme kerja yang terperinci tidak tersedia (Data Gap DG002). Berdasarkan informasi yang diketahui, clofazimine adalah senyawa riminofenazin yang mekanismenya yang mapan melibatkan pengikatan DNA, induksi spesies oksigen reaktif (ROS), dan penghambatan jalur saluran K+ / fosfolipase A2 — profil antimikobakteri dan imunomodulatif yang digunakan melawan *M. leprae* dan *M. tuberculosis*.

*Pneumocystis jirovecii*, organisme penyebab pneumocystosis, adalah jamur dengan komposisi dinding sel dan jalur metabolik yang secara substansial berbeda dari mikobakteri. Tidak ada aktivitas antijamur yang terdokumentasi untuk clofazimine yang akan secara mekanis mendukung prediksi ini. Penjelasan Evidence Pack sendiri untuk peringkat ini menyatakan bahwa skor TxGNN yang tinggi kemungkinan mencerminkan kedekatan grafik antara clofazimine dan pneumocystosis melalui cluster simpul "infeksi oportunistik pada populasi imunokompromi" bersama, daripada hubungan farmakologis sejati — dan secara eksplisit menilai kredibilitas tautan ini sebagai rendah.

Dua kandidat peringkat lebih rendah juga dihasilkan: **malaria** (99.60%, rank 6229) memiliki dasar teoretis yang agak lebih masuk akal — lipofilitasitas clofazimine, penetrasi membran, dan mekanisme induksi ROS secara konseptual tumpang tindih dengan mekanisme antimalarial berbasis stres oksidatif, dan penjelasan mencatat laporan literatur sebelumnya tentang aktivitas antiplasmodial in vitro, meskipun penelusuran PubMed/ClinicalTrials/ICTRP Evidence Pack sendiri mengembalikan nol hit — menunjukkan kesenjangan pengumpulan bukti daripada ketiadaan literatur sejati, dan menjamin pencarian tindak lanjut yang ditargetkan. **Abnormalitas sekresi gastrin** (99.57%, rank 6584) tidak memiliki dasar mekanis yang diketahui dan dinilai sebagai kemungkinan kebisingan grafik.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar

---

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia

---

## Informasi Pasar Malaysia

Empat otorisasi tercatat dengan NPRA Malaysia (total_licenses = 4), tetapi detail tingkat produk (nomor lisensi, nama produk, bentuk sediaan, teks indikasi yang disetujui) tidak diisi dalam Evidence Pack ini — ini adalah kesenjangan data yang memerlukan pencarian langsung NPRA untuk diselesaikan.

---

## Pertimbangan Keamanan

Silakan merujuk pada maklumat kemasan untuk informasi keamanan. (Data peringatan utama, kontraindikasi, dan interaksi obat semuanya ditandai sebagai kesenjangan data dalam Evidence Pack ini — DG001, Blocking severity — dan tidak dapat diambil.)

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Indikasi yang diprediksi peringkat teratas (pneumocystosis) tidak didukung oleh bukti uji klinis atau literatur apa pun, dan analisis mekanis Evidence Pack sendiri menilai tautan yang diturunkan dari grafik sebagai ko-kemunculan berkredibilitas rendah daripada farmakologi sejati. Selain itu, data peringatan TFDA/NPRA dan kesenjangan kontraindikasi adalah Blocking-severity gap, yang mencegah kasus memasuki tahap pra-skrining keamanan S1 terlepas dari indikasi.

**Untuk melanjutkan, diperlukan hal berikut:**
- Maklumat kemasan NPRA/TFDA (peringatan, kontraindikasi) — menyelesaikan Blocking Data Gap DG001, diperlukan sebelum penilaian keamanan S1 apa pun
- Detail mekanisme kerja DrugBank — menyelesaikan Data Gap High-severity DG002
- Teks lisensi NPRA yang dikonfirmasi untuk 4 registrasi Malaysia yang ada (nomor lisensi, nama produk, bentuk sediaan, indikasi yang disetujui)
- Jika mengejar kandidat malaria bukan pneumocystosis: pencarian literatur eksternal yang ditargetkan untuk data antiplasmodial in vitro/in vivo pada clofazimine, karena pencarian otomatis Evidence Pack ini menemukan nol hit meskipun penjelasan mengutip laporan sebelumnya

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

