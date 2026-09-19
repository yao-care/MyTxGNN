---
layout: default
title: Clobazam
parent: Low Evidence (L4-L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: Daripada Epilepsi kepada Febrile Infection-Related Epilepsy Syndrome (FIRES)

## Ringkasan Satu Ayat

> Clobazam ialah benzodiazepin yang pada asalnya digunakan sebagai agen antikonvulsan tambahan untuk epilepsi.
> Model TxGNN meramalkan ia mungkin berkesan untuk **Febrile Infection-Related Epilepsy Syndrome (FIRES)**,
> namun pada masa kini **0 uji klinik** dan **0 penerbitan** secara langsung menyokong arah khusus ini — ramalan ini bergantung pada model pengiraan sahaja.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|------|
| Indikasi Asal | Epilepsi / gangguan sawan (terapi tambahan) — pengetahuan ubat umum; tidak disahkan oleh paket data, kerana `original_indications` dan teks indikasi lesen NPRA kedua-duanya kosong |
| Indikasi Baru Yang Diramalkan | Febrile infection-related epilepsy syndrome (FIRES) |
| Skor Ramalan TxGNN | 99.82% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan Yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa kini, data mekanisme tindakan terperinci tidak tersedia (DG002, medan MOA DrugBank mengembalikan tiada data). Berdasarkan pengetahuan farmakologi umum, clobazam ialah benzodiazepin 1,5 yang bertindak sebagai modulator alosterik positif reseptor GABA-A, dan keberkesanannya sebagai antiepileptik tambahan (contohnya, dalam sindrom Lennox-Gastaut) telah ditubuhkan dengan baik. Mekanisme tahap kelas ini belum diverifikasi secara bebas untuk calon ini dalam paket bukti semasa.

FIRES ialah ensefalopati epileptik yang jarang dan teruk yang mengikuti penyakit berjangkit dengan demam serta mempersembahkan status epileptikus baru yang sangat tahan ubat, didorong oleh ketidakseimbangan yang berlebihan antara aktiviti rangsangan dan perencatan di korteks. Benzodiazepine, termasuk clobazam, diposisikan secara mekanistik untuk mengurangkan keterangsangan ini melalui potensiasi GABAergik, yang konsisten dengan alasan model TxGNN menghubungkan antikonvulsan yang memodulasi GABA-A kepada sindrom sawan yang tahan ubat.

Walau bagaimanapun, kebolehmungkinan mekanistik ini adalah teoretis. Tiada rekod ujian klinik atau kesusasteraan dalam paket bukti ini — mahupun dalam log pertanyaan asas (0 keputusan merentas ClinicalTrials.gov, ICTRP, dan PubMed untuk carian clobazam + FIRES) — memberikan sokongan langsung. Ramalan harus diperlakukan sebagai isyarat penjanaan hipotesis sahaja.

---

## Bukti Ujian Klinik

Pada masa kini tiada ujian klinik berkaitan didaftarkan.

---

## Bukti Kesusasteraan

Pada masa kini tiada kesusasteraan berkaitan tersedia.

---

## Maklumat Pasaran Malaysia

clobazam disahkan sebagai dipasarkan di Malaysia di bawah NPRA, dengan 1 pendaftaran aktif. Maklumat lesen terperinci (nombor pendaftaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak dikembalikan oleh sumber data dan tidak tersedia dalam paket bukti ini.

---

## Pertimbangan Keselamatan

Sila rujuk maklumat dalam bungkus untuk panduan keselamatan.

*(Nota: Data amaran utama, kontraindikasi, dan interaksi ubat tidak tersedia daripada sumber yang ditanya — ini ditandai sebagai jurang data yang menghalang (DG001) yang pada masa kini menghalang penyaringan keselamatan untuk calon ini.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Skor ramalan TxGNN tinggi, tetapi tidak disokong oleh sebarang bukti ujian klinik atau kesusasteraan (Tahap Bukti L5), dan jurang data yang menghalang dalam pelabelan keselamatan (DG001) bermakna calon ini belum dapat melepasi penyaringan keselamatan awal.

**Untuk meneruskan, perkara-perkara berikut diperlukan:**
- Maklumat dalam bungkus ubat TFDA/NPRA (amaran, kontraindikasi) untuk menyelesaikan DG001
- Mekanisme tindakan yang disahkan daripada DrugBank untuk menyelesaikan DG002
- Pencarian kesusasteraan/ujian yang lebih luas menggunakan istilah berkaitan (contohnya, "super-refractory status epilepticus," "benzodiazepine + FIRES") kerana FIRES ialah sindrom yang jarang yang mungkin tidak diindeks di bawah nama tepatnya
- Pengesahan indikasi asal dan butiran lesen Malaysia yang masih tiada daripada kedua-duanya `drug.original_indications` dan `taiwan_regulatory.licenses`

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

