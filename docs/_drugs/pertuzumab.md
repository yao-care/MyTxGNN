---
layout: default
title: Pertuzumab
parent: High Evidence (L1-L2)
nav_order: 568
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Pertuzumab: indikasi baharu diramal Karsinoma payudara positif HER2 (tahap bukti L1). Indikasi asal: Tiada rekod dalam data yang dikumpulkan (lesen tiada)"
monitor_inn: "Pertuzumab"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma"]
---

# Pertuzumab
{: .fs-9 }

Tahap bukti: **L1** | Indikasi diramal: **10** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Laporan penilaian ahli farmasi

</div>

# Pertuzumab: Daripada Indikasi Asal yang Tidak Direkodkan kepada Karsinoma Payudara Positif HER2

## Ringkasan Satu Ayat

Data pendaftaran tempatan tidak merekodkan indikasi asal bagi pertuzumab, iaitu antibodi monoklonal yang menyasarkan reseptor HER2.
Model TxGNN meramalkan ia mungkin berkesan untuk **karsinoma payudara positif HER2**, dan ramalan ini disokong oleh **banyak percubaan klinikal** serta **literatur** termasuk RCT fasa 3 (CLEOPATRA, APHINITY).
Perlu diingat bahawa ini sebenarnya penggunaan yang sudah mantap dan disokong garis panduan, jadi ia bukan calon repurposing yang sebenar. Status "tidak dipasarkan" dan ketiadaan indikasi asal dalam data kemungkinan besar merupakan jurang data.

---

## Gambaran Ringkas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Tiada rekod dalam data yang dikumpulkan (lesen tiada) |
| Indikasi Baharu yang Diramalkan | Karsinoma payudara positif HER2 |
| Skor Ramalan TxGNN | 99.97% |
| Tahap Bukti | L1 |
| Status Pasaran di Malaysia | Tidak dipasarkan (menurut data yang dikumpulkan) |
| Bilangan Pendaftaran | 0 |
| Keputusan Disyorkan | Proceed with Guardrails |

---

## Mengapa Ramalan Ini Munasabah?

Pertuzumab ialah perencat pendimeran HER2. Ia mengikat subdomain II HER2 dan menghalang pembentukan heterodimer HER2-HER3. Ini melengkapi trastuzumab yang mengikat subdomain IV. Gabungan kedua-duanya (dwi-sekatan) menekan isyarat hiliran PI3K/AKT dan MAPK dalam tumor yang didorong oleh HER2. Data farmakologi juga mengesahkan sasarannya ialah ERBB2.

Mekanisme ini sepadan secara langsung dengan biologi penyakit. Skor TxGNN yang sangat tinggi (0.9997) selaras dengan rekod klinikal: pertuzumab bersama trastuzumab dan kemoterapi telah menjadi rawatan piawai untuk kanser payudara positif HER2, sama ada peringkat awal (NeoSphere, APHINITY) mahupun metastatik (CLEOPATRA).

Indikasi asal tidak tersedia dalam data lesen tempatan, maka perbandingan rasmi antara indikasi asal dengan indikasi baharu tidak dapat dibuat.

**Ramalan lain dalam kedudukan teratas (ringkasan):**
- **Kanser payudara positif reseptor progesteron / negatif reseptor progesteron / luminal B:** manfaat bergantung pada status HER2, bukan status PR. Bukti hanya terpakai untuk subset HER2-positif. Terdapat RCT fasa 3 (QL1209 biosimilar, PMID 38906970) dan percubaan WSG TP-II serta PERTAIN untuk subset HR+/HER2+.
- **Subjenis payudara seakan-normal, ektomesenkimoma, tumor sel granular kulit malignan, tumor berkaitan HHV-8, tumor neuroendokrin telinga tengah:** tiada percubaan atau literatur dan tiada rasional mekanistik yang jelas. Keputusan: Hold.
- **Karsinoma urotelium uretra prostat:** HER2 boleh berlebihan dalam sebahagian kes, tetapi tiada bukti khusus. Ia setakat persoalan penyelidikan sahaja dan memerlukan pengesahan biopenanda HER2.

