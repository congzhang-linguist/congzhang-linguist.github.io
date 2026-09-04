---
layout: page
permalink: /resources/
title: resources
description: Some resources that I publish or find useful
years: [2026, 2023, 2022, 2021, 2020, 2019, 2018, 2015, 2014]
nav: true
nav_order: 6
---

<style>
  /* ---------- Filters ---------- */
  .resources-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 0.8rem;
    padding-bottom: 0.9rem;
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

  .count-label {
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    margin: 0 0 1.3rem 0;
  }

  /* ---------- Grid ---------- */
  .resources-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .resource-card {
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 12px;
    padding: 1.25rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
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

  .resource-card.hidden {
    display: none;
  }

  /* ---------- Card heading + visual identity ---------- */
  .resource-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 0.85rem;
  }

  .resource-identity {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    min-width: 0;
    flex: 1;
  }

  .resource-mark {
    width: 52px;
    height: 52px;
    flex: 0 0 52px;
    border-radius: 12px;
    border: 1px solid var(--global-divider-color);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .resource-card[data-preview-image] .resource-mark,
  .resource-card[data-preview-image] .resource-title {
    cursor: zoom-in;
  }

  .resource-card[data-preview-image]:hover .resource-mark {
    transform: scale(1.04);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.10);
  }

  .resource-mark svg {
    width: 25px;
    height: 25px;
    stroke-width: 1.8;
  }

  .resource-mark img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    padding: 4px;
  }

  .resource-logo-mark {
    border: 0;
    background: transparent;
    overflow: visible;
  }

  .resource-logo-mark img {
    padding: 0;
  }

  /* Generic resource icons are deliberately neutral.
     The original coloured category badges are unchanged. */
  .mark-repo,
  .mark-package,
  .mark-webapp,
  .mark-dataset,
  .mark-tutorial {
    background: var(--global-card-bg-color);
    color: var(--global-text-color-light);
  }

  .resource-card:hover .mark-repo,
  .resource-card:hover .mark-package,
  .resource-card:hover .mark-webapp,
  .resource-card:hover .mark-dataset,
  .resource-card:hover .mark-tutorial {
    color: var(--global-theme-color);
    border-color: var(--global-theme-color);
  }

  .resource-heading {
    min-width: 0;
    padding-top: 1px;
  }

  .resource-title {
    font-size: 1.08rem;
    font-weight: 600;
    line-height: 1.3;
    color: var(--global-text-color);
    margin-bottom: 0.25rem;
  }

  .resource-title a {
    color: inherit;
    text-decoration: none;
  }

  .resource-title a:hover {
    color: var(--global-theme-color);
  }

  .resource-meta {
    font-size: 0.75rem;
    line-height: 1.35;
    color: var(--global-text-color-light);
    font-weight: 400;
  }

  /* ---------- Badges ---------- */
  .resource-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    flex-shrink: 0;
    font-size: 0.68rem;
    padding: 0.2rem 0.65rem;
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

  .badge-tutorial {
    background: #fff0db;
    color: #b45309;
    border: 0.5px solid #ffe2bf;
  }

  .badge-dataset {
    background: #e0f2e9;
    color: #0a5c3e;
    border: 0.5px solid #bbdfcd;
  }

  .badge-package {
    background: #f1e6ff;
    color: #5b21b6;
    border: 0.5px solid #e2ceff;
  }

  .badge-webapp {
    background: #ffe4ed;
    color: #a11d5b;
    border: 0.5px solid #ffcbd9;
  }

  html[data-theme='dark'] .badge-repo {
    background: #1e2a4a;
    color: #93c5fd;
    border-color: #374151;
  }

  html[data-theme='dark'] .badge-tutorial {
    background: #3b2a1a;
    color: #fbbf24;
    border-color: #4a3a2a;
  }

  html[data-theme='dark'] .badge-dataset {
    background: #1a3a2a;
    color: #6ee7b7;
    border-color: #2a4a3a;
  }

  html[data-theme='dark'] .badge-package {
    background: #2a1a4a;
    color: #c4b5fd;
    border-color: #3a2a5a;
  }

  html[data-theme='dark'] .badge-webapp {
    background: #4a1a2a;
    color: #f9a8d4;
    border-color: #5a2a3a;
  }

  /* ---------- Card body ---------- */
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

  /* ---------- Hover preview ---------- */
  .preview-tooltip {
    position: fixed;
    width: min(340px, calc(100vw - 24px));
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 12px;
    padding: 9px;
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.16);
    z-index: 10000;
    pointer-events: none;
    opacity: 0;
    visibility: hidden;
    transform: translateY(4px);
    transition: opacity 0.15s ease, transform 0.15s ease, visibility 0.15s;
  }

  .preview-tooltip.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .preview-tooltip img {
    width: 100%;
    max-height: 260px;
    object-fit: contain;
    border-radius: 8px;
    display: block;
    background: white;
  }

  .preview-tooltip-label {
    font-size: 0.72rem;
    color: var(--global-text-color-light);
    margin-top: 7px;
    text-align: center;
  }

  /* Don't try to recreate desktop hover on touch devices. */
  @media (hover: none), (pointer: coarse) {
    .preview-tooltip {
      display: none !important;
    }

    .resource-card[data-preview-image] .resource-mark,
    .resource-card[data-preview-image] .resource-title {
      cursor: default;
    }
  }

  @media (max-width: 520px) {
    .resources-grid {
      grid-template-columns: 1fr;
    }

    .resource-card {
      padding: 1rem;
    }

    .resource-mark {
      width: 46px;
      height: 46px;
      flex-basis: 46px;
    }

    .resource-badge {
      font-size: 0.62rem;
      padding: 0.18rem 0.55rem;
    }
  }
