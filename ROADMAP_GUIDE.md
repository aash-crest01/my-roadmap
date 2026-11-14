# Roadmap guide

## 1. What is in this version

- **Overview tab** (called Whole roadmap before). Summary tiles, a progress ring per track, a 12-week activity grid, the 5 phases with "You are here", then every track on one timeline grouped by phase and month, with a red "Today" line and filters (hide a track, hide finished steps, hide side steps).
- **Progress tab.** A dashboard of how you are doing (section 2b).
- **This week dashboard.** What is due, overdue and in progress on the left; on the right your goal countdown, today's sessions (with a one-click "Book 30 min" for the next step that has no time booked), progress per track and a 7-day study streak.
- **Checklists you tick one by one.**
  - DSA: all 267 items of your Code and Debug "Master DSA with LeetCode" sheet, each with its Problem, Video and Notes links. The 166 extra problems from the "Zero to Hero" sheet sit in dashed "Advanced set" side steps for a second pass.
  - Math: the 16 Khan Academy Statistics and probability units. Units 3 and 4 are already ticked because your screenshot shows them at Proficient.
- **Status follows your ticks.** A step with a checklist turns In progress after the first tick and Done after the last. You can still override it.
- **Plain-English instruction box** at the top of the page (section 3).
- **Edit button** on every step, plus "+ Add step" on every track (section 4).
- **OSSU Data Science courses** added as free resources and optional "OSSU depth" side steps (section 7).
- **Calendar tab** with a live clock, a day / week / month view and study blocks you schedule yourself (section 3a).
- **Sync across devices** through a secret GitHub gist: progress, notes, calendar and step edits save automatically, so you no longer need to download after each change (section 8a).
- **AI assistant** (AI button in the instruction box): write any change in your own words and Claude, or a model from another provider, edits the roadmap and calendar for you (section 3b).

## 2. Finding your way around

- The bar at the top stays visible: title, an overall progress ring (click it to open Overview), the instruction box, help (?) and dark/light mode. A thin green line under it fills up as you finish steps.
- The tabs below it are split in two: views (This week, Calendar, Overview, Progress) on the left, then one tab per track with a small progress ring and its percentage. Swipe or scroll the tabs sideways to see the rest.
- Results of an instruction appear in a small box under the instruction field, on top of the page. Simple confirmations close by themselves after a few seconds; click anywhere else or press Esc to close them sooner.
- On a phone, the title row hides when you scroll down so only the instruction box and tabs stay pinned.
- Keyboard: press `/` to jump to the instruction box, `?` for examples, `Esc` to close boxes and panels.

## 2a. Daily use

1. Open **This week**. The left column lists anything overdue, what is due in the next 7 days, other steps in progress and what comes next. The right column shows the goal countdown, today's booked sessions, progress per track and your study streak.
2. Click the round status icon on a card or timeline step to mark it done in one click. A message appears with **Undo** for a few seconds. Steps with a checklist show a list icon whose ring fills as you tick; clicking it opens the checklist, because their status follows your ticks.
3. Or click a step to open it and pick a status, or type what you did in the instruction box, for example `solved two sum`.

The status icon means: empty ring = not started, half-filled = in progress, green check = done, dashed ring with a slash = skipped. The key is on the Overview tab.

Each track tab opens at your first unfinished step, marked "You are here". The timeline runs down a line with month labels on the left; the line is coloured up to where you are, a red "Today" line marks the date, and side steps sit to the right (below on a phone). "Book study time" in the track header schedules a session for that track.

The study streak and the activity grid count a day as active when you tick a checklist item, finish a step or mark a study session done.

"Done" means you can do it again from a blank page without notes. If not, leave it In progress.

## 2b. The Progress tab

Pick the period at the top (last 4 weeks, 12 weeks or 6 months). Everything below uses it.

- **Tiles:** steps done, pace (how many steps ahead of or behind the dates in the roadmap), checklist items ticked, study time done (and booked) and your streak with your best one.
- **Planned vs done:** a dashed line counts steps by their dates, the solid line counts steps you finished. Where the solid line is above the dashed one at "Today", you are ahead. Point at the chart (or focus it and use the arrow keys) to read any day.
- **Pace by track:** the bar is how much of the track is done; the thin line is how much was due by today. Click a row to open the track.
- **Checklists:** checklist steps, the ones you have started first. Click one to open it.
- **Done per week** and **Study time per week:** columns per week. Study time counts calendar sessions you marked done, split by track.
- **Recently finished:** the last 10 ticks and finished steps.

