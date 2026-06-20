---
layout: about
title: about
permalink: /
subtitle: cong.zhang at newcastle.ac.uk

profile:
  align: right
  image: prof_pic.jpg
  image_circular: False # crops the image to make it circular
  address: >
    <p>张聪 <button class="pron-play-btn" data-audio="/assets/audio/zhangcong.wav" aria-label="Play Mandarin pronunciation"><i class="fas fa-play"></i></button>
    </p>
    <p>
    Cong Zhang <button class="pron-play-btn" data-audio="/assets/audio/congzhang.wav" aria-label="Play English pronunciation"><i class="fas fa-play"></i></button>
    </p>
    <p>Lecturer in Phonetics and Phonology</p>
    <p>Newcastle University</p>


news: true  # includes a list of news items
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true  # includes social icons at the bottom of the page
cv: true
---


Hello! My name Cong Zhang ([tsʰʊŋ˥ tʃɑŋ˥], *Mandarin*: <button class="pron-play-btn" data-audio="/assets/audio/zhangcong.wav" aria-label="Play Mandarin pronunciation"><i class="fas fa-play"></i></button> or *English*: <button class="pron-play-btn" data-audio="/assets/audio/congzhang.wav" aria-label="Play English pronunciation"><i class="fas fa-play"></i></button>, [more about my name](https://congzhang-linguist.github.io/blog/2023/my-name/)). I am a Lecturer in Phonetics and Phonology at the [School of Education, Communication and Language Sciences](http://ncl.ac.uk/ecls/), Newcastle University, UK.

I am a speech scientist (or prosodist/phonetician/laboratory phonologist) specialising in **speech prosody**, with experience in **speech technology** and **clinical speech** research.

I study speech prosody from both phonetic and phonological perspectives, using a range of approaches including computational and psycholinguistic methods. I am particularly interested in how different layers of prosody interact, from lexical tone and postlexical intonation to the interplay between linguistic and paralinguistic meaning. I also study boundary-related phenomena and prosodic variation across languages and accents, especially in under-documented languages and regional varieties. Alongside theoretical questions, I am interested in developing methods for data collection, analysis, and modelling.

More recently, I have been working at the intersection of speech science, AI, and healthcare, exploring how prosodic and other phonetic features can support automatic speech analysis and classification in real-world applications.

My work is shaped by experiences across several different ways of thinking about language. I began in Translation and Interpreting at [Beijing Foreign Studies University](https://www.bfsu.edu.cn/), where language was primarily a tool for communication in real-world contexts. I then moved into linguistics and language acquisition at Newcastle University, becoming increasingly interested in how language is learned and represented. During my DPhil at the [University of Oxford](http://brainlab.clp.ox.ac.uk/), I focused on more theoretical questions in laboratory phonology, investigating intonational tunes in Tianjin Mandarin ([link to my DPhil thesis](https://ora.ox.ac.uk/objects/uuid:3149a35c-e6c2-4f43-a41a-bdc08ebf08f6)).

After Oxford, I moved in the opposite direction, applying linguistic knowledge in industry through work on speech technology (text-to-speech), where I led an AI singing project, managed speech data collection and annotation, and provided linguistic and phonological input to TTS algorithms and evaluation pipelines. I later returned to academia as part of the ERC-funded [SPRINT](https://cordis.europa.eu/project/id/835263/) project, where I continued investigating fundamental questions about speech prosody in interaction. Today, my research increasingly brings these strands together, combining theoretical insights from phonetics and phonology with applications in speech technology, AI, and healthcare.

Across academia and industry, I am particularly interested in bridging theory, data, and application, and in shaping research directions that make speech science usable beyond the lab.


<div class="cv">

</div>

<script>
document.querySelectorAll('.pron-play-btn').forEach(btn => {
  const audio = new Audio(btn.dataset.audio);
  const icon = btn.querySelector('i');
  btn.onclick = () => {
    audio.currentTime = 0;
    audio.play();
    icon.className = 'fas fa-pause';
    btn.classList.add('playing');
    audio.onended = () => {
      icon.className = 'fas fa-play';
      btn.classList.remove('playing');
    };
  };
});
</script>