</style>

<!-- Reusable SVG symbols -->
<svg aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">
  <symbol id="icon-code" viewBox="0 0 24 24">
    <polyline points="16 18 22 12 16 6"></polyline>
    <polyline points="8 6 2 12 8 18"></polyline>
  </symbol>

  <symbol id="icon-package" viewBox="0 0 24 24">
    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
    <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
    <line x1="12" y1="22.08" x2="12" y2="12"></line>
  </symbol>

  <symbol id="icon-app" viewBox="0 0 24 24">
    <rect x="3" y="4" width="18" height="16" rx="2"></rect>
    <line x1="3" y1="9" x2="21" y2="9"></line>
    <circle cx="7" cy="6.5" r="0.5"></circle>
    <circle cx="10" cy="6.5" r="0.5"></circle>
  </symbol>

  <symbol id="icon-keyboard" viewBox="0 0 24 24">
    <rect x="2" y="5" width="20" height="14" rx="2"></rect>
    <line x1="6" y1="9" x2="6.01" y2="9"></line>
    <line x1="10" y1="9" x2="10.01" y2="9"></line>
    <line x1="14" y1="9" x2="14.01" y2="9"></line>
    <line x1="18" y1="9" x2="18.01" y2="9"></line>
    <line x1="6" y1="13" x2="6.01" y2="13"></line>
    <line x1="10" y1="13" x2="10.01" y2="13"></line>
    <line x1="14" y1="13" x2="14.01" y2="13"></line>
    <line x1="18" y1="13" x2="18.01" y2="13"></line>
    <line x1="8" y1="16" x2="16" y2="16"></line>
  </symbol>

  <symbol id="icon-book" viewBox="0 0 24 24">
    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
  </symbol>

  <symbol id="icon-data" viewBox="0 0 24 24">
    <ellipse cx="12" cy="5" rx="8" ry="3"></ellipse>
    <path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5"></path>
    <path d="M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6"></path>
  </symbol>

  <symbol id="icon-grid" viewBox="0 0 24 24">
    <rect x="3" y="3" width="7" height="7" rx="1"></rect>
    <rect x="14" y="3" width="7" height="7" rx="1"></rect>
    <rect x="3" y="14" width="7" height="7" rx="1"></rect>
    <rect x="14" y="14" width="7" height="7" rx="1"></rect>
  </symbol>

  <symbol id="icon-external" viewBox="0 0 24 24">
    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
    <polyline points="15 3 21 3 21 9"></polyline>
    <line x1="10" y1="14" x2="21" y2="3"></line>
  </symbol>
</svg>

