---
layout: page
permalink: /resources/
title: resources
description: Some resources that I publish or find useful
years: [2023, 2022, 2021, 2020, 2019, 2018, 2015, 2014]
nav: true
nav_order: 6
---

<style>
  /* Filter bar styling - follows al-folio theme */
  .resources-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 2rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--global-divider-color);
  }

  .filter-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 18px;
    border-radius: 40px;
    border: 1px solid var(--global-divider-color);
    background: var(--global-card-bg-color);
    color: var(--global-text-color);
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .filter-btn:hover {
    background: var(--global-hover-color);
    border-color: var(--global-hover-border-color);
    transform: translateY(-1px);
  }

  .filter-btn.active {
    background: var(--global-theme-color);
    border-color: var(--global-theme-color);
    color: white;
  }

  .filter-btn svg {
    width: 14px;
    height: 14px;
  }

  .filter-btn.active svg {
    stroke: white;
  }

  /* Resource grid */
  .resources-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  /* Resource card - follows al-folio card styling */
  .resource-card {
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 12px;
    padding: 1.25rem;
    transition: all 0.2s ease;
    position: relative;
    height: 100%;
    display: flex;
    flex-direction: column;
  }

  .resource-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
    border-color: var(--global-theme-color);
  }

  .resource-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 0.75rem;
  }

  .resource-title {
    font-size: 1.1rem;
    font-weight: 600;
    line-height: 1.35;
    color: var(--global-text-color);
  }

  .resource-title a {
    color: inherit;
    text-decoration: none;
  }

  .resource-title a:hover {
    color: var(--global-theme-color);
  }

  /* Badge styles */
  .resource-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
    font-size: 0.7rem;
    padding: 0.2rem 0.7rem;
    border-radius: 50px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }

  .badge-repo {
    background: #eef2ff;
    color: #1e40af;
    border: 0.5px solid #cddcff;
  }

  html[data-theme='dark'] .badge-repo {
    background: #1e2a4a;
    color: #93c5fd;
    border-color: #374151;
  }

  .badge-tutorial {
    background: #fff0db;
    color: #b45309;
    border: 0.5px solid #ffe2bf;
  }

  html[data-theme='dark'] .badge-tutorial {
    background: #3b2a1a;
    color: #fbbf24;
    border-color: #4a3a2a;
  }

  .badge-dataset {
    background: #e0f2e9;
    color: #0a5c3e;
    border: 0.5px solid #bbdfcd;
  }

  html[data-theme='dark'] .badge-dataset {
    background: #1a3a2a;
    color: #6ee7b7;
    border-color: #2a4a3a;
  }

  .badge-package {
    background: #f1e6ff;
    color: #5b21b6;
    border: 0.5px solid #e2ceff;
  }

  html[data-theme='dark'] .badge-package {
    background: #2a1a4a;
    color: #c4b5fd;
    border-color: #3a2a5a;
  }

  .badge-webapp {
    background: #ffe4ed;
    color: #a11d5b;
    border: 0.5px solid #ffcbd9;
  }

  html[data-theme='dark'] .badge-webapp {
    background: #4a1a2a;
    color: #f9a8d4;
    border-color: #5a2a3a;
  }

  .resource-meta {
    font-size: 0.75rem;
    color: var(--global-text-color-light);
    margin-bottom: 0.75rem;
    font-weight: 400;
  }

  .resource-description {
    font-size: 0.85rem;
    line-height: 1.5;
    color: var(--global-text-color);
    margin-bottom: 1rem;
    flex-grow: 1;
  }

  .resource-links {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: auto;
  }

  .resource-link {
    font-size: 0.75rem;
    font-weight: 500;
    color: var(--global-text-color);
    text-decoration: none;
    border: 1px solid var(--global-divider-color);
    border-radius: 20px;
    padding: 0.3rem 0.8rem;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    transition: all 0.15s;
    background: var(--global-card-bg-color);
  }

  .resource-link:hover {
    background: var(--global-theme-color);
    border-color: var(--global-theme-color);
    color: white;
  }

  .resource-link svg {
    width: 12px;
    height: 12px;
  }

  .count-label {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    margin: 1rem 0 1.5rem 0;
  }

  .resource-card.hidden {
    display: none;
  }

  /* Tooltip preview - follows theme */
  .preview-tooltip {
    position: fixed;
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.15);
    z-index: 10000;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.2s;
    max-width: 340px;
  }

  .preview-tooltip.visible {
    opacity: 1;
  }

  .preview-tooltip img {
    width: 300px;
    max-width: 300px;
    border-radius: 8px;
    display: block;
  }

  .preview-tooltip-label {
    font-size: 0.7rem;
    color: var(--global-text-color-light);
    margin-top: 6px;
    text-align: center;
  }

  .preview-placeholder {
    width: 280px;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    color: var(--global-text-color-light);
    font-size: 0.75rem;
    background: var(--global-bg-color);
    border-radius: 8px;
    padding: 16px;
  }
</style>

