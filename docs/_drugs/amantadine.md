---
layout: default
title: Amantadine
parent: Low Evidence (L4-L5)
nav_order: 51
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Amantadine: indikasi baharu diramal Rasmussen subacute encephalitis (tahap bukti L5). Indikasi asal: Penyakit Parkinson (dan gangguan parkinsonisme yang berkaitan)"
monitor_inn: "amantadine"
predicted_indications: ["Rasmussen subacute encephalitis", "transaldolase deficiency", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Amantadine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **4** 
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

## Amantadine: Daripada Penyakit Parkinson kepada Rasmussen Subacute Encephalitis
{: .text-alpha }

## Ringkasan Satu Ayat

Amantadine pada asalnya digunakan untuk merawat penyakit Parkinson dan gangguan parkinsonisme yang berkaitan.
Model TxGNN meramalkan ia mungkin berkesan untuk **Rasmussen subacute encephalitis**,
tetapi pada masa ini **tiada percubaan klinikal** dan **tiada literatur** dalam data yang dikumpulkan untuk laporan ini yang menyokong ramalan tersebut.

## Gambaran Ringkas

| Item | Kandungan |
|------|------|
| Indikasi Asal | Penyakit Parkinson (dan gangguan parkinsonisme yang berkaitan) |
| Indikasi Baharu yang Diramalkan | Rasmussen subacute encephalitis |
| Skor Ramalan TxGNN | 0.9948 |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 1 daripada 1) |
| Bilangan Pendaftaran | 1 (sah: 1) |
| Keputusan Disyorkan | Hold (Tangguh) |

## Mengapa Ramalan Ini Munasabah?

Data terperinci tentang mekanisme tindakan (MOA) amantadine tidak tersedia dalam data yang dikumpulkan untuk laporan ini. Penilaian awal menunjukkan bahawa amantadine ialah antagonis reseptor NMDA, dan secara teori ia boleh mengurangkan eksitotoksisiti yang dimediasi glutamat serta keradangan saraf.

Rasmussen encephalitis ialah ensefalitis kronik yang bersifat imun dan disertai epilepsi. Secara teori, pengurangan eksitotoksisiti glutamat mungkin relevan. Namun, ini hanyalah hipotesis berasaskan ramalan komputasi; tiada data klinikal dalam set data ini yang menyokongnya.

Skor TxGNN yang sangat tinggi tidak boleh dianggap sebagai bukti keberkesanan. Ramalan ini perlu disahkan melalui kajian praklinikal dan klinikal.

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan didaftarkan.

## Bukti Literatur

Pada masa ini tiada literatur berkaitan.

## Pertimbangan Keselamatan

- **Penyakit/keadaan yang dikaitkan dengan kontraindikasi (berdasarkan graf pengetahuan, bukan teks label):** sindrom atrofi sistem berbilang, sindrom takikardia ortostatik postural, hipotensi ortostatik, epilepsi, penyakit buah pinggang, pyoureter, kegagalan jantung kongestif, gangguan psikotik, gangguan skizofreniform, gangguan mental, gangguan skizoafektif, melanoma, glaukoma sudut tertutup, gangguan berkaitan bahan, penyalahgunaan/kebergantungan bahan, ekzema atopik, dermatitis.
  - Nota: epilepsi tersenarai sebagai kontraindikasi dalam graf pengetahuan, sedangkan Rasmussen encephalitis disertai sawan. Perkara ini perlu dinilai dengan teliti.
- **Interaksi Dadah:** sebanyak 93 interaksi dikesan. Yang utama:
  - **Major:** Bupropion
  - **Moderate:** agen antikolinergik/antimuskarinik (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine, mepenzolate, methscopolamine, propantheline, scopolamine, trospium), metoclopramide, polyethylene glycol (3350 dengan elektrolit), picosulfuric acid, natrium sulfat
  - Beberapa interaksi lain (contohnya calcitriol, pantoprazole, glimepiride, doxycycline, metformin) belum ditentukan tahapnya.

Sila rujuk sisipan pakej produk untuk maklumat amaran dan kontraindikasi yang rasmi.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold (Tangguh)**

**Justifikasi:**
- Skor ramalan tinggi (0.9948), tetapi ia hanya ramalan model (L5) tanpa percubaan klinikal atau literatur sokongan. Graf pengetahuan menyenaraikan epilepsi sebagai kontraindikasi.

<!-- review:begin my-lic-20261105-amantadine-1 -->

> **Pembetulan semakan (2026-11-05)**: Asalnya dinyatakan: "Ubat ini juga tidak berdaftar di Malaysia, dan graf pengetahuan menyenaraikan epilepsi sebagai kontraindikasi." Dipadam: ia menyatakan ubat ini tidak berdaftar, pendaftarannya dibatalkan atau tamat tempoh, atau tidak dipasarkan di Malaysia, yang tidak sepadan dengan data pendaftaran produk NPRA (data.gov.my) yang dibina semula mengikut bahan aktif pada 2026-11-05. Ubat ini mempunyai 1 pendaftaran (sah: 1); angka semasa terdapat dalam Gambaran Ringkas dan jadual di bawah Maklumat Pasaran Malaysia. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261105-amantadine-1 -->

**Untuk meneruskan, perkara berikut diperlukan:**
- Data mekanisme tindakan (MOA) yang lengkap
- Maklumat amaran dan kontraindikasi daripada sisipan pakej (data NPRA belum diperoleh; ini menghalang saringan keselamatan)
- Kajian praklinikal atau laporan kes bagi Rasmussen encephalitis
- Penilaian risiko sawan memandangkan epilepsi disenaraikan sebagai kontraindikasi
- Penilaian status pendaftaran dan ketersediaan produk di Malaysia

---

### Nota Tambahan: Indikasi Lain yang Diramalkan

Data yang dikumpulkan turut merangkumi tiga ramalan lain, dan semuanya juga belum cukup kukuh:

| Indikasi Diramalkan | Skor TxGNN | Tahap Bukti | Ringkasan |
|------|------|------|------|
| Transaldolase deficiency | 0.9927 | L5 | Tiada bukti dan tiada rasional mekanistik yang jelas; ramalan mungkin didorong oleh kedekatan rangkaian |
| Myelitis | 0.9924 | L5 | Literatur sebenarnya berkaitan sindrom pasca-polio (contohnya RCT 1995 tentang keletihan, PMID 7611638); kaitan dengan myelitis tidak langsung dan faedahnya tidak jelas |
| PLA2G6-associated neurodegeneration | 0.9923 | L5 | Hanya satu laporan tidak langsung tentang PKAN (PMID 31366412); ekstrapolasi belum disahkan |

<!-- review:begin log -->

## Rekod Semakan

Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA (data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan tidak ditulis semula.

| Tarikh semakan | Perkara | Tindakan | Sumber |
|------|------|------|------|
| 2026-11-05 | Dipadam: "Ubat ini juga tidak berdaftar di Malaysia, dan" | Dibetulkan | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |

<!-- review:end log -->

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

