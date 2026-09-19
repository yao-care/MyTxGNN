---
layout: default
title: Tranexamic Acid
parent: Low Evidence (L4-L5)
nav_order: 661
evidence_level: L4
indication_count: 1
---

# Tranexamic Acid
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **1** 
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

# Asid Traneksamik: Dari Perdarahan Menstruasi Berat kepada Amenorrhea — Isyarat yang Bercanggah

## Ringkasan Satu Ayat

Asid traneksamik adalah ejen antifibrinolitik yang peranannya yang telah terbukti secara klinikal ialah *mengurangkan* perdarahan menstruasi yang berlebihan (menorrhagia/perdarahan uterus abnormal), bukan mendorong atau merawat ketiadaan menstruasi. Model TxGNN meramalkan kaitan dengan **Amenorrhea**, tetapi pakej bukti ini tidak mengandungi **sebarang percubaan klinikal yang menyokong** dan hanya **2 penerbitan jenis ulasan**, tidak satu pun yang mengkaji indikasi ini secara langsung. Arah ramalan yang diramalkan nampaknya bertentangan secara farmakologis dengan kesan ubat yang diketahui, dan telah ditandai dalam pakej ini sebagai artifak graf pengetahuan yang mungkin dan bukannya isyarat repurposing yang tulen.

## Tinjauan Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak dinyatakan dalam teks lesen TFDA yang tersedia; mengikut nota rasional pakej bukti itu sendiri, asid traneksamik adalah ejen antifibrinolitik yang digunakan untuk mengawal/mengurangkan perdarahan menstruasi berat dan keadaan hemoraji lain |
| Indikasi Baru Yang Diramalkan | Amenorrhea (penyakit) |
| Skor Ramalan TxGNN | 99.19% |
| Tahap Bukti | L4 |
| Status Pasaran Malaysia | ✓ Dimasarkan |
| Bilangan Pendaftaran | 10 |
| Keputusan yang Disyorkan | Tahan |

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan yang terperinci tidak tersedia dalam pakej bukti ini (ditandai sebagai jurang data berkesedar tinggi). Berdasarkan maklumat yang tersedia, asid traneksamik adalah penghambat plasminogen/plasmin (antifibrinolitik) yang kesannya klinikal yang terbukti ialah **mengurangkan** perdarahan uterus yang berlebihan — arah fisiologi yang bertentangan dengan amenorrhea (ketiadaan menstruasi).

Pakej bukti itu sendiri menimbulkan kebimbangan ini secara langsung: skor TxGNN yang tinggi (0.99) kemungkinan besar mencerminkan kedekatannya dalam graf antara nod "amenorrhea" dan nod "perdarahan menstruasi / perdarahan uterus abnormal (AUB)", dan bukannya hubungan kausal atau terapeutik. Dalam erti kata lain, model mungkin memilih maklumat bahawa asid traneksamik sangat dikaitkan dengan konsep penyakit berkaitan menstruasi secara umum, tanpa membezakan dengan betul "merawat perdarahan" daripada "menyebabkan ketiadaan perdarahan."

Kerana data MOA asal hilang, konflik mekanik ini tidak boleh disemak silang secara bebas atau diselesaikan daripada pakej ini sahaja. Ia harus dianggap sebagai percanggahan yang belum diselesaikan, bukan sebagai bukti yang menyokong.

## Bukti Percubaan Klinikal

Tiada percubaan klinikal berkaitan yang didaftarkan pada masa ini.

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|------|------|--------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Ulasan | Menopause (New York, N.Y.) | Ulasan berasaskan bukti tentang terapi farmakologi untuk **perdarahan uterus abnormal** (iaitu, merawat perdarahan berlebihan, bukan amenorrhea); tidak menangani asid traneksamik untuk amenorrhea secara khusus |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Ulasan | Journal of Oncology Pharmacy Practice | Pendekatan sistemik kepada **profilaksis menstruasi dan penindasan** pada pesakit kanser hematologi pra-menopaus yang menjalani sitopenias yang berkaitan dengan rawatan; membincangkan strategi penindasan menstruasi secara luas, bukan amenorrhea sebagai indikasi yang dirawat untuk ubat ini |

Tidak satu pun penerbitan memberikan bukti langsung untuk asid traneksamik sebagai rawatan untuk amenorrhea; kedua-duanya berkaitan dengan pengurusan perdarahan menstruasi, memperkuat konflik mekanik yang dinyatakan di atas.

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. Nota: data amaran/kontraindikasi TFDA untuk ubat ini adalah jurang data berkesedar **Menyekat** (DG001) yang tertunggak — penilaian keselamatan (Peringkat S1) tidak boleh diteruskan sehingga ini diselesaikan.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Indikasi yang diramalkan (amenorrhea) bertentangan dengan kesan farmakologis asid traneksamik yang diketahui mengurangkan perdarahan menstruasi, dan tiada bukti percubaan klinikal wujud untuk menyokongnya — kedua-dua penerbitan yang tersedia berkaitan dengan pengurusan perdarahan, bukan merawat ketiadaannya. Digabungkan dengan data MOA dan keselamatan yang hilang, calon ini tidak memenuhi standard untuk maju melampaui skrining awal (peringkat keputusan S0).

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran sisipan pakej TFDA/kontraindikasi (DG001, Menyekat — diperlukan sebelum mana-mana skrining keselamatan S1)
- Data mekanisme tindakan ubat daripada DrugBank (DG002, Tinggi)
- Rasional mekanik atau klinikal bebas yang menjelaskan bagaimana ejen antifibrinolitik mungkin boleh merawat amenorrhea, untuk mengetepikan artifak kedekatannya graf pengetahuan
- Rekod lesen/produk TFDA yang terperinci (nombor lesen, nama produk, bentuk dos, teks indikasi yang diluluskan), yang tidak dikembalikan dalam pakej ini walaupun terdapat 10 pendaftaran yang tersedia

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

