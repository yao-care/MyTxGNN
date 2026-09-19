---
layout: default
title: Piperacillin
parent: Low Evidence (L4-L5)
nav_order: 549
evidence_level: L5
indication_count: 9
---

# Piperacillin
{: .fs-9 }

Tahap bukti: **L5** | Indikasi diramal: **9** 
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

# Piperacillin: Dari Jangkitan Bakteria ke Arthritis Reumatoid

## Ringkasan Satu Ayat

Piperacillin ialah antibiotik beta-lactam spektrum luas yang digunakan secara meluas untuk merawat jangkitan bakteria serius yang disebabkan oleh organisma gram-positif dan gram-negatif, paling lazim dibekalkan sebagai kombinasi piperacillin/tazobactam (Pip-Tazo). Model TxGNN memberikan skor ramalan tertinggi 99.94% untuk **Arthritis Reumatoid (AR)**, namun 18 penerbitan yang dipulihkan tidak mengandungi bukti langsung untuk piperacillin sebagai rawatan AR — mereka secara seragam menerangkan penggunaannya sebagai antibiotik untuk menguruskan jangkitan dalam pesakit AR, menunjukkan isyarat yang membingungkan daripada peluang terapeutik yang tulen.

---

## Gambaran Keseluruhan Cepat

| Item | Kandungan |
|------|----------|
| Petunjuk Asal | Jangkitan bakteria spektrum luas (patogen gram-positif dan gram-negatif) |
| Petunjuk Baru yang Diramalkan | Arthritis Reumatoid |
| Skor Ramalan TxGNN | 99.94% |
| Tahap Bukti | L5 (ramalan model sahaja; tiada kajian yang menyokong secara langsung) |
| Status Pasaran Malaysia | ✓ Dipasarkan |
| Bilangan Pendaftaran | 8 |
| Keputusan yang Disyorkan | **Tahan** |

---

## Mengapa Ramalan Ini Munasabah?

Piperacillin ialah antibiotik jenis penisilin beta-lactam yang mengeluarkan tindakannya dengan ikatan kovalen kepada protein yang mengikat penisilin (PBPs) pada permukaan sel bakteria, dengan itu merencat langkah paut silang akhir biosintesis peptidoglikan dan menyebabkan gangguan dinding sel dan lisis bakteria. Ia merangkumi pelbagai patogen klinikal yang penting termasuk *Pseudomonas aeruginosa*, *Enterobacteriaceae*, dan banyak streptokok. Data mekanistik terperinci dari DrugBank tidak tersedia pada masa ini untuk laporan ini; bagaimanapun, mekanismenya sebagai penghambat sintesis dinding sel sudah mapan dalam kesusasteraan farmakoloji.

Perkaitan TxGNN yang jelas antara piperacillin dan arthritis reumatoid hampir pasti mencerminkan **bias gangguan komorbiditasi** yang tertanam dalam graf pengetahuan. Pesakit AR pada metotreksat, penghambat JAK, atau biologik seperti etanersept secara sistemik disuppreskan imun dan kerap mengalami jangkitan bakteria serius yang memerlukan liputan antibiotik spektrum luas empirik — yang mana piperacillin/tazobactam ialah pilihan garis pertama standard. Model nampaknya telah mentafsir kekerapan tinggi ini "pesakit AR ↔ piperacillin" bersama dalam kesusasteraan biomedis sebagai isyarat terapeutik, sedangkan pada hakikatnya piperacillin merawat komplikasi jangkitan *imunusupresien*, bukan AR itu sendiri.

Beberapa antibiotik beta-lactam telah dilaporkan dalam tetapan preklinik untuk memiliki sifat imunomodulatori yang sederhana, termasuk penghambatan laluan NF-κB separa dan modulasi reseptor jenis Toll. Bagaimanapun, tiada bukti mekanistik atau klinikal langsung wujud untuk kesan sedemikian dengan piperacillin dalam konteks sinovitis autoimmun. Secara paradoks, penggunaan antibiotik spektrum luas yang berpanjangan mengganggu homeostasis mikrobiota usus, yang mungkin memburukkan dysregulasi imun dalam keadaan autoimmun seperti AR — menjadikan penggunaan jangka panjang dalam petunjuk ini secara biologi tidak produktif.

