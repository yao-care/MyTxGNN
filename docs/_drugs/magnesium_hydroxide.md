---
layout: default
title: Magnesium Hydroxide
parent: High Evidence (L1-L2)
nav_order: 461
evidence_level: L2
indication_count: 5
---

# Magnesium Hydroxide
{: .fs-9 }

Tahap bukti: **L2** | Indikasi diramal: **5** 
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

# Magnesium Hydroxide: Daripada Penggunaan Antasid/Laksatif kepada Esofagitis

## Ringkasan Satu Ayat

Magnesium Hydroxide (DrugBank DB09104) ialah antasid dan laksatif osmotik yang telah diiktiraf di pasaran bebas (bahan aktif dalam "Milk of Magnesia"), sedang dipasarkan di Malaysia dengan **41 pendaftaran**. Kandidat petunjuk teratas yang direngka oleh model TxGNN ialah **Esofagitis**, disokong oleh **1 percubaan klinikal** dan **19 penerbitan** — tetapi percubaan itu ditamatkan, kebanyakan literatur membincangkan antasid kombinasi *magnesium/aluminum-hydroxide* bukan magnesium hydroxide sahaja, dan skor ramalan model itu sendiri untuk kandidat ini ialah **0.00%**, yang merupakan kaveat penting yang tidak sepatutnya diabaikan.

---

## Gambaran Keseluruhan Pantas

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Tidak diekstrak dalam paket bukti ini — semua sampel medan `approved_indication_text` lesen NPRA/TFDA adalah kosong. Magnesium hydroxide diiktiraf secara generik sebagai antasid bebas lesen / laksatif osmotik, tetapi dataset khusus ini tidak memberikan teks label yang disahkan (lihat Jurang Data DG001/DG002 di bawah) |
| Petunjuk Baru Diramal | Esofagitis |
| Skor Ramalan TxGNN | 0.00% |
| Tahap Bukti | L2 |
| Status Pasaran Malaysia | ✓ Dipasarkan (Dipasarkan) |
| Bilangan Pendaftaran | 41 |
| Keputusan yang Disyorkan | Teruskan dengan Langkah Kawal |

---

## Mengapa Ramalan Ini Munasabah?

Data mekanisme tindakan terperinci tidak tersedia untuk rekod ini dalam DrugBank. Berdasarkan pengetahuan farmakologi umum, magnesium hydroxide terurai dalam bendalir gastrik untuk mengeluarkan ion hidroksida yang meneutralkan asid hidroklorik, dengan cepat menaikkan pH intragastrik dan (sementara) intra-esofagus; pada dos yang lebih tinggi dan kurang diserap di lumen, ia juga menarik air ke dalam usus secara osmotik, yang mendasari penggunaan berasingannya sebagai laksatif.

Esofagitis adalah terutamanya proses kecederaan mukosa yang dimediasi asid — sama ada didorong oleh reflaks gastroesofagus, pencederaan kimia langsung, atau (dalam satu percubaan yang langsung relevan) terapi radiasi. Kerana tindakan antasid magnesium hydroxide secara langsung menargetkan komponen asid daripada laluan kecederaan itu, sambungan mekanis kepada esofagitis adalah munasabah. Walau bagaimanapun, kekuatan kandidat khusus ini adalah terhad: satu-satunya percubaan berdaftar yang langsung relevan, NCT01336530, menguji **Tepilta®** — kombinasi tetap oxetacaine (anesthetik topical) dan antasid — untuk esofagitis yang disebabkan radiasi, bukan magnesium hydroxide sebagai agen tunggal, dan percubaan itu ditamatkan sebelum selesai. Kebanyakan literatur sokongan juga mengkaji magnesium hydroxide dalam kombinasi dengan aluminum hydroxide (cth, Mylanta, produk jenis Maalox) bukan sebagai monotherapi. Digabungkan dengan skor TxGNN 0.00% untuk kandidat ini, kebolehsuksesan mekanis adalah munasabah tetapi keyakinan model dan bukti tahap percubaan khusus untuk esofagitis adalah kedua-duanya lemah.

---

## Bukti Percubaan Klinikal

