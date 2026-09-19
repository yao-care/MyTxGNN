---
layout: default
title: Turoctocog Alfa Pegol
parent: Low Evidence (L4-L5)
nav_order: 675
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog Alfa Pegol: Daripada Hemofilia A kepada Gangguan Pelepasan Primer Plat

## Ringkasan Satu Ayat

Turoctocog alfa pegol (DrugBank DB14738) ialah produk penggantian Faktor VIII yang tersusun semula dan dipegil, dirujuk dalam pakej bukti sebagai diluluskan untuk kekurangan Faktor VIII bawaan (Hemofilia A). Model TxGNN meramalkan bahawa ia mungkin berkesan untuk **Gangguan Pelepasan Primer Plat**, tetapi arah ini pada masa ini disokong oleh **0 percubaan klinikal** dan **0 penerbitan**, dan anotasi mekanik model itu sendiri menandakan tiada pautan farmakologi langsung antara dua keadaan tersebut.

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak direkodkan secara rasmi dalam dataset ini (`original_indications` kosong; teks petunjuk lesen NPRA juga kosong). Teks rasional di tempat lain dalam pakej mengenal pasti kelas ubat sebagai terapi penggantian kekurangan Faktor VIII bawaan (Hemofilia A). |
| Petunjuk Baru yang Diramalkan | Gangguan pelepasan primer plat |
| Skor Ramalan TxGNN | 99.9966% |
| Tahap Bukti | L5 (ramalan model sahaja, tiada sokongan klinikal atau literatur) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 4 |
| Keputusan yang Disyorkan | Tahan |

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan terperinci untuk turoctocog alfa pegol ditandai sebagai jurang data dalam pakej bukti ini (DG002, keterukan tinggi). Berdasarkan maklumat yang tersedia, beberapa anotasi rasional model itu sendiri menggambarkan ubat ini sebagai terapi penggantian Faktor VIII yang tersusun semula dan dipegil, ditunjukkan untuk kekurangan Faktor VIII bawaan (Hemofilia A) — gangguan lata pembekuan yang diperbetulkan oleh penggantian faktor pembekuan eksogen.

Gangguan pelepasan primer plat, bagaimanapun, ialah kerosakan **fungsi** plat (pelepasan granula terganggu, contohnya penyakit kolam penyimpanan delta/alfa), bukan kekurangan faktor pembekuan. Anotasi mekanik pakej bukti sendiri untuk calon ini menyatakan dengan jelas bahawa terdapat "tiada persatuan mekanik langsung" antara patologi pelepasan granula plat dan penggantian Faktor VIII. Ini mencadangkan bahawa skor TxGNN yang sangat tinggi kemungkinan besar mencerminkan kedekatan topologi graf antara gangguan plat dan gangguan pembekuan dalam graf pengetahuan, dan bukannya rasional farmakologi yang terbukti.

Memandangkan ini, ramalan harus dibaca sebagai isyarat penjanaan hipotesis daripada calon yang berasaskan mekanik, selaras dengan tahap bukti L5 dan cadangan Tahan yang telah diperuntukkan dalam data sumber.

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal terkait yang didaftarkan.

## Bukti Literatur

Pada masa ini tiada literatur terkait yang tersedia.

## Maklumat Pasaran Malaysia

Rekod NPRA menunjukkan turoctocog alfa pegol sebagai dipasarkan di Malaysia dengan **4 pendaftaran aktif**. Namun, butiran lesen individu (nombor kelulusan, nama produk, bentuk dos, teks petunjuk yang diluluskan) tidak diisi dalam dataset semasa dan tidak dapat ditabelkan.

## Pertimbangan Keselamatan

Sila rujuk risalah bungkusan untuk maklumat keselamatan.

*(Nota: Data `key_warnings`, `contraindications`, dan DDI semuanya tidak tersedia dalam pakej bukti ini — DG001, Keterukan Sekatan — yang dengan sendirinya menghalang kemajuan ke peringkat pra-penilaian keselamatan S1.)*

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Ramalan disokong hanya oleh skor model TxGNN (L5, tiada percubaan klinikal atau literatur), dan anotasi mekanik pakej bukti itu sendiri menunjukkan tiada pautan farmakologi langsung antara penggantian Faktor VIII dan gangguan pelepasan granula plat. Jurang data berkadar keterukan Sekatan (amaran label TFDA/NPRA dan kontraindikasi) juga menghalang sebarang pra-penilaian keselamatan pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**
- Risalah bungkusan TFDA/NPRA (amaran, kontraindikasi) — diperlukan sebelum sebarang pra-penilaian keselamatan (DG001, Sekatan)
- Mekanisme tindakan yang disahkan daripada DrugBank atau literatur utama (DG002, Tinggi)
- Teks petunjuk asal yang disahkan (pada masa ini hilang daripada kedua-dua `original_indications` dan rekod lesen NPRA)
- Butiran lesen Malaysia yang lengkap (nombor kelulusan, nama produk, bentuk dos)
- Bukti praklinikal atau mekanik bebas yang secara khusus menghubungkan aktiviti laluan Faktor VIII kepada fisiologi pelepasan granula plat, sebelum sebarang penerokaan klinikal dipertimbangkan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

