---
noindex: true
sitemap: false
layout: default
title: Atovaquone
parent: Low Evidence (L4-L5)
nav_order: 106
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-24
predicted_indications: []
---

# Atovaquone
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **0** 
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

## Atovaquone: Penilaian Penggunaan Semula Ubat Tertangguh — Data Tidak Mencukupi, Analisis Lengkap Tidak Dapat Dilakukan
{: .text-alpha }

---

## Ringkasan Satu Ayat

Atovaquone adalah ubat antiparasit yang digunakan secara meluas untuk rawatan dan pencegahan pneumonia *Pneumocystis jirovecii* (PCP), serta penyakit toksoplasma dan pencegahan malaria (digunakan bersama proguanil).
Walau bagaimanapun, dalam Evidence Pack ini, **medan indikasi yang diprediksi oleh TxGNN kosong**, dan rekod indikasi asal, mekanisme tindakan dan maklumat keselamatan semuanya mempunyai jurang kritis, **penilaian penggunaan semula ubat yang lengkap tidak dapat dilakukan**.
Disyorkan untuk melengkapkan data dan melaksanakan semula proses ramalan, kemudian melakukan penilaian rasmi.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak dicatat dalam Evidence Pack (berdasarkan pengetahuan umum: rawatan/pencegahan PCP, penyakit toksoplasma, pencegahan malaria) |
| Indikasi Baru yang Diprediksi | **Tiada** (`predicted_indications` ialah tatasusunan kosong) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A (Tiada hasil ramalan) |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 1 daripada 1) |
| Bilangan Pendaftaran | 1 (sah: 1) |
| Keputusan yang Disyorkan | **Tahan** |

---

## Maklumat Pasaran Malaysia

Pertanyaan NPRA mengembalikan 1 pendaftaran Dipasarkan.

<!-- licenses:begin -->

| No. Pendaftaran | Nama Produk (NPRA, bahasa asal) | Jenis | Pemegang Pendaftaran | Status |
|------|------|------|------|------|
| MAL20014470ACRZ | MALARONE TABLETS | Kombinasi | GLAXOSMITHKLINE PHARMACEUTICAL SDN. BHD. | Sah |

<!-- licenses:end -->

<!-- review:begin my-lic-20261124b-atovaquone-1 -->

> **Pembetulan semakan (2026-11-24)**: Asalnya dinyatakan: ", tetapi Evidence Pack ini belum mendapatkan medan pendaftaran terperinci (nama produk, bentuk dos, indikasi yang diluluskan, dll.)." Dibetulkan: bahagian ayat ini yang menerangkan keadaan pakej bukti semasa laporan ditulis (medan butiran pendaftaran kosong) dipadam, kerana jadual pendaftaran NPRA dalam bahagian ini kini dijana oleh program daripada data pendaftaran produk NPRA (data.gov.my) dan mengandungi nombor pendaftaran, nama produk, pemegang pendaftaran dan status. Bilangan pendaftaran semasa terdapat dalam Gambaran Ringkas halaman ini. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261124b-atovaquone-1 -->

<!-- review:begin my-lic-20261124b-atovaquone-2 -->

> **Pembetulan semakan (2026-11-24)**: Asalnya dinyatakan: "dan isikan jadual di atas." Dibetulkan: premis bahawa nombor pendaftaran dan nama produk belum tersedia telah dipadam (kini disenaraikan dalam jadual pendaftaran NPRA yang dijana oleh program daripada data pendaftaran produk NPRA, data.gov.my); cadangan tindakan lain tidak diubah. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261124b-atovaquone-2 -->

> **Langkah Pemulihan**: Melalui antara muka pertanyaan rasmi NPRA, dapatkan maklumat produk lengkap menggunakan nombor pendaftaran.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan bungkusan untuk maklumat keselamatan.

> Medan keselamatan Evidence Pack ini (amaran, kontraindikasi, interaksi ubat) semuanya merupakan jurang data, belum diperoleh daripada sisipan produk atau DrugBank.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Evidence Pack Atovaquone ini mempunyai beberapa jurang kritis — hasil ramalan TxGNN hilang, indikasi asal tidak dicatat, mekanisme tindakan belum diperoleh, amaran keselamatan dan kontraindikasi belum diisi, proses penilaian tidak dapat diteruskan.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Blocking — DG001]** Muat turun dan analisis PDF sisipan produk NPRA/TFDA, dapatkan amaran keselamatan dan kontraindikasi, untuk menghapuskan sekatan penilaian keselamatan awal S1
- **[High — DG002]** Pertanyaan API DrugBank untuk mekanisme tindakan (MOA) DB01117, untuk menyokong analisis kaitan mekanisme
- **Laksanakan semula proses ramalan TxGNN**, hasilkan senarai calon indikasi baru untuk Atovaquone (DB01117) (`predicted_indications`)
- **Lengkapkan maklumat pendaftaran NPRA terperinci**: Dapatkan nama produk, bentuk dos, teks penuh indikasi yang diluluskan
- Setelah data dilengkapkan, janakan semula laporan mengikut spesifikasi Evidence Pack v4, jalankan penarafan bukti L1–L5 lengkap dan analisis keputusan

---

> ⚠️ **Penafian YMYL**: Hasil laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan sebarang nasihat perubatan. Ubat calon penggunaan semula ubat mesti melalui pengesahan klinikal rasmi sebelum dapat digunakan dalam keputusan penjagaan kesihatan sebenarnya.

<!-- review:begin log -->

## Rekod Semakan

Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA (data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan tidak ditulis semula.

| Tarikh semakan | Perkara | Tindakan | Sumber |
|------|------|------|------|
| 2026-11-24 | Dipadam: ", tetapi Evidence Pack ini belum mendapatkan medan pendaftaran terperinci (nama produk, bentuk dos, indikasi yang diluluskan, dll.)." | Dibetulkan | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |
| 2026-11-24 | Dipadam: "dan isikan jadual di atas." | Dibetulkan | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |

<!-- review:end log -->

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

