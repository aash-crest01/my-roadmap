# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal Data/AI learning roadmap delivered as a **single self-contained file, `roadmap.html`** (no build, no dependencies, no server). Open it in a browser to run it. The folder is GitHub Pages-ready as is: `index.html` only forwards to `roadmap.html`, and `.nojekyll` turns off Jekyll. `README.md` is the short project overview; `ROADMAP_GUIDE.md` is the end-user guide (instruction-box syntax, editing form, data schema, where course sources were mapped) — keep it in sync when behaviour or the schema changes.

Note: the enclosing git repository is rooted at the user's home directory (`C:\Users\lenovo`), not this folder. Do not commit unless asked.

## Validating changes

Run the browser smoke test after any change to `roadmap.html` (needs Python and Chrome or Edge, about a minute, no network except loading the Anthropic SDK from the CDN):

```sh
python dev/run_smoke.py
```

`dev/run_smoke.py` serves the project folder, mocks the OpenAI-compatible, Anthropic and GitHub Gist APIs, opens `dev/smoke.html` in headless Chrome/Edge (own temporary profile, terminated afterwards) and prints PASS/FAIL per check. Each check loads `roadmap.html` fresh in an iframe and drives it through the DOM and `window.__roadmap`. Add a `test(...)` there for new behaviour. Node is not installed.

After editing the data block, also check that it still parses and ids are unique:

```sh
python -c "import json;s=open('roadmap.html',encoding='utf-8').read();a=s.index('/*ROADMAP_START*/')+17;b=s.index('/*ROADMAP_END*/');d=json.loads(s[a:b]);ids=[n['id'] for t in d['tracks'] for n in t['nodes']];print(len(ids),'nodes',len(ids)-len(set(ids)),'dup ids')"
```

For behaviour, open the page and use the debug hook in the console: `window.__roadmap.run('push pandas by 1 week')`, plus `.parseDate`, `.parseSched`, `.data()`, `.state()`, `.status(id)`, `.occ`, `.reminders()`, `.syncNow()`. The page also reports schema problems (duplicate ids, unknown `dependsOn`/`attachTo` ids, bad dates) collected in `buildIndex()`.

## Architecture

`roadmap.html` has three parts: `<style>` (CSS with `--var` tokens, light/dark via `:root[data-theme]`), a first `<script>` holding only the content, and a second `<script>` IIFE with all app code.

**Content block.** `const ROADMAP = /*ROADMAP_START*/{...}/*ROADMAP_END*/;` must stay **strict JSON** between the markers (double quotes, no trailing commas, no comments) because:
- the app hashes it (`BASE_HASH`) to detect whether browser edits differ from the file, and
- `downloadRoadmap()` rewrites the page by splicing `fmtJSON(DATA)` between those exact markers in `SOURCE` (the page's own `outerHTML` captured at startup). Never rename or duplicate the marker comments; the app code builds them as `'/*ROADMAP_'+'START*/'` so the code itself doesn't match.

Shape: `meta` (title, goal, `goalDate`, `calendarNote`, `phases[]` used by the Overview timeline) and `tracks[]` (`id, name, color, blurb, nodes[]`). Node fields are documented in `ROADMAP_GUIDE.md` §6. Key semantics: `type:"branch"` + `attachTo` = side step rendered beside a main step; `dependsOn` can cross tracks and only shows "needs N" (nothing is locked); main steps are kept in date order. Node `id`s and checklist item `id`s are persistence keys — renaming them orphans saved progress.

**Two layers of state (localStorage):**
- `roadmap-progress-v1` (`state`): `status`, `notes`, `checks` (keyed `nodeId::itemId`), `doneAt`, `sched` (calendar study blocks). Progress is never written into the HTML; Export/Import progress handles backups.
- `roadmap-custom-v2` (`custom`): a full edited copy of the roadmap data from the instruction box / Edit form. On load, `init()` uses it instead of `ROADMAP` if present; it is auto-cleared when its hash equals the file's. The banner (`renderBanner`) handles the "file vs browser edits" conflict.

Runtime globals: `DATA`/`TRACKS`/`META` (active data), `INDEX` (id → `{node, track}`), `UNLOCKS` (reverse deps). Any data mutation goes through `pushHistory()` (session undo) then `commit()`/`saveCustom()` and `renderAll()`.

**Status** is derived: `getStatus()` uses an explicit `state.status` override if set, else `autoStatus()` from checklist progress (first tick → doing, all → done). Skipped steps are excluded from percentages.

**Instruction box.** `runCommand()` is an ordered chain of regexes (first match wins): help/undo → `runScheduleCommand()` (calendar commands) → notes, links, rename, status, move/push dates, add/delete, deps, etc. Step names resolve fuzzily via `findNodes()`; ambiguous matches go through `pick()` which shows choice buttons; bulk changes show a preview before applying. Dates go through `parseDateText()` (day-first numeric dates; a yearless date is this year unless that is more than 60 days ago, then next year); calendar times through `parseSchedule()`/`parseTimeTok()` (bare `at 1`–`6` means pm). When adding a command, place its regex so it doesn't shadow existing ones, and add an example to `helpBox()` and the guide's tables.

**AI assistant** (section `AI ASSISTANT`, just before `init`). `aiRoute()` in the submit handler decides whether input goes to the model (AI toggle on, or an `ai:` prefix) or to `runCommand()`. `aiAsk()` runs a provider-neutral tool loop: `AI_TOOLS` (neutral JSON Schemas) + `AI_IMPL` (handlers that mutate `DATA`/`state` with the same helpers as the form and instruction box) + `ADAPTERS`, which handle the two request formats. `anthropic` uses the official SDK, loaded lazily via `import()` from a pinned jsDelivr URL (`AI_SDK_URL`; the only external script, and only on first use). It sends refusal fallbacks and effort only for the models that accept them. `openai` is raw `fetch` to any OpenAI-compatible `/chat/completions` (`AI_PROVIDERS` holds the presets). Handlers validate everything before calling `aiMut()`, whose first call in a turn does `pushHistory()`, so one AI instruction is exactly one undo step. Settings and per-provider keys live in localStorage `roadmap-ai-v1` and must never reach `state`, `DATA` or the downloaded file. To add a tool, add a schema to `AI_TOOLS` and a handler to `AI_IMPL` that throws on bad input (errors are returned to the model as `is_error` tool results) and pushes a human-readable line to `aiChanges`.

**Gist sync** (section `SYNC THROUGH A GITHUB GIST`). Optional; on when localStorage `roadmap-sync-v1` holds a GitHub token (it also stores `gist` id, `device`, `lastSeen` = `savedAt` of the last copy read or written, and a persisted `dirty` flag). `save()` and `saveCustom()` call `syncDirty()`, which marks the copy dirty and debounces `syncNow()`. `syncOnce()` always reads the gist first: changed elsewhere and not dirty → `syncApply()` (validated, one undo step); changed elsewhere and dirty → `syncConflict` banner, the user picks; dirty only → `syncPush()`. The first connect lists the user's gists to find `roadmap-sync.json` (another device's) or creates a secret gist. Payload: `state` + `roadmap` (only when `custom` exists) + `roadmapBase`. While applying remote data `syncApplying` stops `syncDirty()` from echoing it back. With sync on, the "download your edits" banner is hidden.

