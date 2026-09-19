---
layout: default
title: Adapalene
parent: Low Evidence (L4-L5)
nav_order: 28
evidence_level: L5
indication_count: 1
---

# Adapalene
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **1** 
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

# Adapalene: Daripada Jerawat Vulgaris kepada Zink, Plasma Meningkat

## Ringkasan Satu Ayat

Adapalene ialah retinoid sintetik generasi ketiga, yang pada asalnya telah diluluskan untuk rawatan topikal jerawat vulgaris. Model TxGNN meramalkan ia mungkin mempunyai relevansi kepada **Zink, Plasma Meningkat (hyperзincaemia)**, dengan skor ramalan model yang tinggi iaitu **99.51%**; bagaimanapun, **tiada percubaan klinikal dan tiada kesusastraan yang diterbitkan** yang pada masa ini menyokong arah ini — menjadikan ini sinyal pengiraan murni yang memerlukan penyiasatan lanjutan yang besar.

---

## Gambaran Keseluruhan Pantas

| Perkara | Kandungan |
|---------|----------|
| Indikasi Asal | Jerawat vulgaris (retinoid topikal) |
| Indikasi Baru yang Diramalkan | Zink, Plasma Meningkat |
| Skor Ramalan TxGNN | 99.51% |
| Tahap Bukti | L5 |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 5 |
| Keputusan Disyorkan | **Tungu** |

---

## Mengapa Ramalan Ini Munasabah?

Adapalene adalah retinoid bercetusan asid naftoik generasi ketiga yang terikat secara selektif kepada reseptor asid retinoid RAR-β dan RAR-γ. Dalam rawatan jerawat, ia menghasilkan kesannya dengan menormalkan pembezaan keratinosit, mengurangkan hiperkeratinisasi folikel, dan menindas mediator inflamasi. Adalah penting, retinoid dan metabolisme zink diketahui berinteraksi pada tahap biologi: zink adalah kofaktor penting untuk sintesis protein pengikatan retinol (RBP), yang bertanggungjawab untuk mengangkut vitamin A dalam darah; sebaliknya, reseptor asid retinoid (RAR) boleh mengawal ungkapan gen keluarga pengangkut zink (keluarga ZnT/ZIP), secara teori mempengaruhi homeostasis zink sistemik.

Skor ramalan TxGNN sebesar 0.995 sangat tinggi. Bagaimanapun, ini kemungkinan besar mencerminkan kedekatan topologi nod "retinoid" dan "metabolisme zink" dalam graf pengetahuan, dan bukannya sinyal terapeutik yang benar. Graf pengetahuan mengkodkan persatuan biologi yang diketahui — dalam kes ini, paksi retinol-zink yang terdokumentasikan dengan baik — yang ditafsirkan oleh model sebagai pautan terapeutik yang berpotensi. Ini adalah batasan yang diketahui bagi ramalan berasaskan graf: kesebelahan mekanik tidak sama dengan keberkesanan terapeutik.

Pada masa ini, data mekanisme tindakan terperinci untuk adapalene tidak tersedia dalam Pakej Bukti ini. Berdasarkan farmakologi yang diketahui, adapalene adalah agonis RAR-β/γ yang selektif. Sementara pautan mekanik teori kepada homeostasis zink boleh dibina melalui paksi retinoid–RBP–zink, sambungan ini sangat spekulatif dan tidak telah diuji secara klinikal. Tiada bukti pada masa ini menyokong adapalene sebagai rawatan untuk zink plasma yang meningkat.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal berkaitan yang didaftar.

---

## Bukti Kesusastraan

Pada masa ini tiada kesusastraan berkaitan yang tersedia.

---

## Maklumat Pasaran Malaysia

5 pendaftaran produk disahkan melalui NPRA (Badan Kawal Selia Farmaseutikal Kebangsaan Malaysia) setakat 2026-03-27. Bagaimanapun, maklumat terperinci peringkat produk (nombor kebenaran, nama produk, bentuk dos, dan teks petunjuk yang diluluskan) tidak dapat diambil dalam tarikan set data semasa.

> **Nota:** Adapalene telah ditubuhkan secara global sebagai gel/krim topikal (0.1% dan 0.3%) untuk jerawat vulgaris. Produk yang berdaftar di Malaysia dijangka mengikuti profil ini. Sila rujuk pangkalan data Pendaftaran Produk NPRA secara langsung untuk maklumat kebenaran penuh.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Data keselamatan (amaran utama, kontraindikasi, dan interaksi ubat) tidak tersedia dalam Pakej Bukti ini. Memandangkan adapalene adalah retinoid topikal, pengamal perlu sedar tentang tindakan pencegahan kelas retinoid umum, termasuk penghindaran dalam kehamilan (kelas risiko teratogenisiti), sensitiviti kepada cahaya matahari, dan potensi untuk iritasi kulit tempatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tungu**

**Rasional:**
Model TxGNN memberikan adapalene skor ramalan yang sangat tinggi (99.51%) untuk zink plasma yang meningkat; bagaimanapun, ini adalah **penemuan bukti L5** — disokong semata-mata oleh model pengiraan dengan percubaan klinikal penyokong sifar atau kesusastraan yang diterbitkan. Petunjuk yang diramalkan ("zink, plasma meningkat") adalah penemuan makmal dan bukannya entiti penyakit utama, dan tiada jalan perkembangan klinikal yang munasabah pada masa ini wujud untuk aplikasi ini.

**Untuk meneruskan, yang berikut diperlukan:**

- **Pengesahan mekanik**: Kajian pra-klinikal (in vitro / in vivo) yang secara langsung menilai kesan adapalene pada tahap zink plasma atau ungkapan pengangkut zink
- **Pengambilan data keselamatan**: Muat turun dan huraikan PDF sisipan pakej TFDA/NPRA untuk mengisi amaran utama dan kontraindikasi (pada masa ini jurang data yang menghalang)
- **Data MOA**: Pertanyaan API DrugBank untuk profil farmakodinamik dan farmakokinetik penuh (pada masa ini jurang data dengan keparahan tinggi)
- **Penilaian semula penyakit**: Menilai sama ada "zink, plasma meningkat" mewakili keadaan yang boleh diambil tindakan secara klinikal yang boleh diterima untuk campur tangan farmakologi dengan retinoid
- **Semakan pakar**: Berunding dengan pakar farmakologi atau endokrinologi untuk menilai kemungkinan biologi sebelum sebarang pelaburan sumber dalam petunjuk ini

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

