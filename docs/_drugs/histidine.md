---
layout: default
title: Histidine
parent: Low Evidence (L4-L5)
nav_order: 382
evidence_level: L5
indication_count: 2
---

# Histidine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **2** 
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

# Histidine: Daripada Suplemen Asid Amino kepada Gastroparesis Terprediksi

## Ringkasan Satu Ayat

Histidine ialah asid amino penting yang dipasarkan di Malaysia melalui 32 produk berdaftar, namun teks indikasi yang diluluskan khusus tidak ditangkap dalam set data ini. Model TxGNN meramalkan kemungkinan kaitan dengan **Gastroparesis**, tetapi ramalan ini pada masa kini mempunyai **tiada percubaan klinikal sokongan dan tiada petikan literatur** — ia adalah isyarat algoritma tulen tanpa pengesahan bebas.

---

## Gambaran Keseluruhan Ringkas

| Item | Kandungan |
|------|------|
| Indikasi Asal | Tidak tersedia dalam data daftar (teks indikasi yang diluluskan tidak diekstrak untuk mana-mana 32 lesen Malaysia) |
| Indikasi Baru Terprediksi | Gastroparesis (penyakit) |
| Skor Ramalan TxGNN | 99.55% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 32 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa kini, data mekanisme tindakan terperinci tidak tersedia untuk histidine dalam pak bukti ini. Berdasarkan biokimia yang diketahui, histidine ialah prekursor biosintesis histamin (melalui L-histidine decarboxylase), dan histamin bertindak pada reseptor H2 untuk mengawal motiliti otot licin gastrointestinal — memberikan kaitan teori tak langsung kepada pengosongan gastrik / gastroparesis.

Bagaimanapun, pautan ini adalah spekulatif dan bukannya terbukti: skor TxGNN (0.9955) ialah ramalan tulen berasaskan graf dengan **tiada percubaan klinikal sokongan, percubaan ICTRP, atau literatur PubMed** untuk pasangan histidine–gastroparesis. Tambahan pula, arah kesan netto histamin pada pengosongan gastrik tidak diselesaikan dalam literatur — beberapa laporan menerangkan kesan prokinetik, yang lain kesan perencat — jadi walaupun mekanisme yang dicadangkan tidak boleh ditandatangani dengan yakin sebagai bermanfaat.

Penting untuk diambil perhatian, indikasi TxGNN terprediksi kedua untuk ubat ini (sklerozing kolangitis, bukan fokus utama laporan ini) disokong oleh literatur praklinikal sebenar — tetapi literatur itu sebenarnya menunjukkan dalam arah **bertentangan**: ia menunjukkan bahawa *menghalang* isyarat histamin (bukan menambah prekursornya) mengurangkan kecederaan biliar dan fibrosis. Ini menimbulkan amaran yang lebih luas tentang bergantung pada penalaran laluan histidine→histamin sahaja sebagai asas untuk keputusan penggunaan semula.

---

## Bukti Percubaan Klinikal

Pada masa kini tiada percubaan klinikal yang berkaitan berdaftar untuk pasangan histidine–gastroparesis (0 hit daripada ClinicalTrials.gov dan ICTRP).

---

## Bukti Literatur

Pada masa kini tiada literatur yang berkaitan tersedia untuk pasangan histidine–gastroparesis (0 hit daripada PubMed).

---

## Nota Tambahan: Indikasi Terprediksi Kedua (Sklerozing Kolangitis)

Pak bukti ini (ID calon berakhir dengan "-multi") juga membawa ramalan TxGNN kedua berperingkat lebih rendah yang perlu diperhatikan bersama dengan yang utama, kerana ia mempunyai literatur sokongan sebenar dan kaveat penting:

| Item | Kandungan |
|------|------|
| Penyakit | Sklerozing kolangitis |
| Skor TxGNN | 99.27% (pangkat 9734) |
| Tahap Bukti | L4 (8 petikan PubMed, semua kajian praklinikal/mekanik atau kajian biomarker; tiada percubaan klinikal) |

Pelbagai kajian binatang (PMIDs 27351144, 32054995, 35799467, 29601088) menunjukkan bahawa histamin yang dihasilkan oleh sel mast *mendorong* proliferasi biliar dan fibrosis dalam model kolangiitis sklerosis primer (PSC), dan bahawa **memblok** reseptor H1/H2 atau **knockout gen** histidine decarboxylase (enzim histidine→histamin) *mengurangkan* kerosakan biliar. Ini ialah isyarat arah yang bertentangan: bukti mekanik menyokong *menghalang* laluan histamin sebagai bermanfaat dalam PSC, bukan menambah prekursornya (histidine). Ini harus diperlakukan sebagai isyarat keselamatan yang mungkin dan bukannya peluang penggunaan semula, dan memerlukan tinjauan eksplisit sebelum sebarang penilaian lanjutan histidine dalam penyakit hepatobiliar.

---

## Maklumat Pasaran Malaysia

Histidine memegang 32 pendaftaran aktif di Malaysia di bawah status "Dipasarkan" (dipasarkan). Detail peringkat lesen (nombor kebenaran, nama produk, bentuk dos, teks indikasi yang diluluskan) tidak diisi dalam set data yang diekstrak untuk ubat ini, jadi jadual per-produk tidak boleh dipersembahkan tanpa mengada nilai.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. (Tiada data amaran utama, kontraindikasi, atau interaksi ubat-ubat tersedia dalam pak bukti ini — bendera DG001 menandakan amaran/kontraindikasi label TFDA/NPRA sebagai jurang data Penyekat.)

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Indikasi terprediksi utama (gastroparesis) ialah tahap bukti L5 — skor model tanpa percubaan atau literatur sokongan sama sekali. Indikasi terprediksi sekunder (sklerozing kolangitis) mempunyai bukti mekanik L4, tetapi bukti itu menunjukkan terhadap, bukan ke arah, kebolehplausibilan biologi menambah histidine. Kedua-dua indikasi pada masa kini tidak memenuhi bar untuk maju melampaui S0.

**Untuk meneruskan, yang berikut diperlukan:**
- Sisipan pakej TFDA/NPRA (amaran, kontraindikasi) — pada masa kini jurang data Penyekat (DG001)
- Mekanisme tindakan yang disahkan untuk histidine — pada masa kini jurang Berisiko Tinggi (DG002)
- Sebarang bukti dunia nyata atau praklinikal khusus untuk histidine (bukan hanya histamin hiliran) dalam gangguan motiliti gastrik
- Penyelesaian percanggahan arah yang dilihat dalam literatur sklerozing kolangitis sebelum mempertimbangkan indikasi itu lebih lanjut

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

