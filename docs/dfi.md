---
layout: default
title: Drug-Food Interactions
parent: Safety Data
nav_order: 3
description: "MyTxGNN Drug-Food Interaction database covering 29 common foods that may affect drug efficacy."
permalink: /dfi/
---

# Drug-Food Interactions (DFI)

<p class="key-answer" data-question="What is Drug-Food Interaction?">
<strong>Drug-Food Interaction (DFI)</strong> refers to how food components affect drug absorption, metabolism, or efficacy. Understanding these interactions is important for drug repurposing research as different patient populations may have different dietary habits.
</p>

<div class="key-takeaway">
Drug-food interactions are often overlooked but very important for drug repurposing research. Different disease patient populations may have different dietary habits, and these factors need to be considered for their effects on drug efficacy.
</div>

---

## What is DFI?

Food and drug interactions occur mainly through these mechanisms:

| Mechanism | Description | Example |
|-----------|-------------|---------|
| **Absorption Effect** | Food alters drug absorption in gut | Calcium reducing antibiotic absorption |
| **Metabolism Effect** | Food components affect liver enzyme activity | Grapefruit inhibiting CYP3A4 |
| **Synergistic Action** | Food enhances drug effect | High potassium foods + potassium-sparing diuretics |
| **Antagonistic Action** | Food weakens drug effect | Vitamin K + Warfarin |

---

## Data Source

<table class="comparison-table">
<thead>
<tr><th>Item</th><th>Information</th></tr>
</thead>
<tbody>
<tr>
  <td>Data Source</td>
  <td><a href="https://ddinter2.scbdd.com/" target="_blank" rel="noopener">DDInter 2.0</a></td>
</tr>
<tr>
  <td>DFI Records</td>
  <td>857</td>
</tr>
<tr>
  <td>Food Types Covered</td>
  <td>29</td>
</tr>
<tr>
  <td>License</td>
  <td>CC BY-NC-SA 4.0</td>
</tr>
</tbody>
</table>

---

## DFI Severity Levels

| Level | English | Description | Recommended Action |
|-------|---------|-------------|-------------------|
| **Severe** | Major | Significantly affects efficacy or causes toxicity | Avoid concurrent intake, patient education |
| **Moderate** | Moderate | May need timing or dose adjustment | Recommend separating intake |
| **Mild** | Minor | Low clinical significance | Generally safe to combine |

---

## Common Drug-Food Interactions

### Grapefruit

<p class="key-answer" data-question="How does grapefruit affect drugs?">
Grapefruit contains furanocoumarins that inhibit intestinal CYP3A4 enzymes, causing elevated blood levels of many drugs and potentially increasing side effect risks.
</p>

Commonly affected drugs:
- Statins (cholesterol-lowering drugs)
- Calcium channel blockers
- Some immunosuppressants
- Certain anti-arrhythmic drugs

### High Vitamin K Foods

<ol class="actionable-steps">
<li>Dark green vegetables (spinach, kale) contain high vitamin K</li>
<li>May reduce Warfarin and other anticoagulant effects</li>
<li>Recommend maintaining stable vitamin K intake rather than complete avoidance</li>
</ol>

### Dairy Products

- Calcium binds with certain antibiotics (e.g., Fluoroquinolones)
- Reduces drug absorption
- Recommend 2-hour interval between intake

### Alcohol

- Enhances CNS depressant effects
- May increase hepatotoxic drug risks
- Some drugs cause disulfiram-like reaction

---

## Food Categories Covered

This database covers 29 common foods/food components:

| Category | Foods |
|----------|-------|
| **Fruits** | Grapefruit, citrus, cranberry |
| **Vegetables** | Spinach, kale, broccoli |
| **Dairy** | Milk, cheese, yogurt |
| **Beverages** | Coffee, tea, alcohol |
| **Others** | High fiber foods, high fat foods, seafood |

---

## Application in Drug Repurposing

<blockquote class="expert-quote">
"Drug repurposing research needs to consider the dietary habits of target patient populations. For example, if new indication patients commonly need specific nutritional supplements, we must evaluate interactions between these foods and candidate drugs."
<cite>— Drug Safety Assessment Principles</cite>
</blockquote>

### Evaluation Points

1. **Target population dietary characteristics**: Understand common dietary habits
2. **Supplement use**: Many chronic disease patients take health supplements
3. **Special dietary needs**: Diabetic low-sugar diets, renal patient low-potassium diets
4. **Cultural factors**: Regional dietary habit differences

---

## Related Resources

| Resource | Description | Link |
|----------|-------------|------|
| Drug-Drug Interactions | DDI database | [Go]({{ '/ddi/' | relative_url }}) |
| Drug-Disease Safety | DDSI database | [Go]({{ '/ddsi/' | relative_url }}) |
| Drug-Herb Interactions | DHI database | [Go]({{ '/dhi/' | relative_url }}) |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
DFI data on this page is for research reference only and <strong>does not constitute dietary or medication advice</strong>. Dietary considerations during medication should consult professional pharmacists or physicians. Drug-food interactions vary by individual factors.
<br><br>
<small>Last reviewed: 2026-03-03 | Reviewer: MyTxGNN Research Team</small>
</div>
