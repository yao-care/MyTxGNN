---
layout: default
title: Sumber Integrasi
parent: SMART on FHIR
nav_order: 3
description: "Sumber dan alat untuk integrasi SMART on FHIR MyTxGNN"
permalink: /smart/resources/
---

# Sumber Integrasi

<p class="key-answer" data-question="Apakah sumber yang tersedia untuk integrasi?">
Halaman ini menyenaraikan alat, pustaka, dan sumber yang boleh membantu anda mengintegrasikan MyTxGNN dengan sistem kesihatan anda.
</p>

---

## Pustaka Pelanggan FHIR

### JavaScript

| Pustaka | Penerangan | Pautan |
|---------|------------|--------|
| **SMART on FHIR JS** | Pustaka rasmi SMART | [GitHub](https://github.com/smart-on-fhir/client-js) |
| **fhir.js** | Pelanggan FHIR ringan | [GitHub](https://github.com/FHIR/fhir.js) |

### Python

| Pustaka | Penerangan | Pautan |
|---------|------------|--------|
| **fhirclient** | Pelanggan SMART resmi | [GitHub](https://github.com/smart-on-fhir/client-py) |
| **fhir.resources** | Model sumber FHIR | [PyPI](https://pypi.org/project/fhir.resources/) |

### Java

| Pustaka | Penerangan | Pautan |
|---------|------------|--------|
| **HAPI FHIR** | Pelaksanaan FHIR Java | [hapifhir.io](https://hapifhir.io/) |

---

## Alat Pembangunan

### SMART App Launcher

Gunakan untuk menguji aplikasi SMART tanpa EHR sebenar:

- **URL**: [launch.smarthealthit.org](https://launch.smarthealthit.org/)
- **Tujuan**: Simulasi pelancaran SMART dari EHR
- **Ciri**: Pilih pesakit ujian, skop, dan versi FHIR

### Pelayan FHIR Ujian

| Pelayan | URL | Penerangan |
|---------|-----|------------|
| **HAPI FHIR** | hapi.fhir.org/baseR4 | Pelayan awam percuma |
| **Logica Health** | api.logicahealth.org | Sandbox dengan data ujian |
| **Firely** | server.fire.ly | Pelayan FHIR komersial |

---

## Templat dan Contoh

### Templat Aplikasi SMART

```html
<!DOCTYPE html>
<html>
<head>
  <title>MyTxGNN SMART App</title>
  <script src="https://cdn.jsdelivr.net/npm/fhirclient@2.5.4/build/fhir-client.min.js" integrity="sha384-oPoE+RWX2AZE9PQcDKKsuPU0dLmhGHCmCScrIneODytrl3mhPoRcGbDXVJyt0Q1t" crossorigin="anonymous"></script>
</head>
<body>
  <div id="app">Memuatkan...</div>

  <script>
    FHIR.oauth2.ready()
      .then(client => {
        // Aplikasi sudah dibenarkan
        return client.request("MedicationKnowledge/db00860");
      })
      .then(med => {
        document.getElementById('app').innerHTML =
          '<h1>' + med.code.coding[0].display + '</h1>';
      });
  </script>
</body>
</html>
```

---

## Dokumen Rujukan

| Dokumen | Penerangan | Pautan |
|---------|------------|--------|
| **SMART App Launch IG** | Panduan pelaksanaan rasmi | [HL7](https://hl7.org/fhir/smart-app-launch/) |
| **FHIR R4 Spec** | Spesifikasi FHIR | [hl7.org/fhir](https://hl7.org/fhir/R4/) |
| **OAuth 2.0** | Spesifikasi kebenaran | [RFC 6749](https://tools.ietf.org/html/rfc6749) |

---

## Sokongan

Untuk bantuan dengan integrasi:

- **GitHub Issues**: [MyTxGNN Issues](https://github.com/yao-care/MyTxGNN/issues)
- **Dokumentasi**: Halaman ini dan pautan berkaitan

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Sumber yang disenaraikan adalah untuk <strong>tujuan rujukan</strong>. Sila pastikan pematuhan dengan keperluan keselamatan organisasi anda sebelum menggunakan dalam persekitaran produksi.
<br><br>
<small>Kemas kini terakhir: 2026-03-03 | Pasukan Penyelidikan MyTxGNN</small>
</div>
