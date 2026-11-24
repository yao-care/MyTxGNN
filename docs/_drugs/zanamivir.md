---
layout: default
title: Zanamivir
parent: Low Evidence (L4-L5)
nav_order: 730
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "ZANAMIVIR"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
description: "Zanamivir: indikasi baharu diramal Pyelonephritis (tahap bukti L5). Di Malaysia, pendaftaran NPRA: 1 (sah: 0)"
---

# Zanamivir
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **2** 
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

## Zanamivir: Pyelonephritis
{: .text-alpha }

## Ringkasan Satu Ayat

Zanamivir ialah perencat neuraminidase yang pada asalnya digunakan untuk merawat influenza.
Model TxGNN meramalkan ia mungkin berkesan untuk **pyelonephritis** (jangkitan buah pinggang),
tetapi pada masa ini terdapat **0 ujian klinikal** dan **0 penerbitan** yang menyokong arah ini, jadi ramalan ini hanya berasaskan model.

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Tidak direkodkan dalam data tempatan |
| Indikasi Baharu yang Diramalkan | Pyelonephritis |
| Skor Ramalan TxGNN | 0.9984 |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Tidak dipasarkan (tiada pendaftaran semasa: 1 daripada 1 dibatalkan, tamat tempoh atau tidak lagi tersenarai dalam daftar NPRA) |
| Bilangan Pendaftaran | 1 (sah: 0) |
| Keputusan Disyorkan | Hold |

---

## Mengapakah Ramalan Ini Munasabah?

Menurut bahagian “Mechanism of Action” dan “Microbiology” maklumat preskripsi yang diluluskan oleh FDA Amerika Syarikat (Prescribing Information) bagi Zanamivir (terjemahan tidak rasmi): “Zanamivir ialah ubat antivirus dengan aktiviti terhadap virus influenza. […] Zanamivir ialah perencat neuraminidase (NA) virus influenza, iaitu enzim yang membebaskan partikel virus daripada membran plasma sel yang dijangkiti dan menggalakkan penyebaran virus dalam saluran pernafasan. Dalam asai perencatan neuraminidase, zanamivir aktif terhadap semua subjenis enzim NA N1 hingga N9.” Teks asal bahasa Inggeris: "Zanamivir is an antiviral drug with activity against influenza virus. […] Zanamivir is an inhibitor of influenza virus neuraminidase (NA), an enzyme that releases viral particles from the plasma membrane of infected cells and promotes virus spread in the respiratory tract. In neuraminidase inhibition assays, zanamivir is active against all NA enzyme subtypes N1 to N9." ([DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d), versi 2026-07-23; diakses 2026-11-19). Berdasarkan maklumat yang diketahui, zanamivir ialah perencat sialidase (neuraminidase) virus influenza, dan keberkesanannya dalam influenza telah dibuktikan.

Pyelonephritis pula ialah jangkitan **bakteria** pada buah pinggang, lazimnya disebabkan oleh *Escherichia coli* uropatogenik. Tiada kaitan mekanistik yang kukuh dapat dikenal pasti. Walaupun bakteria juga mempunyai sialidase, tiada data menunjukkan zanamivir merencatnya pada kepekatan yang bermakna secara klinikal, dan tiada bukti kesan antibakteria di saluran kencing.

Skor TxGNN yang sangat tinggi (0.9984) ialah ramalan berasaskan model semata-mata. Skor ini datang daripada model TxGNN (pembelajaran mendalam) dan mungkin mencerminkan persamaan yang dipelajari model antara penyakit yang berkaitan, bukan bukti biologi. Selain itu, ketiadaan data MOA menghadkan kebolehlaksanaan.

<!-- review:begin my-lic-20261105-zanamivir-1 -->

> **Pembetulan semakan (2026-11-05)**: Asalnya dinyatakan: "Selain itu, ubat ini dipasarkan di Malaysia (1 lesen sah daripada 1), tetapi ketiadaan data MOA menghadkan kebolehlaksanaan." Dipadam: bilangan atau status pendaftaran yang dinyatakan tidak sepadan dengan data pendaftaran produk NPRA (data.gov.my) yang dibina semula mengikut bahan aktif pada 2026-11-05. Bilangan pendaftaran semasa terdapat dalam Gambaran Ringkas halaman ini. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261105-zanamivir-1 -->

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan didaftarkan.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan untuk indikasi pyelonephritis.

---

## Maklumat Pasaran Malaysia

<!-- licenses:begin -->

| No. Pendaftaran | Nama Produk (NPRA, bahasa asal) | Jenis | Pemegang Pendaftaran | Status |
|------|------|------|------|------|
| MAL20061471ARZ | RELENZA ROTADISK 5MG | Bahan tunggal | GLAXOSMITHKLINE PHARMACEUTICAL SDN. BHD. | Tamat tempoh (tiada dalam daftar semasa NPRA) |

<!-- licenses:end -->

---

## Pertimbangan Keselamatan

- **Interaksi Ubat** (8 interaksi direkodkan): 
  - Insulin manusia (disedut, bertindak pantas): tahap **Sederhana**
  - Clarithromycin, loratadine, montelukast, ketotifen, fexofenadine, ibuprofen, diclofenac: tahap tidak diketahui
- **Penyakit yang Dikaitkan dengan Kontraindikasi (berdasarkan graf pengetahuan, bukan teks label)**: epilepsi, penyakit pulmonari obstruktif kronik (COPD), penyakit bronkus, delirium.

Untuk amaran dan kontraindikasi rasmi, sila rujuk sisipan pakej.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold**

**Rasional:**
- Ramalan pyelonephritis hanya berasaskan model (L5), tanpa ujian klinikal atau literatur sokongan, dan tiada kaitan mekanistik yang munasabah antara perencatan neuraminidase virus dengan jangkitan bakteria buah pinggang.

**Untuk meneruskan, perkara berikut diperlukan:**
- Data mekanisme tindakan (MOA) yang lengkap
- Data in vitro atau praklinikal yang menunjukkan aktiviti antibakteria terhadap patogen uropatogenik
- Amaran dan kontraindikasi daripada sisipan pakej yang diluluskan oleh NPRA
- Pertimbangan status pendaftaran dan ketersediaan produk di Malaysia

---

<!-- review:begin log -->

## Rekod Semakan

Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA (data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan tidak ditulis semula. Ayat yang menyatakan data mekanisme tindakan tidak tersedia telah diganti dengan petikan daripada maklumat preskripsi rasmi yang dipetik (dengan terjemahan tidak rasmi).

| Tarikh semakan | Perkara | Tindakan | Sumber |
|------|------|------|------|
| 2026-11-05 | Dipadam: "ubat ini dipasarkan di Malaysia (1 lesen sah daripada 1), tetapi" | Dibetulkan (disemak 2026-11-24; versi terdahulu disimpan dalam rekod) | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |
| 2026-11-19 | Ayat “data mekanisme tindakan tidak tersedia” diganti dengan petikan maklumat preskripsi AS | Ayat bahawa data mekanisme tindakan tidak tersedia diganti dengan petikan bersumber | [DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d) |

<!-- review:end log -->

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

