# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」「藥物頁許可證表與張數」兩節；
做法同 UsTxGNN，見 UsTxGNN/CLAUDE.md 同名一節）。規則與程式都在本 repo；頁面文字用馬來文，依據是NPRA 藥品註冊（data.gov.my 的 pharmaceutical_products.csv 現行註冊與撤銷清單）。本站的在地設定集中在 `src/mytxgnn/regulatory/site.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、每頁查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/mytxgnn/regulatory/page_format.py`（規則在 site.py 的 HEADER_RULE） | 頁首＝Gambaran Ringkas「Tahap Bukti」（另有 Aras／Paras Bukti 寫法）格的**第一個**等級（主預測）。2026-11-12 實測 598 頁有總覽等級，全部符合；整格取最高會有 4 頁不同。front matter 沒有 parent 的頁（layout: drug 的 noindex 頁，73 頁）不掛在列表頁下，不驗 parent |
| 撤回預測 | `src/mytxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/my_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/mytxgnn/regulatory/licenses.py` | 快照存本藥號碼與事實層；gate 依快照驗市場段落表格的號碼歸屬、狀態列與張數列、表格列狀態（本站沒有程式產生的許可證表，所以沒有程式區塊標記） |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依成分重建刪句後（`scripts/license_rebuild_run.py` 有的話會自動跑）或依 git 前後版本，把正文刪改轉成 correct 紀錄 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證；本站證據包的 NPRA 紀錄沒有適應症文字，可比對 0 頁（程式照實回報） |
| gate | `scripts/check_seo_docs.py` 第 18–21 項 | 紀錄都已套用、許可證＝快照、頁首＝本站規則算出的等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、license_rebuild_run.py、每週排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（排程與重建會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 依成分重建後直接刪掉的矛盾子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 181 筆紀錄（157 頁；沒有因 AI 重產而原句已不在頁面的）。
`scripts/sync_notes_to_docs.py` 依 notes 重寫整頁時，會重套紀錄（有程式許可證表的站也保留舊頁的程式區塊），notes 裡的舊錯句會被紀錄再更正一次。

正文許可證張數由程式改寫（2026-11-12 用戶決定；比照 Tw 的 `page_postprocess.rewrite_count_prose`）：`scripts/rewrite_license_counts.py` 依 `snapshots/my_licenses.json.gz` 的事實層改寫正文的馬來文「N lesen sah／N pendaftaran／N produk berdaftar」張數，
規則在 `src/mytxgnn/regulatory/count_prose.py`（只改句型明確的；有保留、講證據包或查詢、相對數、劑型或廠商子集、顯示筆數、partial 頁不動；同一行有句子判斷不了就整行不動；數字已等於總數或有效數任一讀法就不動）。
程式改寫的張數不逐筆寫查核紀錄、頁面不加說明框（同 Tw）；查核紀錄 replacement／anchor 所在的句子不改。`apply_drug_reviews.py`（非 --check）結尾與 `build_license_snapshot.py` 寫完快照後都會跑，
所以每週排程、license_rebuild_run、sync_notes_to_docs 之後張數會跟著事實層更新；gate 第 22 項擋「再跑一次會變」。
判斷不了的句子（說「全部有效／全部單方」而事實不符、沒有限定詞而有效數≠總數、建立在 0 張前提上）不改，`--list` 列出，2026-11-12 已用 `--uncertain` 加進待查清單（source：正文許可證張數程式改寫判斷不了的句子），要改請寫查核紀錄。
2026-11-12 待查清單裡程式判斷不了的 20 句（18 頁）已逐句對照事實層與證據包 npra.records，以 `my-lic-20261112-*` 改寫（「全部有效」而實際有 Expired 的改成「N daripadanya sah dan 1 telah tamat tempoh」；張數照事實層；單方／複方張數照證據包成分，與事實層一致），待查清單標 resolved。trastuzumab 證據包 18 張、事實層 14 張，照事實層寫。

## 新資料查不到的登記號（2026-11-17）

2026-11-16 每週排程列出 324 張「新資料查不到」（證據包 12,462 張，超過 2% 開 issue）。用戶要求確認實際狀態：重新下載 data.gov.my
的 pharmaceutical_products.csv（現行註冊，28,387 筆）與 pharmaceutical_products_cancelled.csv（撤銷，1,623 筆；data.gov.my 只有這兩份藥品註冊資料集）逐號比對。
大小寫、空白、號碼格式都對得上（0 張是寫法差異），分三類：
- 50 張是同一張註冊換了尾碼（NPRA 登記號後的類別字母改了，或到期後以新尾碼續證；例：MAL09020971ARZ→MAL09020971ACRZ（Progynova，持有人 Bayer→Menarini）、
  MAL21046030AZ 2026-04-02 到期→MAL21046030ARZ）。判定：前 8 位數字相同、產品名與有效成分相同、現行檔裡只有一個這樣的號。
  `scripts/license_adapter.py` 的 status_index 讓舊號沿用新號的狀態：新號不在同一個證據包（12 張）→ 有效（「… (now listed as 新號)」）；
  新號已在同一個證據包（38 張）→ RETIRED_STATUS（算非有效，免得同一張註冊算兩張）。產品名或成分不同的同號不同尾碼（5 張，例：MAL11030014AZ Prevulcer／MAL11030014HA Toltravet）不認。
