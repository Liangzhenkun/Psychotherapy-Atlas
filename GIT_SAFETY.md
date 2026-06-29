# Git Safety Guide

## What is automated here

This repository now includes three layers of protection:

1. Local `pre-commit` hook
   Checks staged files before each commit.
2. Local `pre-push` hook
   Scans tracked repository files before each push.
3. GitHub Actions workflow
   Runs the same scan again on GitHub for pushes and pull requests.

## What the guard checks

- Common secret filenames such as `.env`, `id_rsa`, `.pem`, `.p12`, `.pfx`, `.jks`, and `.key`
- Strong secret patterns such as GitHub tokens, OpenAI-style keys, AWS access keys, Slack tokens, and private key blocks
- Local absolute filesystem paths
- Large files that should probably live outside normal Git history
- The effective `git user.email` for this repository

## How to install the hooks in this repository

```powershell
pwsh -NoProfile -File .\scripts\install_git_hooks.ps1
```

If you do not have `pwsh`, use:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_git_hooks.ps1
```

## How to run the scan manually

Check only staged files:

```powershell
pwsh -NoProfile -File .\scripts\repo_guard.ps1 -Mode staged
```

Check the tracked repository:

```powershell
pwsh -NoProfile -File .\scripts\repo_guard.ps1 -Mode repo
```

## How to handle intentional exceptions

If a file is intentionally public and the guard blocks it, add a narrow path to `.repo-guard-ignore`.

Do not ignore:

- `.env`
- private keys
- API tokens
- machine-specific paths

## Recommended public-repo defaults

- Use your GitHub-provided `noreply` email as the global default commit email.
- Enable `Keep my email addresses private`.
- Enable `Block command line pushes that expose my email`.
- Keep large assets in Git LFS, Releases, or external object storage instead of normal Git history.
