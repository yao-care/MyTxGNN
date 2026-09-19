---
layout: default
title: Efavirenz
parent: Low Evidence (L4-L5)
nav_order: 307
evidence_level: L4
indication_count: 3
---

# Efavirenz
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **3** 
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

# Efavirenz: Dari Infeksi HIV-1 hingga Feline Acquired Immunodeficiency Syndrome

## Ringkasan Satu Kalimat

Efavirenz adalah inhibitor reverse transcriptase non-nucleoside (NNRTI) yang terbukti untuk mengobati infeksi HIV-1 (digunakan sebagai komponen regimen kombinasi seperti Atripla). Model TxGNN memprediksi itu mungkin efektif untuk **Feline Acquired Immunodeficiency Syndrome (penyakit terkait FIV pada kucing)**, tetapi arah ini saat ini didukung hanya oleh **2 uji klinis (keduanya relevansi langsung rendah)** dan **1 laporan literatur praklinik**, dan rasional mekanistik yang mendasari lemah.

---

## Ikhtisar Cepat

| Item | Konten |
|------|--------|
| Indikasi Asli | Infeksi HIV-1 (disimpulkan dari konteks uji klinis; teks label NPRA terdaftar tidak tersedia dalam dataset saat ini) |
| Indikasi Baru yang Diprediksi | Feline Acquired Immunodeficiency Syndrome |
| Skor Prediksi TxGNN | 99.80% |
| Tingkat Bukti | L4 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Registrasi | 11 |
| Keputusan yang Direkomendasikan | Tahan |

---

## Mengapa Prediksi Ini Masuk Akal?

Saat ini, data mekanisme aksi terperinci tidak tersedia (bidang MOA DrugBank adalah kesenjangan data). Berdasarkan informasi yang diketahui, Efavirenz adalah NNRTI yang digunakan dalam terapi antiretroviral kombinasi untuk infeksi HIV-1 — ini dikonfirmasi secara tidak langsung dalam paket bukti itu sendiri, di mana Efavirenz muncul sebagai bagian dari regimen pembanding Atripla (Efavirenz/Emtricitabine/Tenofovir) dalam uji klinis HIV-1 yang naif terhadap antiretroviral (NCT01263015). Mekanisme intinya adalah penghambatan langsung dari enzim HIV-1 reverse transcriptase (RT).

Model TxGNN menghubungkan Efavirenz ke Feline Acquired Immunodeficiency Syndrome karena Feline Immunodeficiency Virus (FIV) adalah, seperti HIV-1, lentivirus yang bergantung pada reverse transcriptase untuk replikasi — asosiasi grafik pengetahuan yang masuk akal berdasarkan mesin virus bersama. Namun, literatur pendukung (PMID 38031646) adalah studi perbandingan struktural/biokimia yang secara khusus dilakukan *karena* FIV RT berbeda secara signifikan dalam urutan dan struktur dari HIV-1 RT, artinya NNRTI manusia — termasuk Efavirenz — umumnya menunjukkan aktivitas penghambatan yang lemah atau dapat diabaikan terhadap FIV RT. Tujuan studi adalah mengeksplorasi apakah modifikasi struktural kelas NNRTI dapat menghasilkan aktivitas FIV, bukan menunjukkan bahwa Efavirenz itu sendiri efektif terhadap FIV.

Selain itu, indikasi yang diprediksi ini adalah kasus penggunaan veteriner (kucing), yang mengikuti jalur pengembangan dan peraturan yang mendasar berbeda dari repurposing obat manusia. Kelayakan mekanistik oleh karena itu lemah, dan dua uji klinis yang dikutip adalah kedua-duanya uji HIV-1 manusia dari obat-obatan yang tidak terkait (dolutegravir), termasuk hanya melalui asosiasi grafik pengetahuan tidak langsung daripada bukti langsung.

---

## Bukti Uji Klinis

