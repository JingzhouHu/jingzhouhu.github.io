---
permalink: /
title: "About Me"
excerpt: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## Hero

Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision systems, with prior research in identifiable representation learning and non-convex optimization.

## Research Focus

<div class="focus-grid">
  <div class="focus-card">
    <h3>Learning Foundations</h3>
    <p>Representation learning with identifiability, non-convex optimization, and signal-processing-grounded latent variable modeling.</p>
  </div>
  <div class="focus-card">
    <h3>Adaptive Decision Systems</h3>
    <p>Contextual bandits, partial-feedback learning, and uncertainty-aware decision pipelines for robust online adaptation.</p>
  </div>
  <div class="focus-card">
    <h3>LLM &amp; Agentic Reasoning Systems</h3>
    <p>Routing, orchestration, and control strategies for multi-component reasoning systems built on large language models.</p>
  </div>
</div>

## Selected Research &amp; System Contributions

### Published Research

I received my Ph.D. from the Department of Computer &amp; Information Science &amp; Engineering (CISE) at the University of Florida, advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I obtained my bachelor's degree from Nanjing University.

Representative technical directions include identifiability of latent variable models (including nonnegative matrix factorization, bounded and independent component analysis, and dictionary learning), as well as efficient non-convex optimization algorithms with provable guarantees.

### Applied/System Work

Current work centers on uncertainty-aware recommendation and adaptive routing/orchestration in LLM-based agentic systems, with emphasis on system-level methodology and decision quality under partial feedback.

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

## Service &amp; Mentorship

- Reviewer for major machine learning and signal processing venues.
- Mentoring students and early-career researchers on ML fundamentals, research execution, and applied experimentation.

## Links

- <a href="https://scholar.google.com/citations?user=T6FpaqMAAAAJ&hl=en">Google Scholar</a>
- <a href="https://github.com/JingzhouHu">GitHub</a>
- <a href="https://www.linkedin.com/in/jingzhou-hu-772a66208/">LinkedIn</a>

## Previous Research Keywords (kept for continuity)

Machine Learning, Representation Learning, Unsupervised Learning, Optimization, Latent Variable Models, Non-convex Optimization, Large Language Models, Foundation Models, Uncertainty Estimation, Recommendation Systems.
