---
layout: default
title: Dobutamine Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 291
evidence_level: L5
indication_count: 0
---

# Dobutamine Hydrochloride
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

# Dobutamine Hydrochloride: Laporan Penilaian Tujuan Baru Ubat

## Ringkasan Satu Ayat

Dobutamine hydrochloride ialah katekholamin sintetik dan agonis adrenergik beta-1, yang digunakan secara meluas sebagai agen inotrop jangka pendek untuk dekompensasi jantung. Model TxGNN **tidak menjana sebarang petunjuk baru yang diramalkan** untuk ubat ini, dan pakej bukti mengandungi jurang data yang signifikan merentasi domain kawal selia, keselamatan, dan mekanis. Laporan ini berfungsi sebagai **penilaian jurang data** untuk membimbing pengumpulan data seterusnya.

---

## Gambaran Pantas

| Perkara | Kandungan |
|------|------|
| Petunjuk Asal | Tidak tersedia dalam dataset semasa (kegunaan yang diketahui: sokongan inotrop jangka pendek dalam dekompensasi jantung) |
| Petunjuk Baru yang Diramalkan | **Tiada** — Tiada ramalan TxGNN dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **L5** (Tiada ramalan atau kajian yang menyokong) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 4 |
| Keputusan yang Dicadangkan | **Tahan** |

---

## Mengapa Ramalan Ini Masuk Akal?

Pada masa kini, model TxGNN belum menjana sebarang calon tujuan baru untuk dobutamine hydrochloride. Ini mungkin disebabkan oleh satu atau lebih daripada sebab-sebab berikut:

1. **Pemetaan ID DrugBank yang hilang**: Pakej bukti menunjukkan `drugbank_id: null`. Tanpa pengecam DrugBank yang sah, ubat tidak dapat dilabur dengan betul dalam graf pengetahuan TxGNN, menghalang model daripada menjana ramalan persatuan penyakit. Log pertanyaan menunjukkan pencarian DrugBank telah dijalankan dan mengembalikan 1 keputusan, tetapi ID tidak berjaya dikaitkan dengan rekod ini.

2. **Profil terapeutik yang sempit**: Dobutamine ialah agonis adrenergik beta-1 selektif yang digunakan terutamanya sebagai inotrop intravena untuk sokongan jantung akut. Mekanismenya — merangsang kontraktiliti jantung melalui reseptor beta-1 — adalah sangat khusus dan mungkin mempunyai kebolehgunaan silang penyakit yang terhad dalam struktur relasional graf pengetahuan.

3. **Jurang data dalam pakej bukti**: Teks MOA asal, petunjuk yang diluluskan, dan data keselamatan semuanya hilang, yang mengehadkan keupayaan sistem untuk melakukan penalaran mekanis dan inferensi persatuan silang.

Sebelum membuat kesimpulan tentang potensi tujuan baru dobutamine, jurang data yang dikenal pasti di bawah mesti diselesaikan.

---

## Maklumat Pasaran Malaysia

Pakej bukti merekodkan **4 pendaftaran** untuk dobutamine hydrochloride dengan status pasaran "Dipasarkan". Walau bagaimanapun, maklumat pendaftaran terperinci (nombor kebenaran, nama produk, bentuk dos, dan petunjuk yang diluluskan) tidak tersedia dalam dataset semasa.

> **Tindakan diperlukan**: Ambil butiran pendaftaran penuh daripada pangkalan data NPRA untuk melengkapkan bahagian ini.

---

## Pertimbangan Keselamatan

> Sila rujuk leaflet ubat untuk maklumat keselamatan.

**Nota**: Jurang data kritikal berikut telah dikenal pasti:
- **Amaran Utama**: Tidak tersedia — data leaflet ubat TFDA/NPRA belum diuraikan
- **Kontraindikasi**: Tidak tersedia — muat turun PDF leaflet ubat dan penguraian diperlukan
- **Interaksi Ubat**: Pertanyaan DDI DrugBank mengembalikan tiada keputusan (status pertanyaan: `not_found`)

---

## Ringkasan Jurang Data

Jurang data yang menyekat dan berseveriti tinggi berikut mesti ditangani sebelum calon ini dapat meneruskan melalui saluran penilaian:

| ID Jurang | Kategori | Perkara | Severiti | Pemulihan |
|--------|----------|------|----------|-------------|
| DG001 | Peringkat Ubat | Amaran/kontraindikasi leaflet ubat | **Menyekat** | Muat turun dan urai PDF leaflet ubat daripada laman web pihak berkuasa kawal selia |
| DG002 | Peringkat Ubat | Mekanisme Tindakan (MOA) | **Tinggi** | Pertanyaan API DrugBank menggunakan INN "dobutamine" |
| — | Peringkat Ubat | ID DrugBank | **Tinggi** | Kaitkan keputusan pencarian DrugBank (1 hit ditemui) dengan rekod ini |
| — | Peringkat Ramalan | Ramalan TxGNN | **Tinggi** | Jalankan semula saluran ramalan selepas ID DrugBank diselesaikan |
| — | Peringkat Kawal Selia | Butiran Lesen (nombor kebenaran, nama produk, petunjuk) | **Sederhana** | Pertanyaan semula NPRA dengan medan yang diperluas |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan tujuan baru TxGNN dijana untuk dobutamine hydrochloride, terutamanya disebabkan oleh pautan ID DrugBank yang hilang yang menghalang penyepaduan graf pengetahuan. Selain itu, pelbagai jurang data yang menyekat dalam maklumat keselamatan dan kawal selia menghalang sebarang penilaian bermakna pada peringkat ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Selesaikan **pemetaan ID DrugBank** (log pertanyaan menunjukkan 1 keputusan ditemui — sahkan dan kaitkan `DB00841` untuk dobutamine)
- Jalankan semula **saluran ramalan TxGNN** setelah ID DrugBank dikaitkan dengan betul
- Muat turun dan urai **PDF leaflet ubat** untuk melengkapkan amaran keselamatan dan kontraindikasi
- Pertanyaan semula **NPRA** untuk mendapatkan butiran lesen penuh (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan)
- Setelah ramalan tersedia, kumpulkan **bukti ujian klinik** dan **bukti literatur** untuk petunjuk calon baris teratas

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

