---
layout: default
title: Aminophylline Dihydrate
parent: Low Evidence (L4-L5)
nav_order: 55
evidence_level: L5
indication_count: 0
---

# Aminophylline Dihydrate
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

# AMINOPHYLLINE DIHYDRATE: Penilaian Penjelmaan Ubat — Paket Bukti Tidak Lengkap

## Ringkasan Satu Ayat

Aminophylline Dihydrate ialah bronkodilator metilksantin yang digunakan secara meluas untuk keadaan pernafasan termasuk asma dan COPD.
Paket Bukti ini tidak mengandungi **tiada indikasi kegunaan baru yang diramalkan oleh TxGNN**, dan dua jurang data kritikal — mekanisme tindakan dan amaran keselamatan rasmi — masih belum diselesaikan.
Penilaian penjelmaan ubat yang lengkap **tidak dapat diselesaikan** sehingga jurang-jurang ini diperbaiki; keputusan yang disyorkan ialah **Tahan**.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Tidak ditangkap dalam Paket Bukti ini |
| Indikasi Kegunaan Baru yang Diramalkan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 — ramalan model tiada; tiada kajian sokongan yang boleh dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada indikasi yang diramalkan oleh TxGNN yang dikembalikan dalam Paket Bukti ini, jadi tiada rasional mekanistik rasmi untuk indikasi kegunaan baru yang dapat dibina.

Data mekanisme tindakan yang terperinci tidak tersedia dalam Paket Bukti semasa (Jurang Data DG002). Berdasarkan pengetahuan farmakologi yang mapan, Aminophylline ialah garam teofelin dan etilena diamina yang tergolong dalam kelas metilksantin. Ia dipahami bertindak terutamanya sebagai penghambat fosfodiesterase tidak terpilih dan antagonis reseptor adenosin, menghasilkan relaksasi otot licin, bronkodilatasi, dan kesan jantung kronotropik dan inotropik positif yang ringan. Peranan klinikal yang telah ditubuhkan ialah dalam pengurusan bronkospasma yang berkaitan dengan asma dan COPD.

Tanpa indikasi kegunaan baru yang diramalkan daripada model TxGNN, analisis jambatan mekanistik — tiang pusat penilaian penjelmaan ubat — tidak dapat diteruskan. Bahagian ini akan diisi setelah ramalan TxGNN tersedia dan jurang data MOA diselesaikan.

---

## Maklumat Pasaran Malaysia

Satu rekod pendaftaran wujud dalam pangkalan data NPRA Malaysia untuk Aminophylline Dihydrate; bagaimanapun, semua medan lesen yang berkaitan (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak ditangkap semasa pengambilan data dan tiada dalam Paket Bukti ini.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|----------------------|--------------|-------------|---------------------|
| Tidak diperolehi | Tidak diperolehi | Tidak diperolehi | Tidak diperolehi |

Untuk melengkapkan jadual ini, rekod lesen NPRA mesti disiasat semula dan teks indikasi yang diluluskan diambil.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan paket rasmi untuk maklumat keselamatan.

Kedua-dua amaran utama dan kontraindikasi untuk Aminophylline Dihydrate ditandai sebagai jurang data yang menghalang (DG001) dalam Paket Bukti ini. Tiada data interaksi ubat–ubat yang dikembalikan daripada pertanyaan DrugBank. Sehingga sisipan paket diperolehi dan dianalisis, tiada profil keselamatan dapat dipersembahkan, dan ubat ini **tidak dapat maju ke skrining kelayakan klinikal**.

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tahan**

**Rasional:**
Paket Bukti adalah tidak lengkap secara struktur — saluran ramalan TxGNN tidak mengembalikan indikasi calon, dan dua jurang data keutamaan tertinggi (amaran keselamatan dan MOA) tetap tidak diselesaikan, menghalang kedua-dua skrining keselamatan dan analisis mekanistik.

**Untuk meneruskan, perkara berikut diperlukan:**

- **Selesaikan DG001 (Menghalang):** Muat turun PDF sisipan paket berdaftar Malaysia daripada NPRA dan ambil amaran utama, kontraindikasi, dan maklumat dos
- **Selesaikan DG002 (Tinggi):** Soal API DrugBank menggunakan INN "aminophylline" atau "theophylline" untuk mendapatkan ID DrugBank, MOA penuh, dan kategori ubat
- **Dapatkan ramalan TxGNN:** Sahkan bahawa Aminophylline Dihydrate (atau moiti aktifnya theophylline) hadir dalam graf pengetahuan TxGNN; jalankan semula saluran ramalan KG + DL dan isi `predicted_indications`
- **Lengkapkan rekod lesen NPRA:** Siasat semula NPRA untuk mengambil nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk 1 produk berdaftar
- **Jana semula Paket Bukti** setelah semua empat item di atas diselesaikan, kemudian teruskan ke skrining keselamatan S1 lengkap dan penilaian mekanistik

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

