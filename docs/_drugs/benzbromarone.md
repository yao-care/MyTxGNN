---
layout: default
title: Benzbromarone
parent: Low Evidence (L4-L5)
nav_order: 128
evidence_level: L5
indication_count: 1
---

# Benzbromarone
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

# Benzbromarone: Dari Hiperurisemia/Gout kepada Hipourisemia Renal

## Ringkasan Satu Ayat

Benzbromarone adalah agen urikosurik (penghambat URAT1) yang asal digunakan untuk merawat hiperurisemia dan gout.
Model TxGNN meramalkan ia mungkin berkesan untuk **Hipourisemia Renal**, dengan **0 uji klinis** dan **20 penerbitan** dikenal pasti—namun, analisis mekanis menunjukkan ini adalah **positif palsu yang kontra-indikasi**: ubat ini akan memburukkan, bukan merawat, keadaan yang diramalkan.

## Gambaran Pantas

| Item | Kandungan |
|------|------|
| Indikasi Asli | Hiperurisemia / Gout (maklumat lesen tidak tersedia) |
| Indikasi Baru yang Diramalkan | Hipourisemia, renal |
| Skor Ramalan TxGNN | 99.07% |
| Tahap Bukti | L5 — Ramalan model sahaja; tiada bukti klinis terapeutik |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 1 |
| Keputusan yang Disyorkan | **Tahan** ⛔ (Percanggahan mekanis) |

## Mengapa Ramalan Ini Munasabah?

**Jawapan ringkas: ia tidak.** Walaupun model TxGNN memberikan skor keyakinan yang tinggi (99.07%), analisis mekanis yang lebih mendalam mendedahkan ramalan ini adalah positif palsu klasik yang didorong oleh perkaitan laluan tanpa mengambil kira arah terapeutik.

Benzbromarone adalah penghambat potent URAT1 (pengangkut urate 1, dikodkan oleh gen *SLC22A12*). Tindakan farmakologinya menghalang penyerapan semula asid urik di tubulus proksimal renal, dengan itu mempromosikan pembuangan asid urik air kencing. Mekanisme ini menjadikannya berkesan untuk merawat **hiperurisemia** dan **gout**, di mana matlamat terapeutik adalah untuk *menurunkan* urate serum dengan *meningkatkan* pembersihan urate renal.

Hipourisemia renal, sebaliknya, adalah gangguan warisan yang disebabkan oleh **mutasi kehilangan fungsi** dalam URAT1 (*SLC22A12*) atau GLUT9 (*SLC2A9*). Pesakit sudah mempunyai penyerapan semula urate yang rosak, menghasilkan lebihan pembuangan urate air kencing dan tahap urate serum yang berbahaya rendah. Memberikan benzbromarone—ubat yang seterusnya merencat pengangkut yang sudah disfungsi—akan **memburukkan** keadaan daripada merawatnya. Model TxGNN dengan betul mengenal pasti bahawa benzbromarone dan hipourisemia renal berkongsi laluan URAT1, tetapi ia **tidak dapat membezakan antara "merawat melalui laluan ini" dan "bertindak pada laluan yang sama dalam arah yang salah."** Ini adalah batasan yang dikenali dengan baik bagi model pemindahan ubat berasaskan graf pengetahuan.

## Bukti Uji Klinis

Pada masa ini tiada uji klinis yang berkaitan berdaftar untuk benzbromarone dalam merawat hipourisemia renal.

## Bukti Sastera

