---
layout: default
title: Griseofulvin
parent: Low Evidence (L4-L5)
nav_order: 375
evidence_level: L5
indication_count: 5
---

# Griseofulvin
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
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

# Griseofulvin: Dari Dermatomikosis ke Myiasis

## Ringkasan Satu Ayat

Griseofulvin adalah agen antijamur yang sudah lama digunakan untuk merawat infeksi dermatomikosis (infeksi jamur pada kulit, rambut, dan kuku). Model TxGNN meramalkan ia mungkin berkesan untuk **Myiasis** (infestasi larva lalat pada tisu), namun arah ini kini disokong oleh **0 uji klinik** dan hanya **1 artikel literatur veterinar yang longgar berkait**.

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Dermatomikosis (infeksi jamur kulit/rambut/kuku) — teks indikasi yang diluluskan TFDA tidak tersedia dalam pakej bukti semasa |
| Indikasi Baru Dijangka | Myiasis |
| Skor Ramalan TxGNN | 99.41% |
| Tahap Bukti | L5 |
| Status Pasaran Taiwan | ✓ Dipasarkan |
| Bilangan Pendaftaran | 6 |
| Keputusan Disarankan | Tahan |

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan terperinci daripada DrugBank tidak tersedia lagi untuk calon ini. Berdasarkan farmakoloji yang diketahui, griseofulvin mengikat mikrotubul jamur dan mengganggu gelendong mitotik semasa pembahagian sel jamur — mekanisme antijamur tanpa aktiviti antiparasit atau insektisid yang didokumenkan.

Myiasis disebabkan oleh larva lalat yang menginfiltrasi tisu hidup; pengurusan standard adalah penyingkiran larva mekanik/bedah, dengan agen antiparasit seperti ivermektin digunakan secara tambahan. Tiada laluan biologi yang diketahui menghubungkan tindakan antijamur griseofulvin kepada pembunuhan atau pengusiran larva lalat.

Skor TxGNN 99.41% oleh itu kemungkinan besar didorong oleh persatuan graf pengetahuan tidak langsung — griseofulvin dan myiasis mungkin berlaku bersama di bawah nod kluster "penyakit kulit/parasit kulit" yang dikongsi — dan bukan hubungan farmakoloji yang tulin. Corak yang sama berlaku untuk calon berperingkat teratas yang lain dalam pakej bukti ini (myiasis merayap, myiasis furunkuler, myiasis luka, dan echinococcosis), tiada satupun mempunyai pautan mekanistik yang munasabah kepada griseofulvin.

## Bukti Uji Klinik

Tiada uji klinik berkaitan yang didaftarkan pada masa kini.

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Ulasan | The Veterinary record | Ulasan veterinar tentang penyakit kulit parasit dalam anjing dan kucing; tiada abstrak tersedia, dan tidak secara khusus menangani penggunaan griseofulvin dalam myiasis |

## Maklumat Pasaran Taiwan

6 lesen yang dipasarkan ada dalam rekod (status pasaran: Dipasarkan), namun butiran peringkat lesen (nombor kebenaran, nama produk, bentuk dos, teks indikasi yang diluluskan) tidak diisi dalam pakej bukti semasa dan tidak dapat disenaraikan di sini.

## Pertimbangan Keselamatan

Sila rujuk surat pelepasan produk untuk maklumat keselamatan. (Nota: Pengambilan amaran/percanggahan label TFDA ditandakan sebagai jurang data yang menghalang — lihat Langkah Seterusnya.)

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Ramalan bergantung semata-mata kepada skor model TxGNN tanpa uji klinik dan tanpa literatur yang relevan dari segi mekanisme atau klinik — tahap bukti L5. Mekanisme yang dicadangkan (perencatan mikrotubul antijamur) tiada kaitan yang diketahui dengan infestasi larva lalat, jadi persatuan kemungkinan besar adalah artifak graf pengetahuan dan bukan isyarat pemuatan semula yang tulin.

**Untuk meneruskan, yang berikut diperlukan:**
- Amaran/percanggahan label TFDA (jurang penghalang — diperlukan sebelum sebarang ulasan keselamatan S1)
- Mekanisme tindakan yang disahkan melalui API DrugBank
- Sebarang bukti in vitro/in vivo aktiviti antiparasit atau larvacid untuk griseofulvin
- Bukti klinik manusia atau laporan kes khusus untuk myiasis, kerana satu-satunya pukulan literatur adalah ulasan veterinar yang tidak berkaitan dengan ubat ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

