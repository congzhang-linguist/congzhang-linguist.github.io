---
layout: page
title: media
permalink: /media/
description: Media coverage and public engagement across industry and academia.
nav: true
nav_order: 7
---


## AI Music & Singing Synthesis

While working at Rokid Inc., I led an AI singing synthesis project, where we developed a singing synthesis model trained using speech data.

➡️ See the related [project page](/project/sing/) for related research, presentations and publications.

### AI Music Open Platform Launch （2019）


#### 📰 News items

China Unicom's Wo-Music AI Music Open Platform was officially launched at the Global Mobile Internet Conference (GMIC) in Guangzhou. The event, themed "Pearl River Talks" (珠江论道), showcased AI-driven music creation technologies, including singing synthesis. The open platform was presented as an initiative to democratise AI music production and enable independent musicians to access professional-grade tools.


- [联通沃音乐新品亮相GMIC，AI音乐开放平台震撼启动](http://www.cww.net.cn/article?id=455709)
  <br><span style="color:#888; font-size:0.9em;">China Unicom Wo-Music Debuts at GMIC; AI Music Open Platform Makes a Spectacular Launch</span>

- [2019GMIC全球科技文化峰会在广州举行](http://gd.sina.cn/news/2019-08-02/detail-ihytcitm6475238.d.html)
  <br><span style="color:#888; font-size:0.9em;">2019 GMIC Global Technology and Culture Summit Held in Guangzhou</span>

- [联通沃音乐亮相GMIC，重磅推出AI音乐开放平台](https://mp.weixin.qq.com/s/HuX9ehvUSS3Wn1n_uCR2cg)
  <br><span style="color:#888; font-size:0.9em;">China Unicom Wo-Music Appears at GMIC, Launches AI Music Open Platform</span>

- [「珠江论道」亮相GMIC 联通沃音乐AI音乐开放平台发布](http://www.xinhuanet.com/tech/2019-07/27/c_1124806836.htm)
  <br><span style="color:#888; font-size:0.9em;">Pearl River Talks Presents at GMIC; China Unicom Wo-Music AI Music Open Platform Launched</span>


#### 🎬 Exhibition Demo at GMIC Science Renaissance Festival

A short clip recorded at our exhibition booth at the GMIC Science Renaissance Festival, showing the AI singing synthesis demo in action:

<div style="margin: 1.5rem auto; max-width: 340px;">
  <div style="position:relative; padding-bottom:177.78%; height:0; overflow:hidden; border-radius:4px;">
    <video controls style="position:absolute; top:0; left:0; width:100%; height:100%;">
      <source src="/assets/img/media/singing_demo.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  </div>
  <p style="font-size: 0.9em; color: #555; margin-top: 0.5rem;">Demo of the AI singing synthesis system at the GMIC Science Renaissance Festival exhibition booth, 2019.</p>
</div>


#### 📸 GMIC Event Photos
<!-- GMIC Pictures Slideshow -->
{% assign gmic_images = site.static_files | where_exp: "file", "file.path contains '/assets/img/media/gmic_'" %}

<div class="gslideshow">
  <div class="gslides">
    {% for image in gmic_images %}
      {% assign image_number = image.basename | remove: "gmic_" | split: "." | first %}
      <div class="gslide {% if forloop.first %}active{% endif %}">
        {% include figure.liquid 
           path=image.path 
           title="GMIC event photo {{ image_number }}" 
           class="img-fluid" 
           zoomable=false 
        %}
      </div>
    {% endfor %}
  </div>
  
  <button class="gbtn prev" onclick="gStep(-1, 'gmic')">&#10094;</button>
  <button class="gbtn next" onclick="gStep(1, 'gmic')">&#10095;</button>
  
  <div class="gslideshow-footer">
    <span class="gcaption" id="gCaption-gmic">
      {% if gmic_images.size > 0 %}1 / {{ gmic_images.size }}{% endif %}
    </span>
    <div class="gdots" id="gDots-gmic"></div>
  </div>
</div>
---

### AI Singer & Music Video
The AI singer we created was named **小若琪** (Xiǎo Ruòqí, literally "little Rokid"). A song performed by Xiao Ruoqi — *小猪猪* (*Xiǎo Zhūzhū*, "Little Piggy") — was used as the promotional song for the children's film *Lucky Star* (《福星高照朱小八》).

#### News coverage
- [如何借助共享经济模式，发掘下一个周杰伦？](https://www.musicbravo.com.my/Mobile/Home/Column/86ce4378-c72b-4609-8464-c05937cda7d3)
  <br><span style="color:#888; font-size:0.9em;">How to use the sharing economy model to discover the next Jay Chou?</span>
- [虚拟歌手小若琪与音乐霸牵手，一首魔性单曲《小猪猪》送给大家](https://www.163.com/dy/article/EGH6LFLA0511AKBF.html)
  <br><span style="color:#888; font-size:0.9em;">Virtual singer Xiao Ruoqi teams up with Music Master to present everyone with a catchy single, "Little Pig."</span> [[Alternative link 1]](http://www.sohu.com/a/317799318_247408) [[Alternative link 2]](https://read01.com/L25aOBx.html)
- [福星高照朱小八》发布《小猪猪》官方推广曲 AI歌手小若琪首秀大银幕](https://www.sohu.com/a/338416484_745022)
  <br><span style="color:#888; font-size:0.9em;">The film "Lucky Star Zhu Xiaoba" releases the official promotional song "Little Pig," featuring AI singer Xiao Ruoqi making her big-screen debut</span>


<div class="quote-block" style="border-left: 3px solid #aaa; padding: 0.75rem 1.25rem; margin: 1.5rem 0; background: #f9f9f9;">
  <p style="margin: 0 0 0.5rem;">
    「不过，作为人工与AI在儿童歌曲领域的首次合作，制作过程并不容易。Rokid TTS项目负责人张聪博士表示，“关于AI演唱，早期开始做的时候是没有什么参考的，都是通过工程师在一步步的实验中摸索出来的。工程师为了和制作人沟通，也学习了很多音乐方面的知识，从看简谱、节奏、音符开始学起，将歌词对应歌谱，再将拍子换算成时间。在改了很多次计算模型后，终于改进了TTS的演唱技术方法（不同于过去vocaloid的方法），不久将来就可以实现只要输入歌词和曲谱就可以自动生成AI演唱的Demo。”」
  </p>
  <p style="margin: 0 0 0.5rem; color: #555; font-style: italic;">
    "When we first started working on AI singing, there was no reference to speak of — the engineers had to feel their way forward through experiment after experiment. To communicate with the music producers, the engineers also had to pick up a lot of musical knowledge from scratch: reading sheet music, understanding rhythm and notes, mapping lyrics to scores, converting beats to time. After many rounds of revising the computational models, we finally improved our TTS singing method. In the near future, it will be possible to automatically generate an AI singing demo simply by inputting lyrics and a score."
  </p>
  <p style="margin: 0; font-size: 0.9em; color: #888;">— Dr. Cong Zhang, Rokid TTS (AI music) Lead (2019)</p>
</div>


#### 🎵 Music Video

The AI singer Xiao Ruoqi performing *小猪猪* (*Xiǎo Zhūzhū*, "Little Piggy"), promotional song for the film *Lucky Star* (《福星高照朱小八》):

<div class="video-container" style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; margin: 1.5rem 0;">
  <iframe
    style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;"
    src="https://www.youtube.com/embed/Qw9G4loUaHY"
    title="Xiao Ruoqi AI singer - Xiao Zhuzhu"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
  </iframe>
</div>

Alternative link (Bilibili): [bilibili.com/s/video/BV1XU4y1771A](https://www.bilibili.com/s/video/BV1XU4y1771A)


---

## North East Accents & Gamification Project （2024）

My gamification research has attracted public interest and media coverage in the UK, particularly for events exploring North East English accents.

➡️ See the full [project page](/project/gamification/) for research background, the game, and publications.

---



### 📰 News Coverage
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
  
  <div class="gslideshow">
  <div class="gslides">
    <div class="gslide active">{% include figure.liquid path="/assets/img/media/gamification_chronicle.jpg" title=Chronicle in print" class="img-fluid" zoomable=false %}</div>
    <div class="gslide">{% include figure.liquid path="/assets/img/media/gamification_mirror.jpg" title="Mirror in print" class="img-fluid" zoomable=false %}</div>
  </div>
  <button class="gbtn prev" onclick="gStep(-1, 'game')">&#10094;</button>
  <button class="gbtn next" onclick="gStep(1, 'game')">&#10095;</button>
  <div class="gslideshow-footer">
    <span class="gcaption" id="gCaption-game">1 / 9</span>
    <div class="gdots" id="gDots-game"></div>
  </div>