**Data from outside** (backups, sync) goes through `cleanProgress()` / `cleanSched()` / `checkRoadmap()`, which throw on damaged input so nothing changes.

**Views.** Tabs: `week` (This week), `cal` (Calendar: day/week/month grid, recurring blocks via `occurrences()`, `.ics` export, browser notifications), `all` (Overview timeline by `meta.phases`), then one tab per track (`renderTrack` → `rowsFor` lays out main steps down a centre line with branches to the right). Cards and timeline steps are wrapped (`.cw` / `nodeWrap()` → `.nw`) so the one-click `quickTick()` button can sit beside the card button without nesting buttons; it toggles done with `toastUndo()`, or opens the checklist for checklist steps. `renderTrack()` marks the first unfinished main step `.is-next` and inserts a "Today" line; `setTab()` scrolls a track to `.is-next`. `sessionList()` renders today's sessions on both This week and Calendar. The legend and goal line show only on Overview (`renderView()`); This week is a two-column dashboard (`.dash`) with its own goal card, streak (`activityByDay()`/`streakDays()`) and per-track progress, and Overview adds track rings (`ringSvg()`), a 12-week `heatmap()` and the phases list. Status is drawn everywhere by `statusIcon()` (ring / half / check / slash, or a filling ring for checklist steps). The track timeline is a grid of month label | spine with the `quickTick()` | step and side steps (`.r-month`/`.r-spine`/`.r-body`). The side panel (`#panel`) shows a step, its checklist, the Edit form and the calendar block form; `setPanelInert()` makes the closed panel (or, while it is open, the page behind it) `inert`, and `trapPanelTab()` keeps Tab inside it. Tabs use the roving-tabindex pattern (`tabKeys()`: arrows, Home, End).

## Editing conventions

- Large edits to content: edit the JSON directly and re-run the validation command. Text inside JSON must not contain `</script` (download escapes `</` → `<\/`).
- Keep the file self-contained: no external scripts, styles or fonts (the lazily imported Anthropic SDK is the one deliberate exception).
- AI and sync are tested against the mocks in `dev/run_smoke.py`, never real keys. Never kill all `chrome.exe` processes; the runner terminates only the browser it started.
- Secrets (`roadmap-ai-v1`, `roadmap-sync-v1`) must never reach `state`, `DATA`, exports, the gist payload or the downloaded file; a smoke check guards this.
- Checklists over 30 items (DSA sheets) are intentionally not editable in the form, to avoid wiping them.