- 209 張兩份都沒有、證據包到期日已過（原本就是 EXPIRED_STATUS）：`confirmed_absent()` 讓排程列成「現行清單確認已不列」，不算查不到；preprocess 另記 npra_not_listed（第一次發現日，又出現就拿掉）。
- 65 張兩份都沒有、到期日未到（例：Cymbalta MAL05092473ARZ、Forxiga 5mg MAL14015013ARZ）：當時維持 2026-11-05 用戶決定的 UNKNOWN_STATUS（NPRA QUEST3+ 單筆查詢擋自動化請求）；
  2026-11-19 用戶以瀏覽器在 QUEST3+（https://quest3plus.bpfk.gov.my/pmo2/index.php）逐筆查，並對照 data.gov.my 兩份資料集 2026-11-19 03:00 版
  （txgnn/.claude/manual_license_lookup_20261117/my_npra_result_20261119.csv；QUEST3+ 只顯示號碼／品名／持有人、不顯示狀態），結果：
  - 換號 3 張（前 8 碼、持有人、成分相同，產品名不同所以自動換尾碼規則認不到；不放寬自動規則）收在 `scripts/license_adapter.py` 的人工確認表 MY_RENUMBERED（每筆附依據）：
    MAL16035030N→MAL16035030NC（MHD NutriCenta，Cameron Bioscience，到期 2031-03-26）、MAL23046028ACZ→MAL23046028AZ（Xostavid 40→Urilog 40，febuxostat，Healol，2028-04-06）、
    MAL23046029ACZ→MAL23046029AZ（Urilog 80）。處理同換尾碼：新號已在同一個證據包→RETIRED_STATUS（febuxostat、riboflavin、ascorbic_acid 等），不在（vitamin_c）→沿用新號狀態。
  - 61 張兩份資料集都沒有、QUEST3+ 依號碼與品名也查不到（例：Genvoya MAL17025022ACZ、ESBRIET 膠囊 MAL16115027ACRZ——現在只剩膠衣錠 MAL24036008／9ACRZ、Cymbalta 30／60 mg、MabThera 小瓶 2 張）
    收在人工確認表 MY_NOT_LISTED_CONFIRMED：preprocess 寫 NOT_LISTED_STATUS（「Not in current NPRA register (checked 2026-11-19 …); date of removal from the register not published」）、
    license_status＝cancelled（事實層非有效）＋npra_manual_check；confirmed_absent 回真；不依賴下載，任一份清單又查到就照清單狀態並拿掉標記。NPRA 沒有公開撤銷，頁面不寫成 dibatalkan。
    MAL20066031NC 同前 8 碼的 MAL20066031NCR 是 watsons 魚油、持有人不同，不算換號，歸這類。
  - MAL19890435ACZ TUSSIFED SYRUP：QUEST3+ 仍列、data.gov.my 兩份都不列，兩邊矛盾，維持 UNKNOWN_STATUS（每週排程「新資料查不到」1 張）。
  - 頁面（2026-11-19）：56 頁概覽狀態列／張數列照事實層同步（「status tidak dapat disahkan」拿掉）；全部非有效的頁狀態列改用母目錄 check_drug_page.py 的 SCOPE_CANCELLED["MyTxGNN"]
    「Tidak dipasarkan (tiada pendaftaran semasa: N daripada N dibatalkan, tamat tempoh atau tidak lagi tersenarai dalam daftar NPRA)」（本站 tools/txgnn 同步同一份；
    elvitegravir 1 頁新變成全部非有效，依成分對現行檔確認沒有其他 elvitegravir 產品；原本全部註銷的 andexanet_alfa、betaxolol_hydrochloride、tolbutamide、zanamivir 跟著換寫法）。
    正文與表格以 `my-lic-20261119-*`（duloxetine 2、nonivamide 1）、`my-row-20261119-*`（rituximab 2 列、tazobactam 1 列）更正，`my-lic-20261112-levodopa-1`、`my-lic-20261112-clotrimazole-1` 同 id 重發（「tanpa status」不再成立，前版存 history）。
兩份資料集任一份下載失敗或現行號碼少於 MIN_CURRENT（20,000）時不做上述判定。
- 頁面：概覽狀態列／張數列由程式同步（32 頁）；正文與表格跟新事實矛盾的以 `my-lic-20261117-*`、`my-row-20261117-*` 更正（cefoperazone、estradiol_valerate、dexmedetomidine_hydrochloride、netarsudil 2 列、thiotepa 1 列），
  apixaban、cyanocobalamin、vitamin_e 的 11-12 紀錄同 id 重發（前版存 history）。
- 同日修正換尾碼的「同一個證據包」判定：原本用全站聯集（舊號只要在任何一個也含新號的證據包就整站標 RETIRED_STATUS），同一個舊號在好幾個藥的證據包時會誤判。
  改成逐個證據包判斷（preprocess 標 `npra_duplicate_of`、update 換成 RETIRED_STATUS；其他證據包沿用新號的現行狀態）。受影響 5 個證據包 6 筆：trastuzumab（Enhertu MAL24046001ACZ，新號只在 trastuzumab_deruxtecan；14 張中 13→14 張有效，`my-lic-20261112-trastuzumab-1` 同 id 重發）、
  ofloxacin（Ducressa MAL23076003ACZ；142→143 張有效）、calcium_pantothenate、sodium_phosphate、vitamin_d（後三個沒有藥物頁）。trastuzumab 頁收 Enhertu／Kadcyla、ofloxacin 頁收 levofloxacin 產品，是原收集器依藥名子字串比對的既有規則，照舊。
- 同日修 `src/mytxgnn/regulatory/count_prose.py`：「1 sah dan 1 dibatalkan」的第一個數字被當成註銷數（中間跳過 sah），ambroxol 會被改成「0 sah dan 0 dibatalkan」；註銷角色的中間字不能是 sah／aktif 或數字。