Every chart has **Show as table** for the exact numbers. A checklist step that finished by its ticks counts as done on the day of its last tick.

## 3. The instruction box (plain English)

Type what changed and press Enter. Step names can be partial ("pandas", "sql course"). Every step also shows its id at the bottom of its panel (for example `dsa-graph`), which always works. If a name matches more than one step, you get buttons to pick the right one. Big changes (moving many steps, adding, deleting) show a preview with an Apply button first.

| You want to | Type |
|---|---|
| Tick a problem or unit | `solved two sum`, `unit 5 done`, `reverse a linked list done` |
| Untick | `untick reverse a number` |
| Set a status | `finished numpy`, `start sql practice`, `mark pandas in progress`, `skip mongodb`, `reset pandas` |
| Move one step to a date | `move pandas to 20 dec`, `move numpy to 2027-01-15`, `move linux to next friday` |
| Push one step | `push docker compose by 1 week`, `bring forward linux by 2 days` |
| Push a step and the rest of its track | `push sql course and everything after it by 1 week` |
| Push a whole track | `push dsa by 2 weeks`, `push all math by 10 days` |
| Push everything | `push everything by 3 days`, `push everything after 1 jan by 1 week` |
| Add a step | `add "Learn Git rebase" to backend on 5 jan` |
| Add a side step | `add side step "Watch CS50 SQL" under sql course on 20 nov` |
| Rename or delete | `rename linux basics to Linux and bash`, `delete mongodb` |
| Move a step to another track | `move big data one-pager to python track` |
| Dependencies | `make docker depend on linux` |
| Verify tag | `verify pandas` (add tag), `confirm fusemachines application` (remove tag) |
| Notes and links | `note pandas: redo groupby`, `add link My playlist https://... to dsa1` |
| Find a step | `open graphs` |
| Reverse the last change | `undo` |
| See examples | `help` or the `?` button |

Dates it understands: `20 dec`, `dec 20`, `20 december 2027`, `2027-01-15`, `5/1/2027` (day/month/year), `today`, `tomorrow`, `friday`, `next week`, `in 2 weeks`, `end of month`. A date without a year means this year, unless that date was more than 60 days ago, in which case it means next year. So in November, `1 oct` is last month and `5 jan` is January next year.

Undo works for the current visit. After a reload, fix mistakes with a new instruction or the Edit button.

## 3a. The calendar

The **Calendar** tab shows a live clock, what is happening now and next, today's sessions, and a day, week or month grid. The red line is the current time. Roadmap due dates appear in the "due" row at the top of each day, and the **Due soon with no time booked** list at the bottom shows steps coming up that have no time reserved yet, each with a **Book time** button.

**Scheduling work**

- Tap an empty time in the day or week grid, or click **+ Schedule work**, or open any step and press **+ Schedule time for this**.
- A study block has: the step it is for (optional), a title, date, start time, length, repeat (none, every day, weekdays, or weekly on chosen days), an "until" date and a note. Blocks take the colour of their track.
- Tap a block to **mark this session done**, open its step, change it, **skip this session only** (for repeating blocks) or delete it.
- Or type it in the instruction box:

| You want to | Type |
|---|---|
| A daily session | `schedule dsa every day at 7pm for 1 hour` |
| One session for a step | `schedule pandas tomorrow 6pm for 90 min`, `schedule linux on saturday 10am for 2 hours` |
| Chosen days | `schedule math every mon wed fri at 7:30am for 45 min until 20 dec` |
| Weekdays with start and end | `schedule sql course weekdays 8pm to 9pm` |
| Something that is not a step | `schedule gym at 6am daily` |
| Change the time | `move dsa session to 8pm` |
| Mark today's session done | `did my dsa session` |
| Free a day | `clear schedule on friday` (repeating blocks are skipped that day only) |
| Remove a block and its repeats | `unschedule gym` |
| Jump to the calendar | `today` or `calendar` |
| Open the Progress dashboard | `progress`, `dashboard` or `how am i doing` |

