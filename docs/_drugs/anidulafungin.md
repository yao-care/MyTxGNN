---
layout: default
title: Anidulafungin
parent: Low Evidence (L4-L5)
nav_order: 76
evidence_level: L5
indication_count: 0
---

# Anidulafungin
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

# Anidulafungin: Penilaian Penggunaan Semula Ubat (Tiada Ramalan TxGNN Tersedia Pada Masa Ini)

---

## Ringkasan Satu Ayat

Anidulafungin (DB00362) ialah agen antifungal echinocandin dengan satu pendaftaran aktif di Malaysia.
Pakej Bukti semasa mengandungi **tiada ramalan penggunaan semula TxGNN** untuk ubat ini — senarai `predicted_indications` kosong — bermaksud penilaian penggunaan semula ubat standard tidak dapat diselesaikan pada peringkat ini.
Jurang data hulu yang kritikal dalam petunjuk yang diluluskan asal, mekanisme tindakan, dan profil keselamatan mesti diselesaikan sebelum saluran dapat menghasilkan output yang boleh bertindak.

---

## Gambaran Keseluruhan Cepat

| Perkara | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak tersedia dalam data semasa |
| Petunjuk Ramalan Baru | Tiada ramalan dijana |
| Skor Ramalan TxGNN | T/A |
| Tahap Bukti | T/A — tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan Disyorkan | **Tunda** |

---

## Mengapa Tiada Ramalan Dijana

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia. Berdasarkan pengklasifikasiannya dalam DrugBank (DB00362), anidulafungin termasuk dalam kelas **echinocandin** agen antifungal. Echinocandin bertindak dengan menghalang sintesis 1,3-β-D-glukan, enzim yang penting untuk integriti dinding sel fungal yang tidak mempunyai setara mamalia — memberikan kelas ubat ini profil keselamatan yang sangat selektif.

Ketiadaan ramalan TxGNN kemungkinan besar berpunca daripada satu atau lebih kegagalan hulu berikut:

1. **Tiada petunjuk yang diluluskan dimuat** — `original_indications` ialah senarai kosong, yang mungkin telah menghalang ubat daripada dilabuh dengan betul dalam graf pengetahuan.
2. **Data MOA hilang** — tanpa anotasi mekanik, traversal berasaskan graf yang digunakan oleh TxGNN mungkin tidak menemui nod penyakit calon melampaui ambang pelaporan.
3. **Medan butiran lesen kosong** — walaupun 1 pendaftaran NPRA wujud, semua medan berstruktur (nama produk, bentuk dos, teks petunjuk yang diluluskan) mengembalikan rentetan kosong, mencadangkan kegagalan penghuraian atau penarikan data pada langkah pertanyaan NPRA.

Sehingga input ini diperbetulkan dan saluran ramalan dijalankan semula, tiada calon penggunaan semula ubat dapat dinilai.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------------------|--------------|-------------|---------------------|
| Tidak dikembalikan | Tidak dikembalikan | Tidak dikembalikan | Tidak dikembalikan |

> Walaupun pertanyaan NPRA pada 2026-03-27 mengembalikan `result_count` 1, semua medan berstruktur dalam rekod lesen kosong. Respons mentah daripada NPRA harus diperiksa untuk menentukan sama ada isu adalah ketidaksesuaian pemetaan medan dalam `config/fields.yaml` atau masalah kualiti data hulu dalam pangkalan data NPRA itu sendiri.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini ditandai sebagai jurang data atau mengembalikan kosong. Pertanyaan DDI mengembalikan interaksi sifar dengan status `not_found`. Tiada ringkasan keselamatan dapat dihasilkan sehingga sisipan pakej diambil dan diuraikan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunda**

**Rasional:**
Saluran TxGNN menghasilkan sifar calon penggunaan semula ubat untuk anidulafungin, dan setiap input data kritikal — petunjuk yang diluluskan, mekanisme tindakan, amaran keselamatan, dan butiran lesen NPRA — pada masa ini tidak tersedia. Tiada asas bukti untuk membuat cadangan penggunaan semula ubat.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Menghalang — DG001]** Muat turun dan uraikan PDF sisipan pakej NPRA/TFDA untuk mengekstrak petunjuk yang diluluskan, amaran utama, dan kontraindikasi; tanpanya, pra-pemeriksaan keselamatan (pintu S1) tidak dapat dimulai
- **[Tinggi — DG002]** Pertanyaan API DrugBank untuk mekanisme tindakan anidulafungin (DB00362) untuk membolehkan analisis relevansi mekanik
- **[Tinggi]** Selidiki mengapa rekod lesen NPRA tunggal mengembalikan semua medan kosong — periksa pemetaan medan dalam `config/fields.yaml` terhadap struktur respons NPRA sebenar dan betulkan pengurai dalam `scripts/process_fda_data.py`
- **[Tinggi]** Jalankan semula `scripts/run_kg_prediction.py` selepas mengisi medan petunjuk asal dan MOA; sahkan bahawa anidulafungin (DB00362) hadir dan dipetakan dengan betul dalam `data/external/drugbank_vocab.csv`
- **[Sederhana]** Setelah ramalan tersedia, kumpulkan bukti ujian klinikal dan literatur PubMed untuk petunjuk ramalan peringkat teratas dan keluarkan semula laporan ini pada Tahap Bukti L2 atau lebih tinggi sebelum mana-mana keputusan pergi/tidak pergi

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

