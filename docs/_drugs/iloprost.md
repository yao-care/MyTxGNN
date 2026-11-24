---
layout: default
title: Iloprost
parent: Low Evidence (L4-L5)
nav_order: 409
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
description: "Iloprost: indikasi baharu diramal Hipotrikosis simpleks kulit kepala (hypotrichosis simplex of the scalp) (tahap bukti L5). Di Malaysia, pendaftaran NPRA: 1 (sah: 1)"
---

# Iloprost
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **4** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Laporan penilaian ahli farmasi

</div>

## Iloprost: Hipotrikosis simpleks kulit kepala (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Ringkasan Satu Ayat

Iloprost ialah analog prostasiklin yang pada asalnya digunakan untuk merawat hipertensi arteri pulmonari (PAH).
Model TxGNN meramalkan ia mungkin berkesan untuk **hipotrikosis simpleks kulit kepala**,
tetapi pada masa ini terdapat **0 ujian klinikal** dan **0 penerbitan** yang menyokong arah ini, jadi ramalan ini berasaskan model semata-mata.

---

## Gambaran Ringkas

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Tidak direkodkan dalam data tempatan |
| Indikasi Baharu yang Diramalkan | Hipotrikosis simpleks kulit kepala (hypotrichosis simplex of the scalp) |
| Skor Ramalan TxGNN | 0.9945 |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 1 daripada 1) |
| Bilangan Pendaftaran | 1 (sah: 1) |
| Keputusan Disyorkan | Hold (Tangguh) |

---

## Mengapa Ramalan Ini Munasabah?

Menurut bahagian “Mechanism of Action” maklumat preskripsi yang diluluskan oleh FDA Amerika Syarikat (Prescribing Information) bagi Iloprost (terjemahan tidak rasmi): “Iloprost ialah analog sintetik prostasiklin PGI 2. Iloprost ialah vasodilator dan merencat pengagregatan platelet.” Teks asal bahasa Inggeris: "Iloprost is a synthetic analog of prostacyclin PGI 2. Iloprost is a vasodilator and inhibits platelet aggregation." ([DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4), versi 2026-08-13; diakses 2026-11-19). Berdasarkan maklumat sedia ada, iloprost ialah analog prostasiklin (PGI2) yang stabil. Keberkesanannya dalam PAH sudah dibuktikan, dan secara mekanistik ia mungkin ada kaitan dengan isyarat prostaglandin dalam biologi folikel rambut.

Kaitan ini bersifat teori. Beberapa analog prostaglandin F2α diketahui menggalakkan pertumbuhan rambut, manakala PGD2 menghalangnya. Kesan iloprost sebagai agonis prostasiklin ke atas pertumbuhan rambut belum pasti dan tiada data yang menyokongnya di sini.

Hipotrikosis simpleks ialah keadaan keturunan monogenik. Rawatan berasaskan vasodilator tidak mungkin menangani punca genetiknya. Skor model TxGNN (pembelajaran mendalam) yang sangat tinggi mungkin hanya mencerminkan persamaan yang dipelajari oleh model antara penyakit yang berkaitan, dan bukan bukti biologi mahupun rasional farmakologi yang sebenar.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan.

---

## Pertimbangan Keselamatan

Data label (amaran utama dan kontraindikasi daripada sisipan pakej) belum diperoleh. Maklumat di bawah datang daripada graf pengetahuan dan pangkalan data interaksi ubat.

- **Kontraindikasi (daripada graf pengetahuan, bukan teks label):** kegagalan hati, penyakit pulmonari obstruktif kronik (COPD), COPD teruk awal permulaan, gangguan hipotensi, edema pulmonari dan penyakit bronkus.
- **Interaksi Ubat:** 100 interaksi dikenal pasti. Antara yang bertahap sederhana ialah:
  - epinefrin, efedrin (termasuk nasal)
  - asid asetilsalisilik
  - perencat SGLT2 (kanagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - insulin manusia (disedut, bertindak pantas)
  - manitol, gliserin, papaverin
  - fenfluramin, deksfenfluramin, sibutramin

  Beberapa interaksi lain (contohnya kalsitriol, pantoprazol, morfin, metformin, omeprazol) bertahap tidak diketahui.

Sila rujuk sisipan pakej untuk maklumat keselamatan yang lengkap.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold (Tangguh)**

**Justifikasi:**
- Ramalan ini hanya berasaskan model (L5) tanpa ujian klinikal atau literatur. Mekanisme vasodilator juga tidak sepadan dengan sifat genetik keadaan ini, jadi ia tidak wajar diteruskan pada masa ini.
- Sebagai perbandingan, dua indikasi lain dalam senarai ramalan yang sama mempunyai sokongan lebih kukuh, iaitu **PAH berkaitan penyakit jantung kongenital** dan **PAH berkaitan penyakit tisu penghubung**. Kedua-duanya berada pada tahap bukti L3 (kajian pemerhatian) dengan syor *Proceed with Guardrails*. Kedua-duanya masih dalam kelas PAH, jadi ia lebih merupakan lanjutan penggunaan sedia ada daripada pengalihan fungsi sebenar. Jika matlamatnya ialah mengutamakan calon, kedua-dua indikasi ini wajar dinilai dahulu.

**Untuk meneruskan, perkara berikut diperlukan:**
- Muat turun dan huraikan sisipan pakej NPRA untuk amaran dan kontraindikasi (data keselamatan yang menghalang penyaringan keselamatan).
- Data mekanisme tindakan (MOA) terperinci daripada DrugBank.
- Bukti prasiklinikal atau klinikal yang menghubungkan iloprost dengan biologi folikel rambut atau hipotrikosis keturunan.
- Penilaian keserasian laluan pentadbiran (iloprost sedia ada ialah bentuk disedut atau intravena, sedangkan keadaan ini bersifat kulit kepala).
- Pengesahan status pendaftaran iloprost di Malaysia.

<!-- review:begin my-lic-20261105-iloprost-1 -->

> **Pembetulan semakan (2026-11-05)**: Asalnya dinyatakan: "Pengesahan status pendaftaran iloprost di Malaysia, kerana tiada lesen berdaftar direkodkan." Dipadam: ia menyatakan ubat ini tidak berdaftar, pendaftarannya dibatalkan atau tamat tempoh, atau tidak dipasarkan di Malaysia, yang tidak sepadan dengan data pendaftaran produk NPRA (data.gov.my) yang dibina semula mengikut bahan aktif pada 2026-11-05. Bilangan pendaftaran semasa terdapat dalam Gambaran Ringkas halaman ini. Sumber: [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products).

<!-- review:end my-lic-20261105-iloprost-1 -->

<!-- review:begin log -->

## Rekod Semakan

Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA (data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan tidak ditulis semula. Ayat yang menyatakan data mekanisme tindakan tidak tersedia telah diganti dengan petikan daripada maklumat preskripsi rasmi yang dipetik (dengan terjemahan tidak rasmi).

| Tarikh semakan | Perkara | Tindakan | Sumber |
|------|------|------|------|
| 2026-11-05 | Dipadam: "kerana tiada lesen berdaftar direkodkan" | Dibetulkan (disemak 2026-11-24; versi terdahulu disimpan dalam rekod) | [NPRA pharmaceutical product registrations (data.gov.my)](https://data.gov.my/data-catalogue/pharmaceutical_products) |
| 2026-11-19 | Ayat “data mekanisme tindakan tidak tersedia” diganti dengan petikan maklumat preskripsi AS | Ayat bahawa data mekanisme tindakan tidak tersedia diganti dengan petikan bersumber | [DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4) |

<!-- review:end log -->

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

