---
layout: page
permalink: /project/featureTTS/
title: featureTTS
description: Applying phonological features to Text-to-Speech <br><br><br>
img: assets/img/project/featureTTS.png
importance: 1
category: speech technology
related_publications: zhang2026featureTTS
related_talks: zhang2022featurally-c
related_resources: zhang2021TTS
---

This study explores the integration of human linguistic insights into multilingual text-to-speech (TTS) systems by evaluating the Featurally Underspecified Lexicon (FUL) as a theory-driven input representation. Unlike data-intensive end-to-end models, FUL offers a compact, interpretable feature set grounded in phonological principles, enabling scalable and equitable TTS development for low-resource languages. We provide a mapping from language-specific phones to FUL feature vectors via a SAMPA intermediate and incorporate these features into a modified FastSpeech architecture. Experiments were conducted to evaluate their ability to generate native, non-native, and code-mixed speech in English and Mandarin. We ran an experiment with a small dataset and one with a larger dataset, which showed that TTS with FUL features as input could produce intelligible native speech with as little as 8 hours of training data; with 100 hours of training data, intelligible speech could be generated for a language not present in the training data. The approach further supports code-mixed synthesis while preserving consistent timbre and interpretable phonetic control. These results highlight the potential of theory-driven representations for building efficient, scalable, and linguistically informed TTS systems, demonstrating that phonological features can function as both analytical tools and practical inputs for speech technology.


## Demo webpage:
[https://congzhang365.github.io/feature_tts/](https://congzhang365.github.io/feature_tts/)