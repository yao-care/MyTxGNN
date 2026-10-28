---
layout: default
title: "Kegunaan diketahui sahaja (tiada ramalan baharu)"
nav_order: 24
permalink: /known-uses/
description: "Bagi ubat-ubat ini, semua calon daripada model TxGNN sudah merupakan kegunaan yang diketahui (direkodkan dalam graf pengetahuan atau dalam pendaftaran ubat…"
---

# Kegunaan diketahui sahaja (tiada ramalan baharu)

Bagi ubat-ubat ini, semua calon daripada model TxGNN sudah merupakan kegunaan yang diketahui (direkodkan dalam graf pengetahuan atau dalam pendaftaran ubat), jadi tiada indikasi baharu yang diramal. Setiap halaman menyenaraikan kegunaan yang diketahui dan status pasaran tempatan.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} ubat**

| Ubat | Laporan |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Lihat halaman]({{ drug.url | relative_url }}) |
{% endfor %}
