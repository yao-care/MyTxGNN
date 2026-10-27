---
layout: default
title: Trimethoprim
parent: High Evidence (L1-L2)
nav_order: 703
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-15
description: "Trimethoprim: indikasi baharu diramal Pneumocystosis (tahap bukti L1). Indikasi asal: Jangkitan saluran kencing, otitis media berjangkit, pneumocystosis…"
---

# Trimethoprim
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **5** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Laporan penilaian ahli farmasi

</div>

## Trimethoprim: Daripada Jangkitan Saluran Kencing kepada Pneumocystosis
{: .text-alpha }

## Ringkasan Satu Ayat

Trimethoprim ialah antibiotik perencat folat yang pada asalnya digunakan untuk merawat jangkitan saluran kencing, otitis media berjangkit, pneumocystosis, shigellosis dan konjunktivitis.
Model TxGNN meletakkan **pneumocystosis** sebagai indikasi teratas, tetapi skor ramalan ialah **0.0%** dan indikasi ini sebenarnya sudah mantap, jadi ia bukan penemuan repurposing yang baharu.
Bukti klinikal datang daripada **30 percubaan klinikal** dan **20 penerbitan** yang disenaraikan dalam data, kebanyakannya melibatkan gabungan trimethoprim-sulfamethoxazole (TMP-SMX).

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Jangkitan saluran kencing, otitis media berjangkit, pneumocystosis, shigellosis, konjunktivitis (berdasarkan graf pengetahuan TxGNN; tiada teks indikasi berlesen kerana tiada pendaftaran di Malaysia) |
| Indikasi Baharu Diramalkan | Pneumocystosis |
| Skor Ramalan TxGNN | 0.0% |
| Tahap Bukti | L1 |
| Status Pasaran di Malaysia | Tidak dipasarkan (menurut data yang dikumpul; perlu disahkan semula) |
| Bilangan Pendaftaran | 0 |
| Keputusan Disyorkan | Proceed with Guardrails |

---

## Mengapa Ramalan Ini Munasabah?

Data terperinci tentang mekanisme tindakan (MOA) tidak tersedia dalam data yang dikumpul. Berdasarkan maklumat yang diketahui, trimethoprim ialah perencat dihidrofolat reduktase (DHFR). Apabila digabungkan dengan sulfamethoxazole, kedua-duanya menyekat langkah berturutan dalam sintesis folat. Kesan keberkesanannya dalam jangkitan bakteria sudah terbukti, dan mekanisme ini juga menjadi asas aktiviti terhadap *Pneumocystis jirovecii*.

Pneumocystosis merupakan indikasi mantap, iaitu rawatan barisan pertama dan profilaksis menggunakan TMP-SMX. Oleh itu, ini bukan calon repurposing sebenar. Skor TxGNN 0.0 dan medan MOA yang tiada menunjukkan bahawa kesimpulan bergantung pada data klinikal, bukan ramalan model.

Satu perkara perlu dijelaskan: status "Tidak dipasarkan" bercanggah dengan kewujudan banyak produk gabungan trimethoprim-sulfamethoxazole di pasaran. Perkara ini perlu disemak dan disepadankan.

---

## Bukti Percubaan Klinikal

