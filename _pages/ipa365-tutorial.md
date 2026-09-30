---
layout: page
permalink: /resources/ipa365-tutorial/
title: IPA365 Flashcards tutorial
description: A guide to studying IPA symbols with IPA365 Flashcards
nav: false
---

<style>
  .ipa-tutorial {
    max-width: 860px;
  }

  .ipa-tutorial .tutorial-intro {
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 1.6rem;
  }

  .ipa-tutorial .tutorial-video {
    margin: 1.5rem auto 2.5rem;
    max-width: 430px;
  }

  .ipa-tutorial video {
    display: block;
    width: 100%;
    border-radius: 0.75rem;
    background: #111827;
  }

  .ipa-tutorial .video-note {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.55;
    margin: 0.75rem 0 0;
  }

  .ipa-tutorial .chapter-list {
    display: grid;
    gap: 0.85rem;
  }

  .ipa-tutorial details {
    border: 1px solid var(--global-divider-color);
    border-radius: 0.75rem;
    background: var(--global-card-bg-color);
    overflow: hidden;
  }

  .ipa-tutorial summary {
    cursor: pointer;
    padding: 1rem 1.15rem;
    color: var(--global-text-color);
    font-weight: 600;
    line-height: 1.45;
  }

  .ipa-tutorial summary:hover,
  .ipa-tutorial summary:focus-visible {
    color: var(--global-theme-color);
  }

  .ipa-tutorial details[open] summary {
    border-bottom: 1px solid var(--global-divider-color);
  }

  .ipa-tutorial .chapter-content {
    padding: 1.15rem;
  }

  .ipa-tutorial .chapter-content p {
    line-height: 1.7;
  }

  .ipa-tutorial .chapter-gif {
    display: block;
    width: 100%;
    max-width: 360px;
    margin: 1rem auto 0;
    border-radius: 0.6rem;
    background: var(--global-bg-color);
  }

  .ipa-tutorial .tutorial-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: 2rem;
  }

  .ipa-tutorial .tutorial-links a {
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    padding: 0.45rem 0.9rem;
    text-decoration: none;
  }

  .ipa-tutorial .tutorial-links a:hover {
    border-color: var(--global-theme-color);
    color: var(--global-theme-color);
  }
</style>

