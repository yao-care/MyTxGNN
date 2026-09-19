---
layout: default
title: Zanamivir
parent: Low Evidence (L4-L5)
nav_order: 693
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **2** 
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

# Zanamivir: Daripada Influenza kepada Pyelonephritis

## Ringkasan Satu Ayat

> Zanamivir ialah penghambat neuraminidase yang paket bukti tidak merekodkan petunjuk asal yang disahkan atau teks indikasi yang diluluskan, tetapi mekanismenya (menyekat pelepasan virus influenza melalui perencatan glikoprotein permukaan virus) didokumentasikan dengan baik dalam rasional yang disertakan.
> Model TxGNN meramalkan ia mungkin berkesan untuk **Pyelonephritis**, jangkitan saluran kencing atas yang berbakteri,
> tetapi ramalan ini disokong oleh **0 percubaan klinikal** dan **0 penerbitan**, dan paket bukti itu sendiri menandai pautan mekanistik sebagai tidak munasabah secara biologi.

---

## Gambaran Pantas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak direkodkan dalam teks lesen TFDA atau medan `original_indications`; rasional paket bukti mengenal pasti zanamivir sebagai penghambat neuraminidase anti-influenza |
| Indikasi Baru Diramalkan | Pyelonephritis |
| Skor Ramalan TxGNN | 99.84% |
| Tahap Bukti | L5 (ramalan model sahaja, tiada percubaan klinikal atau penerbitan sokongan) |
| Status Pasaran Malaysia | ✓ Berada di Pasaran |
| Bilangan Pendaftaran | 1 |
| Keputusan Disyorkan | **Tunggu** |

---

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan terperinci untuk zanamivir ditandakan sebagai jurang data (`original_moa: [Data Gap]`), tetapi rasional paket bukti itu sendiri menerangkannya sebagai **penghambat neuraminidase** yang bertindak eksklusif pada glikoprotein permukaan virus influenza untuk menyekat pelepasan zarah virus — mekanisme semata-mata antivirus.

Pyelonephritis, sebaliknya, ialah jangkitan saluran kencing atas yang **berbakteri** (paling biasa disebabkan oleh *E. coli*), didorong oleh keadhesifan bakterial, pencerobohan, dan jalur keradangan sepenuhnya tidak berkaitan dengan aktiviti neuraminidase virus influenza. Tiada tindak balas silang yang diketahui, sasaran bersama, atau laluan bertindih antara perencatan neuraminidase virus dan aktiviti antibakteria.

Paket bukti secara eksplisit menilai pautan ini sebagai **bukan sokongan mekanistik**: skor kesamaan TxGNN yang tinggi dikaitkan dengan kedekatan pembenaman graf pengetahuan dan bukannya mana-mana hubungan farmakologi atau klinikal yang sebenar. Ini disokong oleh ramalan kedua yang berpangkat lebih rendah dalam paket yang sama (gangguan metabolisme tirosin, skor 99.02%), di mana satu-satunya kesusasteraan yang dikembalikan membincangkan mutasi rintangan NA influenza (H274Y/N294S) — tidak relevan secara topik dengan gangguan metabolisme asid amino keturunan, sekali lagi menunjukkan artifak padanan kata kunci/entiti dan bukannya isyarat repurposing yang tulen. Corak ini di seluruh kedua-dua ramalan teratas mencadangkan larian semasa mempunyai isu positif palsu sistemik untuk ubat ini dan bukannya anomali terpencil.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal yang berkaitan didaftarkan.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berkaitan tersedia.

---

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |
|---------|------|------|-----------|
| Tidak dinyatakan dalam paket bukti | Tidak dinyatakan dalam paket bukti | Tidak dinyatakan dalam paket bukti | Tidak dinyatakan dalam paket bukti |

*Nota: `total_licenses` melaporkan 1 pendaftaran, tetapi rekod lesen itu sendiri tidak mengandungi medan yang dipenuhi (nombor, nama produk, bentuk dos, atau teks indikasi) dalam paket bukti ini.*

---

## Pertimbangan Keselamatan

Sila rujuk sisipan peket untuk maklumat keselamatan.

*Nota: Paket bukti menandakan amaran label TFDA/keterangan kontra (DG001) sebagai jurang data **Menghalang** — ini sahaja menghalang calon daripada memasuki saringan keselamatan awal (S1), bebas daripada bukti keberkesanan yang dibincangkan di atas.*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Rasional:**
Indikasi yang diramalkan (pyelonephritis) tidak mempunyai pautan mekanistik yang munasabah secara biologi kepada aktiviti antivirus zanamivir yang diketahui (perencatan neuraminidase), tiada percubaan klinikal sokongan, dan tiada kesusasteraan sokongan — paket bukti itu sendiri mengkelaskan ini sebagai Tahap Bukti L5 dengan cadangan pemarkahan "Tunggu". Indikasi yang diramalkan kedua dalam paket yang sama menunjukkan corak yang sama (skor tinggi, kesusasteraan tidak relevan), mencadangkan isyarat asas ialah artifak pembenaman graf dan bukannya calon repurposing yang tulen.

**Untuk diteruskan, yang berikut diperlukan:**
- Selesaikan DG001 (Menghalang): ambil dan huraikan sisipan peket TFDA untuk amaran/keterangan kontra sebelum sebarang saringan keselamatan boleh bermula
- Selesaikan DG002 (Tinggi): sahkan mekanisme tindakan zanamivir melalui API DrugBank untuk mendokumentasikan secara formal ketidakpadanan mekanistik
- Jika calon ini hendak diteruskan lagi, pengesahan bebas bagi rasional biologi yang munasabah (cth., kesan sambilan antibakteria atau imunomodulatif) diperlukan, kerana tiada yang wujud pada masa ini dalam paket bukti

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

