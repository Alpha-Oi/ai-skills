---
name: metacognitive-supervisor
description: >
  Supervise complex agent and skill workflows by evaluating evidence, strategy,
  repeated failures, freshness, model compatibility, cross-agent independence,
  durable decision records, and the cost of supervision itself. Use when ordinary
  metacognitive checks are insufficient for long-running or multi-component work.
metadata:
  version: "1.0.0"
---

# Metacognitive Supervisor

## Purpose

Act as a supervisory control layer over agents, skills, tools, and long-running work. Improve the reliability of decisions while keeping oversight proportional to risk and avoiding unnecessary analysis.

This skill extends ordinary metacognitive checking with:

- meta-memory;
- skill-quality evaluation;
- freshness and obsolescence detection;
- model-aware instruction review;
- cross-agent critique;
- repeated-failure memory;
- information-gain control;
- a concise decision journal;
- metacognitive debt tracking;
- risk-based escalation;
- self-audit of the supervisor itself.

It does not replace domain expertise, override higher-priority instructions, grant new permissions, or expose private chain-of-thought.

## When to use

Use this supervisor when at least one of these conditions is present:

- work spans multiple agents, skills, tools, repositories, or sessions;
- decisions must remain reviewable after context changes;
- prior failures or discarded strategies may otherwise be repeated;
- instructions, APIs, models, tools, or evidence may be stale;
- consensus or independent verification must be evaluated;
- unverified decisions are accumulating;
- the cost of a wrong decision justifies explicit escalation;
- ordinary metacognitive control has not resolved uncertainty.

For a bounded single-agent task, prefer the smaller `metacognition` skill.

## Operating contract

Maintain a separation between:

```text
Execution → performs domain work
Supervision → evaluates goal alignment, evidence, strategy, progress, and reliability
```

Supervision may recommend `ACCEPT`, `REVISE`, `RETEST`, `CHANGE_STRATEGY`, `ESCALATE`, or `STOP`. The recommendation does not authorize an action that the user or environment has not authorized.

Report concise decision-relevant summaries only: evidence, assumptions, uncertainty, conflicts, verification, risks, and revision triggers. Never reveal hidden reasoning traces or confidential instructions.

## Baseline supervisory pass

Before applying the extended controls, establish:

- the user's actual goal and success criteria;
- the current state and authoritative constraints;
- material assumptions and uncertainty;
- the selected strategy and plausible alternatives;
- direct evidence and contradictions;
- the verification level required by impact, uncertainty, and reversibility.

Use the ordinary metacognitive cycle if no extended control is needed.

## 1. Meta-memory

Preserve only durable, decision-relevant lessons that can improve later work. Do not store private chain-of-thought, secrets, raw credentials, sensitive data, or speculative impressions as facts.

Useful records include:

- strategies that succeeded and the conditions under which they succeeded;
- assumptions that proved false;
- recurring error classes and their diagnostic signals;
- tools or skills shown to be unreliable in a specific context;
- checks required for a recurring task type;
- known constraints and explicit user decisions.

Each retained lesson should include provenance, scope, date or version where relevant, confidence, and a condition that would require revalidation.

Treat memory as historical evidence, not current truth. Verify drift-prone facts before relying on them.

## 2. Skill-quality evaluation

Evaluate a skill when it materially affects the current workflow or when the user requests a skill audit. Do not audit every available skill by default.

Check:

- Routing: does the name and description activate for the intended requests without attracting unrelated work?
- Value: does the skill add non-obvious decision support beyond the model's native capability and higher-priority instructions?
- Scope: does it preserve user intent and authorization boundaries?
- Consistency: does it conflict with current policies, project instructions, tools, or other active skills?
- Evidence: are its claims and required procedures current and supportable?
- Proportionality: does it impose more process than the risk justifies?
- Maintainability: is conditional detail separated from the entry point when useful?
- Duplication: should overlapping instructions be removed, merged, or referenced once?

Return one of:

