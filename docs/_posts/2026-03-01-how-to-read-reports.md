---
layout: default
title: "Tutorial: How to Read MyTxGNN Reports"
description: "Step-by-step guide on how to read and understand drug repurposing validation reports, including evidence levels and decision recommendations."
date: 2026-03-01
categories: [Tutorial]
tags: [User Guide, Getting Started]
---

# How to Read Validation Reports

<p class="key-answer" data-question="What are the most important pieces of information in a report?">
Each report has three key pieces of information: <strong>Evidence Level</strong> (L1-L5), <strong>Prediction Score</strong> (AI confidence), and <strong>Decision Recommendation</strong> (Go/Proceed/Hold). These three combined quickly tell you the prediction's reliability and recommended action.
</p>

---

## Report Structure Overview

### 1. One-Sentence Summary

The one-sentence summary at the beginning is the most important quick-read section:

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 1rem; border-radius: 8px; border-left: 4px solid #2E7D32; margin: 1rem 0;">
<strong>Example:</strong> Prednisolone is originally used for inflammatory conditions. TxGNN predicts it may be effective for 3,650 additional indications, with clinical trial evidence supporting some predictions.
</div>

This tells you:
- The drug's original use
- The AI's predicted new use
- How much evidence supports it

### 2. Quick Overview Table

| Item | How to Interpret |
|------|------------------|
| TxGNN Prediction Score | 99%+ indicates very high AI confidence |
| Evidence Level | L1 is strongest, L5 is prediction only |
| Decision Recommendation | Go = proceed directly, Hold = wait |
| NPRA Status | Whether approved in Malaysia |

### 3. Clinical Trial Evidence

Clinical trials are the most important evidence source:

| Phase | Description | Evidence Strength |
|-------|-------------|-------------------|
| **Phase 3** | Large-scale confirmatory trials | Strongest |
| **Phase 2** | Exploratory trials | Moderate |
| **Phase 1** | Safety trials | Weaker |

### 4. Literature Evidence

| Literature Type | Description | Evidence Strength |
|-----------------|-------------|-------------------|
| **RCT** | Randomized Controlled Trial | Highest |
| **Cohort** | Cohort Study | Moderate |
| **Case Report** | Individual Case Report | Reference |

---

## Step-by-Step Guide

<ol class="actionable-steps">
<li><strong>Step 1</strong>: Start from the <a href="/evidence-high/">High Evidence</a> page</li>
<li><strong>Step 2</strong>: Click on a drug of interest to enter the report</li>
<li><strong>Step 3</strong>: First read the "One-Sentence Summary" and "Quick Overview Table"</li>
<li><strong>Step 4</strong>: For deeper understanding, read clinical trials and literature evidence</li>
<li><strong>Step 5</strong>: Check "Conclusion & Next Steps" for recommended actions</li>
</ol>

---

## Frequently Asked Questions

### Q: High prediction score but low evidence level - how to interpret?

<div class="key-takeaway">
Prediction score reflects AI confidence. Evidence level reflects clinical research adequacy. The two can differ.
</div>

For example: A drug might have a 99.97% prediction score but only L2 evidence. This means:
- AI is very confident in the prediction
- But clinical evidence is not yet sufficient (only early-stage research)
- This is a promising research direction worth attention

### Q: What's the difference between Go and Proceed?

| Decision | Meaning | Recommended Action |
|----------|---------|-------------------|
| **Go** | Very strong evidence | Can proceed to in-depth evaluation |
| **Proceed** | Adequate evidence | Worth further feasibility evaluation |
| **Consider** | Some evidence | Weigh risks before deciding |
| **Explore** | Worth exploring | Gather more data first |
| **Hold** | Insufficient evidence | Not recommended to proceed currently |

---

## Further Reading

- [Evidence Levels Explained](/blog/2026/03/02/evidence-levels-explained/)
- [User Guide](/guide/)
- [Methodology](/methodology/)

---

<div class="disclaimer">
<strong>Note</strong><br>
This guide is for research reference only. Any clinical application requires consultation with professional healthcare personnel.
</div>
