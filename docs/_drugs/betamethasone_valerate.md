---
layout: default
title: Betamethasone Valerate
parent: Low Evidence (L4-L5)
nav_order: 138
evidence_level: L5
indication_count: 0
---

# Betamethasone Valerate
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

# Betamethasone Valerate: Laporan Penilaian Repurposing Ubat

## Ringkasan Satu Ayat

Betamethasone valerate ialah kortikosteroid topikal yang digunakan secara meluas untuk dermatosis inflamasi dan pruritus, kini dipasarkan di Malaysia dengan 23 lesen berdaftar. Model TxGNN **belum menghasilkan sebarang petunjuk indikasi baru** untuk ubat ini pada masa ini, dan jurang data kritikal (DrugBank ID, mekanisme tindakan, perincian label pengawalselia) menghalang penilaian repurposing yang bermakna.

---

## Ikhtisar Cepat

| Perkara | Kandungan |
|------|------|
| Petunjuk Asal | Tidak tersedia (teks indikasi lesen tidak didapati) |
| Petunjuk Baru Yang Diramal | **Tiada** — tiada ramalan TxGNN yang dijana |
| Skor Ramalan TxGNN | T/A |
| Aras Bukti | L5 (tiada ramalan atau kajian sokongan) |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 23 |
| Keputusan yang Disyorkan | **Tunggu** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini **tiada ramalan TxGNN untuk dinilai**. Tatasusunan `predicted_indications` adalah kosong, bermaksud model tidak mengembalikan sebarang calon repurposing untuk betamethasone valerate dalam proses ini.

Berdasarkan pengetahuan yang tersedia di kawasan umum, betamethasone valerate ialah ester glukokortikoid sintetik dengan sifat anti-inflamasi yang kuat, supresi imun, dan antipruritus. Ia bertindak dengan mengikat reseptor glukokortikoid intrasel, menekan transkripsi sitokin pro-inflamasi (cth., IL-1, IL-6, TNF-α) dan menghalang fosfolipase A₂, seterusnya mengurangkan sintesis prostaglandin dan leukotrien. Ia digunakan terutamanya sebagai formulasi topikal untuk keadaan dermatologi seperti eksema, psoriasis, dan dermatitis sentuh.

Bagaimanapun, pakej bukti kekurangan DrugBank ID dan data MOA formal (`[Data Gap]`), yang mengehadkan keupayaan untuk menghubungkan ubat ini secara pengkomputeran kepada sasaran penyakit baru dalam graf pengetahuan TxGNN. **Menyelesaikan pemetaan DrugBank ialah prasyarat** untuk menghasilkan ramalan yang bermakna.

---

## Bukti Ujian Klinikal

Pada masa ini tiada indikasi yang diramal wujud, oleh itu tiada pencarian ujian klinikal dilakukan untuk arah repurposing.

> Pada masa ini tiada ujian klinikal berkaitan berdaftar untuk indikasi yang diramal baru.

---

## Bukti Literatur

> Pada masa ini tiada literatur berkaitan tersedia untuk indikasi yang diramal baru.

---

## Maklumat Pasaran Malaysia

23 lesen berdaftar; bagaimanapun, maklumat lesen terperinci (nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan) tidak tersedia dalam pakej bukti.

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|------|------|------|------|
| *(data tidak disediakan)* | — | — | — |

> **Nota:** Rekod lesen mentah mengembalikan medan kosong. Pertanyaan susulan kepada pangkalan data NPRA diperlukan untuk mengisi jadual ini.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan. Data amaran utama, kontraindikasi, dan interaksi ubat–ubat tidak tersedia dalam pakej bukti ini (ditandai sebagai `[Data Gap]` / `not_found`).

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunggu**

**Rasional:**
Tiada calon repurposing yang dijana oleh TxGNN untuk betamethasone valerate. Berbilang jurang data penyekat — termasuk ketiadaan DrugBank ID, mekanisme tindakan, teks label pengawalselia, dan profil keselamatan — menghalang sebarang penilaian yang bermakna. Ubat tidak boleh meneruskan melalui saluran repurposing sehingga unsur data asas ini diselesaikan.

**Untuk meneruskan, yang berikut diperlukan:**

1. **Selesaikan pemetaan DrugBank** — Pertanyaan DrugBank untuk "betamethasone valerate" (berkemungkinan dipetakan ke **DB00394** untuk betamethasone atau entri spesifik garam) dan kemas kini `drugbank_id` dalam pakej bukti.
2. **Ambil data MOA** — Setelah DrugBank ID disahkan, ekstrak mekanisme tindakan, farmakodinamik, dan maklumat sasaran.
3. **Isi perincian lesen NPRA** — Pertanyaan semula pangkalan data NPRA untuk mendapatkan nombor kebenaran, nama produk, bentuk dos, dan teks indikasi yang diluluskan untuk 23 lesen berdaftar.
4. **Ekstrak maklumat keselamatan** — Muat turun dan parsing sisipan pakej (仿單) PDF untuk mengisi amaran utama, kontraindikasi, dan interaksi ubat.
5. **Jalankan semula ramalan TxGNN** — Dengan DrugBank ID dan profil ubat lengkap, jalankan semula saluran ramalan KG dan DL untuk menentukan sama ada sebarang calon repurposing muncul.

---

*Penafian: Laporan ini hanya untuk tujuan penyelidikan dan tidak merupakan nasihat perubatan. Sebarang calon repurposing ubat memerlukan pengesahan klinikal yang ketat sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

