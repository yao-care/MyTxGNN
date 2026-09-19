---
layout: default
title: Bleomycin Sulfate
parent: Low Evidence (L4-L5)
nav_order: 151
evidence_level: L5
indication_count: 0
---

# Bleomycin Sulfate
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

# Bleomycin Sulfate: Laporan Penilaian Penyalahgunaan Semula Ubat

## Ringkasan Satu Ayat

Bleomycin Sulfate ialah antibiotik glikopeptida antineoplastik yang dipasarkan dan secara sejarah digunakan dalam rawatan pelbagai keganasan termasuk limfoma, karsinoma sel skuamosa, dan kanser testis. Model TxGNN **masih belum menjana indikasi baru yang diramalkan** untuk ubat ini, dan Pakej Bukti pada masa kini mengandungi jurang data yang signifikan dalam butiran kawal selia, maklumat keselamatan, dan mekanisme tindakan.

---

## Ikhtisar Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tersedia dalam set data semasa (penggunaan yang diketahui: limfoma, karsinoma sel skuamosa, kanser testis) |
| Indikasi Baru yang Diramalkan | **Tiada — tiada ramalan TxGNN tersedia** |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | **L5** (Tiada ramalan model atau kajian sokongan dalam set data ini) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa kini, tiada ramalan TxGNN telah dijana untuk Bleomycin Sulfate. Medan `predicted_indications` adalah kosong, bermakna graf pengetahuan dan model pembelajaran mendalam belum mengembalikan indikasi calon untuk penilaian penyalahgunaan semula.

Bleomycin Sulfate ialah antibiotik sitotoksik yang mantap yang menjalankan kesan antineoplastiknya dengan mengikat DNA dan mencetuskan pecutus satu dan dua helai melalui mekanisme radikal bebas yang bergantung kepada besi. Penggunaan klinikalnya merangkumi limfoma Hodgkin (sebagai sebahagian daripada rejimen ABVD), karsinoma sel skuamosa kepala dan leher, serviks dan vulva, tumor sel benih testis, dan keselurusan pleura ganas (sebagai agen penyerotan). Data mekanisme tindakan terperinci tidak disertakan dalam Pakej Bukti semasa dan ditandakan sebagai jurang data keterukan tinggi (DG002).

Sebelum ramalan penyalahgunaan semula yang bermakna dapat dijana, data prasyarat berikut mesti diisi: pemetaan ID DrugBank, teks indikasi yang diluluskan daripada lesen kawal selia, dan butiran mekanisme tindakan. Tanpa input ini, model TxGNN tidak dapat menghasilkan indikasi calon yang boleh dipercayai.

---

## Bukti Uji Klinikal

Pada masa kini tiada uji klinikal berkaitan TxGNN tersedia, kerana tiada indikasi yang diramalkan telah dijana.

---

## Bukti Kesusasteraan

Pada masa kini tiada kesusasteraan berkaitan TxGNN tersedia, kerana tiada indikasi yang diramalkan telah dijana.

---

## Maklumat Pasaran Malaysia

Bleomycin Sulfate mempunyai **2 lesen berdaftar** dengan status pasaran "Dipasarkan" (Dipasarkan). Walau bagaimanapun, maklumat pendaftaran terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak tersedia dalam set data semasa.

> **Nota:** Butiran lesen perlu diambil dari pangkalan data NPRA untuk melengkapkan bahagian ini.

---

## Sitotoksisiti

Bleomycin Sulfate ialah agen antineoplastik sitotoksik konvensional. Maklumat berikut adalah berdasarkan pengetahuan farmakoloji yang mantap:

| Item | Kandungan |
|------|----------|
| Klasifikasi Sitotoksisiti | Sitotoksik konvensional (Antibiotik glikopeptida / agen perosakan DNA) |
| Risiko Supresi Sumsum Tulang | **Rendah** (Bleomycin adalah ketara pada sumsum tulang berbanding sitotoksik lain; supresi sumsum tulang jarang berlaku) |
| Klasifikasi Emetogenisiti | **Rendah** |
| Item Pemantauan | **Ujian fungsi paru-paru** (DLCO, CXR — toksisiti paru-paru ialah had dos); fungsi buah pinggang (pembuangan kreatinin, kerana gangguan buah pinggang meningkatkan risiko toksisiti paru-paru); CBC; fungsi hati |
| Perlindungan Pengendalian | Mesti mematuhi peraturan pengendalian ubat sitotoksik (pemindahan sistem tertutup, PPE, almari keselamatan biologi) |

> ⚠️ **Nota Keselamatan Kritikal:** Bleomycin membawa risiko yang diketahui dengan baik iaitu **fibrosis paru-paru**, yang kumulatif dan bergantung dos (biasanya pada dos kumulatif >400 unit). Fungsi paru-paru mesti dipantau sepanjang rawatan. Sila rujuk sisipan paket untuk amaran dan berjaga-jaga penuh.

---

## Pertimbangan Keselamatan

Data keselamatan terperinci (amaran utama, kontraindikasi, dan interaksi ubat-ubatan) tidak tersedia dalam Pakej Bukti semasa. Ini ditandakan sebagai jurang data penyekat (DG001).

> Sila rujuk sisipan paket untuk maklumat keselamatan. Sebagai keutamaan, PDF sisipan paket TFDA harus diambil dan dianalisis untuk mengisi amaran dan kontraindikasi.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan TxGNN telah dijana untuk Bleomycin Sulfate, dan Pakej Bukti mengandungi jurang data kritikal (ID DrugBank, teks indikasi yang diluluskan, MOA, amaran keselamatan). Terdapat data yang tidak mencukupi untuk menilai sebarang peluang penyalahgunaan semula pada masa kini.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Pemetaan ID DrugBank** — Soal API DrugBank untuk Bleomycin Sulfate (dijangka: [DB00290](https://go.drugbank.com/drugs/DB00290)) dan isikan `drugbank_id`
2. **Butiran lesen kawal selia** — Ambil maklumat pendaftaran penuh daripada NPRA (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan)
3. **Mekanisme tindakan (MOA)** — Ambil daripada DrugBank untuk membolehkan analisis kebolehpercayaan mekanik (DG002)
4. **Data keselamatan sisipan paket** — Muat turun dan analisis PDF sisipan paket TFDA untuk mengekstrak amaran dan kontraindikasi (DG001, Penyekat)
5. **Jalankan semula saluran ramalan TxGNN** — Setelah ID DrugBank dan pemetaan indikasi diisi, laksanakan `run_kg_prediction.py` untuk menjana calon penyalahgunaan semula
6. **Pengumpulan bukti** — Selepas ramalan tersedia, jalankan pengumpul ClinicalTrials.gov dan PubMed untuk mengumpul bukti sokongan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