Dua puluh penerbitan telah dikenal pasti; bagaimanapun, tiada satu pun menerangkan penggunaan terapeutik benzbromarone untuk hipourisemia renal. Sebaliknya, benzbromarone muncul secara eksklusif sebagai **penyelaras farmakologi diagnostik** yang digunakan untuk mencirikan kecacatan pengangkutan urate. Penerbitan yang paling relevan diringkaskan di bawah:

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Ulasan | Clin Rheumatol | Ulasan komprehensif hipourisemia untuk ahli reumatologi; mengklasifikasi asal usul dan membincangkan mutasi URAT1/GLUT9. Benzbromarone disebut sebagai alat diagnostik sahaja. |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Pemerhatian/Molekul | J Am Soc Nephrol | Menjujuk SLC22A12 dalam 32 pesakit hipourisemia renal; menetapkan bahawa mutasi URAT1 menyebabkan gangguan. Benzbromarone digunakan dalam analisis pengangkutan tubulus. |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Pra-klinis/Mekanis | J Am Soc Nephrol | Mencirikan homolog URAT1 tikus (RST); benzbromarone menghalang pengangkutan urate yang dimediasi RST dalam oosit Xenopus, mengesahkan mekanisme perencatan URAT1. |
| [18670416](https://pubmed.ncbi.nlm.nih.gov/18670416/) | 2008 | Kajian Farmakologi | Am J Hypertens | Menunjukkan tindakan urikosurik losartan melalui perencatan URAT1 dalam pesakit hipertensi; memberi konteks mekanisme benzbromarone bersama-sama dengan penghambat URAT1 yang lain. |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Laporan Kes | Am J Kidney Dis | Dua adik beradik dengan hipourisemia renal warisan dan kegagalan akut teraruh senaman; mutasi URAT1 (W258X) dikenal pasti. Benzbromarone digunakan sahaja dalam kerja diagnostik. |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Kajian Farmakologi | Nephron | Menganalisis pengangkutan asid urik dalam sindrom Fanconi dengan hipourisemia renal yang ketara menggunakan pyrazinamide dan benzbromarone sebagai penyelaras farmakologi. |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Siri Kes | Clin Nephrol | Pesakit dengan ARF teraruh senaman berulang dan hipourisemia renal; ujian benzbromarone/pyrazinamide digunakan untuk menetapkan lokasi kecacatan pengangkutan tubulus. |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Laporan Kes | Acta Paediatr | ARF teraruh senaman berulang dalam hipourisemia renal; ujian benzbromarone/pyrazinamide mencadangkan penyerapan semula pra-sekretori yang rosak. |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Siri Kes | J Pediatr | Empat anak-anak dengan hipourisemia renal warisan; pyrazinamide dan benzbromarone tidak mempengaruhi nisbah pembersihan, konsisten dengan kecacatan pengangkutan yang teruk. |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Laporan Kes/Mekanis | Nephron | Lelaki muda dengan kecacatan pengangkutan urate renal terpencil; pembersihan urate seterusnya meningkat selepas benzbromarone, mengesahkan ubat memburukkan fenotip. |

> **Pemerhatian utama:** Dalam beberapa laporan kes (PMID 3380222, 8863890, 4009341), pemberian benzbromarone **meningkatkan** pembersihan urate dalam pesakit hipourisemia—iaitu, ia memburukkan keadaan. Ini secara langsung mengesahkan kontra-indikasi mekanis.

## Maklumat Pasaran Malaysia

| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi yang Diluluskan |
|---------|------|------|-----------|
| (Maklumat tidak tersedia) | — | — | — |

*Catatan: Satu pendaftaran dicatat di Malaysia (status pasaran: dipasarkan), tetapi maklumat lesen terperinci tidak diambil. Benzbromarone dikenali secara antarabangsa sebagai agen urikosurik yang ditunjukkan untuk hiperurisemia dan gout.*

## Pertimbangan Keselamatan

Sila rujuk pada surat kenyataan bercetak untuk maklumat keselamatan. Data amaran utama, kontra-indikasi, dan interaksi ubat tidak tersedia dalam pakej bukti ini.

> **Nota penting khusus untuk ramalan ini:** Benzbromarone mempunyai risiko **hepatotoksisiti** yang diketahui (sebab ia ditarik balik di beberapa pasaran Eropah). Selain itu, dalam pesakit dengan hipourisemia renal, penggunaan benzbromarone secara teorinya boleh mencetuskan **kegagalan akut renal teraruh senaman** dengan seterusnya meningkatkan pembuangan asid urik air kencing dan mempromosikan pemendapan kristal urate intratubuler.

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan ⛔**

**Rasional:**
Ramalan ini mewakili **positif palsu mekanis**. Model TxGNN mengesan perkaitan yang kuat antara benzbromarone dan hipourisemia renal melalui laluan URAT1 yang dikongsi, menghasilkan skor ramalan yang tinggi (99.07%). Bagaimanapun, tindakan farmakologi ubat (perencatan URAT1 → peningkatan pembuangan urate) adalah **bertentangan sepenuhnya** dengan apa yang diperlukan oleh pesakit hipourisemia renal (penyerapan semula urate yang dipulihkan → penurunan pembuangan urate). Laporan kes yang diterbitkan mengesahkan bahawa benzbromarone memburukkan pembersihan urate dalam pesakit ini. Calon ini tidak harus meneruskan ke mana-mana peringkat penilaian lanjut.

**Kes ini menyoroti batasan penting bagi model pemindahan berasaskan graf pengetahuan:** perkaitan peringkat laluan tidak sama dengan kebolehan terapeutik. Penalaran farmakologi berarah mesti diterapkan sebagai penapis pasca-ramalan.

**Tiada tindakan lanjut disyorkan untuk calon ini.** Sebaliknya, penambahbaikan model berikut dicadangkan:
- Gabungkan **anotasi arah** (agonis/antagonis, keuntungan fungsi/kehilangan fungsi) ke dalam graf pengetahuan TxGNN untuk mengurangkan positif palsu yang kontra-indikasi
- Bendera calon di mana MOA ubat menyasarkan pengangkut/reseptor yang sama yang terlibat dalam asal usul kehilangan fungsi penyakit

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

