---
layout: default
title: Panduan Pengguna
parent: Bantuan
nav_order: 2
description: "Cara menggunakan platform ramalan penggunaan semula ubat MyTxGNN"
permalink: /guide/
---

# Panduan Pengguna

Pelajari cara menggunakan MyTxGNN secara berkesan untuk penyelidikan penggunaan semula ubat.

---

## Mula Di Sini

### Apa Yang Boleh Anda Lakukan Dengan MyTxGNN?

1. **Layari Ramalan Ubat**: Lihat indikasi baharu yang diramal untuk {{ site.data.drug_stats.total_drugs }} ubat berdaftar NPRA
2. **Akses FHIR API**: Integrasikan ramalan ke dalam sistem klinikal anda
3. **Muat Turun Data**: Dapatkan data ramalan dalam format CSV untuk analisis
4. **Pantau Berita**: Jejaki berita kesihatan berkaitan penggunaan semula ubat di Malaysia

---

## Memahami Ramalan

### Bagaimana Ramalan Dibuat

MyTxGNN menyenaraikan ramalan penggunaan semula ubat daripada model TxGNN (pembelajaran mendalam: rangkaian neural graf yang dilatih pada graf pengetahuan bioperubatan).

- Model memberi skor kepada setiap pasangan ubat–penyakit
- Indikasi yang sudah direkodkan bagi ubat itu dalam graf pengetahuan atau dalam lesen produknya dikira sebagai kegunaan sedia ada; indikasi ini dikecualikan dan tidak dikira sebagai ramalan baharu
- Halaman ubat menyenaraikan sehingga 10 ramalan teratas yang selebihnya, dengan skor sekurang-kurangnya 0.99

### Mentafsir Keputusan

Laman ini hanya menyenaraikan ramalan dengan skor 0.99 atau lebih tinggi (sehingga 10 teratas bagi setiap ubat). Skor ini menyusun kedudukan calon di dalam model; ia bukan kebarangkalian keberkesanan klinikal.

---

## Menggunakan FHIR API

### Penyata Keupayaan

Semak keupayaan API:
```
GET /fhir/metadata
```

### MedicationKnowledge

Dapatkan maklumat ubat:
```
GET /fhir/MedicationKnowledge/{drugbank_id}
```

Contoh:
```
GET /fhir/MedicationKnowledge/db00860
```

### ClinicalUseDefinition

Dapatkan ramalan ubat-indikasi:
```
GET /fhir/ClinicalUseDefinition/{drug}-{indication}
```

Contoh:
```
GET /fhir/ClinicalUseDefinition/db00860-allergic-rhinitis
```

---

## Aliran Kerja Penyelidikan

### Langkah Yang Disyorkan

1. **Kenal Pasti Sasaran**
   - Mula dengan ubat yang diminati
   - Atau mula dengan penyakit yang anda ingin cari rawatan untuknya

2. **Semak Ramalan**
   - Periksa indikasi baharu yang diramal untuk ubat/penyakit tersebut
   - Periksa tahap bukti (L1–L5) bagi setiap ramalan

3. **Kumpul Bukti**
   - Gunakan pengumpul bukti kami (ClinicalTrials.gov, PubMed)
   - Semak ujian klinikal yang sedia ada

4. **Nilai Kebolehlaksanaan**
   - Pertimbangkan ketersediaan ubat di Malaysia (status NPRA)
   - Semak profil keselamatan

5. **Rancang Langkah Seterusnya**
   - Rangka kajian pengesahan
   - Berunding dengan pakar klinikal

---

## Tip Untuk Penyelidik

### Amalan Terbaik

1. **Rujuk-silang ramalan** dengan literatur sedia ada
2. **Semak pelbagai sumber** untuk data ujian klinikal
3. **Pertimbangkan mekanisme tindakan** semasa menilai ramalan
4. **Susun keutamaan mengikut tahap bukti**, bukan skor ramalan (semua ramalan yang disenaraikan berskor ≥0.99, dan skor itu bukan kebarangkalian)

### Perangkap Biasa Yang Perlu Dielakkan

1. **Jangan anggap ramalan sebagai dapatan yang sudah disahkan**
2. **Jangan abaikan pertimbangan keselamatan**
3. **Jangan bergantung semata-mata pada skor tinggi** - konteks penting
4. **Jangan langkau pertimbangan regulatori**

---

## Soalan Lazim

### S: Seberapa tepat ramalan tersebut?

J: TxGNN telah disahkan terhadap hubungan ubat-penyakit yang diketahui dengan ketepatan tinggi. Walau bagaimanapun, ramalan perlu disahkan melalui bukti klinikal sebelum aplikasi.

### S: Bolehkah saya menggunakan data ini untuk tujuan komersial?

J: Data disediakan untuk tujuan penyelidikan. Penggunaan komersial mungkin tertakluk kepada lesen sumber data individu (DrugBank, dll.).

### S: Berapa kerap data dikemas kini?

J: Data NPRA dikemas kini setiap minggu. Ramalan dijana semula secara berkala apabila model asas diperbaiki.

### S: Mengapa sesetengah ubat tidak disertakan?

J: Hanya ubat yang boleh dipetakan kepada ID DrugBank disertakan. Sesetengah produk tempatan atau kombinasi mungkin tidak mempunyai entri DrugBank.

---

## Mendapatkan Bantuan

### Sumber

- **GitHub Issues**: Laporkan pepijat atau minta ciri
- **Halaman Metodologi**: Fahami pendekatan ramalan kami
- **Sumber Data**: Ketahui asal-usul data kami

### Hubungi

Untuk pertanyaan kerjasama penyelidikan, sila buka isu GitHub dengan label "collaboration".

---

<div class="disclaimer">
<strong>Untuk Tujuan Penyelidikan Sahaja</strong><br>
MyTxGNN direka untuk tujuan penyelidikan. Sentiasa sahkan ramalan melalui ujian klinikal yang sewajarnya dan dapatkan nasihat profesional kesihatan untuk keputusan perubatan.
</div>