Berikut ialah percubaan paling relevan bagi pneumocystosis (disenaraikan 10 sahaja). Hampir semua menggunakan TMP-SMX, bukan trimethoprim tunggal.

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT00000748](https://clinicaltrials.gov/study/NCT00000748) | Fasa 3 | Selesai | 2500 | Perbandingan TMP-SMX harian dengan tiga kali seminggu untuk profilaksis PCP pada pesakit HIV |
| [NCT00000715](https://clinicaltrials.gov/study/NCT00000715) | Fasa 3 | Selesai | 240 | Pentamidin aerosol berbanding TMP-SMX untuk rawatan PCP dalam AIDS |
| [NCT00000727](https://clinicaltrials.gov/study/NCT00000727) | Fasa 3 | Selesai | 322 | TMP-SMX berbanding pentamidin aerosol untuk profilaksis sekunder PCP |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fasa 3 | Selesai | 290 | Dapsone/trimethoprim dan clindamycin/primaquine berbanding TMP-SMX untuk PCP ringan-sederhana |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fasa 3 | Selesai | 600 | Tiga agen anti-pneumocystis ditambah zidovudine untuk pencegahan primer pada HIV lanjut |
| [NCT00000655](https://clinicaltrials.gov/study/NCT00000655) | Fasa 2 | Selesai | 300 | Atovaquone berbanding TMP-SMX (pembanding aktif) untuk PCP |
| [NCT00001014](https://clinicaltrials.gov/study/NCT00001014) | Fasa 3 | Selesai | 302 | Trimetrexate dengan leucovorin berbanding TMP-SMX (bukti tidak langsung) |
| [NCT04851015](https://clinicaltrials.gov/study/NCT04851015) | Fasa 3 | Sedang merekrut | 416 | TMP-SMX dos rendah untuk rawatan PCP |
| [NCT06499233](https://clinicaltrials.gov/study/NCT06499233) | Fasa 4 | Sedang merekrut | 800 | Profilaksis PJP pada penyakit reumatik autoimun (belum ada keputusan) |
| [NCT07619027](https://clinicaltrials.gov/study/NCT07619027) | Fasa 4 | Belum merekrut | 1084 | TMP-SMX dos rendah berbanding dos standard selepas pemindahan buah pinggang |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [37574166](https://pubmed.ncbi.nlm.nih.gov/37574166/) | 2024 | RCT (menurut klasifikasi data; abstrak menyatakan kohort retrospektif) | Chest | TMP-SMX dos rendah berbanding dos konvensional untuk PCP bukan HIV, dengan kesan advers yang lebih sedikit |
| [25269391](https://pubmed.ncbi.nlm.nih.gov/25269391/) | 2014 | Kajian sistematik (Cochrane) | Cochrane Database Syst Rev | Profilaksis PCP pada pesakit imunokompromi bukan HIV |
| [29092853](https://pubmed.ncbi.nlm.nih.gov/29092853/) | 2018 | Kohort | Ann Rheum Dis | Kesan profilaktik TMP-SMX pada penyakit reumatik dengan glukokortikoid dos tinggi |
| [32502592](https://pubmed.ncbi.nlm.nih.gov/32502592/) | 2020 | Ulasan | Chest | Faktor risiko dan pencegahan PJP dalam penyakit autoimun/radang |
| [32000290](https://pubmed.ncbi.nlm.nih.gov/32000290/) | 2020 | Ulasan | Semin Respir Crit Care Med | Gambaran keseluruhan *Pneumocystis jirovecii* pada hos imunokompromi |
| [21653531](https://pubmed.ncbi.nlm.nih.gov/21653531/) | 2011 | Ulasan | Proc Am Thorac Soc | PCP berkaitan HIV |
| [22167405](https://pubmed.ncbi.nlm.nih.gov/22167405/) | 2011 | Ulasan | Semin Respir Crit Care Med | Pneumonia Pneumocystis pada hos imunokompromi |
| [40176385](https://pubmed.ncbi.nlm.nih.gov/40176385/) | 2025 | Kajian klinikal | Arthritis Rheumatol | Faktor klinikal PCP walaupun profilaksis primer dan masa penghentian profilaksis |
| [26644039](https://pubmed.ncbi.nlm.nih.gov/26644039/) | 2016 | Ulasan | Rev Med Interne | Pneumocystosis pada pesakit imunokompromi bukan HIV; TMP-SMX dos rendah jangka panjang sangat berkesan |
| [23891358](https://pubmed.ncbi.nlm.nih.gov/23891358/) | 2013 | Laporan kes | Am J Kidney Dis | Hiponatremia berkaitan TMP-SMX semasa rawatan PCP |

---

## Keselamatan dan Pertimbangan

**Penyakit/keadaan yang dikenal pasti sebagai kontraindikasi dalam graf pengetahuan** (bukan teks label produk): porfiria (termasuk porfiria warisan dan gangguan metabolisme porfirin), penyakit buah pinggang, penyakit hati, penyakit pundi hempedu, trombositopenia, neutropenia, agranulositosis, kolitis *Clostridium difficile*, enterokolitis nekrotik perinatal, kekurangan G6PD, penyakit penyimpanan glikogen, sistinuria, galaktosemia dan anemia kekurangan asid folik.

**Interaksi Ubat** (100 interaksi dikesan; contoh utama):
- **Major**: kalium sitrat, kalium bikarbonat, kalium klorida, kalium gluconate (risiko hiperkalemia)
- **Moderate**: metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid, sapropterin
- Tahap tidak diketahui: pantoprazole, doxycycline, omeprazole, simvastatin dan lain-lain

**Isyarat keselamatan daripada literatur**: laporan kes sindrom SCoRCH (konjunktivitis, limfopenia, ruam dan perubahan hemodinamik) selepas penggunaan TMP-SMX, serta hiponatremia berkaitan TMP-SMX. Pemantauan hiperkalemia, mielosupresi dan ruam disyorkan, termasuk semakan interaksi (contohnya zidovudine, methotrexate).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Proceed with Guardrails**

**Justifikasi:**
- Pneumocystosis ialah indikasi mantap dengan banyak percubaan Fasa 3 yang selesai (TMP-SMX sebagai rawatan, profilaksis dan pembanding), jadi tahap bukti L1 munasabah. Namun, bukti kebanyakannya untuk gabungan TMP-SMX dan bukan trimethoprim tunggal, dan skor TxGNN ialah 0.0.

**Untuk meneruskan, perlu dilengkapkan:**
- Data MOA terperinci daripada DrugBank
- Amaran dan kontraindikasi daripada sisipan pakej NPRA (kini tiada, dan ini menghalang saringan keselamatan lanjut)
- Penyelarasan status pasaran Malaysia (laporan "Tidak dipasarkan" berbanding produk TMP-SMX yang wujud)
- Pelan pemantauan keselamatan (kalium, hematologi, fungsi buah pinggang, ruam) dan semakan interaksi ubat

---

## Penilaian Indikasi Lain yang Diramalkan (Ringkas)

| Indikasi | Tahap Bukti | Keputusan | Catatan |
|------|------|------|------|
| Jangkitan saluran kencing | L1 | Proceed with Guardrails | Indikasi sedia ada; percubaan RIVUR (Fasa 3, n=607) menyokong profilaksis TMP-SMX; perhatikan rintangan tempatan, fungsi buah pinggang dan kehamilan |
| Otitis media berjangkit | L2 | Research Question | Bukti terhad (satu kajian fasa NA); rintangan pneumokokus dan *Haemophilus* semakin meningkat |
| Konjunktivitis | L2 | Research Question | Bukti terutamanya untuk gabungan topikal polymyxin B/trimethoprim; tiada percubaan berdaftar |
| Konjunktivitis berjangkit akut | L5 | Hold | Tiada percubaan atau literatur dalam data |
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