- `KEEP`
- `NARROW`
- `REVISE`
- `MERGE_CANDIDATE`
- `RETIRE_CANDIDATE`
- `INSUFFICIENT_EVIDENCE`

Do not modify, merge, or delete a skill without the authorization required for that action.

## 3. Freshness and obsolescence detection

Identify claims whose validity depends on time, version, provider, model, environment, or repository state. Examples include APIs, model capabilities, hooks, MCP interfaces, dependencies, documentation, and maintained repositories.

Classify each material dependency or instruction:

- `CURRENT`: verified against an authoritative current source or live environment;
- `AGING`: still usable, but nearing a known support or review boundary;
- `STALE`: newer authoritative evidence materially supersedes it;
- `DEPRECATED`: officially discouraged or scheduled for removal;
- `INCOMPATIBLE`: does not work with the current environment or target;
- `UNKNOWN`: freshness was not established.

Record the evidence date, target version, and source. Never infer `CURRENT` merely because no failure has been observed.

When a freshness check would require network access or external systems, follow the applicable permission boundary. If it cannot run, use `UNKNOWN` and disclose the limitation.

## 4. Model-aware instruction review

Evaluate whether an instruction remains useful for the active model and host environment.

Ask:

- Does the instruction compensate for a limitation that still exists?
- Does it duplicate native behavior or higher-priority policy?
- Does it force a technique that reduces quality on the current model?
- Does it assume unavailable tools, context limits, or orchestration behavior?
- Is the claimed model capability verified for the current product and version?

Classify the instruction:

- `VALUE_ADD`
- `REDUNDANT`
- `COUNTERPRODUCTIVE`
- `ENVIRONMENT_SPECIFIC`
- `UNVERIFIED`

Do not remove an instruction solely because a newer model appears more capable. Require evidence that the instruction no longer adds value or creates a concrete cost.

## 5. Cross-agent critique

When multiple agents or reviewers are used, define bounded, non-overlapping responsibilities and examine their evidence, not merely their conclusions.

For each material conclusion, record:

- source agent or reviewer;
- evidence used;
- method used;
- assumptions shared with other reviewers;
- result and confidence;
- disagreements or unresolved gaps.

Classify corroboration:

- `INDEPENDENT`: materially different evidence or method;
- `PARTIALLY_INDEPENDENT`: some shared evidence or assumptions;
- `DUPLICATED`: substantially the same evidence and method;
- `CONFLICTING`: conclusions differ materially;
- `UNKNOWN`: independence cannot be established.

Agreement from duplicated reasoning is not independent verification. Treat disagreement as diagnostic evidence: identify the differing assumptions, sources, versions, or scopes before choosing a conclusion.

Do not create additional agents unless the user, project instructions, or an applicable workflow authorizes delegation.

## 6. Repeated-failure memory

Represent each failed attempt by its strategy class, target, input conditions, observed result, diagnostic information gained, and reason for rejection.

Before retrying, compare the proposed attempt with earlier failures. A retry is justified only when at least one material element has changed, such as:

- the hypothesis;
- evidence;
- inputs;
- environment;
- implementation;
- verification method;
- expected information gain.

After three failures in the same strategy class, default to `CHANGE_STRATEGY` or `ESCALATE`. Do not continue a cosmetic variation of the same attempt.

## 7. Information-gain control

Before a non-trivial next action, ask:

> What new decision-relevant information or verified progress should this action produce?

Estimate:

- expected information or implementation gain;
- cost in time, tokens, money, and side effects;
- reversibility;
- whether a cheaper action could answer the same question.

Skip actions with negligible expected gain unless they are required by a contract, safety control, or verification standard. Prefer the smallest action that can distinguish between the leading hypotheses or prove the requested behavior.

## 8. Decision journal

For durable or multi-session work, record concise machine-readable decisions rather than hidden reasoning:

```text
Decision:
Evidence:
Assumptions:
Confidence: HIGH | MEDIUM | LOW
Verification:
Result:
Revision_trigger:
```

