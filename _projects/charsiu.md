---
layout: page
permalink: /project/charsiu/
title: Charsiu
description: Charsiu forced aligner & automatic speech recognition tool
img: assets/img/aligner.jpeg
importance: 1
category: current
related_publications: zhu2022phone-charsiu
---


The task of phone-to-audio alignment has many applications in speech research. Here we introduce two Wav2Vec2-based models for both text-dependent and text-independent phone-to-audio alignment. The proposed Wav2Vec2-FS, a semi-supervised model, directly learns phone-to-audio alignment through contrastive learning and a forward sum loss, and can be coupled with a pretrained phone recognizer to achieve text-independent alignment. The other model, Wav2Vec2-FC, is a frame classification model trained on forced aligned labels that can both perform forced alignment and text-independent segmentation. Evaluation results suggest that both proposed methods, even when transcriptions are not available, generate highly close results to existing forced alignment tools. Our work presents a neural pipeline of fully automated phone-to-audio alignment.


- Github: [https://github.com/lingjzhu/charsiu](https://github.com/lingjzhu/charsiu)
- Tutorial: [Open in Colab](https://colab.research.google.com/github/lingjzhu/charsiu/blob/development/charsiu_tutorial.ipynb)

