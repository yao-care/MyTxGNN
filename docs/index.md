---
layout: default
title: Laporan Pengesahan Penggunaan Semula Ubat
nav_order: 1
description: "Ramalan penggunaan semula ubat berkuasa AI untuk ubat yang diluluskan NPRA Malaysia menggunakan graf pengetahuan TxGNN dan model pembelajaran mendalam."
permalink: /
image: /assets/images/og-default.png
---

# Penggunaan Semula Ubat: Dari Data ke Bukti

<p class="key-answer" data-question="Apakah MyTxGNN?">
<strong>MyTxGNN</strong> adalah platform ramalan penggunaan semula ubat berdasarkan model TxGNN Harvard. Kami meramalkan <strong>41,560</strong> indikasi baharu berpotensi menggunakan kaedah graf pengetahuan, dan <strong>176,021</strong> ramalan keyakinan tinggi (skor ≥ 0.7) menggunakan pembelajaran mendalam untuk <strong>508</strong> ubat yang diluluskan NPRA Malaysia.
</p>

<div class="key-takeaway">
Memanfaatkan AI untuk menemui penggunaan terapeutik baharu bagi ubat sedia ada. Platform kami menggabungkan graf pengetahuan dengan pembelajaran mendalam untuk mengenal pasti hubungan ubat-penyakit yang menjanjikan untuk penyiasatan klinikal lanjut.
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/drugs' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">Layari Ubat</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">Pelajari Metodologi</a>
</p>

---

## Statistik Utama

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #2E7D32;">508</div>
    <div style="color: #666;">Ubat Dianalisis</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #1976D2;">41,560</div>
    <div style="color: #666;">Ramalan KG</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #FB8C00;">176,021</div>
    <div style="color: #666;">Ramalan DL Skor Tinggi</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #9B59B6;">27,938</div>
    <div style="color: #666;">Produk Berdaftar NPRA</div>
  </div>
</div>

---

## Pendekatan Kami

<p class="key-answer" data-question="Bagaimana MyTxGNN berfungsi?">
MyTxGNN menggunakan dua pendekatan pelengkap untuk ramalan penggunaan semula ubat: Kaedah Graf Pengetahuan (KG) memanfaatkan hubungan ubat-penyakit sedia ada, manakala model Pembelajaran Mendalam (DL) mempelajari corak kompleks daripada data bioperubatan.
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">Ramalan Graf Pengetahuan</strong><br>
    <span style="color: #666;">Berdasarkan graf pengetahuan bioperubatan TxGNN yang mengandungi hubungan ubat-penyakit dari DrugBank, ujian klinikal, dan literatur saintifik. 41,560 ramalan untuk 508 ubat.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Ramalan Pembelajaran Mendalam</strong><br>
    <span style="color: #666;">Model rangkaian neural TxGNN memberikan skor keyakinan untuk setiap pasangan ubat-penyakit. 176,021 ramalan dengan skor ≥ 0.7, menunjukkan keyakinan tinggi.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">Integrasi NPRA Malaysia</strong><br>
    <span style="color: #666;">Memfokuskan pada ubat yang berdaftar dengan Agensi Regulatori Farmaseutikal Kebangsaan Malaysia (NPRA), memastikan kesesuaian dengan keperluan penjagaan kesihatan tempatan.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">Pengumpulan Bukti</strong><br>
    <span style="color: #666;">Pengumpulan automatik bukti sokongan dari ClinicalTrials.gov, PubMed, dan sumber berautoriti lain untuk mengesahkan ramalan.</span>
  </div>
</div>

---

## Ramalan Teratas mengikut Kategori Penyakit

| Kategori Penyakit | Ramalan | Ubat Teratas |
|-------------------|---------|--------------|
| **Rinitis Alahan** | 392 | Prednisolone, Betamethasone |
| **Hipertensi** | 366 | Pelbagai antihipertensi |
| **Artritis Reumatoid** | 316 | Kortikosteroid |
| **Dermatitis Seborreik** | 288 | Ketoconazole, Fusidic Acid |
| **Asma** | 259 | Bronkodilator, Steroid |

---

## Navigasi Pantas

| Bahagian | Penerangan | Pautan |
|----------|------------|--------|
| **Senarai Ubat** | Layari semua 508 ubat yang dianalisis | [Lihat Ubat]({{ '/drugs' | relative_url }}) |
| **Metodologi** | Pelajari pendekatan ramalan kami | [Baca Lagi]({{ '/methodology' | relative_url }}) |
| **Sumber Data** | Terokai sumber data kami | [Lihat Sumber]({{ '/sources' | relative_url }}) |
| **Tentang** | Ketahui tentang projek ini | [Tentang Kami]({{ '/about' | relative_url }}) |
| **Muat Turun** | Dapatkan data ramalan | [Muat Turun]({{ '/downloads' | relative_url }}) |
| **FHIR API** | Akses melalui FHIR R4 | [Dokumentasi API]({{ '/fhir/metadata' | relative_url }}) |

---

## Tentang Projek Ini

<p class="key-answer" data-question="Apakah teknologi yang digunakan MyTxGNN?">
Platform ini menggunakan model pembelajaran mendalam <a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> yang diterbitkan dalam <em>Nature Medicine</em> oleh Makmal Zitnik Universiti Harvard untuk meramalkan indikasi baharu berpotensi bagi ubat yang diluluskan NPRA Malaysia.
</p>

<blockquote class="expert-quote">
"TxGNN adalah model asas pertama untuk penggunaan semula ubat yang direka khusus untuk doktor, mengintegrasikan graf pengetahuan dengan pembelajaran mendalam untuk meramalkan keberkesanan ubat bagi penyakit jarang."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### Skala Data

| Item | Jumlah |
|------|--------|
| Produk Berdaftar NPRA | 27,938 |
| Ubat dengan Pemetaan DrugBank | 508 |
| Ramalan KG | 41,560 |
| Ramalan DL Skor Tinggi | 176,021 |
| Penyakit Unik | 17,041 |

[Ketahui Lebih Lanjut]({{ '/about' | relative_url }}) | [Metodologi]({{ '/methodology' | relative_url }}) | [Sumber Data]({{ '/sources' | relative_url }})

---

## Sumber Data

<p class="key-answer" data-question="Apakah sumber data MyTxGNN?">
Platform ini mengintegrasikan pelbagai sumber data awam berautoriti untuk memastikan kebolehkesanan ramalan dan nilai akademik.
</p>

<style>
.data-source-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 12px;
}
.data-source-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.25rem 1rem;
  background: white;
  border-radius: 10px;
  text-decoration: none;
  color: #333;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s, box-shadow 0.2s;
}
.data-source-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>Ujian Klinikal NIH</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #326599;">PubMed</strong>
    <small>Literatur Bioperubatan</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Pangkalan Data Ubat</small>
  </a>
  <a href="https://npra.gov.my/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #00A651;">NPRA Malaysia</strong>
    <small>Agensi Farmaseutikal Kebangsaan</small>
  </a>
  <a href="https://data.gov.my/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #1976D2;">data.gov.my</strong>
    <small>Portal Data Terbuka</small>
  </a>
</div>

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Laporan ini adalah untuk <strong>tujuan penyelidikan akademik sahaja</strong> dan bukan nasihat perubatan. Penggunaan ubat hendaklah mengikut panduan doktor. Jangan mengubah ubatan sendiri. Sebarang keputusan penggunaan semula ubat memerlukan pengesahan klinikal lengkap dan semakan regulatori.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
