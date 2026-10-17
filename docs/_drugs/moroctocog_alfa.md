---
layout: default
title: Moroctocog Alfa
parent: Low Evidence (L4-L5)
nav_order: 512
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Moroctocog Alfa: indikasi baharu diramal Gangguan pelepasan primer platelet (tahap bukti L5). Indikasi asal: Hemofilia"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Moroctocog Alfa
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **8** 
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

# Moroctocog Alfa: Daripada Hemofilia kepada Gangguan Pelepasan Primer Platelet

## Ringkasan Satu Ayat

Moroctocog alfa ialah faktor VIII rekombinan dengan domain-B dibuang, yang pada asalnya digunakan untuk merawat hemofilia (termasuk bentuk bergejala hemofilia pada pembawa wanita).
Model TxGNN meramalkan ia mungkin berkesan untuk **gangguan pelepasan primer platelet** (primary release disorder of platelets) dengan skor tinggi.
Walau bagaimanapun, kini terdapat **0 percubaan klinikal** dan **0 penerbitan** yang menyokong ramalan ini, jadi ia kekal sebagai ramalan model sahaja.

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Hemofilia |
| Indikasi Baharu yang Diramalkan | Gangguan pelepasan primer platelet |
| Skor Ramalan TxGNN | 99.97% |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Tidak dipasarkan |
| Bilangan Pendaftaran | 0 |
| Keputusan Disyorkan | Hold (Tangguh) |

---

## Mengapa Ramalan Ini Munasabah?

Maklumat terperinci mengenai mekanisme tindakan tidak tersedia buat masa ini. Berdasarkan maklumat sedia ada, moroctocog alfa ialah faktor VIII (FVIII) rekombinan yang menggantikan FVIII yang kurang dalam laluan koagulasi intrinsik. Keberkesanannya dalam hemofilia telah dibuktikan.

Namun, gangguan pelepasan primer platelet ialah kecacatan kualitatif fungsi platelet, sedangkan tahap FVIII adalah normal. Oleh itu, tiada asas mekanistik yang jelas untuk penggantian FVIII dalam keadaan ini. Skor TxGNN yang tinggi (0.9997) hanyalah ramalan berasaskan graf dan tidak disokong oleh sebarang percubaan atau penerbitan.

### Indikasi Lain yang Diramalkan

Model turut meramalkan indikasi lain. Semuanya berada pada tahap bukti L5 dengan syor Hold:

| Kedudukan | Penyakit | Skor TxGNN | Penilaian Mekanistik |
|------|------|------|------|
| 2 | Penyakit von Willebrand palsu (pseudo-von Willebrand disease) | 99.97% | Disebabkan kecacatan peningkatan fungsi GP1BA. Penggantian FVIII sahaja tidak membetulkannya. Hanya terdapat kaitan tidak langsung melalui paksi VWF-FVIII. |
| 3 | Trombastenia Glanzmann | 99.96% | Disebabkan ketiadaan atau kecacatan integrin αIIbβ3. Rawatan piawai ialah transfusi platelet dan FVIIa rekombinan. Tiada sokongan mekanistik. |
| 4 | Kekurangan faktor pembekuan yang diperoleh | 99.88% | Paling munasabah dari segi mekanisme, kerana kehilangan aktiviti FVIII boleh diimbangi oleh penggantian faktor. Namun, hemofilia dapatan biasanya didorong oleh autoantibodi perencat yang meneutralkan FVIII yang disuntik. Kategori ini juga luas. |
| 5 | Sindrom Scott | 99.86% | Kecacatan prokoagulan platelet (kekurangan TMEM16F/ANO6). FVIII biasanya normal. |
| 6 | Diatesis pendarahan akibat kecacatan reseptor kolagen | 99.73% | Reseptor kolagen platelet yang cacat. Penggantian FVIII tidak menyasarkan laluan ini. |
| 7 | Gangguan pendarahan akibat trombositopenia konstitusi | 99.72% | FVIII normal. Skor tinggi mungkin mencerminkan kedekatan rangkaian "gangguan pendarahan". |
| 8 | "Flood factor deficiency" | 99.11% | Bukan istilah penyakit piawai dan mungkin artifak ontologi atau penamaan. Tidak boleh dinilai sehingga dipetakan kepada keadaan yang ditakrifkan. |

---

## Bukti Percubaan Klinikal

Buat masa ini tiada percubaan klinikal berkaitan yang didaftarkan.

---

## Bukti Literatur

Buat masa ini tiada literatur berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

Moroctocog alfa kini **tidak dipasarkan** di Malaysia dan tiada pendaftaran (lesen) direkodkan dalam data yang dihimpunkan untuk laporan ini.

---

## Pertimbangan Keselamatan

Sila rujuk risalah pakej (package insert) untuk maklumat keselamatan. Data interaksi ubat tidak ditemui dalam data yang dihimpunkan untuk laporan ini.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold (Tangguh)**

**Justifikasi:**
- Semua indikasi yang diramalkan berada pada tahap bukti L5 (ramalan model sahaja) tanpa sebarang percubaan klinikal atau penerbitan. Kebanyakan indikasi juga tidak mempunyai asas mekanistik yang jelas kerana melibatkan kecacatan platelet dengan FVIII yang normal.
- Ubat ini juga tidak dipasarkan di Malaysia.

**Untuk meneruskan, perkara berikut diperlukan:**
- Risalah pakej NPRA yang memuatkan amaran dan kontraindikasi (jurang data yang menyekat penyaringan keselamatan)
- Data mekanisme tindakan (MOA) terperinci daripada DrugBank
- Pemetaan istilah "flood factor deficiency" kepada keadaan penyakit yang ditakrifkan
- Jika ingin diteruskan, utamakan **kekurangan faktor pembekuan yang diperoleh** untuk semakan literatur dan penilaian peranan autoantibodi perencat
- Maklumat laluan pentadbiran dan kesesuaian formulasi bagi mana-mana indikasi baharu
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

