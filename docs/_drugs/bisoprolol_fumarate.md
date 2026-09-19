---
layout: default
title: Bisoprolol Fumarate
parent: Low Evidence (L4-L5)
nav_order: 150
evidence_level: L5
indication_count: 0
---

# Bisoprolol Fumarate
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

# Bisoprolol Fumarate: Laporan Penilaian Penggunaan Semula Ubat

## Ringkasan Satu Ayat

Bisoprolol fumarate adalah penyekat reseptor adrenergik beta-1 selektif yang digunakan secara meluas untuk pengurusan hipertensi dan kegagalan jantung. Model TxGNN **tidak menghasilkan sebarang petunjuk indikasi baru** untuk ubat ini dalam kitaran analisis semasa. Dengan 34 pendaftaran di Malaysia, ubat ini mempunyai kehadiran pasaran yang mantap tetapi memerlukan pengumpulan data tambahan sebelum penilaian penggunaan semula dapat dilanjutkan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Indikasi Asal | Hipertensi, kegagalan jantung (butiran lesen tidak tersedia dalam data semasa) |
| Indikasi Ramalan Baru | — (Tiada ramalan dijana) |
| Skor Ramalan TxGNN | — |
| Aras Bukti | L5 (Tiada ramalan atau kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 34 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada indikasi ramalan yang dijana oleh model TxGNN untuk Bisoprolol Fumarate dalam pusingan analisis ini. Ini mungkin disebabkan oleh satu atau lebih sebab berikut:

1. **Pemetaan ID DrugBank yang hilang**: Pakej Bukti menunjukkan `drugbank_id: null`. Tanpa pengecam DrugBank yang sah, ubat tidak dapat dipautkan dengan betul ke dalam graf pengetahuan TxGNN, mencegah model daripada menjana ramalan ubat–penyakit. Log pertanyaan menunjukkan pertanyaan DrugBank telah dilaksanakan dengan 1 hasil dikembalikan, tetapi ID tidak berjaya dipetakan ke dalam pakej bukti.

2. **Teks indikasi yang tidak lengkap**: Kesemua lima rekod lesen dalam data kawal selia mempunyai medan `approved_indication_text` yang kosong. Tanpa maklumat indikasi yang diuraikan, sistem tidak dapat menentukan konteks terapeutik asal ubat atau memetakannya ke nod penyakit dalam graf pengetahuan.

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam pakej bukti ini. Berdasarkan pengetahuan farmakologi yang ditubuhkan, Bisoprolol adalah antagonis reseptor adrenergik beta-1 yang sangat selektif (penyekat beta yang kardioselek). Ia mengurangkan kadar jantung, kebolehkontraktusan miokardium, dan tekanan darah dengan menghalang reseptor beta-1 dalam tisu jantung. Indikasi yang ditubuhkannya termasuk hipertensi penting, angina stabil kronik, dan kegagalan jantung kronik (sebagai terapi tambahan). Mekanisme ini boleh secara teorinya relevan kepada keadaan sistem kardiovaskular atau sistem saraf simpatetik yang lain, tetapi tiada ramalan pengiraan tersedia untuk dinilai pada masa ini.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang dikenal pasti — tiada indikasi ramalan dijana untuk penilaian.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang dikenal pasti — tiada indikasi ramalan dijana untuk penilaian.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|------|------|------|------|
| (tidak tersedia) | (tidak tersedia) | (tidak tersedia) | (tidak tersedia) |
| (tidak tersedia) | (tidak tersedia) | (tidak tersedia) | (tidak tersedia) |
| (tidak tersedia) | (tidak tersedia) | (tidak tersedia) | (tidak tersedia) |
| (tidak tersedia) | (tidak tersedia) | (tidak tersedia) | (tidak tersedia) |
| (tidak tersedia) | (tidak tersedia) | (tidak tersedia) | (tidak tersedia) |

> **Nota:** 34 pendaftaran telah diambil daripada NPRA, tetapi medan lesen terperinci (nombor kebenaran, nama produk, bentuk dos, indikasi diluluskan) tidak diisi dalam pakej bukti semasa. Pengekstrakan semula daripada pangkalan data NPRA diperlukan.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti ini. Sebagai penyekat beta yang dikenali, langkah berjaga-jaga umum termasuk penghindaran pada pesakit dengan bradikardia teruk, syok kardiogenik, kegagalan jantung yang tidak terkompensasi, sindrom sinus sakit (tanpa alat rentak), asma bronkial yang teruk, dan feokromositoma (tanpa liputan penyekat alfa).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Tiada ramalan TxGNN dijana untuk Bisoprolol Fumarate disebabkan oleh jurang data kritikal — khususnya, pemetaan ID DrugBank yang hilang dan medan indikasi lesen yang kosong. Tanpa pautan graf pengetahuan yang sah, saluran ramalan penggunaan semula tidak dapat dilaksanakan. Ini adalah isu kelengkapan data, bukan isyarat negatif tentang potensi penggunaan semula ubat.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Resolusi ID DrugBank (Pemblokiran):** Sahkan dan isi ID DrugBank (jangkaan: [DB01612](https://go.drugbank.com/drugs/DB01612) untuk Bisoprolol). Log pertanyaan menunjukkan 1 hasil dikembalikan — selidik mengapa ia tidak dipetakan.
2. **Pengekstrakan butiran lesen NPRA (Pemblokiran):** Ekstrak semula 34 rekod lesen NPRA dengan medan lengkap (nombor kebenaran, nama produk, bentuk dos, teks indikasi diluluskan).
3. **Mekanisme tindakan (Keutamaan Tinggi):** Ambil data MOA daripada API DrugBank untuk membolehkan penaakulan mekanisme–indikasi.
4. **Data keselamatan (Pemblokiran untuk penilaian S1):** Ekstrak amaran sisipan pakej dan kontraindikasi daripada NPRA atau PDF label produk.
5. **Jalankan semula ramalan TxGNN:** Setelah ID DrugBank dan data indikasi diisi, jalankan semula saluran ramalan KG + DL untuk menjana calon penggunaan semula.

---

*Penafian: Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Mana-mana calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

