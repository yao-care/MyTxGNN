---
layout: default
title: Metodologi
parent: Bantuan
nav_order: 1
description: "MyTxGNN prediction and validation methodology"
permalink: /methodology/
---

# Methodology
{: .fs-9 }

From AI prediction to evidence validation
{: .fs-6 .fw-300 }

---

## Overall Pipeline

```
TxGNN Prediction → Data Collection (Bundle) → Evidence Grading → Report Generation
```

---

## Step 1: TxGNN Prediction

### Two Prediction Approaches

MyTxGNN uses two complementary approaches:

#### Knowledge Graph (KG) Prediction

Based on existing relationships in the TxGNN biomedical knowledge graph:

1. **Knowledge Graph Construction**
   - 17,080 nodes (drugs, diseases, genes, proteins)
   - Complex inter-node relationships from multiple sources

2. **Relationship Inference**
   - Identifies drugs with similar relationship patterns
   - Predicts potential new drug-disease associations

3. **Output**
   - Drug-disease pairs based on knowledge graph patterns
   - 41,560 predictions for 508 drugs

#### Deep Learning (DL) Prediction

Using TxGNN's neural network model:

1. **Graph Neural Network**
   - Learns hidden relationships between nodes
   - Predicts new drug-disease associations

2. **Confidence Scoring**
   - Each drug-disease pair receives a prediction score
   - Higher scores indicate higher confidence

3. **Output**
   - 9.97 million total predictions
   - 176,021 high-confidence predictions (score ≥ 0.7)

### Prediction Parameters

| Parameter | KG Method | DL Method |
|-----------|-----------|-----------|
| Score Threshold | Based on graph distance | ≥ 0.7 (high confidence) |
| Exclude Known Indications | Yes | Yes |
| DrugBank Mapping Required | Yes | Yes |

---

## Step 2: Data Collection (Bundle)

For each predicted drug-disease pair, we automatically collect supporting evidence:

### Clinical Trials

- **Source**: [ClinicalTrials.gov](https://clinicaltrials.gov/)
- **Search Strategy**: Drug name + Disease name
- **Fields**: Trial ID (NCT), Phase, Status, Enrollment

### Academic Literature

- **Source**: [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- **Search Strategy**: Drug name + Disease name
- **Fields**: PMID, Title, Year, Journal, Abstract

### Drug Information

- **Source**: [DrugBank](https://go.drugbank.com/)
- **Fields**: Mechanism of action, Pharmacology, Indications

### Malaysia Regulatory

- **Source**: NPRA (via data.gov.my)
- **Fields**: Registration number, Product name, Status, Active ingredients

---

## Step 3: Evidence Level Assessment

Based on collected evidence, we assign evidence levels:

### Level Definitions

| Level | Definition | Criteria |
|:-----:|------------|----------|
| **L1** | Multiple Phase 3 RCTs / Systematic Reviews | ≥2 Phase 3 trials or systematic reviews |
| **L2** | Single RCT or Multiple Phase 2 Trials | 1 RCT or ≥2 Phase 2 trials |
| **L3** | Observational Studies / Large Case Series | Observational studies or case series |
| **L4** | Preclinical / Mechanistic / Case Reports | Basic research or limited cases |
| **L5** | Model Prediction Only | No clinical evidence found |

### Assessment Flow

<style>
.flowchart {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 500px;
  margin: 1.5rem 0;
}
.flow-step {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.flow-question {
  background: #f8f9fa;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  border-left: 3px solid #1976D2;
  flex: 1;
}
.flow-arrow {
  color: #666;
  font-size: 1.2rem;
}
.flow-result {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 600;
  min-width: 50px;
  text-align: center;
}
.flow-l1 { background: #2E7D32; color: white; }
.flow-l2 { background: #66BB6A; color: white; }
.flow-l3 { background: #FDD835; color: #333; }
.flow-l4 { background: #FB8C00; color: white; }
.flow-l5 { background: #9E9E9E; color: white; }
.flow-no {
  margin-left: 2rem;
  padding-left: 1rem;
  border-left: 2px dashed #ddd;
}
</style>

<div class="flowchart">
  <div class="flow-step">
    <div class="flow-question">Phase 3 RCT or Systematic Review?</div>
    <span class="flow-arrow">→</span>
    <div class="flow-result flow-l1">L1</div>
  </div>
  <div class="flow-no">
    <div class="flow-step">
      <div class="flow-question">Phase 2 RCT?</div>
      <span class="flow-arrow">→</span>
      <div class="flow-result flow-l2">L2</div>
    </div>
    <div class="flow-no">
      <div class="flow-step">
        <div class="flow-question">Observational Study?</div>
        <span class="flow-arrow">→</span>
        <div class="flow-result flow-l3">L3</div>
      </div>
      <div class="flow-no">
        <div class="flow-step">
          <div class="flow-question">Preclinical Research?</div>
          <span class="flow-arrow">→</span>
          <div class="flow-result flow-l4">L4</div>
        </div>
        <div class="flow-no">
          <div class="flow-step">
            <div class="flow-question">Model Prediction Only</div>
            <span class="flow-arrow">→</span>
            <div class="flow-result flow-l5">L5</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---

## Step 4: Decision Recommendations

Based on evidence level and other factors, we provide decision recommendations:

| Decision | Description | Recommended Action |
|----------|-------------|-------------------|
| **Go** | Strong evidence support | Proceed to evaluation or trial planning |
| **Proceed** | Sufficient evidence support | Further evaluate feasibility |
| **Consider** | Some evidence exists | Consider with caution |
| **Explore** | Worth exploring | Gather more data |
| **Hold** | Insufficient evidence | Not recommended to proceed |

### Factors Affecting Decisions

- Evidence strength and consistency
- NPRA registration and approval status
- Relationship between predicted and original indications
- Safety considerations

---

## Quality Control

### Data Validation

- Clinical trial ID format verification
- PubMed ID validity check
- Registration status confirmation

### Manual Review

- High evidence level (L1-L2) reports manually confirmed
- Decision recommendation reasonability check

---

## Limitations & Caveats

1. **Prediction ≠ Causation**: TxGNN predictions are based on associations, not causal relationships
2. **Limited Evidence Collection**: Only searches public databases; may miss some evidence
3. **Language Limitation**: Primarily searches English-language data
4. **Timeliness**: Data updates over time; reports reflect status at generation time

{: .note }
> This methodology is continuously improved. Feedback is welcome.
