---
layout: default
title: Tentang Projek
parent: Bantuan
nav_order: 3
description: "MyTxGNN ialah platform ramalan penggunaan semula ubat berdasarkan model TxGNN Harvard, memberi tumpuan kepada ubat-ubatan yang diluluskan NPRA Malaysia."
permalink: /about/
---

# Tentang Projek Ini

<div class="key-takeaway">
Menggunakan AI untuk mempercepat penyelidikan penggunaan semula ubat bagi keperluan penjagaan kesihatan Malaysia.
</div>

---

## Tentang Pembangun

Platform ini dibangunkan dan dikendalikan oleh **藥提醒科技有限公司** (yao.care, nombor pendaftaran
syarikat 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

MyTxGNN ialah laman Malaysia bagi barisan produk "TxGNN Drug Repurposing" syarikat tersebut.
Sistem yang sama digunakan di 30 negara dan wilayah, masing-masing dinamakan `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, dan seterusnya) di `{cc}txgnn.yao.care`.
Gambaran keseluruhan produk: <https://www.yao.care/medical/txgnn/>.

Model TxGNN itu sendiri dibangunkan oleh Zitnik Lab di Harvard Medical School dan diterbitkan
dalam *Nature Medicine*. Platform ini ialah sistem pengeluaran yang dibina oleh 藥提醒科技有限公司
berasaskan model tersebut, merangkumi integrasi data pendaftaran ubat kebangsaan, ramalan pembelajaran mendalam yang mengecualikan kegunaan yang sudah direkodkan dalam graf pengetahuan, penggredan bukti PubMed /
ClinicalTrials, serta integrasi rekod kesihatan elektronik SMART on FHIR.

---

## Latar Belakang Projek

<p class="key-answer" data-question="Apakah MyTxGNN?">
<strong>MyTxGNN</strong> ialah platform penyelidikan penggunaan semula ubat berdasarkan model TxGNN Harvard University yang diterbitkan dalam <em>Nature Medicine</em>. Ia meramal kemungkinan indikasi baharu bagi ubat yang didaftarkan dengan Agensi Pengawalan Farmaseutikal Kebangsaan Malaysia (NPRA), menggabungkan bukti daripada ClinicalTrials.gov, PubMed dan sumber berautoriti lain.
</p>

---

## Pasukan & Atribusi

| Item | Maklumat |
|------|-------------|
| Diselenggara Oleh | 藥提醒科技有限公司 (yao.care) |
| Asas Model | Harvard TxGNN (Zitnik Lab) |
| Sumber Data | NPRA Malaysia, data.gov.my |
| Kemas Kini Terakhir | Mac 2026 |

### Rujukan Akademik

Model ramalan AI projek ini berdasarkan:

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Apakah Penggunaan Semula Ubat?

<p class="key-answer" data-question="Apakah penggunaan semula ubat?">
<strong>Penggunaan Semula Ubat</strong> (juga dikenali sebagai drug repositioning) ialah proses mencari kegunaan terapeutik baharu bagi ubat sedia ada. Berbanding membangunkan ubat baharu dari awal yang mengambil masa 10-15 tahun dan kos USD 1-2 bilion, penggunaan semula ubat boleh disiapkan dalam 3-5 tahun dengan kos jauh lebih rendah, dan risiko kegagalan lebih rendah kerana data keselamatan sudah wujud.
</p>

<table class="comparison-table">
<thead>
<tr><th>Perbandingan</th><th>Pembangunan Ubat Baharu</th><th>Penggunaan Semula Ubat</th></tr>
</thead>
<tbody>
<tr><td>Tempoh Pembangunan</td><td>10-15 tahun</td><td>3-5 tahun</td></tr>
<tr><td>Kos Pembangunan</td><td>USD 1-2 bilion</td><td>USD 100-300 juta</td></tr>
<tr><td>Data Keselamatan</td><td>Perlu diwujudkan baharu</td><td>Sudah tersedia</td></tr>
<tr><td>Risiko Kegagalan</td><td>Sangat tinggi (>90%)</td><td>Lebih rendah</td></tr>
</tbody>
</table>

<div class="key-takeaway">
Kelebihan penggunaan semula ubat: keselamatan, farmakokinetik dan pembuatan sudah disahkan, membolehkan terus memasuki ujian klinikal keberkesanan.
</div>

---

## Apakah TxGNN?

<p class="key-answer" data-question="Apakah TxGNN?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> ialah model pembelajaran mendalam yang dibangunkan oleh Zitnik Lab, Harvard Medical School, diterbitkan dalam <em>Nature Medicine</em>. Ia meramal perkaitan ubat-penyakit baharu dan merupakan model asas pertama yang direka khusus untuk penggunaan semula ubat berpaksikan klinikal.
</p>

<blockquote class="expert-quote">
"TxGNN menggabungkan graf pengetahuan merangkumi 17,080 penyakit, menggunakan rangkaian neural graf untuk mempelajari perkaitan kompleks antara nod, membolehkan ramalan keberkesanan ubat untuk penyakit jarang."
<cite>— Huang et al., Nature Medicine (2024)</cite>
</blockquote>

### Ciri Teknikal

<ol class="actionable-steps">
<li><strong>Graf Pengetahuan</strong>: Graf pengetahuan bioperubatan merangkumi 17,080 penyakit, ditambah ubat, gen dan protein</li>
<li><strong>Rangkaian Neural Graf</strong>: Mempelajari perkaitan kompleks antara nod</li>
<li><strong>Keupayaan Ramalan</strong>: Meramal penyakit yang mungkin dirawat secara berkesan oleh sesuatu ubat</li>
</ol>

---

## Sumber Data

<p class="key-answer" data-question="Apakah sumber data MyTxGNN?">
Platform ini menggabungkan pelbagai sumber data awam termasuk ramalan AI, ujian klinikal, literatur akademik, maklumat ubat, data kawal selia Malaysia dan pangkalan data interaksi ubat.
</p>

<table class="comparison-table">
<thead>
<tr><th>Jenis Data</th><th>Sumber</th><th>Penerangan</th></tr>
</thead>
<tbody>
<tr><td>Ramalan AI</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Rangkaian neural graf Harvard yang dilatih pada graf pengetahuan</td></tr>
<tr><td>Ujian Klinikal</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Pendaftaran ujian klinikal global</td></tr>
<tr><td>Literatur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Pangkalan data literatur bioperubatan</td></tr>
<tr><td>Maklumat Ubat</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Pangkalan data ubat dan sasaran</td></tr>
<tr><td>Kawal Selia Malaysia</td><td><a href="https://npra.gov.my/">NPRA</a></td><td>Agensi Pengawalan Farmaseutikal Kebangsaan</td></tr>
<tr><td>Data Terbuka</td><td><a href="https://data.gov.my/">data.gov.my</a></td><td>Data Terbuka Kerajaan Malaysia</td></tr>
</tbody>
</table>

---

## Skala Projek

| Item | Jumlah |
|------|-------|
| Produk Berdaftar NPRA | 27,938 |
| Ubat dengan Pemetaan DrugBank | 508 |
| Indikasi Baharu Diramal (kegunaan sedia ada dikecualikan) | {{ site.data.site_stats.indications }} |
| Penyakit Unik | 17,041 |

---

## Cara Memetik

Jika menggunakan data platform ini, sila petik:

### Model TxGNN

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

---

## Hubungi & Maklum Balas

Untuk soalan atau cadangan, sila hubungi kami melalui:

- **GitHub Issues**: [https://github.com/yao-care/MyTxGNN/issues](https://github.com/yao-care/MyTxGNN/issues)
- **Laman Utama Projek**: [https://mytxgnn.yao.care/](https://mytxgnn.yao.care/)

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Laporan ini adalah untuk <strong>tujuan penyelidikan akademik sahaja</strong> dan tidak membentuk nasihat perubatan. Penggunaan ubat perlu mengikut panduan doktor; jangan melaraskan ubat sendiri. Sebarang keputusan penggunaan semula ubat memerlukan pengesahan klinikal dan semakan kawal selia yang lengkap.
<br><br>
<small>Semakan terakhir: 2026-03-03 | Penyemak: 藥提醒科技有限公司 (yao.care)</small>
</div>