A time written without am/pm, like `at 7`, is read as evening (7pm) for 1 to 6, and as written otherwise (`at 10` is 10am). Put the step name first and the time after it.

**Reminders and other calendars**

- **Turn on reminders**: the browser asks permission once; after that a notification and a message appear when a session starts, while the page is open in a tab.
- **Export .ics** downloads the next 4 months of sessions as a file you can import into Google Calendar, Apple Calendar or Outlook.
- Sessions are saved in this browser with your progress and are included in **Export progress** backups. They are not written into `roadmap.html`.

## 3b. The AI assistant

The instruction box only understands the phrasings in the tables above. The **AI** button in the box sends what you type to an AI model instead, so you can write anything, including several changes at once:

- `move every statistics step two weeks later except the exam ones`
- `book 45 min of DSA every weekday at 7am until 20 dec, not on fridays`
- `I finished all the easy array problems`
- `add a step after the SQL course to learn dbt, with three actions`
- `what is due in the next two weeks?`

**Setting it up.** Click **AI** (or **AI assistant settings** at the bottom of the page, or type `ai settings`). Pick a provider, enter the model name and paste your API key, then Save.

| Provider | Model name | Notes |
|---|---|---|
| Anthropic (Claude) | `claude-opus-5-5` (filled in) | Uses Anthropic's official SDK, loaded from cdn.jsdelivr.net the first time |
| OpenAI, Google Gemini, Groq, Mistral, DeepSeek | the model id from that provider's docs | Address is filled in |
| OpenRouter | e.g. `anthropic/...`, `openai/...` | One key for many models; works from web pages |
| Ollama | a local model that supports tool calling | No key. Start Ollama with `OLLAMA_ORIGINS=*` set |
| Other OpenAI-compatible API | as its docs say | Enter the address ending in `/v1` (the part before `/chat/completions`) |

The model needs to support tool (function) calling. Some providers refuse requests that come from a web page; the error message says so, and OpenRouter is a way around it.

**How it behaves**

- With **AI** on, everything you type goes to the model, except `undo`, `help`, `today` and `calendar`. With it off, you can still send one instruction by starting it with `ai:`, and when the box does not understand something it offers an **Ask the AI** button.
- The model reads your steps and calendar, then changes them directly. The result box lists every change. **Undo** reverses the whole instruction in one go (or type `undo`).
- Follow-ups remember the conversation (`now do the same for math`). Type `new chat` to start fresh. The conversation is forgotten when you reload.
- **Stop** in the working box cancels a request. Changes made before you stopped stay, and Undo still works.
- Changes to steps work like the Edit form: saved in this browser until you click Download updated roadmap (section 5).

**Privacy and cost.** Keys are stored only in this browser (localStorage), one per provider. They are not written into `roadmap.html`, Download updated roadmap or Export progress. Each instruction sends your words, today's date and a short overview of your steps and calendar blocks (titles, dates, status) to the provider. Your provider bills each instruction from your API credit. The overview makes each request several thousand tokens, and an instruction that changes many things takes several requests. **Forget this key** in settings removes a key. If the page is on GitHub Pages, the key is kept separately for that address, as with your progress.

## 4. Editing with the form

- **Edit** (top of any step): change title, date, track, main or side step, verify tag, text, actions (one per line), links (`Label | https://...`, one per line), needs-first ids and checklist items (one per line). Steps with more than 30 checklist items hide the checklist box so the problem lists cannot be wiped by accident.
- **+ Add step** (top of each track) adds a new step. **Add side step here** (inside Edit) adds one beside the current step.
- **Delete step** is inside Edit. Steps that needed it stop waiting for it.

Main steps are kept in date order automatically when you change a date.

## 5. Make your edits permanent

**If sync is on (section 8a), you can skip this section:** your edits are already saved to GitHub and appear on every connected device. Downloading is then only needed if you want the edits inside the file itself (for example to send it to someone).

Without sync, edits from the instruction box and the form are saved in this browser first. A banner at the top reminds you.