---

## Bukti Percubaan Klinikal

Senarai di bawah ialah percubaan yang paling relevan bagi indikasi teratas (karsinoma payudara positif HER2).

| Nombor Percubaan | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Fasa 3 | Selesai | 315 | TCHP neoadjuvan dengan atau tanpa penafian estrogen dalam HR+/HER2+ |
| [NCT04957212](https://clinicaltrials.gov/study/NCT04957212) | Fasa 3 | Selesai | 214 | Kesetaraan biosimilar pertuzumab CinnaGen berbanding Perjeta (neoadjuvan) |
| [NCT05296798](https://clinicaltrials.gov/study/NCT05296798) | Fasa 3 | Aktif, tidak merekrut | 922 | Giredestrant + Phesgo berbanding Phesgo dalam HER2+/ER+ lanjutan (bukti tidak langsung untuk pertuzumab) |
| [NCT04784715](https://clinicaltrials.gov/study/NCT04784715) | Fasa 3 | Aktif, tidak merekrut | 1157 | DESTINY-Breast09: T-DXd ± pertuzumab berbanding taksan + trastuzumab + pertuzumab, lini pertama metastatik |
| [NCT01491737](https://clinicaltrials.gov/study/NCT01491737) | Fasa 2 | Selesai | 258 | Pertuzumab + trastuzumab + perencat aromatase lini pertama HER2+/HR+ |
| [NCT03272477](https://clinicaltrials.gov/study/NCT03272477) | Fasa 2 | Selesai | 257 | Trastuzumab + pertuzumab dengan paklitaksel atau terapi endokrin sebelum pembedahan (HER2+/HR+) |
| [NCT02132949](https://clinicaltrials.gov/study/NCT02132949) | Fasa 2 | Selesai | 401 | Pertuzumab + trastuzumab + kemoterapi berasaskan antrasiklin neoadjuvan |
| [NCT02445586](https://clinicaltrials.gov/study/NCT02445586) | Fasa 4 | Selesai | 52 | Pertuzumab + trastuzumab + docetaxel lini pertama pesakit India, kajian lengan tunggal |
| [NCT00875979](https://clinicaltrials.gov/study/NCT00875979) | Fasa 1b/2 | Selesai | 67 | T-DM1 + pertuzumab, data keselamatan dan keberkesanan langsung |
| [NCT02536339](https://clinicaltrials.gov/study/NCT02536339) | Fasa 2 | Selesai | 40 | PATRICIA: pertuzumab + trastuzumab dos tinggi untuk perkembangan CNS selepas radioterapi |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [23602601](https://pubmed.ncbi.nlm.nih.gov/23602601/) | 2013 | RCT | Lancet Oncol | CLEOPATRA: keputusan survival keseluruhan pertuzumab + trastuzumab + docetaxel dalam HER2+ metastatik lini pertama |
| [33539215](https://pubmed.ncbi.nlm.nih.gov/33539215/) | 2021 | RCT | J Clin Oncol | APHINITY: susulan 6 tahun, pertuzumab tambahan adjuvan dalam HER2+ awal |
| [39259927](https://pubmed.ncbi.nlm.nih.gov/39259927/) | 2024 | RCT | J Clin Oncol | APHINITY: analisis interim ketiga survival keseluruhan |
| [22153890](https://pubmed.ncbi.nlm.nih.gov/22153890/) | 2012 | RCT | Lancet Oncol | NeoSphere: pertuzumab + trastuzumab neoadjuvan dalam HER2+ |
| [29175149](https://pubmed.ncbi.nlm.nih.gov/29175149/) | 2018 | RCT | Lancet Oncol | KRISTINE: rejimen neoadjuvan T-DM1 + pertuzumab berbanding kemoterapi + trastuzumab + pertuzumab |
| [23704196](https://pubmed.ncbi.nlm.nih.gov/23704196/) | 2013 | RCT | Ann Oncol | TRYPHAENA: keselamatan jantung dengan rejimen berasaskan antrasiklin dan tanpa antrasiklin |
| [29253081](https://pubmed.ncbi.nlm.nih.gov/29253081/) | 2018 | RCT | Ann Oncol | BERENICE: keselamatan jantung neoadjuvan |
| [36716289](https://pubmed.ncbi.nlm.nih.gov/36716289/) | 2023 | Kajian klinikal | Clin Cancer Res | PERTAIN: analisis akhir pertuzumab + trastuzumab + perencat aromatase dalam HER2+/HR+ |
| [27939064](https://pubmed.ncbi.nlm.nih.gov/27939064/) | 2017 | Ulasan | Lancet | Ulasan rawatan anti-HER2 dalam kanser payudara HER2+ |
| [32721042](https://pubmed.ncbi.nlm.nih.gov/32721042/) | 2020 | Ulasan | Cancer | Terapi baharu bersasar HER2 untuk HER2+ metastatik |

---

## Maklumat Pasaran Malaysia

Data yang dikumpulkan tidak menemui sebarang lesen pertuzumab yang berdaftar di Malaysia (jumlah pendaftaran: 0, status: tidak dipasarkan). Ini bercanggah dengan penggunaan klinikal global yang mantap, justeru ia perlu disahkan semula terus dengan NPRA.

---

## Sitotoksisiti

| Perkara | Kandungan |
|------|------|
| Klasifikasi Sitotoksisiti | Terapi bersasar (antibodi monoklonal anti-HER2), bukan sitotoksik konvensional |
| Risiko Mielosupresi | Rendah bagi agen tunggal; risiko meningkat apabila digabungkan dengan kemoterapi (contohnya docetaxel) |
| Klasifikasi Emetogenisiti | Rendah |
| Item Pemantauan | Fungsi jantung (LVEF), hitung darah lengkap apabila bersama kemoterapi, fungsi hati dan buah pinggang |
| Perlindungan Pengendalian | Sila rujuk panduan institusi dan insert pakej |

Keselamatan jantung merupakan fokus beberapa kajian (TRYPHAENA, BERENICE), terutamanya apabila digabungkan dengan antrasiklin.

---

## Pertimbangan Keselamatan

- **Interaksi Ubat**: Interaksi **sederhana** dengan **idelalisib** dilaporkan (sumber: ddinter). Jumlah interaksi yang direkodkan: 2, termasuk entri farmakologi sasaran ERBB2 yang bukan interaksi ubat-ubat klinikal.

Maklumat amaran dan kontraindikasi lain tidak tersedia; sila rujuk insert pakej.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Proceed with Guardrails**

**Rasional:**
- Beberapa RCT fasa 3 (CLEOPATRA, APHINITY, KRISTINE) serta pelbagai kajian fasa 2 menyokong penggunaan pertuzumab dalam kanser payudara positif HER2, dan mekanismenya sepadan secara langsung. Penggunaan ini sudah mantap, tetapi data pendaftaran tempatan yang tidak lengkap memerlukan pengesahan.

**Untuk diteruskan, perlu dilengkapkan:**
- Mengesahkan status pendaftaran sebenar di NPRA (data yang dikumpulkan menunjukkan 0 lesen, kemungkinan jurang data) serta memuat turun inset pakej untuk amaran dan kontraindikasi (jurang data yang menghalang saringan keselamatan).
- Data mekanisme tindakan terperinci daripada DrugBank.
- Pengesahan status HER2 melalui IHC/FISH sebelum penggunaan; bukti tidak menyokong penyakit HER2-negatif.
- Pelan pemantauan jantung (LVEF) dan pertimbangan bagi populasi khas (contohnya kehamilan).
- Bagi indikasi ramalan lain tanpa bukti (L5), kekalkan status Hold; karsinoma urotelium uretra prostat memerlukan pengesahan biopenanda HER2 dan penyelidikan praklinikal atau fasa awal.
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

