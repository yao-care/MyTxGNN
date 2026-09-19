---
layout: default
title: Vitamin E
parent: Low Evidence (L4-L5)
nav_order: 691
evidence_level: L5
indication_count: 10
---

# Vitamin E
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

# Vitamin E: Dari Suplementasi Vitamin kepada Benign Recurrent Intrahepatic Cholestasis

## Ringkasan Satu Ayat

Vitamin E adalah antioksidan yang larut dalam lemak, secara meluas dipasarkan di Malaysia sebagai suplementasi nutrisi (tiada indikasi penyakit spesifik yang tercatat dalam dataset ini). Model TxGNN meramalkan bahawa ia mungkin berkesan untuk **Benign Recurrent Intrahepatic Cholestasis (BRIC)**, namun ramalan ini pada masa ini disokong oleh **0 percubaan klinikal** dan **0 publikasi** — ia bergantung sepenuhnya kepada kesimpulan daripada graf pengetahuan.

---

## Gambaran Ringkas

| Item | Kandungan |
|------|-----------|
| Indikasi Asal | Tidak dinyatakan dalam dataset (kesemua 5 lesen sampel mempunyai teks indikasi kosong); Vitamin E secara amnya dipasarkan sebagai suplementasi vitamin/antioksidan |
| Indikasi Baru yang Diramalkan | Benign Recurrent Intrahepatic Cholestasis |
| Skor Ramalan TxGNN | 99.99% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan (Marketed) |
| Bilangan Pendaftaran | 245 |
| Keputusan yang Disyorkan | Hold |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, data mekanisme tindakan yang terperinci tidak tersedia (Jurang Data DG002, Keseriusan Tinggi). Berdasarkan farmakoloji yang diketahui, Vitamin E adalah antioksidan yang larut dalam lemak yang memerlukan aliran hempedu normal untuk penyerapan usus.

Pautan mekanistik yang dicadangkan adalah tidak langsung: Benign Recurrent Intrahepatic Cholestasis (BRIC) disebabkan oleh kecacatan keluarga gen yang sama (ATP8B1/ABCB11) yang mendasari spektrum Progressive Familial Intrahepatic Cholestasis yang berkaitan (PFIC). Dalam kedua-dua keadaan, aliran hempedu yang terjejas membawa kepada malabsorpsi vitamin yang larut dalam lemak, menghasilkan kekurangan Vitamin E sekunder — komplikasi yang didokumentasikan dengan baik dalam penyakit hati kolestasi. Graf pengetahuan TxGNN nampaknya telah menghubungkan Vitamin E kepada BRIC melalui hubungan kekurangan/pemulihan ini dan bukannya melalui mekanisme pengubah penyakit.

Secara ketara, indikasi yang hampir berkaitan yang disenaraikan #2 dalam pakej bukti ini — familial intrahepatic cholestasis (PFIC) — disokong oleh 6 percubaan klinikal dan 8 publikasi yang mendokumentasikan kekurangan Vitamin E dan suplementasi dalam penyakit hati kolestasi pediatrik. Ini memberikan kemungkinan biologi yang tidak langsung untuk ramalan BRIC, tetapi tiada kajian telah secara langsung menguji suplementasi Vitamin E sebagai rawatan khusus untuk BRIC.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan yang didaftarkan.

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

Butiran produk peringkat lesen (nombor pendaftaran, nama produk, bentuk dos, teks indikasi) tidak diisi dalam pakej bukti ini. Rekod NPRA menunjukkan 245 jumlah pendaftaran untuk produk Vitamin E di Malaysia, tetapi tiada medan per-produk dikembalikan untuk calon ini.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

*(Catatan: Amaran label TFDA/NPRA dan kontraindikasi untuk produk ini adalah Jurang Data yang Menyekat — DG001 — dan mesti diperolehi sebelum sebarang penilaian keselamatan dapat diteruskan.)*

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold**

**Rasional:**
Ramalan yang disenaraikan teratas (BRIC) mempunyai sokongan percubaan klinikal atau kesusasteraan langsung sifar dan diklasifikasikan sebagai L5 (ramalan model sahaja). Digabungkan dengan jurang data keselamatan yang Menyekat (amaran label/kontraindikasi yang hilang) dan jurang MOA keseriusan Tinggi, terdapat bukti yang tidak mencukupi untuk memajukan calon ini.

**Untuk meneruskan, perkara berikut diperlukan:**
- Amaran sisipan pakej TFDA/NPRA dan kontraindikasi (DG001, Menyekat)
- Data mekanisme tindakan DrugBank (DG002, Tinggi)
- Bukti khusus penyakit untuk BRIC (data sokongan semasa hanya meliputi indikasi kolestasis intrahepati familial/PFIC yang berkaitan, bukan BRIC sendiri)
- Data produk peringkat lesen yang lengkap (nombor pendaftaran, teks indikasi yang diluluskan) untuk 245 pendaftaran Malaysia

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

