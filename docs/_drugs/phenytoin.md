---
layout: default
title: Phenytoin
parent: Low Evidence (L4-L5)
nav_order: 545
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Fenitoin: Dari Epilepsi ke Neoplasma Saraf Trigeminal

## Ringkasan Satu Kalimat

Fenitoin adalah agen antiepilepsi klasik yang memblokir saluran natrium; teks indikasi yang disetujui NPRA yang spesifik tidak dikembalikan dalam tarik data ini. Prediksi model TxGNN yang berpangkat teratas adalah **Neoplasma Saraf Trigeminal** (skor 99,99%), tetapi satu-satunya literatur yang mendukung (**5 publikasi, 0 uji klinis**) membahas neuralgia *trigeminal* dan sindrom Sturge-Weber daripada tumor saraf — paket bukti itu sendiri menandai ini sebagai kemungkinan kesalahan pemetaan ontologi penyakit dan merekomendasikan tinjauan manual sebelum melanjutkan.

---

## Tinjauan Cepat

| Item | Konten |
|------|--------|
| Indikasi Asal | Tidak ditentukan dalam ekstrak lisensi NPRA yang tersedia (semua bidang lisensi kosong); Fenitoin ditetapkan secara global sebagai agen antiepilepsi/antikonvulsan |
| Indikasi Baru yang Diprediksi | Neoplasma Saraf Trigeminal |
| Skor Prediksi TxGNN | 99,99% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan (Marketed) |
| Jumlah Pendaftaran | 5 |
| Keputusan yang Direkomendasikan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme aksi terperinci tidak tersedia (kueri DrugBank mengembalikan celah pemblokiran pada bidang ini). Berdasarkan farmakologi yang umumnya ditetapkan, fenitoin adalah pemblokir saluran natrium yang diatur tegangan yang secara klasik digunakan untuk menekan penembakan neuronal yang abnormal dan frekuensi tinggi dalam epilepsi; mekanisme yang sama mendasari penggunaan off-label jangka panjangnya dalam sindrom nyeri neuropatik yang melibatkan hiperekskitabilitas neuronal.

Namun, prediksi peringkat-1 yang spesifik — neoplasma saraf **trigeminal** — tidak didukung dengan baik oleh bukti yang diambil. Kelima publikasi terkait berhubungan dengan neuralgia **trigeminal** (gangguan nyeri/hiperekskitabilitas) atau laporan kasus sindrom Sturge-Weber, tidak ada yang menggambarkan tumor saraf. Ketidakcocokan ini sangat menunjukkan artefak pemetaan ontologi penyakit TxGNN (neuralgia salah diberi label sebagai neoplasma) daripada sinyal mekanistik sejati untuk indikasi onkologi, dan harus direkonsiliasi secara manual sebelum evaluasi lebih lanjut.

Penting untuk dicatat, paket bukti yang sama ini secara terpisah mencantumkan **neuralgia trigeminal** (peringkat 10, skor TxGNN 99,97%) sebagai indikasi prediksi yang berbeda dengan dukungan yang jauh lebih kuat: uji klinis prospektif yang selesai (NCT03712254) dan pedoman praktik klinis EAN. Pemblokiran saluran natrium adalah mekanisme terapeutik yang diterima untuk neuralgia trigeminal (dibagikan dengan karbamazepin), membuat kandidat itu koheren secara mekanis dengan cara label neoplasma tidak.

---

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar untuk "neoplasma saraf trigeminal."

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Temuan Kunci |
|------|-------|-------|--------|-----------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Tinjauan | Expert Rev Neurotherapeutics | Tinjauan pengobatan neuralgia trigeminal (medis dan bedah); kemungkinan etiologi kompresi vaskular — menyangkut neuralgia, bukan neoplasma |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Tinjauan/Laporan kasus | J Assoc Physicians India | Kasus sindrom Sturge-Weber dengan malformasi vaskular wajah/orbital dan kejang |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Seri kasus | Anales Españoles de Pediatría | Seri 14 kasus sindrom Sturge-Weber, perjalanan klinis dan respons pengobatan |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Tidak diklasifikasi | Birth Defects Orig Article Series | Tinjauan gangguan dermatologi pada pasien yang dirawat di institusi; hanya terkait secara tangensial |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Tidak diklasifikasi | Trans Am Neurol Assoc | Studi ukuran serat/konduksi terkait dengan pengobatan nyeri akar trigeminal; tidak ada abstrak yang tersedia |

Tidak ada publikasi ini yang mengatasi neoplasma saraf trigeminal secara khusus.

---

## Informasi Pasar Malaysia

Ekstrak regulasi menunjukkan 5 pendaftaran produk aktif (`total_licenses = 5`) dengan status pasar **Dipasarkan (Marketed)**, tetapi detail lisensi individual — nomor otorisasi, nama produk, bentuk dosis, dan teks indikasi yang disetujui — tidak dikembalikan dalam tarik data ini dan tidak dapat dilaporkan di sini.

---

## Pertimbangan Keamanan

Silakan merujuk ke sisipan kemasan untuk informasi keamanan. (Peringatan kunci, kontraindikasi, dan kueri DDI semua mengembalikan tidak ada data dalam paket bukti ini — DG001 ditandai sebagai celah pemblokiran untuk tinjauan keamanan.)

---

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Alasan:**
Prediksi peringkat-1 (neoplasma saraf trigeminal) tidak memiliki dukungan uji klinis dan basis literaturnya tampaknya mencerminkan kesalahan pemetaan ontologi penyakit daripada bukti asli (L5/S0). Input inti yang diperlukan bahkan untuk pemeriksaan keamanan awal — peringatan sisipan kemasan TFDA/NPRA (DG001, Pemblokiran) dan data MOA (DG002) — juga hilang.

**Untuk melanjutkan, hal berikut diperlukan:**
- Rekonsiliasi manual dari pemetaan ontologi penyakit "neoplasma saraf trigeminal" versus "neuralgia trigeminal" sebelum mencetak ulang kandidat ini
- Pengambilan sisipan kemasan TFDA/NPRA (peringatan, kontraindikasi) — saat ini memblokir
- Pengambilan data kategori DrugBank MOA dan obat
- Pengambilan detail register lisensi NPRA aktual (nama produk, bentuk dosis, teks indikasi yang disetujui)
- Pertimbangkan untuk mengevaluasi **neuralgia trigeminal** (peringkat 10 dalam paket yang sama ini, L3/S2, "Lanjutkan dengan Pengawasan," didukung oleh uji klinis yang selesai dan pedoman EAN) sebagai kandidat repurposing obat yang lebih didukung secara substansial untuk obat ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

