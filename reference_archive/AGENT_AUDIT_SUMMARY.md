# Agent Audit Summary

This file records the classification logic used by the literature-archiving agent.

## Core Evidence

These sources are suitable for supporting main claims about therapy techniques and indications:

- umbrella reviews
- systematic reviews
- meta-analyses
- network meta-analyses
- NICE and APA guidelines

In this archive, that means:

- `01_core_evidence`
- `02_guidelines`

## Supporting But Not Core

These sources are useful, but should not be ranked beside top-tier evidence:

- `03_supporting_overviews`
- `04_theory_and_perspective`
- `05_official_explainers`

## Display Rule

Only items with `can_be_used_as_core_evidence = yes` should be used as the main evidence chain in your report or portfolio narrative.

## Why This Matters

This separation lets you show both:

1. that you are using high-quality evidence for claims about effectiveness and indications
2. that you still keep theory, orientation notes, and institutional explainers available without overstating their status
