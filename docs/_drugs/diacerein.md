---
layout: default
title: Diacerein
parent: Low Evidence (L4-L5)
nav_order: 273
evidence_level: L5
indication_count: 0
---

# Diacerein
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

# Diacerein: Laporan Penilaian Penyusunan Semula Ubat

## Ringkasan Satu Ayat

Diacerein ialah derivatif antrakuinon yang sedang dipasarkan di Malaysia, terutamanya digunakan untuk rawatan gejala osteoartritis. Tiada indikasi baru yang diramalkan dihasilkan oleh model TxGNN dalam kitaran penilaian ini, dan jurang data yang ketara masih kekal dalam mekanisme tindakan, keselamatan, dan butiran label kawal selia.

## Gambaran Ringkas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tersedia (butiran lesen sedang ditunggu) |
| Indikasi Baru Diramalkan | — (Tiada ramalan TxGNN dihasilkan) |
| Skor Ramalan TxGNN | T/A |
| Aras Bukti | L5 (Tiada ramalan atau bukti sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan Disyorkan | **Tahan** |

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, model TxGNN tidak menghasilkan sebarang indikasi baru yang diramalkan untuk Diacerein. Ini mungkin disebabkan oleh pemetaan yang tidak mencukupi antara entri DrugBank ubat (DB11994) dan nod graf pengetahuan, atau data hubungan yang terhad dalam KG untuk sebatian ini.

> Data mekanisme tindakan terperinci (MOA) tidak tersedia dalam pakej bukti ini. Berdasarkan maklumat yang diketahui umum, Diacerein ialah penghambat interleukin-1β (IL-1β) yang termasuk dalam kelas antrakuinon. Ia adalah pro-ubat yang dimetaboliskan kepada bentuk aktifnya, rhein, yang memberikan kesan anti-keradangan dan perlindungan rawan tulang. Penggunaannya yang diluluskan dalam osteoartritis telah ditubuhkan di pelbagai pasaran; bagaimanapun, tanpa output ramalan TxGNN, tiada penghubungan mekanistik kepada indikasi baru yang dapat dinilai pada masa ini.

Ketiadaan ramalan tidak membayangkan bahawa ubat ini tidak mempunyai potensi penyusunan semula — ia menunjukkan bahawa saluran data semasa memerlukan input tambahan (cth., pemetaan DrugBank-ke-KG yang lebih baik, atau teks indikasi yang diperkaya untuk padanan penyakit) sebelum model dapat menghasilkan indikasi calon.

## Bukti Percubaan Klinikal

Pada masa ini tiada indikasi yang diramalkan TxGNN untuk Diacerein; oleh itu, tiada pencarian percubaan klinikal yang disasarkan telah dijalankan.

## Bukti Literatur

Pada masa ini tiada indikasi yang diramalkan TxGNN untuk Diacerein; oleh itu, tiada pencarian literatur yang disasarkan telah dijalankan.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|------|------|------|------|
| (Sedang diambil) | (Sedang diambil) | (Sedang diambil) | (Sedang diambil) |

> **Nota:** Satu pendaftaran telah dikenal pasti dalam pertanyaan NPRA (tarikh pertanyaan: 2026-03-27), tetapi medan lesen terperinci (nombor kebenaran, nama produk, bentuk dos, indikasi diluluskan) tidak diisi dalam pakej bukti ini. Butiran ini perlu diambil daripada pangkalan data NPRA.

## Pertimbangan Keselamatan

> Sila rujuk sisipan pek untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti ini.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada indikasi yang diramalkan TxGNN dihasilkan untuk Diacerein, dan jurang data kritikal wujud merentas MOA, butiran label kawal selia, dan maklumat keselamatan. Penilaian tidak dapat diteruskan kepada penilaian calon tanpa input asas ini.

**Untuk diteruskan, perkara berikut diperlukan:**

1. **Ambil butiran lesen NPRA** — Pertanyaan pangkalan data NPRA untuk maklumat pendaftaran penuh (nombor kebenaran, nama produk, bentuk dos, teks indikasi diluluskan)
2. **Isi jurang data MOA (DG002)** — Pertanyaan API DrugBank untuk mekanisme tindakan Diacerein, farmakodinamik, dan maklumat sasaran
3. **Isi jurang data keselamatan (DG001)** — Muat turun dan huraikan PDF sisipan pek daripada pihak berkuasa kawal selia untuk amaran, kontraindikasi, dan langkah berjaga-jaga
4. **Siasat pemetaan KG** — Sahkan bahawa Diacerein (DB11994) dipetakan dengan betul kepada nod graf pengetahuan TxGNN; semak `node.csv` untuk kehadiran DrugBank ID ini dan sahkan sambungan tepi dalam `kg.csv`
5. **Jalankan semula ramalan TxGNN** — Setelah pemetaan disahkan dan jurang data diselesaikan, jalankan semula saluran ramalan KG dan DL untuk menghasilkan indikasi calon

---

*Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Calon penyusunan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

