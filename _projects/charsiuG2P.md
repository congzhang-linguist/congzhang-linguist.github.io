---
layout: page
permalink: /project/charsiuG2P/
title: CharsiuG2P
description: Grapheme-to-phoneme conversion tool in 100 languages <br><br>
img: assets/img/project/charsiuG2P.png
importance: 1
category: speech technology
related_publications: zhu2022byt5-g2p
related_talks: zhu2022byt5-g2p-c
related_resources: zhu2022charsiug2p, zhu2022charsiug2p-dict, zhu2022charsiug2p-resources
---


CharsiuG2P is transformer based tool for grapheme-to-phoneme conversion in 100 languages. Given an orthographic word, CharsiuG2P predicts its pronunciation through a neural G2P model.


Github repo:

{% if "lingjzhu/CharsiuG2P" %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in "lingjzhu/CharsiuG2P" %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}
