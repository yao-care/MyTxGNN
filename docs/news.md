---
layout: default
title: Berita Kesihatan
nav_order: 3
description: "Pemantauan berita kesihatan automatik untuk ubat dan indikasi di Malaysia."
permalink: /news/
---

# Pemantauan Berita Kesihatan

<p class="key-answer" data-question="Apakah Pemantauan Berita Kesihatan MyTxGNN?">
<strong>Penjejakan automatik berita kesihatan</strong> yang menyebut <strong>kedua-dua ubat DAN penyakit</strong> dalam pangkalan data MyTxGNN. Berita yang hanya menyebut ubat atau penyakit sahaja tidak akan dipaparkan.
</p>

---

## Tapis Berita

<div class="filter-section">
  <label for="filter-select">Tapis mengikut:</label>
  <select id="filter-select">
    <option value="all">Semua Berita</option>
  </select>
  <button id="clear-filter" style="display: none;">Padam Tapis</button>
</div>

---

## Berita Terkini

<div id="news-list">
<p>Memuatkan berita...</p>
</div>

<div id="no-news-message" style="display: none;" class="no-news">
  <p>Tiada berita yang sepadan dengan tapisan ini.</p>
</div>

---

## Kata Kunci Trending

<div id="keyword-cloud">
<p>Memuatkan kata kunci...</p>
</div>

---

<div class="disclaimer">
<strong>Penafian</strong><br>
Berita di halaman ini dikumpul secara automatik oleh sistem dan adalah <strong>untuk rujukan penyelidikan sahaja</strong>, bukan nasihat perubatan. Kandungan berita datang dari pelbagai sumber media. MyTxGNN tidak bertanggungjawab terhadap kandungan berita. Sila ikuti arahan doktor anda untuk penggunaan ubat.
<br><br>
<small>Sumber data: CodeBlue, The Star, Malay Mail, NST, FMT | Kekerapan kemas kini: Setiap jam</small>
</div>

