---
layout: default
title: Thyrotropin Alfa
parent: Low Evidence (L4-L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Thyrotropin Alfa
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

# Thyrotropin Alfa: Dari Penjejakan Kanser Tiroid ke Gangguan Migrain

## Ringkasan Satu Ayat

Thyrotropin alfa (TSH manusia rekombinan) digunakan secara antarabangsa sebagai agen diagnostik dan adjuvan dalam penjejakan kanser tiroid yang terbeza dengan baik selepas thyroidektomi. Ramalan teratas model TxGNN untuk ubat ini ialah **Gangguan Migrain**, tetapi arah ini pada masa kini mempunyai **sifar ujian klinikal** dan **sifar penerbitan** menyokongnya — ramalan ini bergantung pada skor model semata-mata.

## Tinjauan Cepat

| Item | Kandungan |
|------|------|
| Petunjuk Asal | Penjejakan kanser tiroid (adjuvan kepada thyroidektomi) — berdasarkan rujukan farmakologi umum; teks petunjuk yang diluluskan khusus NPRA Malaysia tidak tersedia dalam set data semasa (Halangan Jurang Data, lihat DG001) |
| Petunjuk Baru yang Diramalkan | Gangguan Migrain |
| Skor Ramalan TxGNN | 99.98% |
| Aras Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | Tahan |

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan berstruktur untuk thyrotropin alfa ditandai sebagai Jurang Data (DG002) dalam pakej bukti ini. Berdasarkan pengetahuan farmakologi yang ditubuhkan — dan disahkan oleh analisis pakej bukti yang sama terhadap calon pangkat-10 (hipertiroidisme) — thyrotropin alfa ialah TSH manusia rekombinan yang bertindak sebagai **agonis penerima TSH**, merangsang proliferasi sel folikel tiroid dan sekresi hormon tiroid. Secara antarabangsa, ia digunakan untuk membantu pengesanan penyakit tiroid sisa/berulang dan untuk menyokong ablasi radioiodine pada pesakit dengan kanser tiroid yang terbeza dengan baik.

Bagi ramalan kedudukan teratas, **gangguan migrain**, tidak ada laluan mekanistik yang diketahui menghubungkan isyarat penerima TSH kepada patofisiologi migrain. Alasan pakej bukti sendiri menyatakannya dengan jelas: "無任何臨床試驗或文獻支持；TSH 受體訊號與偏頭痛病理生理無已知直接連結，純為模型預測分數" — iaitu, tiada sokongan ujian klinikal atau literatur yang wujud, dan sambungannya adalah semata-mata artifak skor model. Corak ini berulang di seluruh pangkat 2–9 (penyakit Raynaud, atrophoderma vermiculata, hipertensi paru, POTS, dll.), yang pakej bukti sendiri mencirikan sebagai kemungkinan ralat keberhampiran penanaman graf pengetahuan dan bukannya hubungan biologi tulen.

Perlu diingat, satu-satunya calon dalam set ini dengan ujian klinikal sokongan sebenar — **hipertiroidisme** (pangkat 10, L2/S1) — membawa percanggahan mekanistik yang terdokumen: thyrotropin alfa ialah agen penggerak tiroid, jadi ia dijangka akan mencetuskan atau memburukkan hipertiroidisme dan bukannya merawatnya. Dua ujian sokongan sebenarnya mengkaji rhTSH sebagai rawatan pra untuk terapi radioiodine dalam gondok jinak, bukan sebagai rawatan untuk hipertiroidisme primer. Ini menekankan bahawa set isyarat penggunaan semula keseluruhan untuk ubat ini harus ditangani dengan berhati-hati.

## Bukti Ujian Klinikal

Pada masa kini tiada ujian klinikal berkaitan yang didaftarkan.

## Bukti Literatur

Pada masa kini tiada literatur berkaitan yang tersedia.

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan 1 pendaftaran aktif untuk thyrotropin alfa, dengan status pasaran "Dipasarkan" (Dipasarkan). Walau bagaimanapun, nombor lesen, nama produk, bentuk dos, dan teks petunjuk yang diluluskan tidak diisi dalam set data semasa — pengambilan/penghuraian label produk NPRA diperlukan (lihat DG001, keterukan Halangan) sebelum maklumat ini dapat dilaporkan.

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan. Nota: amaran aras label, kontraindikasi, dan data interaksi ubat tidak dapat diambil untuk ubat ini (DG001, Halangan) — jurang ini sahaja mencukupi untuk menghalang kemajuan melampaui peringkat saringan keselamatan awal (S1).

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Petunjuk yang diramalkan kedudukan teratas (gangguan migrain) tidak mempunyai bukti ujian klinikal atau literatur dan tiada asas mekanistik yang munasabah — ia adalah isyarat skor model tulen (L5, peringkat keputusan S0). Menambah ini, jurang data Halangan dalam maklumat keselamatan label TFDA/NPRA (DG001) menghalang bahkan tinjauan keselamatan awal untuk ubat ini.

**Untuk meneruskan, yang berikut diperlukan:**
- Ambil dan huraikan label produk/sisipan NPRA untuk mengisi DG001 (amaran, kontraindikasi, DDI) dan sahkan teks petunjuk yang diluluskan sebenar
- Dapatkan data mekanisme tindakan dan pengkategorian DrugBank untuk menutup DG002
- Jika mengejar penilaian lebih lanjut tentang potensi penggunaan semula ubat ini, prioritaskan isyarat hipertiroidisme/gondok (pangkat 10) bukannya migrain — tetapi terlebih dahulu selesaikan percanggahan mekanistik (agonis TSH lwn. merawat hipertiroidisme) dengan tinjauan berpengetahuan endokrinologi sebelum sebarang kemajuan S2+
- Memandangkan hampir ketiadaan bukti sokongan di seluruh 9 daripada 10 petunjuk yang diramalkan, pertimbangkan untuk menurunkan prioritas calon ini yang memihak keluaran TxGNN dengan bukti asas yang lebih kuat

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