<div class="resources-filters" aria-label="Filter resources">
  <button class="filter-btn active" data-filter="all" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="3"></circle>
      <path d="M19.4 15a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H5.78a1.65 1.65 0 0 0-1.51 1 1.65 1.65 0 0 0 .33 1.82l.03.03A10 10 0 0 0 12 17.66a10 10 0 0 0 6.37-2.63z"></path>
      <path d="M12 2v3"></path>
      <path d="M12 22v-3"></path>
    </svg>
    All
  </button>

  <button class="filter-btn" data-filter="repo" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <polyline points="16 18 22 12 16 6"></polyline>
      <polyline points="8 6 2 12 8 18"></polyline>
    </svg>
    Code
  </button>

  <button class="filter-btn" data-filter="webapp" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <rect x="2" y="3" width="20" height="14" rx="2"></rect>
      <line x1="8" y1="21" x2="16" y2="21"></line>
      <line x1="12" y1="17" x2="12" y2="21"></line>
    </svg>
    Web App
  </button>

  <button class="filter-btn" data-filter="tutorial" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
      <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
    </svg>
    Tutorial
  </button>

  <button class="filter-btn" data-filter="dataset" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <rect x="3" y="3" width="18" height="18" rx="2"></rect>
      <line x1="3" y1="9" x2="21" y2="9"></line>
      <line x1="3" y1="15" x2="21" y2="15"></line>
      <line x1="9" y1="21" x2="9" y2="9"></line>
    </svg>
    Dataset
  </button>

  <button class="filter-btn" data-filter="package" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
    </svg>
    Package
  </button>
</div>

<div class="count-label"><span id="resource-count">15</span> resources</div>

