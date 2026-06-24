const state = {
  library: [],
  readingLibrary: [],
  listeningLibrary: [],
  libraryMode: "",
  currentShow: null,
  currentReading: null,
  currentListeningTrack: null,
  currentListeningIndex: 0,
  currentReadingIndex: 0,
  currentTime: 0,
  isPlaying: false,
  tickHandle: null,
  isPlayerHistoryActive: false,
};

const els = {
  libraryScreen: document.getElementById("library-screen"),
  playerScreen: document.getElementById("player-screen"),
  readingScreen: document.getElementById("reading-screen"),
  listeningScreen: document.getElementById("listening-screen"),
  libraryList: document.getElementById("library-list"),
  homeMenu: document.getElementById("home-menu"),
  homeButtons: document.querySelectorAll("[data-library-mode]"),
  libraryListHeader: document.getElementById("library-list-header"),
  libraryListTitle: document.getElementById("library-list-title"),
  libraryBackButton: document.getElementById("library-back-button"),
  versionBadge: document.querySelector(".version-badge"),
  backButton: document.getElementById("back-button"),
  readingBackButton: document.getElementById("reading-back-button"),
  readingTitle: document.getElementById("reading-title"),
  readingProgress: document.getElementById("reading-progress"),
  readingRevealToggle: document.getElementById("reading-reveal-toggle"),
  readingFullToggle: document.getElementById("reading-full-toggle"),
  readingPrev: document.getElementById("reading-prev"),
  readingNext: document.getElementById("reading-next"),
  readingPanel: document.querySelector(".reading-panel"),
  readingSentence: document.getElementById("reading-sentence"),
  readingTranslation: document.getElementById("reading-translation"),
  listeningBackButton: document.getElementById("listening-back-button"),
  listeningTitle: document.getElementById("listening-title"),
  listeningSection: document.getElementById("listening-section"),
  listeningTrackTitle: document.getElementById("listening-track-title"),
  listeningProgress: document.getElementById("listening-progress"),
  listeningSentence: document.getElementById("listening-sentence"),
  listeningTranslation: document.getElementById("listening-translation"),
  listeningSegmentPlay: document.getElementById("listening-segment-play"),
  listeningAudio: document.getElementById("listening-audio"),
  listeningLoopToggle: document.getElementById("listening-loop-toggle"),
  listeningPrev: document.getElementById("listening-prev"),
  listeningNext: document.getElementById("listening-next"),
  sentencePrev: document.getElementById("sentence-prev"),
  sentenceNext: document.getElementById("sentence-next"),
  playToggle: document.getElementById("play-toggle"),
  playIcon: document.getElementById("play-icon"),
  seekBackward: document.getElementById("seek-backward"),
  seekForward: document.getElementById("seek-forward"),
  showTitle: document.getElementById("show-title"),
  currentTime: document.getElementById("current-time"),
  currentSentence: document.getElementById("current-sentence"),
  currentTranslation: document.getElementById("current-translation"),
  nextCountdown: document.getElementById("next-countdown"),
  nextPreview: document.getElementById("next-preview"),
  nextPreviewTranslation: document.getElementById("next-preview-translation"),
  annotationRail: document.getElementById("annotation-rail"),
  timeline: document.getElementById("timeline"),
  timelinePosition: document.getElementById("timeline-position"),
  timelineDuration: document.getElementById("timeline-duration"),
};

function formatTime(totalSeconds) {
  const value = Math.max(0, Math.floor(totalSeconds));
  const hours = String(Math.floor(value / 3600)).padStart(2, "0");
  const minutes = String(Math.floor((value % 3600) / 60)).padStart(2, "0");
  const seconds = String(value % 60).padStart(2, "0");
  return `${hours}:${minutes}:${seconds}`;
}

