---
layout: default
title: Berita Kesihatan
nav_order: 3
description: "Pemantauan berita kesihatan automatik untuk 508 ubat dan indikasi mereka di Malaysia."
permalink: /news/
---

# Pemantauan Berita Kesihatan

<p class="key-answer" data-question="Apakah Pemantauan Berita Kesihatan MyTxGNN?">
<strong>Penjejakan automatik berita kesihatan berkaitan 508 ubat dan indikasi mereka</strong>. Apabila berita menyebut ubat atau penyakit dalam pangkalan data MyTxGNN, sistem mengumpul dan menyusunnya secara automatik, menyediakan pautan pantas ke halaman laporan ubat yang berkaitan.
</p>

---

## Berita Terkini

<div id="news-list">
<p>Memuatkan berita...</p>
</div>

---

## Kata Kunci Trending

<div id="keyword-cloud">
<p>Memuatkan kata kunci...</p>
</div>

---

## Layari Semua Ubat

<p>Klik pada nama ubat untuk melihat berita berkaitan:</p>

<div id="drug-list">
<p>Memuatkan senarai ubat...</p>
</div>

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Berita di halaman ini dikumpul secara automatik oleh sistem dan adalah <strong>untuk rujukan penyelidikan sahaja</strong>, bukan nasihat perubatan. Kandungan berita datang dari pelbagai sumber media. MyTxGNN tidak bertanggungjawab terhadap kandungan berita. Sila ikuti arahan doktor anda untuk penggunaan ubat.
<br><br>
<small>Sumber data: CodeBlue, The Star, Malay Mail | Kekerapan kemas kini: Setiap jam</small>
</div>

<style>
.news-card {
  border: 1px solid #e1e4e8;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: #fff;
}

.news-card:hover {
  border-color: #0366d6;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.news-title {
  font-size: 1.1em;
  font-weight: 600;
  margin-bottom: 8px;
  color: #24292e;
}

.news-meta {
  font-size: 0.85em;
  color: #586069;
  margin-bottom: 8px;
}

.news-sources {
  font-size: 0.85em;
}

.news-sources a {
  color: #0366d6;
  margin-right: 8px;
}

.news-keywords {
  margin-top: 8px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
}

.keyword-tag {
  display: inline-flex;
  align-items: center;
  padding: 4px 10px;
  border-radius: 14px;
  font-size: 0.85em;
  text-decoration: none;
  white-space: nowrap;
}

.keyword-drug {
  background: #e3f2fd;
  color: #1565c0;
}

.keyword-indication {
  background: #f3e5f5;
  color: #7b1fa2;
}

.keyword-cloud-item {
  display: inline-block;
  padding: 4px 12px;
  margin: 4px;
  border-radius: 16px;
  background: #f0f0f0;
  color: #333;
  text-decoration: none;
  font-size: 0.9em;
}

.keyword-cloud-item:hover {
  background: #e0e0e0;
}

.no-news {
  text-align: center;
  padding: 40px;
  color: #586069;
}

.drug-list-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 8px;
  margin-top: 16px;
}

.drug-list-item {
  display: block;
  padding: 8px 12px;
  background: #f6f8fa;
  border-radius: 6px;
  text-decoration: none;
  color: #24292e;
  font-size: 0.9em;
  transition: background 0.2s;
}

.drug-list-item:hover {
  background: #e1e4e8;
  text-decoration: none;
}

.drug-list-item.has-news {
  background: #e3f2fd;
  color: #1565c0;
}

.drug-list-item.has-news:hover {
  background: #bbdefb;
}
</style>

<script>
// Tukar nama kepada slug URL
function slugify(text) {
  return text.toLowerCase()
    .replace(/[\s_]+/g, '-')
    .replace(/[^\w\u4e00-\u9fff-]/g, '')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

document.addEventListener('DOMContentLoaded', function() {
  // Muat indeks berita
  fetch('{{ "/data/news-index.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      renderNews(data.news);
      renderKeywordCloud(data.news);
      loadDrugList(data.news);
    })
    .catch(err => {
      console.error('Gagal memuatkan berita:', err);
      document.getElementById('news-list').innerHTML =
        '<p class="no-news">Tidak dapat memuatkan data berita. Pemantauan berita sedang disediakan.</p>';
      loadDrugList([]);
    });
});

