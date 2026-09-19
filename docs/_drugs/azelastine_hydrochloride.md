---
layout: default
title: Azelastine Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 111
evidence_level: L5
indication_count: 0
---

# Azelastine Hydrochloride
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

# Azelastina Hidroklorida: Penilaian Penghematan Ubat — Tiada Indikasi yang Diprediksi Tersedia

## Ringkasan Satu Ayat

Azelastina hidroklorida adalah antihistamin generasi kedua yang kini dipasarkan di Malaysia dengan 2 produk berdaftar. Model TxGNN **tidak menghasilkan sebarang indikasi baru yang diprediksi** untuk ubat ini, dan jurang data yang ketara masih wujud dalam maklumat peringkat ubat termasuk mekanisme tindakan, amaran keselamatan, dan teks indikasi yang diluluskan.

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|---------|
| Indikasi Asal | *(Maklumat tidak tersedia — teks indikasi lesen tidak diambil)* |
| Indikasi Baru yang Diprediksi | Tiada (tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tahan** |

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan TxGNN telah dijana untuk Azelastina Hidroklorida. Bahagian ini tidak dapat dinilai pada masa ini.

Pada masa ini, maklumat mekanisme tindakan yang terperinci tidak tersedia dalam paket bukti. Berdasarkan maklumat yang diketahui umum, azelastina adalah antihistamin derivatif ftalazinon generasi kedua dengan sifat menstabilkan sel mast. Ia biasanya digunakan untuk pelepasan simptomatik rinitis alergik (semburan hidung) dan konjunktivitis alergik (titisan mata). Ia bertindak terutamanya sebagai antagonis reseptor H1 yang selektif dan juga menghalang pelepasan histamin dan perantara inflamasi lain daripada sel mast.

Tanpa ramalan indikasi daripada TxGNN, analisis kebolehimplementasian mekanistik tidak dapat dijalankan. Ketiadaan ramalan mungkin disebabkan oleh ubat yang kekurangan ID DrugBank yang dipetakan (`drugbank_id: null`) dalam paket bukti, yang akan menghalang graf pengetahuan daripada mewujudkan pautan yang diperlukan untuk penjanaan calon penghematan ubat.

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan yang didaftarkan — tiada indikasi yang diprediksi untuk ditanyakan.

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia — tiada indikasi yang diprediksi untuk ditanyakan.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Ubat | Indikasi yang Diluluskan |
|------|------|------|------|
| *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* |
| *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* | *(Tidak diambil)* |

> **Nota:** Dua pendaftaran telah dikenalpasti oleh pertanyaan NPRA (tarikh pertanyaan: 2026-03-27), tetapi medan lesen yang terperinci (nombor kebenaran, nama produk, bentuk ubat, indikasi yang diluluskan) tidak diisi dalam paket bukti. Pengambilan semula data NPRA diperlukan.

## Pertimbangan Keselamatan

> Sila rujuk risalah paket untuk maklumat keselamatan. Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) pada masa ini tidak tersedia dalam paket bukti.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada calon penghematan ubat telah diprediksi oleh TxGNN untuk Azelastina Hidroklorida. Selain itu, jurang data yang kritikal — termasuk pemetaan ID DrugBank, teks indikasi yang diluluskan, mekanisme tindakan, dan profil keselamatan — menghalang sebarang penilaian yang bermakna. Ubat tidak boleh meneruskan saluran penghematan ubat sehingga elemen data asas ini diselesaikan.

**Untuk meneruskan, perkara berikut diperlukan:**

1. **Penyelesaian ID DrugBank** — Petakan Azelastina Hidroklorida kepada ID DrugBanknya (dijangka: DB00972) untuk membolehkan pautan graf pengetahuan dan ramalan TxGNN
2. **Pengambilan Butiran Lesen NPRA** — Tanyakan semula NPRA untuk mengisi nombor kebenaran, nama produk, bentuk ubat, dan teks indikasi yang diluluskan untuk 2 produk berdaftar
3. **Mekanisme Tindakan (MOA)** — Ambil data MOA daripada API DrugBank (Keterukan: Tinggi, per DG002)
4. **Profil Keselamatan (Risalah Paket)** — Muat turun dan analisis risalah paket untuk mengekstrak amaran dan kontraindikasi (Keterukan: Menghalang, per DG001)
5. **Jalankan Semula Ramalan TxGNN** — Selepas ID DrugBank dipetakan, jalankan semula saluran ramalan KG dan DL untuk menjana calon penghematan ubat

---

*Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Semua calon penghematan ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

