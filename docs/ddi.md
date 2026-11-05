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
Platform ini mengintegrasikan data interaksi ubat-ubat dari <strong>DDInter</strong> (fail muat turun <code>ddinter_code_*.csv</code>), serta data ubat–sasaran daripada <strong>Guide to PHARMACOLOGY</strong> (GtoPdb 2026.3.1, bukan data interaksi), untuk membantu penyelidik mempertimbangkan faktor keselamatan apabila menilai calon penggunaan semula ubat.
</p>

<div class="key-takeaway">
Interaksi ubat adalah pertimbangan kritikal untuk penggunaan semula ubat. Apabila ubat digunakan untuk indikasi baharu, ia mungkin perlu digabungkan dengan rawatan standard untuk penyakit tersebut. Memahami risiko DDI berpotensi adalah penting.
</div>

---

## Sumber Data

<table class="comparison-table">
<thead>
<tr><th>Sumber Data</th><th>Rekod</th><th>Ubat Diliputi</th><th>Kemas Kini</th></tr>
</thead>
<tbody>
<tr>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter</a> (fail muat turun)</td>
  <td>160,235</td>
  <td>1,939</td>
  <td>2026-02</td>
</tr>
<tr>
  <td><a href="https://www.guidetopharmacology.org/" target="_blank" rel="noopener">Guide to PHARMACOLOGY</a> (data ubat–sasaran ubat yang diluluskan, bukan DDI)</td>
  <td>4,808</td>
  <td>2,253</td>
  <td>2026-10 (v2026.3.1)</td>
</tr>
</tbody>
</table>

<p><small>Bilangan dikira daripada fail data MyTxGNN sendiri (Release data-20261105-123615, <code>data/external/ddi/</code>). DDInter: pasangan ubat unik selepas membuang pendua merentas fail kod ATC (222,383 baris). Rekod DDI hanya daripada DDInter (160,235 pasangan). Guide to PHARMACOLOGY (GtoPdb 2026.3.1): 4,808 baris data ubat–sasaran, bukan interaksi ubat-ubat, dan bilangan ligan unik.</small></p>

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

---

## Mengapa DDI Penting untuk Penggunaan Semula Ubat

<p>Penyelidikan penggunaan semula ubat mesti menilai bukan sahaja keberkesanan tetapi juga interaksi ubat dalam konteks indikasi baharu. Pesakit indikasi baharu sering juga mengambil ubat rawatan standard penyakit itu, jadi risiko interaksi perlu dinilai bersama.</p>

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