function escapeHtml(text) {
  return String(text ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function setScreen(mode) {
  const isPlayer = mode === "player";
  const isReading = mode === "reading";
  const isListening = mode === "listening";
  els.libraryScreen.classList.toggle("is-hidden", isPlayer || isReading || isListening);
  els.playerScreen.classList.toggle("is-hidden", !isPlayer);
  els.readingScreen.classList.toggle("is-hidden", !isReading);
  els.listeningScreen.classList.toggle("is-hidden", !isListening);
}

function enterPlayerHistory(showId) {
  if (state.isPlayerHistoryActive) return;
  const url = new URL(window.location.href);
  url.hash = `show-${showId}`;
  window.history.pushState({ screen: "player", showId }, "", url);
  state.isPlayerHistoryActive = true;
}

function leavePlayerHistory() {
  state.isPlayerHistoryActive = false;
}

function returnToLibrary() {
  stopPlayback();
  setScreen("library");
  state.currentShow = null;
  state.currentReading = null;
  state.currentListeningTrack = null;
  state.currentListeningIndex = 0;
  els.listeningAudio.pause();
  els.listeningAudio.removeAttribute("src");
  state.currentTime = 0;
  leavePlayerHistory();
}

function setPlayVisual(isPlaying) {
  els.playIcon.textContent = isPlaying ? "❚❚" : "▶";
  els.playToggle.classList.toggle("is-pause", isPlaying);
  els.playToggle.setAttribute("aria-label", isPlaying ? "일시정지" : "재생");
}

function buildHighlightMap(sentence) {
  if (!sentence) return [];

  const highlights = [];
  const seenVocab = new Set();
  const seenGrammar = new Set();

  for (const item of sentence.vocab_matches || []) {
    const text = item.surface_in_sentence || item.surface;
    const key = `${text}:${item.surface}:${item.reading || ""}`;
    if (!text || seenVocab.has(key)) continue;
    seenVocab.add(key);
    highlights.push({
      kind: "vocab",
      text,
      reading: item.reading || "",
      meaning: item.meaning || "",
      className: `hl-vocab-${(item.level || "n5").toLowerCase()}`,
      level: (item.level || "n5").toLowerCase(),
    });
  }

  for (const item of sentence.grammar_matches || []) {
    for (const text of item.matched_texts || []) {
      const normalized = String(text || "").trim();
      const key = `${normalized}:${item.label || ""}:${item.meaning || ""}`;
      if (!normalized || seenGrammar.has(key)) continue;
      seenGrammar.add(key);
      highlights.push({
        kind: "grammar",
        text: normalized,
        label: item.label || normalized,
        meaning: item.meaning || "",
        className: `hl-grammar-${(item.level || "n5").toLowerCase()}`,
        level: (item.level || "n5").toLowerCase(),
      });
    }
  }

  highlights.sort((a, b) => b.text.length - a.text.length);
  return highlights;
}

function buildHighlightRanges(sentence) {
  const text = sentence?.text || "";
  const marks = buildHighlightMap(sentence);
  const ranges = [];

  for (const mark of marks) {
    let cursor = 0;
    while (cursor < text.length) {
      const index = text.indexOf(mark.text, cursor);
      if (index === -1) break;
      const end = index + mark.text.length;
      const overlaps = ranges.some((range) => !(end <= range.start || index >= range.end));
      if (!overlaps) {
        ranges.push({ start: index, end, ...mark });
      }
      cursor = index + Math.max(1, mark.text.length);
    }
  }

  ranges.sort((a, b) => a.start - b.start);
  return ranges;
}

function renderHighlightedSentence(sentence) {
  if (!sentence) return "";

  const text = sentence.text || "";
  const ranges = buildHighlightRanges(sentence);
  if (ranges.length === 0) {
    return escapeHtml(text);
  }

  let cursor = 0;
  const parts = [];
  for (const range of ranges) {
    if (cursor < range.start) {
      parts.push(escapeHtml(text.slice(cursor, range.start)));
    }
    const surface = escapeHtml(text.slice(range.start, range.end));
    if (range.kind === "vocab") {
      parts.push(`
        <span class="inline-note inline-note--vocab inline-note--${range.level}">
          <span class="inline-note__top">${escapeHtml(range.reading || "")}</span>
          <span class="inline-note__anchor ${range.className}">${surface}</span>
          <span class="inline-note__bottom">${escapeHtml(range.meaning || "")}</span>
        </span>
      `);
    } else {
      parts.push(`
        <span class="inline-note inline-note--grammar inline-note--${range.level}">
          <span class="inline-note__anchor ${range.className}">${surface}</span>
          <span class="inline-note__bottom inline-note__bottom--grammar">${escapeHtml(range.meaning || range.label || "")}</span>
        </span>
      `);
    }
    cursor = range.end;
  }
  if (cursor < text.length) {
    parts.push(escapeHtml(text.slice(cursor)));
  }
  return parts.join("");
}

function renderPlainSentence(sentence) {
  return escapeHtml(sentence?.text || "");
}

function findCurrentSentenceIndex(show, currentTime) {
  if (!show || !Array.isArray(show.sentences)) return -1;
  let bestIndex = -1;
  let bestStart = -Infinity;
  show.sentences.forEach((sentence, index) => {
    if (currentTime >= sentence.start_seconds && currentTime <= sentence.end_seconds) {
      if (sentence.start_seconds >= bestStart) {
        bestStart = sentence.start_seconds;
        bestIndex = index;
      }
    }
  });
  return bestIndex;
}

function findCurrentSentence(show, currentTime) {
  const index = findCurrentSentenceIndex(show, currentTime);
  return index >= 0 ? show.sentences[index] : null;
}

function findUpcomingPoint(show, currentTime) {
  if (!show) return null;
  return show.sentences.find((sentence) => sentence.has_jlpt && sentence.start_seconds > currentTime) || null;
}

function findNextSentence(show, currentTime) {
  if (!show || !Array.isArray(show.sentences)) return null;
  const currentIndex = findCurrentSentenceIndex(show, currentTime);
  if (currentIndex >= 0 && currentIndex < show.sentences.length - 1) {
    return show.sentences[currentIndex + 1];
  }
  return show.sentences.find((sentence) => sentence.start_seconds > currentTime + 0.05) || null;
}

function jumpToSentence(direction) {
  const show = state.currentShow;
  if (!show || !Array.isArray(show.sentences) || show.sentences.length === 0) return;

  const currentIndex = findCurrentSentenceIndex(show, state.currentTime);

  let target = null;
  if (direction < 0) {
    if (currentIndex > 0) {
      target = show.sentences[currentIndex - 1];
    } else {
      target = [...show.sentences]
        .reverse()
        .find((sentence) => sentence.start_seconds < state.currentTime - 0.05) || show.sentences[0];
    }
  } else {
    if (currentIndex >= 0 && currentIndex < show.sentences.length - 1) {
      target = show.sentences[currentIndex + 1];
    } else {
      target = show.sentences.find((sentence) => sentence.start_seconds > state.currentTime + 0.05) || show.sentences[show.sentences.length - 1];
    }
  }

  if (!target) return;
  state.currentTime = Number(target.start_seconds || 0) + 0.01;
  els.timeline.value = String(Math.floor(state.currentTime));
  renderCurrentState();
}

function buildAnnotations(sentence) {
  if (!sentence) return [];

  const annotations = [];
  const seen = new Set();

  const grammarSeenByAnchor = new Set();
  for (const item of sentence.grammar_matches || []) {
    const anchor = (item.matched_texts && item.matched_texts[0]) || item.label;
    const normalizedAnchor = String(anchor || "").trim();
    const key = `g:${normalizedAnchor}`;
    if (!normalizedAnchor || grammarSeenByAnchor.has(key) || seen.has(key)) continue;
    grammarSeenByAnchor.add(key);
    seen.add(key);
    annotations.push({
      kind: item.is_pattern ? "pattern" : "grammar",
      anchor: normalizedAnchor,
      detail: `${item.label} - ${item.meaning}`,
      level: (item.level || "n5").toLowerCase(),
    });
  }

  return annotations.slice(0, 3);
}

function renderAnnotations(sentence) {
  els.annotationRail.innerHTML = "";
}

function renderCurrentState() {
  const show = state.currentShow;
  const currentSentence = findCurrentSentence(show, state.currentTime);

  els.showTitle.textContent = show ? show.title : "작품";
  els.currentTime.textContent = formatTime(state.currentTime);
  els.timelinePosition.textContent = formatTime(state.currentTime);
  els.currentSentence.innerHTML = renderHighlightedSentence(currentSentence);
  els.currentTranslation.textContent = currentSentence?.translation || "";
  renderAnnotations(currentSentence);

  const nextSentence = findNextSentence(show, state.currentTime);
  if (nextSentence) {
    const secondsLeft = nextSentence.start_seconds - state.currentTime;
    els.nextCountdown.textContent = `${Math.max(0, Math.ceil(secondsLeft))}초 뒤`;
    els.nextPreview.textContent = nextSentence.text || "";
    els.nextPreviewTranslation.textContent = nextSentence.translation || "";
  } else {
    els.nextCountdown.textContent = "";
    els.nextPreview.textContent = "";
    els.nextPreviewTranslation.textContent = "";
  }
}

function modeTitle(mode) {
  return { video: "자막", reading: "독해", listening: "청해" }[mode] || "";
}

function setLibraryHome() {
  state.libraryMode = "";
  els.homeMenu.classList.remove("is-hidden");
  els.libraryListHeader.classList.add("is-hidden");
  els.libraryList.innerHTML = "";
  window.history.replaceState({ screen: "home" }, "", window.location.pathname + window.location.search);
}

function openLibraryMode(mode, pushHistory = true) {
  state.libraryMode = mode;
  if (pushHistory) {
    window.history.pushState({ screen: "library", mode }, "", `#${mode}`);
  }
  renderLibrary();
}

function episodeLabel(title, index) {
  const match = String(title || "").match(/S(\d{2})E(\d{2})/i);
  if (match) return `${match[2]}번`;
  return `${String(index + 1).padStart(2, "0")}번`;
}

function trackLabel(track, index) {
  const match = String(track?.title || "").match(/(\d+)\s*번/);
  if (match) return `${String(Number(match[1])).padStart(2, "0")}번`;
  return `${String(index + 1).padStart(2, "0")}번`;
}

function listeningProblemGroupTitle(track) {
  const title = String(track?.title || "");
  const drill = title.match(/실력다지기/);
  if (drill) return "문제1";
  const test = title.match(/실전테스트\s*(\d+)/);
  if (test) return `문제${Number(test[1]) + 1}`;
  const n = title.match(/문제\s*(\d+)/);
  return n ? `문제${Number(n[1])}` : "문제";
}

function groupListeningTracks(section) {
  const groups = [];
  const byTitle = new Map();
  for (const track of section.tracks || []) {
    const groupTitle = listeningProblemGroupTitle(track);
    if (!byTitle.has(groupTitle)) {
      const group = { title: groupTitle, tracks: [] };
      byTitle.set(groupTitle, group);
      groups.push(group);
    }
    byTitle.get(groupTitle).tracks.push(track);
  }
  return groups;
}

function renderLibrary() {
  const isHome = !state.libraryMode;
  els.homeMenu.classList.toggle("is-hidden", !isHome);
  els.libraryListHeader.classList.toggle("is-hidden", isHome);
  els.versionBadge.classList.toggle("is-hidden", !isHome);
  els.libraryListTitle.textContent = modeTitle(state.libraryMode);

  if (isHome) {
    els.libraryList.innerHTML = "";
    return;
  }

  if (state.libraryMode === "reading") {
    renderReadingLibrary();
    return;
  }

  if (state.libraryMode === "listening") {
    renderListeningLibrary();
    return;
  }

  const groups = new Map();
  for (const item of state.library) {
    const seriesName = item.title.replace(/\s*-\s*S\d{2}E\d{2}$/i, "").trim() || item.title;
    if (!groups.has(seriesName)) {
      groups.set(seriesName, []);
    }
    groups.get(seriesName).push(item);
  }

  els.libraryList.innerHTML = [...groups.entries()].map(([seriesName, items]) => `
    <section class="series-group">
      <h2 class="series-group__title">${escapeHtml(seriesName)}</h2>
      <div class="series-group__items series-group__items--compact">
        ${items.map((item, index) => `
          <button class="show-item show-item--tile" data-show-id="${item.id}" type="button" title="${escapeHtml(item.title)}">
            <span class="show-title">${escapeHtml(episodeLabel(item.title, index))}</span>
            <span class="show-meta">
              <span>${item.relevant_sentence_count || 0}문장</span>
            </span>
          </button>
        `).join("")}
      </div>
    </section>
  `).join("");

  for (const button of els.libraryList.querySelectorAll("[data-show-id]")) {
    button.addEventListener("click", async () => {
      await loadShow(button.dataset.showId);
    });
  }
}

function renderReadingLibrary() {
  const sections = state.readingLibrary.flatMap((item) => buildReadingParts(item));
  els.libraryList.innerHTML = sections.map((section) => `
    <section class="series-group">
      <h2 class="series-group__title">${escapeHtml(section.title)}</h2>
      <div class="series-group__items series-group__items--compact series-group__items--study">
        ${section.parts.map((part, index) => `
          <button class="show-item show-item--tile show-item--study" data-reading-id="${section.readingId}" data-reading-index="${part.startIndex}" type="button">
            <span class="show-title">${escapeHtml(part.label || `${String(index + 1).padStart(2, "0")}번`)}</span>
          </button>
        `).join("")}
      </div>
    </section>
  `).join("");

  for (const button of els.libraryList.querySelectorAll("[data-reading-id]")) {
    button.addEventListener("click", async () => {
      await loadReading(button.dataset.readingId, Number(button.dataset.readingIndex || 0));
    });
  }
}

function buildReadingParts(reading) {
  if (Array.isArray(reading.sections) && reading.sections.length) {
    return reading.sections.map((section) => ({
      readingId: reading.id,
      title: `${reading.title || "독해"} - ${section.title}`,
      parts: (section.passages || []).map((passage, index) => ({
        title: passage.title,
        label: `${String(index + 1).padStart(2, "0")}번`,
        startIndex: passage.start_index || 0,
        count: passage.sentence_count || (passage.items || []).length || 0,
      })),
    }));
  }

  const items = reading?.items || [];
  const groups = [];
  let current = null;

  items.forEach((item, index) => {
    const text = item.text || "";
    const match = text.match(/問題\s*(\d+)/);
    if (match || !current) {
      current = {
        title: match ? `問題 ${match[1]}` : reading.title,
        startIndex: index,
        count: 0,
      };
      groups.push(current);
    }
    current.count += 1;
  });

  const parts = groups.length ? groups : [{ title: reading.title || "독해", startIndex: 0, count: items.length }];
  return parts.map((part, index) => ({
    readingId: reading.id,
    title: part.title || `독해 ${index + 1}`,
    parts: [{
      ...part,
      label: `${String(index + 1).padStart(2, "0")}번`,
    }],
  }));
}

function renderListeningLibrary() {
  els.libraryList.innerHTML = state.listeningLibrary.map((section) => `
    <section class="series-group">
      <h2 class="series-group__title">${escapeHtml(section.title)}</h2>
      ${groupListeningTracks(section).map((group) => `
        <section class="subseries-group">
          <h3 class="subseries-group__title">${escapeHtml(group.title)}</h3>
          <div class="series-group__items series-group__items--compact series-group__items--study">
            ${group.tracks.map((track, index) => `
              <button class="show-item show-item--tile show-item--study" data-listening-id="${track.id}" type="button" ${track.site_audio ? "" : "disabled"} title="${escapeHtml(track.title)}">
                <span class="show-title">${escapeHtml(trackLabel(track, index))}</span>
              </button>
            `).join("")}
          </div>
        </section>
        `).join("")}
    </section>
  `).join("");

  for (const button of els.libraryList.querySelectorAll("[data-listening-id]")) {
    button.addEventListener("click", () => {
      loadListeningTrack(button.dataset.listeningId);
    });
  }
}

function renderReadingState() {
  const reading = state.currentReading;
  const items = reading?.items || [];
  const item = items[state.currentReadingIndex] || null;
  const reveal = Boolean(els.readingRevealToggle.checked);
  const isFull = Boolean(els.readingFullToggle.checked);

  els.readingTitle.textContent = reading ? reading.title : "독해";
  els.readingProgress.textContent = items.length ? `${state.currentReadingIndex + 1} / ${items.length}` : "0 / 0";
  els.readingPanel.classList.toggle("is-revealed", reveal || isFull);
  els.readingPanel.classList.toggle("is-full-view", isFull);
  els.readingPrev.classList.toggle("is-hidden", isFull);
  els.readingNext.classList.toggle("is-hidden", isFull);

  if (isFull) {
    const passageItems = getCurrentReadingPassageItems();
    els.readingSentence.innerHTML = renderReadingFullView(passageItems, reveal);
    els.readingTranslation.textContent = "";
    return;
  }

  els.readingSentence.innerHTML = renderHighlightedSentence(item);
  els.readingTranslation.textContent = item?.translation || "";
}

function getCurrentReadingPassageItems() {
  const items = state.currentReading?.items || [];
  const item = items[state.currentReadingIndex] || null;
  if (!item?.passage_id) return item ? [item] : [];
  return items.filter((entry) => entry.passage_id === item.passage_id);
}

function renderReadingFullView(items, reveal) {
  if (!items.length) return "";
  const title = items[0].passage_title || "";
  const question = findCurrentReadingPassage()?.question || "";
  return `
    <article class="reading-full">
      <h3 class="reading-full__title">${escapeHtml(title)}</h3>
      ${question ? `<p class="reading-full__question">${escapeHtml(question)}</p>` : ""}
      ${items.map((item) => `
        <section class="reading-full__item">
          <p class="reading-full__sentence">${renderHighlightedSentence(item)}</p>
          ${reveal ? `<p class="reading-full__translation">${escapeHtml(item.translation || "")}</p>` : ""}
        </section>
      `).join("")}
    </article>
  `;
}

function findCurrentReadingPassage() {
  const item = (state.currentReading?.items || [])[state.currentReadingIndex] || null;
  if (!item?.passage_id) return null;
  return (state.currentReading?.passages || []).find((passage) => passage.id === item.passage_id) || null;
}

function getListeningSegments() {
  return state.currentListeningTrack?.segments || [];
}

function renderListeningState() {
  const track = state.currentListeningTrack;
  const segments = getListeningSegments();
  const segment = segments[state.currentListeningIndex] || null;

  els.listeningTrackTitle.textContent = track?.title || "";
  els.listeningProgress.textContent = segments.length ? `${state.currentListeningIndex + 1} / ${segments.length}` : "전사 대기";
  els.listeningSentence.innerHTML = segment ? renderHighlightedSentence(segment) : escapeHtml(track?.text || "");
  els.listeningTranslation.textContent = segment?.translation || "";
  els.listeningPrev.disabled = state.currentListeningIndex <= 0 || segments.length === 0;
  els.listeningNext.disabled = state.currentListeningIndex >= segments.length - 1 || segments.length === 0;
  els.listeningSegmentPlay.disabled = segments.length === 0;
  els.listeningLoopToggle.disabled = segments.length === 0;
}

function isListeningLoopEnabled() {
  return els.listeningLoopToggle.getAttribute("aria-pressed") === "true";
}

function setListeningLoopEnabled(enabled) {
  els.listeningLoopToggle.setAttribute("aria-pressed", enabled ? "true" : "false");
  els.listeningLoopToggle.classList.toggle("is-active", enabled);
}

function restartCurrentListeningSegment() {
  const segment = getListeningSegments()[state.currentListeningIndex];
  if (!segment) return;
  els.listeningAudio.currentTime = Number(segment.start_seconds || 0);
  els.listeningAudio.play();
}

function syncListeningSegmentFromTime() {
  const segments = getListeningSegments();
  if (!segments.length) return;

  const currentTime = els.listeningAudio.currentTime;
  const current = segments[state.currentListeningIndex];

  if (isListeningLoopEnabled() && current) {
    const start = Number(current.start_seconds || 0);
    const end = Number(current.end_seconds || start);
    if (currentTime >= Math.max(start, end - 0.04) || currentTime < start - 0.08) {
      restartCurrentListeningSegment();
    }
    return;
  }

  const index = segments.findIndex((segment) => currentTime >= segment.start_seconds && currentTime < segment.end_seconds);
  if (index >= 0 && index !== state.currentListeningIndex) {
    state.currentListeningIndex = index;
    renderListeningState();
  }
}

function jumpListening(direction) {
  const segments = getListeningSegments();
  if (!segments.length) return;
  state.currentListeningIndex = Math.max(0, Math.min(segments.length - 1, state.currentListeningIndex + direction));
  const segment = segments[state.currentListeningIndex];
  els.listeningAudio.currentTime = segment.start_seconds;
  renderListeningState();
}

function playListeningSegment() {
  const segment = getListeningSegments()[state.currentListeningIndex];
  if (!segment) return;
  els.listeningAudio.currentTime = segment.start_seconds;
  els.listeningAudio.play();
  renderListeningState();
}

function findListeningTrack(trackId) {
  for (const section of state.listeningLibrary) {
    const track = (section.tracks || []).find((item) => item.id === trackId);
    if (track) {
      return { section, track };
    }
  }
  return null;
}

function syncTimelineBounds() {
  const show = state.currentShow;
  const duration = show ? Number(show.duration_seconds || 0) : 0;
  els.timeline.max = String(duration);
  els.timeline.value = String(Math.floor(state.currentTime));
  els.timelineDuration.textContent = formatTime(duration);
}

function stopPlayback() {
  state.isPlaying = false;
  if (state.tickHandle) {
    window.clearInterval(state.tickHandle);
    state.tickHandle = null;
  }
  setPlayVisual(false);
}

function startPlayback() {
  if (!state.currentShow) return;
  stopPlayback();
  state.isPlaying = true;
  setPlayVisual(true);
  state.tickHandle = window.setInterval(() => {
    state.currentTime += 0.25;
    const limit = Number(els.timeline.max || 0);
    if (state.currentTime >= limit) {
      state.currentTime = limit;
      stopPlayback();
    }
    els.timeline.value = String(Math.floor(state.currentTime));
    renderCurrentState();
  }, 250);
}

function jumpBy(delta) {
  const limit = Number(els.timeline.max || 0);
  state.currentTime = Math.max(0, Math.min(limit, state.currentTime + delta));
  els.timeline.value = String(Math.floor(state.currentTime));
  renderCurrentState();
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`데이터를 불러오지 못했습니다: ${url}`);
  }
  return await response.json();
}

