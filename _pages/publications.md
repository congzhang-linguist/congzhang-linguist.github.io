---
layout: page
permalink: /publications/
title: publications
description: I will try my best to keep this page updated.
years: [2023, 2022, 2021, 2020, 2019, 2018, 2015, 2014, 2012]
nav: true
nav_order: 2
---
<!-- _pages/publications.md -->
<div class="publications">

<h1>Articles</h1>

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}


<h1>Preprints</h1>
{% bibliography -f preprints %}

</div>
