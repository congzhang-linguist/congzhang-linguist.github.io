---
layout: page
permalink: /talks/
title: talks
description: A list of my presentations
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2012]
nav: true
nav_order: 4
---
<!-- _pages/publications.md -->
<div class="publications">

<h1>Invited talks & workshops</h1>
  {% bibliography -f invited %}


<h1>Conference presentations</h1>

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f talks -q @*[year={{y}}]* %}
{% endfor %}

</div>
