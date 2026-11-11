# REA — how it works (Relapsa lab)

[REA](https://github.com/morluto/rea) (*Reverse Engineer Anything*) lets an AI agent (or you in a terminal) **inspect software without source**. For Relapsa we use it on Android APKs to learn features and structure for our own diagrams — not to copy code into the product.

## Mental model

```text
You / Cursor agent
       │  asks a question ("what package is this?", "find login classes")
       ▼
REA MCP / CLI  (rea-agents)
       │  calls a tool, e.g. inspect_android_package
       ▼
JADX headless JAR  +  JDK 17+
       │  static read of the APK (never runs the app)
       ▼
Evidence JSON  (findings + limits + file hashes)
       │
       ▼
docs/research/*.md   →   docs/01–05 Mermaid deliverables (+ docs/images/)
```

1. **Ask** — one focused question (package map, auth, meals…).
2. **Inspect** — REA drives JADX; result is **evidence** (what was seen + what is unknown).
3. **Synthesize** — short bullets in `docs/research/` (no decompiled dumps in git).
4. **Design** — update Relapsa Mermaid in `docs/02`–`05` (not a parallel `docs/architecture/` tree).

## What we installed on this machine

| Piece | Where / version |
|-------|------------------|
| Node | v26.13.0 (REA needs recent 22/24/26) |
| JDK | `JAVA_HOME` = `C:\Program Files\Java\jdk-17` |
| JADX bridge | `%USERPROFILE%\.local\share\rea\android\jadx-headless-mcp-0.7.1-all.jar` |
| Env | User `REA_JADX_MCP_JAR` → that JAR |
| Cursor MCP | `rea setup --client cursor` wrote `~\.cursor\mcp.json` |
| Skill | `~\.agents\skills\reverse-engineer-anything` |

**After setup:** restart Cursor so the REA MCP server loads.

## Commands you will use

```powershell
$env:REA_JADX_MCP_JAR = "$env:USERPROFILE\.local\share\rea\android\jadx-headless-mcp-0.7.1-all.jar"
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"

# Overview of an APK
npx rea-agents@latest inspect-android-package "D:\Development\SoftwareLab\rea\source\TFIT_base.apk"

# Find classes by name fragment
npx rea-agents@latest search-android-classes "…\TFIT_base.apk" Login

# Optional: doctor
npx rea-agents@latest doctor --provider jadx
```

Same tools over MCP (underscores): `inspect_android_package`, `search_android_classes`, …

## Smoke test (done)

| Date | Target | Result |
|------|--------|--------|
| 2026-11-02 | TFIT_base.apk | OK — package `app.tfit.web.twa`, TWA wrapper, 4491 classes loaded |

See [../research/tfit.md](../research/tfit.md).

## Lab rules

- APKs stay in `rea/source/` locally (gitignored).
- Commit only research notes + architecture Mermaid.
- Ghidra/IDA are optional; **JADX is enough** for our APK phase.

## Next for TFIT

APK analysis is done (TWA). Analyze the web app: [analyze-web-tfit.md](analyze-web-tfit.md).
