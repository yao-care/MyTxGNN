---
layout: default
title: Safety Data
nav_order: 5
has_children: true
description: "Drug safety information including DDI, DDSI, DFI, and DHI data."
---

# Safety Data

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Comprehensive drug safety information for drug repurposing research
</p>

---

## Overview

Drug safety is a critical consideration in drug repurposing research. This section provides access to various drug interaction and safety databases.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 2rem 0;">

<a href="{{ '/ddi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #E53935;">
  <h3 style="margin: 0 0 0.5rem 0; color: #E53935;">Drug-Drug Interactions</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">222,391 DDI records from DDInter 2.0</p>
</a>

<a href="{{ '/ddsi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #FF9800;">
  <h3 style="margin: 0 0 0.5rem 0; color: #FF9800;">Drug-Disease Safety</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Contraindications and precautions</p>
</a>

<a href="{{ '/dfi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #8BC34A;">
  <h3 style="margin: 0 0 0.5rem 0; color: #689F38;">Drug-Food Interactions</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Food effects on drug efficacy</p>
</a>

<a href="{{ '/dhi/' | relative_url }}" style="display: block; padding: 1.5rem; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-decoration: none; color: inherit; border-left: 4px solid #9C27B0;">
  <h3 style="margin: 0 0 0.5rem 0; color: #9C27B0;">Drug-Herb Interactions</h3>
  <p style="margin: 0; color: #666; font-size: 0.9rem;">Herbal medicine interactions</p>
</a>

</div>

---

## Why Safety Data Matters

When repurposing a drug for a new indication:

1. **Different patient populations** may have different comorbidities
2. **Standard treatments** for the new indication may interact with the repurposed drug
3. **Dietary habits** may vary between patient groups
4. **Supplement use** may be more common in certain conditions

---

## Data Sources

| Database | Records | Coverage |
|----------|---------|----------|
| DDInter 2.0 | 222,391 DDI | 2,310 drugs |
| Guide to PHARMACOLOGY | 4,636 interactions | 2,156 drugs |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Safety data is for research reference only. Clinical decisions should be made in consultation with healthcare professionals.
</div>