| Nomor Uji | Fase | Status | Enrolmen | Temuan Utama |
|---------|------|--------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Selesai | 208 | Studi pemilihan dosis GSK1349572 (dolutegravir, inhibitor integrase) pada pasien HIV-1 manusia; tidak terkait dengan Efavirenz atau FIV — ditandai sebagai relevansi rendah (Tingkat C), termasuk hanya melalui kemunculan bersama area terapeutik. |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Selesai | 844 | Studi SINGLE membandingkan dolutegravir + abacavir/lamivudine vs. Atripla (yang mengandung Efavirenz) pada pasien HIV-1 manusia; mengkonfirmasi peran terbukti Efavirenz dalam HIV-1 tetapi tidak memiliki hubungan dengan FIV — ditandai sebagai relevansi rendah (Tingkat C). |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Temuan Utama |
|------|-------|-------|--------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Perbandingan biokimia/struktural in vitro | Journal of Veterinary Science | Membandingkan NNRTI (nevirapine, efavirenz, rilpivirine) terhadap RT virus immunodefisiensi feline dan manusia; menemukan FIV RT berbeda secara struktural dari HIV-1 RT, menjelaskan mengapa NNRTI yang dikembangkan untuk HIV-1 bukan perawatan yang efektif untuk FIV sebagaimana adanya — tidak ada perawatan FIV yang disetujui saat ini. |

---

## Informasi Pasar Malaysia

Catatan otorisasi terperinci (nomor lisensi, nama produk, bentuk dosis, teks indikasi yang disetujui) tidak tersedia dalam dataset saat ini — semua entri lisensi mengembalikan bidang kosong. Catatan kueri NPRA mengkonfirmasi Efavirenz memiliki **11 produk terdaftar** dengan status **Dipasarkan** di Malaysia (tanggal kueri: 2026-03-27), tetapi teks label yang mendasari belum diambil.

---

## Pertimbangan Keselamatan

Silakan merujuk pada kemasan produk untuk informasi keselamatan. (Data peringatan kunci, kontraindikasi, dan interaksi obat-obat saat ini tidak tersedia dalam dataset ini — pengambilan label produk NPRA/TFDA diperlukan sebelum penilaian pra-keselamatan apa pun dapat dilanjutkan.)

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tahan**

**Rasionalitas:**
Indikasi yang diprediksi (Feline Acquired Immunodeficiency Syndrome) hanya didukung oleh bukti praklinik/mekanistik (L4) pada tahap keputusan S0, kedua uji klinis yang dikutip adalah relevansi langsung rendah (Tingkat C, obat/spesies yang tidak terkait), dan sumber literatur satu-satunya menunjukkan bahwa kelas obat induk Efavirenz *tidak* secara alami efektif terhadap reverse transcriptase FIV. Dikombinasikan dengan kesenjangan data **Penghalang** pada peringatan label TFDA/NPRA dan kontraindikasi, kandidat ini belum dapat melanjutkan ke penilaian pra-keselamatan (S1).

**Untuk melanjutkan, berikut ini diperlukan:**
- Data label produk yang disetujui NPRA (peringatan, kontraindikasi, DDI) — saat ini kesenjangan data Penghalang (DG001)
- Detail mekanisme aksi DrugBank/Efavirenz — saat ini kesenjangan data tingkat keparahan tinggi (DG002)
- Jika indikasi veteriner ini dikejar, bukti struktural/PK tentang apakah Efavirenz (atau analog) dapat dimodifikasi untuk aktivitas RT FIV, ditambah klarifikasi jalur peraturan veteriner yang berlaku (berbeda dari repurposing obat manusia)
- Catatan: prediksi grafik pengetahuan terkait untuk Efavirenz dalam infeksi Simian Immunodeficiency Virus (peringkat 2, tingkat bukti L3) menunjukkan dukungan literatur yang secara substansial lebih kuat (16 publikasi, termasuk pemberian dosis efavirenz in vivo secara langsung pada makaka yang terinfeksi RT-SHIV), meskipun model itu sendiri mewakili alat penelitian translasi HIV daripada indikasi klinis manusia mandiri — mungkin pertanyaan penelitian yang lebih produktif untuk mengejar secara paralel.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

