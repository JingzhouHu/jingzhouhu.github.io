---
layout: minimal-light
permalink: /
title: "Machine Learning Research"
excerpt: "Jingzhou Hu is an Applied Scientist at Amazon working on LLM systems, adaptive decision-making, identifiable representation learning, and optimization."
author_profile: false
redirect_from:
  - /about/
  - /about.html
  - /me/
  - /me/about/
  - /me/about.html
---

<div class="content-section bio" id="about" role="region" aria-labelledby="about-title">
  <h2 id="about-title">About me</h2>
  <p>I am an Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision-making. My research spans identifiable representation learning, non-convex optimization, and learning from partial feedback.</p>
  <p>I received my Ph.D. in Computer Science from the University of Florida, advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I received my bachelor’s degree from Nanjing University.</p>
</div>

<div class="content-section" id="publications" role="region" aria-labelledby="publications-title">
  <div class="section-heading"><h2 id="publications-title">Selected publications</h2><a class="text-link" href="{{ site.author.googlescholar | escape }}">All publications on Scholar ↗</a></div>
  {% include publication-list.html heading="h3" %}
</div>

<div class="content-section" id="research" role="region" aria-labelledby="research-title">
  <h2 id="research-title">Research interests</h2>
  <ul class="research-topics">
    <li><strong>Machine learning foundations.</strong> Identifiable representation learning, latent variable models, and non-convex optimization.</li>
    <li><strong>Adaptive decision systems.</strong> Contextual neural bandits, learning from partial feedback, and uncertainty-aware decisions.</li>
    <li><strong>LLM &amp; agentic reasoning.</strong> Routing, orchestration, evaluation, and control for systems built on large language models.</li>
  </ul>
</div>

<div class="content-section service-copy" id="service" role="region" aria-labelledby="service-title">
  <h2 id="service-title">Academic service</h2>
  <p><strong>Conference reviewer:</strong> NeurIPS, ICML, ICLR, AISTATS, AAAI, ICASSP, MLSP, IJCNN.</p>
  <p><strong>Journal reviewer:</strong> IEEE Transactions on Signal Processing; Journal of Machine Learning Research.</p>
</div>

{% assign more_page = site.pages | where: "url", "/more/" | first %}
{% if more_page %}<div class="content-section"><a class="text-link" href="{{ more_page.url | relative_url }}">Beyond research: mentoring and side projects ↗</a></div>{% endif %}
