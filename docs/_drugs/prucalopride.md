---
layout: default
title: Prucalopride
parent: Low Evidence (L4-L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Prucalopride
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **10** 
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

# Prucalopride: Daripada Konstipasi Kronik kepada Hypoalphalipoproteinemia

## Ringkasan Satu Ayat

Prucalopride ialah agonis reseptor 5-HT4 selektif yang digunakan secara klinis untuk konstipasi kronik melalui tindakan prokinetik usus (mengikut konteks mekanistik yang dicatat di tempat lain dalam pakej bukti ini). Ramalan peringkat teratas model TxGNN ialah **Hypoalphalipoproteinemia** (gangguan kolesterol HDL rendah), tetapi kandidat ini pada masa kini disokong oleh **0 percubaan klinis** dan **0 publikasi**, dan anotasi model itu sendiri secara eksplisit mencatat tiada pautan biologi yang diketahui antara agonis 5-HT4 dan metabolisme lipoprotein.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Tidak ditentukan dalam teks lesen Taiwan; konstipasi kronik dicatat sebagai penggunaan klinis prucalopride yang telah ditetapkan di tempat lain dalam pakej bukti ini |
| Petunjuk Baru yang Diramalkan | Hypoalphalipoproteinemia |
| Skor Ramalan TxGNN | 99.82% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa kini, data mekanisme tindakan terperinci untuk prucalopride tidak tersedia (pencarian MOA DrugBank ialah celah data terbuka dalam pakej ini). Berdasarkan konteks farmakologi yang dirujuk di tempat lain dalam pakej bukti ini, prucalopride bertindak sebagai agonis reseptor 5-HT4 selektif dan digunakan secara klinis untuk menggalakkan motilitas usus.

Hypoalphalipoproteinemia ialah gangguan metabolisme lipoprotein yang dicirikan oleh kolesterol HDL rendah, yang ditadbir oleh laluan (contohnya, reseptor LDL, pengangkutan lipid, pengangkutan kolesterol terbalik) yang tidak mempunyai sambungan yang ditubuhkan kepada isyarat motilitas usus serotonergik. Rasional repurposing model itu sendiri untuk kandidat ini menyatakan secara eksplisit: *"5-HT4 受體致效劑與脂蛋白代謝、HDL 調控無已知機轉關聯，屬於缺乏生物學合理性之預測，無任何臨床或文獻證據支持"* (tiada pautan mekanistik yang diketahui, dan tiada bukti klinis atau literatur yang menyokong). Ini konsisten dengan skor yang mencerminkan persatuan embedding graf daripada hipotesis yang berasaskan biologi, dan dengan klasifikasi L5 / Tahan yang diperuntukkan oleh enjin pemarkahan itu sendiri.

Dua calon lain dalam set ramalan yang sama ini — amyloidosis (peringkat 6) dan amyloidosis utama (peringkat 9) — membawa cerita mekanistik yang lebih koheren (disfungsi autonomi/GI berkaitan amyloid sebagai sasaran untuk penghilangan gejala prokinetik) dan disokong oleh literatur sebenar (L4, tahap keputusan S1, "Research Question"). Ini mungkin calon yang lebih produktif untuk susulan berbanding ramalan hypoalphalipoproteinemia yang peringkat teratas tetapi tidak disokong secara mekanistik.

---

## Bukti Percubaan Klinis

Pada masa kini tiada percubaan klinis berkaitan yang terdaftar.

---

## Bukti Literatur

Pada masa kini tiada literatur berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|---------|------|------|-----------|
| Tidak ditentukan | Tidak ditentukan | Tidak ditentukan | Tidak ditentukan |
| Tidak ditentukan | Tidak ditentukan | Tidak ditentukan | Tidak ditentukan |

Dua lesen aktif disahkan dalam daftar (total_licenses = 2, market_status = Marketed), tetapi nombor lesen, nama produk, bentuk dos, dan teks petunjuk yang diluluskan tidak diisi dalam tarikan data ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

*(Nota: peringatan sisipan pakej TFDA/kontraindikasi ialah celah data Blocking-severity yang terdokumen — lihat Kesimpulan di bawah.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Petunjuk yang diramalkan peringkat teratas (hypoalphalipoproteinemia) tidak mempunyai percubaan klinis atau literatur yang menyokong (L5, evidence-model-only) dan secara eksplisit ditandai oleh rasional model itu sendiri sebagai kekurangan kredibiliti biologi. Secara berasingan, peringatan label TFDA/kontraindikasi ialah celah data Blocking-severity, yang bermaksud kandidat ini tidak boleh memasuki skrining keselamatan S1 tanpa mengira bukti keberkesanan.

**Untuk meneruskan, perkara berikut diperlukan:**
- Sisipan pakej TFDA (peringatan, kontraindikasi) — Blocking gap, diperlukan sebelum mana-mana skrining keselamatan
- Data mekanisme tindakan DrugBank — diperlukan untuk penilaian kredibiliti mekanistik
- Teks lesen yang disahkan (nama produk, bentuk dos, petunjuk yang diluluskan) untuk 2 pendaftaran Taiwan
- Pertimbangkan pengalihan usaha penilaian kepada calon amyloidosis / amyloidosis utama (peringkat 6 dan 9) dalam set ramalan yang sama ini, yang mempunyai sokongan literatur sebenar dan rasional mekanistik yang lebih koheren

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

