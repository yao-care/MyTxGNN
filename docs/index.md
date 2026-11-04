---
layout: default
title: Laporan Pengesahan Penggunaan Semula Ubat
nav_order: 1
description: "Ramalan penggunaan semula ubat berkuasa AI untuk ubat yang diluluskan NPRA Malaysia menggunakan model TxGNN (pembelajaran mendalam)."
last_modified_at: 2026-11-04
permalink: /
image: /assets/images/og-default.png
---

# Penggunaan Semula Ubat: Dari Data ke Bukti

<p class="key-answer" data-question="Apakah MyTxGNN?">
<strong>MyTxGNN</strong> adalah platform ramalan penggunaan semula ubat berdasarkan model TxGNN Harvard. Kami menyenaraikan <strong>{{ site.data.site_stats.indications }}</strong> indikasi baharu yang diramalkan oleh model pembelajaran mendalam (skor ≥ 0.99, selepas kegunaan sedia ada dalam graf pengetahuan dikecualikan) untuk <strong>{{ site.data.site_stats.drugs }}</strong> ubat yang diluluskan NPRA Malaysia.
</p>

<div class="key-takeaway">
Memanfaatkan AI untuk menemui penggunaan terapeutik baharu bagi ubat sedia ada. Platform kami menggunakan model TxGNN (pembelajaran mendalam: rangkaian neural graf yang dilatih pada graf pengetahuan bioperubatan) untuk mengenal pasti hubungan ubat-penyakit yang menjanjikan untuk penyiasatan klinikal lanjut.
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/drugs' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">Layari Ubat</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">Pelajari Metodologi</a>
</p>

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Malaysia: liputan laman ini

Laman ini menerbitkan laporan bagi **{{ site.data.drug_stats.total_drugs }}** ubat dalam data pendaftaran [NPRA](https://npra.gov.my/) (Malaysia).

Set data: [data.gov.my: Pharmaceutical Products (NPRA)](https://data.gov.my/data-catalogue/pharmaceutical_products); dimuat turun dan dibandingkan secara automatik setiap minggu (hari Isnin). Butiran: [Data Sources]({{ '/sources/' | relative_url }}).

Laporan mengikut tahap bukti:

| Tahap bukti | Laporan | Peratusan |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

6 pasangan ubat–penyakit yang diramal di laman ini tidak terdapat di mana-mana laman lain antara 30 laman TxGNN.

### Ubat dengan tahap bukti tertinggi di laman ini

| Ubat | Tahap bukti |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Fludarabine](/drugs/fludarabine/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |

### Ubat yang hanya diliputi oleh laman ini antara 30 laman TxGNN

| Ubat | Tahap bukti |
|---|---|
| [Estradiol Benzoate](/drugs/estradiol-benzoate/) | L4 |
| [Sulodexide](/drugs/sulodexide/) | L5 |
| [Gliclazide](/drugs/gliclazide/) | N/A |

<!-- local-home:end -->

## Statistik Utama

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #2E7D32;">{{ site.data.site_stats.drugs }}</div>
    <div style="color: #666;">Ubat Dianalisis</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #1976D2;">{{ site.data.site_stats.indications }}</div>
    <div style="color: #666;">Indikasi Baharu Diramal</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #9B59B6;">27,938</div>
    <div style="color: #666;">Produk Berdaftar NPRA</div>
  </div>
</div>

---

## Pendekatan Kami

<p class="key-answer" data-question="Bagaimana MyTxGNN berfungsi?">
MyTxGNN menggunakan model Pembelajaran Mendalam (DL) TxGNN untuk meramal indikasi baharu. Indikasi dan kegunaan luar label yang sudah direkodkan dalam Graf Pengetahuan (KG) dikecualikan, supaya hanya ramalan baharu dipaparkan.
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">Semakan Kegunaan Sedia Ada (KG)</strong><br>
    <span style="color: #666;">Indikasi dan kegunaan luar label yang sudah direkodkan dalam graf pengetahuan TxGNN digunakan untuk mengecualikan kegunaan yang telah diketahui. Ia bukan ramalan baharu.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Ramalan Pembelajaran Mendalam</strong><br>
    <span style="color: #666;">Model TxGNN (pembelajaran mendalam) memberikan skor kepada setiap pasangan ubat-penyakit. Laman ini hanya menyenaraikan {{ site.data.site_stats.indications }} ramalan dengan skor ≥ 0.99 (maksimum 10 bagi setiap ubat) selepas kegunaan sedia ada dikecualikan. Skor ialah kedudukan dalaman model, bukan kebarangkalian.</span>
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
| **Senarai Ubat** | Layari semua {{ site.data.site_stats.drugs }} ubat yang dianalisis | [Lihat Ubat]({{ '/drugs' | relative_url }}) |
| **Metodologi** | Pelajari pendekatan ramalan kami | [Baca Lagi]({{ '/methodology' | relative_url }}) |
| **Sumber Data** | Terokai sumber data kami | [Lihat Sumber]({{ '/sources' | relative_url }}) |
| **Tentang** | Ketahui tentang projek ini | [Tentang Kami]({{ '/about' | relative_url }}) |
| **Muat Turun** | Dapatkan data ramalan | [Muat Turun]({{ '/downloads' | relative_url }}) |
| **FHIR API** | Akses melalui FHIR R4 | [Dokumentasi API]({{ '/fhir/metadata' | relative_url }}) |

---

## Tentang Projek Ini

<p class="key-answer" data-question="Apakah teknologi yang digunakan MyTxGNN?">
Platform ini menggunakan model pembelajaran mendalam <a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> yang diterbitkan dalam <em>Nature Medicine</em> oleh Makmal Zitnik Universiti Harvard untuk meramalkan indikasi baharu berpotensi bagi ubat yang diluluskan NPRA Malaysia.
</p>

<blockquote class="expert-quote">
"TxGNN adalah model asas pertama untuk penggunaan semula ubat yang direka khusus untuk doktor, mengintegrasikan graf pengetahuan dengan pembelajaran mendalam untuk meramalkan keberkesanan ubat bagi penyakit jarang."
<cite>— Huang et al., Nature Medicine (2024)</cite>
</blockquote>

### Skala Data

| Item | Jumlah |
|------|--------|
| Produk Berdaftar NPRA | 27,938 |
| Ubat dengan Pemetaan DrugBank | 1,061 |
| Indikasi Baharu Diramal | {{ site.data.site_stats.indications }} |
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
<small>Kemas kini terakhir: {{ page.last_modified_at | date: "%Y-%m-%d" }} | Pasukan Penyelidikan MyTxGNN</small>
</div>

---

## Tentang Pembangun

Platform ini dibangunkan dan dikendalikan oleh **藥提醒科技有限公司** (yao.care). Lihat halaman <a href="{{ '/about/' | relative_url }}">Tentang Projek</a> untuk latar belakang penuh syarikat dan metodologi.
