---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
excerpt: "Selected publications by Jingzhou Hu."
---

For a complete and current list, see my <a href="{{ site.author.googlescholar }}">Google Scholar profile</a>.

<div class="publication-grid">
{% for pub in site.data.selected_publications %}
  <article class="publication-card">
    <img src="{{ pub.image | relative_url }}" alt="Figure for {{ pub.title }}" loading="lazy" decoding="async" />
    <div class="publication-card__content">
      <h2><a href="{{ pub.url }}">{{ pub.title }}</a></h2>
      <p class="publication-meta">{{ pub.venue }} · {{ pub.year }}</p>
      <p>{{ pub.contribution }}</p>
    </div>
  </article>
{% endfor %}
</div>
