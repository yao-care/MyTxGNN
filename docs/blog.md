---
layout: default
title: Case Studies
parent: Sumber
nav_order: 3
description: "MyTxGNN case study analyses and tutorials. Learn how AI predictions are validated with clinical evidence."
permalink: /blog/
---

# Case Studies & Tutorials

<p class="key-answer" data-question="How can I learn from MyTxGNN reports?">
Through real case analyses, understand how AI predictions are validated with clinical evidence, and how to evaluate drug repurposing feasibility. These tutorials will help you use the MyTxGNN platform more effectively.
</p>

<div class="key-takeaway">
Learn from L1 high-evidence cases to understand "what makes a good prediction", and from L2 cases to understand "the difference between prediction scores and evidence levels".
</div>

---

## Featured Case Analyses

### L1 Evidence Level (Highest Evidence)

These cases demonstrate how AI predictions are validated with comprehensive clinical evidence.

<div style="overflow-x: auto;">
<table>
<thead><tr><th>Drug</th><th>Topic</th><th>Key Learning</th></tr></thead>
<tbody>
{% for post in site.posts %}{% if post.categories contains 'L1' %}
<tr>
  <td><a href="{{ post.url | relative_url }}">{{ post.drugs | default: post.title | split: ':' | last }}</a></td>
  <td>{{ post.title | split: ':' | first }}</td>
  <td>{{ post.summary | default: post.description | truncate: 50 }}</td>
</tr>
{% endif %}{% endfor %}
</tbody>
</table>
</div>

### L2 Evidence Level

These cases help understand the difference between prediction scores and evidence levels.

<div style="overflow-x: auto;">
<table>
<thead><tr><th>Drug</th><th>Topic</th><th>Key Learning</th></tr></thead>
<tbody>
{% for post in site.posts %}{% if post.categories contains 'L2' %}
<tr>
  <td><a href="{{ post.url | relative_url }}">{{ post.drugs | default: post.title | split: ':' | last }}</a></td>
  <td>{{ post.title | split: ':' | first }}</td>
  <td>{{ post.summary | default: post.description | truncate: 50 }}</td>
</tr>
{% endif %}{% endfor %}
</tbody>
</table>
</div>

### Tutorials

<div style="overflow-x: auto;">
<table>
<thead><tr><th>Topic</th><th>Description</th></tr></thead>
<tbody>
{% for post in site.posts %}{% if post.categories contains 'Tutorial' %}
<tr>
  <td><a href="{{ post.url | relative_url }}">{{ post.title }}</a></td>
  <td>{{ post.description | truncate: 80 }}</td>
</tr>
{% endif %}{% endfor %}
</tbody>
</table>
</div>

---

## Latest Articles

{% if site.posts.size > 0 %}
{% for post in site.posts limit:5 %}
<article style="margin-bottom: 1.5rem; padding: 1.25rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid {% if post.categories contains 'L1' %}#2E7D32{% elsif post.categories contains 'L2' %}#66BB6A{% elsif post.categories contains 'Tutorial' %}#1976D2{% else %}#9E9E9E{% endif %};">
  <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1rem;">
    <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: #333;">{{ post.title }}</a>
  </h3>
  <p style="color: #666; margin: 0; font-size: 0.9rem;">
    <span style="background: {% if post.categories contains 'L1' %}#e8f5e9{% elsif post.categories contains 'L2' %}#e8f5e9{% elsif post.categories contains 'Tutorial' %}#e3f2fd{% else %}#f5f5f5{% endif %}; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.8rem; margin-right: 0.5rem;">{{ post.categories | first }}</span>
    {{ post.date | date: "%Y-%m-%d" }} | {{ post.description | truncate: 80 }}
  </p>
</article>
{% endfor %}
{% else %}
<p style="color: #666; font-style: italic;">Case studies and tutorials coming soon...</p>
{% endif %}

---

## All Articles

{% if site.posts.size > 0 %}
| Date | Category | Title |
|------|----------|-------|
{% for post in site.posts %}| {{ post.date | date: "%Y-%m-%d" }} | {{ post.categories | first }} | [{{ post.title }}]({{ post.url | relative_url }}) |
{% endfor %}
{% else %}
*Articles coming soon*
{% endif %}

---

## Quick Links

| Resource | Description |
|----------|-------------|
| [User Guide]({{ '/guide/' | relative_url }}) | Detailed report structure explanation |
| [Methodology]({{ '/methodology/' | relative_url }}) | Prediction and validation process |
| [High Evidence Drugs]({{ '/evidence-high/' | relative_url }}) | L1-L2 drug list |

---

<div class="disclaimer">
<strong>Note</strong><br>
Case analyses are for academic research reference only and do not constitute medical advice. Actual medication decisions should consult professional healthcare personnel.
</div>
