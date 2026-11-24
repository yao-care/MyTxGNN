---
noindex: true
sitemap: false
layout: default
title: Bismuth Subgallate
parent: Low Evidence (L4-L5)
nav_order: 154
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-24
predicted_indications: []
---

# Bismuth Subgallate
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

## Bismuth Subgallate: Laporan Penilaian Penambahan Kegunaan Ubat
{: .text-alpha }

## Ringkasan Satu Ayat

Bismuth Subgallate (DrugBank: DB13909) adalah sebatian bismut yang sedang dipasarkan di Malaysia dengan 1 produk berdaftar. Tiada petunjuk kegunaan baru yang telah dijangka oleh model TxGNN pada masa ini, dan jurang data kritikal — termasuk mekanisme tindakan, teks petunjuk kegunaan yang diluluskan, dan maklumat keselamatan — menghalang penilaian penambahan kegunaan yang bermakna.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|------|
| Petunjuk Kegunaan Asal | Tidak tersedia (medan petunjuk kegunaan lesen adalah kosong) |
| Petunjuk Kegunaan yang Dijangka | Tiada (tiada ramalan TxGNN dihasilkan) |
| Skor Ramalan TxGNN | N/A |
| Aras Bukti | N/A — Tiada ramalan untuk dinilai |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 1 daripada 1) |
| Bilangan Pendaftaran | 1 (sah: 1) |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Buat masa ini **tiada ramalan TxGNN** tersedia untuk Bismuth Subgallate. Tatasusunan `predicted_indications` adalah kosong, bermakna model sama ada tidak menghasilkan calon penambahan kegunaan untuk ubat ini atau saluran paip ramalan belum dijalankan untuknya.

Selain itu, data mekanisme tindakan (MOA) yang terperinci tidak tersedia. Bismuth subgallate adalah garam bismut yang diketahui dalam farmakologi am untuk sifat astringent dan haemostatic, tetapi tanpa entri MOA yang disahkan dalam pakej bukti, penalaran mekanik untuk sebarang petunjuk kegunaan baru yang berpotensi tidak dapat ditubuhkan.

Sebelum sebarang penilaian penambahan kegunaan dapat diteruskan, ubat mesti terlebih dahulu lulus melalui saluran paip ramalan TxGNN dengan pemetaan nod KG-ke-DrugBank yang berjaya, dan jurang data asas (MOA, petunjuk kegunaan yang diluluskan, profil keselamatan) mesti diselesaikan.

---

## Bukti Uji Kaji Klinikal

Buat masa ini tiada uji kaji klinikal yang berkaitan berdaftar — tiada petunjuk kegunaan yang dijangka tersedia untuk dicari.

---

## Bukti Literatur

Buat masa ini tiada literatur yang berkaitan tersedia — tiada petunjuk kegunaan yang dijangka tersedia untuk dicari.

---

## Maklumat Pasaran Malaysia

<!-- licenses:begin -->

| No. Pendaftaran | Nama Produk (NPRA, bahasa asal) | Jenis | Pemegang Pendaftaran | Status |
|------|------|------|------|------|
| MAL19921538AZ | ROWATANAL CREAM | Kombinasi | DCH AURIGA (MALAYSIA) SDN. BHD. | Sah |

<!-- licenses:end -->

<!-- review:begin my-lic-20261124b-bismuth_subgallate-1 -->

> **Pembetulan semakan (2026-11-24)**: Asalnya dinyatakan: "**Nota:** Satu lesen dicatat dalam pangkalan data NPRA, tetapi semua medan perincian (nombor lesen, nama produk, bentuk dos, petunjuk kegunaan yang diluluskan) adalah kosong dalam pakej bukti semasa. Ini perlu diambil daripada portal NPRA." Dipadam: ayat ini menerangkan keadaan pakej bukti semasa laporan ditulis (medan butiran pendaftaran kosong); jadual pendaftaran NPRA dalam bahagian ini kini dijana oleh program daripada data pendaftaran produk NPRA (data.gov.my) dan mengandungi nombor pendaftaran, nama produk, pemegang pendaftaran dan status. Bilangan pendaftaran semasa terdapat dalam Gambaran Ringkas halaman ini. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261124b-bismuth_subgallate-1 -->

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat-ubat) buat masa ini tidak tersedia. Pertanyaan DrugBank DDI tidak mengembalikan hasil apa pun. Profil keselamatan lengkap mesti diperolehi daripada sisipan pakej produk atau pangkalan data NPRA sebelum sebarang penilaian penambahan kegunaan dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan penambahan kegunaan TxGNN telah dihasilkan untuk Bismuth Subgallate, dan beberapa jurang data penyekat wujud. Tanpa petunjuk kegunaan yang dijangka, tiada apa pun untuk dinilai bagi kemasukakalan klinikal atau sokongan bukti.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Jalankan saluran paip ramalan TxGNN** — Sahkan bahawa DB13909 dipetakan ke nod yang sah dalam graf pengetahuan; jika pemetaan gagal, siasat ID DrugBank alternatif atau bentuk garam
2. **Ambil data MOA** (Jurang Data DG002, keseriusan: Tinggi) — Pertanyaan DrugBank API untuk farmakodinamik dan mekanisme tindakan
3. **Ambil butiran lesen NPRA** — Perolehi maklumat pendaftaran lengkap (nombor lesen, nama produk, bentuk dos, teks petunjuk kegunaan yang diluluskan) daripada portal NPRA
4. **Ambil maklumat keselamatan** (Jurang Data DG001, keseriusan: Menyekat) — Muat turun dan huraikan PDF sisipan pakej daripada pihak berkuasa kawal selia untuk amaran, kontraindikasi, dan tindakan berjaga-jaga
5. **Nilai semula** setelah hasil ramalan dan data asas tersedia

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penambahan kegunaan ubat memerlukan pengesahan klinikal sebelum aplikasi.*

<!-- review:begin log -->

## Rekod Semakan

Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA (data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan tidak ditulis semula.

| Tarikh semakan | Perkara | Tindakan | Sumber |
|------|------|------|------|
| 2026-11-24 | Dipadam: "**Nota:** Satu lesen dicatat dalam pangkalan data NPRA, tetapi semua medan perincian (nombor lesen, nama produk, bentuk dos, petunjuk kegunaan yang diluluskan) adalah kosong dalam pakej bukti semasa. Ini perlu diambil daripada portal NPRA." | Dibetulkan | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |

<!-- review:end log -->

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

