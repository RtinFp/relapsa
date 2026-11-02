# REA (local analysis)

Used to inspect TFIT / Samsung Health APKs for lab requirements.  
APKs stay under `rea/source/` locally and are gitignored.

## Needs

- Node 22+ or 24+
- JDK 17+
- `jadx-headless-mcp` 0.7.1 JAR → set `REA_JADX_MCP_JAR`
- [rea-agents](https://github.com/morluto/rea): `npx rea-agents@latest setup`

## Smoke test

```powershell
npx rea-agents@latest inspect-android-package "D:\Development\SoftwareLab\rea\source\TFIT_base.apk"
```

Write findings into `docs/research/` (short notes only, no decompiled source).
