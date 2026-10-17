---
layout: default
title: Insulin Lispro
parent: Low Evidence (L4-L5)
nav_order: 423
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Insulin Lispro: indikasi baharu diramal Autoimmune oophoritis (tahap bukti L5). Indikasi asal: Diabetes mellitus jenis 2, diabetes mellitus jenis 1…"
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **9** 
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

# Insulin Lispro: Daripada Diabetes Mellitus kepada Autoimmune Oophoritis

## Ringkasan Satu Ayat

Insulin lispro ialah analog insulin yang digunakan untuk merawat diabetes mellitus (jenis 1 dan jenis 2) serta ketoasidosis diabetes.
Model TxGNN meramalkan ia mungkin berkesan untuk **autoimmune oophoritis**,
tetapi pada masa ini **tiada percubaan klinikal** dan **tiada penerbitan** yang menyokong ramalan ini. Ramalan ini hanyalah hasil pengiraan model.

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Diabetes mellitus jenis 2, diabetes mellitus jenis 1, ketoasidosis diabetes |
| Indikasi Baharu yang Diramalkan | Autoimmune oophoritis |
| Skor Ramalan TxGNN | 99.78% |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Tidak dipasarkan |
| Bilangan Pendaftaran | 0 |
| Keputusan Disyorkan | Hold |

---

## Mengapa Ramalan Ini Munasabah?

Data terperinci mengenai mekanisme tindakan insulin lispro tidak tersedia buat masa ini. Berdasarkan maklumat yang diketahui, insulin lispro ialah analog insulin yang khasiatnya dalam mengawal glukosa darah pada diabetes telah terbukti, tetapi tiada mekanisme yang dapat disahkan untuk autoimmune oophoritis.

Satu kemungkinan hubungan ialah autoimmune oophoritis sering berlaku bersama sindrom poliendokrin autoimun yang merangkumi diabetes jenis 1. Oleh itu, perkaitan dalam graf pengetahuan mungkin mencerminkan kejadian bersama penyakit, dan **bukan** kesan terapeutik insulin terhadap autoimuniti ovari.

Skor TxGNN yang tinggi (0.998) tidak boleh ditafsirkan sebagai bukti keberkesanan. Ia ialah ramalan komputasi semata-mata.

### Ramalan Lain yang Dinilai

Ramalan lain bagi ubat ini juga berada pada tahap bukti rendah dan semuanya disyorkan **Hold**:

| Penyakit Diramalkan | Skor TxGNN | Tahap Bukti | Catatan |
|------|------|------|------|
| Thiamine-responsive dysfunction syndrome | 99.37% | L5 | Insulin hanya merawat hiperglisemia secara simptomatik; rawatan utama ialah tiamina |
| Classic stiff person syndrome | 99.36% | L5 | Mungkin mencerminkan autoimuniti anti-GAD65 dan komorbiditi diabetes jenis 1 |
| Focal stiff limb syndrome | 99.36% | L5 | Skor serupa dengan sindrom di atas; kemungkinan diwarisi daripada nod penyakit berkaitan |
| Opsismodysplasia | 99.34% | L5 | Hubungan spekulatif melalui INPPL1 (SHIP2) dalam isyarat insulin/PI3K |
| Drug-induced localized lipodystrophy | 99.09% | L5 | Kesan advers insulin yang diketahui; isyarat keselamatan, bukan peluang repurposing |
| Pancreatic agenesis | 99.09% | L4 | Penggantian insulin ialah rawatan standard sedia ada, bukan repurposing baharu |
| Centrifugal lipodystrophy | 99.04% | L5 | Kemungkinan daripada kluster nod lipodistrofi dalam graf |
| Pressure-induced localized lipoatrophy | 99.03% | L5 | Mungkin mencerminkan kesan tempatan suntikan insulin, iaitu potensi bahaya |

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan didaftarkan.

---

## Bukti Literatur

Untuk ramalan utama (autoimmune oophoritis), pada masa ini tiada literatur berkaitan.

Satu penerbitan ditemui bagi ramalan peringkat ketujuh (pancreatic agenesis), tetapi ia hanya bukti tidak langsung:

| PMID | Tahun | Jenis | Jurnal | Dapatan Utama |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Ulasan | Journal of the American Pharmaceutical Association | Ulasan penggunaan terapi insulin yang semakin meningkat pada pesakit diabetes jenis 2 dan aspek praktikal memulakannya. Tidak membincangkan pancreatic agenesis secara langsung. |

---

## Keselamatan

- **Interaksi Ubat**: Pertanyaan interaksi ubat telah selesai dengan 100 interaksi direkodkan. Kebanyakannya bertahap **Sederhana**, dan sebahagian kecil bertahap **Minor**. Contoh utama:
  - Agen antidiabetik lain (metformin, alogliptin, albiglutide): kesan hipoglisemik boleh bertambah.
  - Agonis beta dan simpatomimetik (salbutamol, formoterol, epinefrin, fenilefrin, pseudoefedrin): boleh mengubah kawalan glukosa.
  - Beta-blocker (asebutolol): boleh menyembunyikan tanda hipoglisemia.
  - Kortikosteroid (hidrokortison): boleh meningkatkan glukosa darah.
  - Hormon (estradiol, etinilestradiol, levonorgestrel), diuretik (hidroklorotiazid, asetazolamida), doksisiklin, alpelisib dan etanol.
- **Isyarat keselamatan daripada ramalan**: lipodistrofi setempat ialah kesan advers yang diketahui pada tapak suntikan insulin berulang. Ramalan lipodistrofi dalam model harus dianggap sebagai isyarat keselamatan.

Untuk amaran utama dan kontraindikasi, sila rujuk sisipan pakej.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold**

**Justifikasi:**
- Ramalan autoimmune oophoritis berada pada tahap bukti L5 tanpa percubaan klinikal atau literatur. Perkaitan itu berkemungkinan mencerminkan kejadian bersama penyakit autoimun dan diabetes, bukan kesan terapeutik. Ubat ini juga tidak berdaftar di Malaysia.

**Untuk meneruskan, perkara berikut diperlukan:**
- Data mekanisme tindakan (MOA) yang terperinci
- Amaran dan kontraindikasi daripada sisipan pakej (data ini diperlukan sebelum saringan keselamatan boleh diteruskan)
- Kajian praklinikal atau klinikal yang menilai insulin secara langsung dalam autoimmune oophoritis
- Penjelasan status pendaftaran dan laluan pentadbiran yang diperlukan di Malaysia
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