1. Click **Download updated roadmap**. You get a new `roadmap.html` with your edits written into the file.
2. Replace your old file with it (or `index.html` on GitHub, see section 9).
3. Open the new file once. The banner disappears because the file now matches.

If you open a newer file while old browser edits exist, the banner asks which to use: **Keep my edits** or **Use the file version**. Ticks and statuses are never lost either way.

You can also send `roadmap.html` to Claude with an instruction like "add a step for the Kaggle Learn SQL course after the MySQL step" and replace your file with what comes back.

## 6. Where the content lives (for manual editing)

Open `roadmap.html` in a text editor and find `const ROADMAP = /*ROADMAP_START*/` ... `/*ROADMAP_END*/`. Do not change the code below it.

- `meta`: title, goal, `goalDate`, `calendarNote` and `phases` (name, `from`, `to`, note) used by the Overview tab.
- `tracks`: each has `id`, `name`, `color`, `blurb` and `nodes`.

A node:

```json
{
  "id": "py2",
  "title": "Pandas and a data-cleaning notebook",
  "date": "2026-12-12",
  "verify": true,
  "dependsOn": ["py1"],
  "type": "branch",
  "attachTo": "py2",
  "what": "One or two sentences on what the step is.",
  "why": "Why it matters.",
  "actions": ["First concrete action", "Second concrete action"],
  "resources": [{"label": "Link text", "url": "https://example.com"}],
  "checklist": [{"id": "c1", "label": "Two Sum", "group": "EASY", "url": "https://...", "video": "https://...", "article": "https://...", "done": true}]
}
```

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Unique across the file. Progress is saved against it, so do not rename it after you start. |
| `title`, `date` | yes | Date as `YYYY-MM-DD`. |
| `verify` | no | Shows the yellow "verify" tag. |
| `dependsOn` | no | Ids from any track. Unfinished ones show "needs N". Nothing is locked. |
| `type`, `attachTo` | no | `"branch"` makes a side step beside the main step `attachTo`. |
| `what`, `why`, `actions` | yes | Shown in the step panel. |
| `resources` | no | Links. An entry with only a `label` shows as text. |
| `checklist` | no | Items to tick. Item `id` must be unique inside the step. `group` shows a sub-heading. `done: true` means ticked from the start. |

A missing comma, an extra comma after the last item, or a double quote inside text breaks the page. Use single quotes inside text. If the page goes blank, undo your last edit. The form and instruction box avoid these mistakes for you.

## 7. Where your sources went

**DSA (Code and Debug sheet).** One main step per sheet section, in the sheet's order, with two changes the sheet itself asks for: Strings come last, and Heaps come after Binary trees. Your existing steps stay: Big-O cheat sheet, system design docs and mock interviews. Pace is about one item a day, with a pause from 18 Jan to 14 Feb for assignments and exams. Main sheet done by 17 Oct 2027. Advanced sets run Nov 2027 to May 2028.

**Khan Academy statistics.** Part 1 (units 1-6, due 13 Dec), Part 2 (units 7-10, due 28 Mar), Part 3 (units 11-16 plus running the tests in Python, due 23 May). Khan says unit 5 is next for you.

**OSSU Data Science (ds.ossu.dev).** You are not doing OSSU in full, so its courses are used where they fit:

