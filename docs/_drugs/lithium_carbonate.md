---
layout: default
title: Lithium Carbonate
parent: Low Evidence (L4-L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Litium Karbonat: Dari Penstabilan Suasana Hati kepada Pseudoakondroplas

## Ringkasan Satu Kalimat

Litium Karbonat adalah agen psikiatri yang telah mapan dan banyak digunakan sebagai penstabil suasana hati untuk gangguan bipolar dan kondisi terkait. Model TxGNN meramalkan ia mungkin memiliki potensi utiliti dalam **Pseudoakondroplas**, sebuah displasia skeletal yang jarang disebabkan oleh mutasi gen COMP. Namun, dengan **tidak ada uji klinis** dan **tidak ada publikasi** yang secara langsung mendukung indikasi ini, bukti saat ini terbatas pada prediksi model semata-mata (Level L5).

---

## Gambaran Ringkas

| Perkara | Isi |
|--------|-----|
| Indikasi Asal | Data pendaftaran Malaysia tidak tersedia |
| Indikasi Baru yang Diprediksi | Pseudoakondroplas |
| Skor Prediksi TxGNN | 99.98% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 1 |
| Keputusan yang Direkomendasikan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme kerja yang terperinci tidak tersedia dari Paket Bukti (celah data MOA DrugBank). Berdasarkan farmakologi yang diketahui, Litium Karbonat adalah kation monovalent yang menjalankan efek utamanya melalui penghambatan **GSK-3β (Glycogen Synthase Kinase-3 beta)**, sehingga mengaktifkan **jalur sinyal Wnt/β-catenin**. Ia juga memodulasi metabolisme fosfat inositol dan mempengaruhi beberapa jalur neurotrofik termasuk BDNF.

Pseudoakondroplas disebabkan oleh mutasi yang meningkatkan fungsi pada gen **COMP (cartilage oligomeric matrix protein)**, yang menyebabkan salah lipatan protein COMP, akumulasi patologisnya dalam retikulum endoplasma (ER) kondrosit, dan stress ER serta kematian sel yang dihasilkan. Secara teoritis, penghambatan GSK-3β oleh Litium dapat mengurangi stress ER dan mempromosikan kelangsungan hidup osteoblas melalui aktivasi jalur Wnt/β-catenin, yang memainkan peran yang diketahui dalam pengembangan skeletal dan homeostasis tulang.

Namun, tautan mekanistik antara aktivasi Wnt/β-catenin Litium dan koreksi agregasi protein COMP tetap **sangat spekulatif dan belum terbukti**. Saat ini tidak ada model praklinik yang diterbitkan (lini sel atau hewan) yang menunjukkan bahwa pengobatan Litium mengurangi penanda stress ER terkait COMP atau meningkatkan fenotipe skeletal pseudoakondroplas. Prediksi ini harus ditafsirkan sebagai sinyal pembangkit hipotesis dari model grafik pengetahuan daripada temuan yang dapat ditindaklanjuti secara klinis.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar.

---

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia.

---

## Informasi Pasar Malaysia

Paket Bukti mencatat 1 pendaftaran aktif untuk Litium Karbonat di Malaysia; namun, rincian pendaftaran terperinci (nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui) tidak diisi dalam ekstraksi data saat ini. Silakan rujuk langsung ke Daftar Ubat Badan Peraturan Farmasi Nasional (NPRA) untuk detail produk lengkap.

---

## Pertimbangan Keselamatan

Silakan rujuk pada selebaran kemasan untuk informasi keselamatan.

> **Catatan:** Peringatan selebaran kemasan, kontraindikasi, dan data interaksi ubat diidentifikasi sebagai celah data dalam Paket Bukti ini (DG001). Litium Karbonat adalah ubat dengan indeks terapi yang sempit dan memerlukan pemantauan ubat terapeutik. Sebelum eksplorasi repurposing apa pun, tinjauan keselamatan lengkap dari informasi peraturan resmi yang disetujui NPRA harus dilakukan.

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tahan**

**Alasan:**
Model TxGNN memberikan skor prediksi yang sangat tinggi (99.98%) untuk Litium Karbonat untuk pseudoakondroplas, tetapi ini saat ini didukung oleh **tidak ada uji klinis, tidak ada literatur yang diterbitkan, dan tidak ada data eksperimental praklinik** — menjadikan ini hipotesis komputasi murni (Tingkat Bukti L5). Tautan mekanistik yang diusulkan (penghambatan GSK-3β → pengurangan stress ER → koreksi agregasi COMP) secara biologis tidak langsung dan belum divalidasi, dan basis bukti keseluruhan tidak cukup untuk membenarkan investasi klinis atau translasional pada tahap ini.

**Untuk melanjutkan, berikut ini diperlukan:**

- **Selesaikan Celah Data DG001**: Unduh dan parsing PDF selebaran kemasan yang disetujui NPRA untuk mengekstrak peringatan resmi, kontraindikasi, dan bimbingan dosis sebelum penilaian keselamatan apa pun dapat dilakukan
- **Selesaikan Celah Data DG002**: Kueri API DrugBank untuk mengkonfirmasi profil mekanisme kerja lengkap untuk Litium Karbonat
- **Validasi praklinik**: Lakukan studi in vitro pada model kondrosit bermutasi COMP (misalnya, kondrosit yang berasal dari iPSC COMP-p.T585M) untuk menentukan apakah Litium atau penghambat GSK-3β mengurangi penanda stress ER
- **Tinjauan cakupan literatur**: Lakukan pencarian yang lebih luas menggabungkan "lithium" dengan "stress ER," "kondrosit," "COMP," dan "displasia skeletal" untuk menangkap penelitian mekanistik apa pun yang tidak tertangkap oleh kueri pasangan ubat-penyakit saat ini
- **Tinjau sindrom WHIM secara terpisah**: Di antara indikasi teratas ke-10 yang diprediksi, sindrom WHIM (Rank 9) menyajikan hipotesis yang lebih koheren secara mekanistik — efek mobilisasi neutrofil Litium yang diketahui selaras arah dengan patofisiologi WHIM dari retensi neutrofil sumsum tulang. Kandidat ini mungkin layak untuk tinjauan bukti khusus sebelum pseudoakondroplas

---

*Laporan ini dihasilkan untuk tujuan referensi penelitian semata dan tidak merupakan saran perubatan. Semua kandidat repurposing ubat memerlukan validasi klinis sebelum aplikasi terapeutik apa pun.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

