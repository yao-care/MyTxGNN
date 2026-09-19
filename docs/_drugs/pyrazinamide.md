---
layout: default
title: Pyrazinamide
parent: Low Evidence (L4-L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: Daripada Tuberkulosis Paru-paru kepada Otitis Media Berjangkit

## Ringkasan Satu Ayat

Pyrazinamide ialah ejen anti-tuberkulosis garis pertama, digunakan sebagai sebahagian daripada terapi kombinasi piawai (bersama-sama isoniazid, rifampicin, ± ethambutol) untuk tuberkulosis paru-paru. Model TxGNN meramalkan ia mungkin berkesan untuk **Otitis Media Berjangkit**, namun calon khusus ini pada masa kini mempunyai **0 ujian klinikal** dan **0 penerbitan** yang menyokongnya secara langsung — skor tinggi model nampaknya mencerminkan kesamaan penyisipan kepada entiti berkaitan yang lebih terdokumen (otitis media tuberkulosis) daripada bukti langsung.

---

## Gambaran Pantas

| Item | Kandungan |
|------|---------|
| Indikasi Asal | Tuberkulosis paru-paru (komponen rejimen kombinasi anti-TB garis pertama; teks indikasi peringkat lesen NPRA tidak tersedia dalam data sumber) |
| Indikasi Baru yang Dijangka | Otitis Media Berjangkit |
| Skor Ramalan TxGNN | 99.96% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 5 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Masuk Akal?

Pada masa kini, data mekanisme tindakan terperinci tidak tersedia (ditandakan sebagai jurang data dalam pakej sumber). Berdasarkan farmakologi yang diketahui, pyrazinamide ialah ubat prodrug yang diubah oleh pyrazinamidase mikoakteri kepada asid pyrazinoik, yang mengganggu potensi membran dan metabolisme tenaga *Mycobacterium tuberculosis* dalam persekitaran asid dan nekrotik lesi TB. Ia adalah komponen utama rejimen kombinasi empat ubat garis pertama piawai untuk tuberkulosis paru-paru, dan keberkesanannya dalam indikasi itu sudah terbukti.

Untuk calon puncak itu sendiri — otitis media berjangkit — tiada bukti ujian klinikal atau kesusasteraan yang dikembalikan dalam pakej bukti ini. Menurut rasionalisasi model itu sendiri, skor TxGNN yang tinggi (pangkat 1030 secara dalaman) berkemungkinan besar mencerminkan kesamaan penyisipan graf pengetahuan kepada nod penyakit jiran yang lebih spesifik — "otitis media tuberkulosis" — daripada suatu isyarat baru yang tulen dan disokong bukti.

Terutamanya, beberapa calon yang berkaitan rapat dalam set ramalan yang sama (penyakit telinga tengah, otitis media kronik, otitis media bernanah — pangkat 2, 4, 5) **adalah** masing-masing disokong oleh 5–8 laporan kes/tinjauan. Semua kesusasteraan itu menerangkan **otitis media tuberkulosis** — manifestasi ekstrapulmoner TB yang jarang mempengaruhi telinga tengah — berjaya dirawat dengan rejimen anti-TB piawai yang merangkumi pyrazinamide. Ini mencadangkan bahawa indikasi yang boleh dipertahankan secara farmakologi adalah lebih sempit daripada "otitis media berjangkit" secara umum: ia adalah otitis media **sekunder kepada jangkitan tuberkulosis yang disahkan**, bukan otitis media dengan etiologi lain (seperti bakteri tipikal), kerana spektrum antimikrobial pyrazinamide pada asasnya terhad kepada mikoakteri.

---

## Bukti Ujian Klinikal

Pada masa kini tiada ujian klinikal yang berkaitan didaftarkan.

---

## Bukti Kesusasteraan

Pada masa kini tiada kesusasteraan yang berkaitan tersedia.

---

## Maklumat Pasaran Malaysia

5 kebenaran produk didaftarkan dengan NPRA (status pasaran: Dipasarkan), namun butiran peringkat lesen (nombor lesen, nama produk, bentuk dos, teks indikasi yang diluluskan) tidak dikembalikan dalam pakej data sumber dan tidak dapat dilengkapkan di sini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Walaupun skor keyakinan TxGNN yang tinggi, "otitis media berjangkit" mempunyai sokongan ujian klinikal atau kesusasteraan langsung yang sifar, memenuhi hanya tahap bukti ramalan model sahaja (L5). Bukti sokongan sebenarnya dalam set data ini tertumpu pada otitis media tuberkulosis khususnya, yang boleh dikatakan sebagai lanjutan indikasi TB pyrazinamide yang sudah ada daripada satu yang benar-benar baru.

**Untuk meneruskan, perkara berikut diperlukan:**
- Sisipan pakej TFDA/NPRA (amaran, kontraindikasi) — pada masa kini merupakan jurang data yang menghalang penyaringan keselamatan awal
- Data mekanisme tindakan DrugBank melalui API — diperlukan untuk menilai secara formal kerasionalan mekanik
- Pertimbangkan untuk mengubah semula skop calon daripada "otitis media berjangkit" kepada "otitis media tuberkulosis" dan kumpulkan bukti klinikal yang dikaitkan dengan diagnosis untuk indikasi yang lebih sempit itu
- Data produk lesen Malaysia (nombor lesen, nama produk, bentuk dos, teks indikasi yang diluluskan) untuk melengkapkan bahagian maklumat pasaran

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