<div class="ipa-tutorial">
  <p class="tutorial-intro">
    IPA365 Flashcards is an interactive tool for practising IPA symbols, their labels,
    pronunciation and examples. The full demo below walks through the complete workflow;
    the chapter guides then explain each feature in text, with a short silent GIF for readers
    who want to inspect a particular action.
  </p>

  <div class="tutorial-video">
    <video controls preload="metadata" playsinline aria-label="Full IPA365 Flashcards demonstration">
      <source src="{{ '/assets/img/resources/IPA365-flashcard/video-00-full-demo.mp4' | relative_url }}" type="video/mp4">
      Your browser does not support the video element.
    </video>
    <p class="video-note">
      The full demonstration is silent; the instructions are provided in the written guide
      below and in the captions embedded in the recording.
    </p>
  </div>

  <div class="chapter-list">
    <details>
      <summary>1. Changing the category</summary>
      <div class="chapter-content">
        <p>
          The Study tab opens with the full IPA deck. Use the <strong>FOCUS CATEGORY</strong>
          controls to narrow it to <strong>ALL</strong>, <strong>CONSONANTS</strong>,
          <strong>VOWELS</strong> or <strong>DIACRITICS</strong>. Choosing a category rebuilds
          the deck around the sounds you want to practise; choose <strong>ALL IPA</strong>
          whenever you want to return to the complete set.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-01-category.gif' | relative_url }}" alt="Selecting a focus category and returning to the full IPA deck">
      </div>
    </details>

    <details>
      <summary>2. Features in Card</summary>
      <div class="chapter-content">
        <p>
          Open the gear icon to open <strong>Study Setup</strong>. Under
          <strong>Features in Card</strong>, choose which information appears on each card:
          <strong>SYMBOL</strong>, <strong>LABEL</strong>, <strong>SOUND</strong> and
          <strong>EXAMPLES</strong>. After choosing the features, select
          <strong>Start Studying</strong>. In Flashcard mode, the front presents the prompt;
          turn the card over to see the answer and use <strong>NO</strong>,
          <strong>MAYBE</strong> or <strong>YES</strong> to grade yourself.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-02-features.gif' | relative_url }}" alt="Choosing card features, starting a study session, and turning over a flashcard">
      </div>
    </details>

    <details>
      <summary>3. Changing the prompt</summary>
      <div class="chapter-content">
        <p>
          The prompt determines what you must recall first. By default, the IPA
          <strong>SYMBOL</strong> is shown as the prompt and the <strong>LABEL</strong> is the
          answer. In <strong>Study Setup</strong>, change the <strong>Prompt</strong> row to
          <strong>LABEL</strong> when you want to read a phonetic description and recall its
          symbol instead. The card and its selected features stay the same; only the direction
          of recall changes.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-03-prompt.gif' | relative_url }}" alt="Changing the flashcard prompt from an IPA symbol to its label">
      </div>
    </details>

    <details>
      <summary>4. Tabbed cards</summary>
      <div class="chapter-content">
        <p>
          When three or more features are enabled, the Flashcard becomes a tabbed card rather
          than a single crowded view. Each feature gets its own tab: use the label tab to read
          the name, the speaker tab to hear the sound, and the examples tab for a pronunciation
          tip and a real word. The prompt can still be changed in <strong>Study Setup</strong>,
          while all of the feature tabs remain available on the card.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-04-tabbed.gif' | relative_url }}" alt="Using the tabs for the symbol, label, sound, and examples on a flashcard">
      </div>
    </details>

    <details>
      <summary>5. Quiz mode and full stars</summary>
      <div class="chapter-content">
        <p>
          Choose <strong>Quiz</strong> in the <strong>Study Mode</strong> row when you want to
          answer before seeing the solution. For example, set the prompt to <strong>LABEL</strong>
          and use the IPA keyboard to enter the matching symbol. Submit the answer with
          <strong>CHECK ANSWER</strong>. A completely correct response earns a full star in the
          <strong>STAR JAR</strong>.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-05-quiz-star.gif' | relative_url }}" alt="Answering an IPA quiz question correctly and earning a full star">
      </div>
    </details>

    <details>
      <summary>6. Half stars</summary>
      <div class="chapter-content">
        <p>
          Quiz answers can also earn partial credit. Many labels contain three descriptive terms,
          such as <em>close front unrounded vowel</em>. Matching two of those terms earns half a
          star, whether you answer with a sound that shares two terms or provide a label that is
          missing one term. This gives useful feedback while still showing which part of the
          description needs more practice.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-06-half-star.gif' | relative_url }}" alt="Receiving half a star for a partially correct IPA quiz answer">
      </div>
    </details>

    <details>
      <summary>7. Flashcard grading and the deck</summary>
      <div class="chapter-content">
        <p>
          In Flashcard mode, turn the card over before grading yourself. Choose
          <strong>YES</strong> when you knew the answer; that card leaves the deck for the
          current session. Choose <strong>NO</strong> or <strong>MAYBE</strong> when you need to
          see it again. The deck counter shows this progress as the remaining cards become a
          smaller, more focused set.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-07-deck.gif' | relative_url }}" alt="Grading flashcards with No, Maybe, and Yes as the study deck changes">
      </div>
    </details>

    <details>
      <summary>8. Installing the app</summary>
      <div class="chapter-content">
        <p>
          IPA365 works like an app and can be added to your home screen. Open the gear icon and
          look for the install option at the top of <strong>Study Setup</strong>. If your browser
          cannot offer a native install prompt, open the <strong>Tutorial</strong> tab for
          device-specific instructions: on iPhone or iPad use <strong>Share</strong> and
          <strong>Add to Home Screen</strong>; on Android use the browser menu and
          <strong>Install app</strong>.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-08-install.gif' | relative_url }}" alt="Finding the IPA365 install instructions for a phone or tablet">
      </div>
    </details>

    <details>
      <summary>9. Completing a session</summary>
      <div class="chapter-content">
        <p>
          Clear every card in a study session to reach the <strong>Queue Clear!</strong>
          celebration screen. It shows the stars collected during that session, including any
          half stars from partially correct quiz answers. Close the preview when you are ready
          to start another session.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-09-celebration.gif' | relative_url }}" alt="The Queue Clear celebration screen showing stars collected in a study session">
      </div>
    </details>

    <details>
      <summary>10. Resetting progress</summary>
      <div class="chapter-content">
        <p>
          Your progress is saved, so cards you have successfully learned leave the active deck.
          To start over, open the gear icon and choose <strong>Reset Progress</strong>. This
          restores the learned cards and brings the deck back to its starting state, ready for a
          fresh study session.
        </p>
        <img class="chapter-gif" loading="lazy" src="{{ '/assets/img/resources/IPA365-flashcard/gif-10-reset.gif' | relative_url }}" alt="Resetting IPA365 progress and restoring the full study deck">
      </div>
    </details>
  </div>

  <div class="tutorial-links">
    <a href="{{ '/resources/' | relative_url }}">Back to resources</a>
    <a href="https://congzhang365.github.io/IPA_flashcard/" target="_blank" rel="noopener">Open IPA365 Flashcards</a>
  </div>
</div>
