# Relapsa — Docs Index

Health, nutrition, and fitness management system (سیستم مدیریت سلامت و تغذیه و تناسب اندام).

**Product:** Relapsa — track the protocol, survive the slip, return.  
**Stack (planned):** Django + DRF · Expo · PostgreSQL  
**Comparables:** تی‌فیت (primary RE) · Samsung Health (selective)  
**Repo goal:** private mono-repo `relapsa` (not created until you approve)

## Start here

| Need | File |
|------|------|
| Brand / name | [brand.md](brand.md) |
| This week’s lab session | [sessions/](sessions/) |
| Canonical requirements | [requirements/](requirements/) |
| Competitive research | [research/](research/) |
| Diagrams & system design | [architecture/](architecture/) |
| How to run tools | [howto/](howto/) |

## Sessions

1. [Topic & comparables](sessions/01-topic.md)
2. [Requirements exercise](sessions/02-requirements.md)
3. [Activity + Class diagrams](sessions/03-diagrams.md) ← current

## Architecture (canonical)

- [Use cases](architecture/use-cases.md)
- [Activity — auth & onboarding](architecture/activity-auth.md)
- [Activity — meal](architecture/activity-meal.md)
- [Activity — fitness](architecture/activity-fitness.md)
- [Activity — progress](architecture/activity-progress.md)
- [Class — domain](architecture/class-domain.md)
- [System](architecture/system.md)
- [API sketch](architecture/api-sketch.md)

## Research

- [Comparison matrix](research/comparison.md)
- [TFIT findings](research/tfit.md)
- [Samsung Health findings](research/samsung-health.md)

## How-to

- [REA setup & smoke test](howto/rea-setup.md)
- [Stack notes](howto/stack.md)

## Rules

- Session notes = what you showed that week. Canonical truth = `requirements/` + `architecture/`.
- Research = short bullets with evidence. No decompiled source dumps in git.
- APKs stay under `rea/source/` locally and are gitignored.
