---
layout: default
title: Alectinib Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 37
evidence_level: L5
indication_count: 0
---

# Alectinib Hydrochloride
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **0** 
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

# Alectinib Hydrochloride: Daripada Kanser Paru Sel Bukan Kecil ALK+ kepada [Tiada Ramalan Penyalahgunaan Ubat Dijana]

## Ringkasan Satu Ayat

Alectinib hydrochloride adalah inhibitor kinase tirosin ALK/RET yang terpilih dengan indikasi yang sudah mapan dalam kanser paru sel bukan kecil positif ALK (NSCLC), dan dikonfirmasi sebagai produk yang dipasarkan di Malaysia dengan 1 lesen terdaftar.
Walau bagaimanapun, Pakej Bukti semasa tidak mengandungi **ramalan penyalahgunaan ubat yang dijana oleh TxGNN** untuk sebatian ini, kerana data upstream utama — termasuk ID DrugBank, teks indikasi yang diluluskan, dan maklumat keselamatan — tidak berjaya diambil semula.
Penilaian penyalahgunaan ubat yang menyeluruh **tidak dapat diselesaikan** sehingga jurang data ini diselesaikan dan saluran ramalan dijalankan semula.

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|------|---------|
| Indikasi Asal | Tidak diisi dalam data semasa (diketahui daripada latar belakang: NSCLC positif ALK) |
| Indikasi Baru yang Diramalkan | Tiada ramalan dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan (Marketed) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Latar Belakang dan Status Data

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia dalam Pakej Bukti. Berdasarkan maklumat yang diketahui, alectinib adalah inhibitor kinase ALK (Anaplastic Lymphoma Kinase) dan RET yang terpilih dan diberikan secara oral. Keberkesanannya dalam NSCLC positif ALK telah ditetapkan dengan baik melalui ujian Fasa 3 utama (contohnya, ALEX, J-ALEX, ALESIA), menunjukkan kelangsungan hidup tanpa perkembangan yang lebih baik berbanding crizotinib, termasuk aktiviti terhadap metastasis sistem saraf pusat.

Langkah ramalan graf pengetahuan TxGNN tidak menghasilkan sebarang calon indikasi penyalahgunaan dalam larian semasa. Ini kemungkinan besar disebabkan oleh medan `drugbank_id: null` yang belum diselesaikan — ID DrugBank diperlukan sebagai pengecam nod dalam graf pengetahuan, dan ketiadaannya menghalang TxGNN daripada mengira skor persamaan terhadap nod penyakit.

Setelah pemetaan DrugBank dipulihkan (DB ID: DB11363 untuk alectinib) dan saluran dijalankan semula, calon penyalahgunaan yang boleh dipercayai secara biologi mungkin termasuk keganasan lain yang didorong oleh ALK seperti limfoma sel besar anaplastik (ALCL), tumor mikofibroblastik radang (IMT), dan neuroblastoma — semuanya mengekspresikan berlebihan atau mengandungi fusi ALK. Walau bagaimanapun, calon-calon ini mesti diskor secara formal oleh TxGNN sebelum penilaian dapat diteruskan.

---

## Sitotoksisiti

| Perkara | Kandungan |
|------|---------|
| Pengelasan Sitotoksisiti | Terapi yang disasarkan — inhibitor kinase tirosin ALK/RET yang terpilih (generasi kedua) |
| Risiko Penindasan Sum-sum | Rendah hingga sederhana; anemia dan neutropenia dilaporkan tetapi kurang kerap daripada sitostatik konvensional |
| Pengelasan Emetogenisiti | Rendah (ejen oral; mual dilaporkan dalam ~18% pesakit) |
| Item Pemantauan | CBC dengan pembezaan, ujian fungsi hati (ALT/AST/bilirubin), fungsi buah pinggang, fungsi paru, ECG (QTc), CPK (risiko rhabdomiolisis/myalgia) |
| Perlindungan Pengendalian | Bentuk dos pepejal oral; langkah perlindungan pengendalian standard untuk terapi sasaran oral dikenakan; elakkan menghancurkan kapsul tanpa pembendungan |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> **Nota:** Kedua-dua amaran utama dan kontraindikasi disenaraikan sebagai jurang data dalam Pakej Bukti semasa (DG001: Keterukan — Menyekat). Tiada data interaksi ubat-ubatan diambil semula (status pertanyaan: not_found). Penilaian keselamatan penuh disekat sehingga sisipan produk diambil semula dan dianalisis.

---

## Maklumat Pasaran Malaysia

Pakej Bukti mengesahkan **1 pendaftaran aktif** dengan status pasaran **✓ Dipasarkan (Marketed)**. Walau bagaimanapun, semua medan rekod lesen (nombor lesen, nama produk, bentuk dos, pengilang, dan teks indikasi yang diluluskan) dikembalikan sebagai rentetan kosong dan tidak dapat diisi dalam laporan ini.

> **Tindakan diperlukan:** Soal pangkalan data Pendaftaran Produk NPRA secara langsung di [https://www.npra.gov.my](https://www.npra.gov.my) menggunakan istilah carian "ALECTINIB" untuk memperoleh rekod pendaftaran penuh dan teks indikasi yang diluluskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Saluran ramalan tidak menghasilkan sebarang calon penyalahgunaan TxGNN untuk alectinib, kemungkinan besar disebabkan oleh ID DrugBank yang hilang yang menghalang ubat daripada terletak sebagai nod dalam graf pengetahuan. Tanpa ramalan yang diskor, tiada penilaian penyalahgunaan berasaskan bukti dapat dijalankan.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Kritikal — DG001]** Ambil semula sisipan produk Malaysia (PI/SmPC) daripada pangkalan data NPRA untuk mengisi indikasi yang diluluskan, amaran, dan kontraindikasi
- **[Kritikal — DG002]** Selesaikan `drugbank_id: null` — ID DrugBank yang disahkan ialah **DB11363**; kemaskini jadual pemetaan dan jalankan semula `scripts/run_kg_prediction.py`
- **[Kritikal]** Jalankan semula saluran ramalan TxGNN penuh selepas pemetaan DrugBank dipulihkan; calon penyalahgunaan yang dijangka termasuk tumor yang didorong ALK di luar NSCLC
- **[Tinggi]** Isikan medan rekod lesen (nama produk, bentuk dos, indikasi yang diluluskan) daripada NPRA untuk melengkapkan bahagian pengawalseliaan
- **[Tinggi]** Setelah ramalan tersedia, kumpul ujian klinikal (ClinicalTrials.gov / ICTRP) dan bukti literatur PubMed untuk indikasi yang diprediksi tertinggi sebelum menjana semula laporan ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

