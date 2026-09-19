---
layout: default
title: Pitavastatin Calcium
parent: Low Evidence (L4-L5)
nav_order: 556
evidence_level: L5
indication_count: 0
---

# Pitavastatin Calcium
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

# Pitavastatin Calcium: Penilaian Ubah Tujuan Ubat — Data Tidak Mencukupi untuk Menyelesaikan Ramalan

## Ringkasan Satu Ayat

Pitavastatin Calcium ialah agen penurun lipid kelas statin, yang ditubuhkan secara klinikal untuk pengurusan hiperkolesterolaemia dan disolipidaemia bercampur melalui perencatan HMG-CoA reductase.
Tiada ramalan ubah tujuan TxGNN yang dihasilkan untuk ubat ini dalam pakej bukti semasa, menjadikannya mustahil untuk mengenal pasti atau menilai calon petunjuk baru.
Ketiga-tiga komponen data utama — mekanisme tindakan, pelabelan keselamatan, dan butir pendaftaran NPRA peringkat produk — kekal sebagai jurang data yang tidak diselesaikan; saluran mesti dijalankan semula dengan input lengkap sebelum penilaian penuh dapat dihasilkan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Petunjuk Asal | Hiperkolesterolaemia / Disolipidaemia *(disimpulkan dari kelas ubat; teks yang diluluskan khusus NPRA tidak diambil)* |
| Petunjuk Baru yang Diramalkan | — *(Tiada ramalan TxGNN tersedia dalam pakej bukti ini)* |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | — *(Tiada ramalan untuk dinilai)* |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 3 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada petunjuk yang diramalkan oleh TxGNN dalam pakej bukti semasa (tatasusunan `predicted_indications` kosong). Rasional ubah tujuan berstruktur tidak dapat dibina tanpa penyakit sasaran.

Berdasarkan maklumat yang tersedia umum, Pitavastatin Calcium ialah statin sintetik yang terfluorinasi sepenuhnya yang melakukan perencatan kompetitif 3-hidroksil-3-metilglutaril-koenzim A (HMG-CoA) reductase — enzim pembatas kadar dalam biosintesis kolesterol hepatik. Dengan mengurangkan kolesterol intraselular, ia meningkatkan reseptor LDL, menurunkan LDL-C dan trigliserida yang beredar, dan sederhana meningkatkan HDL-C. Selain kesan lipid, statin sebagai kelas juga menjalankan tindakan pleiotropik termasuk kesan anti-radang, antioksidan, dan imunomodulatori, sifat yang telah mendorong penyelidikan ubah tujuan dalam onkologi, pengurangan risiko kardiovaskular melebihi penurunan lipid, dan penyakit neurodegeneratif.

Walau bagaimanapun, semua perkara di atas adalah pengetahuan kelas umum, bukan bukti yang diambil daripada pakej bukti ini. Medan data mekanisme tindakan formal (`original_moa`) ditanda sebagai jurang data (kesukaran: Tinggi), dan tiada bukti peringkat petunjuk (percubaan klinikal atau literatur) telah diambil. Setelah ramalan TxGNN dan bukti sokongan dimuatkan ke dalam pakej, analisis penjajaran mekanisme-ke-petunjuk yang lengkap dapat dilakukan.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal yang berkaitan didaftarkan — tiada petunjuk yang diramalkan tersedia dalam pakej bukti ini untuk pertanyaan.

---

## Bukti Literatur

Pada masa ini tiada literatur yang berkaitan tersedia — tiada petunjuk yang diramalkan tersedia dalam pakej bukti ini untuk pertanyaan.

---

## Maklumat Pasaran Malaysia

Pakej bukti merekodkan **3 produk yang didaftarkan** di Malaysia, tetapi semua medan butir peringkat produk (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak diisi semasa pengambilan data. Jadual di bawah mencerminkan keadaan data seperti yang diterima.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Petunjuk yang Diluluskan |
|------------------|-------------|-----------|------------------------|
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |
| Tidak diambil | Tidak diambil | Tidak diambil | Tidak diambil |

> **Nota:** Butir pendaftaran produk NPRA harus diambil terus daripada [portal NPRA Quest 3+](https://quest3plus.bpfk.gov.my) atau melalui penghuraian PDF sisipan pakej untuk melengkapkan medan ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Semua medan keselamatan — amaran utama, kontraindikasi, dan interaksi ubat-ubat — ditanda sebagai jurang data dalam pakej bukti ini. Jurang data penyekat (DG001) menunjukkan bahawa PDF sisipan pakej TFDA/NPRA belum dimuat turun dan diuraikan. Ini mesti diselesaikan sebelum sebarang keputusan preskripsi atau ubah tujuan berdasarkan keselamatan dapat dibuat.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Pakej bukti untuk Pitavastatin Calcium tidak mengandungi ramalan ubah tujuan TxGNN dan tiada ketiga-tiga lapisan data kritikal (MOA, pelabelan keselamatan, dan butir produk NPRA); tiada calon ubah tujuan dapat dinilai, dimarkahkan, atau disyorkan pada peringkat ini.

**Untuk meneruskan, perkara berikut diperlukan:**

- **Jalankan semula saluran ramalan TxGNN** dengan Pitavastatin Calcium dipetakan dengan betul kepada ID DrugBank-nya (DB08860) supaya `predicted_indications` diisi dengan penyakit calon, markah, dan bukti sokongan
- **Selesaikan jurang data DrugBank (DG002):** Pertanyaan API DrugBank menggunakan ID DrugBank DB08860 untuk mengambil profil ubat lengkap termasuk farmakoloji, MOA, kategori ubat, dan data ketoksikan
- **Selesaikan jurang data sisipan pakej NPRA/TFDA (DG001):** Muat turun dan uraikan PDF sisipan produk daripada portal NPRA atau laman web TFDA untuk melengkapkan amaran utama, kontraindikasi, teks petunjuk yang diluluskan bagi setiap pendaftaran, dan data interaksi ubat
- **Isikan butir lesen NPRA:** Pertanyaan semula pangkalan data NPRA Quest 3+ untuk mengambil nombor kebenaran, nama produk, bentuk dos, dan pengilang untuk ketiga-tiga produk yang didaftarkan
- **Hasilkan semula pakej bukti** setelah jurang di atas diselesaikan, kemudian hasilkan laporan penilaian penuh dengan petunjuk sasaran yang ditakrifkan, tahap bukti, dan cadangan Go/Proceed/Hold berdasarkan data sebenar

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

