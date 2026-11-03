---
layout: default
title: "Ubat dengan bukti ujian klinikal untuk indikasi baharu"
parent: Laporan Ubat
nav_order: 5
permalink: /clinical-trial-evidence/
description: "Ubat berdaftar NPRA yang indikasi baharunya, diramalkan oleh TxGNN, mempunyai bukti ujian klinikal (L1-L2): indikasi, tahap bukti, ujian berdaftar."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「lihat laporan」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Indikasi Baharu yang Diramalkan|Indikasi Baharu yang Diramal|Petunjuk Baharu yang Diramalkan|Indikasi Baharu Diramal" | split: "|" -%}
{%- assign lev_labels = "Tahap Bukti" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Ubat di Malaysia dengan bukti ujian klinikal untuk indikasi baharu

<p class="key-answer" data-question="Ubat manakah di Malaysia yang mempunyai bukti ujian klinikal untuk indikasi baharu?">
<strong>{{ trial_drugs.size }}</strong> daripada {{ listed.size }} ubat yang mempunyai laporan MyTxGNN mempunyai indikasi baharu yang diramalkan oleh TxGNN pada tahap bukti <strong>L1 atau L2</strong> ({{ l1.size }} pada L1, {{ l2.size }} pada L2), iaitu bukti ujian klinikal (ujian rawak terkawal, ujian fasa 2–3 atau ulasan sistematik) telah ditemui.
</p>

Ubat-ubat ini diambil daripada data pendaftaran [NPRA](https://npra.gov.my/) (status pendaftaran, Aktif atau Dibatalkan, ditunjukkan dalam setiap laporan ubat); senarai ini mencerminkan laporan ubat yang terakhir dikemas kini pada {{ latest_date }}.

<div class="key-takeaway">
Bukti ujian bagi indikasi yang diramalkan tidak membuktikan keberkesanan. Setiap calon di bawah masih <strong>memerlukan pengesahan klinikal</strong> dan semakan kawal selia sebelum sebarang penggunaan klinikal.
</div>

---

## Ubat dengan bukti ujian (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Ubat</th><th>Indikasi baharu yang diramalkan</th><th>Tahap bukti</th><th>Ujian berdaftar yang dipetik (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}lihat laporan{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(dengan kaveat)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Cara membaca senarai ini

- **Tahap bukti** mengikut [kriteria]({{ '/evidence-high/' | relative_url }}) laman ini: L1 = Multiple Phase 3 RCTs / Systematic Reviews; L2 = Single RCT or multiple Phase 2 trials. "(dengan kaveat)" bermaksud laporan meletakkan syarat pada tahap tersebut; baca nota dalam laporan sebelum bergantung padanya.
- **Indikasi baharu yang diramalkan** ialah ramalan utama setiap laporan. Indikasi dan kontraindikasi yang sudah direkodkan dalam graf pengetahuan TxGNN dikecualikan, tetapi sesetengah ramalan masih boleh bertindih dengan kegunaan sedia ada; laporan menerangkannya jika berkaitan.
- **Ujian berdaftar yang dipetik** mengira nombor ClinicalTrials.gov (NCT) yang dipetik dalam laporan. Laporan memetik sebahagian daripada ujian yang ditemui; 0 bermaksud laporan tidak memetik sebarang ujian berdaftar, dan bahagian bukti literatur menunjukkan asas tahap tersebut.
- Untuk semua tahap dan kaedah penuh, lihat [High Evidence (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Senarai Ubat]({{ '/drugs/' | relative_url }}) dan [metodologi]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Drug repurposing predictions are for research purposes only. These predictions have not been clinically validated and should not be used for medical decisions. Always consult healthcare professionals.
</div>
