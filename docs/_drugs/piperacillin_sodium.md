---
layout: default
title: Piperacillin Sodium
parent: Low Evidence (L4-L5)
nav_order: 550
evidence_level: L5
indication_count: 0
---

# Piperacillin Sodium
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

# Piperacillin Sodium: Penilaian Penggunaan Semula Ubat — Tiada Ramalan TxGNN Tersedia

## Ringkasan Satu Ayat

Piperacillin Sodium adalah antibiotik beta-laktam spektrum luas (penisilin semisintesis) yang digunakan secara meluas dalam persekitaran klinikal untuk merawat jangkitan bakteria yang serius, sering dikombinasikan dengan perencat beta-laktamase tazobactam.
Pakej Bukti semasa mengandungi **tiada ramalan indikasi baharu yang disokong TxGNN** untuk ubat ini, dan data penting termasuk butiran mekanisme tindakan, maklumat kemasan, dan maklumat lesen masih dalam proses pengumpulan.
Hasilnya, laporan ini berfungsi terutamanya sebagai ringkasan jurang data dan garis asas pra-penilaian; penilaian penggunaan semula yang lengkap tidak dapat diselesaikan pada peringkat ini.

---

## Pandangan Umum Cepat

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Jangkitan bakteria (antibiotik spektrum luas; disahkan daripada pengetahuan kelas ubat) |
| Indikasi Baharu yang Diramalkan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A — Tiada indikasi yang diramalkan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 6 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Belum Tersedia?

Piperacillin Sodium adalah antibiotik penisilin semisintesis spektrum luas. Ia menghambat sintesis dinding sel bakteria dengan mengikat kepada protein pengikat penisilin (PBPs), dengan itu menyekat transpeptidasi dan akhirnya menyebabkan lisis sel bakteria. Ia paling kerap diagih bersama tazobactam (perencat beta-laktamase) untuk memperluaskan spektrumnya terhadap organisma pengeluar beta-laktamase.

Model TxGNN bergantung pada kehadiran ubat dan hubungannya dalam graf pengetahuan bioperubatan untuk menghasilkan calon penggunaan semula. Ketiadaan DrugBank ID dalam Pakej Bukti ini (`drugbank_id: null`) kemungkinan besar menghalang model daripada menambat Piperacillin Sodium dalam graf, yang menjelaskan mengapa `predicted_indications` adalah kosong.

Selain itu, mekanisme utama piperacillin — menyasarkan enzim bakteria — mempunyai tindihan mekanistik terhad dengan laluan penyakit bukan jangkitan, yang mungkin seterusnya mengurangkan kemungkinan isyarat penggunaan semula berkeyakinan tinggi. Walau bagaimanapun, ini tidak boleh disahkan tanpa menyelesaikan pemetaan DrugBank dan menjalankan semula saluran ramalan.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan berdaftar dalam konteks penggunaan semula, kerana tiada indikasi yang diramalkan telah dihasilkan oleh TxGNN.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan tersedia untuk penilaian, kerana tiada indikasi yang diramalkan untuk dicari.

---

## Maklumat Pasaran Malaysia

Enam pendaftaran aktif direkodkan untuk Piperacillin Sodium di Malaysia. Walau bagaimanapun, maklumat terperinci peringkat lesen (nombor kelulusan, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak dikembalikan dalam penarik data semasa. Jadual di bawah mencerminkan apa yang tersedia:

| Nombor Kelulusan | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| Data belum selesai | Data belum selesai | Data belum selesai | Data belum selesai |
| Data belum selesai | Data belum selesai | Data belum selesai | Data belum selesai |
| Data belum selesai | Data belum selesai | Data belum selesai | Data belum selesai |
| Data belum selesai | Data belum selesai | Data belum selesai | Data belum selesai |
| Data belum selesai | Data belum selesai | Data belum selesai | Data belum selesai |

> **Nota:** 6 pendaftaran disahkan sebagai aktif di NPRA. Butiran lesen lengkap harus diambil melalui pertanyaan NPRA yang disasarkan atau muat turun langsung daripada daftar produk NPRA.

---

## Pertimbangan Keselamatan

Sila rujuk maklumat kemasan untuk maklumat keselamatan. Data keselamatan formal (amaran utama, kontraindikasi, dan interaksi ubat) tidak dapat diambil dalam kitaran pengumpulan bukti ini dan mesti bersumber daripada:
- Maklumat kemasan Malaysia yang diluluskan NPRA (PDF label produk)
- Penyertaan DrugBank untuk Piperacillin / Piperacillin-Tazobactam (apabila DrugBank ID telah dipetakan)

Sebagai rujukan kelas umum, antibiotik kelas penisilin biasanya dikaitkan dengan reaksi hipersensitiviti (termasuk anafilaksis), diare berkaitan Clostridioides difficile, dan nefrotoksisiti pada dos tinggi — tetapi ini mesti disahkan secara formal daripada maklumat kemasan sebelum sebarang penilaian diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Model TxGNN tidak mengembalikan ramalan indikasi baharu untuk Piperacillin Sodium, kemungkinan besar kerana ubat tidak boleh ditambat dalam graf pengetahuan kerana DrugBank ID yang hilang. Tanpa ramalan, tidak ada calon penggunaan semula untuk dinilai, dan semua lapisan data penting (MOA, amaran keselamatan, butiran lesen) tetap tidak lengkap.

**Untuk meneruskan, perkara berikut diperlukan:**

- **Pemetaan DrugBank**: Selesaikan `drugbank_id` untuk Piperacillin Sodium (kemungkinan `DB00319` untuk piperacillin atau `DB00728` untuk piperacillin/tazobactam) dan jalankan semula saluran ramalan graf pengetahuan TxGNN
- **Pengambilan maklumat kemasan**: Muat turun dan analisis PDF label produk yang diluluskan NPRA untuk mengisi MOA, amaran utama, dan kontraindikasi (menangani Jurang Data DG001 dan DG002)
- **Pertanyaan butiran lesen NPRA**: Pertanyaan semula daftar NPRA untuk mengambil nombor kelulusan lengkap, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk kesemua 6 pendaftaran
- **Jalankan semula Pakej Bukti**: Apabila DrugBank ID diselesaikan dan saluran ramalan dijalankan semula, janakan semula Pakej Bukti ini dengan `predicted_indications` yang dipenuhi sebelum meneruskan ke penilaian bukti klinikal dan literatur

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Mana-mana calon penggunaan semula yang dikenal pasti mesti disahkan melalui kajian klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

