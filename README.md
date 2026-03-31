# MyTxGNN - Malaysia: Ramalan Penggunaan Semula Ubat

[![Website](https://img.shields.io/badge/Website-mytxgnn.yao.care-blue)](https://mytxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ramalan penggunaan semula ubat (drug repurposing) untuk Malaysia menggunakan model TxGNN.

## Notis Penting

- Keputusan projek ini adalah untuk tujuan penyelidikan sahaja dan bukan nasihat perubatan.
- Calon penggunaan semula ubat memerlukan pengesahan klinikal sebelum aplikasi.

## Gambaran Keseluruhan Projek

| Perkara | Jumlah |
|---------|--------|
| **Laporan Ubat** | 508 |
| **Jumlah Ramalan** | 18,287,982 |

## Kaedah Ramalan

### Kaedah Graf Pengetahuan (Knowledge Graph)
Pertanyaan langsung hubungan ubat-penyakit dalam graf pengetahuan TxGNN, mengenal pasti calon penggunaan semula yang berpotensi berdasarkan hubungan sedia ada dalam rangkaian biomedikal.

### Kaedah Pembelajaran Mendalam (Deep Learning)
Menggunakan model rangkaian neural pra-latih TxGNN untuk mengira skor ramalan, menilai kebarangkalian petunjuk terapeutik baharu untuk ubat yang diluluskan.

## Pautan

- Laman Web: https://mytxgnn.yao.care
- Kertas TxGNN: https://doi.org/10.1038/s41591-023-02233-x
