<div align="center">

# ◈ AI Skills

### Reusable control systems for AI agents

**Metacognition · Biology-inspired architecture · 10D engineering**

[![Validate skills](https://github.com/Alpha-Oi/ai-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/Alpha-Oi/ai-skills/actions/workflows/validate-skills.yml)
[![Skills](https://img.shields.io/badge/skills-8-6f5cff)](#skill-catalog)
[![License: MIT](https://img.shields.io/badge/license-MIT-22a06b.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/Alpha-Oi/ai-skills?color=1f6feb)](https://github.com/Alpha-Oi/ai-skills/commits/main)

[English](README.md) · [Русский](README.ru.md) · [Contributing](CONTRIBUTING.md) · [Conduct](CODE_OF_CONDUCT.md) · [Security](SECURITY.md)

</div>

---

AI Skills is a curated collection of portable instruction packages for AI coding
agents and general-purpose assistants. Each skill turns a difficult decision pattern
into a focused, reviewable workflow with explicit boundaries and verification.

The collection explores three related ideas:

- **Metacognitive control** — check goals, evidence, uncertainty, and completion.
- **Biology-inspired architecture** — translate biological mechanisms into testable
  engineering patterns while preserving the limits of the analogy.
- **Ten-dimensional engineering** — evaluate decisions through interacting quality
  dimensions instead of optimizing one property in isolation.

## Quick start

Choose a skill from the [catalog](#skill-catalog), review its `SKILL.md`, and copy
the complete skill directory into the skills location supported by your agent.

```text
skills/<skill-name>/
├── SKILL.md
└── references/       # present only when the skill needs supporting material
```

Then ask the agent to use the skill by name, or let the host discover it from the
frontmatter description when automatic selection is supported.

> [!IMPORTANT]
> A skill provides instructions and decision support. It does not grant permission
> to modify files, access credentials, call external services, publish changes, or
> perform destructive actions.

## Skill catalog

### Metacognitive control

| Skill | Use it for |
| --- | --- |
| [Metacognition](skills/metacognition/SKILL.md) | Checking task understanding, assumptions, evidence, contradictions, progress, and verification. |
| [Metacognitive Supervisor](skills/metacognitive-supervisor/SKILL.md) | Supervising long-running or multi-component work with freshness checks, failure memory, decision records, escalation, and self-audit. |

### Biology-inspired architecture

| Skill | Engineering pattern | Biological inspiration |
| --- | --- | --- |
| [Aquaporin Flow](skills/aquaporin-flow/SKILL.md) | Selective data boundaries and verified artifact delivery | Aquaporins and intracellular transport |
| [Complementary Integrity](skills/complementary-integrity/SKILL.md) | Redundancy, source authority, and bounded recovery | DNA complementarity and repair |
| [Contextual Structures](skills/contextual-structures/SKILL.md) | Relationship-dependent meaning and coherent updates | Glycan diversity and the glycocalyx |
| [Asymmetric State Flow](skills/asymmetric-state-flow/SKILL.md) | Direction-specific transitions and controlled redistribution | Lipid movement across membrane leaflets |

Each biological skill includes `references/biology.md` with sources and limits.
Biological inspiration is a design lens, not evidence of software correctness,
security, performance, or intentional design in nature.

### Ten-dimensional engineering

| Skill | Use it for |
| --- | --- |
| [Ten-Dimensional Review](skills/ten-dimensional-review/SKILL.md) | Broad system decisions across purpose, context, information, structure, behavior, time, resources, failure, trust, and evolution. |
| [10D Quality Vector](skills/10d-quality-vector/SKILL.md) | Code changes and reviews across correctness, reliability, maintainability, testability, security, performance, compatibility, observability, simplicity, and architectural fit. |

The two 10D skills are complementary: the first explores a system decision space;
the second applies a concrete quality contract to engineering work.

## Design principles

- **Clear routing:** every description says what the skill does and when to use it.
- **Progressive disclosure:** essential instructions stay in `SKILL.md`; conditional
  detail belongs in `references/`, `scripts/`, or `assets/` only when needed.
- **Evidence over confidence:** proposed checks and observed results remain distinct.
- **Bounded authority:** a workflow never expands the user's permission by itself.
- **Useful restraint:** the smallest adequate skill and intervention should win.
- **Portable structure:** every skill remains self-contained and easy to review.

## Repository structure

```text
ai-skills/
├── .github/                  # contribution templates and validation workflow
├── scripts/
│   └── validate_skills.py
├── skills/
│   ├── metacognition/
│   ├── metacognitive-supervisor/
│   ├── aquaporin-flow/
│   ├── complementary-integrity/
│   ├── contextual-structures/
│   ├── asymmetric-state-flow/
│   ├── ten-dimensional-review/
│   └── 10d-quality-vector/
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── README.md
└── README.ru.md
```

## Add a skill

Create `skills/<skill-name>/SKILL.md` with lowercase hyphenated naming and concise
YAML frontmatter:

```yaml
---
name: my-skill
description: Explain what the skill does and when an agent should use it.
---
```

Keep the entry point focused, add resources only when they change decisions, and run:

```bash
python scripts/validate_skills.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the acceptance criteria and pull request
process.

## Project status

This is an evolving collection of initial skill versions. Structural validation
checks packaging and local references; it does not establish behavioral effectiveness
across models, prompts, repositories, or host products. Realistic forward evaluations
are welcome.

## License

Code and original documentation in this repository are available under the
[MIT License](LICENSE). External sources linked from biological references retain
their respective rights.
