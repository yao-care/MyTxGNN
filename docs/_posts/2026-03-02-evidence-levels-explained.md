---
layout: default
title: "Tutorial: Understanding Evidence Levels"
description: "Complete explanation of the L1-L5 evidence level system used in MyTxGNN drug repurposing reports."
date: 2026-03-02
categories: [Tutorial]
tags: [Evidence Levels, Methodology]
---

# Understanding Evidence Levels

<p class="key-answer" data-question="What are the 5 evidence levels?">
MyTxGNN uses a 5-level evidence classification system (L1-L5) to help researchers quickly assess the clinical validity of drug repurposing predictions. L1 represents the highest evidence quality, while L5 indicates AI prediction only.
</p>

---

## The 5 Evidence Levels

| Level | Name | Definition | Clinical Implication |
|-------|------|------------|---------------------|
| **L1** | Very High | Multiple Phase 3 RCTs or Systematic Reviews | Strong support for clinical consideration |
| **L2** | High | Single RCT or Multiple Phase 2 trials | Design validation studies |
| **L3** | Moderate | Phase 1/2 trials or Observational studies | Requires more research |
| **L4** | Low | Case reports or Preclinical only | Exploratory research |
| **L5** | Prediction Only | AI prediction, no clinical evidence | Hypothesis generation |

---

## Detailed Explanations

### L1: Very High Evidence

<div style="background: #e8f5e9; padding: 1rem; border-radius: 8px; border-left: 4px solid #2E7D32; margin: 1rem 0;">
<strong>What qualifies:</strong>
<ul>
<li>Multiple Phase 3 randomized controlled trials</li>
<li>Systematic reviews with meta-analysis</li>
<li>Regulatory approval for the new indication</li>
</ul>
</div>

**Recommended Action**: Can proceed to clinical evaluation planning

### L2: High Evidence

<div style="background: #e8f5e9; padding: 1rem; border-radius: 8px; border-left: 4px solid #66BB6A; margin: 1rem 0;">
<strong>What qualifies:</strong>
<ul>
<li>Single well-designed RCT</li>
<li>Multiple Phase 2 clinical trials</li>
<li>Strong observational study with large sample</li>
</ul>
</div>

**Recommended Action**: Worth pursuing validation studies

### L3: Moderate Evidence

<div style="background: #fff3e0; padding: 1rem; border-radius: 8px; border-left: 4px solid #FF9800; margin: 1rem 0;">
<strong>What qualifies:</strong>
<ul>
<li>Phase 1 or early Phase 2 trials</li>
<li>Cohort or case-control studies</li>
<li>Mechanistic studies with clinical endpoints</li>
</ul>
</div>

**Recommended Action**: Monitor for additional evidence

### L4: Low Evidence

<div style="background: #fce4ec; padding: 1rem; border-radius: 8px; border-left: 4px solid #E91E63; margin: 1rem 0;">
<strong>What qualifies:</strong>
<ul>
<li>Case reports or case series</li>
<li>Preclinical studies only (animal/in vitro)</li>
<li>Expert opinion with mechanism support</li>
</ul>
</div>

**Recommended Action**: Exploratory research only

### L5: Prediction Only

<div style="background: #f5f5f5; padding: 1rem; border-radius: 8px; border-left: 4px solid #9E9E9E; margin: 1rem 0;">
<strong>What qualifies:</strong>
<ul>
<li>TxGNN AI prediction only</li>
<li>Knowledge graph relationship inference</li>
<li>No clinical human studies found</li>
</ul>
</div>

**Recommended Action**: Use for hypothesis generation

---

## Evidence vs. Prediction Score

<div class="key-takeaway">
A high TxGNN prediction score does NOT guarantee high evidence level. The prediction score reflects AI confidence based on knowledge graph patterns, while evidence level reflects actual clinical validation.
</div>

| Scenario | Prediction Score | Evidence Level | Interpretation |
|----------|-----------------|----------------|----------------|
| A | 99%+ | L1 | Excellent - AI prediction validated by strong evidence |
| B | 99%+ | L5 | Novel prediction - worth investigating but unvalidated |
| C | 70% | L1 | Validated relationship but AI uncertain |
| D | 70% | L5 | Low priority - uncertain and unvalidated |

---

## How to Use Evidence Levels

### For Researchers

1. **Prioritize L1-L2** for immediate investigation
2. **Monitor L3** for emerging evidence
3. **Use L4-L5** for hypothesis generation and grant applications

### For Clinicians

1. **L1 only** should be considered for clinical discussion
2. **L2-L3** may inform clinical trial enrollment decisions
3. **L4-L5** are for research context only

---

## Further Reading

- [How to Read Reports](/blog/2026/03/01/how-to-read-reports/)
- [Methodology](/methodology/)
- [High Evidence Drugs](/evidence-high/)

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Evidence levels are assigned based on available literature and may not reflect the most recent publications. Always verify with primary sources for clinical decisions.
</div>
