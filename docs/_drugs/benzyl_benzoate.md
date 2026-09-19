---
layout: default
title: Benzyl Benzoate
parent: Low Evidence (L4-L5)
nav_order: 133
evidence_level: L5
indication_count: 0
---

# Benzyl Benzoate
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

# Benzyl Benzoate: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu Ayat

Benzyl Benzoate (DrugBank: DB00676) adalah ubat yang dipasarkan di Malaysia dengan 6 lesen yang didaftarkan. Walau bagaimanapun, model TxGNN **belum menghasilkan sebarang ramalan indikasi baru** untuk sebatian ini, dan jurang data yang kritikal kekal dalam mekanisme tindakan dan maklumat keselamatan, menghalang penilaian penggunaan semula lanjutan pada masa ini.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Nama Ubat (INN) | Benzyl Benzoate |
| DrugBank ID | DB00676 |
| Indikasi Asal | Tidak tersedia dalam set data semasa |
| Indikasi Baru Diramal | **Tiada** — tiada ramalan TxGNN dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A — tiada ramalan untuk dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 6 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Tiada Ramalan?

Benzyl Benzoate adalah agen antiparasitik topical dan scabisidal yang telah tertegak lama. Model TxGNN tidak menghasilkan sebarang calon penggunaan semula untuk ubat ini. Beberapa faktor mungkin menyumbang kepada hasil ini:

1. **Ciri ubat yang tidak lengkap**: Data mekanisme tindakan (MOA) tidak tersedia pada masa ini dalam pakej bukti. Tanpa maklumat MOA, keupayaan model untuk mengenalpasti indikasi baru yang munasabah dari segi mekanika mungkin terhad.

2. **Sifat ubat**: Benzyl Benzoate digunakan terutamanya sebagai agen topical (untuk kudis dan pediculosis). Ubat dengan mekanisme terutamanya tempatan/topical mungkin mempunyai interaksi sasaran sistemik yang lebih sedikit dalam graf pengetahuan, menghasilkan calon penggunaan semula yang lebih sedikit atau tiada.

3. **Ketersambungan graf pengetahuan yang jarang**: Jika nod ubat dalam graf pengetahuan TxGNN mempunyai tepi yang terhad (sambungan ubat–sasaran, ubat–penyakit, atau ubat–laluan yang diketahui yang sedikit), algoritma ramalan mungkin tidak mempunyai isyarat yang mencukupi untuk menghasilkan hipotesis penggunaan semula yang yakin.

---

## Bukti Ujian Klinikal

Pada masa ini tiada indikasi diramal untuk dinilai — tiada carian ujian klinikal dilakukan.

---

## Bukti Literatur

Pada masa ini tiada indikasi diramal untuk dinilai — tiada carian literatur dilakukan.

---

## Maklumat Pasaran Malaysia

6 lesen didaftarkan di Malaysia. Walau bagaimanapun, maklumat lesen yang terperinci (nombor kebenaran, nama produk, bentuk dos, dan indikasi yang diluluskan) tidak tersedia dalam set data semasa.

> **Nota**: Butiran lesen harus diambil dari pangkalan data NPRA untuk menyelesaikan bahagian ini.

---

## Pertimbangan Keselamatan

> Sila rujuk risalah produk untuk maklumat keselamatan. Maklumat amaran utama, kontraindikasi, dan data interaksi ubat tidak tersedia dalam pakej bukti semasa.

---

## Ringkasan Jurang Data

Jurang data yang kritikal berikut telah dikenal pasti dan mesti diselesaikan sebelum sebarang penilaian penggunaan semula boleh diteruskan:

| ID | Item | Keterukan | Kesan | Penyelesaian |
|----|------|----------|-------|-------------|
| DG001 | Amaran risalah produk / kontraindikasi | **Menyekat** | Tidak boleh memasuki pemeriksaan keselamatan Peringkat 1 | Muat turun dan analisis risalah produk PDF dari laman web pihak berkuasa kawal selia |
| DG002 | Mekanisme Tindakan (MOA) | **Penting** | Mempengaruhi analisis relevansi mekanika | Pertanyaan API DrugBank |

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Model TxGNN tidak menghasilkan sebarang ramalan penggunaan semula untuk Benzyl Benzoate. Digabungkan dengan ketiadaan data MOA dan maklumat keselamatan, tidak ada asas yang mencukupi untuk memajukan calon ini ke dalam penilaian selanjutnya.

**Untuk diteruskan, yang berikut diperlukan:**
- Selesaikan **DG001** (Menyekat): Dapatkan amaran risalah produk dan kontraindikasi dari pihak berkuasa kawal selia
- Selesaikan **DG002** (Penting): Ambil data mekanisme tindakan dari DrugBank
- Isi butiran lesen Malaysia (nombor kebenaran, nama produk, bentuk dos, indikasi yang diluluskan) dari pangkalan data NPRA
- Jalankan semula saluran ramalan TxGNN selepas memperkaya nod ubat graf pengetahuan dengan data MOA dan indikasi
- Jika ramalan kekal tiada selepas pengayaan data, pertimbangkan sama ada profil tindakan topical/tempatan ubat secara inheren mengehadkan potensi penggunaan semula sistemik

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