| Nombor Percubaan | Fasa | Status | Penggabungan | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT01336530](https://clinicaltrials.gov/study/NCT01336530) | Fasa 3 | Ditamatkan | 40 | Percubaan adaptif terkawal plasebo buta dua hala, rawak bagi Tepilta® (oxetacaine + antasid) berbanding komponen individunya berbanding plasebo untuk esofagitis yang disebabkan radiasi; dirancang untuk menunjukkan keunggulan kombinasi tetapi ditamatkan sebelum penggabungan penuh, mengehadkan kesimpulan. |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [2986275](https://pubmed.ncbi.nlm.nih.gov/2986275/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | Sukralfat berbanding alginate/antasid dalam percubaan rawak 6 minggu untuk esofagitis reflaks; ~70% pesakit di kedua-dua lengan bertambah baik, esofagitis sembuh sepenuhnya dalam 53% pada sukralfat. |
| [6250928](https://pubmed.ncbi.nlm.nih.gov/6250928/) | 1980 | RCT (crossover) | J Int Med Res | Percubaan crossover membandingkan Liquid Gaviscon dengan gel antasid magnesium/aluminum hydroxide untuk heartburn; Gaviscon memberikan pelepasan yang lebih cepat dan lebih lengkap daripada antasid Mg/Al. |
| [8047802](https://pubmed.ncbi.nlm.nih.gov/8047802/) | 1994 | RCT | Scand J Gastroenterol | Percubaan buta dua hala dalam 80 kanak-kanak dengan GER membandingkan domperidone + Mg(OH)2/Al(OH)3, domperidone + alginate, domperidone sahaja, dan plasebo; lengan kombinasi menunjukkan penambahbaikkan klinikal dan pemantauan pH. |
| [1798406](https://pubmed.ncbi.nlm.nih.gov/1798406/) | 1991 | Kohort | Minerva Pediatrica | 15 kanak-kanak dengan GER yang dirawat dengan Mg(OH)2/Al(OH)3 selama 8 minggu; 12/15 sembuh, 3/15 bertambah baik, dengan masa dedahan asid esofagus yang berkurangan pada pemantauan pH. |
| [11854825](https://pubmed.ncbi.nlm.nih.gov/11854825/) | 1995 | Kohort/perbandingan | American Journal of Therapeutics | Crossover buta tunggal dalam 83 subjek heartburn membandingkan Al(OH)3/Mg(OH)2 berbanding CaCO3 berbanding plasebo pada pH esofagus/gastrik selepas makanan refluksogenik. |
| [25419906](https://pubmed.ncbi.nlm.nih.gov/25419906/) | 2014 | Tinjauan Sistematis Cochrane | Cochrane Database of Systematic Reviews | Tinjauan rawatan farmakologi (termasuk antasid) untuk reflaks gastro-esofagus pediatrik; menyoroti bukti berkualiti tinggi yang terhad secara keseluruhan. |
| [10908549](https://pubmed.ncbi.nlm.nih.gov/10908549/) | 2000 | Tinjauan Sistematis Cochrane | Cochrane Database of Systematic Reviews | Tinjauan cisapride untuk GOR pediatrik, mencatat kebimbangan keselamatan (perpanjangan QTc, aritmia) dengan alternatif prokinetik kepada terapi antasid. |
| [24355558](https://pubmed.ncbi.nlm.nih.gov/24355558/) | 2014 | Tinjauan | Gastroenterología y Hepatología | Kemas kini pengurusan GERD, mencatat ~1/3 pesakit non-erosif bertindak balas tidak memuaskan kepada PPI, memotivasi minat dalam terapi asid-penetral pelengkap/alternatif. |
| [10848650](https://pubmed.ncbi.nlm.nih.gov/10848650/) | 2000 | Tinjauan | Alimentary Pharmacology & Therapeutics | Tinjauan formulasi alginate pembentukan rakit (cth, Gaviscon, sering digabung dengan antasid) untuk heartburn dan esofagitis, menerangkan mekanisme rakit gel yang berbeza. |
| [1783346](https://pubmed.ncbi.nlm.nih.gov/1783346/) | 1991 | Kajian perbandingan buta dua hala | Fortschritte der Medizin | Kajian berbilang pusat buta dua hala dalam 97 pesakit membandingkan kombinasi antasid smectite/Al(OH)3/Mg(OH)2 terhadap antasid aluminum hydroxide standard untuk gastritis, esofagitis, dan simptom perut atas fungsional. |

---

## Maklumat Pasaran Malaysia

Status pasaran Malaysia dicatatkan sebagai **Dipasarkan (Dipasarkan)** dengan **41 pendaftaran keseluruhannya**, tetapi rekod lesen individu yang dibekalkan dalam paket bukti ini (nombor lesen, nama produk, bentuk dos, pengilang, teks petunjuk yang disahkan) semuanya dikembalikan kosong — ini nampaknya merupakan jurang pengekstrakan data bukan ketiadaan pendaftaran, dan harus diperbaharui sebelum maklumat ini digunakan dalam sebarang penilaian kawal selia atau keselamatan (lihat Jurang Data DG001).

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan — data `key_warnings`, `contraindications`, dan DDI berstruktur semuanya dikembalikan sebagai jurang data (DG001, ditandakan graviti Penyekat) dan tiada rekod interaksi ditemui.

**Nota tambahan daripada bukti literatur (bukan daripada data keselamatan berstruktur):** dua laporan kes bebas yang dikenal pasti di tempat lain dalam paket bukti ini — [38152602](https://pubmed.ncbi.nlm.nih.gov/38152602/) (hipermagnesemia fatal dalam pesakit yang mengambil magnesium hydroxide, 2023) dan [9533062](https://pubmed.ncbi.nlm.nih.gov/9533062/) (hipermagnesemia yang disebabkan antasid dalam pesakit dengan fungsi ginjal normal dan penyumbatan usus) — menandai risiko hipermagnesemia yang nyata dengan magnesium hydroxide, terutamanya dalam gangguan ginjal atau mobilitas GI yang berkurangan. Ini harus dianggap sebagai item keselamatan keutamaan untuk mana-mana laluan repurposing, walaupun ia tidak muncul dalam medan `safety` rasmi.

---

## Petunjuk Lain yang Diramal (Paket Bukti Sama)

Paket bukti ini ("TW-DB09104-multi") menilai lima petunjuk kandidat bersama-sama. Untuk konteks, empat kandidat terkawal lain yang disenaraikan ialah:

| Kedudukan | Penyakit | Tahap Bukti | Peringkat Keputusan | Saranan |
|------|----------|----------------|----------------|-----------------|
| 2 | Gangguan sembelit | L2 | S2 | Teruskan dengan Langkah Kawal |
| 3 | Penyakit reflaks gastroesofagus | L2 | S2 | Teruskan dengan Langkah Kawal |
| 4 | Esofagitis peptik | L3 | S1 | Soalan Penyelidikan |
| 5 | Penyakit ulser peptik | L4 | S1 | Tahan |

Adalah ketara bahawa **sembelit** (penggunaan laksatif osmotik klasik Mg(OH)2) dan **GERD** (dua percubaan Fasa 1, NCT03065816 dan NCT03069963, secara langsung mengukur aktiviti antasid dengan scintigrafi/pH-metry) mempunyai bukti langsung yang sebanding atau lebih kuat daripada esofagitis itu sendiri, dan mungkin menjamin keutamaan yang sama atau lebih tinggi dalam penilaian susulan.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Teruskan dengan Langkah Kawal**

**Alasan:**
Mekanisme penetral asid adalah munasabah untuk esofagitis dan tahap bukti adalah L2, tetapi satu-satunya percubaan yang langsung relevan adalah kajian Fasa 3 yang ditamatkan bagi produk kombinasi yang berbeza, kebanyakan literatur meliputi magnesium hydroxide hanya sebagai sebahagian daripada antasid kombinasi, dan skor ramalan model itu sendiri (0.00%) adalah anomali rendah dan tidak harus dianggap sebagai isyarat keyakinan tanpa pengesahan.

**Untuk meneruskan, perkara berikut diperlukan:**
- Pengekstrakan teks lesen dan label NPRA/TFDA sebenar (sedang kosong untuk semua entri yang disampel — DG001, Penyekat)
- Data mekanisme tindakan DrugBank/DrugBank API (DG002, Tinggi)
- Pelabelan keselamatan rasmi: amaran utama, kontraindikasi, dan data DDI (semua jurang data pada masa ini)
- Penjelasan/pengesahan saluran pemarkahan TxGNN untuk kandidat ini, memandangkan skor 0.00% di semua lima petunjuk terkawal
- Penilaian keselamatan yang tertumpu pada risiko hipermagnesemia (dimaklumi oleh PMID 38152602 dan 9533062), terutamanya untuk pesakit dengan gangguan ginjal, sebelum mempertimbangkan sebarang penggunaan monotherapi dalam esofagitis
- Pertimbangkan untuk menilai kandidat sembelit dan GERD (juga L2, dengan bukti percubaan agen tunggal yang lebih langsung) secara selari, kerana mereka mungkin mewakili peluang repurposing jangka pendek yang lebih kuat daripada esofagitis

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

