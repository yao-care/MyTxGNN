---
layout: default
title: Betaxolol Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 140
evidence_level: L5
indication_count: 0
---

# Betaxolol Hydrochloride
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

# Betaxolol Hidroklorida: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu Ayat

Betaxolol hidroklorida adalah antagonis reseptor adrenergik beta-1 selektif (penyekat beta), yang biasa digunakan untuk hipertensi dan glaukoma (hipertensi okular). Model TxGNN **tidak menghasilkan sebarang indikasi baru yang diramalkan** untuk ubat ini, dan jurang data kritikal (ID DrugBank, MOA, profil keselamatan) tetap belum diselesaikan, menghalang penilaian lanjutan buat masa ini.

---

## Panduan Ringkas

| Item | Kandungan |
|------|------|
| Indikasi Asal | *(Data tidak tersedia — medan teks indikasi lesen kosong)* |
| Indikasi Baru yang Diramalkan | **Tiada** (tiada ramalan TxGNN dihasilkan) |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | **L5** (Tiada ramalan, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Jumlah Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tangguhkan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan TxGNN yang dihasilkan untuk Betaxolol Hidroklorida, oleh itu tiada nisbah mekanik untuk dinilai buat masa ini.

Berdasarkan pengetahuan farmakologi am, Betaxolol adalah penyekat reseptor adrenergik pemilihan jantung (beta-1 selektif). Dalam bentuk oral ia digunakan untuk mengurus hipertensi, dan dalam bentuk oftalmik ia digunakan untuk mengurangkan tekanan intraokuler dalam glaukoma sudut terbuka dan hipertensi okular. Keseselektifannya untuk reseptor beta-1 bermakna ia mempunyai kesan yang agak kurang pada reseptor beta-2 dalam otot licin bronkial dan vaskular berbanding penyekat beta tidak selektif.

Pada masa ini, data mekanisme tindakan terperinci tidak diambil daripada DrugBank (ID DrugBank hilang daripada paket bukti ini). Tanpa pemetaan DrugBank yang disahkan dan tanpa sebarang hasil ramalan TxGNN, adalah tidak mungkin untuk menilai kemungkinan mekanik lintas-indikasi.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada indikasi diramalkan, oleh itu tiada carian percubaan klinikal dilakukan.

---

## Bukti Kesusasteraan

Pada masa ini tiada indikasi diramalkan, oleh itu tiada carian kesusasteraan dilakukan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(kosong)* | *(kosong)* | *(kosong)* | *(kosong)* |

> **Nota:** Satu rekod pendaftaran wujud dalam pangkalan data NPRA, tetapi semua medan butiran (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) hilang daripada paket bukti. Jurang data ini harus diperbetulkan dengan soal semula pangkalan data NPRA.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan paket untuk maklumat keselamatan.
>
> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) tidak tersedia pada masa ini. Ini diklasifikasikan sebagai jurang data **Menghalang** (DG001) yang mesti diselesaikan sebelum sebarang penilaian keselamatan dapat diteruskan.

---

## Ringkasan Jurang Data

Jurang data kritikal berikut telah dikenal pasti dan mesti ditangani:

| ID Jurang | Item | Keterukan | Kesan | Remediasi |
|------|------|------|------|------|
| DG001 | Amaran Label TFDA / Kontraindikasi | **Menghalang** | Tidak boleh memasuki saringan keselamatan S1 | Muat turun dan huraikan PDF label daripada laman web pihak berkuasa kawal selia |
| DG002 | Mekanisme Tindakan (MOA) | **Tinggi** | Mempengaruhi analisis relevansi mekanik | Soal API DrugBank (Betaxolol berkemungkinan DB00195) |
| — | ID DrugBank | Tinggi | Tidak boleh mendapatkan MOA, DDI, atau data ketoksikan | Sahkan pemetaan: Betaxolol → DrugBank DB00195 |
| — | Medan butiran lesen | Sederhana | Jadual maklumat pasaran kosong | Soal semula NPRA dengan parameter yang diperbetulkan |
| — | Ramalan TxGNN | Tinggi | Tiada calon penggunaan semula untuk dinilai | Sahkan bahawa Betaxolol telah disertakan dalam input KG dan jalankan semula saluran ramalan |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguhkan**

**Nisbah:**
Tiada ramalan penggunaan semula TxGNN yang dihasilkan untuk Betaxolol Hidroklorida, dan jurang data menghalang berganda (profil keselamatan, ID DrugBank, MOA) tetap belum diselesaikan. Tidak ada maklumat yang mencukupi untuk menilai sebarang peluang penggunaan semula.

**Untuk meneruskan, yang berikut diperlukan:**
- **Selesaikan pemetaan DrugBank**: Betaxolol Hidroklorida berkemungkinan besar DrugBank [DB00195](https://go.drugbank.com/drugs/DB00195) — sahkan dan isi paket bukti
- **Dapatkan data MOA** daripada DrugBank untuk membolehkan analisis mekanik
- **Dapatkan maklumat keselamatan** (amaran, kontraindikasi, DDI) daripada sisipan paket atau pangkalan data kawal selia
- **Isi semula butiran lesen NPRA** (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan)
- **Sahkan input saluran TxGNN**: Sahkan bahawa Betaxolol telah dipetakan dengan betul dalam graf pengetahuan dan jalankan semula ramalan jika perlu
- **Hasilkan semula paket bukti** apabila jurang di atas telah diisi, kemudian nilai semula

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