<div class="resources-grid" id="resources-grid">

  <!-- 1. Praat Scripts -->
  <div class="resource-card" data-type="repo">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-repo" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-code"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://github.com/congzhang365/Praat" target="_blank" rel="noopener">Praat Scripts</a>
          </div>
          <div class="resource-meta">Cong Zhang · GitHub</div>
        </div>
      </div>
      <span class="resource-badge badge-repo">Repository</span>
    </div>
    <div class="resource-description">Various Praat scripts for phonetic and speech analysis.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/congzhang365/Praat" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- 2. Python Scripts -->
  <div class="resource-card" data-type="repo">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-repo" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-code"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://github.com/congzhang365/PythonScripts" target="_blank" rel="noopener">Python Scripts</a>
          </div>
          <div class="resource-meta">Cong Zhang · GitHub</div>
        </div>
      </div>
      <span class="resource-badge badge-repo">Repository</span>
    </div>
    <div class="resource-description">Various Python scripts for speech, language and data-processing tasks.</div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/congzhang365/PythonScripts" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- 3. rhythm.metrics -->
  <div
    class="resource-card"
    data-type="package"
    data-preview-image="https://raw.githubusercontent.com/congzhang365/rhythm.metrics/main/man/figures/logo.png"
    data-preview-title="rhythm.metrics"
  >
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark resource-logo-mark" aria-hidden="true">
          <!-- Uses the published logo directly, it is shown here. The JS adds a fallback if it cannot load. -->
          <img
            class="resource-logo"
            src="https://raw.githubusercontent.com/congzhang365/rhythm.metrics/main/man/figures/logo.png"
            alt=""
          >
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://congzhang365.github.io/rhythm.metrics/" target="_blank" rel="noopener">rhythm.metrics</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2022 · R package · CRAN 2026</div>
        </div>
      </div>
      <span class="resource-badge badge-package">Package</span>
    </div>
    <div class="resource-description">
      R package for calculating and visualising speech rhythm and timing metrics, including ΔC/ΔV, Varco, %V, rPVI-C and nPVI-V. 
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://congzhang365.github.io/rhythm.metrics/" target="_blank" rel="noopener">Documentation</a>
      <a class="resource-link" href="https://CRAN.R-project.org/package=rhythm.metrics" target="_blank" rel="noopener">CRAN</a>
      <a class="resource-link" href="https://github.com/congzhang365/rhythm.metrics" target="_blank" rel="noopener">GitHub</a>
      <a class="resource-link" href="https://osf.io/kfnzt" target="_blank" rel="noopener">Manual</a>
    </div>
  </div>


  <!-- shinytone web app -->
  <div
    class="resource-card"
    data-type="webapp"
    data-preview-image="https://raw.githubusercontent.com/chenchenzi/citationtone_hub/main/inst/app/www/shinytone.svg"
    data-preview-title="shinytone web app"
  >
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark resource-logo-mark" aria-hidden="true">
          <img
            class="resource-logo"
            src="https://raw.githubusercontent.com/chenchenzi/citationtone_hub/main/inst/app/www/shinytone.svg"
            alt=""
          >
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://chenzixu.shinyapps.io/shinytone/" target="_blank" rel="noopener">shinytone web app</a>
          </div>
          <div class="resource-meta">Chenzi Xu &amp; Cong Zhang · 2026 · Shiny app</div>
        </div>
      </div>
      <span class="resource-badge badge-webapp">Web App</span>
    </div>
    <div class="resource-description">
      Zero-install interface for citation-tone workflows: f0 extraction, inspection, normalisation, contour visualisation, modelling and Chao tone summaries.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://chenzixu.shinyapps.io/shinytone/" target="_blank" rel="noopener">
        <svg fill="none" stroke="currentColor"><use href="#icon-external"></use></svg>
        Open App
      </a>
      <a class="resource-link" href="https://chenchenzi.github.io/citationtone_hub/" target="_blank" rel="noopener">Documentation</a>
      <a class="resource-link" href="https://github.com/chenchenzi/citationtone_hub" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- shinytone R package -->
  <div
    class="resource-card"
    data-type="package"
    data-preview-image="https://raw.githubusercontent.com/chenchenzi/citationtone_hub/main/man/figures/logo.png"
    data-preview-title="shinytone R package"
  >
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark resource-logo-mark" aria-hidden="true">
          <img
            class="resource-logo"
            src="https://raw.githubusercontent.com/chenchenzi/citationtone_hub/main/man/figures/logo.png"
            alt=""
          >
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://chenchenzi.github.io/citationtone_hub/" target="_blank" rel="noopener">shinytone R package</a>
          </div>
          <div class="resource-meta">Chenzi Xu &amp; Cong Zhang · 2026 · R package</div>
        </div>
      </div>
      <span class="resource-badge badge-package">Package</span>
    </div>
    <div class="resource-description">
      Local R package for citation-tone analysis, supporting scripted and batch workflows as well as launching the Shiny interface offline.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://chenchenzi.github.io/citationtone_hub/" target="_blank" rel="noopener">Documentation</a>
      <a class="resource-link" href="https://chenchenzi.github.io/citationtone_hub/articles/shinytone.html" target="_blank" rel="noopener">Get Started</a>
      <a class="resource-link" href="https://github.com/chenchenzi/citationtone_hub" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- 4. Charsiu Phonetic Aligner -->
  <div class="resource-card" data-type="package">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-package" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-package"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://github.com/lingjzhu/charsiu" target="_blank" rel="noopener">Charsiu Phonetic Aligner</a>
          </div>
          <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-package">Package</span>
    </div>
    <div class="resource-description">
      A multilingual phonetic aligner supporting both forced alignment and textless phonetic alignment.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/lingjzhu/charsiu" target="_blank" rel="noopener">GitHub</a>
      <a class="resource-link" href="https://arxiv.org/pdf/2110.03876" target="_blank" rel="noopener">Paper</a>
    </div>
  </div>

  <!-- 5. CharsiuG2P -->
  <div class="resource-card" data-type="package">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-package" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-package"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://github.com/lingjzhu/CharsiuG2P" target="_blank" rel="noopener">CharsiuG2P</a>
          </div>
          <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-package">Package</span>
    </div>
    <div class="resource-description">
      Transformer-based grapheme-to-phoneme resources and models for more than 100 languages.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/lingjzhu/CharsiuG2P" target="_blank" rel="noopener">GitHub</a>
      <a class="resource-link" href="https://www.isca-speech.org/archive/pdfs/interspeech_2022/zhu22_interspeech.pdf" target="_blank" rel="noopener">Paper</a>
    </div>
  </div>

  <!-- 6. IPA Flashcard -->
  <div class="resource-card" data-type="webapp">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-webapp" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-app"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://congzhang365.github.io/IPA_flashcard/" target="_blank" rel="noopener">IPA365 Flashcard</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2026</div>
        </div>
      </div>
      <span class="resource-badge badge-webapp">Web App</span>
    </div>
    <div class="resource-description">
      An interactive flashcard tool for learning IPA symbols, labels, pronunciation and examples.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://congzhang365.github.io/IPA_flashcard/" target="_blank" rel="noopener">
        <svg fill="none" stroke="currentColor"><use href="#icon-external"></use></svg>
        Open App
      </a>
      <a class="resource-link" href="https://github.com/congzhang365/IPA_flashcard" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- 7. IPA Keyboard -->
  <div class="resource-card" data-type="webapp">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-webapp" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-keyboard"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://congzhang365.github.io/IPA_keyboard/" target="_blank" rel="noopener">IPA365 Keyboard</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2026</div>
        </div>
      </div>
      <span class="resource-badge badge-webapp">Web App</span>
    </div>
    <div class="resource-description">
      An IPA keyboard for phonetics exams that deliberately hides three-term labels, so it does not give away answers.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://congzhang365.github.io/IPA_keyboard/" target="_blank" rel="noopener">
        <svg fill="none" stroke="currentColor"><use href="#icon-external"></use></svg>
        Open App
      </a>
      <a class="resource-link" href="https://github.com/congzhang365/IPA_keyboard" target="_blank" rel="noopener">GitHub</a>
    </div>
  </div>

  <!-- 8. CharsiuG2P dictionaries
       Fixed: this is now data-type="dataset", so the Dataset filter works correctly.
  -->
  <div class="resource-card" data-type="dataset">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-dataset" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-book"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://github.com/lingjzhu/CharsiuG2P/tree/main/dicts" target="_blank" rel="noopener">CharsiuG2P dictionaries</a>
          </div>
          <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-dataset">Dictionary</span>
    </div>
    <div class="resource-description">
      Pronunciation dictionaries for over 100 languages, collected for the CharsiuG2P project.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://github.com/lingjzhu/CharsiuG2P/tree/main/dicts" target="_blank" rel="noopener">Browse</a>
    </div>
  </div>

  <!-- 9. Phonological feature mapping -->
  <div class="resource-card" data-type="dataset">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-dataset" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-grid"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://zenodo.org/record/5553685" target="_blank" rel="noopener">Phonological feature mapping</a>
          </div>
          <div class="resource-meta">Cong Zhang, Huinan Zeng · 2021</div>
        </div>
      </div>
      <span class="resource-badge badge-dataset">Dictionary</span>
    </div>
    <div class="resource-description">
      Feature-to-phone mapping data used to train the FeatureTTS system.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://zenodo.org/record/5553685" target="_blank" rel="noopener">Zenodo</a>
    </div>
  </div>

  <!-- 10. MFA tutorial -->
  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-tutorial" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-book"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://osf.io/yu48g/" target="_blank" rel="noopener">MFA 2.0 Installation (Windows)</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-description">
      Step-by-step guide for installing Montreal Forced Aligner 2.0 on Windows, including Linux-on-Windows setup.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/yu48g/" target="_blank" rel="noopener">OSF</a>
      <a class="resource-link" href="https://osf.io/yu48g/download" target="_blank" rel="noopener">PDF</a>
    </div>
  </div>

  <!-- 11. REAPER tutorial -->
  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-tutorial" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-book"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://osf.io/bz5wk/" target="_blank" rel="noopener">Compiling REAPER on Windows</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-description">
      Guide for compiling and installing REAPER (Robust Epoch And Pitch EstimatoR) on Windows.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/bz5wk/" target="_blank" rel="noopener">OSF</a>
      <a class="resource-link" href="https://osf.io/bz5wk/download" target="_blank" rel="noopener">PDF</a>
    </div>
  </div>

  <!-- 12. P2FA tutorial -->
  <div class="resource-card" data-type="tutorial">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-tutorial" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-book"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://osf.io/542qj/" target="_blank" rel="noopener">P2FA Chinese on Windows</a>
          </div>
          <div class="resource-meta">Cong Zhang · 2018</div>
        </div>
      </div>
      <span class="resource-badge badge-tutorial">Tutorial</span>
    </div>
    <div class="resource-description">
      Tutorial for installing and using the Penn Forced Aligner for Mandarin Chinese on Windows.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://osf.io/542qj/" target="_blank" rel="noopener">OSF</a>
      <a class="resource-link" href="https://osf.io/542qj/download" target="_blank" rel="noopener">PDF</a>
    </div>
  </div>

  <!-- 13. CharsiuG2P multilingual corpora -->
  <div class="resource-card" data-type="dataset">
    <div class="resource-header">
      <div class="resource-identity">
        <div class="resource-mark mark-dataset" aria-hidden="true">
          <svg fill="none" stroke="currentColor"><use href="#icon-data"></use></svg>
        </div>
        <div class="resource-heading">
          <div class="resource-title">
            <a href="https://docs.google.com/spreadsheets/d/1Aq54Un6Q_Dj99_H1Y61iWnTB7xN0xgac5lg4sHU4Gdk/edit" target="_blank" rel="noopener">CharsiuG2P multilingual corpora</a>
          </div>
          <div class="resource-meta">Jian Zhu, Cong Zhang, David Jurgens · 2022</div>
        </div>
      </div>
      <span class="resource-badge badge-dataset">Dataset</span>
    </div>
    <div class="resource-description">
      Multilingual G2P training data for over 100 languages, compiled for the CharsiuG2P project.
    </div>
    <div class="resource-links">
      <a class="resource-link" href="https://docs.google.com/spreadsheets/d/1Aq54Un6Q_Dj99_H1Y61iWnTB7xN0xgac5lg4sHU4Gdk/edit" target="_blank" rel="noopener">Google Sheets</a>
    </div>
  </div>

