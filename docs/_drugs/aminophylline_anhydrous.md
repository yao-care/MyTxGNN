---
layout: default
title: Aminophylline Anhydrous
parent: Low Evidence (L4-L5)
nav_order: 54
evidence_level: L5
indication_count: 0
---

# Aminophylline Anhydrous
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

# Aminophylline Anhydrous: Bronkodilator dengan Data Ubah Tujuan Penggunaan Tidak Mencukupi

## Ringkasan Satu Ayat

Aminophylline Anhydrous adalah bronkodilator metilksantin yang secara klasik digunakan untuk asma bronkial dan penyakit paru obstruktif kronik (PPOK).
Tiada ramalan ubah tujuan TxGNN yang tersedia untuk ubat ini pada masa ini — medan `predicted_indications` kosong — bermakna **tiada sasaran indikasi baru** dan **tiada bukti sokongan** boleh dilaporkan pada masa ini.
Laporan ini mendokumentasikan status data semasa dan menggariskan langkah pemulihan sebelum penilaian ubah tujuan penggunaan penuh boleh diteruskan.

---

## Gambaran Pantas

| Item | Kandungan |
|------|----------|
| Indikasi Asli | Asma bronkial / PPOK / Bronkospasme akut (berdasarkan farmakologi yang diketahui; teks kemasukan pakej tidak diambil) |
| Indikasi Baru yang Diramalkan | — (Tiada ramalan TxGNN tersedia) |
| Skor Ramalan TxGNN | — |
| Tahap Bukti | L5 (Ramalan model belum dijana) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Tiada ramalan ubah tujuan TxGNN tersedia untuk calon ini pada masa laporan dijana (`predicted_indications: []`). Oleh itu, pautan mekanik kepada mana-mana indikasi baru tidak dapat dinilai.

Daripada farmakologi yang ditubuhkan, Aminophylline adalah kompleks 2:1 teofolin dan etilendiamin. Teofolin bertindak terutamanya sebagai **penghambat fosfodiesterase (PDE) bukan selektif**, meningkatkan tahap cAMP dan cGMP intrasel, yang membawa kepada relaksasi otot halus bronkial. Ia juga bertindak sebagai **antagonis reseptor adenosina** (A1, A2A), yang menyumbang kepada kesan sampingan termasuk kronotropi positif, diuresis ringan, dan rangsangan pernafasan pusat.

Mekanisme pleiotropik ini — terutamanya antagonisme adenosina dan kesan anti-radang melalui penghambatan PDE4 — telah menjana minat dalam pengubahan semula ksantin menuju kepada keadaan neurologi, kardiologi, dan radang. Bagaimanapun, tanpa skor TxGNN atau bukti sokongan, tiada calon ubah tujuan penggunaan khusus dapat disyorkan pada peringkat ini.

---

## Bukti Percubaan Klinikal

Pada masa ini tiada percubaan klinikal yang berhubung didaftarkan untuk indikasi baru yang diramalkan (data ramalan tidak tersedia).

---

## Bukti Kesusasteraan

Pada masa ini tiada kesusasteraan yang berhubung tersedia untuk indikasi baru yang diramalkan (data ramalan tidak tersedia).

---

## Maklumat Pasaran Malaysia

Pakej Bukti melaporkan **1 pendaftaran aktif** di Malaysia, tetapi semua medan butiran lesen (nombor kebenaran, nama produk, bentuk dos, pengilang, teks indikasi yang diluluskan) dikembalikan sebagai rentetan kosong. Yang berikut adalah pemegang tempat sementara tertunda pemulihan data:

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------|----------|----------|----------|
| *(Tertunda pemulihan)* | Aminophylline Anhydrous | *(Tertunda)* | *(Tertunda — muat turun kemasukan pakej daripada portal NPRA)* |

> **Tindakan diperlukan**: Soal pangkalan data produk NPRA secara langsung untuk produk tunggal yang terdaftar untuk mengisi medan ini.

---

## Pertimbangan Keselamatan

Sila rujuk kemasukan pakej untuk maklumat keselamatan.

> Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat) dikembalikan sebagai `[Data Gap]` atau kosong. Kebimbangan keselamatan yang diketahui berikut didokumentasikan dalam rujukan antarabangsa dan harus disahkan terhadap kemasukan pakej yang diluluskan Malaysia sebelum penggunaan klinikal:
>
> - **Indeks terapeutik sempit**: Tahap serum teofolin mesti dipantau (sasaran 10–20 µg/mL; ketoksikan di atas 20 µg/mL).
> - **Kardiovaskular**: Risiko takikardia, aritmia, dan hipotensi — gunakan dengan berhati-hati dalam penyakit jantung.
> - **CNS**: Kejang-kejang dilaporkan pada kepekatan toksik.
> - **Interaksi ubat**: Pelbagai interaksi penting (cth., dengan siprofloksasin, simetdin, rifampisin, feniton) yang mengubah penjelasan teofolin; modul DDI mengembalikan 0 hasil dan memerlukan soal semula.
>
> Ini adalah pemerhatian rujukan sahaja dan tidak menggantikan label setempat yang diluluskan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Paip ramalan TxGNN belum mengembalikan mana-mana calon ubah tujuan penggunaan untuk Aminophylline Anhydrous, menjadikan mustahil untuk mengenalpasti indikasi baru, menilai kebolehmangsaan mekanik, atau menilai bukti sokongan. Profil keselamatan tidak dapat disemak secara formal sehingga kemasukan pakej diambil.

**Untuk meneruskan, yang berikut diperlukan:**

- [ ] **Jalankan semula ramalan TxGNN** — Sahkan bahawa `AMINOPHYLLINE ANHYDROUS` dipetakan dengan betul ke entri DrugBank-nya (teofolin: DB00277; aminofolin: DB01223) dan jalankan semula paip ramalan KG dan DL untuk mengisi `predicted_indications`.
- [ ] **Selesaikan ID DrugBank** — `drugbank_id` adalah `null`; pautan kepada DrugBank DB01223 (aminofolin) atau DB00277 (teofolin) untuk membuka data MOA, ketoksikan, dan DDI.
- [ ] **Ambil kemasukan pakej NPRA** — Muat turun dan huraikan PDF daripada portal NPRA untuk mengisi `approved_indication_text`, amaran, dan kontraindikasi (Jurang Data DG001, DG002).
- [ ] **Isi butiran lesen** — Rekod pendaftaran tunggal mempunyai semua medan kosong; ambil nama produk, bentuk dos, dan pengilang daripada pangkalan data NPRA.
- [ ] **Soal semula modul DDI** — Setelah ID DrugBank diselesaikan, jalankan semula soalan interaksi ubat-ubatan untuk menggantikan tatasusunan `interactions` kosong.
- [ ] **Terbitkan semula laporan ini** selepas jurang data di atas diselesaikan untuk membolehkan penilaian gred bukti L1–L5 penuh dan keputusan Lanjut / Teruskan dengan Langkah Pelindung yang substantif.

---

> ⚠️ *Laporan ini adalah untuk rujukan penyelidikan sahaja dan tidak merupakan nasihat perubatan. Mana-mana calon ubah tujuan penggunaan ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

