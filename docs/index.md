---
layout: default
title: Drug Repurposing Predictions
nav_order: 1
description: "AI-powered drug repurposing predictions for Malaysia NPRA-approved drugs using TxGNN knowledge graph and deep learning models."
permalink: /
image: /assets/images/og-default.png
---

# Drug Repurposing: From Data to Evidence

<p class="key-answer" data-question="What is MyTxGNN?">
<strong>MyTxGNN</strong> is a drug repurposing prediction platform based on Harvard's TxGNN model. We predicted <strong>41,560</strong> potential new indications using knowledge graph methods, and <strong>176,021</strong> high-confidence predictions (score ≥ 0.7) using deep learning for <strong>508</strong> drugs approved by Malaysia's NPRA.
</p>

<div class="key-takeaway">
Leveraging AI to discover new therapeutic uses for existing medications. Our platform combines knowledge graphs with deep learning to identify promising drug-disease relationships for further clinical investigation.
</div>

<p style="margin-top: 1.5rem;">
  <a href="{{ '/drugs' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; margin-right: 0.5rem;">Browse Drugs</a>
  <a href="{{ '/methodology' | relative_url }}" style="display: inline-block; padding: 0.75rem 1.5rem; background: #f5f5f5; color: #333; text-decoration: none; border-radius: 4px; font-weight: 500;">Learn Methodology</a>
</p>

---

## Key Statistics

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #2E7D32;">508</div>
    <div style="color: #666;">Drugs Analyzed</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #1976D2;">41,560</div>
    <div style="color: #666;">KG Predictions</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #FB8C00;">176,021</div>
    <div style="color: #666;">High-Score DL Predictions</div>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
    <div style="font-size: 2.5rem; font-weight: 700; color: #9B59B6;">27,938</div>
    <div style="color: #666;">NPRA Registered Products</div>
  </div>
</div>

---

## Our Approach

<p class="key-answer" data-question="How does MyTxGNN work?">
MyTxGNN uses two complementary approaches for drug repurposing prediction: Knowledge Graph (KG) methods leverage existing drug-disease relationships, while Deep Learning (DL) models learn complex patterns from biomedical data.
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">Knowledge Graph Predictions</strong><br>
    <span style="color: #666;">Based on TxGNN's biomedical knowledge graph containing drug-disease relationships from DrugBank, clinical trials, and scientific literature. 41,560 predictions for 508 drugs.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Deep Learning Predictions</strong><br>
    <span style="color: #666;">TxGNN's neural network model provides confidence scores for each drug-disease pair. 176,021 predictions with score ≥ 0.7, indicating high confidence.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">Malaysia NPRA Integration</strong><br>
    <span style="color: #666;">Focused on drugs registered with Malaysia's National Pharmaceutical Regulatory Agency (NPRA), ensuring relevance to local healthcare needs.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">Evidence Collection</strong><br>
    <span style="color: #666;">Automated collection of supporting evidence from ClinicalTrials.gov, PubMed, and other authoritative sources to validate predictions.</span>
  </div>
</div>

---

## Top Predictions by Disease Category

| Disease Category | Predictions | Top Drug |
|------------------|-------------|----------|
| **Allergic Rhinitis** | 392 | Prednisolone, Betamethasone |
| **Hypertension** | 366 | Multiple antihypertensives |
| **Rheumatoid Arthritis** | 316 | Corticosteroids |
| **Seborrheic Dermatitis** | 288 | Ketoconazole, Fusidic Acid |
| **Asthma** | 259 | Bronchodilators, Steroids |

---

## Quick Navigation

| Section | Description | Link |
|---------|-------------|------|
| **Drug List** | Browse all 508 analyzed drugs | [View Drugs]({{ '/drugs' | relative_url }}) |
| **Methodology** | Learn about our prediction approach | [Read More]({{ '/methodology' | relative_url }}) |
| **Data Sources** | Explore our data sources | [View Sources]({{ '/DATA_SOURCES' | relative_url }}) |
| **About** | Learn about this project | [About Us]({{ '/about' | relative_url }}) |
| **Downloads** | Get prediction data | [Download]({{ '/downloads' | relative_url }}) |
| **FHIR API** | Access via FHIR R4 | [API Docs]({{ '/fhir/metadata' | relative_url }}) |

---

## About This Project

<p class="key-answer" data-question="What technology does MyTxGNN use?">
This platform uses the <a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> deep learning model published in <em>Nature Medicine</em> by Harvard University's Zitnik Lab to predict potential new indications for Malaysia NPRA-approved drugs.
</p>

<blockquote class="expert-quote">
"TxGNN is the first foundation model for drug repurposing designed specifically for clinicians, integrating knowledge graphs with deep learning to predict drug efficacy for rare diseases."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### Data Scale

| Item | Count |
|------|-------|
| NPRA Registered Products | 27,938 |
| Drugs with DrugBank Mapping | 508 |
| KG Predictions | 41,560 |
| DL High-Score Predictions | 176,021 |
| Unique Diseases | 17,041 |

[Learn More]({{ '/about' | relative_url }}) | [Methodology]({{ '/methodology' | relative_url }}) | [Data Sources]({{ '/DATA_SOURCES' | relative_url }})

---

## Data Sources

<p class="key-answer" data-question="What are the data sources for MyTxGNN?">
This platform integrates multiple authoritative public data sources to ensure prediction traceability and academic value.
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
    <small>NIH Clinical Trials</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #326599;">PubMed</strong>
    <small>Biomedical Literature</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Drug Database</small>
  </a>
  <a href="https://npra.gov.my/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #00A651;">NPRA Malaysia</strong>
    <small>National Pharma Agency</small>
  </a>
  <a href="https://data.gov.my/" target="_blank" rel="noopener" class="data-source-card">
    <strong style="color: #1976D2;">data.gov.my</strong>
    <small>Open Data Portal</small>
  </a>
</div>

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for <strong>academic research purposes only</strong> and does not constitute medical advice. Drug use should follow physician guidance. Do not self-adjust medications. Any drug repurposing decisions require complete clinical validation and regulatory review.
<br><br>
<small>Last updated: 2026-03-03 | MyTxGNN Research Team</small>
</div>
