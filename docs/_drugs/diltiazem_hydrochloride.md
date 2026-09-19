---
layout: default
title: Diltiazem Hydrochloride
parent: Low Evidence (L4-L5)
nav_order: 282
evidence_level: L5
indication_count: 0
---

# Diltiazem Hydrochloride
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

# Diltiazem Hydrochloride: Penilaian Penggunaan Semula Ubat — Data Ramalan Tertangguh

## Ringkasan Satu Ayat

Diltiazem Hydrochloride ialah penyekat saluran kalsium kelas benzothiazepine yang digunakan secara luas untuk hipertensi, angina pektoris, dan aritmia jantung tertentu. Pada masa ini, model TxGNN **tidak mempunyai petunjukan baru yang diramalkan** untuk sebatian ini, dan pakej bukti mengandungi jurang data yang ketara dalam butir kawal selia, maklumat keselamatan, dan mekanisme tindakan, menghalang penilaian penggunaan semula yang bermakna pada masa ini.

---

## Tinjauan Pantas

| Item | Kandungan |
|------|----------|
| Petunjukan Asal | Hipertensi, angina pektoris, aritmia (menurut farmakoloji yang ditetapkan; butir peringkat lesen tidak tersedia dalam pakej ini) |
| Petunjukan Baru Diramalkan | **Tiada** — ramalan TxGNN tidak tersedia |
| Skor Ramalan TxGNN | T/A |
| Aras Bukti | T/A |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 6 |
| Keputusan Yang Disyorkan | **Tunda** |

---

## Mengapa Ramalan Ini Munasabah?

Pada masa ini, tiada petunjukan yang diramalkan TxGNN wujud untuk Diltiazem Hydrochloride dalam pakej bukti ini, jadi analisis kebolehplausibilan mekanis tidak boleh dilakukan.

Untuk rujukan, Diltiazem Hydrochloride ialah penyekat saluran kalsium bukan-dihidropiridin yang dicirikan dengan baik. Ia menghalang kemasukan ion kalsium ekstraselular melalui saluran kalsium jenis L dalam otot licin vaskular dan miosit jantung. Ini menghasilkan vasodilatasi (mengurangkan tekanan darah dan vasospasma koroner) dan melambatkan konduksi atrioventrikel (berguna dalam kawalan kadar takiaritmia supraventrikel). Pakej bukti menyenaraikan mekanisme tindakan sebagai jurang data; walau bagaimanapun, farmakoloji didokumentasikan secara meluas dalam kesusasteraan dan dalam DrugBank (DB00343).

Setelah ramalan TxGNN dihasilkan dan diisi ke dalam pakej bukti ini, kebolehplausibilan mekanis sebarang petunjukan calon harus dinilai terhadap sifat penyekat saluran kalsium, vasodilatasi, dan negatif kronomotropi Diltiazem.

---

## Maklumat Pasaran Malaysia

Pakej bukti merekodkan **6 pendaftaran produk** dengan status pasaran "Dipasarkan." Walau bagaimanapun, semua butir peringkat lesen (nombor kelulusan, nama produk, bentuk dos, dan teks petunjukan yang diluluskan) sedang hilang dari data pada masa ini.

| Item | Status |
|------|--------|
| Jumlah Pendaftaran | 6 |
| Status Pasaran | Dipasarkan |
| Butir Lesen | Tidak tersedia — medan data kosong |

> **Tindakan diperlukan:** Ambil rekod pendaftaran NPRA lengkap untuk Diltiazem Hydrochloride untuk mengisi nombor kelulusan, nama produk, bentuk dos, dan teks petunjukan yang diluluskan.

---

## Pertimbangan Keselamatan

> Sila rujuk sisipan pakej untuk maklumat keselamatan.

Semua medan keselamatan (amaran utama, kontraindikasi, interaksi ubat-ubat) ditandakan sebagai jurang data dalam pakej bukti ini. Log pertanyaan DrugBank menunjukkan pertanyaan yang berjaya (result_count = 1), mencadangkan bahawa data keselamatan mungkin dapat diambil tetapi tidak diintegrasikan ke dalam pakej ini.

**Profil keselamatan yang diketahui (pengetahuan farmakoloji umum):**
- Diltiazem tidak dianjurkan dalam hipotensyen teruk, sindrom nodus sinus sakit (tanpa pembuat rentak jantung), blok AV darjah kedua atau ketiga, dan infark miokardium akut dengan kepenatan paru.
- Interaksi ubat yang ketara wujud dengan beta-penyekat (pendepresan jantung aditif), substrat CYP3A4 (Diltiazem ialah perencat CYP3A4 sederhana), siklosporin, simvastatin, dan agen lain.
- Kesan buruk yang biasa termasuk bradikardia, edema, pusing-pusing, dan sakit kepala.

> **Tindakan diperlukan:** Muat turun dan analisis sisipan pakej (仿單) dari pihak berkuasa kawal selia dan isi medan keselamatan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tunda**

**Alasan:**
Pakej bukti ini kekurangan data kritikal yang diperlukan untuk penilaian penggunaan semula ubat. Tiada **petunjukan yang diramalkan TxGNN**, ID DrugBank tidak dipautkan (walaupun pertanyaan berjaya), butir kawal selia peringkat lesen hilang, dan semua medan keselamatan kosong. Tanpa petunjukan calon untuk dinilai, tiada penilaian penggunaan semula boleh diteruskan.

**Untuk diteruskan, perkara berikut diperlukan:**

1. **Jalankan saluran ramalan TxGNN** untuk Diltiazem Hydrochloride dan isikan `predicted_indications` dengan penyakit calon, skor, ujian klinikal, dan bukti kesusasteraan
2. **Pautkan ID DrugBank** — log pertanyaan mengesahkan carian DrugBank berjaya (result_count = 1); petakan ke **DB00343** dan ambil data MOA, farmakodinamik, dan ketoksikanan
3. **Isikan butir lesen NPRA** — ambil nombor kelulusan, nama produk, bentuk dos, dan teks petunjukan yang diluluskan untuk semua 6 produk berdaftar
4. **Ambil data keselamatan** — muat turun sisipan pakej dan analisis amaran utama, kontraindikasi, dan maklumat interaksi ubat-ubat (menangani jurang data Menyekat DG001)
5. **Isikan medan MOA** — ambil mekanisme tindakan dari DrugBank untuk membolehkan analisis kebolehplausibilan mekanis (menangani jurang data keberatan tinggi DG002)

---

*Penafian: Laporan ini adalah untuk tujuan penyelidikan sahaja dan tidak membentuk nasihat perubatan. Sebarang calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.*

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

