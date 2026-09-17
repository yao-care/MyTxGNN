---
layout: default
title: Tipiracil
parent: High Evidence (L1-L2)
nav_order: 652
evidence_level: L1
indication_count: 10
---

# Tipiracil
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Laporan penilaian ahli farmasi

</div>

# Tipiracil: 從轉移性大腸直腸癌到 Colonic Neoplasm

## 一句話總結

Tipiracil 本身並非單獨藥物，而是與 trifluridine 固定劑量合併（TAS-102/Lonsurf）用於治療轉移性大腸直腸癌之藥物成分。
TxGNN 模型預測其對 **Colonic Neoplasm（大腸腫瘤）** 具高度關聯性，
目前有 **50+ 筆臨床試驗**與 **20 篇文獻**支持此方向，
但需注意此預測實質上是對「既有適應症」的再確認，而非全新訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 轉移性大腸直腸癌（作為 trifluridine/tipiracil 合併劑 TAS-102/Lonsurf 之成分；NPRA 仿單文字尚未取得） |
| 預測新適應症 | Colonic Neoplasm |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 馬來西亞市場狀態 | Marketed |
| 註冊許可證數量 | 2 |
| 建議決策 | Proceed with Guardrails |

---

## 為何此預測合理？

目前尚無 DrugBank 詳細作用機轉資料（[Data Gap]）。根據已知資訊，Tipiracil 是 trifluridine/tipiracil 複方（TAS-102/Lonsurf）的組成成分，其於轉移性大腸直腸癌之療效已獲證實，機轉上與大腸腫瘤治療直接相關。Tipiracil 為 thymidine phosphorylase 抑制劑，可抑制 trifluridine 之代謝分解、提高其血中濃度與抗腫瘤活性；trifluridine 本身經磷酸化後併入癌細胞 DNA，造成細胞毒性並抑制腫瘤生長。

值得特別說明的是：此案例的「原始適應症」與「預測新適應症」高度重疊——TAS-102 早已是後線轉移性大腸直腸癌的標準治療藥物之一。因此本預測的證據強度雖達 L1（多筆完成之 Phase 3 RCT，如 SUNLIGHT 試驗），但性質上屬於**既有已核准用途的再確認**，而非典型的老藥新用（drug repurposing）訊號，這點會影響決策解讀。

---

## 臨床試驗證據

