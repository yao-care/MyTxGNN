---
layout: default
title: Antazoline Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 78
evidence_level: L5
indication_count: 0
---

# Antazoline Hydrochloride
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

# Antazoline Hydrochloride: Penilaian Penggunaan Semula Ubat — Tiada Ramalan TxGNN Tersedia

## Ringkasan Satu Ayat

Antazoline hydrochloride adalah antihistamin generasi pertama dengan sifat penyekatan alfa-adrenergik tambahan, secara klasiknya digunakan dalam formulasi oftalmik untuk konjunktivitis alergik.
Model TxGNN **tidak menghasilkan sebarang ramalan penggunaan semula** untuk ubat ini dalam pelaksanaan semasa, berkemungkinan disebabkan oleh pautan DrugBank ID yang hilang diperlukan untuk pentarsuran graf pengetahuan.
Tanpa skor ramalan atau petunjuk calon, penilaian ini terhad kepada penilaian kesempurnaan data dan kawal selia sahaja.

---

## Gambaran Keseluruhan Ringkas

| Perkara | Kandungan |
|---------|-----------|
| Indikasi Asal | Tidak tersedia dalam rekod kawal selia semasa |
| Indikasi Baru yang Diramal | Tiada — TxGNN tidak mengembalikan sebarang calon |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | Tidak mencukupi — tiada ramalan dihasilkan |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan Dihasilkan

Antazoline hydrochloride adalah antihistamin generasi pertama (antagonis reseptor H1) yang juga mempamerkan aktiviti penyekatan alfa-adrenergik sederhana. Ia biasanya diformulasikan sebagai titisan oftalmik (sering dikombinasikan dengan naphazoline atau xylometazoline) untuk menghilangkan konjunktivitis alergik, dan telah mengalami kajian sejarah sebagai agen antiaritmia Kelas Ia.

Enjin graf pengetahuan TxGNN memetakan ubat melalui **DrugBank ID** mereka untuk pentarsuran hubungan penyakit–ubat–gen–laluan. Dalam Pakej Bukti ini, `drugbank_id` adalah **null**, bermakna entiti ubat tidak dapat diancurkan dalam graf pengetahuan. Tanpa sauh ini, skor penggunaan semula berasaskan KG mahupun berasaskan pembelajaran mendalam tidak dapat dikira.

Selain itu, data mekanisme tindakan (MOA) tidak tersedia dalam pakej semasa. Secara mekanik, antihistamin dalam kelas ini telah diterokai dalam konteks seperti alergi saluran pernafasan atas, insomnia (kesan sedatif), dan penyakit gerakan — tetapi ini tetap merupakan arah yang belum disahkan tanpa skor ramalan TxGNN formal untuk menilai.

---

## Maklumat Pasaran Malaysia

Data kawal selia semasa mengembalikan **1 lesen aktif**, tetapi medan rekod lesen (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) tidak diisi dalam pengekstrakan Pakej Bukti ini. Status pasaran disahkan sebagai **Dipasarkan (Dipasarkan)**.

| Perkara | Status |
|---------|--------|
| Status Pasaran | ✓ Dipasarkan di Malaysia |
| Jumlah Lesen Aktif | 1 |
| Butiran Lesen | Rekod wujud tetapi medan tidak diisi — carian manual NPRA diperlukan |

> Untuk mendapatkan butiran lesen lengkap, cari pangkalan data Pendaftaran Produk NPRA di [https://www.npra.gov.my](https://www.npra.gov.my) menggunakan bahan aktif "ANTAZOLINE HYDROCHLORIDE".

---

## Pertimbangan Keselamatan

Sila merujuk sisipan pakej untuk maklumat keselamatan.

> Nota: Kedua-dua amaran utama dan kontraindikasi ditandai sebagai jurang data dalam Pakej Bukti ini (keterukan: **Penghalang** dan **Tinggi** masing-masing). Tiada rekod interaksi ubat–ubat ditemui dalam pertanyaan DDI. Menyelesaikan jurang ini diperlukan sebelum sebarang laluan penggunaan semula dapat diteruskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Model TxGNN tidak mengembalikan sebarang calon penggunaan semula untuk antazoline hydrochloride kerana pautan DrugBank ID hilang, mencegah pentarsuran graf pengetahuan sepenuhnya. Tanpa sasaran ramalan, penilaian bukti tidak dapat dimulakan.

**Untuk melanjutkan, perkara berikut diperlukan:**

- **[Kritikal — Penghalang]** Selesaikan `drugbank_id`: Cari DrugBank (https://www.drugbank.ca) untuk "antazoline" dan sahkan ID yang betul (berkemungkinan DB01114 atau serupa); kemas kini Pakej Bukti dan jalankan semula saluran ramalan TxGNN
- **[Kritikal — Penghalang]** Dapatkan sisipan pakej TFDA/NPRA: Muat turun PDF sisipan produk yang diluluskan dan ekstrak amaran, kontraindikasi, dan teks indikasi yang diluluskan untuk membuka kunci skrin keselamatan S1
- **[Tinggi]** Isikan data MOA: Pertanyaan API DrugBank untuk farmakodinamik dan mekanisme tindakan untuk membolehkan analisis kebolehpercayaan mekanik setelah indikasi yang diramal tersedia
- **[Sederhana]** Isikan medan rekod lesen NPRA: Sahkan nombor kebenaran, nama produk, bentuk dos, pengilang, dan teks indikasi yang diluluskan daripada daftar NPRA
- **[Susulan]** Jalankan semula penjanaan Pakej Bukti selepas DrugBank ID disahkan dan serahkan semula untuk penilaian laporan lengkap

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

