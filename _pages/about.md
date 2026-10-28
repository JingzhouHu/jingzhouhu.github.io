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
    <div class="social-links" aria-label="Research and professional profiles">{% include profile-links.html %}</div>
  </div>
  <div class="hero-portrait">
    <div class="portrait-frame"><img src="{{ '/images/Hu.png' | relative_url }}" alt="Jingzhou Hu" width="450" height="540" fetchpriority="high" decoding="async"></div>
    <div class="portrait-caption"><span>Research &amp; applied science</span><span>Ph.D. · University of Florida</span></div>
  </div>
</section>

<section class="work-section" id="publications" aria-labelledby="publications-title">
  <div class="section-heading"><div><h2 id="publications-title">Selected publications</h2></div><a class="text-link" href="{{ site.author.googlescholar }}">All publications on Scholar <span aria-hidden="true">↗</span></a></div>
  {% include publication-list.html heading="h3" %}
</section>

<section class="research-section" id="research" aria-labelledby="research-title">
  <h2 id="research-title">Research interests</h2>
  <dl class="research-topics">
    <div><dt>Machine learning foundations</dt><dd>Identifiable representation learning, latent variable models, and non-convex optimization.</dd></div>
    <div><dt>Adaptive decision systems</dt><dd>Contextual neural bandits, learning from partial feedback, and uncertainty-aware decisions.</dd></div>
    <div><dt>LLM &amp; agentic reasoning</dt><dd>Routing, orchestration, evaluation, and control for systems built on large language models.</dd></div>
  </dl>
</section>

<section class="about-section" id="about" aria-labelledby="about-title">
  <div class="about-copy"><p class="eyebrow">Background</p><h2 id="about-title">About me<span>.</span></h2><p>I am an Applied Scientist at Amazon, working on LLM-based agentic reasoning systems and adaptive decision-making pipelines.</p><p>I received my Ph.D. in Computer Science from the University of Florida, advised by <a href="https://www.cise.ufl.edu/~kejun/">Prof. Kejun Huang</a>. Before joining UF, I received my bachelor’s degree from Nanjing University.</p>{% assign linkedin_link = site.author.links | where: "label", "LinkedIn" | first %}{% if linkedin_link %}<a class="text-link" href="{{ linkedin_link.url | escape }}">Connect on LinkedIn <span aria-hidden="true">↗</span></a>{% endif %}</div>
  <aside class="service-panel" aria-labelledby="service-title"><p class="eyebrow">Research community</p><h3 id="service-title">Academic service</h3><p class="service-label">Conference reviewer</p><p>NeurIPS · ICML · ICLR · AISTATS · AAAI · ICASSP · MLSP · IJCNN</p><p class="service-label">Journal reviewer</p><p>IEEE Transactions on Signal Processing<br>Journal of Machine Learning Research</p></aside>
</section>

{% assign more_page = site.pages | where: "url", "/more/" | first %}
{% if more_page %}<section class="more-section"><a class="text-link" href="{{ more_page.url | relative_url }}">Beyond research: mentoring and side projects <span aria-hidden="true">↗</span></a></section>{% endif %}
