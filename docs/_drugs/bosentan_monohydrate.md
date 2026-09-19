---
layout: default
title: Bosentan Monohydrate
parent: Low Evidence (L4-L5)
nav_order: 155
evidence_level: L5
indication_count: 0
---

# Bosentan Monohydrate
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

# Bosentan Monohydrate: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu Ayat

Bosentan ialah antagonis reseptor endothelin (ERA) yang diindikasikan terutamanya untuk hipertension arteri pulmonari (PAH). Pakej Bukti semasa mengandungi **tiada indikasi baru yang diramalkan** daripada model TxGNN, dan jurang data kritikal (ID DrugBank, mekanisme tindakan, teks indikasi yang diluluskan, data keselamatan) mesti diselesaikan sebelum sebarang penilaian penggunaan semula dapat diteruskan.

---

## Gambaran Keseluruhan

| Item | Kandungan |
|------|------|
| Nama Ubat (INN) | Bosentan Monohydrate |
| Indikasi Asal | *(Tidak disediakan dalam pakej bukti — lihat Jurang Data di bawah)* |
| Indikasi Baru yang Diramalkan | **Tiada** (tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **N/A** — Tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 5 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada **indikasi yang diramalkan oleh TxGNN** dalam Pakej Bukti ini, jadi penilaian kebolehplausibilan berdasarkan mekanisme tidak dapat dilakukan pada masa ini.

Berdasarkan pengetahuan farmaseutikal umum, Bosentan Monohydrate ialah antagonis reseptor endothelin dwi (ET~A~ dan ET~B~) yang menghalang kesan vasokonstriktif dan proliferatif endothelin-1. Ia sudah terkenal dalam rawatan hipertension arteri pulmonari (PAH) dan juga telah diluluskan di beberapa bidang kuasa untuk mengurangkan bilangan ulser digital baharu pada pesakit skleroderma sistemik. Walau bagaimanapun, konteks mekanistik ini bukan bersumber daripada Pakej Bukti itu sendiri, dan medan `original_moa` tetap tidak diselesaikan.

Sebelum sebarang calon penggunaan semula dapat dinilai, saluran ramalan TxGNN mesti dijalankan dengan pemetaan ID DrugBank yang sah untuk Bosentan, dan indikasi yang diramalkan yang terhasil mesti diisi ke dalam pakej bukti.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada indikasi yang diramalkan tersedia; oleh itu, tiada carian percubaan klinikal yang disasarkan telah dijalankan.

---

## Bukti Kesusasteraan

Pada masa ini tiada indikasi yang diramalkan tersedia; oleh itu, tiada carian kesusasteraan yang disasarkan telah dijalankan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Sediaan | Indikasi yang Diluluskan |
|------|------|------|------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Nota:** 5 pendaftaran ditemui melalui pertanyaan NPRA (2026-03-27), tetapi medan butir lesen (nombor kebenaran, nama produk, bentuk sediaan, indikasi yang diluluskan) tidak diisi. Data ini perlu diambil semula daripada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk risalah pakej untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat–ubatan) tidak diselesaikan pada masa ini dalam Pakej Bukti ini.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pakej Bukti ini tidak lengkap — tiada indikasi yang diramalkan oleh TxGNN, tiada pemetaan ID DrugBank, tiada data mekanisme tindakan, dan tiada butir lesen atau keselamatan yang diisi. Penilaian penggunaan semula tidak dapat diteruskan sehingga jurang data asas ini diselesaikan.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Penyelesaian ID DrugBank** — Petakan "BOSENTAN MONOHYDRATE" kepada ID DrugBanknya (dijangka: **DB00559**) supaya graf pengetahuan TxGNN boleh menghubungkannya dengan nod penyakit
2. **Pelaksanaan Ramalan TxGNN** — Jalankan semula saluran ramalan KG dan/atau DL dengan pemetaan DrugBank yang diperbetulkan untuk menjana `predicted_indications`
3. **Populasi Butir Lesen NPRA** — Pertanyakan semula pangkalan data NPRA untuk mengisi nombor kebenaran, nama produk, bentuk sediaan, dan teks indikasi yang diluluskan untuk semua 5 pendaftaran
4. **Pengambilan Data Mekanisme Tindakan** — Pertanyakan API DrugBank untuk mekanisme tindakan (antagonisme reseptor endothelin)
5. **Pengumpulan Data Keselamatan** — Ekstrak amaran utama, kontraindikasi, dan interaksi ubat–ubatan daripada risalah pakej atau DrugBank
6. **Pengumpulan Bukti** — Setelah indikasi yang diramalkan tersedia, jalankan pemungut ClinicalTrials.gov, PubMed, dan ICTRP untuk bukti sokongan

---

*Laporan ini untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

