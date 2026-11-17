"""Smoke test for roadmap.html, run in a real browser with no real API keys.

    python dev/run_smoke.py            # needs Python 3.8+ and Chrome or Edge

It serves the project folder on 127.0.0.1, opens dev/smoke.html in headless
Chrome/Edge, and prints one line per check. Requests the page would send to
Anthropic, an OpenAI-compatible API or GitHub's Gist API go to small mocks in
this file instead, so nothing leaves the computer and nothing is billed.
Set CHROME=<path to chrome.exe or msedge.exe> if the browser is not found.
Exit code 0 means every check passed.
"""
import json, os, shutil, subprocess, sys, tempfile, threading, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(os.environ.get("SMOKE_PORT", "8765"))
TYPES = {".html": "text/html; charset=utf-8", ".js": "text/javascript", ".json": "application/json", ".md": "text/plain; charset=utf-8"}
REPORT = {}
GISTS = {}          # id -> {"files": {name: {"content": str}}, "updated_at": str}
CALLS = []          # (method, path) of mock API calls, for the report


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "%06d" % (time.time_ns() // 1000 % 1000000)


# ---------- scripted model replies ----------
def openai_reply(body):
    first = next((str(m.get("content") or "") for m in body["messages"] if m["role"] == "user"), "")
    if "make a new track" in first:
        if not [m for m in body["messages"] if m["role"] == "tool"]:
            calls = [
                ("c1", "add_track", {"name": "Languages", "color": "#22c55e", "blurb": "German practice",
                                     "steps": [
                                         {"title": "Duolingo warm-up", "date": "2026-12-01", "checklist": ["10 XP"]},
                                         {"title": "Anki deck", "side_step_of": "Duolingo warm-up"}]}),
                ("c2", "update_track", {"track": "languages", "name": "Languages & tools"}),
                ("c3", "update_roadmap", {"goal": "Test goal", "goal_date": "2027-01-15",
                                          "phases": [{"name": "P1", "from": "2026-11-01", "to": "2027-02-14"}]}),
            ]
            msg = {"role": "assistant", "content": None, "tool_calls": [
                {"id": i, "type": "function", "function": {"name": n, "arguments": json.dumps(a)}} for i, n, a in calls]}
            return {"model": body["model"], "choices": [{"finish_reason": "tool_calls", "message": msg}]}
        return {"model": body["model"], "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "Done: made the Languages track and set the goal."}}]}
    tool_msgs = [m for m in body["messages"] if m["role"] == "tool"]
    if not tool_msgs:
        calls = [
            ("c1", "search", {"query": "pandas"}),
            ("c2", "shift_dates", {"track": "math", "weeks": 1}),
            ("c3", "add_block", {"step_id": "dsa1", "date": "2026-11-16", "start": "19:00", "minutes": 60, "repeat": "daily", "until": "2026-12-20"}),
            ("c4", "update_step", {"id": "py2", "date": "2026-12-20", "side_step_of": "nonexistent"}),
        ]
        msg = {"role": "assistant", "content": None, "tool_calls": [
            {"id": i, "type": "function", "function": {"name": n, "arguments": json.dumps(a)}} for i, n, a in calls]}
        return {"model": body["model"], "choices": [{"finish_reason": "tool_calls", "message": msg}]}
    return {"model": body["model"], "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "Done: moved math a week later and booked DSA."}}]}


def anthropic_reply(body):
    if len(body["messages"]) == 1:
        return {"id": "m1", "type": "message", "role": "assistant", "model": body["model"], "stop_reason": "tool_use",
                "usage": {"input_tokens": 1, "output_tokens": 1},
                "content": [{"type": "tool_use", "id": "t1", "name": "set_status", "input": {"ids": ["car1"], "status": "done"}}]}
    return {"id": "m2", "type": "message", "role": "assistant", "model": body["model"], "stop_reason": "end_turn",
            "usage": {"input_tokens": 1, "output_tokens": 1}, "content": [{"type": "text", "text": "Marked it done."}]}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,PATCH,OPTIONS")

    def send_json(self, code, obj):
        data = json.dumps(obj).encode()
        self.send_response(code); self.cors()
        self.send_header("Content-Type", "application/json"); self.send_header("Cache-Control", "no-store")
        self.end_headers(); self.wfile.write(data)

    def body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def do_OPTIONS(self):
        self.send_response(204); self.cors(); self.end_headers()

    # ---------- static files and GitHub mock (GET) ----------
    def do_GET(self):
        path = self.path.split("?")[0]
        if path.startswith("/gh/"):
            return self.github("GET", path[3:], None)
        rel = os.path.normpath(path.lstrip("/") or "index.html")
        full = os.path.join(ROOT, rel)
        if rel.startswith("..") or not os.path.isfile(full):
            self.send_response(404); self.end_headers(); return
        data = open(full, "rb").read()
        self.send_response(200)
        self.send_header("Content-Type", TYPES.get(os.path.splitext(full)[1], "application/octet-stream"))
        self.send_header("Cache-Control", "no-store")
        self.end_headers(); self.wfile.write(data)

    def do_PATCH(self):
        if self.path.startswith("/gh/"):
            return self.github("PATCH", self.path[3:], self.body())
        self.send_response(404); self.end_headers()

    def do_POST(self):
        path = self.path.split("?")[0]
        if path == "/report":
            REPORT.update(self.body()); self.send_json(200, {}); return
        if path.startswith("/gh/"):
            return self.github("POST", path[3:], self.body())
        if path.startswith("/__test/gist/"):          # lets the test play "another device"
            gid = path.rsplit("/", 1)[1]; b = self.body()
            GISTS[gid]["files"]["roadmap-sync.json"]["content"] = b["content"]; GISTS[gid]["updated_at"] = now_iso()
            self.send_json(200, {}); return
        if path.endswith("/chat/completions"):
            CALLS.append(("POST", "chat/completions")); self.send_json(200, openai_reply(self.body())); return
        if path.endswith("/v1/messages"):
            CALLS.append(("POST", "v1/messages")); self.send_json(200, anthropic_reply(self.body())); return
        self.send_response(404); self.end_headers()

    def github(self, method, path, body):
        CALLS.append((method, path))
        if self.headers.get("Authorization") != "Bearer test-token":
            return self.send_json(401, {"message": "Bad credentials"})
        def out(gid):
            g = GISTS[gid]
            return {"id": gid, "updated_at": g["updated_at"], "public": False,
                    "files": {k: {"filename": k, "content": v["content"], "truncated": False} for k, v in g["files"].items()}}
        if path == "/gists" and method == "GET":
            return self.send_json(200, [out(g) for g in GISTS])
        if path == "/gists" and method == "POST":
            gid = "g%d" % (len(GISTS) + 1)
            GISTS[gid] = {"files": {k: {"content": v["content"]} for k, v in body["files"].items()}, "updated_at": now_iso()}
            return self.send_json(201, out(gid))
        gid = path.split("/")[-1]
        if gid not in GISTS:
            return self.send_json(404, {"message": "Not Found"})
        if method == "PATCH":
            for k, v in body["files"].items():
                GISTS[gid]["files"][k] = {"content": v["content"]}
            GISTS[gid]["updated_at"] = now_iso()
        return self.send_json(200, out(gid))


def find_browser():
    cands = [os.environ.get("CHROME", "")]
    for base in (os.environ.get("PROGRAMFILES", ""), os.environ.get("PROGRAMFILES(X86)", ""), os.environ.get("LOCALAPPDATA", "")):
        cands += [os.path.join(base, "Google", "Chrome", "Application", "chrome.exe"),
                  os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe")]
    cands += [shutil.which(n) or "" for n in ("google-chrome", "chromium", "chromium-browser", "chrome", "msedge")]
    cands += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    return next((c for c in cands if c and os.path.isfile(c)), None)


def main():
    browser = find_browser()
    if not browser:
        print("Chrome or Edge not found. Set CHROME=<path>."); return 2
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    profile = tempfile.mkdtemp(prefix="roadmap-smoke-")
    proc = subprocess.Popen([browser, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
                             "--user-data-dir=" + profile, "http://127.0.0.1:%d/dev/smoke.html" % PORT],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    deadline = time.time() + float(os.environ.get("SMOKE_TIMEOUT", "120"))
    while not REPORT and time.time() < deadline:
        time.sleep(0.3)
    proc.terminate()
    try:
        proc.wait(10)
    except subprocess.TimeoutExpired:
        proc.kill()
    server.shutdown()
    shutil.rmtree(profile, ignore_errors=True)
    if not REPORT:
        print("No report from the browser (timed out)."); return 1
    failed = 0
    for r in REPORT.get("results", []):
        ok = r["ok"]; failed += 0 if ok else 1
        print(("PASS " if ok else "FAIL ") + r["name"] + ("" if ok else "  ->  " + r.get("info", "")))
    for e in REPORT.get("pageErrors", []):
        failed += 1; print("FAIL page error: " + e)
    print("\n%d checks, %d failed" % (len(REPORT.get("results", [])), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
