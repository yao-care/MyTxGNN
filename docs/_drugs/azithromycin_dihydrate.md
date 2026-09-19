---
layout: default
title: Azithromycin Dihydrate
parent: Low Evidence (L4-L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Azithromycin Dihydrate
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

# Azithromycin Dihydrate: Laporan Penilaian Pengguna Semula Ubat

## Ringkasan Satu Ayat

Azithromycin dihydrate ialah antibiotik makrolida yang digunakan secara meluas untuk rawatan jangkitan bakteria, dengan 39 pendaftaran yang sedang aktif di Malaysia. Model TxGNN telah **tidak menjana sebarang petunjuk baru yang diramalkan** untuk ubat ini pada masa ini, dan jurang data kritikal (mekanisme tindakan, profil keselamatan) tetap tidak diselesaikan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|---------|
| Petunjuk Asal | Tidak tersedia (teks petunjuk lesen tidak disediakan) |
| Petunjuk Baru Diramalkan | **Tiada** — TxGNN tidak mengembalikan sebarang ramalan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 (Tiada ramalan, tiada kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 39 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, model TxGNN tidak menghasilkan sebarang ramalan pengguna semula untuk Azithromycin Dihydrate. Ini mungkin disebabkan oleh satu atau lebih daripada alasan-alasan berikut:

1. **Pemetaan ID DrugBank yang Hilang**: Pakej bukti menunjukkan `drugbank_id: null`. Tanpa pengenalan DrugBank yang sah, ubat tidak dapat ditempatkan dengan betul dalam graf pengetahuan TxGNN, yang bergantung pada nod DrugBank untuk mewujudkan hubungan ubat–penyakit. Log pertanyaan menunjukkan pencarian DrugBank telah dilakukan dan mengembalikan 1 hasil, tetapi pemetaan ini tidak berjaya diintegrasikan ke dalam pakej bukti.

2. **Data Mekanisme Tindakan yang Tidak Lengkap**: Data MOA terperinci tidak tersedia dalam pakej bukti ini. Azithromycin diketahui sebagai antibiotik makrolida yang menghalang sintesis protein bakteria dengan mengikat subunit ribosom 50S. Selain aktiviti antimikrobanya, azithromycin mempunyai sifat imunomodulatori dan anti-inflamasi yang didokumenkan, yang telah mendorong penyiasatan dalam keadaan seperti penyakit paru obstruktif kronik (COPD), fibrosis kistik, dan COVID-19. Walau bagaimanapun, tanpa data MOA yang terikat secara formal dalam graf pengetahuan, model tidak dapat memanfaatkan sambungan mekanik ini.

3. **Jurang Integrasi Data**: Teks petunjuk yang diluluskan untuk semua 39 pendaftaran Malaysia kosong, bermakna saluran paip tidak dapat mengeluarkan konteks terapeutik asal yang diperlukan untuk penalaran berasaskan petunjuk.

---

## Bukti Uji Klinikal

Pada masa ini tiada petunjuk yang diramalkan tersedia; oleh itu, tiada carian uji klinikal tertarget yang dijalankan.

---

## Bukti Kesusasteraan

Pada masa ini tiada petunjuk yang diramalkan tersedia; oleh itu, tiada carian kesusasteraan tertarget yang dijalankan.

---

## Maklumat Pasaran Malaysia

Pangkalan data NPRA mengembalikan 39 pendaftaran untuk Azithromycin Dihydrate; bagaimanapun, maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan petunjuk yang diluluskan) tidak ditangkap dalam pakej bukti ini.

| Item | Kandungan |
|------|---------|
| Jumlah Pendaftaran | 39 |
| Butiran Produk | Tidak tersedia — medan data lesen kosong |

> **Catatan:** Untuk melengkapkan bahagian ini, pangkalan data NPRA Quest (https://quest3plus.bpfk.gov.my/) harus disiasat semula untuk mendapatkan butiran pendaftaran produk lengkap.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti ini.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Model TxGNN tidak menghasilkan sebarang ramalan pengguna semula untuk Azithromycin Dihydrate. Ini terutamanya boleh dikaitkan dengan pemetaan ID DrugBank yang hilang dan ketiadaan teks petunjuk yang diluluskan, yang bersama-sama mencegah graf pengetahuan daripada mewujudkan kedudukan ubat dalam rangkaian penyakit–ubat. Tiada penilaian potensi pengguna semula dapat diteruskan sehingga jurang data asas ini diselesaikan.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Selesaikan pemetaan DrugBank** — Soal API DrugBank untuk "Azithromycin" (DB00207) dan pautkannya ke pakej bukti. Log pertanyaan mengesahkan padanan wujud tetapi tidak diintegrasikan.
2. **Keluarkan Semula Data Lesen NPRA** — Soal semula pangkalan data NPRA Quest untuk mengisi nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan untuk semua 39 pendaftaran.
3. **Dapatkan Data MOA** — Dapatkan mekanisme tindakan daripada DrugBank (antibiotik makrolida; perencatan subunit ribosom 50S; sifat imunomodulatori).
4. **Dapatkan Profil Keselamatan** — Muat turun dan analisis sisipan pakej (PIL) daripada NPRA untuk mengeluarkan amaran utama, kontraindikasi, dan interaksi ubat.
5. **Jalankan Semula Ramalan TxGNN** — Sebaik sahaja ID DrugBank dan data petunjuk diintegrasikan, jalankan semula saluran paip ramalan KG dan DL untuk menjana calon pengguna semula.

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon pengguna semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

