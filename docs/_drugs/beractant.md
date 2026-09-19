---
layout: default
title: Beractant
parent: Low Evidence (L4-L5)
nav_order: 134
evidence_level: L5
indication_count: 0
---

# Beractant
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

# Beractant: Surfaktan Pulmonari — Tiada Petunjuk Indikasi Baru

## Ringkasan Satu Ayat

Beractant ialah surfaktan pulmonari bovine semula jadi yang ditunjukkan untuk pencegahan dan rawatan Respiratory Distress Syndrome (RDS) pada bayi prematur. Model TxGNN **tidak menghasilkan sebarang petunjuk indikasi baru** untuk ubat ini. Digabungkan dengan jurang data yang ketara dalam mekanisme tindakan dan maklumat keselamatan, calon ini pada masa ini kekurangan asas yang mencukupi untuk penilaian ubat yang digunakan semula.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Neonatal Respiratory Distress Syndrome (RDS) — *teks lesen tidak tersedia dalam data* |
| Petunjuk Indikasi Baru | **Tiada** (tiada petunjuk TxGNN dihasilkan) |
| Skor Petunjuk TxGNN | N/A |
| Tahap Bukti | **L5** — Tiada petunjuk, tiada kajian sokongan |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 2 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Tiada Petunjuk?

Beractant (nama jenama: Survanta) ialah ekstrak surfaktan paru-paru yang diperoleh daripada lembu yang mengandungi fosfolipid, lipid neutral, asid lemak, dan protein yang berkaitan surfaktan (SP-B dan SP-C). Ia berfungsi dengan mengurangkan ketegangan permukaan di antarmuka udara–cecair alveoli, mencegah kolaps alveolar pada bayi prematur yang paru-parunya belum menghasilkan surfaktan endogen yang mencukupi.

Model TxGNN tidak menghasilkan sebarang calon ubat yang digunakan semula untuk beractant. Ini mungkin disebabkan oleh beberapa faktor:

1. **Mekanisme yang sangat khusus**: Beractant bertindak sebagai pengganti surfaktan fizikal dan bukannya melalui sasaran farmakologi konvensional (reseptor, enzim, atau laluan). Model berasaskan graf pengetahuan seperti TxGNN bergantung pada hubungan ubat–sasaran–penyakit, dan mekanisme beractant tidak memetakan dengan baik kepada sasaran yang boleh diubati secara tipikal.

2. **Keterhubungan graf pengetahuan yang terbatas**: Sebagai surfaktan yang diperolehi secara biologi, beractant mungkin mempunyai sambungan yang jarang dalam graf pengetahuan TxGNN (beberapa interaksi ubat–sasaran atau ubat–gen yang direkodkan dalam DrugBank), mengurangkan keupayaan model untuk membuat kesimpulan tentang perkaitan penyakit yang baru.

3. **Penggunaan klinikal yang khusus**: Beractant diberikan secara intratrakhea kepada bayi neonatal — laluan dan populasi yang sangat khusus — yang seterusnya mengehadkan inferens indikasi silang.

---

## Bukti Ujian Klinikal

Tiada petunjuk indikasi yang dihasilkan oleh TxGNN; oleh itu, tiada carian ujian klinikal yang disasarkan telah dilakukan untuk arah ubat yang digunakan semula.

> Pada masa ini tiada ujian klinikal yang berkaitan untuk indikasi baru untuk dilaporkan.

---

## Bukti Kesusasteraan

Tiada petunjuk indikasi yang dihasilkan oleh TxGNN; oleh itu, tiada carian kesusasteraan yang disasarkan telah dilakukan untuk arah ubat yang digunakan semula.

> Pada masa ini tiada kesusasteraan yang berkaitan untuk indikasi baru untuk dilaporkan.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(tidak tersedia)* | *(tidak tersedia)* | *(tidak tersedia)* | *(tidak tersedia)* |

> Dua pendaftaran direkodkan dalam pangkalan data NPRA, tetapi maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak ditangkap dalam ekstraksi data semasa. Sila dayakan portal [NPRA Quest3+](https://quest3plus.bpfk.gov.my/) secara terus untuk butiran lengkap.

---

## Pertimbangan Keselamatan

> Sila rujuk leaflet bungkusan untuk maklumat keselamatan. Data amaran kunci, kontraindikasi, dan interaksi ubat tidak tersedia dalam pakej bukti semasa.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Model TxGNN tidak menghasilkan sebarang calon ubat yang digunakan semula untuk beractant. Ini mungkin didapati daripada mekanisme unik ubat sebagai pengganti surfaktan fizikal (bukan agen farmakologi konvensional), yang menghasilkan keterhubungan terbatas dalam graf pengetahuan. Tanpa petunjuk indikasi, tiada hipotesis ubat yang digunakan semula yang boleh diambil tindakan untuk dinilai.

**Untuk meninjau semula calon ini, perkara berikut akan diperlukan:**
- Pengayaan nod graf pengetahuan beractant dengan anotasi ubat–sasaran dan ubat–laluan tambahan (cth., interaksi protein surfaktan, laluan metabolisme lipid)
- Data mekanisme tindakan terperinci (pada masa ini jurang data)
- Maklumat lesen NPRA lengkap (nombor kebenaran, nama produk, teks indikasi yang diluluskan)
- Data keselamatan leaflet bungkusan (amaran kunci, kontraindikasi)
- Pertimbangkan sama ada persediaan surfaktan alternatif (poractant alfa, calfactant) mempunyai data KG yang lebih kaya yang boleh memaklumkan rujukan silang

---

*Penafian: Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon ubat yang digunakan semula memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

