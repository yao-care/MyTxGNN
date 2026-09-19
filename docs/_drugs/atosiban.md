---
layout: default
title: Atosiban
parent: Low Evidence (L4-L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: Dari Persalinan Praterm ke Glaukoma Herediter Primer

## Ringkasan Satu Kalimat

Atosiban adalah penghambat reseptor oksitosin yang terdaftar di Malaysia sebagai agen tokolitis untuk menghambat persalinan praterm. Model TxGNN menempatkan **Glaukoma Herediter Primer** sebagai indikasi baru yang diprediksi teratas, dengan skor prediksi 99.92%. Namun, prediksi ini didukung oleh **tidak ada uji klinis dan tidak ada literatur yang dipublikasikan**, dan mekanisme yang diusulkan berlawanan arah dengan tujuan terapeutik.

---

## Tinjauan Cepat

| Item | Konten |
|------|--------|
| Indikasi Asli | Penghambatan persalinan praterm (tokolisis) |
| Indikasi Baru yang Diprediksi | Glaukoma Herediter Primer |
| Skor Prediksi TxGNN | 99.92% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Pendaftaran | 2 |
| Keputusan yang Direkomendasikan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Atosiban adalah penghambat kompetitif reseptor oksitosin (OT) dan reseptor V1b vasopresin. Secara klinis, ia menekan kontraksi uterus dengan memblokir reseptor OT di miometrium, menjadikannya pilihan farmakologi standar untuk persalinan praterm yang terancam. Data mekanisme aksi terperinci dari DrugBank tidak diambil dalam paket bukti ini (DrugBank ID tidak tersedia), namun kelas farmakologinya sudah mapan dalam praktik klinis.

Prediksi TxGNN untuk glaukoma herediter primer kemungkinan besar berasal dari kehadiran reseptor OT yang diketahui di jala trabekula mata anterior. Beberapa penelitian dasar menyarankan bahwa OT endogen dapat memfasilitasi aliran humor akuos, berpotensi berkontribusi pada regulasi tekanan intraokular (IOP). Glaukoma herediter primer — didorong oleh mutasi pada gen seperti MYOC dan CYP1B1 — melibatkan kerusakan saraf optik progresif yang disebabkan oleh IOP yang kronis meningkat.

**Namun, kontradiksi mekanistik yang kritis melemahkan prediksi ini.** Atosiban *memblokir* pensinyalan OT/OTR, yang secara teoretis akan *mengganggu* aliran keluar akuos dan *meningkatkan* IOP — kebalikan dari yang dibutuhkan pengobatan glaukoma. Lebih lanjut, glaukoma herediter adalah penyakit monogenik yang didorong struktur tanpa hubungan langsung yang terbentuk dengan jalur pensinyalan OT. Prediksi ini kemungkinan besar mencerminkan artefak kedekatan grafik dalam grafik pengetahuan TxGNN (simpul jaringan OTR bersama), bukan peluang terapeutik yang nyata.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar untuk Atosiban dalam glaukoma herediter primer.

---

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia untuk Atosiban dalam glaukoma herediter primer.

---

## Informasi Pasar Malaysia

Atosiban memiliki **2 pendaftaran** di Malaysia dengan status pasar saat ini **Dipasarkan**. Detail pendaftaran — termasuk nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui — tidak diambil dalam paket data ini. Ini harus diverifikasi langsung melalui basis data Badan Regulasi Farmasi Nasional (NPRA) sebelum penilaian regulasi lebih lanjut.

---

## Pertimbangan Keselamatan

Silakan lihat sisipan kemasan untuk informasi keselamatan.

> ⚠️ **Catatan:** Baik peringatan kunci maupun kontraindikasi saat ini ditandai sebagai celah data level pemblokiran dalam paket bukti ini. Pengambilan sisipan kemasan NPRA/TFDA diperlukan sebelum penilaian keselamatan apa pun dapat dilanjutkan.

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Bukti untuk indikasi ini berada pada L5 (prediksi model saja), tanpa uji klinis pendukung atau literatur peer-review. Lebih kritis, mekanisme inti Atosiban — *antagonisme* reseptor OT — berlawanan arah dengan tujuan terapeutik dalam glaukoma herediter primer, di mana *agonis* OT akan diperlukan untuk mempromosikan aliran akuos keluar dan mengurangi IOP. Kontradiksi mekanistik yang sama ini diidentifikasi di seluruh **semua 10 indikasi teratas yang diprediksi** yang ditinjau dalam paket ini:

| Indikasi | Kontradiksi |
|---|---|
| Glaukoma herediter primer | OT memblokir aliran keluar → meningkatkan IOP |
| Glaukoma sudut terbuka | Sama seperti di atas |
| Alopecia / Varian hipotrikosis | OT mempromosikan siklus pertumbuhan folikel rambut; antagonis mungkin memperburuk |
| Alopecia areata yang tersebar | OT memiliki peran anti-inflamasi/imunomodulator; antagonis tidak produktif |
| Penyakit vaskular | Semua 17 makalah literatur yang diambil mendokumentasikan kardioproteksi *agonis* OT; Atosiban memblokir jalur ini |
| Sindrom outlet toraks (vena/arteri) | Penyakit anatomis/struktural; tidak ada relevansi jalur OT |
| Kalsifiaksi vaskular | Penyakit kalsium-fosfat vaskular; tidak ada relevansi jalur OT |

Uji klinis tunggal yang diambil (NCT03570294, terkait dengan sindrom outlet toraks vena) dengan benar diidentifikasi sebagai kesalahan pemetaan data — ini adalah studi keselamatan tokolisis Atosiban tanpa relevansi dengan indikasi yang terdaftar.

**Untuk melanjutkan, berikut yang diperlukan:**

- Ambil detail pendaftaran NPRA untuk Atosiban (nomor otorisasi, nama produk, bentuk dosis, dan indikasi yang disetujui) dari basis data NPRA
- Dapatkan profil mekanisme aksi lengkap dan keselamatan dari DrugBank (DrugBank ID saat ini tidak tersedia)
- Unduh dan analisis sisipan kemasan TFDA/NPRA untuk mengatasi celah data level pemblokiran keselamatan (peringatan dan kontraindikasi)
- Lakukan pencarian literatur yang didorong hipotesis secara khusus menyelidiki apakah *antagonisme* reseptor OT — bukan agonis — dapat memiliki efek penurun IOP atau neuroprotektif dalam model glaukoma
- Pertimbangkan untuk mengevaluasi *agonis* OT (bukan Atosiban) sebagai kandidat repurposing yang lebih rasional secara mekanistik untuk indikasi glaukoma, kardioproteksi, atau alopecia, di mana basis bukti yang ada menunjuk ke arah itu

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

