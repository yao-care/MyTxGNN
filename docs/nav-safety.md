---
layout: default
title: Data Keselamatan
nav_order: 5
has_children: true
description: "Data keselamatan ubat: interaksi ubat-ubat (DDI) daripada DDInter, serta data ubat–sasaran daripada Guide to PHARMACOLOGY."
permalink: /keselamatan/
---

# Data Keselamatan

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Pangkalan data keselamatan untuk penilaian penggunaan semula ubat
</p>

---

## Kategori Keselamatan

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/ddi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #E53935;">
  <h3 style="margin: 0 0 0.5rem 0; color: #C62828;">Interaksi Ubat-Ubat (DDI)</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">160,235 pasangan interaksi antara ubat konvensional</p>
  <small style="color: #999;">Sumber: DDInter (fail muat turun)</small>
</a>

</div>

---

## Mengapa Data Keselamatan Penting?

<div class="key-takeaway">
Apabila menggunakan semula ubat untuk indikasi baharu, kita perlu mempertimbangkan profil keselamatan dalam konteks populasi pesakit sasaran. Data keselamatan membantu mengenal pasti risiko berpotensi lebih awal.
</div>

### Pertimbangan Utama

| Aspek | Penerangan |
|-------|------------|
| **Poli-farmasi** | Pesakit sering mengambil pelbagai ubat |
| **Komorbiditi** | Penyakit sampingan mungkin mempengaruhi keselamatan |
| **Diet** | Makanan boleh mengubah keberkesanan ubat |
| **Ubat Tradisional** | Penggunaan herba tradisional perlu dipertimbangkan |

---

## Tahap Keterukan

| Tahap | Penerangan | Tindakan |
|-------|------------|----------|
| **Teruk (Major)** | Signifikan secara klinikal, berpotensi berbahaya | Elakkan, cari alternatif |
| **Sederhana (Moderate)** | Mungkin memerlukan pelarasan dos atau pemantauan | Guna dengan berhati-hati |
| **Ringan (Minor)** | Kepentingan klinikal rendah | Secara amnya selamat |

---

## Sumber Data

<table class="comparison-table">
<thead>
<tr><th>Sumber</th><th>Jenis Data</th><th>Rekod</th></tr>
</thead>
<tbody>
<tr>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter</a> (fail muat turun)</td>
  <td>DDI</td>
  <td>160,235</td>
</tr>
<tr>
  <td><a href="https://www.guidetopharmacology.org/" target="_blank" rel="noopener">Guide to PHARMACOLOGY</a> (GtoPdb 2026.3)</td>
  <td>Ubat–sasaran (bukan DDI)</td>
  <td>4,799</td>
</tr>
</tbody>
</table>

<p><small>Bilangan sama seperti halaman <a href="{{ '/ddi/' | relative_url }}">Interaksi Ubat-Ubat</a>: dikira daripada fail data MyTxGNN sendiri (Release data-20261031-141747, <code>data/external/ddi/</code>).</small></p>

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Data keselamatan adalah untuk <strong>rujukan penyelidikan sahaja</strong> dan bukan nasihat perubatan. Keputusan klinikal hendaklah berdasarkan penilaian profesional kesihatan.
<br><br>
<small>Kemas kini terakhir: 2026-11-04 | Pasukan Penyelidikan MyTxGNN</small>
</div>
