---
layout: default
title: Tiotropium
parent: High Evidence (L1-L2)
nav_order: 651
evidence_level: L1
indication_count: 10
---

# Tiotropium
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
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

# Tiotropium: Dari Penyakit Obstruktif Paru-paru Kronik hingga Penyakit Paru-paru Obstruktif

## Ringkasan Satu Ayat

> Tiotropium ialah antagonis muskarinik kerja panjang (LAMA) bronkodilator yang telah terbukti untuk penyakit obstruktif paru-paru kronik (COPD) dan, sebagai terapi tambahan, asma persisten yang teruk.
> Model TxGNN dengan kedudukan tertinggi meramalkan **Penyakit Paru-paru Obstruktif**, disokong oleh **50 kajian klinikal** dan **20 penerbitan** — namun, istilah ini adalah payung kategori penyakit yang sudah termasuk petunjuk kegunaan yang diluluskan untuk tiotropium, jadi ia harus dibaca sebagai isyarat pengesahan daripada calon pertukaran guna yang benar-benar baru.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak dinyatakan dalam ekstrak lesen TFDA/NPRA (teks petunjuk kelulusan kosong untuk semua 3 pendaftaran); berdasarkan farmakoloji yang mapan, tiotropium ditunjukkan untuk rawatan penyelenggaraan COPD dan sebagai terapi pengawal tambahan dalam asma persisten yang teruk |
| Petunjuk Baharu Diramalkan | Penyakit Paru-paru Obstruktif *(istilah payung — bukan petunjuk baru; lihat kaveat di bawah)* |
| Skor Ramalan TxGNN | 99.99% |
| Tahap Bukti | L1 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | Teruskan dengan Penjaga *(label terbitan model — lihat Kesimpulan untuk cadangan yang dibetulkan)* |

---

## Mengapa Ramalan Ini Munasabah?

`drug.original_moa` ditandai sebagai jurang data dalam Pek Bukti ini, jadi mekanisme di bawah diambil daripada medan `repurposing_rationale` yang dilampirkan pada ramalan individu daripada rekod MOA berdedikasi: Tiotropium ialah antagonis muskarinik kerja panjang (LAMA) yang secara selektif menghalang reseptor M3 pada otot licin saluran udara, menghasilkan bronkodilasi yang berkelanjutan. Ini adalah asas mekanistik yang mapan untuk peranannya dalam pengurusan COPD dan asma.

**Kaveat penting**: teks rasional yang dibekalkan untuk ramalan dengan kedudukan tertinggi ini secara jelas menyatakan bahawa "penyakit paru-paru obstruktif" adalah konsep superordinat yang meliputi COPD dan asma — iaitu, penyakit yang tiotropium *sudah* ditunjukkan untuk — dan adalah "bukan ramalan baru." Perkara yang sama berlaku untuk kedudukan 5 dalam Pek Bukti ini, "penyakit obstruktif paru-paru kronik" itu sendiri (L1, disertakan nampaknya sebagai merujuk asas/semakan akal masuk). Kedua-dua skor sangat tinggi (>99.8%) tepat kerana model itu dengan betul memulihkan pautan ubat-penyakit yang diketahui, bukan menampilkan potensi terapeutik baru.

Di antara calon yang tinggal, hanya kedudukan 4 ("COPD, permulaan usia awal yang teruk") mewakili sambungan tambahan yang munasabah tetapi kurang berkuasa — mekanisme LAMA yang sama, tetapi tiada kajian yang khusus telah mendaftarkan atau menstratifikasi fenotip permulaan usia awal yang teruk ini. Kedudukan 2, 3, dan 6–10 (malformasi respiratori, sindrom Rienhoff, paru-paru bercahaya, emfisema pampasan, emfisema interstisial, stenosis trakea, dan gangguan imun kekurangan CD8α) adalah keadaan struktur, genetik, atau imunologi tanpa sambungan mekanistik kepada antagonisme reseptor M3; teks rasional mereka sendiri menandainya sebagai kemungkinan besar bunyi bersama nama ubat daripada isyarat sebenar, dan 6 daripada 7 telah tidak ada kajian sokongan atau literatur (L5).

