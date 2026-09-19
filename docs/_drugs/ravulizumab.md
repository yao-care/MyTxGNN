---
layout: default
title: Ravulizumab
parent: Low Evidence (L4-L5)
nav_order: 587
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: Dari Penyakit Dimediasi Komplemen ke Neutropenia Kongenital Berat (Defisiensi G6PC3)

## Ringkasan Satu Kalimat

Ravulizumab adalah penghambat komplemen C5 terminal jangka panjang, dengan indikasi global yang ditetapkan mencakup penyakit yang terkait dengan komplemen dan mikroangiopati trombotik (PNH, aHUS, gMG, NMOSD). Prediksi teratas model TxGNN adalah **neutropenia kongenital berat resesif autosom akibat defisiensi G6PC3**, tetapi arah ini — bersama dengan semua 9 kandidat lainnya dalam paket bukti ini — memiliki **nol uji klinis dan nol dukungan literatur**, dan rasional yang dihasilkan model secara eksplisit menandainya sebagai artefak pengelompokan grafik yang mungkin daripada tautan mekanis yang sebenarnya.

## Gambaran Umum Cepat

| Item | Konten |
|------|---------|
| Indikasi Asli | Tidak ditangkap dalam penarikan data peraturan Malaysia saat ini; berdasarkan anotasi dalam paket bukti ini, indikasi global Ravulizumab yang diketahui adalah penyakit yang dimediasi komplemen (PNH, aHUS, gMG, NMOSD) |
| Indikasi Baru yang Diprediksi | Neutropenia kongenital berat resesif autosom akibat defisiensi G6PC3 |
| Skor Prediksi TxGNN | 99.96% |
| Tingkat Bukti | L5 |
| Status Pasar Malaysia | ✓ Dipasarkan |
| Jumlah Registrasi | 1 |
| Keputusan yang Disarankan | Tahan |

## Mengapa Prediksi Ini Dapat Diterima?

Data mekanisme aksi terperinci tidak tersedia dalam catatan terstruktur (`original_moa`: Kesenjangan Data). Namun, anotasi yang tertanam di tempat lain dalam paket bukti ini menunjukkan bahwa Ravulizumab adalah penghambat komplemen C5 terminal jangka panjang (kelas mekanis yang sama dengan eculizumab), memblokir pembelahan C5 menjadi C5a/C5b dan mencegah pembentukan kompleks serangan membran (MAC). Indikasi yang ditetapkannya adalah penyakit yang dimediasi komplemen dan mikroangiopati trombotik.

Kandidat peringkat teratas model — neutropenia kongenital akibat defisiensi G6PC3 — tidak memiliki koneksi patofisiologis yang diketahui dengan mekanisme ini: hal ini timbul dari defek glukosa-6-fosfatase yang menyebabkan stres retikulum endoplasma dan pematangan neutrofil yang terganggu, bukan aktivasi komplemen. Rasional paket bukti untuk kandidat ini secara eksplisit menyatakan bahwa skor TxGNN yang tinggi kemungkinan besar didorong oleh pengelompokan node "penyakit genetik hematologis/imun langka" dalam grafik pengetahuan daripada tautan biologis yang sebenarnya. Pola ini berulang di semua 10 kandidat peringkat dalam paket ini (subtipe neutropenia kongenital, gangguan trombosit, anemia megaloblastik, dll.) — setiap rasional secara independen menyimpulkan tidak ada jembatan mekanis yang masuk akal ke penghambatan C5. Satu pengecualian parsial adalah peringkat 3, hyperoxaluria primer, di mana rasional mencatat rute spekulatif dan tidak langsung (nephropati oksalat dapat memicu mikroangiopati trombotik hilir, yang kadang-kadang diobati di luar label dengan penghambat komplemen) — tetapi ini menargetkan komplikasi, bukan defek enzimatik yang mendasari penyakit (AGXT/GRHPR/HOGA1), dan juga tidak memiliki bukti pendukung langsung.

Secara keseluruhan, set kandidat ini terlihat sebagai kasus di mana skor kepercayaan diri TxGNN yang tinggi tidak didukung dengan baik oleh kelayakan mekanis, dan tidak ada yang didukung oleh bukti klinis dunia nyata atau literatur.

## Bukti Uji Klinis

Saat ini tidak ada uji klinis terkait yang terdaftar.

## Bukti Literatur

Saat ini tidak ada literatur terkait yang tersedia.

## Informasi Pasar Malaysia

Catatan NPRA mengkonfirmasi 1 registrasi ada di file dengan status pasar ✓ Dipasarkan. Nomor lisensi, nama produk, bentuk dosis, dan teks indikasi yang disetujui tidak ditangkap dalam penarikan data ini.

## Pertimbangan Keselamatan

Silakan merujuk pada risalah ubat untuk informasi keselamatan.

*(Catatan: `key_warnings` dan `contraindications` ditandai sebagai kesenjangan data yang menghalangi — DG001 — dalam paket bukti ini, yang berarti penyaringan keselamatan S1 formal tidak dapat dilanjutkan sampai risalah ubat TFDA diperoleh.)*

## Kesimpulan dan Langkah Selanjutnya

**Keputusan: Tahan**

**Rasional:**
Semua 10 indikasi yang diprediksi adalah L5 (prediksi model saja) tanpa uji klinis atau literatur pendukung, dan rasional mekanis 9 dari 10 kandidat sendiri secara eksplisit menemukan tidak ada tautan yang masuk akal untuk mekanisme kerja penghambatan C5 Ravulizumab. Dikombinasikan dengan kesenjangan data yang menghalangi pada peringatan keselamatan/kontraindikasi (DG001), saat ini tidak ada dasar untuk memajukan salah satu dari kandidat ini melampaui penyaringan awal.

**Untuk melanjutkan, yang berikut diperlukan:**
- Risalah ubat TFDA (peringatan, kontraindikasi) — menyelesaikan DG001, diperlukan sebelum evaluasi keselamatan S1 apa pun
- Catatan mekanisme kerja DrugBank yang dikonfirmasi — menyelesaikan DG002
- Jika mengejar arah hyperoxaluria primer (peringkat 3) secara khusus: bukti tingkat kasus atau registri pada penggunaan penghambat komplemen dalam TMA yang terkait dengan nephropati oksalat, karena ini saat ini hipotesis komplikasi hilir daripada hipotesis indikasi primer
- Detail lisensi peraturan Malaysia yang lengkap (nama produk, bentuk dosis, teks indikasi yang disetujui) untuk registrasi yang ada

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

