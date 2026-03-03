---
layout: default
title: Nota Pembelajaran Sintaks CQL
parent: SMART on FHIR
nav_order: 9
description: "Nota pembelajaran untuk Clinical Quality Language (CQL) dalam konteks MyTxGNN"
permalink: /smart/cql/
---

# Nota Pembelajaran Sintaks CQL

<p class="key-answer" data-question="Apakah CQL?">
<strong>Clinical Quality Language (CQL)</strong> adalah bahasa formal untuk menyatakan logik klinikal. Ia digunakan dalam FHIR untuk mendefinisikan kriteria pengukuran kualiti, peraturan sokongan keputusan, dan logik klinikal lain.
</p>

---

## Pengenalan CQL

### Mengapa CQL?

| Masalah | Penyelesaian CQL |
|---------|------------------|
| Logik klinikal tidak standard | Bahasa formal yang boleh digunakan semula |
| Sukar untuk dikongsi | Sintaks yang jelas dan boleh dibaca |
| Tidak boleh dijalankan | Boleh dikompil dan dijalankan terhadap data FHIR |

---

## Struktur Asas

### Library Definition

```cql
library DrugRepurposingLibrary version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

codesystem DrugBank: 'https://go.drugbank.com/drugs/'
```

### Value Sets

```cql
valueset "Corticosteroids": 'https://mytxgnn.yao.care/fhir/ValueSet/corticosteroids'
valueset "Allergic Conditions": 'https://mytxgnn.yao.care/fhir/ValueSet/allergic-conditions'
```

### Context

```cql
context Patient
```

---

## Jenis Data

| Jenis | Penerangan | Contoh |
|-------|------------|--------|
| `Boolean` | Benar/Palsu | `true`, `false` |
| `Integer` | Nombor bulat | `42`, `-10` |
| `Decimal` | Nombor perpuluhan | `3.14`, `0.85` |
| `String` | Teks | `'Prednisolone'` |
| `DateTime` | Tarikh dan masa | `@2026-03-03T10:30:00` |
| `Code` | Kod dari sistem | `Code 'DB00860' from DrugBank` |

---

## Pengendali

### Perbandingan

```cql
// Sama dengan
medication.code = 'DB00860'

// Tidak sama
status != 'completed'

// Lebih besar/kurang
score > 0.7
score >= 0.5
score < 0.3
score <= 0.9

// Dalam julat
score in Interval[0.7, 1.0]
```

### Logik

```cql
// DAN
condition1 and condition2

// ATAU
condition1 or condition2

// TIDAK
not condition

// Implikasi
condition1 implies condition2
```

---

## Pengekstrakan Data FHIR

### Dapatkan Sumber

```cql
// Semua MedicationRequest untuk pesakit
define "Active Medications":
  [MedicationRequest: status = 'active']

// Dengan kod tertentu
define "Prednisolone Orders":
  [MedicationRequest: medication in "Corticosteroids"]
```

### Akses Medan

```cql
define "Medication Codes":
  "Active Medications" M
    return M.medication.coding[0].code
```

---

## Fungsi

### Fungsi Terbina Dalam

```cql
// Tarikh
Today()
Now()
AgeInYears()

// String
StartsWith('Pred', drugName)
Contains('steroid', description)
Lower(drugName)

// Senarai
Count(medications)
First(medications)
Last(medications)
Exists(medications)
```

### Fungsi Tersuai

```cql
define function HighConfidencePrediction(score Decimal):
  score >= 0.7

define function FormatDrugName(name String):
  Upper(Substring(name, 0, 1)) + Lower(Substring(name, 1))
```

---

## Contoh MyTxGNN

### Pustaka Penggunaan Semula Ubat

```cql
library DrugRepurposingLibrary version '1.0.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1'

codesystem DrugBank: 'https://go.drugbank.com/drugs/'

// Konteks pesakit
context Patient

// Ubat aktif pesakit
define "Current Medications":
  [MedicationRequest: status = 'active']

// Ubat dengan ramalan keyakinan tinggi
define "High Confidence Repurposing Candidates":
  "Current Medications" M
    where exists (
      [ClinicalUseDefinition: subject = M.medication]
        CUD where CUD.extension('prediction-score').value >= 0.7
    )

// Periksa sama ada pesakit mengambil kortikosteroid
define "On Corticosteroids":
  exists (
    "Current Medications" M
      where M.medication.coding.code in {
        'DB00860', 'DB00443', 'DB00741', 'DB01234'
      }
  )

// Cadangan untuk kajian lanjut
define "Repurposing Alert":
  if "On Corticosteroids" and exists "High Confidence Repurposing Candidates"
  then 'Consider reviewing repurposing predictions for current corticosteroid therapy'
  else null
```

---

## Menjalankan CQL

### Dengan cql-execution

```javascript
const cql = require('cql-execution');
const fhir = require('cql-exec-fhir');

// Muat pustaka CQL
const library = cql.Library.parse(cqlSource);

// Buat pelaksana
const executor = new cql.Executor(library);

// Jalankan terhadap data pesakit
const patientSource = fhir.PatientSource.create('4.0.1');
patientSource.loadBundles([patientBundle]);

const results = executor.exec(patientSource);
console.log(results.patientResults);
```

---

## Sumber Pembelajaran

| Sumber | Penerangan | Pautan |
|--------|------------|--------|
| Spesifikasi CQL | Dokumentasi rasmi HL7 | [cql.hl7.org](https://cql.hl7.org/) |
| CQL Tutorial | Panduan bermula | [GitHub](https://github.com/cqframework/CQL-Formatting-and-Usage-Wiki) |
| cql-execution | Pustaka JavaScript | [npm](https://www.npmjs.com/package/cql-execution) |

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Nota pembelajaran ini adalah untuk <strong>tujuan pendidikan</strong>. Logik CQL untuk kegunaan klinikal memerlukan pengesahan dan pengujian yang teliti.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
