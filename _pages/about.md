---
permalink: /
title: "About Me"
excerpt: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## Bio

Applied Scientist at Amazon, building LLM-based agentic reasoning systems and adaptive decision pipelines, with prior research in theoretical machine learning: identifiable representation learning, signal processing, matrix factorization, and non-convex optimization. 

I received my Ph.D. from the Department of Computer &amp; Information Science &amp; Engineering (CISE) at the University of Florida, advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I obtained my bachelor’s degree from Nanjing University.

## Research Focus

<div class="focus-grid">
  <div class="focus-card">
    <h3>Machine Learning Foundations</h3>
    <p>Representation learning with identifiability guarantee, non-convex optimization, and latent variable modeling.</p>
  </div>
  <div class="focus-card">
    <h3>Adaptive Decision Systems</h3>
    <p>Contextual neural bandits, partial-feedback learning, and uncertainty-aware decision making pipelines for ML system at scale.</p>
  </div>
  <div class="focus-card">
    <h3>LLM &amp; Agentic Reasoning Systems</h3>
    <p>Routing, orchestration, and control strategies for multi-component agentic reasoning systems built on large language models.</p>
  </div>
</div>

## Selected Research &amp; System Contributions

### Published Research during my Ph.D.

- Established identifiability results for latent representation learning models, including bounded component analysis and dictionary learning.
- Developed non-convex optimization methods with theoretical guarantees fo identifiable latent representation learning problems.

### Applied ML System at Industry

- Built uncertainty-aware decision methods for recommendation settings with partial feedback.
- Developed routing and orchestration strategies for LLM-based agentic reasoning systems.
- Focused on system-level control design and decision quality under practical constraints.

## Selected Publications

<div class="publication-grid">
{% for pub in site.data.selected_publications %}
  <article class="publication-card">
    <img src="{{ pub.image }}" alt="Teaser for {{ pub.title }}" loading="lazy" />
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

## Links

- <a href="https://scholar.google.com/citations?user=T6FpaqMAAAAJ&hl=en">Google Scholar</a>
- <a href="https://www.linkedin.com/in/jingzhouhu/">LinkedIn</a>

## Previous Research Keywords (kept for continuity)

Machine Learning, Representation Learning, Unsupervised Learning, Optimization, Latent Variable Models, Non-convex Optimization, Uncertainty Estimation, Recommendation Systems, Reinforcement Learning, Large Language Models, Agentic System.

## Func Fact: A small historical curiosity.

I only later realized that one branch of my academic genealogy seems to pass through Poisson, Lagrange, and Laplace. This made my work on matrix-volume dictionary learning feel like a small historical echo: determinants, volume minimization, and Bernoulli-Gaussian sparse models had already appeared naturally in the work, before I knew about the lineage.