</div>

<!-- One tooltip is reused by all cards that have data-preview-image -->
<div class="preview-tooltip" id="preview-tooltip" role="presentation" aria-hidden="true">
  <img id="preview-tooltip-image" alt="">
  <div class="preview-tooltip-label" id="preview-tooltip-label"></div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    /* ---------- Filter functionality ---------- */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.resource-card');
    const countSpan = document.getElementById('resource-count');

    function updateFilter() {
      const activeButton = document.querySelector('.filter-btn.active');
      const activeFilter = activeButton ? activeButton.dataset.filter : 'all';
      let visibleCount = 0;

      cards.forEach(card => {
        const shouldShow = activeFilter === 'all' || card.dataset.type === activeFilter;
        card.classList.toggle('hidden', !shouldShow);
        if (shouldShow) visibleCount++;
      });

      if (countSpan) countSpan.textContent = visibleCount;
    }

    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        filterButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        updateFilter();
      });
    });

    updateFilter();

    /* ---------- Logo fallback ---------- */
    function replaceBrokenLogo(img) {
      const mark = img.parentElement;
      if (!mark) return;

      img.remove();

      if (!mark.querySelector('svg')) {
        mark.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true"><path d="M3 12h3l2-6 4 12 3-9 2 3h4"></path></svg>';
      }
    }

    document.querySelectorAll('.resource-logo').forEach(img => {
      img.addEventListener('error', function () {
        replaceBrokenLogo(this);
      });

      /* Handles the case where the missing image failed before this listener was attached. */
      if (img.complete && img.naturalWidth === 0) {
        replaceBrokenLogo(img);
      }
    });

    /* ---------- Hover preview ---------- */
    const tooltip = document.getElementById('preview-tooltip');
    const tooltipImage = document.getElementById('preview-tooltip-image');
    const tooltipLabel = document.getElementById('preview-tooltip-label');

    if (!tooltip || !tooltipImage || !tooltipLabel) return;

    const hoverCapable = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
    if (!hoverCapable) return;

    let activeCard = null;

    function hidePreview() {
      tooltip.classList.remove('visible');
      tooltip.setAttribute('aria-hidden', 'true');
      activeCard = null;
    }

    function positionPreview(event) {
      const gap = 16;
      const tooltipWidth = tooltip.offsetWidth || 340;
      const tooltipHeight = tooltip.offsetHeight || 220;

      let left = event.clientX + gap;
      let top = event.clientY + gap;

      if (left + tooltipWidth > window.innerWidth - 12) {
        left = event.clientX - tooltipWidth - gap;
      }

      if (top + tooltipHeight > window.innerHeight - 12) {
        top = event.clientY - tooltipHeight - gap;
      }

      left = Math.max(12, left);
      top = Math.max(12, top);

      tooltip.style.left = left + 'px';
      tooltip.style.top = top + 'px';
    }

    document.querySelectorAll('.resource-card[data-preview-image]').forEach(card => {
      const triggers = card.querySelectorAll('.resource-mark, .resource-title');

      triggers.forEach(trigger => {
        trigger.addEventListener('mouseenter', function (event) {
          const src = card.dataset.previewImage;
          if (!src) return;

          activeCard = card;
          tooltipImage.src = src;
          tooltipImage.alt = card.dataset.previewTitle || '';
          tooltipLabel.textContent = card.dataset.previewTitle || '';
          tooltip.classList.add('visible');
          tooltip.setAttribute('aria-hidden', 'false');
          positionPreview(event);
        });

        trigger.addEventListener('mousemove', function (event) {
          if (activeCard === card) positionPreview(event);
        });

        trigger.addEventListener('mouseleave', hidePreview);
      });
    });

    tooltipImage.addEventListener('error', hidePreview);
    window.addEventListener('scroll', hidePreview, { passive: true });
  });
</script>
