---
layout: default
title: Activated Charcoal
parent: Low Evidence (L4-L5)
nav_order: 24
evidence_level: L5
indication_count: 0
---

# Activated Charcoal
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

# Activated Charcoal: Agen Adsorpsi Toksin Kecemasan — Tiada Prediksi TxGNN Tersedia

## Ringkasan Satu Ayat

Activated charcoal adalah adsorben gastrointestinal spektrum luas yang digunakan terutamanya dalam pengurusan kecemasan untuk menangani keracunan akut dan overdosis ubat.
Analisis TxGNN semasa tidak menunjukkan sebarang indikasi baru yang diramalkan untuk ubat ini.
Akibatnya, penilaian formal untuk penggunaan ubat bagi indikasi baru tidak dapat diselesaikan tanpa menjalankan semula saluran paip ramalan dengan data input yang lengkap.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Keracunan akut / Adsorpsi toksin (penggunaan kecemasan) |
| Indikasi Baru Yang Diramalkan | Tiada — tiada prediksi TxGNN dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 (tiada prediksi atau kajian sokongan diperolehi) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan Yang Disyorkan | Tangguhkan |

---

## Mengapa Tiada Prediksi Tersedia

Tatasusunan `predicted_indications` dalam Pakej Bukti ini kosong. Ini biasanya berlaku untuk satu atau lebih daripada sebab-sebab berikut:

1. **Kegagalan pemetaan**: Activated charcoal mungkin belum dipadankan dengan nod dalam graf pengetahuan TxGNN. Kerana ia adalah adsorben fizikal bukan spesifik dan bukannya molekul kecil bertarget, ia mungkin kekurangan jejak farmakologi (pengikatan reseptor, sasaran enzimatik) yang diperlukan untuk pemarkahan kesamaan berasaskan graf.

2. **Penapisan ambang skor**: Sebarang ramalan calon mungkin telah dialih keluar oleh ambang pemotongan skor pemprosesan pasca sebelum mencapai laporan ini.

3. **Ketidaklengkapan saluran paip**: Pakej Bukti telah ditandai dengan dua jurang data menghalang/keterukan tinggi (DG001: amaran TFDA, DG002: MOA), yang mungkin telah menghentikan langkah ramalan hiliran.

Sehingga saluran paip ramalan dijalankan semula dengan jurang data yang diselesaikan, tidak ada hipotesis penggunaan ubat bagi indikasi baru yang akan dinilai.

---

## Maklumat Pasaran Malaysia

Tiga pendaftaran produk disahkan dalam pangkalan data NPRA, namun rekod lesen terperinci (nama produk, bentuk dos, indikasi yang diluluskan) tidak diperolehi dalam pengambilan data ini.

| Item | Status |
|------|--------|
| Bilangan Produk Berdaftar | 3 |
| Status Pasaran | ✓ Dipasarkan |
| Rekod Lesen Terperinci | Tidak diperolehi — memerlukan pertanyaan rekod NPRA yang disasarkan |

Untuk mengisi jadual lesen penuh, lakukan pertanyaan semula pada portal NPRA dengan nombor pendaftaran produk individu yang berkaitan dengan DB09278.

---

## Pertimbangan Keselamatan

Sila rujuk selebaran produk untuk maklumat keselamatan.

> **Nota**: Amaran selebaran produk TFDA/kontraindikasi (DG001, keterukan: Menghalang) dan data interaksi ubat tidak terdapat dalam Pakej Bukti ini. Perkara ini mesti diselesaikan sebelum sebarang penilaian keselamatan dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguhkan**

**Alasan:**
Tiada indikasi yang diramalkan TxGNN untuk dinilai, dan dua jurang data yang kritikal (MOA dan teks keselamatan kawal selia) tetap tidak diselesaikan, menjadikan ia mustahil untuk menilai sama ada kelayakan mekanistik atau keselamatan pada peringkat ini.

**Untuk meneruskan, perkara-perkara berikut diperlukan:**

- **Selesaikan DG001 (Menghalang)**: Muat turun dan huraikan PDF selebaran produk TFDA untuk mengeluarkan indikasi yang diluluskan, amaran, dan kontraindikasi.
- **Selesaikan DG002 (Tinggi)**: Pertanyakan API DrugBank untuk DB09278 untuk mendapatkan mekanisme tindakan, kategori ubat, dan data toksisiti.
- **Jalankan semula saluran paip ramalan TxGNN**: Selepas mengesahkan bahawa activated charcoal memetakan dengan betul kepada nod graf pengetahuan, jalankan semula `run_kg_prediction.py` untuk menjana calon penggunaan ubat yang berdiskor.
- **Sahkan butiran lesen NPRA**: Perolehi tiga rekod pendaftaran produk sepenuhnya (nama produk, bentuk dos, teks indikasi yang diluluskan) daripada pangkalan data NPRA.
- **Sahkan kelayakan nod KG**: Tentukan sama ada activated charcoal diwakili sebagai nod yang dapat diselesaikan dalam graf pengetahuan TxGNN (`data/node.csv`); jika tidak wujud, nilai sama ada sebatian pengganti atau pemegang tempat tahap mekanisme boleh digunakan.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

