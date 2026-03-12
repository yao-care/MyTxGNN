---
layout: default
title: Bantuan
nav_order: 7
has_children: true
description: "Bantuan dan dokumentasi untuk platform MyTxGNN."
permalink: /bantuan/
---

# Bantuan & Dokumentasi

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Dapatkan bantuan menggunakan MyTxGNN
</p>

---

## Mula Di Sini

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/guide/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #1976D2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #1976D2;">Panduan Pengguna</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Pelajari cara menggunakan MyTxGNN untuk penyelidikan penggunaan semula ubat</p>
</a>

<a href="{{ '/methodology/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #4CAF50;">
  <h3 style="margin: 0 0 0.5rem 0; color: #388E3C;">Metodologi</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Fahami pendekatan ramalan dan pengesahan kami</p>
</a>

<a href="{{ '/blog/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #F57C00;">Tutorial</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Panduan langkah demi langkah dan kajian kes</p>
</a>

<a href="{{ '/about/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">Tentang</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Ketahui tentang projek MyTxGNN</p>
</a>

</div>

---

## Soalan Lazim

### Seberapa tepat ramalan tersebut?

TxGNN telah disahkan terhadap hubungan ubat-penyakit yang diketahui dengan ketepatan tinggi. Walau bagaimanapun, ramalan perlu disahkan melalui bukti klinikal sebelum aplikasi.

### Bolehkah saya menggunakan data ini secara komersial?

Data disediakan untuk tujuan penyelidikan. Penggunaan komersial mungkin tertakluk kepada lesen sumber data individu (DrugBank, dll.).

### Berapa kerap data dikemas kini?

- Data NPRA: Mingguan
- Ramalan: Berkala apabila model diperbaiki
- Pengumpulan bukti: Atas permintaan

### Mengapa sesetengah ubat tidak disertakan?

Hanya ubat yang boleh dipetakan kepada ID DrugBank disertakan. Sesetengah produk tempatan atau kombinasi mungkin tidak mempunyai entri DrugBank.

---

## Tahap Bukti

| Tahap | Penerangan | Keperluan |
|-------|------------|-----------|
| **L1** | Bukti kuat | Fasa III ujian klinikal atau kelulusan FDA |
| **L2** | Bukti sederhana-kuat | Fasa II atau pelbagai kajian konsisten |
| **L3** | Bukti sederhana | Kajian awal atau laporan kes |
| **L4** | Bukti terhad | Ramalan KG sahaja |
| **L5** | Ramalan sahaja | Ramalan DL sahaja |

---

## Hubungi & Sokongan

- **GitHub Issues**: [Laporkan pepijat atau minta ciri](https://github.com/yao-care/MyTxGNN/issues)
- **Laman Web Projek**: [mytxgnn.yao.care](https://mytxgnn.yao.care)

---

## Perundangan

- [Dasar Privasi]({{ '/privacy-policy/' | relative_url }})
- [Syarat Penggunaan]({{ '/downloads/' | relative_url }}#syarat-penggunaan)

---

<div class="disclaimer">
<strong>Penafian</strong><br>
MyTxGNN adalah untuk <strong>tujuan penyelidikan sahaja</strong> dan bukan nasihat perubatan. Sentiasa dapatkan nasihat profesional kesihatan untuk keputusan rawatan.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
