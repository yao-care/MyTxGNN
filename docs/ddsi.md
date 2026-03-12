---
layout: default
title: Keselamatan Ubat-Penyakit
parent: Data Keselamatan
nav_order: 2
description: "Pangkalan data Maklumat Keselamatan Ubat-Penyakit MyTxGNN untuk menilai risiko keselamatan ubat dalam populasi pesakit tertentu."
permalink: /ddsi/
---

# Maklumat Keselamatan Ubat-Penyakit (DDSI)

<p class="key-answer" data-question="Apakah DDSI?">
<strong>Maklumat Keselamatan Ubat-Penyakit (DDSI)</strong> merujuk kepada amaran tentang ubat yang mungkin memburukkan keadaan atau menyebabkan reaksi buruk pada pesakit dengan penyakit tertentu. Ini membantu penyelidik mempertimbangkan komorbiditi pesakit apabila menilai calon penggunaan semula ubat.
</p>

<div class="key-takeaway">
Apabila menggunakan semula ubat, adalah penting untuk mempertimbangkan komorbiditi biasa populasi pesakit sasaran. Contohnya, apabila menggunakan ubat untuk pesakit kanser, pertimbangkan keabnormalan fungsi hati dan buah pinggang yang biasa mereka alami.
</div>

---

## Apakah DDSI?

Apabila ubat digunakan pada pesakit dengan penyakit tertentu, ia mungkin:

| Situasi | Penerangan | Contoh |
|---------|------------|--------|
| **Memburukkan Penyakit** | Ubat mungkin memburukkan keadaan sedia ada | NSAID memburukkan fungsi buah pinggang |
| **Keberkesanan Berubah** | Keadaan penyakit mempengaruhi metabolisme ubat | Sirosis mempengaruhi pelepasan ubat |
| **Peningkatan Toksisiti** | Penyakit menjadikan organ lebih mudah terjejas | Pesakit kegagalan jantung lebih sensitif kepada digoxin |
| **Penyembunyian Gejala** | Ubat mungkin menyembunyikan tanda penyakit | Penyekat beta menyembunyikan gejala hipoglisemia |

---

## Sumber Data

<table class="comparison-table">
<thead>
<tr><th>Item</th><th>Maklumat</th></tr>
</thead>
<tbody>
<tr>
  <td>Sumber Data</td>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
</tr>
<tr>
  <td>Rekod DDSI</td>
  <td>8,359</td>
</tr>
<tr>
  <td>Ubat Diliputi</td>
  <td>115</td>
</tr>
<tr>
  <td>Lesen</td>
  <td>CC BY-NC-SA 4.0</td>
</tr>
</tbody>
</table>

---

## Tahap Keterukan DDSI

| Tahap | Bahasa Inggeris | Penerangan | Tindakan Disyorkan |
|-------|-----------------|------------|-------------------|
| **Teruk** | Major | Kontraindikasi mutlak atau mengancam nyawa | Elakkan penggunaan, cari alternatif |
| **Sederhana** | Moderate | Mungkin memerlukan pelarasan dos atau pemantauan | Guna dengan berhati-hati, pantau rapi |
| **Ringan** | Minor | Kepentingan klinikal rendah | Secara amnya selamat, pantau jika perlu |

---

## Pertimbangan Ubat-Penyakit Biasa

### Penyakit Hati

<ol class="actionable-steps">
<li><strong>Ubat hepatotoksik dikontraindikasikan</strong>: Elakkan dalam kegagalan hati teruk</li>
<li><strong>Pelarasan dos diperlukan</strong>: Kurangkan dos untuk ubat yang dimetabolismekan oleh hati</li>
<li><strong>Kebimbangan pembekuan</strong>: Risiko meningkat dengan antikoagulan dalam sirosis</li>
</ol>

### Penyakit Buah Pinggang

- Laraskan dos untuk ubat yang dikumuhkan melalui buah pinggang
- Elakkan atau gunakan ubat nefrotoksik dengan berhati-hati
- Pantau perubahan elektrolit

### Penyakit Kardiovaskular

- Pesakit kegagalan jantung lebih sensitif kepada ubat tertentu
- Ubat berisiko pemanjangan QT perlu semakan sejarah aritmia
- Ubat berisiko hipotensi perlu penilaian status kardiovaskular

---

## Aplikasi dalam Penggunaan Semula Ubat

<blockquote class="expert-quote">
"Apabila menilai penggunaan semula ubat, kita mesti mempertimbangkan bukan sahaja sama ada ubat itu berkesan untuk indikasi baharu, tetapi juga ciri-ciri komorbiditi populasi pesakit sasaran untuk mengelakkan isu keselamatan."
<cite>— Prinsip Penilaian Keselamatan Ubat</cite>
</blockquote>

### Proses Penilaian

1. **Kenal Pasti Populasi Sasaran**: Fahami komorbiditi biasa
2. **Rujuk Silang Data DDSI**: Semak kontraindikasi
3. **Penilaian Risiko-Faedah**: Timbang keberkesanan terhadap risiko berpotensi
4. **Rancangan Pemantauan**: Reka pengawasan untuk kumpulan berisiko tinggi

---

## Sumber Berkaitan

| Sumber | Penerangan | Pautan |
|--------|------------|--------|
| Interaksi Ubat-Ubat | Pangkalan data DDI | [Pergi]({{ '/ddi/' | relative_url }}) |
| Interaksi Ubat-Makanan | Pangkalan data DFI | [Pergi]({{ '/dfi/' | relative_url }}) |
| Interaksi Ubat-Herba | Pangkalan data DHI | [Pergi]({{ '/dhi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Data DDSI di halaman ini adalah untuk rujukan penyelidikan sahaja dan <strong>bukan nasihat pengubatan</strong>. Keputusan pengubatan sebenar hendaklah berunding dengan farmasis atau doktor profesional. Kesan ubat terhadap penyakit tertentu berbeza mengikut faktor individu.
<br><br>
<small>Disemak terakhir: 2026-03-03 | Penyemak: Pasukan Penyelidikan MyTxGNN</small>
</div>
