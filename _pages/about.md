---
layout: profile
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

<section class="hero" aria-labelledby="profile-name">
  <div class="hero-copy">
    <p class="eyebrow"><span class="accent-line" aria-hidden="true"></span>Applied Scientist at Amazon</p>
    <h1 id="profile-name">Jingzhou Hu<span>.</span></h1>
    <p class="hero-statement">From identifiable representations<br class="desktop-break"> to adaptive decision-making.</p>
    <p class="hero-description">I work on machine learning foundations and LLM-based systems, with interests in representation learning, optimization, and adaptive decision-making.</p>
    <div class="hero-actions"><a class="primary-link" href="#publications">Explore my research <span aria-hidden="true">↗</span></a><a class="secondary-link" href="#about">About me <span aria-hidden="true">↓</span></a></div>
    <div class="social-links" aria-label="Research and professional profiles">{% include profile-links.html %}</div>
  </div>
  <div class="hero-portrait">
    <div class="portrait-frame"><img src="{{ '/images/Hu.png' | relative_url }}" alt="Jingzhou Hu" width="450" height="540" fetchpriority="high" decoding="async"></div>
    <div class="portrait-caption"><span>Research &amp; applied science</span><span>Ph.D. · University of Florida</span></div>
  </div>
</section>

<section class="research-section" id="research" aria-labelledby="research-title">
  <div class="section-heading"><div><p class="eyebrow">Research directions</p><h2 id="research-title">Foundations. Decisions. Reasoning.</h2></div><p class="section-intro">The questions behind my work, from latent representations to systems that learn and act.</p></div>
  <div class="research-grid">
    <article class="research-card"><span class="section-number" aria-hidden="true">01 /</span><h3>Machine learning<br> foundations</h3><p>Identifiable representation learning, latent variable models, and non-convex optimization.</p><div class="topic-label">Representation &amp; optimization</div></article>
    <article class="research-card"><span class="section-number" aria-hidden="true">02 /</span><h3>Adaptive<br> decision systems</h3><p>Contextual neural bandits, learning from partial feedback, and uncertainty-aware decisions.</p><div class="topic-label">Learning under uncertainty</div></article>
    <article class="research-card"><span class="section-number" aria-hidden="true">03 /</span><h3>LLM &amp; agentic<br> reasoning systems</h3><p>Routing, orchestration, evaluation, and control for systems built on large language models.</p><div class="topic-label">Reasoning &amp; orchestration</div></article>
  </div>
</section>

<section class="work-section" id="publications" aria-labelledby="publications-title">
  <div class="section-heading"><div><p class="eyebrow">Selected work</p><h2 id="publications-title">Research in focus<span>.</span></h2></div><a class="text-link" href="{{ site.author.googlescholar }}">All publications on Scholar <span aria-hidden="true">↗</span></a></div>
  {% include publication-list.html heading="h3" %}
</section>

<section class="about-section" id="about" aria-labelledby="about-title">
  <div class="about-copy"><p class="eyebrow">Background</p><h2 id="about-title">About me<span>.</span></h2><p>I am an Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision-making pipelines.</p><p>I received my Ph.D. in Computer Science from the University of Florida, advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I received my bachelor’s degree from Nanjing University.</p>{% assign linkedin_link = site.author.links | where: "label", "LinkedIn" | first %}{% if linkedin_link %}<a class="text-link" href="{{ linkedin_link.url | escape }}">Connect on LinkedIn <span aria-hidden="true">↗</span></a>{% endif %}</div>
  <aside class="service-panel" aria-labelledby="service-title"><p class="eyebrow">Research community</p><h3 id="service-title">Academic service</h3><p class="service-label">Conference reviewer</p><p>NeurIPS · ICML · ICLR · AISTATS · AAAI · ICASSP · MLSP · IJCNN</p><p class="service-label">Journal reviewer</p><p>IEEE Transactions on Signal Processing<br>Journal of Machine Learning Research</p></aside>
</section>

{% assign more_page = site.pages | where: "url", "/more/" | first %}
{% if more_page %}<section class="more-section"><a class="text-link" href="{{ more_page.url | relative_url }}">Beyond research: mentoring and side projects <span aria-hidden="true">↗</span></a></section>{% endif %}
