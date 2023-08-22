---
layout: page
permalink: /project/charsiu/
title: Charsiu
description: Charsiu forced aligner & automatic speech recognition tool <br><br>
img: assets/img/project/charsiu.png
importance: 1
category: speech technology
related_publications: zhu2022phone-charsiu
related_talks: zhu2022phone-c
related_resources: zhu2022phone-charsiu, zhu2022aligned-en, zhu2022aligned-cn
---

The **Charsiu phonetic aligner** can:
- force align: require speech audio + corresponding text transcription
- automatically recognise and align: require speech audio only  

The task of phone-to-audio alignment has many applications in speech research. Here we introduce two Wav2Vec2-based models for both text-dependent and text-independent phone-to-audio alignment. The proposed Wav2Vec2-FS, a semi-supervised model, directly learns phone-to-audio alignment through contrastive learning and a forward sum loss, and can be coupled with a pretrained phone recognizer to achieve text-independent alignment. The other model, Wav2Vec2-FC, is a frame classification model trained on forced aligned labels that can both perform forced alignment and text-independent segmentation. Evaluation results suggest that both proposed methods, even when transcriptions are not available, generate highly close results to existing forced alignment tools. Our work presents a neural pipeline of fully automated phone-to-audio alignment.


The evaluation results against other aligners are：
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/project/charsiu.png" title="charsiu evaluation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<br>
## Github repo:
{% if "lingjzhu/Charsiu" %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo in "lingjzhu/Charsiu" %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}
<br>

## Tutorial: 
A step-by-step tutorial for linguists:
<a target="_blank" href="https://colab.research.google.com/github/lingjzhu/charsiu/blob/main/charsiu_tutorial.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

<br>

