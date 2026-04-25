---
layout: page
permalink: /project/gamification/
title: Gamification
description: Making data collection more fun<br><br><br><br>
img: assets/img/project/game.jpg
importance: 1
category: facilitating research

related_publications: kim2024collecting, li2026gamification
related_talks: gamifying-c
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap');

.gpage { font-family: 'DM Sans', sans-serif; max-width: 720px; margin: 0 auto; }

.gpage-hero {
  border-left: 3px solid #1D9E75;
  padding-left: 1.25rem;
  margin-bottom: 2rem;
}
.gpage-hero .tag {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #1D9E75;
  margin-bottom: 0.4rem;
}
.gpage-hero .subtitle {
  font-size: 15px;
  color: #888;
  font-style: italic;
}

.gpage-intro {
  font-size: 15px;
  line-height: 1.75;
  color: #555;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #eee;
}
.gpage-intro a { color: #1D9E75; text-decoration: none; }
.gpage-intro a:hover { text-decoration: underline; }

.section-label {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #888;
  margin-bottom: 0.75rem;
}
.section-title {
  font-family: 'Lora', serif;
  font-size: 1.35rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.game-card {
  background: #f8f8f6;
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 1.5rem;
}
.game-card p { font-size: 14px; color: #666; line-height: 1.7; margin-bottom: 1rem; }
.game-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: #1D9E75;
  text-decoration: none;
  border: 1px solid #1D9E75;
  border-radius: 20px;
  padding: 6px 16px;
}
.game-link:hover { background: #E1F5EE; }

.resources { margin-bottom: 2rem; border-top: 1px solid #eee; }
.resource-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  padding: 0.85rem 0;
  border-bottom: 1px solid #eee;
}
.resource-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #1D9E75;
  margin-top: 7px;
  flex-shrink: 0;
}
.resource-item a { font-size: 14px; font-weight: 500; color: #222; text-decoration: none; }
.resource-item a:hover { color: #1D9E75; }
.resource-item p { font-size: 13px; color: #888; margin-top: 2px; line-height: 1.5; }

.funding-note {
  font-size: 12px;
  color: #888;
  font-style: italic;
  margin: 1rem 0 2rem;
  padding: 0.75rem 1rem;
  border-left: 2px solid #ddd;
  line-height: 1.6;
}

/* SLIDESHOW */
.gslideshow {
  position: relative;
  margin: 2rem 0;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid #eee;
  background: #f5f5f5;
}
.gslides { position: relative; height: 360px; }
.gslide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.7s ease;
}
.gslide.active { opacity: 1; }
.gslide img { width: 100%; height: 360px; object-fit: cover; display: block; }
.gslide figure { margin: 0; height: 100%; }
.gslide figure img { height: 360px; object-fit: cover; border-radius: 0; }
.gbtn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0,0,0,0.4);
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 8px 14px;
  font-size: 1rem;
  cursor: pointer;
  z-index: 10;
}
.gbtn:hover { background: rgba(0,0,0,0.65); }
.gbtn.prev { left: 10px; }
.gbtn.next { right: 10px; }
.gslideshow-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-top: 1px solid #eee;
  background: #fafafa;
}
.gslideshow-footer .gcaption { font-size: 12px; color: #999; font-style: italic; }
.gdots { display: flex; gap: 5px; align-items: center; }
.gdot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #ccc;
  cursor: pointer;
  transition: background 0.2s, transform 0.2s;
}
.gdot.active { background: #1D9E75; transform: scale(1.3); }

.section-divider { border: none; border-top: 1px solid #eee; margin: 2.5rem 0; }

.media-grid { display: flex; flex-direction: column; gap: 8px; margin-bottom: 1.5rem; }
.media-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: 8px;
  border: 1px solid #eee;
  text-decoration: none;
  transition: border-color 0.15s, background 0.15s;
}
.media-item:hover { border-color: #1D9E75; background: #f9fdfb; }
.media-outlet {
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #999;
  min-width: 64px;
  flex-shrink: 0;
}
.media-headline { font-size: 13px; color: #333; line-height: 1.45; flex: 1; }
.media-arrow { font-size: 13px; color: #bbb; flex-shrink: 0; }

.weyaye-img {
  width: 100%;
  border-radius: 10px;
  border: 1px solid #eee;
  object-fit: cover;
  max-height: 280px;
  display: block;
  margin-bottom: 1.5rem;
}
</style>

<div class="gpage">
  This project examines gamification as a methodological solution to long-standing challenges in research data collection, particularly issues of scale, participant diversity, and ecological validity. We use gamified approaches to embed experimental tasks within engaging interfaces that allow for large-scale data collection outside the laboratory. The project includes both a theoretical overview of gamified approaches in applied linguistics (Kim et al., 2024), and an empirical implementation using an accent identification game in North East England (Li et al., 2026). Together, these studies evaluate whether gamification can function as a valid experimental paradigm for linguistics research. <br><br>
  University project site: <a href="https://research.ncl.ac.uk/ne-accent-games/" target="_blank">research.ncl.ac.uk/ne-accent-games</a>


<hr class="section-divider">
<div class="section-label">North East Language Game</div>
<div class="section-title">Think you know North East accents?</div>

<div class="game-card">
  <p>Data were collected through this online game. Voucher prizes are no longer available. The university server may occasionally go down; when this happens, only the questionnaire section is accessible. We apologise for any inconvenience.</p>
  <a class="game-link" href="https://research.ncl.ac.uk/ne-accent-games/game/">&#9654;&nbsp; Play the game</a>
</div>

<div class="resources">
  <div class="resource-item">
    <div class="resource-dot"></div>
    <div>
      <a href="{{ site.baseurl }}participant_info/">Participant Information Sheet</a>
      <p>Information you are provided before your participation in the study.</p>
    </div>
  </div>
  <div class="resource-item">
    <div class="resource-dot"></div>
    <div>
      <a href="{{ site.baseurl }}debriefing/">Debriefing</a>
      <p>Target answers for game questions, latest study results, and publications.</p>
    </div>
  </div>
</div>



<br>
<div class="section-label">Game screenshots</div>

<!-- ======= AUTO-PLAYING PHOTO GALLERY ======= -->
<div class="gslideshow">
  <div class="gslides">
    <div class="gslide active">{% include figure.liquid path="assets/img/project/gamification/game1.png" title="Photo 1" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game2.png" title="Photo 2" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game3.png" title="Photo 3" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game4.png" title="Photo 4" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game5.png" title="Photo 5" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game6.png" title="Photo 6" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game7.png" title="Photo 7" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game8.png" title="Photo 8" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="assets/img/project/gamification/game9.png" title="Photo 9" class="img-fluid" zoomable=false %}</div>
  </div>
  <button class="gbtn prev" onclick="gStep(-1)">&#10094;</button>
  <button class="gbtn next" onclick="gStep(1)">&#10095;</button>
  <div class="gslideshow-footer">
    <span class="gcaption" id="gCaption">1 / 9</span>
    <div class="gdots" id="gDots"></div>
  </div>
</div>
<!-- ======= END GALLERY ======= -->

<hr class="section-divider">

<div class="section-label">Knowledge Exchange Events</div>
<div class="resources">
  <div class="resource-item">
    <div class="resource-dot"></div>
    <div>
      <a href="https://research.ncl.ac.uk/ne-accent-games/newsevents/weyayemanthinkyouknowanorth-eastaccentwhenyouhearone.html">Festival of Social Science Event</a>
      <p>Wey aye, man: Think you know a North-East accent when you hear one?</p>
    </div>
  </div>
  <div class="resource-item">
    <div class="resource-dot"></div>
    <div>
      <a href="https://research.ncl.ac.uk/ne-accent-games/newsevents/howayjoinusatthediscoverfestivalon7thjuneathancockmuseum.html">Discover Festival Event</a>
      <p>Howay! Think you know a North-East accent when you hear one?</p>
    </div>
  </div>
</div>






<div class="section-label">Media Coverage</div>
<div class="media-grid">
  <a class="media-item" href="https://www.bbc.co.uk/news/articles/crezw2zx138o" target="_blank">
    <span class="media-outlet">BBC</span>
    <span class="media-headline">Can you tell North East accents apart?</span>
    <span class="media-arrow">&#8599;</span>
  </a>
  <a class="media-item" href="https://www.mirror.co.uk/news/uk-news/geordie-accent-studied-newcastle-university-34004194" target="_blank">
    <span class="media-outlet">Mirror</span>
    <span class="media-headline">Geordie accent to be studied at Newcastle University in 'celebration of diversity'</span>
    <span class="media-arrow">&#8599;</span>
  </a>
  <a class="media-item" href="https://www.chroniclelive.co.uk/news/north-east-news/wey-aye-man-newcastle-university-30246657" target="_blank">
    <span class="media-outlet">Chronicle</span>
    <span class="media-headline">'Wey aye, man' — Newcastle University running event exploring North East dialects</span>
    <span class="media-arrow">&#8599;</span>
  </a>
</div>

<div class="center">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/project/gamification/NU_ISS.png" title="Newcastle University Institute of Social Science" class="img-fluid rounded z-depth-1" zoomable=false %}
  </div>
</div>
<div class="funding-note">
  This project is funded by the Institute for Social Science, Newcastle University through a Pioneer Award to Dr. Cong Zhang.
</div>



</div>

<script>
(function(){
  var cur = 0;
  var slides = document.querySelectorAll('.gslide');
  var dotsEl = document.getElementById('gDots');
  var caption = document.getElementById('gCaption');
  var total = slides.length;
  var timer;

  slides.forEach(function(_, i){
    var d = document.createElement('span');
    d.className = 'gdot' + (i === 0 ? ' active' : '');
    d.onclick = function(){ goTo(i); reset(); };
    dotsEl.appendChild(d);
  });

  function goTo(n){
    slides[cur].classList.remove('active');
    dotsEl.children[cur].classList.remove('active');
    cur = (n + total) % total;
    slides[cur].classList.add('active');
    dotsEl.children[cur].classList.add('active');
    caption.textContent = (cur + 1) + ' / ' + total;
  }

  window.gStep = function(dir){ goTo(cur + dir); reset(); };

  function reset(){
    clearInterval(timer);
    timer = setInterval(function(){ goTo(cur + 1); }, 4000);
  }

  reset();
})();
</script>