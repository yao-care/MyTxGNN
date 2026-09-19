---
layout: default
title: Pretomanid
parent: Low Evidence (L4-L5)
nav_order: 571
evidence_level: L5
indication_count: 5
---

# Pretomanid
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **5** 
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

# Pretomanid: Daripada Tuberkulosis Rintang Ubat Luas kepada Kandidiasis

## Ringkasan Satu Ayat

> Pretomanid ialah antimikobakteri nitroimidazooksazin yang diluluskan sebagai bahagian daripada rejimen BPaL (Bedaquiline-Pretomanid-Linezolid) untuk tuberkulosis paru-paru rintang ubat luas (XDR) dan tuberkulosis rintang ubat berbilang (MDR) yang tidak bertoleransi/tidak responsif terhadap rawatan. Model TxGNN meramalkan ia mungkin berkesan untuk **Kandidiasis**, tetapi arah ini pada masa ini disokong oleh **0 ujian klinikal** dan **0 penerbitan**, dan mekanisme ubat yang diketahui (perencatan dinding sel mikobakteri/sintesis asid mikolik dan pengaktifan bergantung hipoksia) tidak mempunyai kaitan yang ditubuhkan dengan patogen kulat — ramalan harus diperlakukan sebagai artifak graf pengetahuan yang berkemungkinan besar daripada petunjuk penggunaan semula yang sebenar.

*(Nota: `taiwan_regulatory.licenses[0].approved_indication_text` dalam pakej bukti adalah kosong; petunjuk asal di atas disimpulkan daripada literatur dalam pakej bukti yang sama, cth PMID 41263908.)*

---

## Gambaran Umum Pantas

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tuberkulosis paru-paru rintang ubat luas (XDR-TB), sebagai bahagian daripada rejimen BPaL |
| Petunjuk Baru Diramalkan | Kandidiasis |
| Skor Ramalan TxGNN | 99.69% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | Tahan |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan yang terperinci (`original_moa`) tidak tersedia untuk pakej bukti ini. Berdasarkan maklumat kontekstual yang ditangkap di tempat lain dalam pakej, aktiviti antimikobakteri pretomanid yang diketahui bergantung pada dua laluan yang khusus untuk mikobakteri: perencatan biosintesis asid mikolik (dinding sel), dan mekanisme pengaktifan nitro-imidazol yang bergantung pada enzim khusus mikobakteri yang aktif dalam keadaan hipoksia.

Kandidiasis disebabkan oleh spesies *Candida*, yang merupakan kulat dengan komposisi dinding sel yang secara asasnya berbeza (kitin/glukan, bukan asid mikolik) dan tiada pergantungan yang diketahui pada laluan pengaktifan hipoksia yang dimanfaatkan pretomanid. Tiada persamaan struktur, taksonomi, atau farmakoloji antara petunjuk asal (jangkitan mikobakteri) dan petunjuk diramalkan (jangkitan kulat) yang akan menyokong hubungan mekanistik yang munasabah.

Memandangkan ketiadaan sebarang ujian klinikal atau literatur yang menyokong, dan kekurangan nisbah mekanistik yang koheren, skor TxGNN yang tinggi kemungkinan besar mencerminkan sambungan graf pengetahuan tidak langsung (cth, morbiditi bersama yang dikongsi atau nod preskripsi bersama dengan anti-infektif lain) daripada isyarat farmakoloji yang sebenar.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal berkaitan yang didaftarkan.

---

## Bukti Literatur

Pada masa ini tiada literatur berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

Status pasaran Malaysia menunjukkan produk **dipasarkan** dengan **1** lesen berdaftar. Walau bagaimanapun, nombor pendaftaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan untuk lesen ini tidak dipenuhi dalam data sumber — tiada maklumat lanjut boleh dilaporkan tanpa mengakses rekod NPRA utama.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan. Amaran utama, kontraindikasi, dan semakan formal interaksi ubat (DDI) tidak tersedia dalam set data semasa (pertanyaan DDI mengembalikan hasil kosong).

**Isyarat yang ditandai tambahan (bukan daripada medan keselamatan formal, tetapi dicatat di tempat lain dalam pakej bukti ini):** nisbah untuk dua calon yang diramalkan TxGNN lain (penyakit arteri koroner, iskemia miokardial) merujuk kepada risiko pemanjangan QT yang diketahui untuk pretomanid. Ini harus disahkan terhadap label rasmi sebelum sebarang pertimbangan klinikal selanjutnya.

---

## Petunjuk Lain yang Diramalkan TxGNN (Tidak Dinilai Lanjut Di Atas)

Pakej bukti ini adalah tarikan berbilang calon (`TW-DB05154-multi`) yang meliputi 5 petunjuk diramalkan, semuanya pada masa ini pada **Tahan**:

| Kedudukan | Penyakit | Skor | Tahap Bukti | Nota |
|------|---------|-------|------|------|
| 2 | Kusta | 99.27% | L4 | Mempunyai 3 ujian klinikal + 9 penerbitan, tetapi PMID 17005816 secara langsung menunjukkan *M. leprae* **secara semula jadi rintang** terhadap pretomanid (PA-824) — suatu sanggahan mekanistik, bukan hanya jurang bukti. |
| 3 | Penyakit arteri koroner | 99.25% | L5 | Tiada ujian/literatur; berkonflik dengan risiko pemanjangan QT pretomanid yang diketahui. |
| 4 | Iskemia miokardial | 99.17% | L5 | Rasional yang sama seperti di atas. |
| 5 | Arteri koroner sinistra anomali daripada arteri pulmonari (ALCAPA) | 99.08% | L5 | Keabnormalan kongenital struktur yang memerlukan pembedahan; tiada mekanisme yang boleh dirawat ubat. |

Tiada satu pun daripada lima calon dalam pakej ini pada masa ini menjelaskan ujian saringan mekanistik awal.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Ramalan berlatar tertinggi (kandidiasis) tiada bukti ujian klinikal atau literatur yang menyokong dan tiada asas mekanistik yang munasabah. Di seluruh set calon penuh dalam pakej ini, calon yang paling terbukti (kusta) secara langsung bertentangan dengan kajian kerentanan antimikrob yang berdedikasi, dan calon yang tinggal berkonflik dengan isyarat keselamatan jantung yang diketahui atau tidak boleh dirawat secara farmakoloji. Ini adalah kes di mana skor TxGNN yang tinggi tidak disokong oleh mekanisme atau bukti.

**Untuk meneruskan, perkara berikut diperlukan:**
- Sisipan pakej TFDA/NPRA (amaran, kontraindikasi) — pada masa ini jurang data menyekat (DG001)
- Mekanisme tindakan yang disahkan (MOA) daripada DrugBank atau literatur utama — pada masa ini jurang data keterukan tinggi (DG002)
- Jika sebarang calon diteruskan lebih jauh, carian literatur/ujian tertumpu yang khusus untuk petunjuk itu, memandangkan pertanyaan automatik untuk kandidiasis, penyakit arteri koroner, iskemia miokardial, dan ALCAPA mengembalikan hasil kosong
- Pengesahan isyarat pemanjangan QT yang dirujuk dalam teks rasional terhadap label rasmi sebelum mempertimbangkan sebarang petunjuk berkaitan jantung

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

