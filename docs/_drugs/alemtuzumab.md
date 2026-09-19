---
layout: default
title: Alemtuzumab
parent: Low Evidence (L4-L5)
nav_order: 38
evidence_level: L5
indication_count: 0
---

# Alemtuzumab
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

# Alemtuzumab: Penilaian Ditangguhkan — Tiada Petunjuk Indikasi yang Diramalkan

---

## Ringkasan Satu Ayat

Alemtuzumab (DrugBank ID: DB00087) disahkan sebagai produk yang dipasarkan di Malaysia dengan sekurang-kurangnya satu pendaftaran produk aktif.
Bagaimanapun, penilaian ini **tidak dapat diselesaikan** kerana Evidence Pack tidak mengandungi calon penggunaan semula yang diramalkan oleh TxGNN, dan dua jurang data yang kritikal — mekanisme tindakan yang hilang (DG002) dan amaran keselamatan/kontraindikasi yang hilang (DG001, Blocking severity) — tetap belum diselesaikan.
Tiada keputusan penggunaan semula boleh diberikan sehingga jurang-jurang ini diisi.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak tersedia dalam Evidence Pack ini |
| Indikasi Baru yang Diramalkan | Tiada — tiada calon penggunaan semula yang diramalkan oleh TxGNN |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A (tiada calon penggunaan semula untuk dinilai) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tangguh** |

---

## Mengapa Ramalan Ini Munasabah?

Tidak terpakai — tatasusunan `predicted_indications` adalah kosong dalam Evidence Pack ini. TxGNN tidak mengembalikan sebarang calon penggunaan semula untuk Alemtuzumab di bawah konfigurasi data semasa. Tanpa indikasi sasaran yang diramalkan, tiada analisis keselamatan mekanis boleh dijalankan.

Menambah masalah ini, mekanisme tindakan ubat itu ditandakan sebagai jurang data tahap keterukan tinggi (DG002). Tanpa data MOA, malah penilaian kualitatif kemungkinan indikasi baru tidak boleh dicuba.

Tiga langkah prasyarat mesti diselesaikan sebelum bahagian ini boleh diisi:
1. Jalankan semula saluran ramalan TxGNN untuk Alemtuzumab dan sahkan sekurang-kurangnya satu calon penyakit dikembalikan.
2. Dapatkan MOA daripada DrugBank API (pemulihan DG002).
3. Selesaikan amaran keselamatan TFDA/NPRA dan kontraindikasi (pemulihan DG001, pada masa ini Blocking).

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan berdaftar — tiada indikasi yang diramalkan tersedia untuk dicari.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan tersedia — tiada indikasi yang diramalkan tersedia untuk dicari.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|------------------|------------|-----------|-------------------|
| (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) | (Tidak disediakan) |

> **Nota:** Pertanyaan NPRA (Query Log ID 1, dilaksanakan 2026-03-27) mengesahkan 1 lesen aktif dan `market_status: Marketed` (Dipasarkan). Bagaimanapun, semua medan butiran lesen — nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan — adalah kosong dalam Evidence Pack semasa. Butiran lesen lengkap harus diambil terus daripada pangkalan data pendaftaran produk NPRA.

---

## Sitotoksisiti

Alemtuzumab adalah antibodi monoklonal anti-CD52. Berdasarkan kelas farmakologi yang diketahuinya (antibodi monoklonal yang menyasarkan CD52 yang digunakan secara sejarah dalam indikasi onkologi seperti leukemia limfositik kronik), bahagian ini disertakan secara tentatif. Pengesahan rasmi pengelasan antineoplastik memerlukan data kategori DrugBank, yang pada masa ini tidak tersedia (DG002).

| Item | Kandungan |
|------|-----------|
| Pengelasan Sitotoksisiti | Terapi biologi yang disasarkan (Antibodi monoklonal anti-CD52) — menunggu pengesahan kategori DrugBank |
| Risiko Supresi Sumsum Tulang | Sila rujuk amaran pakej sisipan dan prekausi |
| Pengelasan Emetogenisiti | Sila rujuk amaran pakej sisipan dan prekausi |
| Item Pemantauan | Sila rujuk amaran pakej sisipan dan prekausi |
| Perlindungan Pengendalian | Sila rujuk amaran pakej sisipan dan prekausi |

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Semua medan keselamatan — amaran utama, kontraindikasi, dan interaksi ubat-ubat — adalah sama ada jurang data atau tidak mengembalikan sebarang hasil dalam Evidence Pack ini. DG001 (amaran/kontraindikasi TFDA) diklasifikasikan sebagai **Blocking severity**, bermakna tiada pemeriksaan keselamatan boleh diteruskan sehingga data ini diambil. Laluan pemulihan: muat turun dan analisis PDF sisipan pakej TFDA.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguh**

**Nisbah:**
Tiada indikasi yang diramalkan oleh TxGNN dikembalikan untuk Alemtuzumab, dan dua jurang data kritikal (DG001: maklumat keselamatan, Blocking; DG002: MOA, High) menghalang sebarang penilaian penggunaan semula atau keselamatan yang bermakna daripada diteruskan.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Blocking] Selesaikan DG001:** Muat turun PDF sisipan pakej TFDA/NPRA dan ekstrak amaran dan kontraindikasi utama sebelum sebarang pemeriksaan keselamatan boleh dimulai.
- **[High] Selesaikan DG002:** Pertanyaan DrugBank API untuk Alemtuzumab (DB00087) untuk mendapatkan data mekanisme tindakan, diperlukan untuk analisis keselarasan mekanis.
- **[Critical] Jalankan semula ramalan TxGNN:** Selidiki mengapa `predicted_indications` mengembalikan tatasusunan kosong — periksa sama ada ID DrugBank Alemtuzumab hadir dalam senarai nod graf pengetahuan dan jalankan semula saluran ramalan.
- **[Required] Selesaikan butiran lesen NPRA:** Dapatkan nama produk, bentuk dos, nombor kebenaran, dan teks indikasi yang diluluskan untuk 1 produk Malaysia yang terdaftar.
- **[Subsequent]** Apabila indikasi yang diramalkan dikenalpasti, jalankan carian bukti yang disasarkan pada ClinicalTrials.gov dan PubMed, dan tetapkan semula tahap bukti (L1–L5).

---

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Semua calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

