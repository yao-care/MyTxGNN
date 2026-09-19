---
layout: default
title: Desmopressin
parent: Low Evidence (L4-L5)
nav_order: 259
evidence_level: L4
indication_count: 7
---

# Desmopressin
{: .fs-9 }

Tahap bukti: **L4** | Indikasi diramal: **7** 
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

# Desmopressin: Dari Indikasi Asal (Tidak Diekstrak) ke Kekurangan Protrombin Kongenital

## Ringkasan Satu Ayat

Desmopressin (DrugBank DB00035) ialah ubat terdaftar di Taiwan (7 lesen TFDA, status pasaran "Dipasarkan"), walaupun teks indikasi asal yang berlabel tidak ditangkap dalam ekstrak data ini. Ramalan teratas model TxGNN ialah keberkesanan dalam **kekurangan protrombin kongenital**, tetapi bukti yang menyokong — **1 uji klinis** (mengkaji ubat yang berbeza, emicizumab) dan **4 penerbitan** (tidak ada yang secara khusus menangani penyakit ini) — tidak membuktikan pasangan mekanik, dan pakej bukti itu sendiri menandainya sebagai kemungkinan **ketidakpadanan bukti**.

---

## Panduan Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tersedia — teks indikasi lesen TFDA tidak diekstrak untuk mana-mana 7 pendaftaran (Jurang Data DG001) |
| Indikasi Baru yang Diramalkan | Kekurangan Protrombin Kongenital |
| Skor Ramalan TxGNN | 99.70% |
| Tahap Bukti | L4 |
| Status Pasaran Malaysia (data TFDA/Taiwan) | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 7 |
| Keputusan yang Disyorkan | Tangguh |

---

## Mengapa Ramalan Ini Masuk Akal?

Data mekanisme tindakan terperinci untuk desmopressin tidak tersedia dalam rekod sumber (`original_moa` adalah Jurang Data yang ditandai, DG002). Bagaimanapun, rasional yang diperoleh daripada literatur pakej bukti itu sendiri secara konsisten menerangkan farmakologi desmopressin yang telah ditetapkan: ia adalah agonis reseptor vasopressin V2 yang mencetuskan pelepasan faktor von Willebrand endogen (vWF) dan Faktor VIII daripada badan Weibel-Palade endotel, dan meningkatkan perlekatan platelet. Mekanisme ini mendasari penggunaannya yang diterima (termasuk penggunaan di luar label) dalam hemofilia A ringan, penyakit von Willebrand, dan gangguan pelepasan platelet tertentu — pola yang tercermin dalam literatur yang dilampirkan pada beberapa indikasi lain yang diramalkan dalam pakej bukti ini (cth. PMID 36656570, PMID 21509710).

Untuk kekurangan protrombin (Faktor II) kongenital khususnya, mekanisme ini tidak terpakai: sintesis dan aktiviti protrombin tidak berkaitan dengan laluan pelepasan vWF/Faktor VIII yang desmopressin bertindak. Konsisten dengan ini, uji klinis yang dilampirkan (NCT04567511) mengkaji emicizumab — bukan desmopressin — untuk hemofilia A ringan, dan empat petikan literatur menyangkut hemofilia A yang diperoleh, kekurangan Faktor V/VIII gabungan, dan rawatan rasional umum gangguan pendarahan, tidak ada satupun yang secara langsung menangani kekurangan protrombin. Pakej bukti itu sendiri mencirikan ini sebagai "ketidakpadanan bukti": skor TxGNN yang tinggi tanpa asas mekanik atau klinis yang koheren.

Dua calon lain dalam kumpulan penilaian yang sama menunjukkan penjajaran yang lebih kuat secara material dan mungkin memerlukan susulan berasingan: **gangguan pelepasan primer platelet** (kedudukan 4, tahap bukti L3, peringkat keputusan S2, cadangan "Teruskan dengan Pengawalan") dan **trombasenia Glanzmann** (kedudukan 3, tahap bukti L3, peringkat keputusan S1, "Soalan Penyelidikan"), kedua-duanya disokong secara langsung oleh literatur yang relevan dengan mekanisme tentang kesan pemendekkan masa pendarahan desmopressin yang diketahui.

---

## Bukti Uji Klinis

| Nombor Uji | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Fasa 4 | Merekrut | 20 | Mengkaji Hemlibra (emicizumab) — bukan desmopressin — dalam hemofilia A ringan. Perkaitan dinilai **C** (rendah): ubat yang berbeza, indikasi yang berbeza daripada kekurangan protrombin kongenital. |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Ulasan | Autoimmunity Reviews | Diagnosis, etiologi, dan rawatan hemofilia A yang diperoleh — bukan kekurangan protrombin. |
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Ulasan | Drugs | Pilihan rawatan rasional untuk gangguan pendarahan kongenital secara umum (hemofilia A, penyakit von Willebrand). |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Laporan Kes | Rinsho Ketsueki | Pengurusan seksyen kaisar dengan penggantian Faktor VIII dalam kekurangan Faktor V/VIII gabungan — bukan kekurangan protrombin. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Laporan Kes | Rinsho Ketsueki | Pentadbiran DDAVP dalam kekurangan Faktor V/VIII gabungan — bukan kekurangan protrombin. |

Tidak ada literatur di atas yang secara langsung mengkaji desmopressin dalam kekurangan protrombin kongenital.

---

## Maklumat Pasaran Malaysia

Butiran peringkat lesen (nombor kebenaran, nama produk, bentuk dos, teks indikasi) tidak ditangkap untuk mana-mana 7 pendaftaran TFDA dalam ekstrak data ini — hanya kiraan agregat dan status pasaran ("Dipasarkan") tersedia. Menurut Jurang Data DG001, menyelesaikan ini memerlukan memuat turun dan menganalisis PDF label TFDA secara langsung.

---

## Pertimbangan Keselamatan

Sila merujuk sisipan pakej untuk maklumat keselamatan. Nota: Amaran label TFDA dan kontraindikasi untuk desmopressin tidak tersedia dalam ekstrak ini (Jurang Data DG001, keterukan: Menyekat) — jurang ini pada masa kini menghalang calon daripada memasuki peringkat penilaian keselamatan S1.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tangguh**

**Rasional:**
Skor TxGNN untuk kekurangan protrombin kongenital adalah tinggi, tetapi uji klinis yang dilampirkan dan bukti literatur tidak menangani pasangan ubat-penyakit ini, dan mekanisme yang mendasar (pelepasan vWF/Faktor VIII) tidak mempunyai sambungan yang ditetapkan dengan sintesis atau aktiviti protrombin. Ini dinilai sebagai ketidakpadanan bukti yang mungkin daripada isyarat penyusunan semula yang tulen.

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran label TFDA/kontraindikasi (DG001, Menyekat) — diperlukan sebelum sebarang penilaian keselamatan boleh dimulai
- Butiran mekanisme tindakan DrugBank (DG002) untuk mengesahkan atau menolak mana-mana laluan tidak langsung kepada kekurangan protrombin
- Jika pasangan ubat-penyakit ini akan diikuti lebih lanjut, carian literatur/uji yang disasarkan khusus untuk desmopressin dan kekurangan Faktor II (tidak ada yang wujud dalam pakej ini)
- Pertimbangkan untuk mengutamakan semakan calon yang lebih kuat dalam kumpulan yang sama — **gangguan pelepasan primer platelet** (S2, "Teruskan dengan Pengawalan") dan **trombasenia Glanzmann** (S1, "Soalan Penyelidikan") — yang mempunyai sokongan mekanik dan literatur langsung

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

