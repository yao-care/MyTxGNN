---
layout: default
title: Bedaquiline Fumarate
parent: Low Evidence (L4-L5)
nav_order: 122
evidence_level: L5
indication_count: 0
---

# Bedaquiline Fumarate
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

# Bedaquiline Fumarate: Penilaian Penggunaan Semula Ubat — Tiada Indikasi Baru yang Diramalkan

## Ringkasan Satu Ayat

Bedaquiline fumarate adalah ubat yang dipasarkan di Malaysia dengan 1 lesen berdaftar; bagaimanapun, teks indikasi yang diluluskan tidak ditangkap dalam pengekstrakan data semasa. Model TxGNN **tidak menghasilkan sebarang ramalan penggunaan semula** untuk sebatian ini, dan jurang data yang ketara kekal dalam keselamatan, mekanisme tindakan, dan perincian kawal selia, menghalang penilaian bermakna pada masa ini.

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | *(Tidak ditangkap dalam data semasa — lihat Jurang Data di bawah)* |
| Indikasi Baru yang Diramalkan | **Tiada** — TxGNN tidak mengembalikan sebarang ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | **L5** (Tiada ramalan, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

## Mengapa Tiada Ramalan yang Dijana?

Bedaquiline fumarate adalah agen antimikobakteri diarilkuinolin yang terutamanya ditunjukkan untuk rawatan tuberkulosis yang tahan terhadap pelbagai ubat (MDR-TB). Ia berfungsi dengan menghalang sintase ATP mikobakteri, mekanisme yang sangat spesifik kepada *Mycobacterium tuberculosis*.

Model graf pengetahuan TxGNN mengembalikan **sifar calon penggunaan semula** untuk ubat ini. Beberapa faktor mungkin menjelaskan perkara ini:

1. **Pemetaan ID DrugBank yang hilang**: Pek bukti menunjukkan `drugbank_id: null`. Tanpa pengenalan DrugBank yang sah, ubat tidak boleh dilokalkan dalam graf pengetahuan TxGNN (yang bergantung pada nod DrugBank), secara berkesan mengecualikannya daripada saluran ramalan.

2. **Kekhususan mekanisme yang sempit**: Sasaran bedaquiline — sintase ATP mikobakteri — adalah berbeza daripada struktur sintase ATP mitokondrion manusia. Kekhususan sasaran tinggi ini mungkin mengehadkan keupayaan model untuk mengenali tepi penyakit–ubat yang munasabah dalam graf pengetahuan.

3. **Data input yang tidak lengkap**: Teks indikasi asal, MOA, dan medan keselamatan semuanya hilang atau ditandai sebagai `[Jurang Data]`, seterusnya mengurangkan maklumat yang tersedia untuk ramalan.

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan penggunaan semula untuk dilaporkan, kerana tiada indikasi baru yang diramalkan.

## Bukti Literatur

Pada masa ini tiada bukti literatur berkaitan penggunaan semula untuk dilaporkan, kerana tiada indikasi baru yang diramalkan.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(Tidak ditangkap)* | *(Tidak ditangkap)* | *(Tidak ditangkap)* | *(Tidak ditangkap)* |

> **Nota:** Soalan NPRA mengembalikan 1 lesen (tarikh soalan: 2026-03-27), tetapi medan perincian lesen (nombor, nama produk, bentuk dos, indikasi) tidak diisi semasa pengekstrakan data. Pengesahan manual pada [pangkalan data NPRA Quest](https://quest3plus.bpfk.gov.my/) disyorkan.

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) tidak tersedia dalam pek bukti semasa.

## Ringkasan Jurang Data

Jurang data kritikal berikut telah dikenal pasti dan harus diselesaikan sebelum penilaian semula:

| ID Jurang | Item | Keterukan | Kesan | Pembetulan |
|--------|------|----------|--------|-------------|
| DG001 | Amaran Label TFDA / Kontraindikasi | **Menghalang** | Tidak boleh memasuki saringan keselamatan S1 | Muat turun dan huraikan PDF label daripada laman web pihak berkuasa kawal selia |
| DG002 | Mekanisme Tindakan (MOA) | **Tinggi** | Menjejaskan analisis kerelevanan mekanisme–indikasi | Kueri API DrugBank (bedaquiline → DB09034) |
| — | ID DrugBank | **Tinggi** | Ubat dikecualikan daripada graf pengetahuan TxGNN | Petakan BEDAQUILINE FUMARATE → DB09034 dan jalankan semula ramalan |
| — | Teks Indikasi yang Diluluskan | **Sederhana** | Tidak boleh menetapkan indikasi asas | Kueri semula NPRA atau ekstrak daripada label produk |

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada calon penggunaan semula yang dijana oleh TxGNN, kemungkinan besar kerana ubat tidak dapat dipetakan ke dalam graf pengetahuan (ID DrugBank yang hilang). Beberapa jurang data kritis menghalang penilaian keselamatan. Calon ini tidak boleh diteruskan sehingga data asas diselesaikan.

**Untuk meneruskan, berikut diperlukan:**
- Selesaikan pemetaan ID DrugBank (bedaquiline fumarate → **DB09034**) dan jalankan semula saluran ramalan TxGNN
- Ekstrak teks indikasi yang diluluskan daripada label produk NPRA atau pangkalan data Quest
- Dapatkan sisipan pakej untuk melengkapkan data amaran keselamatan, kontraindikasi, dan interaksi ubat
- Hasilkan semula pek bukti dengan medan lengkap sebelum penilaian semula

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

