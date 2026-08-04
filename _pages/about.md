---
permalink: /
title: "About Me"
excerpt: "Jingzhou Hu is an Applied Scientist at Amazon working on LLM systems, adaptive decision-making, identifiable representation learning, and optimization."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## Bio

I am an Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision-making pipelines. My research spans identifiable representation learning, signal processing, matrix factorization, contextual bandits, and non-convex optimization.

I received my Ph.D. from the Department of Computer &amp; Information Science &amp; Engineering (CISE) at the University of Florida, where I was advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I received my bachelor’s degree from Nanjing University.

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

## Selected Research &amp; System Contributions

### Research

- Established identifiability results for latent representation learning models, including bounded component analysis and dictionary learning.
- Developed non-convex optimization methods with theoretical guarantees for identifiable latent representation learning problems.

### Applied ML Systems

- Built uncertainty-aware decision methods for recommendation systems with partial feedback.
- Developed routing and orchestration strategies for LLM-based systems.
- Worked on system-level control and decision quality under practical constraints.

## Selected Publications

<div class="publication-grid">
{% for pub in site.data.selected_publications %}
  <article class="publication-card">
    <img src="{{ pub.image | relative_url }}" alt="Figure for {{ pub.title }}" loading="lazy" decoding="async" />
    <div class="publication-card__content">
      <h3><a href="{{ pub.url }}">{{ pub.title }}</a></h3>
      <p class="publication-meta">{{ pub.venue }} · {{ pub.year }}</p>
      <p>{{ pub.contribution }}</p>
    </div>
  </article>
{% endfor %}
</div>

## Academic Service

- Conference reviewer: NeurIPS, ICML, ICLR, AISTATS, AAAI, ICASSP, MLSP, IJCNN.
- Journal reviewer: IEEE Transactions on Signal Processing (TSP), Journal of Machine Learning Research (JMLR).

## Beyond Research

<div class="more-panel">
  <div>
    <p class="more-panel__eyebrow">Mentoring · Side Projects · Other Interests</p>
    <p>A separate, lightweight page leaves room for work and interests that do not fit naturally into a research summary.</p>
  </div>
  <a class="more-panel__link" href="{{ '/more/' | relative_url }}">More about me <span aria-hidden="true">→</span></a>
</div>

## Links

- <a href="https://scholar.google.com/citations?user=T6FpaqMAAAAJ&hl=en">Google Scholar</a>
- <a href="https://www.linkedin.com/in/jingzhouhu/">LinkedIn</a>
