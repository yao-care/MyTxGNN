---
layout: default
title: Data Keselamatan
nav_order: 5
has_children: true
description: "Data keselamatan ubat termasuk interaksi ubat-ubat, ubat-penyakit, ubat-makanan, dan ubat-herba."
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
  <p style="margin: 0; color: #666; font-size: 0.9rem;">200,000+ interaksi antara ubat konvensional</p>
  <small style="color: #999;">Sumber: DDInter 2.0</small>
</a>

<a href="{{ '/ddsi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FB8C00;">
  <h3 style="margin: 0 0 0.5rem 0; color: #EF6C00;">Keselamatan Ubat-Penyakit (DDSI)</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">8,359 amaran ubat pada pesakit dengan penyakit tertentu</p>
  <small style="color: #999;">Sumber: DDInter 2.0</small>
</a>

<a href="{{ '/dfi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #43A047;">
  <h3 style="margin: 0 0 0.5rem 0; color: #2E7D32;">Interaksi Ubat-Makanan (DFI)</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">857 interaksi dengan 29 jenis makanan biasa</p>
  <small style="color: #999;">Sumber: DDInter 2.0</small>
</a>

<a href="{{ '/dhi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #7B1FA2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #6A1B9A;">Interaksi Ubat-Herba (DHI)</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Interaksi dengan ubat tradisional dan herba</p>
  <small style="color: #999;">Sumber: DDInter 2.0 + Literatur</small>
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
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
  <td>DDI, DDSI, DFI</td>
  <td>200,000+</td>
</tr>
<tr>
  <td>Literatur</td>
  <td>DHI</td>
  <td>Pelbagai</td>
</tr>
</tbody>
</table>

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Data keselamatan adalah untuk <strong>rujukan penyelidikan sahaja</strong> dan bukan nasihat perubatan. Keputusan klinikal hendaklah berdasarkan penilaian profesional kesihatan.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
