---
layout: default
title: Baloxavir Marboxil
parent: Low Evidence (L4-L5)
nav_order: 117
evidence_level: L5
indication_count: 0
---

# Baloxavir Marboxil
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

# Baloxavir Marboxil: Laporan Penilaian Penggunaan Kembali Ubat

## Ringkasan Satu Ayat

Baloxavir marboxil (Xofluza) ialah penghambat endonuklease yang bergantung pada cap yang dikembangkan asalnya untuk rawatan influenza. Model TxGNN **tidak menghasilkan sebarang petunjukan baru yang diramalkan** untuk ubat ini, dan Evidence Pack mengandungi jurang data yang signifikan dalam butiran kawal selia, mekanisme tindakan, dan maklumat keselamatan.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Petunjukan Asal | Influenza (butiran lesen tidak disediakan dalam sumber data) |
| Petunjukan Baru yang Diramalkan | — (Tiada ramalan yang dijana) |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Tiada ramalan atau kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada **petunjukan baru yang diramalkan oleh TxGNN** untuk Baloxavir marboxil dalam Evidence Pack ini. Tatasusunan `predicted_indications` adalah kosong, bermakna model sama ada tidak mengenal pasti calon penggunaan kembali yang cukup yakin atau ubat itu tidak berjaya dipetakan ke dalam grafik pengetahuan untuk ramalan.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam Evidence Pack. Berdasarkan maklumat yang diketahui umum, Baloxavir marboxil ialah penghambat selektif bagi endonuklease yang bergantung pada cap bagi protein asid polimerasi virus influenza (PA). Ia menyekat sintesis mRNA viral pada peringkat awal jangkitan, mewakili mekanisme yang berbeza daripada penghambat neuraminidase (contohnya, oseltamivir). Kekhususannya untuk polimerasi influenza mungkin mengehadkan keluasan peluang penggunaan kembali yang boleh dikenal pasti oleh pendekatan grafik pengetahuan.

Tanpa petunjukan yang diramalkan, tiada penilaian kerasionalan yang berasaskan mekanisme boleh dilakukan pada masa ini.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada petunjukan yang diramalkan telah dijana; oleh itu, tiada carian percubaan klinikal yang disasarkan telah dijalankan.

---

## Bukti Kesusasteraan

Pada masa ini tiada petunjukan yang diramalkan telah dijana; oleh itu, tiada carian kesusasteraan yang disasarkan telah dijalankan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjukan yang Diluluskan |
|------|------|------|------|
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |

> **Nota:** Pertanyaan NPRA mengesahkan 1 pendaftaran untuk Baloxavir marboxil di Malaysia, tetapi butiran lesen (nombor kebenaran, nama produk, bentuk dos, dan teks petunjukan yang diluluskan) tidak diisi dalam Evidence Pack. Jurang data ini harus diperbaiki dengan menanyakan [pangkalan data NPRA Quest3+](https://quest3plus.bpfk.gov.my/).

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan bungkusan untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, dan interaksi ubat) kini tidak tersedia dalam Evidence Pack.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada petunjukan baru yang diramalkan oleh TxGNN untuk Baloxavir marboxil. Tambahan pula, jurang data yang kritikal wujud merentasi butiran kawal selia, mekanisme tindakan, dan maklumat keselamatan, menjadikan sebarang penilaian penggunaan kembali adalah pramatang.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Selesaikan Jurang Data (Menghalang):**
   - Dapatkan butiran lesen NPRA (nombor kebenaran, nama produk, bentuk dos, petunjukan yang diluluskan) daripada pangkalan data NPRA Quest3+
   - Ambil amaran pakej sisipan dan kontraindikasi daripada label produk Malaysia atau rekod NPRA

2. **Selesaikan Jurang Data (Keutamaan Tinggi):**
   - Pertanyaan API DrugBank untuk data mekanisme tindakan (MOA) untuk DB13997
   - Isi medan `original_indications` daripada sumber kawal selia atau DrugBank

3. **Jalankan Semula Saluran Ramalan:**
   - Sahkan bahawa DB13997 (Baloxavir marboxil) dipetakan dengan betul dalam grafik pengetahuan TxGNN (`node.csv` / `kg.csv`)
   - Jika nod ubat wujud tetapi tiada tepi menyambungnya ke nod penyakit, selidiki sama ada pemetaan DrugBank atau penormalan bahan aktif gagal
   - Jalankan semula `run_kg_prediction.py` selepas menyelesaikan isu pemetaan

4. **Jika Ramalan Muncul Selepas Menjalankan Semula:**
   - Kumpulkan bukti percubaan klinikal daripada ClinicalTrials.gov dan ICTRP
   - Kumpulkan bukti kesusasteraan daripada PubMed
   - Kemas kini Evidence Pack dan jana semula laporan ini

---

*Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon penggunaan kembali ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

