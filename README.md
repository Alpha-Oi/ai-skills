# AI Skills

A public collection of reusable skills for AI coding and general-purpose agents.

Each skill is stored in its own directory and has a `SKILL.md` entry point with YAML frontmatter. The collection is designed to remain simple to browse, install, review, and extend.

## Repository structure

```text
ai-skills/
├── README.md
└── skills/
    ├── metacognition/
    │   └── SKILL.md
    └── metacognitive-supervisor/
        └── SKILL.md
```

Add future skills under `skills/<skill-name>/`. Use a lowercase, hyphen-separated directory name and keep the main instructions in `SKILL.md`. Add `scripts/`, `references/`, or `assets/` inside a skill only when that skill actually needs them.

## Included skills

### Metacognition v1.0

A focused quality-control loop for an AI agent. It checks the goal, assumptions, uncertainty, evidence, contradictions, strategy, progress, and verification without exposing private chain-of-thought.

Path: [`skills/metacognition/SKILL.md`](skills/metacognition/SKILL.md)

### Metacognitive Supervisor

An extended supervisory layer for agents and skills. It adds meta-memory, skill-quality and freshness checks, model compatibility, cross-agent critique, repeated-failure control, information-gain gating, decision journals, metacognitive debt, escalation, and self-audit.

Path: [`skills/metacognitive-supervisor/SKILL.md`](skills/metacognitive-supervisor/SKILL.md)

## Using a skill

Copy the selected skill directory into the skills location supported by your agent environment, or reference its `SKILL.md` from your own skill loader. Exact installation and discovery behavior depends on the host product.

Review every skill before use. A skill provides instructions and decision support; it does not grant permission to modify files, call external services, use credentials, or perform destructive actions.