async function loadLibrary() {
  const payload = await fetchJson("./data/library.json");
  state.library = payload.items || [];
  try {
    const reading = await fetchJson("./data/jlpt/reading/n3_official_workbook_reading.json");
    const customReading = await fetchJson("./data/jlpt/reading/n3_custom_reading.json");
    state.readingLibrary = [customReading, reading];
  } catch {
    try {
      const reading = await fetchJson("./data/jlpt/reading/n3_official_workbook_reading.json");
      state.readingLibrary = [reading];
    } catch {
      state.readingLibrary = [];
    }
  }
  try {
    const listening = await fetchJson("./data/jlpt/listening/n3_listening_review_index.json");
    state.listeningLibrary = listening.sections || [];
  } catch {
    state.listeningLibrary = [];
  }
  renderLibrary();
}

async function loadShow(showId) {
  stopPlayback();
  setScreen("player");
  enterPlayerHistory(showId);
  els.currentSentence.textContent = "";
  els.currentTranslation.textContent = "";
  els.annotationRail.innerHTML = "";

  const payload = await fetchJson(`./data/shows/${showId}.json`);
  state.currentShow = payload;
  state.currentTime = 0;
  syncTimelineBounds();
  renderCurrentState();
}

async function loadReading(readingId, startIndex = 0) {
  const item = state.readingLibrary.find((entry) => entry.id === readingId);
  if (!item) return;
  stopPlayback();
  state.currentReading = item;
  state.currentReadingIndex = Math.max(0, Math.min((item.items || []).length - 1, startIndex));
  els.readingRevealToggle.checked = false;
  els.readingFullToggle.checked = false;
  setScreen("reading");
  renderReadingState();
}

