---
layout: default
title: Trastuzumab Deruxtecan
parent: Low Evidence (L4-L5)
nav_order: 663
evidence_level: L5
indication_count: 1
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **1** 
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

# Trastuzumab Deruxtecan: Daripada Kanser Payudara/Gastrik Positif HER2 kepada Osteoporosis Teraruh Ubat

## Ringkasan Satu Ayat

Trastuzumab deruxtecan adalah konjugat antibodi-ubat (ADC) yang disasarkan HER2, di mana muatan sitotoksiknya digunakan untuk merawat kanser payudara dan gastrik positif HER2. Model TxGNN meramalkan kemungkinan hubungan dengan **osteoporosis teraruh ubat**, tetapi ramalan ini disokong oleh **0 ujian klinikal** dan **0 penerbitan**, dan pakej bukti ubat itu sendiri menandai arah mekanik sebagai berkemungkinan terbalik (iaitu, model mungkin mengesan perkaitan kesan sampingan yang diketahui dan bukannya hubungan terapeutik).

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Kanser payudara positif HER2 / kanser gastrik (mengikut profil ubat yang diketahui — teks petunjuk yang diluluskan TFDA tidak tersedia dalam set data ini) |
| Petunjuk Baharu yang Diramalkan | Osteoporosis teraruh ubat |
| Skor Ramalan TxGNN | 99.31% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci dari DrugBank tidak tersedia (jurang data DG002). Berdasarkan profil ubat yang diketahui, trastuzumab deruxtecan adalah ADC yang menggabungkan antibodi yang menyasarkan HER2 dengan muatan perencat topoisomerase I (DXd), dan penggunaan klinikalnya adalah kemoterapi sitotoksik untuk tumor pepejal positif HER2.

Mekanisme ini tidak menunjuk ke arah kesan perlindungan tulang. Sebaliknya, kemoterapi sitotoksik, menopaus/hipogonadisme teraruh kemoterapi, dan terapi sokongan yang berkaitan adalah **punca yang mapan** bagi **osteoporosis teraruh ubat** dalam amalan klinikal — bukan rawatannya. Skor TxGNN sebanyak 99.31% sangat tinggi, tetapi penilaian nisbah pakej bukti itu sendiri menilai ini sebagai kes yang berkemungkinan di mana graf pengetahuan mengelirukan kedekatannya dalam "ubat → kesan sampingan → penyakit" dengan hubungan tulin "ubat → merawat → penyakit". Dengan kata lain, arah kausaliti yang diramalkan mungkin terbalik.

Memandangkan perkara ini, ramalan harus diperlakukan sebagai tidak munasabah secara mekanik sehingga disokong oleh bukti bebas, dan bukannya sebagai calon ubat semula guna yang menjanjikan.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia

---

## Maklumat Pasaran Malaysia

Produk ini dipasarkan di Malaysia dengan 1 lesen berdaftar, tetapi nombor lesen, nama produk, bentuk dos, dan teks petunjuk yang diluluskan tidak diisi dalam set data semasa. Perincian ini perlu diambil terus dari pendaftaran NPRA sebelum penilaian lanjutan.

---

## Sitotoksisiti

Ubat ini layak sebagai sitostatik (ADC yang disasarkan HER2 dengan muatan perencat topoisomerase I sitotoksik konvensional, digunakan untuk kanser payudara/gastrik).

| Item | Kandungan |
|------|------|
| Klasifikasi Sitotoksisiti | Terapi yang disasarkan (konjugat antibodi-ubat) dengan muatan sitotoksik konvensional (perencat topoisomerase I) |
| Risiko Supresi Sum Tulang | Sila rujuk amaran dan langkah berhati-hati dalam sisipan paket |
| Klasifikasi Emetogenisiti | Sila rujuk amaran dan langkah berhati-hati dalam sisipan paket |
| Item Pemantauan | Sila rujuk amaran dan langkah berhati-hati dalam sisipan paket |
| Perlindungan Pengendalian | Sila rujuk amaran dan langkah berhati-hati dalam sisipan paket |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Nisbah:**
Ramalan ini tidak mempunyai sokongan ujian klinikal atau literatur (L5, model sahaja), dan nisbah ubat semula guna ubat itu sendiri menunjukkan arah mekanik berkemungkinan terbalik — mekanisme sitotoksik trastuzumab deruxtecan adalah penyebab yang munasabah bagi osteoporosis teraruh ubat, bukan rawatannya.

**Untuk meneruskan, perkara berikut diperlukan:**
- PDF label TFDA/NPRA dengan amaran dan kontraindikasi lengkap (menghalang jurang data DG001; diperlukan sebelum sebarang semakan keselamatan S1)
- Mekanisme tindakan yang disahkan melalui API DrugBank (DG002)
- Perincian lesen Malaysia yang lengkap (nombor lesen, nama produk, bentuk dos, teks petunjuk yang diluluskan)
- Semakan mekanik bebas untuk mengesahkan/menolak kausaliti terbalik sebelum sebarang pengumpulan bukti lanjut dimulakan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