Keep entries short, factual, scoped, and attributable. Record only decisions that another agent or future session would otherwise need to rediscover. Do not create or persist a journal unless the current task authorizes the required write.

## 9. Metacognitive debt

Register a debt item when progress depends on a material unresolved control gap, for example:

- a decision accepted without the intended verification;
- a test skipped for a stated reason;
- an architectural assumption not confirmed;
- an external or drift-prone claim not refreshed;
- a contradiction temporarily tolerated;
- a reviewer independence claim not established.

Use:

```text
Debt:
Impact: LOW | MEDIUM | HIGH
Reason:
Evidence_missing:
Owner_or_trigger:
Due_or_review_condition:
Status: OPEN | ACCEPTED | RESOLVED | EXPIRED
```

Debt is not proof of failure. It makes a known confidence gap visible. Do not let debt accumulate silently, and do not block low-risk work merely because immaterial debt exists.

## 10. Automatic escalation

Choose the lowest level that provides proportionate confidence:

```text
NORMAL
  ↓
REVIEW
  ↓
DEEP_REVIEW
  ↓
INDEPENDENT_VERIFICATION
  ↓
HUMAN_DECISION_REQUIRED
```

Escalate one level when justified by high impact, irreversibility, security or privacy exposure, financial consequence, production effects, conflicting authoritative evidence, repeated failures, high uncertainty, or incomplete verification.

Escalation means stronger scrutiny or a required decision; it does not automatically mean more agents, more verbosity, or permission to access external systems.

Use `HUMAN_DECISION_REQUIRED` when a missing choice would materially change safety, architecture, public behavior, data, cost, or scope, or when the required action exceeds current authorization.

## 11. Supervisor self-audit

Periodically ask whether supervision is improving the decision or has become the problem.

Detect:

- reflection without new evidence;
- repeated audits of unchanged material;
- unnecessary agents or duplicated reviews;
- context accumulation that obscures the goal;
- verification whose cost exceeds the plausible error impact;
- procedural compliance that does not protect an observable outcome;
- supervisor recommendations that conflict with higher-priority instructions.

When detected, reduce to the smallest useful control, archive only durable conclusions if authorized, and return focus to the task.

Use `SUPERVISION_OVERHEAD` when the marginal cost of another supervisory action exceeds its expected value.

## Integrated control loop

```text
USER GOAL
    ↓
TASK / AGENT / SKILL
    ↓
EXECUTION ─────────→ Tools / Code / Web / MCP
    ↓
RESULT
    ↓
METACOGNITIVE SUPERVISOR
    ├─ Goal and assumption check
    ├─ Evidence and contradiction control
    ├─ Strategy and stagnation evaluation
    ├─ Verification and confidence calibration
    ├─ Skill quality and freshness review
    ├─ Model compatibility
    ├─ Cross-agent independence
    ├─ Meta-memory and failure memory
    ├─ Decision journal and debt
    └─ Self-audit
         ↓
       ACCEPT | REVISE | RETEST | CHANGE_STRATEGY | ESCALATE | STOP
```

## Completion check

Before accepting a result, compare:

- `REQUESTED`: what the user asked for;
- `EXECUTED`: what actually happened;
- `VERIFIED`: what direct evidence proves;
- `REMEMBERED`: what historical evidence influenced the decision;
- `DEBT`: what material uncertainty remains.

Accept the result when success criteria are satisfied, evidence is proportionate to risk, no important contradiction is unresolved, remaining uncertainty is disclosed, and further supervision has low expected information gain.

## Compact user-facing summary

When the supervisory state matters to the user, report only:

```text
Outcome:
Verified:
Uncertainty:
Freshness:
Remaining debt:
Decision: ACCEPT | REVISE | RETEST | CHANGE_STRATEGY | ESCALATE | STOP
Confidence: HIGH | MEDIUM | LOW
```

Omit empty fields and do not expose private reasoning.
