---
layout: default
title: Laporan Ubat
nav_order: 4
has_children: true
description: "Layari 508 laporan pengesahan penggunaan semula ubat mengikut tahap bukti L1-L5."
---

# Laporan Ubat

<p style="font-size: 1.1rem; color: #666; margin-bottom: 1.5rem;">
Layari <strong>508</strong> laporan pengesahan penggunaan semula ubat mengikut tahap bukti
</p>

<style>
.drug-dist-container {
  margin: 2rem 0;
}
.drug-dist-bar {
  display: flex;
  height: 32px;
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.drug-dist-bar a {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.85rem;
  text-decoration: none;
  transition: filter 0.2s, transform 0.2s;
}
.drug-dist-bar a:hover {
  filter: brightness(1.1);
  transform: scaleY(1.1);
}
.dist-high { background: linear-gradient(135deg, #2E7D32, #4CAF50); }
.dist-medium { background: linear-gradient(135deg, #F9A825, #FDD835); color: #333 !important; }
.dist-low { background: linear-gradient(135deg, #9E9E9E, #BDBDBD); }

.drug-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}
.drug-card {
  display: flex;
  align-items: center;
  padding: 1.25rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  border-left: 5px solid;
}
.drug-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
}
.drug-card.high { border-color: #2E7D32; }
.drug-card.medium { border-color: #F9A825; }
.drug-card.low { border-color: #9E9E9E; }

.drug-card-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  flex-shrink: 0;
}
.drug-card.high .drug-card-icon { background: #E8F5E9; }
.drug-card.medium .drug-card-icon { background: #FFF8E1; }
.drug-card.low .drug-card-icon { background: #F5F5F5; }

.drug-card-count {
  font-size: 1.75rem;
  font-weight: 700;
  line-height: 1;
}
.drug-card.high .drug-card-count { color: #2E7D32; }
.drug-card.medium .drug-card-count { color: #F9A825; }
.drug-card.low .drug-card-count { color: #757575; }

.drug-card-info {
  flex: 1;
}
.drug-card-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: #333;
}
.drug-card-desc {
  font-size: 0.875rem;
  color: #666;
}
.drug-card-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  margin-left: auto;
}
.drug-card.high .drug-card-badge { background: #E8F5E9; color: #2E7D32; }
.drug-card.medium .drug-card-badge { background: #FFF8E1; color: #F57F17; }
.drug-card.low .drug-card-badge { background: #F5F5F5; color: #757575; }
</style>

<div class="drug-dist-container">
  <div class="drug-dist-bar">
    <a href="{{ '/evidence-high' | relative_url }}" class="dist-high" style="width: 5%;" title="Bukti Tinggi: L1-L2">L1-L2</a>
    <a href="{{ '/evidence-medium' | relative_url }}" class="dist-medium" style="width: 15%;" title="Bukti Sederhana: L3">L3</a>
    <a href="{{ '/evidence-low' | relative_url }}" class="dist-low" style="width: 80%;" title="Ramalan Model Sahaja: L4-L5">L4-L5</a>
  </div>

  <div class="drug-cards">
    <a href="{{ '/evidence-high' | relative_url }}" class="drug-card high">
      <div class="drug-card-icon">
        <span class="drug-card-count">L1-L2</span>
      </div>
      <div class="drug-card-info">
        <div class="drug-card-title">Bukti Tinggi</div>
        <div class="drug-card-desc">Sokongan ujian klinikal, keutamaan untuk penilaian</div>
      </div>
      <span class="drug-card-badge">L1-L2</span>
    </a>

    <a href="{{ '/evidence-medium' | relative_url }}" class="drug-card medium">
      <div class="drug-card-icon">
        <span class="drug-card-count">L3</span>
      </div>
      <div class="drug-card-info">
        <div class="drug-card-title">Bukti Sederhana</div>
        <div class="drug-card-desc">Bukti literatur, memerlukan penyelidikan lanjut</div>
      </div>
      <span class="drug-card-badge">L3</span>
    </a>

    <a href="{{ '/evidence-low' | relative_url }}" class="drug-card low">
      <div class="drug-card-icon">
        <span class="drug-card-count">L4-L5</span>
      </div>
      <div class="drug-card-info">
        <div class="drug-card-title">Ramalan Model Sahaja</div>
        <div class="drug-card-desc">Hasil ramalan AI, rujukan arah penyelidikan</div>
      </div>
      <span class="drug-card-badge">L4-L5</span>
    </a>
  </div>
</div>

<p style="text-align: center; margin-top: 2rem;">
  <a href="{{ '/drugs/' | relative_url }}" style="display: inline-block; padding: 0.75rem 2rem; background: #2E7D32; color: white; text-decoration: none; border-radius: 8px; font-weight: 600;">Lihat Senarai Penuh Ubat</a>
</p>
