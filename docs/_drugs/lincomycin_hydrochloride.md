---
layout: default
title: Lincomycin Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 444
evidence_level: L5
indication_count: 0
---

# Lincomycin Hydrochloride
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

# Lincomycin Hydrochloride: Laporan Penilaian Penggunaan Ubat Ulang — Data Ramalan Tidak Mencukupi

---

## Ringkasan Satu Ayat

Lincomycin Hydrochloride adalah antibiotik linkosamida yang secara historis digunakan untuk merawat jangkitan serius yang disebabkan oleh organisma Gram-positif yang peka termasuk streptokoki, stafilokoki, dan pneumokoki.
Model TxGNN **tidak mengembalikan sebarang indikasi penggunaan ubat ulang yang diramalkan** untuk sebatian ini dalam pakej bukti semasa — tidak dapat menyelesaikan sebarang penilaian penggunaan ubat ulang pada peringkat ini.
Laporan ini mendokumenkan jurang data semasa dan menggariskan langkah-langkah yang diperlukan sebelum penilaian yang bermakna dapat dilakukan.

---

## Gambaran Keseluruhan Ringkas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Jangkitan bakteria Gram-positif yang serius (pengetahuan kelas antibiotik) |
| Indikasi Baru yang Diramalkan | — Tidak tersedia |
| Skor Ramalan TxGNN | — Tidak tersedia |
| Tahap Bukti | — Tidak boleh dinilai |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 20 |
| Keputusan yang Disyorkan | **Tunggu** |

---

## Mengapa Penilaian Tidak Boleh Diteruskan

Persyaratan utama untuk penilaian penggunaan ubat ulang — ramalan TxGNN — tiada dalam pakej bukti ini (`predicted_indications: []`). Dua punca yang mungkin wujud:

1. **Saluran paip ramalan mungkin belum dijalankan** untuk sebatian ini. Lincomycin Hydrochloride mungkin belum dipadankan kepada nod DrugBank (ID DrugBank kini kosong), yang akan menghalang model graf pengetahuan daripada memberikan skor kepada asosiasi penyakit calon.

2. **Model mengembalikan tiada calon di atas ambang keyakinan**, yang itu sendiri mungkin mencerminkan sambungan graf yang tidak mencukupi disebabkan oleh pemetaan DrugBank yang hilang.

Selain itu, teks indikasi yang diluluskan di semua 20 pendaftaran Malaysia tidak ditangkap dalam langkah pengekstrakan data, bermakna kedua-dua peranan terapeutik asas ubat mahupun profil keselamatannya yang diketahui tidak dapat disahkan daripada data berstruktur sahaja.

Tanpa indikasi sasaran, bahagian-bahagian berikut — *Bukti Percubaan Klinikal*, *Bukti Kesusasteraan*, dan *Mengapa Ramalan Ini Wajar?* — tidak boleh diisi secara bermakna dan ditinggalkan mengikut peraturan pelaporan.

---

## Maklumat Pasaran Malaysia

Lincomycin Hydrochloride memegang **20 pendaftaran produk** dengan pihak berkuasa ubat Malaysia (NPRA) dan disahkan sebagai dipasarkan semasa. Walau bagaimanapun, butiran lesen berstruktur (nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak diperoleh semula dalam kitaran pengekstrakan data ini — semua medan rekod lesen dikembalikan kosong. Jadual pendaftaran individu tidak boleh dikemukakan tanpa data ini.

> **Tindakan diperlukan**: Soal semula pangkalan data produk NPRA untuk mendapatkan semula nombor lesen, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk semua 20 pendaftaran.

---

## Pertimbangan Keselamatan

> Sila rujuk leaflet ubat untuk maklumat keselamatan.
>
> Tiada data amaran utama, keterangan bertentangan, atau data interaksi ubat ditangkap dalam pakej bukti ini. PDF leaflet ubat NPRA/TFDA harus dimuat turun dan diurai sebelum sebarang semakan klinikal atau kawal selia dilakukan.

---

## Kesimpulan dan Langkah-Langkah Seterusnya

**Keputusan: Tunggu**

**Alasan:**
Pakej bukti untuk Lincomycin Hydrochloride tidak lengkap secara struktur — tiada ramalan penggunaan ubat ulang TxGNN hadir, sambungan DrugBank hilang, dan semua medan butiran kawal selia berstruktur kosong. Tiada indikasi untuk dinilai dan tiada garis dasar keselamatan untuk dinilai melawannya pada masa ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **[Blocking]** Selesaikan pemetaan ID DrugBank untuk Lincomycin Hydrochloride (cari `DB01190` — entri DrugBank yang diketahui untuk linkomasin) untuk membolehkan pemeringkatan graf pengetahuan dan membuka keluaran ramalan TxGNN.
- **[Blocking]** Jalankan semula pertanyaan pangkalan data produk NPRA untuk mengisi nombor lesen, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk semua 20 pendaftaran.
- **[Blocking]** Muat turun dan urai PDF leaflet ubat NPRA/TFDA untuk mengeluarkan amaran utama dan keterangan bertentangan — diperlukan sebelum sebarang langkah pemeriksaan keselamatan (kini ditandakan sebagai jurang data Blocking).
- **[High]** Isi medan mekanisme tindakan (MOA) dengan membuat pertanyaan kepada API DrugBank setelah ID DrugBank disahkan — Lincomycin menghalang sintesis protein bakteria dengan mengikat kepada subunit ribosomal 50S, tetapi ini mesti bersumber daripada data berstruktur dan bukannya pengetahuan latar belakang.
- **[Pipeline]** Setelah jurang di atas diselesaikan, jalankan semula saluran paip ramalan TxGNN penuh (langkah KG + DL + pemetaan) dan hasilkan semula pakej bukti untuk mendapatkan `predicted_indications` sebelum memulakan penilaian penggunaan ubat ulang penuh.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

