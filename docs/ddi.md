---
layout: default
title: Interaksi Ubat-Ubat
parent: Data Keselamatan
nav_order: 1
description: "Pangkalan data interaksi ubat-ubat MyTxGNN untuk menilai keselamatan penggunaan semula ubat."
permalink: /ddi/
---

# Interaksi Ubat-Ubat (DDI)

<p class="key-answer" data-question="Apakah data DDI yang ada dalam MyTxGNN?">
Platform ini mengintegrasikan data interaksi ubat dari <strong>DDInter 2.0</strong> dan <strong>Guide to PHARMACOLOGY</strong> untuk membantu penyelidik mempertimbangkan faktor keselamatan apabila menilai calon penggunaan semula ubat.
</p>

<div class="key-takeaway">
Interaksi ubat adalah pertimbangan kritikal untuk penggunaan semula ubat. Apabila ubat digunakan untuk indikasi baharu, ia mungkin perlu digabungkan dengan rawatan standard untuk penyakit tersebut. Memahami risiko DDI berpotensi adalah penting.
</div>

---

## Sumber Data

<table class="comparison-table">
<thead>
<tr><th>Sumber Data</th><th>Rekod DDI</th><th>Ubat Diliputi</th><th>Kemas Kini</th></tr>
</thead>
<tbody>
<tr>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
  <td>222,391</td>
  <td>2,310</td>
  <td>2026-02</td>
</tr>
<tr>
  <td><a href="https://www.guidetopharmacology.org/" target="_blank" rel="noopener">Guide to PHARMACOLOGY</a></td>
  <td>4,636</td>
  <td>2,156</td>
  <td>2026-02 (v2025.4)</td>
</tr>
</tbody>
</table>

---

## Tahap Keterukan DDI

<p class="key-answer" data-question="Apakah tahap keterukan interaksi ubat?">
Interaksi ubat dikelaskan kepada tiga tahap berdasarkan keterukan, dari Teruk hingga Ringan, setiap satu dengan cadangan pengurusan klinikal yang berbeza.
</p>

| Tahap | Bahasa Inggeris | Penerangan | Tindakan Disyorkan |
|-------|-----------------|------------|-------------------|
| **Teruk** | Major | Mungkin mengancam nyawa atau menyebabkan kemudaratan kekal | Elakkan gabungan, cari alternatif |
| **Sederhana** | Moderate | Mungkin memerlukan pelarasan dos atau pemantauan rapi | Guna dengan berhati-hati, pantau kesan sampingan |
| **Ringan** | Minor | Kepentingan klinikal rendah | Secara amnya selamat untuk digabungkan, pantau jika perlu |

---

## Cara Menggunakan Data DDI

### Dalam Laporan Ubat

Setiap bahagian "Pertimbangan Keselamatan" laporan ubat termasuk maklumat interaksi ubat yang penting.

<ol class="actionable-steps">
<li>Pergi ke <a href="{{ '/drugs/' | relative_url }}">Senarai Ubat</a> dan cari ubat sasaran anda</li>
<li>Tatal ke bahagian "Pertimbangan Keselamatan" dalam laporan</li>
<li>Semak amaran DDI dan kontraindikasi ubat</li>
</ol>

### Muat Turun Set Data Penuh

Perlukan analisis berskala besar? Muat turun data DDI mentah dari GitHub:

| Data | Penerangan | Pautan |
|------|------------|--------|
| Data DDInter | Jadual rujukan DDI lengkap | [GitHub](https://github.com/yao-care/MyTxGNN/tree/main/data/external/ddi) |
| Data Pharmacology | Interaksi ubat yang diluluskan | [GitHub](https://github.com/yao-care/MyTxGNN/tree/main/data/external/ddi) |

---

## Mengapa DDI Penting untuk Penggunaan Semula Ubat

<blockquote class="expert-quote">
"Penyelidikan penggunaan semula ubat mesti menilai bukan sahaja keberkesanan tetapi juga interaksi ubat dalam konteks indikasi baharu. Banyak kegagalan penggunaan semula ubat berlaku tepat kerana interaksi dengan ubat rawatan standard diabaikan."
<cite>— Prinsip Penilaian Keselamatan Ubat</cite>
</blockquote>

### Pertimbangan DDI dalam Penggunaan Semula Ubat

1. **Ubat Rawatan Standard**: Indikasi baharu biasanya mempunyai rawatan standard sedia ada; nilai risiko gabungan
2. **Perbezaan Populasi Pesakit**: Penyakit berbeza mempunyai komorbiditi dan tabiat pengubatan berbeza
3. **Keperluan Pelarasan Dos**: Sesetengah DDI boleh diuruskan melalui pelarasan dos dan bukan pengelakan sepenuhnya

---

## Senario DDI Biasa

### Kortikosteroid (cth. Prednisolone)

| Interaksi | Kelas Ubat | Keterukan | Nota |
|-----------|------------|-----------|------|
| NSAID | Anti-radang | Sederhana | Risiko pendarahan GI meningkat |
| Warfarin | Antikoagulan | Sederhana | Mungkin mengubah INR |
| Diuretik | Kardiovaskular | Sederhana | Hipokalemia dipertingkatkan |

### Statin (cth. Simvastatin)

| Interaksi | Kelas Ubat | Keterukan | Nota |
|-----------|------------|-----------|------|
| Perencat CYP3A4 | Pelbagai | Teruk | Risiko miopati meningkat |
| Fibrat | Penurun lipid | Sederhana | Risiko miopati dipertingkatkan |
| Jus limau gedang | Makanan | Sederhana | Paras ubat meningkat |

---

## Sumber Berkaitan

| Sumber | Penerangan | Pautan |
|--------|------------|--------|
| Senarai Ubat | Lihat laporan ubat individu | [Pergi]({{ '/drugs/' | relative_url }}) |
| Metodologi | Memahami tahap bukti | [Pergi]({{ '/methodology/' | relative_url }}) |
| Sumber Data | Maklumat sumber data lengkap | [Pergi]({{ '/sources/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Data DDI di halaman ini adalah untuk rujukan penyelidikan sahaja dan <strong>bukan nasihat pengubatan</strong>. Keputusan pengubatan sebenar hendaklah berunding dengan farmasis atau doktor profesional. Kesan klinikal interaksi ubat berbeza mengikut faktor individu.
<br><br>
<small>Disemak terakhir: 2026-03-03 | Penyemak: Pasukan Penyelidikan MyTxGNN</small>
</div>