---

## Bukti Ujian Klinikal

Pada masa ini tiada ujian klinikal yang berkaitan didaftarkan untuk piperacillin dalam arthritis reumatoid.

---

## Bukti Kesusasteraan

18 penerbitan telah dipulihkan dengan menggabungkan "piperacillin" dengan "rheumatoid arthritis" dalam carian PubMed. **Tiada satu pun kertas kerja ini mengkaji piperacillin sebagai rawatan untuk AR.** Mereka mendokumentasikan piperacillin yang digunakan sebagai antibiotik untuk menguruskan jangkitan yang timbul dalam pesakit AR yang disuppreskan imun, atau komplikasi berkaitan metotreksat di mana piperacillin tidak muncul pun. 10 entri yang paling informatif dipersembahkan di bawah untuk ketelusan:

| PMID | Tahun | Jenis | Jurnal | Penemuan Utama |
|------|-------|-------|--------|----------------|
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Laporan Kes | Orthopädie | Pesakit AR pada penghambat JAK1 (upadacitinib) mengalami jangkitan lutut prostetik; piperacillin/tazobactam IV dimulai untuk pneumonia serentak — penggunaan antibiotik, bukan terapi AR |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Laporan Kes | BMJ Case Reports | Pesakit AR pada etanersept + metotreksat mengalami perikarditis purulen; piperacillin/tazobactam empirik dimulakan untuk jangkitan yang disyaki — ubat digunakan sebagai antibiotik, bukan pengubah AR |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Kohort Retrospektif | Br J Clin Pharmacol | Model pemarkahan risiko pembelajaran mesin untuk eosinofilia yang diinduksi antibiotik pada pesakit yang dirawat di hospital yang menerima piperacillin/tazobactam atau ampisilin/sulbaktam — kajian farmakoloji keselamatan, tiada kaitan AR |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Kohort Retrospektif | Ann Transl Med | Prevalensi dan ciri klinikal kecederaan hati yang diinduksi ubat yang berkaitan antibiotik (DILI); piperacillin disenaraikan dalam kalangan agen penyebab — kajian pengawasan DILI |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Laporan Kes | Cureus | Pesakit AR dalam pelepasan 9 tahun pada sulfasalazin mengalami efusi pleura berulang terpencil; piperacillin tidak terlibat |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Laporan Kes | Proc Baylor Univ Med Ctr | Ketoksikan metotreksat dos rendah menyebabkan sitopenia pankreas dan stomatitis dalam AR; penyelamatan leukovorin — piperacillin tidak terlibat |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Laporan Kes | Cureus | Sitopenia pankreas sebagai cabaran diagnostik dalam pesakit AR pada metotreksat dos rendah — piperacillin tidak disebut |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Laporan Kes | Orthopedics | Osteomielitis emfisematosa femoral bilateral yang disebabkan oleh *E. coli* dalam pesakit AR pada prednisone jangka panjang; dirawat dengan antibiotik IV dan semen antibiotik intramedular |
| [19621776](https://pubmed.ncbi.nlm.nih.gov/19621776/) | 2009 | Laporan Kes | No Shinkei Geka | Pachymeningitis hipertrofik dirawat dengan rejimen yang termasuk piperacillin; minosiklin mengurangkan CRP — piperacillin digunakan sebagai antibiotik, tiada kaitan autoimmun/AR |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Laporan Kes | Med J Australia | Sitopenia pankreas hampir fatal berikutan petasan metotreksat yang tidak disengajakan dalam AR — piperacillin tidak terlibat |

> ⚠️ **Nota Tafsiran Kritikal**: Tidak satu pun penerbitan yang dipulihkan menyediakan bukti bahawa piperacillin merawat, mengubah, atau mengurangkan arthritis reumatoid. Kehadiran bersama piperacillin dan AR dalam kertas ini mencerminkan peranan antibiotik dalam menguruskan komplikasi jangkitan dalam pesakit AR yang disuppreskan imun — satu senario gangguan klasik dalam ramalan berasaskan graf pengetahuan.

---

## Maklumat Pasaran Malaysia

Lapan lesen produk didaftarkan di Malaysia di bawah status Dipasarkan. Rekod pendaftaran terperinci (nama produk, bentuk dos, pengilang, teks petunjuk yang diluluskan) tidak dikembalikan oleh pertanyaan data NPRA untuk calon ini. Sila rujuk pangkalan data [Pendaftaran Produk NPRA](https://www.npra.gov.my) secara langsung untuk butiran lesen semasa.

---

## Pertimbangan Keselamatan

Sila rujuk sisipan pakej untuk maklumat keselamatan.

> Nota: Teks amaran penuh, kontraindikasi, dan data interaksi ubat-ubat tidak tersedia dalam sumber data pada masa laporan ini. Secara klinikal, piperacillin/tazobactam diketahui membawa risiko tindak balas hipersensitiviti (termasuk anafilaksis), DILI berkaitan antibiotik, dan eosinofilia dengan penggunaan yang berpanjangan. Pelarasan dos diperlukan dalam gangguan ginjal (CrCl yang berkurangan) — pertimbangan yang sangat relevan jika ubat ini pernah dinilai dalam pesakit AR dengan nefropati diabetik atau keradangan bersama.

---

## Kesimpulan dan Langkah Seterusnya

**Keputusan: Tahan**

**Alasan:**
Skor peringkat teratas model TxGNN sebanyak 99.94% untuk piperacillin dalam arthritis reumatoid hampir pasti merupakan artifak yang membingungkan yang didorong oleh frekuensi tinggi yang menerima piperacillin untuk jangkitan bakteria dalam pesakit AR yang disuppreskan imun; sifar ujian klinikal dan sifar penerbitan yang menyokong secara langsung mengesahkan bahawa tiada isyarat penyusunan semula yang tulen wujud. Tiada asas mekanistik — dan beberapa kemudaratan teori (disbiosis usus memburukkan autoimmuniti) — untuk mewajarkan pembangunan lanjutan calon ini.

**Untuk bergerak melampaui Tahan, yang berikut diperlukan:**

- **Pengesahan mekanisme**: Bukti preklinik yang menunjukkan kesan anti-keradangan langsung piperacillin pada laluan yang relevan dengan AR (cth., pencerobohan fibroblast sinovial, keseimbangan Th17/Treg, penghambatan NF-κB atau NLRP3) dalam model arthritis *in vitro* atau haiwan
- **Penyahberat graf pengetahuan**: Analisis semula graf TxGNN untuk membetulkan struktur gangguan "jangkitan dalam pesakit yang disuppreskan imun" sebelum penilaian semula
- **Perolehan data MOA**: Profil farmakoloji DrugBank penuh (pada masa ini tidak tersedia — jurang data DG002) untuk mengenal pasti sebarang sasaran imunomodulatori sekunder
- **Profil keselamatan kawal selia**: Perolehan dan penghuraian PDF sisipan produk Malaysia (pada masa ini tidak tersedia — jurang data DG001) untuk melengkapkan penilaian keselamatan yang diperlukan untuk penilaian S1
- **Penilaian kesan mikrobiom**: Kajian kesusasteraan tentang kesan beta-lactam pada komposisi mikrobiota usus dalam model penyakit autoimmun, memandangkan risiko teori memburukkan AR melalui disbiosis

## Penafian

Kandungan ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
Pengesahan klinikal diperlukan sebelum sebarang aplikasi klinikal.

---

