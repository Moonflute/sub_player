const state = {
  library: [],
  currentShow: null,
  currentTime: 0,
  isPlaying: false,
  tickHandle: null,
  isPlayerHistoryActive: false,
};

const els = {
  libraryScreen: document.getElementById("library-screen"),
  playerScreen: document.getElementById("player-screen"),
  libraryList: document.getElementById("library-list"),
  backButton: document.getElementById("back-button"),
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
  els.libraryScreen.classList.toggle("is-hidden", isPlayer);
  els.playerScreen.classList.toggle("is-hidden", !isPlayer);
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
      if (!normalized || seenGrammar.has(normalized)) continue;
      seenGrammar.add(normalized);
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
      parts.push(`<span class="${range.className}">${surface}</span>`);
    }
    cursor = range.end;
  }
  if (cursor < text.length) {
    parts.push(escapeHtml(text.slice(cursor)));
  }
  return parts.join("");
}

function findCurrentSentence(show, currentTime) {
  if (!show) return null;
  return show.sentences.find((sentence) => {
    return currentTime >= sentence.start_seconds && currentTime <= sentence.end_seconds;
  }) || null;
}

function findUpcomingPoint(show, currentTime) {
  if (!show) return null;
  return show.sentences.find((sentence) => sentence.has_jlpt && sentence.start_seconds > currentTime) || null;
}

function jumpToSentence(direction) {
  const show = state.currentShow;
  if (!show || !Array.isArray(show.sentences) || show.sentences.length === 0) return;

  const currentIndex = show.sentences.findIndex((sentence) => {
    return state.currentTime >= sentence.start_seconds && state.currentTime <= sentence.end_seconds;
  });

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
  state.currentTime = Number(target.start_seconds || 0);
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
  const annotations = buildAnnotations(sentence);
  if (annotations.length === 0) {
    els.annotationRail.innerHTML = "";
    return;
  }

  els.annotationRail.innerHTML = annotations.map((item) => `
    <div class="annotation-chip annotation-chip--${item.kind} annotation-chip--${item.level}">
      ${escapeHtml(item.detail)}
    </div>
  `).join("");
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

  const upcoming = findUpcomingPoint(show, state.currentTime);
  if (upcoming) {
    const secondsLeft = upcoming.start_seconds - state.currentTime;
    els.nextCountdown.textContent = `${Math.max(0, Math.ceil(secondsLeft))}초 뒤`;
    els.nextPreview.textContent = upcoming.text;
  } else {
    els.nextCountdown.textContent = "";
    els.nextPreview.textContent = "";
  }
}

function renderLibrary() {
  els.libraryList.innerHTML = state.library.map((item) => `
    <button class="show-item" data-show-id="${item.id}" type="button">
      <span class="show-title">${escapeHtml(item.title)}</span>
      <span class="show-meta">
        <span>문장 ${item.sentence_count || 0}</span>
        <span>포인트 ${item.relevant_sentence_count || 0}</span>
      </span>
    </button>
  `).join("");

  for (const button of els.libraryList.querySelectorAll("[data-show-id]")) {
    button.addEventListener("click", async () => {
      await loadShow(button.dataset.showId);
    });
  }
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

function bindEvents() {
  els.backButton.addEventListener("click", () => {
    if (state.isPlayerHistoryActive) {
      window.history.back();
      return;
    }
    returnToLibrary();
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
