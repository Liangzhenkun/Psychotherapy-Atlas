# Psychotherapy Atlas

A bilingual research-and-creation project on psychotherapy approaches, techniques, indications, and narrative translation.

## What this repository includes

- `index.html`
  A bilingual static site with a Chinese / English switch.
- `psychotherapy_research_pack.md`
  The Chinese long-form research pack.
- `psychotherapy_research_pack_en.md`
  The English long-form research pack.
- `reference_archive/`
  An auditable literature archive with bilingual tables, summaries, open-access links, selected PDFs, citation counts, and journal-ranking fields.

## Main entry points

- Site: [index.html](index.html)
- Chinese pack: [psychotherapy_research_pack.md](psychotherapy_research_pack.md)
- English pack: [psychotherapy_research_pack_en.md](psychotherapy_research_pack_en.md)
- Bilingual archive table: [reference_archive/reference_table_bilingual.md](reference_archive/reference_table_bilingual.md)
- Bilingual archive CSV: [reference_archive/reference_index_bilingual.csv](reference_archive/reference_index_bilingual.csv)
- Git safety guide: [GIT_SAFETY.md](GIT_SAFETY.md)

## Privacy and publishing notes

- Local absolute filesystem paths were removed or converted to repository-relative paths before publication.
- Ignore rules are included for local editor files, virtual environments, caches, and other machine-specific artifacts.
- This repository is intended to be safe for public GitHub publication.

## Safety automation

- Local hooks are stored in `.githooks/` and can be installed with:
  - `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_git_hooks.ps1`
- Manual scan:
  - `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\repo_guard.ps1 -Mode staged`
  - `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\repo_guard.ps1 -Mode repo`
- A GitHub Actions workflow runs the same repository scan on push and pull request.

## Project title

**Psychotherapy Atlas**  
Subtitle: **Approaches, Techniques, Indications, and Narrative Translation**
