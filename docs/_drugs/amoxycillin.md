---
layout: default
title: Amoxycillin
parent: Low Evidence (L4-L5)
nav_order: 66
evidence_level: L5
indication_count: 0
---

# Amoxycillin
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

# Amoxycillin: Antibiotik Spektrum Luas — Analisis Repurposing TxGNN Dalam Proses

---

## Ringkasan Satu Ayat

Amoxycillin ialah antibiotik aminopenicillin yang digunakan secara meluas dan ditunjukkan untuk pelbagai jangkauan jangkitan bakteria, dengan 66 produk yang didaftar di Malaysia mengesahkan kehadiran pasaran yang kukuh.
Model TxGNN **belum menghasilkan ramalan repurposing** untuk ubat ini dalam Pek Bukti semasa.
Tanpa indikasi yang diramalkan, pencarian ujian klinikal dan bukti literatur belum dimulakan, dan penilaian repurposing penuh tidak boleh diteruskan pada peringkat ini.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Jangkitan bakteria (saluran pernafasan, saluran kencing, kulit dan tisu lembut, pemberantasan *H. pylori*) |
| Indikasi Baru yang Diramalkan | Belum dijana |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | Tidak berkenaan |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 66 |
| Keputusan yang Disyorkan | **Tunggu** |

---

## Mengapa Ramalan Ini Munasabah?

Amoxycillin ialah aminopenicillin spektrum luas dalam kelas antibiotik beta-laktam. Mekanisme tindakannya berpusat pada pengikatan kepada protein pengikat penicillin (PBP) yang tertanam dalam membran sel bakteria, menghalang langkah transpeptidasi akhir bagi keratan silang peptidoglikan. Ini menghalang sintesis dinding sel, menyebabkan ketidakstabilan osmotik dan lisis bakterisida. Ia aktif terhadap pelbagai organisma Gram-positif (cth. *Streptococcus*, *Enterococcus*) dan patogen Gram-negatif terpilih (cth. *H. pylori*, *E. coli*, *H. influenzae*).

Dari segi klinikal, amoxycillin ialah agen garis pertama bagi pneumonia yang diperoleh komuniti, otitis media akut, jangkitan saluran kencing, jangkitan gigi, dan pemberantasan *Helicobacter pylori* sebagai sebahagian daripada rejimen terapi tiga atau empat ubat. Ia adalah antara antibiotik yang paling dipersembahkan secara global, dengan pangkalan data keselamatan dan keberkesanan selama beberapa dekad merentasi semua kumpulan umur.

Kerana Pek Bukti semasa mengandungi **tiada ramalan TxGNN bagi indikasi baru**, rasional mekanik penyakit khusus untuk repurposing tidak dapat diberikan pada masa ini. Bahagian ini akan dikemas kini apabila saluran ramalan TxGNN telah dilaksanakan dengan pengenal DrugBank yang betul untuk Amoxycillin.

---

## Maklumat Pasaran Malaysia

Pangkalan data NPRA Malaysia mengesahkan **66 produk yang terdaftar** untuk Amoxycillin, menunjukkan akses pasaran yang mantap di seluruh pelbagai pengeluar dan bentuk dos. Walau bagaimanapun, rekod lesen individu tidak diisi dalam versi Pek Bukti ini.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------------------|------------|-----------|------------------------|
| — | Tidak diisi dalam pek data semasa | — | — |

> Butiran lesen lengkap (nama produk, bentuk dos, pengeluar, dan teks indikasi yang diluluskan) boleh diambil daripada **portal eBiz NPRA** (https://www.npra.gov.my/) dengan mencari bahan aktif **"Amoxycillin"**.

---

## Pertimbangan Keselamatan

Data keselamatan belum diisi dalam Pek Bukti ini. Sila rujuk bungkus yang diluluskan Malaysia yang dibekalkan oleh pengeluar untuk maklumat keselamatan yang lengkap.

Berdasarkan literatur terbitan yang mantap, kawasan berikut wajar perhatian semasa semakan keselamatan formal:

- **Hipersensitiviti**: Alergi kelas penicillin, termasuk risiko anafilaksis, adalah kebimbangan keselamatan utama; reaktiviti silang dengan sefalosporin harus dinilai
- **Interaksi Ubat**: Interaksi klinikal yang relevan dengan baik dijelaskan dengan warfarin (kesan antikoagulan yang diperkuat), metotreksat (pelepasan ginjal yang dikurangkan), dan ubat kontraseptif oral gabungan (kemanjuran yang berkurangan secara teorinya)
- **Kontraindikasi**: Hipersensitiviti yang diketahui terhadap penicillin atau sebarang antibiotik beta-laktam

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Alasan:**
Tiada ramalan repurposing TxGNN tersedia dalam Pek Bukti semasa, dan ID DrugBank — diperlukan sebagai input model utama — belum disahkan. Semua analisis aliran hilir (ramalan indikasi, pengumpulan bukti, pemetaan keselamatan) bergantung pada penyiapan langkah data asas ini terlebih dahulu.

**Untuk diteruskan, perkara berikut diperlukan:**

- **Sahkan ID DrugBank** (dijangka: DB01060) dan ambil data MOA lengkap melalui API DrugBank untuk menyelesaikan Jurang Data DG002
- **Jalankan saluran ramalan TxGNN** untuk Amoxycillin bagi menjana calon repurposing yang ditarafkan
- **Muat turun PDF bungkus produk Malaysia** daripada laman web NPRA dan asingkan bagi amaran dan kontraindikasi, menyelesaikan Jurang Data DG001
- **Ambil butiran lesen lengkap** daripada portal eBiz NPRA (nama produk, bentuk dos, teks indikasi yang diluluskan bagi semua 66 pendaftaran)
- **Setelah ramalan tersedia**, jalankan semula pengumpulan bukti daripada ClinicalTrials.gov dan PubMed bagi indikasi yang diramalkan terpangkat teratas, kemudian hasilkan semula laporan ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

