---
layout: default
title: Azithromycin Monohydrate
parent: Low Evidence (L4-L5)
nav_order: 114
evidence_level: L5
indication_count: 0
---

# Azithromycin Monohydrate
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

# Azithromycin Monohydrate: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu-Ayat

Azithromycin ialah antibiotik makrolida yang digunakan secara meluas dan terdaftar di Malaysia untuk rawatan jangkitan bakteria. Model TxGNN **tidak menghasilkan sebarang ramalan petunjuk baru** untuk ubat ini dalam perlaksanaan analisis semasa. Oleh itu, **tiada calon penggunaan semula untuk dinilai** pada masa ini, dan jurang data yang ketara tetap wujud dalam pakej bukti.

---

## Gambaran Pantas

| Perkara | Kandungan |
|------|------|
| Petunjuk Asal | Tidak tersedia dalam pakej bukti (perincian lesen hilang) |
| Petunjuk Baru Dijangka | **Tiada** — tiada ramalan dihasilkan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 (Tiada ramalan atau kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 4 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Masuk Akal?

**Tiada ramalan TxGNN untuk dinilai** bagi Azithromycin Monohydrate. Tatasusunan `predicted_indications` dalam pakej bukti adalah kosong, bermakna model sama ada tidak menemui calon penggunaan semula keyakinan tinggi atau ubat itu tidak berjaya dipetakan ke dalam graf pengetahuan.

Azithromycin ialah antibiotik makrolida yang terkenal yang menghalang sintesis protein bakteria dengan mengikat unit ribosom 50S. Ia biasanya ditetapkan untuk jangkitan saluran pernafasan, jangkitan kulit dan tisu lembut, jangkitan berpindah seks, dan otitis media. Bagaimanapun, maklumat mekanisme tindakan ini tidak disertakan dalam pakej bukti (disenaraikan sebagai jurang data), dan tiada ID DrugBank yang disediakan, yang mungkin telah menyumbang kepada kekurangan ramalan.

Tanpa pemetaan DrugBank yang berjaya (drugbank_id ialah null), graf pengetahuan TxGNN tidak dapat menghubungkan ubat ini ke sasaran farmakologi yang dikenali dan persatuan penyakit, menjadikan ia mustahil untuk menghasilkan ramalan penggunaan semula. **Menyelesaikan pemetaan DrugBank adalah prasyarat** sebelum menjalankan semula saluran ramalan.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal yang berkaitan untuk dilaporkan, kerana tiada petunjuk baru dijangka.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan untuk dilaporkan, kerana tiada petunjuk baru dijangka.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk Diluluskan |
|------|------|------|------|
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |

> **Nota:** 4 pendaftaran ditemui melalui pertanyaan NPRA (tarikh pertanyaan: 2026-03-27), tetapi medan perincian lesen (nombor kebenaran, nama produk, bentuk dos, petunjuk diluluskan) tidak diisi dalam pakej bukti. Jurang data ini perlu diselesaikan dengan pertanyaan semula pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, dan interaksi ubat) kini tiada dari pakej bukti.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan Rasional:**
Tiada calon penggunaan semula yang dihasilkan oleh TxGNN untuk Azithromycin Monohydrate. Pakej bukti mengandungi jurang data kritikal — yang paling penting, DrugBank ID yang hilang (yang menghalang penyepaduan graf pengetahuan) dan perincian lesen/petunjuk kosong dari NPRA. Tanpa data asas ini, tidak mungkin untuk menjalankan penilaian penggunaan semula yang bermakna.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Pemetaan DrugBank ID** — ID DrugBank Azithromycin berkemungkinan `DB00207`. Ini mesti disahkan dan diisi supaya ubat dapat dipautkan ke dalam graf pengetahuan TxGNN.
2. **Perincian lesen NPRA** — Pertanyaan semula pangkalan data NPRA untuk mendapatkan perincian pendaftaran penuh (nombor kebenaran, nama produk, bentuk dos, petunjuk diluluskan) untuk semua 4 pendaftaran.
3. **Mekanisme tindakan (MOA)** — Ambil dari DrugBank sebaik sahaja ID dipetakan (antibiotik makrolida, inhibitor unit ribosom 50S).
4. **Data keselamatan** — Muat turun dan analisis sisipan pakej untuk mengeluarkan amaran utama, kontraindikasi, dan maklumat interaksi ubat.
5. **Jalankan semula ramalan TxGNN** — Selepas menyelesaikan pemetaan DrugBank, jalankan semula saluran pemetaan graf pengetahuan dan ramalan pembelajaran mendalam untuk menghasilkan calon penggunaan semula.

---

*Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

