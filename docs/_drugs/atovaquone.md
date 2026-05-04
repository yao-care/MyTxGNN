---
layout: default
title: Atovaquone
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 0
---

# Atovaquone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Atovaquone: 老藥新用評估待完成 — 資料不足，無法進行完整分析

---

## One-Sentence Summary

Atovaquone 是一種抗寄生蟲藥物，廣泛用於 *Pneumocystis jirovecii* 肺炎（PCP）的治療與預防，以及弓形蟲病和瘧疾預防（與proguanil併用）。
然而，本次 Evidence Pack 中 **TxGNN 預測適應症欄位為空**，且原始適應症記錄、作用機轉與安全性資訊均存在關鍵缺口，**無法進行完整的老藥新用評估**。
建議補齊資料後重新執行預測流程，再進行正式評估。

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | 未記錄於 Evidence Pack（依一般知識：PCP 治療/預防、弓形蟲病、瘧疾預防） |
| Predicted New Indication | **無**（`predicted_indications` 為空陣列） |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A（無預測結果） |
| Malaysia Market Status | ✓ Marketed（已上市） |
| Number of Registrations | 1 |
| Recommended Decision | **Hold** |

---

## Malaysia Market Information

NPRA 查詢回傳 1 筆已上市登記，但本次 Evidence Pack 未取得詳細登記欄位（產品名稱、劑型、核准適應症等）。

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|----------------------|--------------|-------------|---------------------|
| （未取得） | （未取得） | （未取得） | （未取得） |

> **補救措施**：透過 NPRA 官方查詢介面，以登記編號取得完整產品資訊並填入上表。

---

## Safety Considerations

Please refer to the package insert for safety information.

> 本次 Evidence Pack 的安全性欄位（警語、禁忌、藥物交互作用）均為資料缺口，尚未自仿單或 DrugBank 取得。

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
本次 Atovaquone Evidence Pack 存在多項關鍵缺口——TxGNN 預測結果缺失、原始適應症未記錄、作用機轉未取得、安全性警語與禁忌均未填入，評估流程無法繼續推進。

**To proceed, the following is needed:**

- **[Blocking — DG001]** 下載並解析 NPRA/TFDA 仿單 PDF，取得安全性警語與禁忌症，以解除 S1 安全性初評阻擋
- **[High — DG002]** 透過 DrugBank API 查詢 DB01117 的作用機轉（MOA），以支援機轉關聯性分析
- **重新執行 TxGNN 預測流程**，針對 Atovaquone (DB01117) 生成新適應症候選清單（`predicted_indications`）
- **補全 NPRA 登記詳細資訊**：取得產品名稱、劑型、核准適應症全文
- 資料補齊後，依照 Evidence Pack v4 規格重新生成報告，進行完整 L1–L5 證據評級與決策分析

---

> ⚠️ **YMYL 免責聲明**：本報告結果僅供研究參考，不構成任何醫療建議。老藥新用候選藥物需經過正式臨床驗證後，方可應用於實際醫療決策。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