<style>
.filter-section {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.filter-section label {
  font-weight: 500;
}

.filter-section select {
  padding: 8px 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.95em;
  min-width: 200px;
  background: #fff;
}

.filter-section button {
  padding: 8px 16px;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9em;
}

.filter-section button:hover {
  background: #dc2626;
}

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

.news-card.hidden {
  display: none;
}

.news-title {
  font-size: 1.1em;
  font-weight: 600;
  margin-bottom: 8px;
  color: #24292e;
}

.news-title a {
  color: inherit;
  text-decoration: none;
}

.news-title a:hover {
  color: #0366d6;
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
  cursor: pointer;
  white-space: nowrap;
  transition: transform 0.1s;
}

.keyword-tag:hover {
  transform: scale(1.05);
}

.keyword-drug {
  background: #e3f2fd;
  color: #1565c0;
}

.keyword-indication {
  background: #f3e5f5;
  color: #7b1fa2;
}

.keyword-via {
  font-size: 0.75em;
  opacity: 0.7;
  margin-left: 4px;
}

.keyword-cloud-item {
  display: inline-block;
  padding: 4px 12px;
  margin: 4px;
  border-radius: 16px;
  background: #f0f0f0;
  color: #333;
  cursor: pointer;
  font-size: 0.9em;
  transition: background 0.2s;
}

.keyword-cloud-item:hover {
  background: #e0e0e0;
}

.keyword-cloud-item.active {
  background: #2196f3;
  color: white;
}

.no-news {
  text-align: center;
  padding: 40px;
  color: #586069;
  background: #f6f8fa;
  border-radius: 8px;
}
</style>

<script>
let allNewsItems = [];
let currentFilter = 'all';

document.addEventListener('DOMContentLoaded', function() {
  fetch('{{ "/data/news-index.json" | relative_url }}')
    .then(response => response.json())
    .then(data => {
      allNewsItems = data.news || [];
      renderNews(allNewsItems);
      renderKeywordCloud(allNewsItems);
      populateFilterOptions(allNewsItems);
    })
    .catch(err => {
      console.error('Gagal memuatkan berita:', err);
      document.getElementById('news-list').innerHTML =
        '<p class="no-news">Tidak dapat memuatkan data berita.</p>';
    });

  // Filter change handler
  document.getElementById('filter-select').addEventListener('change', function(e) {
    currentFilter = e.target.value;
    applyFilter();
    document.getElementById('clear-filter').style.display = currentFilter === 'all' ? 'none' : 'inline-block';
  });

  // Clear filter button
  document.getElementById('clear-filter').addEventListener('click', function() {
    document.getElementById('filter-select').value = 'all';
    currentFilter = 'all';
    applyFilter();
    this.style.display = 'none';
  });
});

function populateFilterOptions(newsItems) {
  const select = document.getElementById('filter-select');
  const keywords = new Map();

  newsItems.forEach(item => {
    if (item.keywords) {
      item.keywords.forEach(k => {
        const key = k.slug || k.name.toLowerCase();
        if (!keywords.has(key)) {
          keywords.set(key, {
            name: k.name,
            type: k.type,
            slug: k.slug
          });
        }
      });
    }
  });

  // Sort by name
  const sorted = Array.from(keywords.values()).sort((a, b) => a.name.localeCompare(b.name));

  // Group by type
  const drugs = sorted.filter(k => k.type === 'drug');
  const indications = sorted.filter(k => k.type === 'indication');

  if (drugs.length > 0) {
    const drugGroup = document.createElement('optgroup');
    drugGroup.label = 'Ubat';
    drugs.forEach(k => {
      const opt = document.createElement('option');
      opt.value = `drug:${k.slug}`;
      opt.textContent = k.name;
      drugGroup.appendChild(opt);
    });
    select.appendChild(drugGroup);
  }

  if (indications.length > 0) {
    const indGroup = document.createElement('optgroup');
    indGroup.label = 'Penyakit';
    indications.forEach(k => {
      const opt = document.createElement('option');
      opt.value = `indication:${k.name.toLowerCase()}`;
      opt.textContent = k.name;
      indGroup.appendChild(opt);
    });
    select.appendChild(indGroup);
  }
}

function applyFilter() {
  const cards = document.querySelectorAll('.news-card');
  let visibleCount = 0;

  cards.forEach(card => {
    if (currentFilter === 'all') {
      card.classList.remove('hidden');
      visibleCount++;
    } else {
      const cardKeywords = card.dataset.keywords || '';
      if (cardKeywords.includes(currentFilter)) {
        card.classList.remove('hidden');
        visibleCount++;
      } else {
        card.classList.add('hidden');
      }
    }
  });

  document.getElementById('no-news-message').style.display = visibleCount === 0 ? 'block' : 'none';

  // Update keyword cloud active state
  document.querySelectorAll('.keyword-cloud-item').forEach(item => {
    item.classList.remove('active');
    if (currentFilter !== 'all' && item.dataset.filter === currentFilter) {
      item.classList.add('active');
    }
  });
}

function setFilter(filterValue) {
  document.getElementById('filter-select').value = filterValue;
  currentFilter = filterValue;
  applyFilter();
  document.getElementById('clear-filter').style.display = filterValue === 'all' ? 'none' : 'inline-block';
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

    // Build keyword data for filtering
    const keywordData = [];
    let keywordsHtml = '';

    if (item.keywords && item.keywords.length > 0) {
      const seenKeywords = new Set();

      item.keywords.forEach(k => {
        const key = k.slug || k.name.toLowerCase();
        if (seenKeywords.has(key)) return;
        seenKeywords.add(key);

        const filterKey = k.type === 'drug' ? `drug:${k.slug}` : `indication:${k.name.toLowerCase()}`;
        keywordData.push(filterKey);

        if (k.type === 'drug') {
          const via = k.via_indication ? `<span class="keyword-via">(via ${k.via_indication})</span>` : '';
          keywordsHtml += `<span class="keyword-tag keyword-drug" onclick="setFilter('${filterKey}')">${k.name}${via}</span>`;
        } else {
          const label = k.keyword || k.name;
          keywordsHtml += `<span class="keyword-tag keyword-indication" onclick="setFilter('${filterKey}')">${label}</span>`;
        }
      });
    }

    html += `
      <div class="news-card" data-keywords="${keywordData.join(',')}">
        <div class="news-title">
          <a href="${item.sources[0]?.link || '#'}" target="_blank" rel="noopener">${item.title}</a>
        </div>
        <div class="news-meta">${dateStr}</div>
        <div class="news-sources">Sumber: ${sources}</div>
        ${keywordsHtml ? `<div class="news-keywords">${keywordsHtml}</div>` : ''}
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
        const key = k.type === 'drug' ? `drug:${k.slug}` : `indication:${k.name.toLowerCase()}`;
        const label = k.name;
        if (!keywordCounts[key]) {
          keywordCounts[key] = { label, count: 0, type: k.type, key };
        }
        keywordCounts[key].count++;
      });
    }
  });

  const sortedKeywords = Object.values(keywordCounts)
    .sort((a, b) => b.count - a.count)
    .slice(0, 15);

  if (sortedKeywords.length === 0) {
    container.innerHTML = '<p>Tiada data kata kunci buat masa ini</p>';
    return;
  }

  let html = sortedKeywords.map(k => {
    return `<span class="keyword-cloud-item" data-filter="${k.key}" onclick="setFilter('${k.key}')">${k.label} (${k.count})</span>`;
  }).join('');

  container.innerHTML = html;
}
</script>
