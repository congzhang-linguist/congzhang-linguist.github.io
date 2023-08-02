---
layout: page
permalink: /resources/
title: resources
description: Some resources that I publish or find useful
years: [2023, 2022, 2021, 2020, 2019, 2018, 2015, 2014]
nav: true
nav_order: 6
---
<!-- _pages/publications.md -->


<h1><font color="#F78769">Scripts repositories</font></h1>

I sometimes upload praat, python, and R scripts to my [github repository](https://github.com/congzhang365)
{% if site.data.repositories.github_repos %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}

<div class="publications">

<h1>Tools, datasets, and tutorials</h1>
{% bibliography -f resources %}


</div>

