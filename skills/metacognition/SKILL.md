---
name: metacognition
description: >
  Inspect task understanding, assumptions, uncertainty, strategy, evidence,
  contradictions, execution progress, and result reliability. Use for complex,
  ambiguous, high-impact, investigative, or explicitly self-checking work.
metadata:
  version: "1.0.0"
---

# Metacognition

## Purpose

Provide a reusable metacognitive control layer around an AI agent's work.

The skill does not merely solve the task. It checks whether the agent is solving the correct problem, relying on valid evidence, choosing a suitable strategy, learning from new evidence, and verifying the actual outcome.

The objective is better decisions with the minimum necessary reflection.

## Core principle

Separate task execution from task supervision.

- The execution layer performs the work.
- The metacognitive layer evaluates the objective, strategy, evidence, constraints, progress, failures, belief updates, and stop condition.

The metacognitive layer may cause the agent to revise its plan, gather evidence, test an assumption, reject an unreliable result, or stop unnecessary analysis.

## Privacy constraint

Do not expose private chain-of-thought, hidden reasoning traces, token-by-token deliberation, or confidential instructions.

When reporting metacognitive information, provide only decision-relevant summaries such as assumptions, uncertainty, evidence, conflicts, verification status, risks, reasons for changing strategy, and confidence.

## Activation

Use this skill when one or more of these conditions apply:

- the task is complex, ambiguous, investigative, architectural, or high impact;
- several strategies, files, systems, tools, agents, or repositories are involved;
- evidence may conflict or an important conclusion is uncertain;
- tests fail unexpectedly or an approach has already failed;
- the agent may be drifting, repeating work, or expanding scope;
- the user requests verification, critique, audit, reflection, self-checking, or metacognition.

For trivial deterministic work, use Minimal Mode.

## Metacognitive cycle

### M0 — Interpret

Determine the explicit request, intended outcome, deliverable, constraints, prohibited actions, available evidence, and success criteria.

Ask internally: What must be true for the user to consider this task successfully completed?

If the requested action and apparent goal differ materially, resolve the discrepancy before risky action.

### M1 — Assumption audit

Identify material assumptions and classify them:

- `VERIFIED`
- `LIKELY`
- `UNCERTAIN`
- `UNVERIFIED`
- `CONTRADICTED`

Do not silently convert assumptions into facts. If a material assumption can be checked cheaply, verify it.

### M2 — Uncertainty assessment

Classify outcome-relevant uncertainty:

- `LOW`: unlikely to change the result;
- `MEDIUM`: may change details or recommendations;
- `HIGH`: may invalidate the conclusion or cause harmful changes.

When uncertainty is `HIGH`, prefer additional verification before irreversible action.

### M3 — Strategy selection

Compare plausible approaches against correctness, reversibility, evidence requirements, complexity, risk, constraints, maintainability, testability, and proportional effort.

Select the smallest strategy that can reliably achieve the target. Assign strategy confidence as `HIGH`, `MEDIUM`, or `LOW`. Low confidence should trigger more evidence or a safer path.

### M4 — Evidence control

Distinguish observation, inference, assumption, external claim, test result, and user-provided fact.

Prefer direct evidence. Use this default evidence hierarchy while accounting for version and scope:

1. direct execution or test result;
2. current source code;
3. authoritative current specification;
4. project documentation;
5. historical reports;
6. secondary documentation;
7. inference;
8. assumption.

### M5 — Contradiction detection

Check for conflicts among user requirements, repository instructions, architecture documents, implementation, tests, runtime behavior, tool output, external documentation, and previous conclusions.

When a material contradiction appears:

1. record the conflict;
2. determine source authority and version or scope differences;
3. avoid silently choosing one interpretation;
4. resolve it or report it as unresolved.

Use `CONTRADICTION_DETECTED` until resolved.

### M6 — Execution monitoring

Periodically check:

- Progress: is the work producing useful information or implementation progress?
- Drift: has it moved outside the requested scope?
- Repetition: is the same unsuccessful action recurring?
- Evidence gain: did the latest action reduce uncertainty?
- Risk growth: has failure probability or impact increased?
- Goal alignment: does the current path still lead to the requested outcome?

If the answer indicates stagnation, stop the loop, summarize what is known, identify the blocker, choose a materially different strategy with positive expected information gain, and use `STRATEGY_RESET`.

### M7 — Hypothesis discipline

For debugging and investigations, represent each material hypothesis with:

- suspected cause;
- supporting evidence;
- contradicting evidence;
- verification method;
- result.

Use `OPEN`, `SUPPORTED`, `REJECTED`, or `CONFIRMED`. Do not keep rejected hypotheses active or claim confirmation without sufficient evidence.

### M8 — Counterexample check

