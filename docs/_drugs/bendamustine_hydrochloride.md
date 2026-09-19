---
layout: default
title: Bendamustine Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 125
evidence_level: L5
indication_count: 0
---

# Bendamustine Hydrochloride
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

# Bendamustine Hydrochloride: Laporan Penilaian Ubat Repurposing

## Ringkasan Satu Ayat

Bendamustine hydrochloride ialah agen antineoplastik pengalkilan yang digunakan terutamanya untuk rawatan leukaemia limfositik kronik (CLL) dan limfoma bukan-Hodgkin sel B tak beragresif. Model TxGNN pada masa ini **tiada ramalan indikasi baru** untuk ubat ini. Pakej bukti mengandungi **jurang data yang ketara** — termasuk ID DrugBank yang hilang, MOA, butiran lesen, dan maklumat keselamatan — yang mesti diselesaikan sebelum sebarang penilaian repurposing dapat diteruskan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asal | Tidak tersedia dalam pakej bukti (diketahui: CLL, NHL tak beragresif) |
| Indikasi Baru Diramal | Tiada — tiada ramalan TxGNN dijana |
| Skor Ramalan TxGNN | N/A |
| Tahap Bukti | L5 — Ramalan model tidak tersedia |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 10 |
| Keputusan Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

> Pada masa ini, tiada ramalan TxGNN telah dijana untuk Bendamustine Hydrochloride, jadi penilaian kemungkinan mekanistik tidak dapat dilakukan.

Berdasarkan pengetahuan farmakologi umum, bendamustine ialah agen pengalkilan bifungsional unik yang menggabungkan sifat-sifat kedua-dua agen pengalkilan (kumpulan nitrogen mustard) dan analog purin (gelang benzimidazol). Mekanisme dwi ini menyebabkan sambung silang DNA, pecahan helai, dan gangguan titik pemeriksaan mitotik, yang membawa kepada apoptosis dalam sel yang cepat membelah. Ia telah menunjukkan keberkesanan klinikal dalam CLL, limfoma bukan-Hodgkin sel B tak beragresif, dan multiple myeloma.

Ketiadaan ramalan TxGNN mungkin disebabkan oleh pemetaan ID DrugBank yang hilang (pada masa ini `null`), yang akan menghalang ubat daripada dipadankan dalam graf pengetahuan. **Menyelesaikan pemetaan DrugBank adalah prasyarat** untuk menjana calon repurposing.

---

## Maklumat Pasaran Malaysia

Pakej bukti melaporkan **10 lesen terdaftar** dengan status pasaran "Dipasarkan" (Dipasarkan), namun semua medan butiran lesen adalah kosong. Data peringkat lesen perlu dikumpul semula.

| Item | Keadaan |
|------|--------|
| Jumlah Lesen | 10 |
| Butiran Lesen Tersedia | ✗ Tidak tersedia — semua medan kosong |
| Tindakan Diperlukan | Pertanyaan semula pangkalan data NPRA untuk rekod lesen lengkap |

---

## Sitotoksisiti

Bendamustine hydrochloride ialah agen antineoplastik sitotoksik yang diketahui (kelas agen pengalkilan). Penilaian berikut adalah berdasarkan pengetahuan farmakologi yang telah ditetapkan, kerana pakej bukti tidak mengandungi data toksisiti DrugBank.

| Item | Kandungan |
|------|----------|
| Pengelasan Sitotoksisiti | Sitotoksik konvensional (Agen pengalkilan bifungsional / Hibrid analog purin) |
| Risiko Penindasan Sumsum | **Tinggi** — neutropenia, trombositopenia, dan anemia adalah toksisiti yang mengehadkan dosis |
| Pengelasan Emetogenisiti | Rendah hingga sederhana |
| Item Pemantauan | CBC dengan pembezaan (sebelum setiap kitaran), fungsi hati (ALT, AST, bilirubin), fungsi buah pinggang (kreatinin, eGFR), tanda-tanda jangkitan |
| Perlindungan Pengendalian | Mesti mematuhi peraturan pengendalian ubat sitotoksik (pemindahan sistem tertutup, PPE, kit tumpahan) |

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.
>
> **Nota:** Pakej bukti tidak mengandungi data keselamatan yang boleh digunakan — amaran utama, kontraindikasi, dan interaksi ubat–ubat semuanya ditandai sebagai jurang data. Ini diklasifikasikan sebagai jurang keterukan **Halangan** (DG001) yang menghalang masuk ke penilaian keselamatan Peringkat 1.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Tiada ramalan repurposing TxGNN wujud untuk Bendamustine Hydrochloride, dan pelbagai jurang data kritikal (ID DrugBank, MOA, profil keselamatan, butiran lesen) menghalang sebarang penilaian bermakna. Ubat ini tidak dapat meneruskan penilaian repurposing dalam keadaan semasanya.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Pemetaan ID DrugBank** (DG002 — Keterukan Tinggi): Pertanyaan API DrugBank untuk "Bendamustine" untuk mendapatkan ID DrugBank (dijangka: DB06769) dan integrasikannya ke dalam graf pengetahuan untuk ramalan TxGNN
2. **Data mekanisme tindakan** (DG002 — Keterukan Tinggi): Ambil maklumat MOA terperinci, sasaran, dan laluan daripada DrugBank
3. **Butiran lesen NPRA**: Pertanyaan semula pangkalan data NPRA untuk mengisi semua 10 rekod lesen dengan nama produk, bentuk dos, pengilang, dan indikasi yang diluluskan
4. **Profil keselamatan** (DG001 — Halangan): Muat turun dan huraikan PDF sisipan pakej daripada laman web pihak berkuasa kawal selia untuk mengeluarkan amaran utama, kontraindikasi, dan interaksi ubat
5. **Lari semula ramalan TxGNN**: Setelah ID DrugBank dipetakan, laksanakan semula saluran ramalan graf pengetahuan dan pembelajaran mendalam untuk menjana calon repurposing

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Sebarang calon repurposing ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

