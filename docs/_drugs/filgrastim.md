---
layout: default
title: Filgrastim
parent: Low Evidence (L4-L5)
nav_order: 345
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: Dari Indikasi Asal yang Tidak Ditentukan kepada Gangguan Pelepasan Trombosit Utama

## Ringkasan Satu Ayat

> Evidence pack tidak menyertakan indikasi asal yang diluluskan bagi Filgrastim (medan data kosong), walaupun ia adalah produk pasaran di Malaysia dengan 10 pendaftaran dalam fail.
> Model TxGNN meramalkan potensi keberkesanan untuk **Gangguan Pelepasan Trombosit Utama**, tetapi ulasan mekanisme evidence pack sendiri menandai ini sebagai kemungkinan **artifak topologi graf dan bukannya farmakologi sebenar** — tiada satupun daripada 14 percubaan klinikal yang diambil, dan tiada kesusasteraan, secara langsung menyokong indikasi ini.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tersedia dalam evidence pack (medan lesen dan indikasi kosong) |
| Indikasi Baru Diramalkan | Gangguan pelepasan trombosit utama |
| Skor Ramalan TxGNN | 99.99% |
| Tahap Bukti | L5 (ramalan model sahaja, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 10 |
| Keputusan Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Filgrastim ialah faktor rangsangan koloni granulosit rekombinan (G-CSF) yang mengikat reseptor CSF3R pada sel pemula mieloid sumsum tulang, mendorong proliferasi/pembezaan neutrofil dan mobilisasi sel induk hematopoietik. Ini ialah satu-satunya maklumat mekanisme yang tersedia untuk ubat ini dalam evidence pack (`original_moa` sendiri ditandai sebagai jurang data; mekanisme di atas diambil daripada bukti nisbah-ubat penggunaan semula).

Gangguan pelepasan trombosit utama, sebaliknya, adalah gangguan fungsi trombosit yang melibatkan sekresion granula padat/gran-α yang rosak semasa pengaktifan trombosit — laluan yang tidak berkaitan dengan isyarat mieloid yang dimediasi CSF3R. Penilaian mekanisme evidence pack sendiri menyatakan ini secara jelas: tiada pautan mekanisme langsung yang diketahui wujud antara keduanya, dan skor TxGNN yang tinggi kemungkinan besar mencerminkan kedekatan topologi nod "sumsum tulang / hematopoiesis" dalam graf pengetahuan dan bukannya hubungan farmakologi sebenar.

Menyokong berhati-hati ini, kesemua 14 percubaan klinikal yang diambil untuk pasangan ini dinilai "C" (relevansi rendah) oleh sistem pemeringkatan relevansi evidence pack sendiri — ia adalah pemindahan sel induk, profilaksis GVHD, atau kajian pencegahan CMV dengan Filgrastim digunakan hanya sebagai agen mobilisasi sel induk/penjagaan sokongan, bukan sebagai rawatan untuk gangguan pelepasan trombosit. Tiada kesusasteraan ditemui sama sekali.

---

## Bukti Percubaan Klinikal

**Berhati-hati: percubaan di bawah ini diambil melalui kesamaan ubat/penyakit tetapi dinilai sebagai relevansi rendah (Gred C) oleh ulasan evidence pack sendiri — Filgrastim muncul hanya sebagai agen sokongan/mobilisasi dalam tetapan pemindahan sel induk atau onkologi, bukan sebagai rawatan bagi indikasi yang diramalkan.**

| Bilangan Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fasa 2 | Selesai | 64 | Pemindahan sel induk autologi CD34+ dipilih vs. tidak dipilih dalam MCL/DLBCL; G-CSF digunakan hanya untuk mobilisasi sel induk, bukan percubaan rawatan gangguan trombosit. |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fasa 1 | Ditarik balik | 0 | Kajian pemindahan sumsum tulang penderma tidak berkaitan yang dipaparcaair; ditarik balik dengan pendaftaran sifar. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fasa 3 | Merekrut | 156 | HSCT autologi vs. terapi terbaik yang tersedia dalam MS rintangan rawatan; tidak berkaitan dengan gangguan trombosit. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fasa 1/2 | Merekrut | 260 | Pencarian dos untuk siklofosfamida pasca-pemindahan profilaksis GVHD; bukan kajian gangguan trombosit. |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Fasa 2 | Selesai | 124 | Profilaksis antiviral untuk penggiataktifan CMV dalam penjagaan kritikal; indikasi tidak berkaitan. |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Fasa 2 | Ditamatkan | 49 | Dapansutrile untuk COVID-19 sederhana; ditamatkan, tidak berkaitan dengan Filgrastim atau gangguan trombosit. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Fasa 2 | Selesai | 160 | Gansiklovir/valgansiklovir untuk penggiataktifan CMV dalam kegagalan pernafasan; indikasi tidak berkaitan. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fasa 2 | Selesai | 60 | Pilot pemindahan sel induk alogenei/singenei dalam sarkoma pediatrik; indikasi tidak berkaitan. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fasa 1/2 | Selesai | 147 | HSCT alogenei intensiti kurang bagi keganasan hematologi; indikasi tidak berkaitan. |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Fasa 2 | Selesai | 19 | Pilot HSCT intensiti berkurangan untuk pesakit mutasi GATA2; indikasi tidak berkaitan. |

4 percubaan tambahan diambil tetapi belum dinilai untuk relevansi (tidak ditunjukkan; tiada satupun menyasarkan indikasi yang diramalkan secara langsung berdasarkan tajuk mereka).

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

*(Nota: amaran label TFDA/NPRA dan kontraindikasi ditandai sebagai jurang data Sekatan dalam evidence pack ini — lihat Kesimpulan di bawah.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada percubaan klinikal atau kesusasteraan yang secara langsung menyokong Filgrastim untuk gangguan pelepasan trombosit utama, dan mekanisme yang dicadangkan (mielopoiesis yang didorong CSF3R) tidak mempunyai pautan yang ditubuhkan dengan laluan sekresion granula trombosit — ulasan evidence pack sendiri mengaitkan skor TxGNN yang tinggi dengan topologi graf pengetahuan dan bukannya farmakologi sebenar. Digabungkan dengan jurang data Sekatan pada amaran label produk/kontraindikasi, calon ini tidak memenuhi ambang untuk maju melampaui S0.

**Untuk meneruskan, perkara berikut diperlukan:**
- Label produk TFDA/NPRA (amaran, kontraindikasi) — pada masa ini jurang data Sekatan (DG001)
- Rekod mekanisme tindakan DrugBank yang disahkan — pada masa ini jurang data Keterukan Tinggi (DG002)
- Kajian praklinik atau mekanisme yang secara langsung menghubungkan isyarat G-CSF/CSF3R kepada pelepasan granula padat/gran-α trombosit
- Percubaan klinikal khusus atau siri kes yang menguji Filgrastim dalam pesakit dengan gangguan pelepasan trombosit (tiada yang wujud pada masa ini)
- Indikasi asal yang diluluskan yang disahkan untuk Filgrastim, yang tidak hadir dalam evidence pack ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

