---
layout: default
title: Aripiprazole Monohydrate
parent: Low Evidence (L4-L5)
nav_order: 86
evidence_level: L5
indication_count: 0
---

# Aripiprazole Monohydrate
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

# Aripiprazole Monohydrate: Penilaian Repurposing Ubat — Data Ramalan TxGNN Tertunda

---

## Ringkasan Satu Ayat

Aripiprazole monohydrate ialah antipsikotik atipik (generasi kedua), yang telah ditubuhkan secara meluas untuk rawatan skizofrenia, gangguan bipolar I, dan rawatan adjuvant bagi gangguan depresi major.
Pakej Bukti ini mengesahkan **1 pendaftaran pasaran Malaysia yang aktif**, tetapi **ramalan repurposing TxGNN belum tersedia** — susunan `predicted_indications` kosong, yang bermakna penilaian indikasi-ke-indikasi yang lengkap tidak dapat diselesaikan pada peringkat ini.
Laporan tersebut oleh itu diklasifikasikan sebagai **tidak lengkap** dan keputusan **Tahan** disyorkan sehingga data ramalan, mekanisme tindakan, dan butir-butir lesen kawal selia yang lengkap diperolehi.

---

## Panduan Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Skizofrenia; Gangguan bipolar I; Rawatan adjuvant bagi gangguan depresi major *(daripada pengetahuan farmakoloji yang ditubuhkan — tidak terdapat dalam Pakej Bukti semasa)* |
| Indikasi Baru yang Diramalkan | **Tertunda** — Data ramalan TxGNN belum tersedia |
| Skor Ramalan TxGNN | Tertunda |
| Tahap Bukti | **Tidak Ditentukan** (tiada ramalan untuk dinilai) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam Pakej Bukti ini. Berdasarkan pengetahuan farmakoloji yang ditubuhkan, aripiprazole monohydrate ialah antipsikotik atipik yang termasuk dalam kelas kinolinon. Ia bertindak sebagai **agonis separa pada reseptor dopamin D2 dan D3** dan **reseptor serotonin 5-HT1A**, dan sebagai **antagonis pada reseptor 5-HT2A**. Profil "penstabil sistem dopamin" yang unik ini membezakannya daripada antipsikotik terdahulu yang bertindak sebagai antagonis D2 penuh.

Kerana aripiprazole memodulasi kedua-dua laluan dopaminergik dan serotonergik secara serentak, ia telah menghasilkan minat penyelidikan dalam keadaan di luar psikosis klasik — termasuk gangguan kawalan impuls, kaitan lekas angin spektrum autisme–kerengsuan, sindrom Tourette, dan kemurungan tahan rawatan. Jambatan mekanik lintas indikasi ini menjadikan aripiprazole calon yang munasabah untuk kajian repurposing ubat.

Namun, **tiada skor ramalan model TxGNN atau penyakit calon yang terdapat dalam Pakej Bukti ini**. Sehingga saluran ramalan dijalankan semula dan keputusan dipenuhi, tiada indikasi baru tertentu boleh dinilai secara formal, dan naratif mekanistik di atas tidak dapat dipautkan kepada penilaian bukti kuantitatif.

---

## Bukti Ujian Klinikal

Data ramalan TxGNN tidak tersedia dalam Pakej Bukti ini. Setelah indikasi sasaran dikenal pasti, bukti ujian klinikal akan diperolehi daripada ClinicalTrials.gov dan ICTRP.

Pada masa ini tiada ujian klinikal berkaitan yang dipautkan kepada penilaian ini.

---

## Bukti Sastera

Data ramalan TxGNN tidak tersedia dalam Pakej Bukti ini. Setelah indikasi sasaran dikenal pasti, bukti sastera PubMed akan diperolehi dan dinilai.

Pada masa ini tiada sastera berkaitan yang dipautkan kepada penilaian ini.

---

## Maklumat Pasaran Malaysia

Pakej Bukti mengesahkan **1 pendaftaran aktif** dengan NPRA Malaysia dan status pasaran **Dipasarkan (Dipasarkan)**. Walau bagaimanapun, medan butir-butir lesen (nombor pendaftaran, nama produk, bentuk dos, pengilang, teks indikasi yang diluluskan) dikembalikan sebagai rentetan kosong dalam ekstrak data semasa.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|-----------------|------------|-----------|-------------------------|
| *(tidak diperolehi)* | *(tidak diperolehi)* | *(tidak diperolehi)* | *(tidak diperolehi)* |

> **Tindakan Diperlukan:** Soal semula pangkalan data NPRA untuk mendapatkan butir-butir rekod lesen lengkap untuk ARIPIPRAZOLE MONOHYDRATE.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Kedua-dua amaran utama dan kontraindikasi ditandai sebagai jurang data dalam Pakej Bukti ini (keterukan: Penyekat dan Tinggi masing-masing). Tiada rekod interaksi ubat–ubat dikembalikan. Penilaian keselamatan tidak dapat diteruskan sehingga maklumat preskripsi lengkap diperolehi daripada monograf produk NPRA atau fail PDF sisipan pakej rasmi.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Asas:**
Pakej Bukti ini secara struktur tidak lengkap — ramalan TxGNN, data mekanisme tindakan, butir-butir lesen, dan maklumat keselamatan semuanya tiada atau kosong, menjadikannya mustahil untuk menjalankan penilaian repurposing bermakna pada masa ini.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Penyekat — DG001]** Muat turun dan parskan fail PDF sisipan pakej NPRA/TFDA untuk mengekstrak indikasi yang diluluskan, amaran utama, dan kontraindikasi; ini diperlukan sebelum sebarang penyaringan keselamatan pra-S1 (S1) dapat dimulakan
- **[Tinggi — DG002]** Pertanyaan API DrugBank menggunakan nama ubat `ARIPIPRAZOLE MONOHYDRATE` untuk mendapatkan ID DrugBank, mekanisme tindakan lengkap, kategori farmakoloji, dan profil toksisiti
- **[Kritikal]** Jalankan semula saluran ramalan TxGNN — susunan `predicted_indications` kosong; tanpa sekurang-kurangnya satu penyakit calon, laporan tidak dapat diselesaikan
- **[Diperlukan]** Soal semula NPRA untuk mendapatkan medan rekod lesen lengkap (nombor pendaftaran, nama produk, bentuk dos, teks indikasi yang diluluskan)
- **[Pilihan]** Sahkan sama ada bentuk garam monohydrate berkongsi entri DrugBank dengan bentuk bebas aripiprazole (ID DrugBank: DB01238) untuk mengelakkan kegagalan pemetaan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

