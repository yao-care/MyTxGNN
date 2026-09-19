---
layout: default
title: Acalabrutinib Maleate
parent: Low Evidence (L4-L5)
nav_order: 15
evidence_level: L5
indication_count: 0
---

# Acalabrutinib Maleate
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

# ACALABRUTINIB MALEATE: Penilaian Penggunaan Kembali — Data Tidak Mencukupi untuk Melengkapi Penilaian Penuh

---

## Ringkasan Satu Kalimat

Acalabrutinib maleate adalah agen antikanker tersasaran (penghambat BTK) yang saat ini terdaftar di Malaysia, diindikasikan untuk keganasan hematologi seperti leukemia limfositik kronis dan limfoma sel mantel.
Namun, **tidak ada prediksi TxGNN yang dihasilkan** dalam Paket Bukti ini karena pemetaan ID DrugBank yang hilang, dan bidang data kritis — termasuk teks indikasi yang disetujui, mekanisme aksi, dan peringatan keselamatan — tidak ada.
Penilaian penggunaan kembali yang lengkap **tidak dapat dilanjutkan** sampai celah-celah ini diselesaikan.

---

## Gambaran Singkat

| Item | Konten |
|------|--------|
| Indikasi Asli | Tidak tersedia dalam data saat ini |
| Indikasi Baru yang Diprediksi | Tidak ada prediksi yang dihasilkan |
| Skor Prediksi TxGNN | N/A |
| Tingkat Bukti | L5 — Belum ada prediksi yang dijalankan |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 1 |
| Keputusan yang Direkomendasikan | **Tahan** |

---

## Mengapa Tidak Ada Prediksi yang Tersedia

Saluran pipa penggunaan kembali TxGNN memerlukan **ID DrugBank** yang valid untuk menemukan simpul obat dalam grafik pengetahuan dan menghitung skor asosiasi obat-penyakit. Untuk pengajuan ini, `drugbank_id` adalah `null`, yang berarti:

1. Obat tidak dapat ditambatkan dalam grafik pengetahuan TxGNN.
2. Baik metode grafik pengetahuan (KG) maupun metode pembelajaran mendalam (DL) tidak menghasilkan skor kandidat.
3. Tanpa daftar kandidat yang terskor, tidak ada indikasi prediksi yang dipecah peringkat dapat dilaporkan.

Selain itu, data mekanisme aksi (MOA) tidak tersedia, mencegah analisis kelayakan mekanistik apa pun bahkan jika indikasi kandidat diidentifikasi secara manual.

Acalabrutinib diketahui dari literatur terpublikasi adalah **penghambat tirosin kinase Bruton (BTK) generasi kedua, kovalen**. BTK memainkan peran sentral dalam pensinyalan reseptor sel B, menjadikannya relevan tidak hanya untuk indikasi hematologi yang disetujuinya tetapi berpotensi untuk kondisi autoimun dan inflamasi. Namun, wawasan ini tidak dapat dimasukkan secara formal ke dalam laporan TxGNN tanpa menyelesaikan saluran pipa.

---

## Informasi Pasar Malaysia

Obat ini dikonfirmasi sebagai **dipasarkan** di Malaysia (1 pendaftaran aktif melalui NPRA). Namun, catatan lisensi terperinci yang dikembalikan kosong — nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui semuanya tidak ada dalam Paket Bukti ini.

| Nomor Otorisasi | Nama Produk | Bentuk Dosis | Indikasi yang Disetujui |
|-----------------|------------|-------------|------------------------|
| *(Tidak dikembalikan oleh kueri)* | *(Tidak dikembalikan)* | *(Tidak dikembalikan)* | *(Tidak dikembalikan)* |

> **Catatan:** Log kueri NPRA mengkonfirmasi 1 hasil ditemukan (ID kueri 1, status: sukses). Bidang kosong menunjukkan masalah ekstraksi atau penguraian data dalam aliran saluran pipa saat ini, bukan ketiadaan pendaftaran.

---

## Sitotoksisitas

Acalabrutinib adalah terapi antineoplastik tersasaran. Berikut ini berlaku menunggu pengambilan vademekum lengkap:

| Item | Konten |
|------|--------|
| Klasifikasi Sitotoksisitas | Terapi tersasaran — penghambat BTK kovalen |
| Risiko Supresi Sumsum Tulang | Silakan lihat peringatan dan tindakan pencegahan vademekum |
| Klasifikasi Emetogenisitas | Rendah (khas untuk agen penghambat kecil oral tersasaran) |
| Item Pemantauan | CBC dengan diferensial, tes fungsi hati, fungsi ginjal |
| Perlindungan Penanganan | Ikuti protokol penanganan obat sitotoksik institusional |

---

## Pertimbangan Keselamatan

Silakan lihat vademekum untuk informasi keselamatan.

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Saluran pipa prediksi TxGNN tidak menghasilkan indikasi yang terskor apa pun karena ID DrugBank yang hilang, dan semua detail keselamatan dan indikasi dari catatan regulasi tidak ada — Paket Bukti ini tidak berisi data yang cukup untuk mendukung penilaian penggunaan kembali.

**Untuk melanjutkan, berikut yang diperlukan:**

- **Selesaikan pemetaan ID DrugBank**: Kueri DrugBank untuk "acalabrutinib" (INN bentuk bebas); bentuk garam maleate mungkin tidak cocok secara langsung. ID yang diharapkan: DB12116. Jalankan ulang `scripts/run_kg_prediction.py` setelah pemetaan.
- **Urai ulang catatan lisensi NPRA**: Kueri NPRA mengembalikan 1 hasil tetapi semua bidang kosong. Tinjau respons mentah dalam `data/raw/malaysia_fda_drugs.json` dan perbaiki ekstraksi bidang dalam `scripts/process_fda_data.py`.
- **Ambil MOA dari DrugBank**: Setelah ID DrugBank dikonfirmasi, tarik bidang `pharmacodynamics`, `mechanism-of-action`, dan `categories` melalui API DrugBank.
- **Unduh PDF vademekum**: Dapatkan vademekum yang disetujui NPRA untuk mengekstrak indikasi yang disetujui, peringatan utama, dan kontraindikasi. Ini ditandai sebagai kesenjangan data **Pemblokiran** (DG001).
- **Jalankan ulang pembuatan Paket Bukti** setelah empat item di atas diselesaikan untuk menghasilkan laporan grading bukti penuh L1–L5.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

