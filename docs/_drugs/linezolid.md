---
layout: default
title: Linezolid
parent: Low Evidence (L4-L5)
nav_order: 445
evidence_level: L5
indication_count: 0
---

# Linezolid
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

# Linezolid: Laporan Penilaian Penggubahan Semula Ubat (Ramalan TxGNN Menunggu)

## Ringkasan Satu Ayat

Linezolid adalah antibiotik sintetik kelas oxazolidinone yang diluluskan untuk merawat jangkitan bakteria Gram-positif yang serius, termasuk yang disebabkan oleh *Staphylococcus aureus* yang tahan methicillin (MRSA) dan *Enterococcus* yang tahan vancomycin (VRE).
Pada masa ini, **tiada ramalan penggubahan semula TxGNN tersedia** untuk ubat ini, kerana senarai `predicted_indications` dalam Evidence Pack semasa adalah kosong.
Tanpa sasaran ramalan, penilaian mekanistik dan klinikal yang lengkap tidak boleh disempurnakan; laporan ini mendokumentasikan status data semasa dan menggariskan langkah-langkah yang diperlukan sebelum penilaian dapat diteruskan.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak boleh diperolehi daripada data semasa (semua medan butiran lesen adalah kosong) |
| Petunjuk Baru yang Diramalkan | Tiada ramalan tersedia |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A — tiada sasaran ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 9 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Bahagian ini tidak boleh disempurnakan dalam bentuk piawainya kerana tiada sasaran penggubahan semula yang telah diramalkan. Maklumat kontekstual berikut disediakan berdasarkan farmakologi yang diketahui umum untuk menyokong penilaian masa depan apabila ramalan dihasilkan.

Linezolid menghambat sintesis protein bakteria dengan mengikat pada komponen RNA ribosomal 23S subunit ribosomal 50S, dengan itu mencegah pembentukan kompleks permulaan 70S. Mekanisme ini adalah berbeza daripada semua kelas antibiotik lain, yang menjelaskan aktivitasnya terhadap organisma Gram-positif yang tahan pelbagai ubat. Dalam literatur penggubahan semula ubat, perancah oxazolidinone telah menarik minat melampaui penyakit berjangkit — terutamanya dalam onkologi (pertindihan biologi ribosomal) dan beberapa keadaan inflamasi — walaupun tiada ramalan sedemikian tersedia dalam pakej ini.

Medan MOA kini ditandakan sebagai jurang data (DG002). Mendapatkan semula entri MOA DrugBank yang lengkap harus menjadi langkah pemulihan pertama, kerana ia adalah asas kepada sebarang hujah kebolehkerjaan mekanistik untuk petunjuk baru yang diramalkan.

---

## Bukti Ujian Klinikal

Tiada petunjuk yang diramalkan tersedia dalam Evidence Pack ini; oleh itu, tiada bukti ujian klinikal khusus penyakit boleh dipersembahkan.

Setelah sasaran ramalan disahkan, pemungut ClinicalTrials.gov dan ICTRP harus dikueri untuk pasangan ubat–penyakit tertentu itu.

---

## Bukti Literatur

Tiada petunjuk yang diramalkan tersedia dalam Evidence Pack ini; oleh itu, tiada bukti literatur khusus penyakit boleh dipersembahkan.

---

## Maklumat Pasaran Malaysia

Sembilan pendaftaran aktif direkodkan dengan Agensi Kawal Selia Farmaseutikal Kebangsaan (NPRA) Malaysia. Walau bagaimanapun, semua medan butiran lesen (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) telah dikembalikan sebagai rentetan kosong dalam gabungan data semasa. Jadual di bawah mencerminkan jurang data ini.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------------------|-------------|-------------|---------------------|
| — | — | — | Medan butiran tidak diisi dalam tarikan data semasa |

> **Tindakan diperlukan:** Kueri semula pangkalan data NPRA dengan pengekstrakan medan yang jelas untuk semua 9 pendaftaran, atau muat turun risalah maklumat produk yang sepadan, untuk memenuhi jadual ini.

---

## Pertimbangan Keselamatan

Semua medan keselamatan dalam Evidence Pack semasa ditandakan sebagai jurang data:

- **Amaran Utama**: Tidak tersedia (DG001 — Keterukan pemblokiran)
- **Kontraindikasi**: Tidak tersedia (DG001 — Keterukan pemblokiran)
- **Interaksi Ubat**: Kueri tidak mengembalikan hasil (`not_found` status)

> Sila rujuk risalah pembungkusan (SmPC / PIL) yang tersedia di halaman produk NPRA atau pemula untuk maklumat keselamatan yang lengkap. Linezolid diketahui membawa amaran penting berkaitan mielosupresi, sindrom serotonin (dalam kombinasi dengan agen serotonergik), neuropati perifer dan opik, serta asidosis laktat — ini mesti diekstrak secara formal sebelum sebarang penilaian keselamatan boleh diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Evidence Pack untuk Linezolid pada masa ini tidak mengandungi ramalan penggubahan semula TxGNN dan hilang semua data keselamatan, MOA, dan peraturan butiran. Tiada ramalan yang boleh ditindakan untuk dinilai, dan tiga daripada empat domain data yang diperlukan untuk penilaian piawai adalah tidak lengkap.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Kritikal — DG001]** Muat turun dan analisis PDF risalah produk NPRA / pemula untuk mengekstrak petunjuk yang diluluskan, amaran, dan kontraindikasi bagi semua 9 produk terdaftar.
- **[Kritikal — DG002]** Kueri API DrugBank untuk Linezolid (DB00601) untuk mendapatkan semula mekanisme tindakan yang lengkap, farmakodinamik, dan profil ketoksikan.
- **[Kritikal]** Jalankan semula saluran ramalan TxGNN untuk menjana `predicted_indications` untuk Linezolid; sahkan sama ada senarai kosong mencerminkan output model yang benar (tiada calon di atas ambang) atau kegagalan saluran.
- **[Tinggi]** Kueri semula NPRA dengan pengekstrakan medan berstruktur untuk memenuhi semua 9 rekod lesen (nombor kebenaran, nama produk, bentuk dos, teks petunjuk).
- **[Sederhana]** Jalankan semula kueri DDI terhadap data interaksi DrugBank (status `not_found` mungkin mencerminkan masalah kueri daripada ketiadaan interaksi yang tulen, memandangkan profil interaksi serotonergik linezolid yang diketahui dengan baik).
- **[Sederhana]** Setelah sasaran ramalan disahkan, jalankan pemungut ClinicalTrials.gov dan PubMed untuk pasangan ubat–penyakit tertentu itu untuk menetapkan tahap bukti (L1–L5).

---

*Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon penggubahan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