function loadListeningTrack(trackId) {
  const result = findListeningTrack(trackId);
  if (!result || !result.track.site_audio) return;

  stopPlayback();
  state.currentListeningTrack = result.track;
  state.currentListeningIndex = 0;
  els.listeningTitle.textContent = "청해";
  els.listeningSection.textContent = result.section.title || "";
  setListeningLoopEnabled(false);
  els.listeningAudio.loop = false;
  els.listeningAudio.src = result.track.site_audio;
  setScreen("listening");
  renderListeningState();
}

function jumpReading(direction) {
  const items = state.currentReading?.items || [];
  if (!items.length) return;
  state.currentReadingIndex = Math.max(0, Math.min(items.length - 1, state.currentReadingIndex + direction));
  renderReadingState();
}

function bindEvents() {
  els.homeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      openLibraryMode(button.dataset.libraryMode || "video");
    });
  });
  els.libraryBackButton.addEventListener("click", setLibraryHome);

  els.backButton.addEventListener("click", () => {
    if (state.isPlayerHistoryActive) {
      window.history.back();
      return;
    }
    returnToLibrary();
  });

  els.readingBackButton.addEventListener("click", returnToLibrary);
  els.readingRevealToggle.addEventListener("change", renderReadingState);
  els.readingFullToggle.addEventListener("change", renderReadingState);
  els.readingPrev.addEventListener("click", () => jumpReading(-1));
  els.readingNext.addEventListener("click", () => jumpReading(1));
  els.listeningBackButton.addEventListener("click", returnToLibrary);
  els.listeningLoopToggle.addEventListener("click", () => {
    setListeningLoopEnabled(!isListeningLoopEnabled());
    els.listeningAudio.loop = false;
  });
  els.listeningPrev.addEventListener("click", () => jumpListening(-1));
  els.listeningNext.addEventListener("click", () => jumpListening(1));
  els.listeningSegmentPlay.addEventListener("click", playListeningSegment);
  els.listeningAudio.addEventListener("timeupdate", syncListeningSegmentFromTime);
  els.listeningAudio.addEventListener("ended", () => {
    if (isListeningLoopEnabled()) {
      restartCurrentListeningSegment();
    }
  });

  els.playToggle.addEventListener("click", () => {
    if (!state.currentShow) return;
    if (state.isPlaying) {
      stopPlayback();
    } else {
      startPlayback();
    }
  });

  els.seekBackward.addEventListener("click", () => jumpBy(-5));
  els.seekForward.addEventListener("click", () => jumpBy(5));
  els.sentencePrev.addEventListener("click", () => jumpToSentence(-1));
  els.sentenceNext.addEventListener("click", () => jumpToSentence(1));

  els.timeline.addEventListener("input", () => {
    state.currentTime = Number(els.timeline.value || 0);
    renderCurrentState();
  });

  window.addEventListener("popstate", () => {
    if (state.currentShow || state.currentReading || state.currentListeningTrack) {
      returnToLibrary();
      return;
    }
    if (state.libraryMode) {
      setLibraryHome();
    }
  });
}

async function main() {
  setPlayVisual(false);
  bindEvents();
  await loadLibrary();
  if (window.location.hash) {
    const mode = window.location.hash.replace("#", "");
    if (["video", "reading", "listening"].includes(mode)) {
      openLibraryMode(mode, false);
    }
  }
}

main().catch((error) => {
  console.error(error);
  els.currentSentence.textContent = error.message;
});