| 試驗編號 | 期別 | 狀態 | 收案人數 | 關鍵發現 |
|---------|------|------|------|---------|
| [NCT03665506](https://clinicaltrials.gov/study/NCT03665506) | N/A（非介入性） | Completed | 315 | 德國真實世界研究，評估 trifluridine/tipiracil 於轉移性大腸直腸癌之療效與安全性 |
| [NCT06992648](https://clinicaltrials.gov/study/NCT06992648) | Phase 3 | Recruiting | 302 | trifluridine/tipiracil + regorafenib 對比 + bevacizumab，於難治性 mCRC 之非劣性試驗 |
| [NCT04737187](https://clinicaltrials.gov/study/NCT04737187) | Phase 3 | Completed | 492 | SUNLIGHT 試驗：trifluridine/tipiracil + bevacizumab 對比單獨使用於難治性 mCRC |
| [NCT03520946](https://clinicaltrials.gov/study/NCT03520946) | Phase 3 | Completed | 430 | Ramucirumab + TAS-102 對比 TAS-102 單藥於化療難治性 mCRC |
| [NCT05198934](https://clinicaltrials.gov/study/NCT05198934) | Phase 3 | Active, not recruiting | 160 | Sotorasib+panitumumab 對比研究者選擇（含 trifluridine/tipiracil）於 KRAS p.G12C 突變 mCRC |
| [NCT04776148](https://clinicaltrials.gov/study/NCT04776148) | Phase 3 | Completed | 563 | Lenvatinib+pembrolizumab 對比標準治療（含 regorafenib 及 TAS-102）於 mCRC |
| [NCT05600309](https://clinicaltrials.gov/study/NCT05600309) | Phase 3 | Completed | 94 | MK-4280A 對比標準治療（含 regorafenib 及 TAS-102）於 PD-L1 陽性 mCRC（KEYFORM-007） |
| [NCT05007132](https://clinicaltrials.gov/study/NCT05007132) | Phase 2 | Recruiting | 153 | FIRE-8 試驗：trifluridine/tipiracil + panitumumab 對比 + bevacizumab 作為 mCRC 一線治療 |
| [NCT02743221](https://clinicaltrials.gov/study/NCT02743221) | Phase 2 | Completed | 154 | TASCO1 試驗：TAS-102 + bevacizumab 對比 capecitabine + bevacizumab 於未經治療之 mCRC |
| [NCT07071844](https://clinicaltrials.gov/study/NCT07071844) | Phase 2 | Not yet recruiting | 162 | 評估雙週給藥方案降低 trifluridine/tipiracil + bevacizumab 之第3-4級嗜中性球低下發生率 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 關鍵發現 |
|------|-----|------|------|---------|
| [37133585](https://pubmed.ncbi.nlm.nih.gov/37133585/) | 2023 | RCT | New England Journal of Medicine | SUNLIGHT 試驗：trifluridine-tipiracil + bevacizumab 延長難治性 mCRC 病人整體存活期 |
| [37284901](https://pubmed.ncbi.nlm.nih.gov/37284901/) | 2023 | RCT | The Oncologist | MODURATE Phase Ib 試驗：優化 trifluridine/tipiracil + irinotecan + bevacizumab 給藥排程 |
| [37366880](https://pubmed.ncbi.nlm.nih.gov/37366880/) | 2023 | Review/Meta-analysis | Current Oncology | 系統性回顧：trifluridine/tipiracil + bevacizumab 於真實世界系列研究之療效與安全性 |
| [37414979](https://pubmed.ncbi.nlm.nih.gov/37414979/) | 2024 | Review | Clinical & Translational Oncology | TAS-102 於 mCRC 治療之療效與安全性系統性回顧與統合分析 |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Research | TAS-102 作用機轉綜述：抑制 DPD 增強 5-FU 抗腫瘤效果之機轉基礎 |
| [36864254](https://pubmed.ncbi.nlm.nih.gov/36864254/) | 2023 | Cohort | Nature Medicine | KRAS G12 密碼子特異性突變可預測 FTD/TPI 治療存活效益之生物標記研究 |
| [36990929](https://pubmed.ncbi.nlm.nih.gov/36990929/) | 2023 | Cohort | Journal of Geriatric Oncology | 高齡病人使用 FTD/TPI 與 regorafenib 之敘述性文獻回顧 |
| [38423630](https://pubmed.ncbi.nlm.nih.gov/38423630/) | 2024 | Cohort | Anticancer Research | 標準給藥 vs 雙週給藥 FTD/TPI 療效與安全性比較 |
| [37097664](https://pubmed.ncbi.nlm.nih.gov/37097664/) | 2023 | Cohort | Anticancer Research | FTD/TPI + bevacizumab 治療中噁心嘔吐之致吐性與風險因子分析 |
| [35474007](https://pubmed.ncbi.nlm.nih.gov/35474007/) | 2022 | Cohort | Clinical Colorectal Cancer | QUALITAS 研究：真實世界中 FTD/TPI 治療病人之生活品質與存活評估 |

---

## 馬來西亞市場資訊

NPRA 資料庫顯示 Tipiracil 相關製劑於馬來西亞共有 **2 筆有效註冊許可證**（市場狀態：Marketed），但許可證編號、產品名稱、劑型、製造商及核准適應症文字等細項尚未取得，需另行向 NPRA 官網查詢補齊。

---

## 細胞毒性資訊（抗腫瘤藥物）

本藥物（trifluridine/tipiracil 複方，臨床用名 TAS-102/Lonsurf）屬抗腫瘤化療藥物，故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | Conventional cytotoxic（核苷類似物／氟嘧啶類抗代謝藥物合併製劑） |
| 骨髓抑制風險 | High — 多筆試驗（如 NCT07071844、NCT04166604）以降低第3-4級嗜中性球低下為主要試驗目標，顯示嗜中性球低下為常見且需密切監測之毒性 |
| 致吐性分類 | Low to Moderate（文獻 PMID 37097664 顯示合併 bevacizumab 使用時仍有噁心嘔吐風險，需依風險因子評估） |
| 監測項目 | 全血球計數（含分類計數，特別是嗜中性球）、腎功能、電解質 |
| 處理防護 | 屬口服細胞毒性化療藥物，應依細胞毒性藥物處理規範進行防護與廢棄物處置 |

---

## 安全性考量

請參閱仿單以取得完整安全性資訊。

（TFDA/NPRA 仿單警語與禁忌症資料為阻斷性缺口 DG001，目前無法取得；藥物交互作用查詢亦無結果。）

---

## 結論與後續步驟

**決策：Proceed with Guardrails**

**理由：**
證據等級達 L1（含 SUNLIGHT 等多筆完成之 Phase 3 RCT），支持 trifluridine/tipiracil 於大腸直腸腫瘤之療效；但此預測實質上是對既有核准適應症的再確認而非新訊號，且 NPRA 安全性標籤資料（DG001，阻斷性）尚未取得，無法完成 S1 安全性初評。

**下一步需要補齊：**
- NPRA 仿單警語／禁忌症全文（DG001，阻斷性缺口）
- DrugBank 作用機轉確認資料（DG002）
- 完整的馬來西亞許可證明細（許可證號、產品名、劑型、核准適應症文字）
- 釐清「Colonic Neoplasm」預測與現行核准適應症（轉移性大腸直腸癌）之差異，確認是否構成真正的老藥新用機會
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

