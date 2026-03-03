---
layout: default
title: Resources
nav_order: 6
has_children: true
description: "MyTxGNN resources including data sources, downloads, and case studies."
---

# Resources

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Access data, documentation, and learning materials
</p>

---

## Available Resources

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/sources/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #1976D2;">
  <h3 style="margin: 0 0 0.5rem 0; color: #1976D2;">Data Sources</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Information about TxGNN, NPRA, DrugBank, and other data sources</p>
</a>

<a href="{{ '/downloads/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #4CAF50;">
  <h3 style="margin: 0 0 0.5rem 0; color: #388E3C;">Downloads</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Download prediction data in CSV format</p>
</a>

<a href="{{ '/blog/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #F57C00;">Case Studies</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Tutorials and example analyses</p>
</a>

<a href="{{ '/guide/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #7B1FA2;">User Guide</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">How to use MyTxGNN effectively</p>
</a>

</div>

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [FHIR API](/fhir/metadata) | Access drug data via FHIR R4 |
| [GitHub Repository](https://github.com/yao-care/MyTxGNN) | Source code and data files |
| [CDS Hooks Demo](/cds-hooks/demo.html) | Clinical decision support demo |

---

## Citation

When using MyTxGNN data in your research, please cite:

```bibtex
@misc{mytxgnn2026,
  title={MyTxGNN: Malaysia Drug Repurposing Prediction Platform},
  url={https://mytxgnn.yao.care},
  year={2026}
}

@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```