| OSSU area | Where it is |
|---|---|
| Prerequisites: high school math and Khan statistics | `math2` resources, the three Khan statistics steps |
| Intro to Data Science, Intro to CS | `car2` resource; side steps `py-b6` (DS Methodology, Tools for DS) and `py-b7` (MIT 6.0002) |
| Data Structures and Algorithms | Replaced by your Python DSA sheet (OSSU's courses use Java) |
| Databases | `deg3` (Database Management Essentials), `car-b2` (Data Warehouse), `bk-b2` (MongoDB) |
| Calculus, Linear Algebra, Multivariable | `math3`, `math4`, `math7` (MITx Calculus 1A), side steps `math-b2` (MIT 18.06), `math-b4` (Calculus 1B/1C), new step `math10` (MIT 18.02) |
| Statistics and Probability | `math8` (Udacity inferential stats link), side steps `math-b3` (Harvard Stat 110), `py-b8` (ISLP) |
| Machine Learning | Andrew Ng's three courses in `py5`, `py10`, `py-b2`; new step `py11` (Mining Massive Datasets) |
| Final project | `car6` |

Coursera's free audit option is not available for every course. If a course asks you to pay, look for the same course on its free page or use the free textbook link where one is given.

## 8. Progress and backups

- Statuses, ticks, notes and browser edits are saved in this browser, per device.
- **Export progress** downloads a backup (it includes your edited steps if you have any). **Import progress** restores it on another browser or device.
- Skipped steps are left out of the percentage.
- **Reset progress** clears statuses, ticks and notes, not your step edits or your calendar.
- **Import progress** checks the file first. A damaged or wrong file is refused with a message and nothing changes.

## 8a. Sync across devices (GitHub gist)

With sync on, everything you change (statuses, ticks, notes, calendar sessions and step edits) is saved to a file in a secret gist on your GitHub account a few seconds after you stop editing. Every device you connect loads it, so your laptop and phone show the same roadmap and you never need to download.

**Setting it up (once per device)**

1. Click **Sync across devices (GitHub)** at the bottom of the page.
2. Click **Create a GitHub token**. On GitHub, keep the "gist" box ticked (nothing else), choose an expiry and click Generate. Copy the token (it starts with `ghp_`).
3. Paste it into the box and click **Connect**. The first device creates the gist. Other devices find the same gist automatically: on each one, paste a token from the same GitHub account (the same token is fine).

A cloud button appears next to the help button. Its dot is green when everything is saved, orange while saving, and red when something needs attention. Hover over it or tap it to see the status, sync now, or disconnect.

**How it behaves**

- The page checks GitHub when it opens, when you come back to the tab, and every two minutes.
- If you changed things on two devices before either could save (for example offline on both), a banner asks which copy to keep: **Use the other device's copy** or **Keep this device's copy**. Nothing is overwritten without asking. Loading the other copy can be reversed with `undo`.
- Offline changes wait and save when you are back online.
- When you connect a device that already has progress and a gist already exists, you get the same choice, so neither side is lost.
- **Disconnect** stops syncing in that browser. Your data stays both in the browser and in the gist.

**Privacy.** The token is stored only in that browser, never in `roadmap.html`, backups or the gist. GitHub has no fully private gists: a "secret" gist is not listed or searchable, but anyone who has its link can read it. Keep passwords and other secrets out of your notes. If a token leaks, delete it on GitHub (Settings, Developer settings, Personal access tokens) and connect again with a new one.

## 9. Put it on GitHub Pages

1. Create a repository, for example `my-roadmap`.
2. Upload the whole folder as it is: `roadmap.html`, `index.html`, `.nojekyll`, `README.md`, `ROADMAP_GUIDE.md` (the `dev/` folder is optional). No renaming is needed: `index.html` forwards to `roadmap.html`.
3. Settings, then Pages: source = deploy from a branch, `main`, root folder. Save.
4. After a minute it is live at `https://<your-username>.github.io/my-roadmap/`.
5. Turn on sync (section 8a) in the browser you use there. Your changes then save to GitHub and you do not need to upload anything again. Without sync: click Download updated roadmap and upload the new `roadmap.html`.

Browser storage is separate for each web address. With sync on, connecting at the new address brings everything across. Without sync, export your progress before moving to a new address, then import it there.

## 10. Ten-minute weekly review (same day every week)

1. **0-2 min: update.** Open This week. Tick what you finished and set statuses. Glance at Progress: is the pace for each track ahead or behind?
   Then open Calendar and book time for anything in "Due soon with no time booked".
2. **2-5 min: overdue.** For each overdue step, do it this week, move it (`push pandas by 1 week`), or skip it. Do not leave anything overdue without a decision.
3. **5-7 min: calendar.** Check college deadlines for the next two weeks. If an exam or submission week is coming, push study steps (`push everything by 1 week`).
4. **7-9 min: focus.** Pick at most one step per track from "Coming up next", no more than 4 in total, and write one line in its notes on what finished looks like.
5. **10 min: save.** With sync on, check the cloud button's dot is green. Without sync, click Download updated roadmap if you changed any steps. Export progress once a month either way.
