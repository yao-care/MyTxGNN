---
layout: default
title: Cinchocaine
parent: Low Evidence (L4-L5)
nav_order: 217
evidence_level: L5
indication_count: 7
---

# Cinchocaine
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **7** 
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

# Cinchocaine: Daripada Anestesi Lokal kepada Bronkitis

## Ringkasan Satu Ayat

Cinchocaine (DrugBank DB00527) adalah anestesi lokal jenis amida yang telah ditubuhkan untuk pelepasan rasa sakit topikal/mukosal.
Model TxGNN meramalkan ia mungkin berkesan untuk **Bronkitis**, dengan skor ramalan **99.77%**,
tetapi pada masa kini **tiada percubaan klinikal dan tiada penerbitan** menyokong arah ini — ia adalah hipotesis peringkat model tulen.

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Anestesi lokal (penggunaan topikal/mukosal) — teks petunjuk label NPRA khusus tidak tersedia dalam data sumber |
| Petunjuk Baru yang Diramalkan | Bronkitis |
| Skor Ramalan TxGNN | 99.77% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | Tahan |

## Mengapa Ramalan Ini Adalah Munasabah?

Pada masa kini, data mekanisme tindakan terperinci tidak tersedia (ditandakan sebagai jurang data keterukan Tinggi). Berdasarkan farmakologi yang diketahui, Cinchocaine adalah anestesi lokal kelas amida yang menyekat saluran natrium bergantung-voltan untuk menghalang penghantaran saraf, dan ia juga mempunyai kesan analgesik mukosal topikal ringan dan penstabilan membran (kesan antiradang yang lemah). Penggunaan klinikal yang telah ditubuhkan adalah pelepasan rasa sakit lokal/topikal.

Sebaliknya, bronkitis terutamanya adalah keadaan jalan udara yang bersifat radang/infektif. Pakej bukti TxGNN sendiri yang memberi alasan mekanis untuk calon ini secara eksplisit mencirikan pautan sebagai lemah: cinchocaine tidak mempunyai laluan antiradang atau antimikrob yang ditubuhkan yang relevan dengan bronkitis, dan sebarang sambungan hanya akan terbatas kepada kesan antitussif/analgesik bukan khusus pada mukosa jalan udara dan bukannya mekanisme yang menangani patologi asas.

Memandangkan ketiadaan laluan mekanis langsung yang munasabah dan ketiadaan sepenuhnya bukti klinikal atau kesusasteraan yang menyokong, calon ini harus dianggap sebagai output model peringkat awal dan penerokaan sahaja dan bukannya hipotesis yang berdasarkan farmakologi dengan baik.

## Bukti Percubaan Klinikal

Pada masa kini tiada percubaan klinikal berkaitan yang didaftarkan.

## Bukti Kesusasteraan

Pada masa kini tiada kesusasteraan berkaitan yang tersedia.

## Maklumat Pasaran Malaysia

Rekod NPRA mengesahkan Cinchocaine dipasarkan di Malaysia dengan 1 pendaftaran aktif, tetapi data sumber tidak mengandungi nombor lesen yang dipenuhi, nama produk, bentuk dos, atau medan teks petunjuk yang diluluskan untuk entri ini — butir-butir ini perlu diambil terus daripada daftar produk NPRA sebelum penilaian lanjutan.

## Pertimbangan Keselamatan

Sila rujuk sisipan paket untuk maklumat keselamatan.

*(Nota: Pengambilan label NPRA — amaran dan kontraindikasi — ditandakan sebagai jurang data Menghalang; ini menghalang selesainya penilaian keselamatan awal S1 untuk calon ini.)*

## Calon Lain yang Diramalkan Model (Ubat Sama)

TxGNN juga menandakan enam petunjuk keyakinan rendah tambahan untuk Cinchocaine, semua pada tahap bukti L5 tanpa ujian atau kesusasteraan yang menyokong, dan semua disyorkan Tahan:

| Pangkat | Petunjuk yang Diramalkan | Skor | Kebolehpercayaan Mekanis |
|--------|----------------------|-------|---------------------------|
| 2 | Acrodermatitis chronica atrophicans | 99.76% | Tiada — jangkitan Borrelia kronik; cinchocaine tidak mempunyai aktiviti antimikrob |
| 3 | Dermatomyositis neonat | 99.72% | Tiada — patologi autoimmun/pelengkap; tiada tindakan imunomodulatif |
| 4 | Penyakit paru interstisial sekunder kanak-kanak dengan penyakit jaringan ikat | 99.72% | Tiada — patologi paru berserat/autoimmun yang tidak berkaitan dengan penyekat saluran natrium |
| 5 | Keloid jerawat | 99.67% | Lemah — kemungkinan analgesia simptomatik sahaja, tiada kesan antifibrosa/antimikrob |
| 6 | Hydroa vacciniforme, keluarga | 99.66% | Tiada — fotosensitiviti/limfoproliferasi yang didorong oleh EBV |
| 7 | Dermatomyositis amyopathic | 99.65% | Tiada — patologi autoimmun yang didorong oleh interferon jenis I |

Corak ini (skor TxGNN yang sama tinggi dengan rasional mekanis lemah yang sama-sama seragam dan bukti dunia nyata sifar) mencadangkan ini adalah persatuan peringkat model yang luas dan bukannya isyarat penentuan ubat khusus, dan memerlukan berhati-hati sebelum pelaburan lanjutan dalam calon tunggal.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Rasional:**
Ramalan Bronkitis bergantung semata-mata pada skor model TxGNN (L5) tanpa percubaan klinikal, tanpa kesusasteraan, dan rasional mekanis yang jelas lemah. Sebagai tambahan, jurang data Menghalang (amaran/kontraindikasi label NPRA yang hilang) menghalang penilaian keselamatan awal sahaja, dan data MOA belum disahkan secara rasmi.

**Untuk meneruskan, perkara berikut diperlukan:**
- Ambil label produk NPRA (amaran, kontraindikasi) untuk produk Cinchocaine yang didaftarkan Malaysia — menyelesaikan DG001 (Menghalang)
- Sahkan mekanisme tindakan melalui rujukan DrugBank/farmakologi — menyelesaikan DG002 (Tinggi)
- Selesaikan butir-butir pendaftaran Malaysia yang hilang (nombor lesen, nama produk, bentuk dos, teks petunjuk yang diluluskan)
- Carian kesusasteraan/praklinikal bebas khusus untuk cinchocaine (atau analog kelas) dalam radang jalan udara, untuk menguji hipotesis mekanis sebelum komitmen kepada penilaian peringkat percubaan

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

