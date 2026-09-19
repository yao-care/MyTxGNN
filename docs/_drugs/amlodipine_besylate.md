---
layout: default
title: Amlodipine Besylate
parent: Low Evidence (L4-L5)
nav_order: 59
evidence_level: L5
indication_count: 0
---

# Amlodipine Besylate
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

# Amlodipine Besylate: Dari Hipertensi/Angina — Ramalan Pengubahgunaan Ubat Belum Tersedia

## Ringkasan Satu Ayat

Amlodipine Besylate ialah penghambat saluran kalsium dihidropiridin yang telah ditetapkan dengan baik dan diresepkan secara meluas untuk hipertensi dan angina pectoris, dengan 50 lesen produk berdaftar di Malaysia. Pakej Bukti semasa mengandungi **tiada ramalan pengubahgunaan ubat yang dihasilkan oleh TxGNN** untuk sebatian ini, kerana pautan ID DrugBank dan data mekanisme tindakan kedua-duanya merupakan jurang data yang belum diselesaikan. Laporan ini meringkaskan maklumat yang tersedia dan mengesyorkan keputusan **Tahan** sehingga saluran paip selesai.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Tidak diisi dalam Pakej Bukti ini |
| Petunjuk Baru yang Diramalkan | Tiada — tiada ramalan pengubahgunaan ubat TxGNN yang dihasilkan |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | N/A |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 50 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Masuk Akal?

Tiada ramalan pengubahgunaan ubat yang dihasilkan untuk Amlodipine Besylate dalam Pakej Bukti ini. Tatasusunan `predicted_indications` adalah kosong, yang biasanya menunjukkan bahawa sebatian itu tidak dapat berjaya dipautkan ke nod dalam graf pengetahuan TxGNN — kemungkinan besar kerana ID DrugBank tidak diselesaikan (dicatat sebagai `null` walaupun terdapat pertanyaan API DrugBank yang berjaya pada 2026-03-27).

Pada masa ini, data mekanisme tindakan terperinci tidak tersedia dalam Pakej Bukti ini. Berdasarkan pengetahuan farmakoloji umum, Amlodipine Besylate ialah penghambat saluran kalsium L-jenis berdaya voltan yang selektif dalam otot polos vaskular dan miokardium jantung kelas dihidropiridin jangka panjang. Ia mengurangkan rintangan vaskular persifer dan keperluan oksigen miokardium. Mekanisme ini mendasari penggunaannya yang telah ditetapkan dalam hipertensi dan angina stabil kronik atau vasospastik. Pemblokiran saluran kalsium juga telah diterokai dalam kawasan terapeutik yang bersebelahan — termasuk fenomena Raynaud, hipertensi arteri pulmonari, dan vasospasma berkaitan pendarahan subaraknoid — tetapi tiada satu pun daripada ini muncul sebagai ramalan dalam pakej semasa.

Untuk menjana calon pengubahgunaan ubat yang sah, saluran paip data mesti terlebih dahulu mengesahkan ID DrugBank (dijangka: **DB00381**), pautkan sebatian itu ke nod graf pengetahuan TxGNN, dan jalankan semula larian ramalan.

---

## Bukti Ujian Klinikal

Tiada petunjuk yang diramalkan oleh TxGNN tersedia untuk sebatian ini. Bukti ujian klinikal khusus penyakit tidak dapat dibentangkan sehingga petunjuk sasaran dikenal pasti oleh model ramalan.

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan dalam konteks pengubahgunaan ubat.

---

## Bukti Kesusasteraan

Tiada petunjuk yang diramalkan oleh TxGNN tersedia untuk sebatian ini. Bukti kesusasteraan khusus penyakit tidak dapat dibentangkan sehingga petunjuk sasaran dikenal pasti oleh model ramalan.

Pada masa ini tiada kesusasteraan berkaitan yang tersedia dalam konteks pengubahgunaan ubat.

---

## Maklumat Pasaran Malaysia

Amlodipine Besylate memegang **50 lesen produk berdaftar** dengan Agensi Kawal Selia Farmaseutikal Kebangsaan Malaysia (NPRA), disahkan melalui pertanyaan pada 2026-03-27. Walau bagaimanapun, butiran peringkat produk individu (nombor lesen, nama produk, bentuk dos, teks petunjuk yang diluluskan) tidak dikembalikan dalam Pakej Bukti ini.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------------------|--------------|-----------|-----------------------|
| — | Butiran tidak diisi dalam Pakej Bukti ini | — | — |

> **Nota**: 50 lesen aktif disahkan melalui NPRA. Rekod peringkat produk penuh harus diambil terus daripada portal NPRA untuk mengisi jadual di atas sebelum meneruskan.

---

## Pertimbangan Keselamatan

Sila rujuk nota pengguna untuk maklumat keselamatan.

> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) ditandakan sebagai jurang data dalam Pakej Bukti ini. Tiada interaksi dikembalikan oleh pertanyaan DDI. Ini berkemungkinan disebabkan oleh ID DrugBank yang belum diselesaikan dan bukannya ketiadaan interaksi yang sebenar — Amlodipine diketahui mempunyai interaksi yang relevan secara klinikal dengan perencat/penginduksi CYP3A4.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Pakej Bukti ini secara struktur tidak lengkap — saluran paip ramalan TxGNN tidak dapat menjana calon pengubahgunaan ubat kerana pautan ID DrugBank gagal, dan semua medan petunjuk dan keselamatan adalah jurang data yang belum diselesaikan. Penilaian pengubahgunaan ubat yang bermakna tidak dapat diteruskan dalam keadaan ini.

**Untuk meneruskan, perkara berikut diperlukan:**

- **[Menghalang — DG001]** Ambil teks petunjuk yang diluluskan dan amaran keselamatan penuh (kontraindikasi, amaran kotak hitam) daripada nota pengguna produk NPRA-berdaftar Malaysia; ini diperlukan sebelum sebarang saringan keselamatan dapat dilakukan.
- **[Tinggi — DG002]** Sahkan dan rekodkan ID DrugBank untuk Amlodipine Besylate (dijangka: **DB00381**) melalui API DrugBank, dan ekstrak entri mekanisme tindakan penuh untuk menyokong analisis kebolehpercayaan mekanik.
- **Jalankan semula saluran paip ramalan TxGNN** dengan ID DrugBank yang disahkan untuk menjana calon pengubahgunaan ubat; ini akan membuka kunci semua bahagian hiliran (petunjuk yang diramalkan, bukti ujian klinikal, bukti kesusasteraan).
- **Isi semua 50 rekod lesen NPRA** dengan butiran produk lengkap (nama produk, bentuk dos, teks petunjuk yang diluluskan) untuk memungkinkan ringkasan pasaran Malaysia yang betul.
- Setelah semua jurang diselesaikan, **jana semula laporan ini** menggunakan Pakej Bukti yang selesai.

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

