---
layout: default
title: Cyclophosphamide
parent: Low Evidence (L4-L5)
nav_order: 240
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
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

# Cyclophosphamide: Dari Kemoterapi Alkilasi ke Leukemia Myeloid

## Ringkasan Satu Kalimat

> Cyclophosphamide adalah agen alkilasi nitrogen mustard klasik yang telah lama digunakan sebagai komponen inti dari kemoterapi kombinasi dan sebagai imunosupresan.
> Model TxGNN memprediksi ia mungkin efektif untuk **Leukemia Myeloid**,
> tetapi saat ini **tidak ada uji klinis** dan **tidak ada publikasi** dalam dataset ini yang mendukung arah spesifik ini — prediksi ini berdasarkan pada plausibilitas mekanistik semata.

---

## Ringkasan Cepat

| Item | Konten |
|------|--------|
| Indikasi Asli | Tidak tersedia dalam dataset ini (teks label dan daftar indikasi adalah kesenjangan data). Cyclophosphamide umumnya dikenal sebagai agen antineoplastik/imunosupresan spektrum luas yang digunakan dalam limfoma, leukemia dan regimen kemoterapi kombinasi lainnya. |
| Indikasi Baru yang Diprediksi | Leukemia Myeloid |
| Skor Prediksi TxGNN | 99.47% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Jumlah Pendaftaran | 1 |
| Rekomendasi Keputusan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Data mekanisme aksi terperinci tidak tersedia dalam paket bukti ini (ditandai sebagai kesenjangan data keparahan tinggi). Berdasarkan pengetahuan farmakologi umum, cyclophosphamide adalah agen alkilasi nitrogen mustard yang diaktifkan secara metabolis untuk membentuk metabolit penyambung DNA, menghasilkan efek sitotoksik lebih disukai dalam populasi sel yang membelah dengan cepat — prinsip yang sama yang mendasari peran yang sudah ditetapkan dalam limfoma, leukemia dan regimen kemoterapi kombinasi lainnya.

Leukemia myeloid dicirikan oleh populasi blast myeloid yang sangat proliferatif, yang secara teoritis rentan terhadap sitotoksisitas agen alkilasi dengan cara yang sama nitrogen mustard lainnya digunakan dalam protokol pengobatan leukemia. Ini memberikan prediksi TxGNN plausibilitas mekanistik yang masuk akal.

Namun, koneksi ini harus diinterpretasi dengan hati-hati: karena cyclophosphamide sudah merupakan komponen yang mapan dalam banyak regimen kemoterapi leukemia dan limfoma (misalnya, regimen kondisioning, protokol tipe CHOP), tidak jelas apakah "leukemia myeloid" di sini mewakili sinyal repurposing yang benar-benar baru atau hanya mencerminkan indikasi yang sudah ada dan nyata yang tidak ditangkap dalam field `original_indications` dari dataset ini. Ambiguitas ini harus diselesaikan sebelum tindakan lebih lanjut diambil.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar.

---

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia.

---

## Informasi Pasar Malaysia

Rekam Malaysia (NPRA) menunjukkan produk dipasarkan dengan **1 pendaftaran**, tetapi field lisensi terperinci (nomor lisensi, nama produk, bentuk dosis, pabrikan, teks indikasi yang disetujui) tidak diisi dalam dataset ini dan tidak dapat diekstrak.

---

## Sitotoksisitas

Cyclophosphamide adalah agen antineoplastik sitotoksik yang mapan (indikasi yang diprediksi/terkait dalam paket ini semuanya onkologis), jadi bagian ini berlaku.

| Item | Konten |
|------|--------|
| Klasifikasi Sitotoksisitas | Sitotoksik konvensional (agen alkilasi, kelas nitrogen mustard) |
| Risiko Supresi Sumsum | Tinggi — leukopenia dan trombositopenia adalah toksisitas pembatas dosis yang terdokumentasi dengan baik dari kelas obat ini |
| Klasifikasi Emetogenisitas | Sedang hingga Tinggi (tergantung dosis; lebih tinggi dengan pemberian IV) |
| Item Pemantauan | CBC dengan diferensial, hitung platelet, fungsi ginjal dan hati, urinalisis (risiko sistitis hemoragik) |
| Perlindungan Penanganan | Ya — memerlukan tindakan pencegahan penanganan obat sitotoksik/berbahaya |

Ambang batas toksisitas spesifik dan jadwal pemantauan harus dikonfirmasi terhadap sisipan kemasan resmi setelah tersedia, karena tidak ada data toksisitas spesifik produk yang ada dalam paket bukti ini.

---

## Pertimbangan Keselamatan

Silakan rujuk sisipan kemasan untuk informasi keselamatan.

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Prediksi didukung hanya oleh plausibilitas mekanistik (Tingkat Bukti L5) tanpa uji klinis atau literatur yang teridentifikasi, dan kesenjangan data keparahan Pemblokiran (label NPRA yang hilang/peringatan kontraindikasi) mencegah bahkan penilaian keselamatan awal.

**Untuk melanjutkan, berikut ini diperlukan:**
- PDF label NPRA (peringatan, kontraindikasi) untuk mengatasi kesenjangan data Pemblokiran
- Mekanisme aksi yang dikonfirmasi DrugBank untuk memvalidasi rasional mekanistik
- Klarifikasi apakah "leukemia myeloid" adalah indikasi yang sudah ada sebelumnya yang tidak ditangkap dalam `original_indications`, atau prediksi baru yang asli
- Pencarian literatur/uji klinis yang ditargetkan khusus untuk cyclophosphamide dalam leukemia myeloid untuk membangun tingkat bukti yang lebih tinggi sebelum keputusan Go apa pun

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