<div class="resources-filters">
  <button class="filter-btn active" data-filter="all">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H5.78a1.65 1.65 0 0 0-1.51 1 1.65 1.65 0 0 0 .33 1.82l.03.03A10 10 0 0 0 12 17.66a10 10 0 0 0 6.37-2.63z"/><path d="M12 2v3"/><path d="M12 22v-3"/></svg>
    All
  </button>
  <button class="filter-btn" data-filter="repo">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
    Code
  </button>
  <button class="filter-btn" data-filter="webapp">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
    Web App
  </button>
  <button class="filter-btn" data-filter="tutorial">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
    Tutorial
  </button>
  <button class="filter-btn" data-filter="dataset">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
    Dataset
  </button>
  <button class="filter-btn" data-filter="package">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
    Package
  </button>
</div>

<div class="resources-grid" id="resources-grid">



  <!-- Code Repositories from your YAML -->
  {% for repo in site.data.repositories.github_repos %}
    {% assign repo_parts = repo.id | split: '/' %}
    {% assign repo_name = repo_parts[1] %}
    
    {% if repo.id contains "Praat" %}
    <div class="resource-card" data-type="repo">
      <div class="resource-header">
        <div class="resource-title">
          <a href="https://github.com/{{ repo.id }}" target="_blank">Praat Scripts</a>
        </div>
        <span class="resource-badge badge-repo">Repository</span>
      </div>
      <div class="resource-meta">Cong Zhang · GitHub</div>
      <div class="resource-description">{{ repo.recommendation }}</div>
      <div class="resource-links">
        <a class="resource-link" href="https://github.com/{{ repo.id }}" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
          GitHub
        </a>
      </div>
    </div>
    {% elsif repo.id contains "PythonScripts" %}
    <div class="resource-card" data-type="repo">
      <div class="resource-header">
        <div class="resource-title">
          <a href="https://github.com/{{ repo.id }}" target="_blank">Python Scripts</a>
        </div>
        <span class="resource-badge badge-repo">Repository</span>
      </div>
      
      
      <div class="resource-meta">Cong Zhang · GitHub</div>
      <div class="resource-description">{{ repo.recommendation }}</div>
      <div class="resource-links">
        <a class="resource-link" href="https://github.com/{{ repo.id }}" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
          GitHub
        </a>
      </div>
    </div>
    {% elsif repo.id contains "rhythm.metrics" %}
    <div class="resource-card" data-type="package">
      <div class="resource-header">
        <div class="resource-title">
          <a href="https://github.com/{{ repo.id }}" target="_blank">rhythm.metrics (R package)</a>
        </div>
        <span class="resource-badge badge-package">Package</span>
      </div>
      <div class="resource-meta">Cong Zhang · 2022</div>
      <div class="resource-description">{{ repo.recommendation }} Includes ΔC/ΔV, Varco, %V, rPVI_C, nPVI_V metrics.</div>
      <div class="resource-links">
        <a class="resource-link" href="https://github.com/{{ repo.id }}" target="_blank">GitHub</a>
        <a class="resource-link" href="https://osf.io/kfnzt" target="_blank">OSF</a>
        <a class="resource-link" href="https://osf.io/q6edh/download" target="_blank">PDF</a>
      </div>
    </div>
    {% elsif repo.id contains "charsiu" and repo.id contains "G2P" == false %}
    <div class="resource-card" data-type="package">
      <div class="resource-header">
        <div class="resource-title">
          <a href="https://github.com/{{ repo.id }}" target="_blank">Charsiu Phonetic Aligner</a>
        </div>
        <span class="resource-badge badge-package">Package</span>
      </div>
      <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
      <div class="resource-description">{{ repo.recommendation }} Handles both forced alignment and textless phonetic alignment.</div>
      <div class="resource-links">
        <a class="resource-link" href="https://github.com/{{ repo.id }}" target="_blank">GitHub</a>
        <a class="resource-link" href="https://arxiv.org/pdf/2110.03876" target="_blank">Paper</a>
      </div>
    </div>
    {% elsif repo.id contains "CharsiuG2P" %}
    <div class="resource-card" data-type="package">
      <div class="resource-header">
        <div class="resource-title">
          <a href="https://github.com/{{ repo.id }}" target="_blank">CharsiuG2P</a>
        </div>
        <span class="resource-badge badge-package">Package</span>
      </div>
      <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
      <div class="resource-description">{{ repo.recommendation }} Transformer-based grapheme-to-phoneme conversion.</div>
      <div class="resource-links">
        <a class="resource-link" href="https://github.com/{{ repo.id }}" target="_blank">GitHub</a>
        <a class="resource-link" href="https://www.isca-speech.org/archive/pdfs/interspeech_2022/zhu22_interspeech.pdf" target="_blank">Paper</a>
      </div>
    </div>
    {% endif %}
  {% endfor %}

  <!-- Web Apps -->
  <div class="resource-card" data-type="webapp">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://congzhang365.github.io/IPA_flashcard/" target="_blank">IPA Flashcard</a>
      </div>
      <span class="resource-badge badge-webapp">Web App</span>
    </div>
    <div class="resource-meta">Cong Zhang · 2026</div>
    <div class="resource-description">
      An interactive flashcard tool to learn IPA symbol, labels, pronunciation, and examples.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://congzhang365.github.io/IPA_flashcard/" target="_blank">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        Open App
      </a>
      <a class="resource-link" href="https://github.com/congzhang365/IPA_flashcard" target="_blank">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
        GitHub
      </a>
    </div>
  </div>


  <div class="resource-card" data-type="webapp">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://congzhang365.github.io/IPA_keyboard/" target="_blank">IPA Keyboard</a>
      </div>
      <span class="resource-badge badge-webapp">Web App</span>
    </div>
    <div class="resource-meta">Cong Zhang · 2026</div>
    <div class="resource-description">
      An IPA keyboard for phonetics exams that deliberately hides three-term labels, so it doesn't give away answers.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://congzhang365.github.io/IPA_keyboard/" target="_blank">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        Open App
      </a>
      <a class="resource-link" href="https://github.com/congzhang365/IPA_keyboard" target="_blank">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
        GitHub
      </a>
    </div>
  </div>


  <!-- Additional Resources (not in YAML) -->
  <div class="resource-card" data-type="webapp">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://github.com/lingjzhu/CharsiuG2P/tree/main/dicts" target="_blank">CharsiuG2P dictionaries</a>
      </div>
      <span class="resource-badge badge-dataset">Dictionary</span>
    </div>
    <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
    <div class="resource-description">Pronunciation dictionaries for over 100 languages, collected for the CharsiuG2P project.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/lingjzhu/CharsiuG2P/tree/main/dicts" target="_blank">Browse</a>
    </div>
  </div>


  <div class="resource-card" data-type="dataset">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://zenodo.org/record/5553685" target="_blank">Phonological feature mapping</a>
      </div>
      <span class="resource-badge badge-dataset">Dictionary</span>
    </div>
    <div class="resource-meta">Cong Zhang, Huinan Zeng · 2021</div>
    <div class="resource-description">Feature-to-phone mapping data used to train the FeatureTTS system.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://zenodo.org/record/5553685" target="_blank">Zenodo</a>
    </div>
  </div>

  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://osf.io/yu48g/" target="_blank">MFA 2.0 Installation (Windows)</a>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-meta">Cong Zhang · 2022</div>
    <div class="resource-description">Step-by-step guide for installing Montreal Forced Aligner 2.0 on Windows, including Linux-on-Windows setup.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/yu48g/" target="_blank">OSF</a>
      <a class="resource-link" href="https://osf.io/yu48g/download" target="_blank">PDF</a>
    </div>
  </div>

  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://osf.io/bz5wk/" target="_blank">Compiling REAPER on Windows</a>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-meta">Cong Zhang · 2022</div>
    <div class="resource-description">Guide for compiling and installing REAPER (Robust Epoch And Pitch EstimatoR) on Windows.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/bz5wk/" target="_blank">OSF</a>
      <a class="resource-link" href="https://osf.io/bz5wk/download" target="_blank">PDF</a>
    </div>
  </div>

  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://osf.io/542qj/" target="_blank">P2FA Chinese on Windows</a>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-meta">Cong Zhang · 2018</div>
    <div class="resource-description">Tutorial for installing and using the Penn Forced Aligner for Mandarin Chinese on Windows.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/542qj/" target="_blank">OSF</a>
      <a class="resource-link" href="https://osf.io/542qj/download" target="_blank">PDF</a>
    </div>
  </div>

  <div class="resource-card" data-type="dataset">
    <div class="resource-header">
      <div class="resource-title">
        <a href="https://docs.google.com/spreadsheets/d/1Aq54Un6Q_Dj99_H1Y61iWnTB7xN0xgac5lg4sHU4Gdk/edit" target="_blank">CharsiuG2P multilingual corpora</a>
      </div>
      <span class="resource-badge badge-dataset">Dataset</span>
    </div>
    <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
    <div class="resource-description">Multi-lingual G2P training data for over 100 languages, compiled for the CharsiuG2P project.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://docs.google.com/spreadsheets/d/1Aq54Un6Q_Dj99_H1Y61iWnTB7xN0xgac5lg4sHU4Gdk/edit" target="_blank">Google Sheets</a>
    </div>
  </div>

</div>

<script>
  // Filter functionality
  const filterButtons = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.resource-card');
  const countSpan = document.getElementById('resource-count');

  function updateFilter() {
    const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
    let visibleCount = 0;
    
    cards.forEach(card => {
      const cardType = card.dataset.type;
      if (activeFilter === 'all' || cardType === activeFilter) {
        card.classList.remove('hidden');
        visibleCount++;
      } else {
        card.classList.add('hidden');
      }
    });
    
    countSpan.textContent = visibleCount;
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateFilter();
    });
  });

  // Initial count
  updateFilter();
</script>