function loadDrugList(newsItems) {
  fetch('{{ "/data/drugs.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      const drugsWithNews = new Set();
      if (newsItems) {
        newsItems.forEach(item => {
          if (item.keywords) {
            item.keywords.forEach(k => {
              if (k.type === 'drug' && k.slug) {
                drugsWithNews.add(k.slug);
              }
            });
          }
        });
      }
      renderDrugList(data.drugs, drugsWithNews);
    })
    .catch(err => {
      console.error('Gagal memuatkan senarai ubat:', err);
      document.getElementById('drug-list').innerHTML =
        '<p>Tidak dapat memuatkan senarai ubat</p>';
    });
}

function renderNews(newsItems) {
  const container = document.getElementById('news-list');

  if (!newsItems || newsItems.length === 0) {
    container.innerHTML = '<p class="no-news">Tiada berita yang sepadan buat masa ini. Pemantauan berita aktif.</p>';
    return;
  }

  newsItems.sort((a, b) => new Date(b.published) - new Date(a.published));

  let html = '';

  newsItems.forEach(item => {
    const date = new Date(item.published);
    const dateStr = date.toLocaleDateString('ms-MY', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });

    const sources = item.sources.map(s =>
      `<a href="${s.link}" target="_blank" rel="noopener">${s.name} ↗</a>`
    ).join(' ');

    let keywords = '';
    const baseUrl = '{{ "/" | relative_url }}';
    if (item.keywords && item.keywords.length > 0) {
      const seenKeywords = new Set();
      const uniqueKeywords = item.keywords.filter(k => {
        const key = k.keyword || k.name;
        if (seenKeywords.has(key)) return false;
        seenKeywords.add(key);
        return true;
      });

      keywords = uniqueKeywords.map(k => {
        if (k.type === 'drug') {
          return `<a href="${baseUrl}news/${k.slug}/" class="keyword-tag keyword-drug">${k.name} →</a>`;
        } else {
          const indSlug = slugify(k.name);
          const indLabel = k.keyword || k.name;
          return `<a href="${baseUrl}news/${indSlug}/" class="keyword-tag keyword-indication">${indLabel} →</a>`;
        }
      }).join(' ');
    }

    html += `
      <div class="news-card">
        <div class="news-title">${item.title}</div>
        <div class="news-meta">${dateStr}</div>
        <div class="news-sources">Sumber: ${sources}</div>
        ${keywords ? `<div class="news-keywords">${keywords}</div>` : ''}
      </div>
    `;
  });

  container.innerHTML = html;
}

function renderKeywordCloud(newsItems) {
  const container = document.getElementById('keyword-cloud');

  if (!newsItems || newsItems.length === 0) {
    container.innerHTML = '<p>Tiada data kata kunci buat masa ini</p>';
    return;
  }

  const keywordCounts = {};

  newsItems.forEach(item => {
    if (item.keywords) {
      item.keywords.forEach(k => {
        const key = k.type === 'drug' ? k.slug : (k.keyword || k.name);
        const label = k.type === 'drug' ? k.name : (k.keyword || k.name);
        const slug = k.type === 'drug' ? k.slug : slugify(k.name);
        if (!keywordCounts[key]) {
          keywordCounts[key] = { label, count: 0, type: k.type, slug: slug };
        }
        keywordCounts[key].count++;
      });
    }
  });

  const sortedKeywords = Object.values(keywordCounts)
    .sort((a, b) => b.count - a.count)
    .slice(0, 20);

  if (sortedKeywords.length === 0) {
    container.innerHTML = '<p>Tiada data kata kunci buat masa ini</p>';
    return;
  }

  const baseUrl = '{{ "/" | relative_url }}';
  let html = sortedKeywords.map(k => {
    return `<a href="${baseUrl}news/${k.slug}/" class="keyword-cloud-item">${k.label} (${k.count})</a>`;
  }).join('');

  container.innerHTML = html;
}

function renderDrugList(drugs, drugsWithNews) {
  const container = document.getElementById('drug-list');

  if (!drugs || drugs.length === 0) {
    container.innerHTML = '<p>Tidak dapat memuatkan senarai ubat</p>';
    return;
  }

  drugs.sort((a, b) => a.name.localeCompare(b.name));

  const baseUrl = '{{ "/" | relative_url }}';
  let html = '<div class="drug-list-grid">';

  drugs.forEach(drug => {
    const hasNews = drugsWithNews.has(drug.slug);
    const className = hasNews ? 'drug-list-item has-news' : 'drug-list-item';
    html += `<a href="${baseUrl}news/${drug.slug}/" class="${className}">${drug.name}</a>`;
  });

  html += '</div>';
  container.innerHTML = html;
}
</script>
