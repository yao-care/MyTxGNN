---
layout: default
title: Deferiprone
parent: Low Evidence (L4-L5)
nav_order: 254
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **9** 
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

# Deferiprone: Dari Beban Besi (Talasemia) ke Porfira Hepatik

## Ringkasan Satu Ayat

> Deferiprone ialah chelator besi oral; berdasarkan pengetahuan ubat am (Ferriprox), ia digunakan untuk beban besi transfusi dalam talasemia, walaupun medan `original_indications` dalam pakej bukti ini sedang menjadi jurang data. Ramalan berada di kedudukan teratas model TxGNN ialah **Porfira Hepatik**, tetapi ini disokong oleh **0 uji klinik** dan **0 penerbitan** — rasional model sendiri menandakannya sebagai kemungkinan positif palsu yang didorong oleh pengelompokan embedding graf daripada isyarat farmakologi tulen.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Beban besi dalam talasemia (pengetahuan latar belakang, dirujuk dalam rasional kedudukan ke-8 pakej ini sebagai penggunaan yang diluluskan Ferriprox; **tidak bersumber daripada data TFDA/NPRA** — `original_indications` ialah jurang data) |
| Indikasi Baru yang Diramal | Porfira Hepatik |
| Skor Ramalan TxGNN | 99.20% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 6 |
| Keputusan yang Disarankan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia (`original_moa` = Jurang Data). Berdasarkan rasional TxGNN yang disediakan dalam pakej ini, deferiprone ialah chelator besi ferik yang selektif, dan porfira hepatik melibatkan gangguan laluan biosintesis hem, yang mana besi diperlukan sebagai kofaktor. Ini memberikan pautan laluan teori, tidak langsung antara farmakologi ubat yang diketahui dan penyakit yang diramal.

Bagaimanapun, arah pautan ini dijelaskan secara eksplisit tidak jelas dalam rasional asas: chelasi besi yang berlebihan boleh sama munasabahnya memburukkan subtype porfira tertentu dengan menyebabkan kekurangan besi, daripada membantu. Tiada bukti klinikal, praklinik, atau laporan kes dalam pakej bukti ini untuk menyelesaikan ketidakjelasan tersebut.

Adalah juga patut dinyatakan bahawa kedudukan 2–6 dalam senarai indikasi-ramalan (sirosis yang berkaitan dengan tembaga idiopatik, hipertensi portal, sklerosis hepatoportal, trombosis vena portal, sindrom hepatopulmoner) semua membawa skor hampir sama (~0.99196) satu sama lain dan kekurangan sebarang rasional mekanik khusus ubat. Anotasi pakej bukti sendiri mengaitkan ini dengan pengelompokan nod "penyakit hati" graf pengetahuan TxGNN daripada isyarat farmakologi nyata yang khusus ubat — corak yang juga menimbulkan hati-hati tentang ramalan porfira hepatik berpangkat teratas, kerana ia berada dalam jalur skor yang sama.

---

## Bukti Uji Klinik

Pada masa ini, tiada uji klinik yang terkait didaftarkan.

---

## Bukti Kesusasteraan

Pada masa ini, tiada kesusasteraan yang terkait tersedia.

---

## Maklumat Pasaran Malaysia

Pakej bukti merekodkan 6 jumlah pendaftaran keseluruhan dengan status pasaran "Dipasarkan" (Dipasarkan), tetapi 5 entri lesen yang dikembalikan tidak mengandungi medan yang diisi (nombor lesen, nama produk, bentuk dos, pengilang, dan teks indikasi semuanya kosong) — ini ialah jurang data dalam pertanyaan sumber, bukan ketiadaan pendaftaran. Butiran peringkat lesen perlu dikumpul semula daripada NPRA sebelum ia boleh dilaporkan di sini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Ramalan berpangkat teratas (porfira hepatik) disokong hanya oleh skor L5, model sahaja tanpa uji klinik atau kesusasteraan, dan rasional mekanik itu sendiri menandakan ketidakjelasan arah — chelasi besi boleh munasabahnya memburukkan beberapa subtype porfira daripada merawatnya. Beberapa ramalan jiran dalam jalur skor yang sama menunjukkan tanda-tanda menjadi artifak pengelompokan graf daripada isyarat tulen, yang seterusnya melemahkan keyakinan dalam hasil kedudukan pertama khusus ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran sisipan paket TFDA/NPRA dan kontraindikasi (DG001, menghalang — diperlukan sebelum mana-mana screening keselamatan S1)
- Data mekanisme tindakan yang disahkan daripada DrugBank (DG002)
- Kajian praklinik atau mekanik yang menjelaskan *arah* kesan chelasi besi merentas subtype porfira sebelum mempertimbangkan porfira hepatik sebagai calon penggunaan semula
- Pengesahan `original_indications` (sedang kosong) — perhatian bahawa **talasemia beta dengan manifestasi lain (kedudukan 8)** nampaknya penggunaan deferiprone yang sudah diluluskan (Ferriprox), bukan indikasi yang benar-benar baru; ini harus disahkan supaya ia tidak disalah kira sebagai calon penggunaan semula
- Data lesen/indikasi Malaysia yang diisi untuk menggantikan entri kosong semasa

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

