---
layout: default
title: Help
nav_order: 8
has_children: true
description: "Help and documentation for MyTxGNN platform."
---

# Help & Documentation

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Get help with using MyTxGNN
</p>

---

## Getting Started

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/guide/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #1976D2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #1976D2;">User Guide</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Learn how to use MyTxGNN for drug repurposing research</p>
</a>

<a href="{{ '/methodology/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #4CAF50;">
  <h3 style="margin: 0 0 0.5rem 0; color: #388E3C;">Methodology</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Understand our prediction and validation approach</p>
</a>

<a href="{{ '/blog/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #F57C00;">Tutorials</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Step-by-step guides and case studies</p>
</a>

<a href="{{ '/about/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">About</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Learn about the MyTxGNN project</p>
</a>

</div>

---

## Frequently Asked Questions

### How accurate are the predictions?

TxGNN has been validated against known drug-disease relationships with high accuracy. However, predictions should be validated through clinical evidence before application.

### Can I use this data commercially?

The data is provided for research purposes. Commercial use may be subject to individual data source licenses (DrugBank, etc.).

### How often is the data updated?

- NPRA data: Weekly
- Predictions: Periodically as models improve
- Evidence collection: On-demand

### Why are some drugs not included?

Only drugs that could be mapped to DrugBank IDs are included. Some local or combination products may not have DrugBank entries.

---

## Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/yao-care/MyTxGNN/issues)
- **Project Website**: [mytxgnn.yao.care](https://mytxgnn.yao.care)

---

## Legal

- [Privacy Policy]({{ '/privacy-policy/' | relative_url }})
- [Terms of Use]({{ '/downloads/' | relative_url }}#terms-of-use)