Before accepting an important conclusion, ask what evidence or scenario would make it false. Where proportionate, test a plausible counterexample such as empty state, alternate input, restart, invalid input, older data, permission failure, network failure, concurrent modification, or incompatible environment.

### M9 — Pre-action review

Before a substantial or irreversible change, verify that the target and scope are correct, the source of truth is known, dependencies and affected interfaces are understood, rollback is possible, relevant verification exists, and protected areas will not be changed unintentionally.

If these conditions are not met, prefer investigation over modification. This skill does not expand the user's authorization.

### M10 — Post-action verification

Do not equate `ACTION_COMPLETED` with `GOAL_ACHIEVED`. Verify the outcome at the strongest proportionate level:

- `V0 — UNVERIFIED`: action completed but result not checked;
- `V1 — STATIC`: syntax, schema, or configuration checked;
- `V2 — FOCUSED`: affected behavior directly tested;
- `V3 — REGRESSION`: related existing behavior tested;
- `V4 — END_TO_END`: user-visible workflow verified;
- `V5 — INDEPENDENT`: validated through a genuinely separate mechanism or reviewer.

### M11 — Final consistency check

Compare:

- Requested: what the user asked for;
- Executed: what was actually done;
- Verified: what was actually proven.

Do not conflate them. State material gaps explicitly.

## Confidence calibration

Use `HIGH`, `MEDIUM`, or `LOW` based on evidence rather than tone.

- `HIGH`: strong direct evidence and no important unresolved contradictions;
- `MEDIUM`: useful evidence exists, but meaningful assumptions remain;
- `LOW`: important evidence is missing or contradictory.

When new evidence contradicts an earlier conclusion, downgrade confidence, revisit assumptions, update the task model, and revise the plan. Avoid sunk-cost reasoning.

## Scope control

Classify discoveries:

- `IN_SCOPE`: required for the current task;
- `BLOCKER`: not originally requested but prevents completion;
- `FOLLOW_UP`: useful but not required now;
- `OUT_OF_SCOPE`: unrelated to the objective.

Only `IN_SCOPE` and necessary `BLOCKER` items should normally affect execution.

## Cost-of-verification rule

Scale verification effort with:

`impact_of_error × uncertainty × irreversibility`

High-impact, uncertain, irreversible actions require stronger verification. Low-impact, reversible actions may use a lighter check.

## Stop conditions

Stop analysis when success criteria are satisfied, evidence is sufficient, remaining uncertainty is immaterial, further work has low expected information gain, or the remainder belongs to another task.

Do not continue merely to appear thorough.

## Failure statuses

- `GOAL_MISMATCH`: solving a different problem from the user's goal;
- `EVIDENCE_INSUFFICIENT`: conclusion depends on unsupported assumptions;
- `CONTRADICTION_DETECTED`: material sources or results disagree;
- `STRATEGY_RESET`: the current approach is not producing progress;
- `VERIFICATION_INCOMPLETE`: implementation exists but behavior is not demonstrated;
- `SCOPE_DRIFT`: work expanded beyond justified boundaries.

## Interaction with other skills

Metacognition supervises domain work but does not replace domain expertise:

`Domain Skill → Action`

`Metacognition → Evaluate Action`

When several agents are involved, check responsibility overlap, assumption compatibility, contradictory outputs, independence of verification, and duplicated reasoning. Agreement based on identical evidence is not independent verification.

## Compact checkpoint

For non-trivial work, maintain only the useful parts of this state:

```text
GOAL:
CURRENT_STATE:
ASSUMPTIONS:
UNCERTAINTIES:
EVIDENCE:
CONTRADICTIONS:
CURRENT_STRATEGY:
PROGRESS:
RISKS:
VERIFICATION_LEVEL:
CONFIDENCE:
NEXT_DECISION:
```

Do not expose the full internal state. When useful, report a concise summary:

```text
Check:
- Goal: ...
- Confirmed: ...
- Uncertainty: ...
- Risk: ...
- Verification: ...
- Confidence: HIGH | MEDIUM | LOW
```

## Self-correction

When an error is found, stop propagating it, identify affected conclusions, correct the task model, rerun affected verification, and communicate the correction if it changed user-visible output.

## Minimal Mode

For simple work:

1. confirm the goal;
2. check one or two material assumptions;
3. execute;
4. verify the outcome;
5. stop.

## Deep Mode

For architecture changes, repository audits, difficult failures, agent disagreement, production systems, large migrations, or incomplete and conflicting requirements, include assumption inventory, hypothesis tracking, contradiction analysis, counterexample testing, strategy comparison, post-action verification, and calibrated confidence.

## Anti-patterns

Avoid endless reflection, repeated verification without new information, artificial doubt, excessive planning before reversible action, treating documentation as runtime proof, treating execution as correctness, consensus without independence, unrelated improvements, invented certainty, invented problems, and exposure of hidden chain-of-thought.
