# Data and AI Roadmap

A personal study roadmap in a single web page: six tracks (degree, math, Python and ML, DSA, backend, career) on a timeline toward the Fusemachines AI Fellowship, with checklists, a study calendar, a plain-English instruction box and an optional AI assistant.

**Open it:** double-click `roadmap.html`, or visit the GitHub Pages address of this repository. There is nothing to install or build.

## What it does

- **This week, Calendar, Overview** and one tab per track, with progress for every step and checklist item.
- **Instruction box:** type `solved two sum`, `push dsa by 2 weeks` or `schedule math every mon wed at 7am for 45 min`.
- **AI assistant** (optional): turn on the **AI** button and write anything. Works with Claude, OpenAI, Gemini, OpenRouter, Groq, Mistral, DeepSeek, Ollama or any OpenAI-compatible API, using your own key.
- **Sync across devices** (optional): connect a GitHub token once per device and your progress, notes, calendar and step edits save to a secret gist automatically. No downloads needed.
- **Backups:** Export / Import progress, `.ics` calendar export, and Download updated roadmap to write your edits into the file itself.

The full user guide is in [ROADMAP_GUIDE.md](ROADMAP_GUIDE.md).

## Put it on GitHub Pages

1. Push this folder to a GitHub repository.
2. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. After a minute it is live at `https://<your-username>.github.io/<repository>/`. `index.html` forwards to `roadmap.html`, so nothing needs renaming.

Your progress lives in the browser (or in your sync gist), not in the repository, so the repository can be public. Keys and tokens are stored only in each browser and are never written into any file.

## Files

| File | What it is |
|---|---|
| `roadmap.html` | The whole app: styles, roadmap content (between `/*ROADMAP_START*/` and `/*ROADMAP_END*/`) and code |
| `index.html` | Forwards the GitHub Pages address to `roadmap.html` |
| `ROADMAP_GUIDE.md` | User guide |
| `CLAUDE.md` | Notes for working on the code |
| `dev/` | Smoke test: `python dev/run_smoke.py` (needs Python and Chrome or Edge; uses mock APIs, no keys) |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are |
