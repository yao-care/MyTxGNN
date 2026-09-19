---
layout: default
title: Clonazepam
parent: Low Evidence (L4-L5)
nav_order: 231
evidence_level: L5
indication_count: 3
---

# Clonazepam
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

# Klonazepam: Menuju Indikasi Baru dalam Sindrom Kaki Gelisah

> Teks indikasi yang diluluskan secara asal tidak tersedia dalam paket bukti ini (rekod lesen TFDA/NPRA wujud tetapi medan indikasi tidak dirakam), jadi tajuk mengikuti format "menuju indikasi baru" daripada standar "Dari X ke Y."

## Ringkasan Satu Ayat

Klonazepam ialah benzodiasepin yang dipasarkan (4 pendaftaran, sedang berada di pasaran) yang indikasi asal yang diluluskan tidak dirakam dalam dataset ini. Model TxGNN meramalkan bahawa ia mungkin berkesan untuk **Sindrom Kaki Gelisah (SKG)**, dengan skor ramalan **99.65%**, tetapi paket bukti ini pada masa ini mengandungi **tiada ujian klinis dan tiada literatur** yang secara khusus menyokong penggunaan semula ini — rasionalnya berdasarkan farmakologi kelas ubat yang diketahui dan amalan klinis luar label yang sedia ada daripada kajian yang disahkan dataset.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak tersedia dalam dataset semasa (celah data) |
| Indikasi Baru yang Diramalkan | Sindrom Kaki Gelisah |
| Skor Ramalan TxGNN | 99.65% |
| Tahap Bukti | L4 (mekanisme/amalan klinis yang diketahui, tiada ujian atau literatur yang disahkan dataset) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 4 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Masuk Akal?

Data mekanisme tindakan terperinci DrugBank untuk klonazepam ditandai sebagai celah data dalam paket bukti ini. Walau bagaimanapun, rasional penggunaan semula model sendiri mengenalpasti klonazepam sebagai **pemodulator alostrik positif reseptor GABA-A** (kelas benzodiasepin), yang menekan kesergaman berlebihan dalam litar sensorimotor.

Benzodiasepin — klonazepam khususnya — sudah disenaraikan dalam beberapa panduan rawatan SKG sebagai agen tambahan garisan kedua/ketiga, biasanya dikhaskan untuk pesakit dengan tindak balas tidak mencukupi terhadap terapi dopaminergik atau dengan gangguan tidur yang ketara. Ini adalah amalan klinis luar label yang sedia ada daripada hipotesis mekanistik yang baru, yang konsisten dengan skor ramalan model yang sangat tinggi (99.65%).

Walau demikian, paket bukti ini mengandungi **sifar ujian klinis dan sifar penerbitan** yang secara khusus menghubungkan klonazepam kepada SKG (semua pertanyaan ClinicalTrials.gov, ICTRP, dan PubMed mengembalikan 0 hasil). Ramalan itu harus dibaca sebagai "konsisten dengan farmakologi yang diketahui dan penggunaan luar label yang sedia ada," bukan sebagai bukti yang baru ditemui atau yang disahkan dataset.

---

## Bukti Ujian Klinis

Pada masa ini tiada ujian klinis berkaitan yang didaftarkan.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

Klonazepam dipasarkan di Malaysia dengan **4 pendaftaran aktif**, tetapi medan tahap lesen (nombor pendaftaran, nama produk, bentuk dos, teks indikasi yang diluluskan) tidak diisi dalam paket bukti ini, jadi jadual bagi setiap produk tidak dapat dihasilkan tanpa memanipulasi data.

---

## Pertimbangan Keselamatan

Sila rujuk kepada risalah paket untuk maklumat keselamatan.

**⚠ Nota:** Amaran risalah paket/kontraindikasi (DG001) ditandai sebagai celah data **Sekatan** dalam paket bukti ini — ini secara khusus menghalang kes daripada memasuki peringkat pra-penilaian keselamatan S1. Celah ini mesti ditutup sebelum penilaian lanjutan.

---

## Kesimpulan dan Langkah Berikutnya

**Keputusan: Tahan**

**Rasional:**
- Ramalan SKG secara biologi adalah munasabah dan selaras dengan penggunaan luar label yang diketahui, tetapi didukung hanya oleh penalaran mekanis — tiada ujian klinis atau literatur dalam dataset ini yang mengesahkannya, dan data keselamatan risalah paket TFDA/NPRA (amaran, kontraindikasi) hilang dan memblokir (DG001), jadi pra-penilaian keselamatan S1 tidak dapat diselesaikan pada masa ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Dapatkan PDF risalah paket TFDA/NPRA dan ekstrak amaran/kontraindikasi (menyelesaikan DG001, memblokir)
- Pertanyakan DrugBank untuk data mekanisme tindakan yang disahkan (menyelesaikan DG002)
- Isi medan tahap lesen (nombor pendaftaran, teks indikasi yang diluluskan, bentuk dos) untuk 4 pendaftaran Malaysia
- Carian literatur/ujian sasaran menggunakan sinonim khusus SKG (contohnya, "penyakit Willis-Ekbom") jika istilah standard kurang mengira bukti yang sedia ada
- **Nota QA:** Indikasi yang diramalkan ketiga dalam paket ini, *neoplasma saraf trigeminal* (pangkat 3, skor 99.30%), ditandai oleh rasional itu sendiri sebagai kemungkinan kekeliruan embedding graf pengetahuan dengan *neuralgia trigeminal* — syorkan semakan pemetaan KG manual sebelum calon ini digunakan untuk sebarang keputusan hiliran.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

