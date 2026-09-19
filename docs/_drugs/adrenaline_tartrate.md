---
layout: default
title: Adrenaline Tartrate
parent: Low Evidence (L4-L5)
nav_order: 31
evidence_level: L5
indication_count: 0
---

# Adrenaline Tartrate
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

# Adrenalin Tartrat: Penilaian Repositioning Ubat (Data Ramalan Tertangguh)

## Ringkasan Satu Ayat

Adrenalin Tartrat (epinefrin tartrat) ialah katekolamin simpatomiemetik yang bertindak langsung, digunakan terutamanya dalam situasi kecemasan untuk anafilaksis, henti jantung, dan bronkospasma teruk.
Tiada petunjuk repositioning baru telah dijana oleh model TxGNN pada masa ini, kerana dua jurang data kritikal — pemetaan ID DrugBank yang hilang dan data mekanisme tindakan — menghalang saluran ramalan daripada berjalan.
Penilaian repositioning lengkap tidak boleh diselesaikan sehingga jurang-jurang ini diselesaikan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Penggunaan kecemasan: anafilaksis, henti jantung, bronkospasma teruk |
| Petunjuk Baru Diramal | Tidak tersedia |
| Skor Ramalan TxGNN | Tidak tersedia |
| Tahap Bukti | Tidak boleh dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 5 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Belum Tersedia?

Adrenalin Tartrat ialah bentuk garam tartrat epinefrin, hormon katekolamin yang terkenal dan neurotransmiter. Secara farmakologi, ia bertindak sebagai agonis kuat pada kedua-dua reseptor α-adrenergik (vasokonstriksi, miadrisis) dan reseptor β-adrenergik (bronkodilatasi, kronotropi positif dan inotropi), menjadikannya tidak dapat digantikan dalam keadaan darurat yang mengancam nyawa.

Walau bagaimanapun, Pakej Bukti ini dihasilkan tanpa ID DrugBank yang diselesaikan, yang merupakan pengecam utama yang diperlukan untuk menambat ubat dalam grafik pengetahuan TxGNN. Tanpa pautan ini, langkah-langkah ramalan grafik-pengetahuan (KG) dan pembelajaran mendalam (DL) tidak boleh dilaksanakan, dan tiada petunjuk calon baru dikembalikan.

Secara mekanisme, profil adrenergik adrenalin yang luas memang menawarkan kepentingan repositioning teoritikal — sebagai contoh, dalam bidang seperti glaukoma (penyekatan β topikal), sokongan vasopresor dalam kejutan septik, atau modulasi penyembuhan luka — tetapi tiada ramalan berasaskan model tersedia dalam pakej ini untuk dinilai terhadapnya.

---

## Maklumat Pasaran Malaysia

Lima pendaftaran produk direkodkan sebagai dipasarkan pada masa ini di Malaysia. Malangnya, pengambilan data NPRA dalam kitaran ini tidak mengisi butiran lesen individu (nombor kebenaran, nama produk, bentuk dos, teks petunjuk yang diluluskan). Pertanyaan semula langsung ke pangkalan data Pendaftaran Produk NPRA menggunakan istilah carian **"ADRENALINE TARTRATE"** diperlukan untuk mendapatkan rekod lengkap untuk semua lima pendaftaran.

---

## Pertimbangan Keselamatan

Maklumat keselamatan dalam sisipan pakej — termasuk amaran utama dan kontraindikasi — tidak diambil dalam kitaran data ini. Ini mewakili jurang data **Menyekat** yang mesti diselesaikan sebelum sebarang ulasan klinikal atau kawal selia dapat diteruskan.

> Sila rujuk sisipan pakej yang diluluskan NPRA untuk maklumat keselamatan semasa, termasuk amaran tentang risiko kardiovaskular, hipertiroidisme, diabetes, dan interaksi dengan perencat MAO dan ubat antidepressan trisiklik.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Saluran ramalan TxGNN tidak boleh dilaksanakan disebabkan pemetaan ID DrugBank yang tidak diselesaikan, dan dua jurang data kritikal (amaran keselamatan dan MOA) kekal terbuka; tiada calon repositioning boleh dinilai tanpa ramalan model.

**Untuk meneruskan, perkara berikut diperlukan:**

- **Selesaikan ID DrugBank** — Petakan "ADRENALINE TARTRATE" ke entri DrugBanknya (kemungkinan DB00668, Epinefrin) untuk membolehkan ramalan KG + DL penuh
- **Jalankan semula saluran TxGNN** — Setelah ID DrugBank disahkan, janakan semula calon repositioning
- **Dapatkan sisipan pakej** *(DG001 — Menyekat)* — Muat turun dan hurai PDF sisipan pakej NPRA/TFDA untuk mengisi amaran utama dan kontraindikasi
- **Pertanyakan DrugBank API untuk MOA** *(DG002 — Tinggi)* — Dapatkan mekanisme tindakan, farmakodinamik, dan data sasaran untuk analisis relevan mekanisme
- **Pertanyakan semula pangkalan data lesen NPRA** — Dapatkan butiran pendaftaran penuh (nombor kebenaran, nama produk, bentuk dos, petunjuk yang diluluskan) untuk semua 5 produk berdaftar
- **Keluarkan semula Pakej Bukti** — Setelah semua jurang data diselesaikan, janakan semula Pakej Bukti v5 untuk menyokong penilaian repositioning lengkap

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

