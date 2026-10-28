---
layout: default
title: Nonivamide
parent: Low Evidence (L4-L5)
nav_order: 531
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
monitor_inn: "Nonivamide"
predicted_indications: ["pulmonary hypertension", "peripheral arterial disease", "acute lymphoblastic leukemia (disease)", "kyphoscoliotic heart disease", "peripheral vascular disease", "ventricular tachycardia", "anaphylaxis", "migraine disorder", "catecholaminergic polymorphic ventricular tachycardia", "intermittent vascular claudication"]
description: "Nonivamide: indikasi baharu diramal Hipertensi pulmonari (pulmonary hypertension) (tahap bukti L5). Indikasi asal: Tidak direkodkan dalam data tempatan"
---

# Nonivamide
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

## Nonivamide: Hipertensi pulmonari (pulmonary hypertension)
{: .text-alpha }

## Ringkasan Satu Ayat

Nonivamide ialah analog kapsaisin sintetik dan agonis TRPV1, tetapi data yang dikumpulkan untuk laporan ini tidak mengandungi sebarang indikasi asal yang diluluskan di Malaysia.
Model TxGNN meramalkan ia mungkin berkesan untuk **hipertensi pulmonari**, namun terdapat **0 percubaan klinikal** dan **0 penerbitan** yang menyokong arah ini.
Ramalan ini hanya berasaskan skor model komputasi (Tahap Bukti L5).

---

## Gambaran Ringkas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Tidak direkodkan dalam data tempatan |
| Indikasi Baharu yang Diramalkan | Hipertensi pulmonari (pulmonary hypertension) |
| Skor Ramalan TxGNN | 0.9981 |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 5 daripada 5) |
| Bilangan Pendaftaran | 5 (sah: 5) |
| Keputusan Disyorkan | Hold (Tangguh) |

---

## Mengapa Ramalan Ini Munasabah?

Data terperinci mengenai mekanisme tindakan asal tidak tersedia buat masa ini. Berdasarkan maklumat yang diketahui, nonivamide ialah analog kapsaisin sintetik dan agonis TRPV1. Tiada indikasi asal yang diluluskan direkodkan di Malaysia, jadi hubungan dengan indikasi baharu tidak dapat dinilai melalui perbandingan indikasi.

Secara hipotesis, TRPV1 diekspresikan pada saluran darah pulmonari dan saraf deria, dan modulasinya mungkin mempengaruhi tonus vaskular serta pembentukan semula vaskular pulmonari. Pautan ini bersifat andaian sahaja. Skor tinggi TxGNN ialah ramalan komputasi tanpa sokongan klinikal atau literatur.

### Calon Ramalan Lain

Selain hipertensi pulmonari, model turut meramalkan indikasi berikut. Kesemuanya berada pada Tahap Bukti L5 dan berstatus Hold.

| Kedudukan | Penyakit | Skor TxGNN | Penilaian Pautan Mekanistik |
|------|------|------|------|
| 2 | Penyakit arteri periferal | 0.9981 | Pelepasan CGRP dan bahan P melalui TRPV1 boleh menyebabkan vasodilasi; masih hipotesis |
| 3 | Leukemia limfoblastik akut | 0.9979 | Kesan antiproliferatif kapsaisin pada sel kanser dalam kajian praklinikal; rasional lemah dan tidak langsung |
| 4 | Penyakit jantung kifoskoliotik | 0.9977 | Tiada pautan mekanistik langsung; kemungkinan artifak model |
| 5 | Penyakit vaskular periferal | 0.9972 | Bertindih dengan penyakit arteri periferal; rasional hipotesis yang sama |
| 6 | Takikardia ventrikel | 0.9972 | Pautan spekulatif; pengaktifan simpatetik mungkin pro-aritmia, jadi keselamatan menjadi kebimbangan |
| 7 | Anafilaksis | 0.9967 | Hubungan konseptual longgar melalui keradangan neurogenik; tidak sesuai untuk kecemasan akut |
| 8 | Gangguan migrain | 0.9967 | Pautan paling koheren: TRPV1 pada neuron trigeminal dan peranan CGRP dalam migrain |
| 9 | Takikardia ventrikel polimorfik katekolaminergik | 0.9966 | Tiada pautan jelas dengan TRPV1; rangsangan simpatetik mungkin berbahaya |
| 10 | Klaudikasi vaskular berselang-seli | 0.9965 | Manifestasi gejala penyakit arteri periferal; rasional sama seperti PAD |

Walaupun migrain mempunyai pautan mekanistik yang paling koheren antara semua calon, tiada bukti khusus nonivamide dibekalkan, jadi ia kekal sebagai ramalan semata-mata.

---

## Bukti Percubaan Klinikal

Buat masa ini tiada percubaan klinikal berkaitan didaftarkan.

---

## Bukti Literatur

Buat masa ini tiada literatur berkaitan tersedia.

---

## Maklumat Pasaran Malaysia


---

## Pertimbangan Keselamatan

- **Interaksi Ubat**: Pertanyaan interaksi ubat tidak menemui sebarang rekod dalam data yang dikumpulkan.
- **Kebimbangan khusus calon**: Untuk indikasi aritmia (takikardia ventrikel dan CPVT), pengaktifan simpatetik oleh agonis TRPV1 berpotensi memudaratkan dan perlu dinilai dengan teliti.

Sila rujuk sisipan pakej untuk maklumat keselamatan lanjut.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold (Tangguh)**

**Rasional:**
- Semua ramalan hanya bergantung pada skor model TxGNN (pembelajaran mendalam) (Tahap Bukti L5) tanpa percubaan klinikal atau literatur sokongan; skor ini mungkin mencerminkan persamaan yang dipelajari oleh model antara penyakit yang berkaitan, bukan bukti biologi. Ubat ini dipasarkan di Malaysia (5 lesen sah daripada 5), dan data mekanisme tindakan serta keselamatan masih tidak lengkap.

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran dan kontraindikasi daripada sisipan pakej NPRA (jurang data yang menyekat peringkat saringan keselamatan seterusnya)
- Data mekanisme tindakan (MOA) terperinci daripada DrugBank
- Semakan literatur dan percubaan klinikal khusus nonivamide, terutamanya untuk migrain (calon paling koheren secara mekanistik) dan hipertensi pulmonari
- Penilaian keserasian laluan pentadbiran (topikal, intranasal atau sistemik) bagi setiap indikasi calon
- Penilaian keselamatan kardiovaskular sebelum mempertimbangkan sebarang indikasi kardiak
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

