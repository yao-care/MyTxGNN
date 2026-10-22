---
layout: default
title: Panduan Pengguna
parent: Bantuan
nav_order: 2
description: "How to use MyTxGNN drug repurposing prediction platform"
permalink: /guide/
---

# User Guide

Learn how to effectively use MyTxGNN for drug repurposing research.

---

## Getting Started

### What Can You Do with MyTxGNN?

1. **Browse Drug Predictions**: View predicted new indications for 508 NPRA-approved drugs
2. **Access FHIR API**: Integrate predictions into your clinical systems
3. **Download Data**: Get prediction data in CSV format for analysis
4. **Monitor News**: Track health news related to drug repurposing in Malaysia

---

## Understanding Predictions

### How Predictions Are Made

MyTxGNN lists drug repurposing predictions from the TxGNN model (deep learning: a graph neural network trained on a biomedical knowledge graph).

- The model gives every drug–disease pair a score
- Indications already recorded for the drug in the knowledge graph or in its product licence are known uses; they are excluded and not counted as new predictions
- Drug pages list up to the top 10 remaining predictions with a score of at least 0.99

### Interpreting Results

This site only lists predictions with a score of 0.99 or higher (up to the top 10 per drug). The score ranks candidates inside the model; it is not a probability of clinical efficacy.

---

## Using the FHIR API

### Capability Statement

Check API capabilities:
```
GET /fhir/metadata
```

### MedicationKnowledge

Get drug information:
```
GET /fhir/MedicationKnowledge/{drugbank_id}
```

Example:
```
GET /fhir/MedicationKnowledge/db00860
```

### ClinicalUseDefinition

Get drug-indication predictions:
```
GET /fhir/ClinicalUseDefinition/{drug}-{indication}
```

Example:
```
GET /fhir/ClinicalUseDefinition/db00860-allergic-rhinitis
```

---

## Research Workflow

### Recommended Steps

1. **Identify Target**
   - Start with a drug of interest
   - Or start with a disease you want to find treatments for

2. **Review Predictions**
   - Check the predicted new indications for the drug/disease
   - Review DL confidence scores

3. **Gather Evidence**
   - Use our evidence collectors (ClinicalTrials.gov, PubMed)
   - Check for existing clinical trials

4. **Assess Feasibility**
   - Consider drug availability in Malaysia (NPRA status)
   - Review safety profile

5. **Plan Next Steps**
   - Design validation studies
   - Consult with clinical experts

---

## Tips for Researchers

### Best Practices

1. **Cross-reference predictions** with existing literature
2. **Check multiple sources** for clinical trial data
3. **Consider mechanism of action** when evaluating predictions
4. **Note prediction confidence scores** when prioritizing candidates

### Common Pitfalls to Avoid

1. **Don't treat predictions as validated findings**
2. **Don't ignore safety considerations**
3. **Don't rely solely on high scores** - context matters
4. **Don't skip regulatory considerations**

---

## Frequently Asked Questions

### Q: How accurate are the predictions?

A: TxGNN has been validated against known drug-disease relationships with high accuracy. However, predictions should be validated through clinical evidence before application.

### Q: Can I use this data for commercial purposes?

A: The data is provided for research purposes. Commercial use may be subject to individual data source licenses (DrugBank, etc.).

### Q: How often is the data updated?

A: NPRA data is updated weekly. Predictions are regenerated periodically as the underlying models improve.

### Q: Why are some drugs not included?

A: Only drugs that could be mapped to DrugBank IDs are included. Some local or combination products may not have DrugBank entries.

---

## Getting Help

### Resources

- **GitHub Issues**: Report bugs or request features
- **Methodology Page**: Understand our prediction approach
- **Data Sources**: Learn about our data origins

### Contact

For research collaboration inquiries, please open a GitHub issue with the "collaboration" label.

---

<div class="disclaimer">
<strong>Research Use Only</strong><br>
MyTxGNN is designed for research purposes. Always validate predictions through proper clinical trials and consult healthcare professionals for medical decisions.
</div>
