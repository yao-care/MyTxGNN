---
layout: default
title: Posaconazole
parent: Low Evidence (L4-L5)
nav_order: 589
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: indikasi baharu diramal Pneumocystosis (tahap bukti L5). Indikasi asal: Tidak direkodkan dalam data tempatan"
---

# Posaconazole
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **1** 
{: .fs-6 .fw-300 }

---

## Isi kandungan
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Laporan penilaian ahli farmasi

</div>

## Posaconazole: Pneumocystosis
{: .text-alpha }

## Ringkasan Satu Ayat

Posaconazole ialah ubat antikulat kumpulan triazole yang pada asalnya digunakan untuk merawat pelbagai jangkitan kulat seperti kandidiasis, aspergillosis, histoplasmosis dan sporotrikosis.
Model TxGNN meramalkan ia mungkin berkesan untuk **pneumocystosis**, tetapi sokongan buktinya masih lemah: terdapat **1 ujian klinikal** (tidak menguji posaconazole secara langsung) dan **5 penerbitan** (kebanyakannya ulasan umum).

---

## Gambaran Keseluruhan

| Perkara | Kandungan |
|------|------|
| Indikasi Asal | Tidak direkodkan dalam data tempatan |
| Indikasi Baharu Diramal | Pneumocystosis |
| Skor Ramalan TxGNN | 0.9977 |
| Tahap Bukti | L5 |
| Status Pasaran di Malaysia | Dipasarkan (pendaftaran sah: 3 daripada 3) |
| Bilangan Pendaftaran | 3 (sah: 3) |
| Keputusan Disyorkan | Hold (Tahan) |

---

## Mengapa Ramalan Ini Munasabah?

Data terperinci mengenai mekanisme tindakan (MOA) asal tidak tersedia dalam data yang dihimpunkan untuk laporan ini. Berdasarkan pengetahuan umum, posaconazole ialah antikulat triazole yang menghalang enzim lanosterol 14-alfa-demetilase (CYP51), lalu menyekat sintesis ergosterol dalam membran sel kulat.

Namun, *Pneumocystis jirovecii* tidak mempunyai ergosterol dalam membran selnya dan menggunakan kolesterol serta sterol lain. Oleh itu, mekanisme azole hanya mempunyai asas biologi yang sangat terhad untuk organisma ini. Skor yang sangat tinggi (0.9977) datang daripada model TxGNN (pembelajaran mendalam) dan mungkin mencerminkan persamaan yang dipelajari oleh model antara penyakit berkaitan, bukan bukti biologi.

Hubungan antara indikasi asal dengan indikasi baharu juga masih belum dinilai secara terperinci. Ramalan ini harus dianggap sebagai hipotesis yang perlu disahkan dan bukan petunjuk keberkesanan.

---

## Bukti Ujian Klinikal

| Nombor Ujian | Fasa | Status | Pendaftaran | Penemuan Utama |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fasa 3 | Selesai | 602 | Rezafungin IV berbanding rejimen antimikrob standard untuk mencegah penyakit kulat invasif selepas pemindahan darah dan sumsum tulang alogenik. Ujian ini **tidak menguji posaconazole** dan tidak memberi bukti langsung untuk pneumocystosis. |

---

## Bukti Literatur

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Ulasan | The Lancet Infectious Diseases | Cadangan amalan terbaik British Society for Medical Mycology (kemas kini 2025) untuk diagnosis penyakit kulat serius; tertumpu pada kaedah diagnostik bukan kultur |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Ulasan | Zhonghua Jie He He Hu Xi Za Zhi | Garis panduan China (edisi 2025) untuk diagnosis dan pengurusan penyakit kulat pulmonari invasif |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Ulasan | Swiss Medical Weekly | Gambaran keseluruhan kandidiasis, aspergillosis, kriptokokosis dan pneumonia Pneumocystis invasif; profilaksis posaconazole aktif terhadap kulat acuan mengurangkan jangkitan pada pesakit hemato-onkologi berisiko tinggi |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Ulasan | Clinical Pharmacokinetics | Penembusan agen anti-infeksi, termasuk antikulat, ke dalam cecair lapisan epitelium pulmonari |

Tiada daripada penerbitan ini ialah ujian terkawal rawak yang menilai posaconazole untuk pneumocystosis.

---

## Pertimbangan Keselamatan

**Interaksi Ubat** (pertanyaan selesai; 100 interaksi direkodkan, sebahagian disenaraikan di sini):

- **Major**: loperamide, triamcinolone, budesonide
- **Moderate**: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, clarithromycin, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol (3350 dengan elektrolit)

Untuk amaran utama dan kontraindikasi, sila rujuk risalah maklumat produk.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Hold (Tahan)**

**Justifikasi:**
- Ramalan hanya bersandarkan model TxGNN (pembelajaran mendalam): skor tinggi tetapi mungkin mencerminkan persamaan yang dipelajari model antara penyakit berkaitan, bukan bukti biologi. Tiada ujian klinikal atau kajian yang menilai posaconazole untuk pneumocystosis. Asas mekanisme juga lemah kerana *Pneumocystis* tidak mempunyai ergosterol. Ubat ini dipasarkan di Malaysia dengan 3 lesen sah daripada 3 lesen.

**Untuk meneruskan, perkara berikut diperlukan:**
- Data mekanisme tindakan (MOA) yang lengkap daripada DrugBank
- Risalah maklumat produk daripada NPRA untuk amaran dan kontraindikasi (data keselamatan masih belum lengkap dan menghalang saringan keselamatan)
- Bukti praklinikal atau klinikal yang menilai posaconazole secara langsung terhadap *Pneumocystis*
- Penilaian status pendaftaran dan ketersediaan di Malaysia
- Penilaian keserasian laluan pentadbiran dan kesan interaksi ubat yang bermakna secara klinikal
## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

