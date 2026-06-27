const state = {
  library: [],
  readingLibrary: [],
  listeningLibrary: [],
  grammarLibrary: null,
  libraryMode: "",
  currentShow: null,
  currentReading: null,
  currentListeningTrack: null,
  currentListeningIndex: 0,
  currentListeningSectionTitle: "",
  selectedListeningSectionIndex: null,
  currentGrammarSet: null,
  currentGrammarIndex: 0,
  selectedGrammarChoice: null,
  grammarMistakes: [],
  grammarBookmarks: [],
  currentReadingIndex: 0,
  readingBookmarks: [],
  listeningBookmarks: [],
  isReadingBookmarkMode: false,
  isListeningBookmarkMode: false,
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
  grammarScreen: document.getElementById("grammar-screen"),
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
  readingBookmarkToggle: document.getElementById("reading-bookmark-toggle"),
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
  listeningAudio: document.getElementById("listening-audio"),
  listeningLoopToggle: document.getElementById("listening-loop-toggle"),
  listeningBookmarkToggle: document.getElementById("listening-bookmark-toggle"),
  listeningPrev: document.getElementById("listening-prev"),
  listeningNext: document.getElementById("listening-next"),
  grammarBackButton: document.getElementById("grammar-back-button"),
  grammarTitle: document.getElementById("grammar-title"),
  grammarProgress: document.getElementById("grammar-progress"),
  grammarNumber: document.getElementById("grammar-number"),
  grammarSection: document.getElementById("grammar-section"),
  grammarQuestion: document.getElementById("grammar-question"),
  grammarTranslation: document.getElementById("grammar-translation"),
  grammarOptions: document.getElementById("grammar-options"),
  grammarFeedback: document.getElementById("grammar-feedback"),
  grammarBookmarkToggle: document.getElementById("grammar-bookmark-toggle"),
  grammarPrev: document.getElementById("grammar-prev"),
  grammarNext: document.getElementById("grammar-next"),
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

const BOOKMARK_STORAGE_KEY = "jlpt-study-bookmarks-v1";

function loadBookmarks() {
  try {
    const saved = JSON.parse(localStorage.getItem(BOOKMARK_STORAGE_KEY) || "{}");
    state.readingBookmarks = Array.isArray(saved.reading) ? saved.reading : [];
    state.listeningBookmarks = Array.isArray(saved.listening) ? saved.listening : [];
    state.grammarMistakes = Array.isArray(saved.grammar) ? saved.grammar : [];
    state.grammarBookmarks = Array.isArray(saved.grammarBookmarks) ? saved.grammarBookmarks : [];
  } catch {
    state.readingBookmarks = [];
    state.listeningBookmarks = [];
    state.grammarMistakes = [];
    state.grammarBookmarks = [];
  }
}

function saveBookmarks() {
  localStorage.setItem(BOOKMARK_STORAGE_KEY, JSON.stringify({
    reading: state.readingBookmarks,
    listening: state.listeningBookmarks,
    grammar: state.grammarMistakes,
    grammarBookmarks: state.grammarBookmarks,
  }));
}

function readingBookmarkKey(readingId, itemIndex) {
  return `${readingId}:${itemIndex}`;
}

function listeningBookmarkKey(trackId, segmentIndex) {
  return `${trackId}:${segmentIndex}`;
}

function grammarBookmarkKey(question) {
  return question?.id || "";
}

function getCurrentReadingBookmarkInfo() {
  const item = (state.currentReading?.items || [])[state.currentReadingIndex] || null;
  if (!item) return null;
  const readingId = item.__bookmarkReadingId || state.currentReading?.id;
  const itemIndex = item.__bookmarkItemIndex || item.index;
  if (!readingId || itemIndex == null) return null;
  return {
    key: readingBookmarkKey(readingId, itemIndex),
    readingId,
    itemIndex,
    title: state.currentReading?.title || "독해",
  };
}

function getCurrentListeningBookmarkInfo() {
  const segment = getListeningSegments()[state.currentListeningIndex] || null;
  const track = state.currentListeningTrack;
  if (!segment || !track) return null;
  const trackId = segment.__bookmarkTrackId || track.id;
  const segmentIndex = segment.__bookmarkSegmentIndex || segment.index;
  if (!trackId || segmentIndex == null) return null;
  return {
    key: listeningBookmarkKey(trackId, segmentIndex),
    trackId,
    segmentIndex,
    title: segment.__trackTitle || track.title || "\uCCAD\uD574",
    sectionTitle: segment.__sectionTitle || state.currentListeningSectionTitle || "",
  };
}

function getCurrentGrammarBookmarkInfo() {
  const question = getGrammarQuestions()[state.currentGrammarIndex] || null;
  if (!question) return null;
  const key = grammarBookmarkKey(question);
  if (!key) return null;
  return {
    key,
    questionId: key,
    title: state.currentGrammarSet?.title || "\uBB38\uBC95",
    sectionTitle: question.__sectionTitle || question.section || "\uBB38\uBC95",
  };
}

function updateBookmarkButtons() {
  const readingInfo = getCurrentReadingBookmarkInfo();
  const readingActive = Boolean(readingInfo && state.readingBookmarks.some((item) => item.key === readingInfo.key));
  els.readingBookmarkToggle.classList.toggle("is-active", readingActive);
  els.readingBookmarkToggle.setAttribute("aria-pressed", readingActive ? "true" : "false");

  const listeningInfo = getCurrentListeningBookmarkInfo();
  const listeningActive = Boolean(listeningInfo && state.listeningBookmarks.some((item) => item.key === listeningInfo.key));
  els.listeningBookmarkToggle.classList.toggle("is-active", listeningActive);
  els.listeningBookmarkToggle.setAttribute("aria-pressed", listeningActive ? "true" : "false");

  const grammarInfo = getCurrentGrammarBookmarkInfo();
  const grammarActive = Boolean(grammarInfo && state.grammarBookmarks.some((item) => item.key === grammarInfo.key));
  if (els.grammarBookmarkToggle) {
    els.grammarBookmarkToggle.classList.toggle("is-active", grammarActive);
    els.grammarBookmarkToggle.setAttribute("aria-pressed", grammarActive ? "true" : "false");
    els.grammarBookmarkToggle.disabled = !grammarInfo;
  }
}

function setScreen(mode) {
  const isPlayer = mode === "player";
  const isReading = mode === "reading";
  const isListening = mode === "listening";
  const isGrammar = mode === "grammar";
  els.libraryScreen.classList.toggle("is-hidden", isPlayer || isReading || isListening || isGrammar);
  els.playerScreen.classList.toggle("is-hidden", !isPlayer);
  els.readingScreen.classList.toggle("is-hidden", !isReading);
  els.listeningScreen.classList.toggle("is-hidden", !isListening);
  els.grammarScreen.classList.toggle("is-hidden", !isGrammar);
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
  state.currentListeningSectionTitle = "";
  state.selectedListeningSectionIndex = null;
  state.currentGrammarSet = null;
  state.currentGrammarIndex = 0;
  state.selectedGrammarChoice = null;
  state.isReadingBookmarkMode = false;
  state.isListeningBookmarkMode = false;
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
  return { video: "\uC790\uB9C9", reading: "\uB3C5\uD574", listening: "\uCCAD\uD574", grammar: "\uBB38\uBC95" }[mode] || "";
}

function setLibraryHome() {
  state.libraryMode = "";
  state.selectedListeningSectionIndex = null;
  els.homeMenu.classList.remove("is-hidden");
  els.libraryListHeader.classList.add("is-hidden");
  els.libraryList.innerHTML = "";
  window.history.replaceState({ screen: "home" }, "", window.location.pathname + window.location.search);
}

function openLibraryMode(mode, pushHistory = true) {
  state.libraryMode = mode;
  state.selectedListeningSectionIndex = null;
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

function listeningCategoryGroups() {
  const groups = [
    { title: "\uCCAD\uD574", items: [] },
    { title: "\uBAA8\uC758\uACE0\uC0AC", items: [] },
  ];

  (state.listeningLibrary || []).forEach((section, index) => {
    const title = String(section.title || "");
    let label = title;
    let target = groups[0];
    const mock = title.match(/^\uC2E4\uC804\uBAA8\uC758\uACE0\uC0AC\s*(\d+)/u);
    const hackers = title.match(/^\uD574\uCEE4\uC2A4\s*N3\s*\uC2E4\uC804\uBAA8\uC758\uACE0\uC0AC\s*(\d+)\uD68C/u);

    if (title.startsWith("\uCCAD\uD574")) {
      label = title.replace(/^\uCCAD\uD574\s*/u, "");
    } else if (mock) {
      target = groups[1];
      label = `${String(Number(mock[1])).padStart(2, "0")}\uD68C`;
    } else if (hackers) {
      target = groups[1];
      label = `${String(Number(hackers[1]) + 3).padStart(2, "0")}\uD68C (H)`;
    }

    target.items.push({ section, index, label });
  });

  return groups.filter((group) => group.items.length);
}

function buildReadingBookmarkEntries() {
  const entries = [];
  const seen = new Set();
  for (const bookmark of state.readingBookmarks) {
    if (!bookmark?.readingId || bookmark.itemIndex == null || seen.has(bookmark.key)) continue;
    seen.add(bookmark.key);
    const reading = state.readingLibrary.find((item) => item.id === bookmark.readingId);
    const sourceItem = (reading?.items || []).find((item) => String(item.index) === String(bookmark.itemIndex));
    if (!reading || !sourceItem) continue;
    entries.push({
      ...sourceItem,
      __bookmarkReadingId: reading.id,
      __bookmarkItemIndex: sourceItem.index,
      __bookmarkSourceTitle: reading.title,
    });
  }
  return entries;
}

function buildListeningBookmarkEntries() {
  const entries = [];
  const seen = new Set();
  for (const bookmark of state.listeningBookmarks) {
    if (!bookmark?.trackId || bookmark.segmentIndex == null || seen.has(bookmark.key)) continue;
    seen.add(bookmark.key);
    const result = findListeningTrack(bookmark.trackId);
    const segment = (result?.track?.segments || []).find((item) => String(item.index) === String(bookmark.segmentIndex));
    if (!result || !segment || !result.track.site_audio) continue;
    entries.push({
      ...segment,
      __bookmarkTrackId: result.track.id,
      __bookmarkSegmentIndex: segment.index,
      __trackTitle: result.track.title,
      __sectionTitle: result.section.title || "",
      __siteAudio: result.track.site_audio,
    });
  }
  return entries;
}

function renderLibrary() {
  const isHome = !state.libraryMode;
  els.homeMenu.classList.toggle("is-hidden", !isHome);
  els.libraryListHeader.classList.toggle("is-hidden", isHome);
  els.versionBadge.classList.toggle("is-hidden", !isHome);
  els.libraryListTitle.textContent = modeTitle(state.libraryMode);
  els.libraryList.classList.toggle("library-list--grammar", state.libraryMode === "grammar");

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

  if (state.libraryMode === "grammar") {
    renderGrammarLibrary();
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
  const bookmarkCount = buildReadingBookmarkEntries().length;
  const bookmarkSection = `
    <section class="series-group bookmark-entry">
      <h2 class="series-group__title">북마크</h2>
      <div class="series-group__items series-group__items--compact series-group__items--study">
        <button class="show-item show-item--tile show-item--study" data-reading-bookmarks type="button" ${bookmarkCount ? "" : "disabled"}>
          <span class="show-title">${bookmarkCount ? "보기" : "없음"}</span>
        </button>
      </div>
    </section>
  `;
  els.libraryList.innerHTML = bookmarkSection + sections.map((section) => `
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
  const bookmarkButton = els.libraryList.querySelector("[data-reading-bookmarks]");
  bookmarkButton?.addEventListener("click", loadReadingBookmarks);
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

function grammarMistakeKey(question) {
  return question?.id || "";
}

function shuffleItems(items) {
  const copy = [...items];
  for (let index = copy.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [copy[index], copy[swapIndex]] = [copy[swapIndex], copy[index]];
  }
  return copy;
}

function getAllGrammarQuestions() {
  const entries = [];
  for (const section of state.grammarLibrary?.sections || []) {
    for (const question of section.questions || []) {
      entries.push({ ...question, __sectionTitle: section.title || "문법" });
    }
  }
  return entries;
}

function buildGrammarMistakeEntries() {
  const mistakeKeys = new Set(state.grammarMistakes);
  return getAllGrammarQuestions().filter((question) => mistakeKeys.has(grammarMistakeKey(question)));
}

function buildGrammarBookmarkEntries() {
  const bookmarkKeys = new Set(state.grammarBookmarks.map((item) => item?.key || item?.questionId || item).filter(Boolean));
  return getAllGrammarQuestions().filter((question) => bookmarkKeys.has(grammarBookmarkKey(question)));
}

function renderGrammarLibrary() {
  const sections = state.grammarLibrary?.sections || [];
  if (!sections.length) {
    els.libraryList.innerHTML = `<p class="bookmark-empty">\uBB38\uBC95 \uBB38\uC81C \uB370\uC774\uD130\uAC00 \uC544\uC9C1 \uC5C6\uC2B5\uB2C8\uB2E4.</p>`;
    return;
  }

  const mistakeCount = buildGrammarMistakeEntries().length;
  const bookmarkCount = buildGrammarBookmarkEntries().length;

  els.libraryList.innerHTML = `
    <section class="grammar-library">
      <div class="grammar-part-grid">
        ${sections.map((section, index) => `
          <button class="grammar-part-button" data-grammar-section-index="${index}" type="button">
            <span class="grammar-part-title">${escapeHtml(section.title || "\uBB38\uBC95")}</span>
          </button>
        `).join("")}
      </div>
      <div class="grammar-action-divider" aria-hidden="true"></div>
      <div class="grammar-action-grid">
        <button class="grammar-action-button" data-grammar-mistakes type="button" ${mistakeCount ? "" : "disabled"}>\uC624\uB2F5</button>
        <button class="grammar-action-button" data-grammar-bookmarks type="button" ${bookmarkCount ? "" : "disabled"}>\uBD81\uB9C8\uD06C</button>
        <button class="grammar-action-button" data-grammar-random type="button">\uB79C\uB364\uD480\uAE30</button>
      </div>
    </section>
  `;

  for (const button of els.libraryList.querySelectorAll("[data-grammar-section-index]")) {
    button.addEventListener("click", () => {
      loadGrammarSet(Number(button.dataset.grammarSectionIndex || 0));
    });
  }
  els.libraryList.querySelector("[data-grammar-mistakes]")?.addEventListener("click", loadGrammarMistakes);
  els.libraryList.querySelector("[data-grammar-bookmarks]")?.addEventListener("click", loadGrammarBookmarks);
  els.libraryList.querySelector("[data-grammar-random]")?.addEventListener("click", loadGrammarRandom);
}

function getGrammarQuestions() {
  return state.currentGrammarSet?.questions || [];
}

function loadGrammarSet(sectionIndex) {
  const section = (state.grammarLibrary?.sections || [])[sectionIndex];
  if (!section || !Array.isArray(section.questions) || !section.questions.length) return;
  stopPlayback();
  state.currentGrammarSet = {
    id: section.id || `grammar-${sectionIndex}`,
    title: section.title || "\uBB38\uBC95",
    questions: shuffleItems(section.questions.map((question) => ({ ...question, __sectionTitle: section.title || "\uBB38\uBC95" }))),
    isMistakeReview: false,
    isBookmarkReview: false,
  };
  state.currentGrammarIndex = 0;
  state.selectedGrammarChoice = null;
  setScreen("grammar");
  renderGrammarState();
}

function loadGrammarMistakes() {
  const questions = buildGrammarMistakeEntries();
  if (!questions.length) return;
  stopPlayback();
  state.currentGrammarSet = {
    id: "grammar-mistakes",
    title: "\uBB38\uBC95 \uC624\uB2F5",
    questions: shuffleItems(questions),
    isMistakeReview: true,
    isBookmarkReview: false,
  };
  state.currentGrammarIndex = 0;
  state.selectedGrammarChoice = null;
  setScreen("grammar");
  renderGrammarState();
}

function loadGrammarBookmarks() {
  const questions = buildGrammarBookmarkEntries();
  if (!questions.length) return;
  stopPlayback();
  state.currentGrammarSet = {
    id: "grammar-bookmarks",
    title: "\uBB38\uBC95 \uBD81\uB9C8\uD06C",
    questions,
    isMistakeReview: false,
    isBookmarkReview: true,
  };
  state.currentGrammarIndex = 0;
  state.selectedGrammarChoice = null;
  setScreen("grammar");
  renderGrammarState();
}

function buildBalancedGrammarRandomQuestions(limit) {
  const buckets = (state.grammarLibrary?.sections || [])
    .map((section) => shuffleItems((section.questions || []).map((question) => ({ ...question, __sectionTitle: section.title || "\uBB38\uBC95" }))))
    .filter((bucket) => bucket.length);
  const total = buckets.reduce((sum, bucket) => sum + bucket.length, 0);
  const target = Math.max(1, Math.min(Number(limit) || 1, total));
  const result = [];
  let cursor = 0;
  while (result.length < target && buckets.some((bucket) => bucket.length)) {
    const bucket = buckets[cursor % buckets.length];
    if (bucket.length) result.push(bucket.shift());
    cursor += 1;
  }
  return result;
}

function loadGrammarRandom() {
  const total = getAllGrammarQuestions().length;
  if (!total) return;
  const input = window.prompt(`\uBA87 \uBB38\uC81C\uB97C \uD480\uAE4C\uC694? (1-${total})`, "30");
  if (input === null) return;
  const count = Math.floor(Number(input));
  if (!Number.isFinite(count) || count <= 0) return;
  const questions = buildBalancedGrammarRandomQuestions(count);
  if (!questions.length) return;
  stopPlayback();
  state.currentGrammarSet = {
    id: "grammar-random",
    title: "\uBB38\uBC95 \uB79C\uB364\uD480\uAE30",
    questions,
    isMistakeReview: false,
    isBookmarkReview: false,
  };
  state.currentGrammarIndex = 0;
  state.selectedGrammarChoice = null;
  setScreen("grammar");
  renderGrammarState();
}

function toggleGrammarBookmark() {
  const info = getCurrentGrammarBookmarkInfo();
  if (!info) return;
  const index = state.grammarBookmarks.findIndex((item) => item.key === info.key);
  if (index >= 0) {
    state.grammarBookmarks.splice(index, 1);
    if (state.currentGrammarSet?.isBookmarkReview) {
      const questions = buildGrammarBookmarkEntries();
      if (!questions.length) {
        saveBookmarks();
        returnToLibrary();
        renderLibrary();
        return;
      }
      state.currentGrammarSet.questions = questions;
      state.currentGrammarIndex = Math.min(state.currentGrammarIndex, questions.length - 1);
    }
  } else {
    state.grammarBookmarks.push(info);
  }
  saveBookmarks();
  updateBookmarkButtons();
  if (state.libraryMode === "grammar") renderLibrary();
}

function recordGrammarAnswer(question, selected, answer) {
  const key = grammarMistakeKey(question);
  if (!key) return;
  const existingIndex = state.grammarMistakes.indexOf(key);
  if (selected === answer) {
    if (existingIndex >= 0) state.grammarMistakes.splice(existingIndex, 1);
  } else if (existingIndex < 0) {
    state.grammarMistakes.push(key);
  }
  saveBookmarks();
  if (state.libraryMode === "grammar") renderLibrary();
}

function renderGrammarOptionDetails(question) {
  const details = Array.isArray(question.option_explanations) ? question.option_explanations : [];
  if (!details.length) return "";
  const rows = details.map((item, index) =>
    `<div class="grammar-option-detail"><strong>${index + 1}. ${escapeHtml(item.option || "")}</strong><span>${escapeHtml(item.meaning || "")}</span></div>`
  ).join("");
  return `<div class="grammar-option-details">${rows}</div>`;
}
function renderGrammarState() {
  const questions = getGrammarQuestions();
  const question = questions[state.currentGrammarIndex] || null;
  els.grammarTitle.textContent = state.currentGrammarSet?.title || "문법";
  els.grammarProgress.textContent = questions.length ? `${state.currentGrammarIndex + 1} / ${questions.length}` : "0 / 0";
  els.grammarPrev.disabled = state.currentGrammarIndex <= 0 || !questions.length;
  els.grammarNext.disabled = state.currentGrammarIndex >= questions.length - 1 || !questions.length;

  if (!question) {
    els.grammarNumber.textContent = "";
    els.grammarSection.textContent = "";
    els.grammarQuestion.textContent = "";
    els.grammarTranslation.textContent = "";
    els.grammarOptions.innerHTML = "";
    els.grammarFeedback.textContent = "";
    return;
  }

  const answer = Number(question.answer ?? -1);
  const selected = state.selectedGrammarChoice;
  const isAnswered = selected !== null;
  els.grammarNumber.textContent = question.number ? `No. ${String(question.number).padStart(3, "0")}` : `No. ${String(state.currentGrammarIndex + 1).padStart(3, "0")}`;
  els.grammarSection.textContent = isAnswered && question.point ? `\uBB38\uBC95 \uD3EC\uC778\uD2B8: ${question.point}` : "";
  els.grammarQuestion.innerHTML = escapeHtml(question.question || "").replaceAll("\uFF3F\uFF3F\uFF3F", '<span class="grammar-blank">\uFF3F\uFF3F\uFF3F</span>');
  els.grammarTranslation.textContent = isAnswered ? (question.translation || "") : "";
  els.grammarOptions.innerHTML = (question.options || []).map((option, index) => {
    const classes = ["grammar-option"];
    if (isAnswered && index === answer) classes.push("is-correct");
    if (isAnswered && index === selected && index !== answer) classes.push("is-wrong");
    return `
      <button class="${classes.join(" ")}" data-grammar-choice="${index}" type="button" ${isAnswered ? "disabled" : ""}>
        <span class="grammar-option__number">${index + 1}</span>
        <span class="grammar-option__text">${escapeHtml(option)}</span>
      </button>
    `;
  }).join("");

  if (isAnswered) {
    const prefix = selected === answer ? "\uC815\uB2F5" : `\uC624\uB2F5 \u00B7 \uC815\uB2F5 ${answer + 1}\uBC88`;
    els.grammarFeedback.innerHTML = `
      <strong>${escapeHtml(prefix)}</strong>
      <span>${escapeHtml(question.explanation || "")}</span>
      ${renderGrammarOptionDetails(question)}
    `;
  } else {
    els.grammarFeedback.textContent = "";
  }

  updateBookmarkButtons();

  for (const button of els.grammarOptions.querySelectorAll("[data-grammar-choice]")) {
    button.addEventListener("click", () => {
      state.selectedGrammarChoice = Number(button.dataset.grammarChoice);
      recordGrammarAnswer(question, state.selectedGrammarChoice, answer);
      renderGrammarState();
    });
  }
}

function jumpGrammar(direction) {
  const questions = getGrammarQuestions();
  if (!questions.length) return;
  state.currentGrammarIndex = Math.max(0, Math.min(questions.length - 1, state.currentGrammarIndex + direction));
  state.selectedGrammarChoice = null;
  renderGrammarState();
}

function renderListeningLibrary() {
  const bookmarkCount = buildListeningBookmarkEntries().length;
  const bookmarkSection = `
    <section class="series-group bookmark-entry">
      <h2 class="series-group__title">\uBD81\uB9C8\uD06C</h2>
      <div class="series-group__items series-group__items--compact series-group__items--study">
        <button class="show-item show-item--tile show-item--study" data-listening-bookmarks type="button" ${bookmarkCount ? "" : "disabled"}>
          <span class="show-title">${bookmarkCount ? "\uBCF4\uAE30" : "\uC5C6\uC74C"}</span>
        </button>
      </div>
    </section>
  `;

  const selectedSection = state.selectedListeningSectionIndex === null
    ? null
    : (state.listeningLibrary || [])[state.selectedListeningSectionIndex];

  if (!selectedSection) {
    els.libraryListTitle.textContent = modeTitle("listening");
    els.libraryList.innerHTML = bookmarkSection + listeningCategoryGroups().map((group) => `
      <section class="series-group listening-category-entry">
        <h2 class="series-group__title listening-category-heading">${group.title}</h2>
        <div class="listening-category-grid">
          ${group.items.map((item) => `
            <button class="show-item show-item--tile listening-category-button" data-listening-section-index="${item.index}" type="button" title="${escapeHtml(item.section.title || "")}">
              <span class="show-title">${escapeHtml(item.label || "\uCCAD\uD574")}</span>
            </button>
          `).join("")}
        </div>
      </section>
    `).join("");

    for (const button of els.libraryList.querySelectorAll("[data-listening-section-index]")) {
      button.addEventListener("click", () => {
        state.selectedListeningSectionIndex = Number(button.dataset.listeningSectionIndex || 0);
        renderLibrary();
      });
    }
    els.libraryList.querySelector("[data-listening-bookmarks]")?.addEventListener("click", loadListeningBookmarks);
    return;
  }

  els.libraryListTitle.textContent = selectedSection.title || modeTitle("listening");
  els.libraryList.innerHTML = bookmarkSection + `
    <section class="series-group listening-track-entry">
      ${groupListeningTracks(selectedSection).map((group) => `
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
  `;

  for (const button of els.libraryList.querySelectorAll("[data-listening-id]")) {
    button.addEventListener("click", () => {
      loadListeningTrack(button.dataset.listeningId);
    });
  }
  els.libraryList.querySelector("[data-listening-bookmarks]")?.addEventListener("click", loadListeningBookmarks);
}

function renderReadingState() {
  const reading = state.currentReading;
  const items = reading?.items || [];
  const item = items[state.currentReadingIndex] || null;
  const reveal = Boolean(els.readingRevealToggle.checked);
  const isFull = !state.isReadingBookmarkMode && Boolean(els.readingFullToggle.checked);

  els.readingTitle.textContent = reading ? reading.title : "독해";
  els.readingProgress.textContent = items.length ? `${state.currentReadingIndex + 1} / ${items.length}` : "0 / 0";
  els.readingFullToggle.disabled = state.isReadingBookmarkMode;
  els.readingPanel.classList.toggle("is-revealed", reveal || isFull);
  els.readingPanel.classList.toggle("is-full-view", isFull);
  els.readingPrev.classList.toggle("is-hidden", isFull);
  els.readingNext.classList.toggle("is-hidden", isFull);

  if (isFull) {
    const passageItems = getCurrentReadingPassageItems();
    els.readingSentence.innerHTML = renderReadingFullView(passageItems);
    els.readingTranslation.textContent = "";
    return;
  }

  els.readingSentence.innerHTML = renderHighlightedSentence(item);
  els.readingTranslation.textContent = item?.translation || "";
  updateBookmarkButtons();
}

function getCurrentReadingPassageItems() {
  const items = state.currentReading?.items || [];
  const item = items[state.currentReadingIndex] || null;
  if (!item?.passage_id) return item ? [item] : [];
  return items.filter((entry) => entry.passage_id === item.passage_id);
}

function renderReadingQuiz(passage) {
  const quiz = passage?.reading_quiz || passage?.quiz || null;
  if (!quiz?.question) return "";
  const options = Array.isArray(quiz.options) ? quiz.options : [];
  const hasAnswer = Number.isInteger(quiz.answer) && quiz.answer >= 0 && quiz.answer < options.length;
  const fallback = "\uC9C0\uBB38 \uADFC\uAC70\uC640 \uBCF4\uAE30\uB97C \uB300\uC870\uD574 \uD655\uC778\uD569\uB2C8\uB2E4.";
  return `
    <section class="reading-full__quiz">
      <div class="reading-full__quiz-label">JLPT N3 \uB3C5\uD574 \uBB38\uC81C</div>
      <p class="reading-full__quiz-question">${escapeHtml(quiz.question)}</p>
      ${options.length ? `
        <ol class="reading-full__quiz-options">
          ${options.map((option, index) => `
            <li class="${hasAnswer && index === quiz.answer ? "is-answer" : ""}">
              <span class="reading-full__quiz-number">${index + 1}</span>
              <span>${escapeHtml(option)}</span>
            </li>
          `).join("")}
        </ol>
      ` : ""}
      <details class="reading-full__quiz-answer">
        <summary>${hasAnswer ? "\uC815\uB2F5/\uD574\uC124 \uBCF4\uAE30" : "\uD480\uC774 \uD3EC\uC778\uD2B8 \uBCF4\uAE30"}</summary>
        ${hasAnswer ? `<p><strong>\uC815\uB2F5 ${quiz.answer + 1}\uBC88.</strong> ${escapeHtml(quiz.explanation || fallback)}</p>` : `<p>${escapeHtml(quiz.explanation || fallback)}</p>`}
      </details>
    </section>
  `;
}

function renderReadingFullView(items) {
  if (!items.length) return "";
  const title = items[0].passage_title || "";
  const passage = findCurrentReadingPassage();
  const question = passage?.question || "";
  return `
    <article class="reading-full">
      <h3 class="reading-full__title">${escapeHtml(title)}</h3>
      ${question ? `<p class="reading-full__question">${escapeHtml(question)}</p>` : ""}
      ${items.map((item) => `
        <section class="reading-full__item">
          <p class="reading-full__sentence">${renderHighlightedSentence(item)}</p>
          <p class="reading-full__translation">${escapeHtml(item.translation || "")}</p>
        </section>
      `).join("")}
      ${renderReadingQuiz(passage || items[0])}
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

  els.listeningTrackTitle.textContent = segment?.__trackTitle || track?.title || "";
  els.listeningProgress.textContent = segments.length ? `${state.currentListeningIndex + 1} / ${segments.length}` : "전사 대기";
  els.listeningSentence.innerHTML = segment ? renderHighlightedSentence(segment) : escapeHtml(track?.text || "");
  els.listeningTranslation.textContent = segment?.translation || "";
  els.listeningPrev.disabled = state.currentListeningIndex <= 0 || segments.length === 0;
  els.listeningNext.disabled = state.currentListeningIndex >= segments.length - 1 || segments.length === 0;
  els.listeningLoopToggle.disabled = segments.length === 0;
  updateListeningBookmarkAudio();
  updateBookmarkButtons();
}

function isListeningLoopEnabled() {
  return els.listeningLoopToggle.getAttribute("aria-pressed") === "true";
}

function setListeningLoopEnabled(enabled) {
  els.listeningLoopToggle.setAttribute("aria-pressed", enabled ? "true" : "false");
  els.listeningLoopToggle.classList.toggle("is-active", enabled);
}

function updateListeningBookmarkAudio() {
  if (!state.isListeningBookmarkMode) return;
  const segment = getListeningSegments()[state.currentListeningIndex];
  if (!segment?.__siteAudio) return;
  const audioUrl = segment.__siteAudio;
  const wasPlaying = !els.listeningAudio.paused;
  if (els.listeningAudio.getAttribute("src") !== audioUrl) {
    els.listeningAudio.src = audioUrl;
    els.listeningAudio.currentTime = Number(segment.start_seconds || 0);
  }
  const start = Number(segment.start_seconds || 0);
  const end = Number(segment.end_seconds || start);
  if (els.listeningAudio.currentTime < start - 0.08 || els.listeningAudio.currentTime >= end) {
    els.listeningAudio.currentTime = start;
  }
  if (wasPlaying) {
    els.listeningAudio.play();
  }
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

  if (state.isListeningBookmarkMode && current) {
    const start = Number(current.start_seconds || 0);
    const end = Number(current.end_seconds || start);
    if (currentTime < start - 0.08) {
      els.listeningAudio.currentTime = start;
      return;
    }
    if (currentTime >= Math.max(start, end - 0.04)) {
      if (isListeningLoopEnabled()) {
        restartCurrentListeningSegment();
      } else {
        els.listeningAudio.pause();
        els.listeningAudio.currentTime = start;
      }
    }
    return;
  }

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
  try {
    state.grammarLibrary = await fetchJson("./data/jlpt/grammar/n3_grammar_quiz.json");
  } catch {
    state.grammarLibrary = null;
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
  state.isReadingBookmarkMode = false;
  els.readingRevealToggle.checked = false;
  els.readingFullToggle.checked = false;
  els.readingFullToggle.disabled = false;
  setScreen("reading");
  renderReadingState();
}

function loadReadingBookmarks() {
  const items = buildReadingBookmarkEntries();
  if (!items.length) return;
  stopPlayback();
  state.currentReading = {
    id: "reading-bookmarks",
    title: "독해 북마크",
    items,
    isBookmarkList: true,
  };
  state.currentReadingIndex = 0;
  state.isReadingBookmarkMode = true;
  els.readingRevealToggle.checked = true;
  els.readingFullToggle.checked = false;
  els.readingFullToggle.disabled = true;
  setScreen("reading");
  renderReadingState();
}

function loadListeningTrack(trackId) {
  const result = findListeningTrack(trackId);
  if (!result || !result.track.site_audio) return;

  stopPlayback();
  state.currentListeningTrack = result.track;
  state.currentListeningIndex = 0;
  state.currentListeningSectionTitle = result.section.title || "";
  state.isListeningBookmarkMode = false;
  els.listeningTitle.textContent = "청해";
  els.listeningSection.textContent = result.section.title || "";
  setListeningLoopEnabled(false);
  els.listeningAudio.loop = false;
  els.listeningAudio.src = result.track.site_audio;
  setScreen("listening");
  renderListeningState();
}

function loadListeningBookmarks() {
  const segments = buildListeningBookmarkEntries();
  if (!segments.length) return;
  stopPlayback();
  state.currentListeningTrack = {
    id: "listening-bookmarks",
    title: "청해 북마크",
    site_audio: segments[0].__siteAudio,
    segments,
  };
  state.currentListeningIndex = 0;
  state.currentListeningSectionTitle = "북마크";
  state.isListeningBookmarkMode = true;
  els.listeningTitle.textContent = "청해 북마크";
  els.listeningSection.textContent = "북마크";
  setListeningLoopEnabled(false);
  els.listeningAudio.loop = false;
  els.listeningAudio.src = segments[0].__siteAudio;
  els.listeningAudio.currentTime = Number(segments[0].start_seconds || 0);
  setScreen("listening");
  renderListeningState();
}

function jumpReading(direction) {
  const items = state.currentReading?.items || [];
  if (!items.length) return;
  state.currentReadingIndex = Math.max(0, Math.min(items.length - 1, state.currentReadingIndex + direction));
  renderReadingState();
}

function toggleReadingBookmark() {
  const info = getCurrentReadingBookmarkInfo();
  if (!info) return;
  const existingIndex = state.readingBookmarks.findIndex((item) => item.key === info.key);
  if (existingIndex >= 0) {
    state.readingBookmarks.splice(existingIndex, 1);
  } else {
    state.readingBookmarks.push(info);
  }
  saveBookmarks();
  if (state.isReadingBookmarkMode && existingIndex >= 0) {
    const items = buildReadingBookmarkEntries();
    if (!items.length) {
      returnToLibrary();
      renderLibrary();
      return;
    }
    state.currentReading.items = items;
    state.currentReadingIndex = Math.min(state.currentReadingIndex, items.length - 1);
  }
  renderReadingState();
  if (state.libraryMode === "reading") renderLibrary();
}

function toggleListeningBookmark() {
  const info = getCurrentListeningBookmarkInfo();
  if (!info) return;
  const existingIndex = state.listeningBookmarks.findIndex((item) => item.key === info.key);
  if (existingIndex >= 0) {
    state.listeningBookmarks.splice(existingIndex, 1);
  } else {
    state.listeningBookmarks.push(info);
  }
  saveBookmarks();
  if (state.isListeningBookmarkMode && existingIndex >= 0) {
    const segments = buildListeningBookmarkEntries();
    if (!segments.length) {
      returnToLibrary();
      renderLibrary();
      return;
    }
    state.currentListeningTrack.segments = segments;
    state.currentListeningIndex = Math.min(state.currentListeningIndex, segments.length - 1);
  }
  renderListeningState();
  if (state.libraryMode === "listening") renderLibrary();
}

function bindEvents() {
  els.homeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      openLibraryMode(button.dataset.libraryMode || "video");
    });
  });
  els.libraryBackButton.addEventListener("click", () => {
    if (state.libraryMode === "listening" && state.selectedListeningSectionIndex !== null) {
      state.selectedListeningSectionIndex = null;
      els.libraryListTitle.textContent = modeTitle("listening");
      renderLibrary();
      return;
    }
    setLibraryHome();
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
  els.readingFullToggle.addEventListener("change", renderReadingState);
  els.readingBookmarkToggle.addEventListener("click", toggleReadingBookmark);
  els.readingPrev.addEventListener("click", () => jumpReading(-1));
  els.readingNext.addEventListener("click", () => jumpReading(1));
  els.listeningBackButton.addEventListener("click", returnToLibrary);
  els.listeningBookmarkToggle.addEventListener("click", toggleListeningBookmark);
  els.listeningLoopToggle.addEventListener("click", () => {
    setListeningLoopEnabled(!isListeningLoopEnabled());
    els.listeningAudio.loop = false;
  });
  els.listeningPrev.addEventListener("click", () => jumpListening(-1));
  els.listeningNext.addEventListener("click", () => jumpListening(1));
  els.grammarBackButton.addEventListener("click", returnToLibrary);
  els.grammarBookmarkToggle?.addEventListener("click", toggleGrammarBookmark);
  els.grammarPrev.addEventListener("click", () => jumpGrammar(-1));
  els.grammarNext.addEventListener("click", () => jumpGrammar(1));
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
    if (state.currentShow || state.currentReading || state.currentListeningTrack || state.currentGrammarSet) {
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
  loadBookmarks();
  bindEvents();
  await loadLibrary();
  if (window.location.hash) {
    const mode = window.location.hash.replace("#", "");
    if (["video", "reading", "listening", "grammar"].includes(mode)) {
      openLibraryMode(mode, false);
    }
  }
}

main().catch((error) => {
  console.error(error);
  els.currentSentence.textContent = error.message;
});