---

## Bukti Kajian Klinikal

*(daripada `predicted_indications[0]` — "penyakit paru-paru obstruktif")*

| Nombor Kajian | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Fasa 3 | Selesai | 453 | Kajian terkawal plasebo tiotropium Respimat 5 mcg/hari sebagai terapi pengawal tambahan lebih 48 minggu dalam asma persisten yang teruk |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Fasa 4 | Selesai | 457 | Kajian multipusat 24 minggu tiotropium 18 mcg HandiHaler + albuterol PRN lwn. plasebo + albuterol PRN dalam penyelenggaraan COPD tanpa rawatan terdahulu |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Fasa 3 | Selesai | 5993 | Kajian skala UPLIFT menilai sama ada tiotropium harian mengurangkan kadar penurunan fungsi paru-paru dalam COPD |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Fasa 3 | Selesai | 914 | Kajian SAFE — kesan setahun tiotropium 18 mcg pada perubahan FEV1 trofi dalam COPD, distratifikasi mengikut status merokok |
| [NCT01911364](https://clinicaltrials.gov/study/NCT01911364) | Fasa 3 | Selesai | 3686 | Kajian 52 minggu membandingkan terapi tiga (beklometason+formoterol+glikopirronium) lwn. tiotropium dan lwn. tiotropium+beklometason/formoterol dalam COPD yang teruk |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Fasa 3 | Selesai | 872 | Perbandingan 24 minggu GSK573719/GW642444 lwn. GSK573719 lwn. tiotropium dalam COPD |
| [NCT02173769](https://clinicaltrials.gov/study/NCT02173769) | T/A | Selesai | 1845 | Penilaian dunia sebenar perubahan fungsi fizikal dengan terapi gabungan tiotropium+olodaterol dalam COPD |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Fasa 4 | Selesai | 17 | Responsif bronkodilator akut kepada tiotropium dan albuterol dalam bronkiolitis obliteratif selepas pemindahan sel stem hematopoietik |
| [NCT00662740](https://clinicaltrials.gov/study/NCT00662740) | Fasa 3 | Ditamatkan | 220 | Perbandingan 1 tahun regimen gabungan tiotropium+salmeterol lwn. terapi agen tunggal dalam COPD |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Fasa 4 | Ditamatkan | 80 | Tiotropium+salbutamol berkala lwn. flutikazon+salbutamol lwn. salbutamol sahaja untuk hari bebas episod dalam pernafasan awal kanak-kanak |

---

## Bukti Literatur

*(daripada `predicted_indications[0]` — "penyakit paru-paru obstruktif")*

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | The New England Journal of Medicine | Penggunaan tiotropium jangka panjang meningkatkan fungsi paru-paru dan memperlahankan penurunan dalam COPD awal/sederhana yang ringan |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Ulasan Sistematik (Cochrane) | Cochrane Database of Systematic Reviews | Kemaskini bukti keberkesanan/keselamatan tiotropium lwn. plasebo merentasi format kajian termasuk inhaler Respimat lembut-kabus |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Ulasan Sistematik (Cochrane) | Cochrane Database of Systematic Reviews | Kemaskini membandingkan tiotropium terhadap bromida ipratropium dalam COPD stabil |
| [29206658](https://pubmed.ncbi.nlm.nih.gov/29206658/) | 2018 | Ulasan | Current Opinion in Pulmonary Medicine | Ulasan trajektori fungsi paru-paru dalam COPD dan peranan campur tangan farmakoloji dalam fasa penyakit awal |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Ulasan | Life Sciences | Profil mekanistik tiotropium sebagai antagonis muskarinik pelembap-nyahkepada yang bermassa kinesis M3/M1-selektif bronkodilator |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Kohort/Perbandingan | The Annals of Pharmacotherapy | Ulasan data keberkesanan/keselamatan penggunaan bersama ipratropium tambah tiotropium dalam COPD |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Ulasan | Current Medical Research and Opinion | Ulasan bukti gabungan tiotropium+olodaterol dosis tetap bagi cadangan GOLD 2020 untuk pengurangan eksaserbasi |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Ulasan | Respiratory Research | Ulasan sejarah pembangunan klinikal tiotropium sebagai monoterap LAMA untuk kumpulan GOLD B, C, dan D |
| [22562275](https://pubmed.ncbi.nlm.nih.gov/22562275/) | 2012 | Kajian (tidak diklasifikasi) | Pneumonologia i Alergologia Polska | Kesan formoterol, formoterol+tiotropium, formoterol+ICS, dan tiotropium pada fungsi paru-paru, toleransi latihan, dan aktiviti pagi dalam COPD |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Kajian (tidak diklasifikasi) | Drugs | Profil farmakoloji dan klinikal tiotropium bromida sebagai bronkodilator antikolin sekali sehari dalam COPD |

---

## Maklumat Pasaran Malaysia

Pek bukti mengesahkan **3 pendaftaran aktif** untuk tiotropium dengan status pasaran "Dipasarkan," tetapi medan peringkat produk (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) kosong dalam ekstrak data semasa dan tidak dapat diisi tanpa mengkaji semula sumber daftar.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan bungkusan untuk maklumat keselamatan.

*(Data asas: pertanyaan `key_warnings`, `contraindications`, dan DDI semuanya mengembalikan tiada kandungan boleh guna dalam Pek Bukti ini — status pertanyaan DDI: tidak dijumpai, 0 interaksi direkodkan.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguhkan — Bukan Calon Pertukaran Guna Baru (sebagai kedudukan tertinggi)**

**Rasional:**
- Rasional Pek Bukti itu sendiri untuk ramalan beredudukan #1 ("penyakit paru-paru obstruktif") menyatakan ia adalah konsep superordinat yang sudah merangkumi petunjuk kegunaan COPD/asma yang diluluskan untuk tiotropium — tahap bukti L1 mencerminkan pengesahan penggunaan sedia ada, bukan isyarat terapeutik baru, jadi ia tidak boleh dimajukan melalui laluan pertukaran guna.
- Daripada calon yang tinggal, hanya kedudukan 4 ("COPD, permulaan usia awal yang teruk," L3, "Soalan Penyelidikan") adalah munasabah secara mekanistik tetapi kurang bukti kajian khusus fenotip; semua yang lain (malformasi respiratori, sindrom Rienhoff, paru-paru bercahaya, emfisema pampasan, emfisema interstisial, stenosis trakea, dan kerentanan kekurangan CD8α) adalah keadaan struktur/genetik/imunologi tanpa rasional mekanistik dan, dalam 6 daripada 7 kes, kajian atau literatur sokongan sifar (L5) — cadangan Tangguhkan semua.

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran sisipan bungkusan TFDA/NPRA dan kontraindikasi (ditandai sebagai jurang data **Menyekat** — diperlukan sebelum sebarang skrin keselamatan Peringkat 1 dapat diteruskan)
- Rekod mekanisme-tindakan formal untuk tiotropium (Jurang data keterukan tinggi; mekanisme yang disebut di atas telah dibina semula daripada teks rasional tahap ramalan, bukan sumber MOA berdedikasi)
- Jika meneruskan kedudukan 4 ("COPD, permulaan usia awal yang teruk") selanjutnya: carian literatur/kajian yang khusus menyasarkan fenotip COPD permulaan usia awal yang teruk daripada populasi COPD umum
- Data pendaftaran Malaysia peringkat produk lengkap (nama jenama, bentuk dos, teks petunjuk yang diluluskan) sedang hilang daripada ekstrak lesen

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

