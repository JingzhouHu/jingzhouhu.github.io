---
permalink: /
title: "About Me"
excerpt: "Jingzhou Hu is an Applied Scientist at Amazon working on LLM systems, adaptive decision-making, identifiable representation learning, and optimization."
author_profile: true
redirect_from:
  - /about/
  - /about.html
  - /me/
  - /me/about/
  - /me/about.html
---

I am an Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision-making pipelines. My research spans identifiable representation learning, signal processing, matrix factorization, contextual bandits, and non-convex optimization.

I received my Ph.D. from the Department of Computer &amp; Information Science &amp; Engineering (CISE) at the University of Florida, where I was advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I received my bachelor’s degree from Nanjing University.

## Selected Publications

{% include publication-list.html heading="h3" %}

<p><a href="{{ site.author.googlescholar }}">Full publication list on Google Scholar →</a></p>

## Research Focus

<div class="focus-grid">
  <div class="focus-card">
    <h3>Machine Learning Foundations</h3>
    <p>Representation learning with identifiability guarantees, non-convex optimization, and latent variable modeling.</p>
  </div>
  <div class="focus-card">
    <h3>Adaptive Decision Systems</h3>
    <p>Contextual neural bandits, learning from partial feedback, and uncertainty-aware decision-making for ML systems at scale.</p>
  </div>
  <div class="focus-card">
    <h3>LLM &amp; Agentic Reasoning Systems</h3>
    <p>Routing, orchestration, evaluation, and control for multi-component systems built on large language models.</p>
  </div>
</div>

## Academic Service

- Conference reviewer: NeurIPS, ICML, ICLR, AISTATS, AAAI, ICASSP, MLSP, IJCNN.
- Journal reviewer: IEEE Transactions on Signal Processing (TSP), Journal of Machine Learning Research (JMLR).

{% assign more_page = site.pages | where: "url", "/more/" | first %}
{% if more_page %}
## Beyond Research

[More about mentoring and side projects →]({{ more_page.url | relative_url }})
{% endif %}

## Links

- <a href="https://scholar.google.com/citations?user=T6FpaqMAAAAJ&hl=en">Google Scholar</a>
- <a href="https://www.linkedin.com/in/jingzhouhu/">LinkedIn</a>
