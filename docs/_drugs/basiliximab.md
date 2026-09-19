---
layout: default
title: Basiliximab
parent: Low Evidence (L4-L5)
nav_order: 119
evidence_level: L5
indication_count: 0
---

# Basiliximab
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

# Basiliximab: Laporan Penilaian Ubah Tujuan Ubat

## Ringkasan Satu Ayat

Basiliximab adalah antibodi monoklonal kimera yang menyasarkan rantai penerima IL-2 α (CD25), terutamanya digunakan untuk profilaksis penolakan organ akut dalam pemindahan ginjal. Pada masa kini, model TxGNN **tiada indikasi baru yang diramalkan** untuk ubat ini, dan pek bukti mengandungi jurang data yang ketara yang mesti diselesaikan sebelum analisis ubah tujuan ubat dapat diteruskan.

---

## Gambaran Panduan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Profilaksis penolakan organ akut dalam pemindahan ginjal (diketahui; tidak dipenuhi dalam pek bukti) |
| Indikasi Baru Yang Diramalkan | — (Tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Tiada ramalan atau kajian untuk dinilai) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan Yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

> Pada masa kini, data mekanisme tindakan terperinci tidak tersedia dalam pek bukti. Berdasarkan maklumat yang diketahui umum, Basiliximab (nama jenama: Simulect) adalah antibodi monoklonal kimera (tikus/manusia) yang mengikat secara spesifik pada rantai penerima IL-2 α (CD25) pada permukaan limfosit T yang diaktifkan. Dengan menghalang pengikatan IL-2, ia menghalang proliferasi sel T yang dimediasi IL-2, langkah kritikal dalam tindak balas imun selular yang terlibat dalam penolakan allograf.

Mekanisme ini — penyerangan imun terpilih melalui perencatan laluan IL-2 — mempunyai kebolehgunaan teori kepada keadaan terkait imun yang lain seperti penyakit lawan-tuan ubat (GvHD), gangguan autoimun, dan penyakit radang tertentu yang dimediasi sel T. Bagaimanapun, **model TxGNN belum menghasilkan sebarang indikasi yang diramalkan** untuk Basiliximab dalam operasi semasa, yang mungkin disebabkan oleh data masukan yang tidak lengkap (cth: pemetaan DrugBank yang hilang dalam graf pengetahuan) atau sifat biologi yang sangat khusus ubat itu yang mengehadkan inferens berasaskan graf.

Tanpa ramalan TxGNN, tiada analisis jambatan mekanik antara indikasi asal dan indikasi baru dapat dilakukan pada masa ini.

---

## Bukti Percubaan Klinikal

Pada masa kini tiada indikasi yang diramalkan tersedia daripada TxGNN; oleh itu, bukti percubaan klinikal yang disasarkan tidak dapat diambil.

> Untuk mengisi bahagian ini, ramalan TxGNN mesti terlebih dahulu dihasilkan, selepas itu pertanyaan ClinicalTrials.gov dan ICTRP dapat dijalankan untuk penyakit yang diramalkan.

---

## Bukti Kesusasteraan

Pada masa kini tiada indikasi yang diramalkan tersedia daripada TxGNN; oleh itu, bukti kesusasteraan yang disasarkan tidak dapat diambil.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Yang Diluluskan |
|------|------|------|------|
| (Tidak tersedia dalam pek bukti) | (Tidak tersedia) | (Tidak tersedia) | (Tidak tersedia) |

> **Nota:** Pertanyaan NPRA mengembalikan 1 rekod pendaftaran untuk Basiliximab, tetapi medan lesen terperinci (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak dipenuhi dalam pek bukti. Ini perlu diambil daripada pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk pamflet ubat untuk maklumat keselamatan.
>
> Pek bukti tidak mengandungi amaran utama, kontraindikasi, atau data interaksi ubat untuk Basiliximab. Ini dikelaskan sebagai jurang data **Menghalang** (DG001) yang mesti diselesaikan sebelum penilaian keselamatan dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pek bukti untuk Basiliximab mengandungi jurang data yang kritikal — belum ada ramalan TxGNN dihasilkan, medan mekanisme tindakan adalah kosong, data keselamatan (amaran dan kontraindikasi) hilang, dan perincian lesen Malaysia tidak lengkap. Tanpa sekurang-kurangnya satu indikasi baru yang diramalkan, saluran penilaian ubah tujuan ubat tidak dapat diteruskan.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Selesaikan DG001 (Menghalang):** Ambil amaran pamflet ubat dan kontraindikasi daripada laman web NPRA atau dokumentasi pengeluar ubat
2. **Selesaikan DG002 (Tinggi):** Soal API DrugBank untuk mekanisme tindakan, sasaran, dan pengelasan farmakologi Basiliximab
3. **Isi perincian lesen Malaysia:** Lengkapkan rekod pendaftaran NPRA (nombor kebenaran, nama produk, bentuk dos, teks indikasi yang diluluskan)
4. **Jalankan semula saluran ramalan TxGNN:** Pastikan Basiliximab (DB00074) dipetakan dengan betul dalam graf pengetahuan dan laksanakan semula kedua-dua kaedah ramalan KG dan DL
5. **Apabila ramalan tersedia:** Kumpulkan bukti percubaan klinikal dan kesusasteraan untuk indikasi ramalan teratas

---

*Penafian: Laporan ini untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Calon ubah tujuan ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

