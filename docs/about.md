---
layout: default
title: About
nav_order: 3
description: "MyTxGNN is a drug repurposing prediction platform based on Harvard's TxGNN model, focused on Malaysia NPRA-approved drugs."
permalink: /about/
---

# About This Project

<div class="key-takeaway">
Using AI to accelerate drug repurposing research for Malaysia's healthcare needs.
</div>

---

## Project Background

<p class="key-answer" data-question="What is MyTxGNN?">
<strong>MyTxGNN</strong> is a drug repurposing research platform based on Harvard University's TxGNN model published in <em>Nature Medicine</em>. It predicts potential new indications for drugs registered with Malaysia's National Pharmaceutical Regulatory Agency (NPRA), integrating evidence from ClinicalTrials.gov, PubMed, and other authoritative sources.
</p>

---

## Team & Attribution

| Item | Information |
|------|-------------|
| Project Maintained By | Yao.Care |
| Model Foundation | Harvard TxGNN (Zitnik Lab) |
| Data Source | NPRA Malaysia, data.gov.my |
| Last Updated | March 2026 |

### Academic Reference

This project's AI prediction model is based on:

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## What is Drug Repurposing?

<p class="key-answer" data-question="What is drug repurposing?">
<strong>Drug Repurposing</strong> (also known as drug repositioning) is the process of finding new therapeutic uses for existing drugs. Compared to developing new drugs from scratch, which takes 10-15 years and costs $1-2 billion, drug repurposing can be completed in 3-5 years at a fraction of the cost, with lower failure risk since safety data already exists.
</p>

<table class="comparison-table">
<thead>
<tr><th>Comparison</th><th>New Drug Development</th><th>Drug Repurposing</th></tr>
</thead>
<tbody>
<tr><td>Development Time</td><td>10-15 years</td><td>3-5 years</td></tr>
<tr><td>Development Cost</td><td>$1-2 billion</td><td>$100-300 million</td></tr>
<tr><td>Safety Data</td><td>Must establish new</td><td>Already available</td></tr>
<tr><td>Failure Risk</td><td>Very high (>90%)</td><td>Lower</td></tr>
</tbody>
</table>

<div class="key-takeaway">
The advantage of drug repurposing: safety, pharmacokinetics, and manufacturing have already been validated, allowing direct entry into clinical efficacy trials.
</div>

---

## What is TxGNN?

<p class="key-answer" data-question="What is TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> is a deep learning model developed by Harvard Medical School's Zitnik Lab, published in <em>Nature Medicine</em>. It predicts new drug-disease relationships and is the first foundation model designed specifically for clinician-centered drug repurposing.
</p>

<blockquote class="expert-quote">
"TxGNN integrates a knowledge graph of 17,080 biomedical entities, using graph neural networks to learn complex relationships between nodes, enabling prediction of drug efficacy for rare diseases."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### Technical Features

<ol class="actionable-steps">
<li><strong>Knowledge Graph</strong>: Integrates 17,080 nodes including drugs, diseases, genes, and proteins</li>
<li><strong>Graph Neural Network</strong>: Learns complex relationships between nodes</li>
<li><strong>Prediction Capability</strong>: Predicts which diseases a drug may be effective for</li>
</ol>

---

## Data Sources

<p class="key-answer" data-question="What are MyTxGNN's data sources?">
This platform integrates multiple public data sources including AI predictions, clinical trials, academic literature, drug information, Malaysia regulatory data, and drug interaction databases.
</p>

<table class="comparison-table">
<thead>
<tr><th>Data Type</th><th>Source</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>AI Prediction</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvard knowledge graph prediction model</td></tr>
<tr><td>Clinical Trials</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Global clinical trial registry</td></tr>
<tr><td>Literature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Biomedical literature database</td></tr>
<tr><td>Drug Information</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Drug and target database</td></tr>
<tr><td>Malaysia Regulatory</td><td><a href="https://npra.gov.my/">NPRA</a></td><td>National Pharmaceutical Regulatory Agency</td></tr>
<tr><td>Open Data</td><td><a href="https://data.gov.my/">data.gov.my</a></td><td>Malaysia Government Open Data</td></tr>
</tbody>
</table>

---

## Project Scale

| Item | Count |
|------|-------|
| NPRA Registered Products | 27,938 |
| Drugs with DrugBank Mapping | 508 |
| KG Predictions | 41,560 |
| DL High-Score Predictions | 176,021 |
| Unique Diseases | 17,041 |

---

## How to Cite

If using this platform's data, please cite:

### TxGNN Model

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## Contact & Feedback

For questions or suggestions, please contact us through:

- **GitHub Issues**: [https://github.com/yao-care/MyTxGNN/issues](https://github.com/yao-care/MyTxGNN/issues)
- **Project Homepage**: [https://mytxgnn.yao.care/](https://mytxgnn.yao.care/)

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for <strong>academic research purposes only</strong> and does not constitute medical advice. Drug use should follow physician guidance. Do not self-adjust medications. Any drug repurposing decisions require complete clinical validation and regulatory review.
<br><br>
<small>Last reviewed: 2026-03-03 | Reviewer: MyTxGNN Research Team</small>
</div>
