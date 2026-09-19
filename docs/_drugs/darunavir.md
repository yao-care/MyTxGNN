---
layout: default
title: Darunavir
parent: Low Evidence (L4-L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **4** 
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

# Darunavir: Daripada Perencat Protease HIV-1 kepada Tiada Indikasi Baru yang Boleh Diambil Tindakan

## Ringkasan Satu Ayat

Darunavir (DrugBank DB01264) ialah perencat protease HIV-1 yang telah mantap; teks indikasi khusus yang diluluskan TFDA tidak hadir dalam ekstrak data semasa, dan perincian mekanisme tindakan juga hilang menunggu pertanyaan API DrugBank. Ramalan TxGNN yang berpangkat paling tinggi, **feline acquired immunodeficiency syndrome**, bersama tiga calon lain, disokong oleh **0 ujian klinikal** dan **0 penerbitan**, dan rasional mekanik yang disertakan untuk setiap calon membuat hujah menentang kebolehupayaan klinikal yang munasabah daripada menyokongnya.

---

## Tinjauan Cepat

| Item | Kandungan |
|------|--------|
| Indikasi Asal | Tidak tersedia dalam rekod semasa (teks indikasi lesen TFDA adalah kosong; darunavir ialah perencat protease HIV-1 yang diiktiraf kelas) |
| Indikasi Baru yang Diramalkan | Feline Acquired Immunodeficiency Syndrome |
| Skor Ramalan TxGNN | 99.97% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | Tangguh |

---

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan terperinci tidak tersedia pada masa ini (ditandai sebagai jurang data berketerasan tinggi, remediasi: pertanyaan API DrugBank). Berdasarkan pengetahuan farmakologi umum, darunavir ialah perencat protease HIV-1 peptidomimetik yang digunakan untuk menghalang kematangan virus dalam jangkitan HIV-1 manusia.

Ramalan TxGNN yang berpangkat tertinggi — feline acquired immunodeficiency syndrome (FIV) — ialah penyakit veterinar di luar skop ubat pelbagai guna manusia, dan rasional model itu sendiri melemahkan ramalan: protease FIV mempunyai homologi urutan rendah dengan protease HIV, dan farmakologi veterinar yang diterbitkan menunjukkan kebanyakan perencat protease HIV menunjukkan aktiviti persilangan-perencat yang sedikit atau tiada terhadap protease FIV. Calon berpangkat kedua (jangkitan SIV) ialah konstruk penyelidikan primata bukan manusia/model hewan dan bukannya indikasi klinikal manusia, jadi ia tidak boleh diterjemahkan ke dalam laluan pelbagai guna manusia walaupun terdapat homologi protease teori. Calon ketiga (gangguan neurokembangan yang jarang) tiada pautan biologi yang diketahui dengan perencatan protease dan dinilai sebagai kemungkinan artifak daripada pemprosesan data model graf-pengetahuan. Calon keempat (hiperlidemia gabungan keluarga) adalah tidak munasabah dari segi arah: dislipidemia ialah kesan sampingan yang terdokumen dengan baik bagi perencat protease HIV sebagai satu kelas (melalui kesan metabolisme lipid yang dimediasi SREBP-1), bukan sasaran terapeutik — persatuan KG kemungkinan besar mencerminkan kejadian bersama ubat-peristiwa sampingan yang disalah baca sebagai perhubungan rawatan, dan istilah penyakit itu sendiri ditandai sebagai "usang" dalam ontologi yang mendasari.

Tiada satu pun daripada keempat-empat calon mempersembahkan isyarat pelbagai guna klinikal yang boleh diambil tindakan dan munasabah secara mekanik berdasarkan bukti yang tersedia pada masa ini.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal yang berkaitan berdaftar.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan tersedia.

---

## Maklumat Pasaran Malaysia

Darunavir mempunyai 1 lesen berdaftar dan sedang dipasarkan, tetapi rekod lesen dalam ekstrak data semasa tidak merangkumi nombor lesen, nama produk, bentuk dos, atau teks indikasi yang diluluskan — medan-medan ini kosong menunggu pengesahan sumber.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. (Nota: pengambilan amaran/kontraindikasi sisipan pakej TFDA ialah jurang data terbuka, berketerasan penghalang — lihat Kesimpulan di bawah.)

---

## Kesimpulan dan Langkah-Langkah Seterusnya

**Keputusan: Tangguh**

**Rasional:**
Semua empat calon yang diramalkan TxGNN ialah Tahap Bukti L5 (ramalan model sahaja) tanpa ujian klinikal atau kesusasteraan yang menyokong, dan rasional mekanik model itu sendiri untuk setiap calon sama ada mengenal pasti ketidakpadanan spesies/terjemahan (penyakit veterinar atau model hewan), kemungkinan artifak pembenaman, atau arah kausa yang terbalik (kesan sampingan yang diketahui disalah baca sebagai indikasi). Tiada isyarat pelbagai guna klinikal yang boleh diambil tindakan dalam set calon ini.

**Untuk meneruskan, berikut diperlukan:**
- Sisipan pakej TFDA (amaran/kontraindikasi) — Jurang data berketerasan penghalang (DG001); diperlukan sebelum sebarang pemeriksaan keselamatan S1 dapat berlaku
- Mekanisme tindakan darunavir melalui API DrugBank — Jurang berprioriti tinggi (DG002); diperlukan untuk analisis pautan mekanik
- Teks indikasi yang diluluskan TFDA yang disahkan daripada rekod lesen (pada masa ini kosong)
- Pemeriksaan semula keluaran TxGNN melangkaui 4 teratas semasa (pangkat 806–10,598) untuk calon dengan kaitan penyakit manusia yang munasabah dan sokongan ujian/kesusasteraan yang bukan sifar

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

