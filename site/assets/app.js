const state = {
  library: [],
  readingLibrary: [],
  listeningLibrary: [],
  libraryMode: "video",
  currentShow: null,
  currentReading: null,
  currentListeningTrack: null,
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
  modeTabs: document.querySelectorAll("[data-library-mode]"),
  backButton: document.getElementById("back-button"),
  readingBackButton: document.getElementById("reading-back-button"),
  readingTitle: document.getElementById("reading-title"),
  readingProgress: document.getElementById("reading-progress"),
  readingRevealToggle: document.getElementById("reading-reveal-toggle"),
  readingPrev: document.getElementById("reading-prev"),
  readingNext: document.getElementById("reading-next"),
  readingSentence: document.getElementById("reading-sentence"),
  readingTranslation: document.getElementById("reading-translation"),
  listeningBackButton: document.getElementById("listening-back-button"),
  listeningTitle: document.getElementById("listening-title"),
  listeningSection: document.getElementById("listening-section"),
  listeningTrackTitle: document.getElementById("listening-track-title"),
  listeningAudio: document.getElementById("listening-audio"),
  listeningLoopToggle: document.getElementById("listening-loop-toggle"),
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

function renderLibrary() {
  els.modeTabs.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.libraryMode === state.libraryMode);
  });

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
      <div class="series-group__items">
        ${items.map((item) => `
          <button class="show-item" data-show-id="${item.id}" type="button">
            <span class="show-title">${escapeHtml(item.title)}</span>
            <span class="show-meta">
              <span>문장 ${item.sentence_count || 0}</span>
              <span>포인트 ${item.relevant_sentence_count || 0}</span>
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
  els.libraryList.innerHTML = state.readingLibrary.map((item) => `
    <section class="series-group">
      <h2 class="series-group__title">독해</h2>
      <div class="series-group__items">
        <button class="show-item" data-reading-id="${item.id}" type="button">
          <span class="show-title">${escapeHtml(item.title)}</span>
          <span class="show-meta">
            <span>문장 ${item.sentence_count || 0}</span>
            <span>${escapeHtml(item.level || "N3")}</span>
          </span>
        </button>
      </div>
    </section>
  `).join("");

  for (const button of els.libraryList.querySelectorAll("[data-reading-id]")) {
    button.addEventListener("click", async () => {
      await loadReading(button.dataset.readingId);
    });
  }
}

function renderListeningLibrary() {
  els.libraryList.innerHTML = state.listeningLibrary.map((section) => `
    <section class="series-group">
      <h2 class="series-group__title">${escapeHtml(section.title)}</h2>
      <div class="series-group__items">
        ${(section.tracks || []).map((track) => `
          <button class="show-item show-item--compact" data-listening-id="${track.id}" type="button" ${track.site_audio ? "" : "disabled"}>
            <span class="show-title">${escapeHtml(track.title)}</span>
            <span class="show-meta">
              <span>${escapeHtml(section.title)}</span>
              <span>${Math.round((track.compressed_file_size || track.file_size || 0) / 1024 / 1024 * 10) / 10}MB</span>
            </span>
          </button>
        `).join("")}
      </div>
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

  els.readingTitle.textContent = reading ? reading.title : "독해";
  els.readingProgress.textContent = items.length ? `${state.currentReadingIndex + 1} / ${items.length}` : "0 / 0";
  els.readingSentence.innerHTML = reveal ? renderHighlightedSentence(item) : renderPlainSentence(item);
  els.readingTranslation.textContent = reveal ? item?.translation || "" : "";
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
    state.readingLibrary = [reading];
  } catch {
    state.readingLibrary = [];
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

async function loadReading(readingId) {
  const item = state.readingLibrary.find((entry) => entry.id === readingId);
  if (!item) return;
  stopPlayback();
  state.currentReading = item;
  state.currentReadingIndex = 0;
  els.readingRevealToggle.checked = false;
  setScreen("reading");
  renderReadingState();
}

function loadListeningTrack(trackId) {
  const result = findListeningTrack(trackId);
  if (!result || !result.track.site_audio) return;

  stopPlayback();
  state.currentListeningTrack = result.track;
  els.listeningTitle.textContent = "청해";
  els.listeningSection.textContent = result.section.title || "";
  els.listeningTrackTitle.textContent = result.track.title || "";
  els.listeningLoopToggle.checked = false;
  els.listeningAudio.loop = false;
  els.listeningAudio.src = result.track.site_audio;
  setScreen("listening");
}

function jumpReading(direction) {
  const items = state.currentReading?.items || [];
  if (!items.length) return;
  state.currentReadingIndex = Math.max(0, Math.min(items.length - 1, state.currentReadingIndex + direction));
  renderReadingState();
}

function bindEvents() {
  els.modeTabs.forEach((button) => {
    button.addEventListener("click", () => {
      state.libraryMode = button.dataset.libraryMode || "video";
      renderLibrary();
    });
  });

  els.backButton.addEventListener("click", () => {
    if (state.isPlayerHistoryActive) {
      window.history.back();
      return;
    }
    returnToLibrary();
  });

  els.readingBackButton.addEventListener("click", returnToLibrary);
  els.readingRevealToggle.addEventListener("change", renderReadingState);
  els.readingPrev.addEventListener("click", () => jumpReading(-1));
  els.readingNext.addEventListener("click", () => jumpReading(1));
  els.listeningBackButton.addEventListener("click", returnToLibrary);
  els.listeningLoopToggle.addEventListener("change", () => {
    els.listeningAudio.loop = els.listeningLoopToggle.checked;
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
    if (!state.currentShow) return;
    returnToLibrary();
  });
}

async function main() {
  setPlayVisual(false);
  bindEvents();
  await loadLibrary();
}

main().catch((error) => {
  console.error(error);
  els.currentSentence.textContent = error.message;
});
