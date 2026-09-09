---
name: ten-dimensional-review
description: >
  Analyze complex engineering decisions through ten explicit dimensions and their
  interactions. Use for architecture choices, consequential changes, and tradeoffs
  where a locally attractive solution may conflict with system-wide constraints.
metadata:
  version: "1.0.0"
---

# Ten-Dimensional Review

Treat a proposed solution as a point in a ten-dimensional decision space. Each
dimension captures a different property of the same scenario. Examine interactions
to expose local improvements that cause important losses elsewhere.

This is an authored engineering framework inspired by the term “ten-dimensional
space.” It makes no claim about physical dimensions, hidden model capabilities,
mathematical independence of the axes, or superior reasoning simply from using ten.

## Establish the decision

Identify who needs what outcome, the decision being made, the current baseline,
and observable acceptance criteria. Read relevant evidence before evaluating.
Separate hard constraints from preferences. Preserve the user's stated priorities.

Use this skill for a decision with material tradeoffs. For a straightforward task,
check the relevant constraints and finish without generating a ten-part report.
Analysis does not authorize implementation, deployment, agents, or external writes.

## The ten dimensions

| Axis | Question | Useful evidence |
| --- | --- | --- |
| D1 Purpose | Does this solve the user's actual problem, and for whom? | User scenario, acceptance criteria, observed need |
| D2 Context | Under which environment, boundaries, and constraints must it work? | Current configuration, project rules, supported environments |
| D3 Information | What data, meaning, provenance, and consistency must be preserved? | Schemas, source authority, state and retention contracts |
| D4 Structure | Which components, responsibilities, interfaces, and dependencies are affected? | Current code, interface contracts, dependency traces |
| D5 Behavior | What happens on the normal path and relevant alternate inputs? | Executed scenarios, state transitions, consumer behavior |
| D6 Time | What changes across retries, concurrency, restarts, versions, and later use? | Lifecycle rules, ordering, compatibility and freshness evidence |
| D7 Resources | What time, memory, compute, money, and operating effort does it require? | Measurements, workload assumptions, explicit budgets |
| D8 Failure | How can it fail, how is failure detected, and what can be recovered? | Failure cases, recovery checks, observability and rollback limits |
| D9 Trust | Who may do what, and which boundaries or sensitive assets are involved? | Permissions, trust boundaries, actual enforcement mechanisms |
| D10 Evolution | Can people understand, verify, change, and retire the solution? | Tests, ownership, maintenance burden, change and exit paths |

The axes may overlap. Put evidence in its most useful location and cross-reference
it instead of counting the same concern several times. D6 concerns behavior over
time; D10 concerns the ability to deliberately change the system.

## Make a proportionate projection

Briefly consider all ten axes, then select those that can change this decision.
Use a focused projection of the space rather than demanding equal work on every axis.
An omitted axis is not automatically satisfied: mark a consequential gap unknown.

For each material axis, capture only what helps decide:

- requirement or question;
- supporting evidence and its scope;
- status: `SATISFIED`, `VIOLATED`, `UNKNOWN`, or `NOT_APPLICABLE`;
- consequence for the decision and the smallest useful next check.

Use `SATISFIED` only for a stated criterion supported by evidence. A design intention
is not an observed result. Give a concrete reason for `NOT_APPLICABLE` when it matters.
Qualitative findings are the default. Do not invent numerical scores, confidence
percentages, distances, or a universal total-quality score.

## Examine interactions

Identify the few pairs or chains where an improvement in one axis may change another.
For each material interaction, state the proposed change, affected property,
consequence, and evidence or test that would distinguish the alternatives.

Examples to use only when relevant:

- D7 caching savings can conflict with D3 consistency and D6 freshness.
- D4 service separation can improve ownership in D10 but add D8 partial failures.
- D5 automation can reduce manual work while expanding D9 effective authority.
- D8 retries can improve recovery while duplicating D5 effects over D6 time.

Do not enumerate every pair merely because ten axes exist. Review claims of
independence skeptically when options share a dependency or failure domain.

## Compare feasible options

Include the current baseline and only materially distinct alternatives. Reject an
option that violates a hard constraint; benefits on other axes do not compensate
for that violation. An unresolved hard constraint prevents treating the option as
verified feasible, though reversible investigation may continue within scope.

Prefer an option that meets the criteria with less cost and complexity. When one
option is better on one axis and worse on another, describe the tradeoff in the
user's terms. Avoid presenting a preference as a fact.

If weights or scores are explicitly useful, define their units, evidence, and source
of priorities. Check whether a plausible priority change reverses the choice.
Do not average incompatible measurements or hide an important weakness in a total.

Ask for a user decision only when an unresolved preference materially changes the
outcome and cannot be inferred from the request. State the concrete tradeoff.

## Validate the recommendation

Find the assumption or interaction most likely to invalidate the chosen option.
Run the smallest authorized check that can resolve it. For implementation requests,
verify the affected user behavior and material failure case using existing checks
where possible. For design requests, provide acceptance scenarios labelled not run.

After new evidence, revisit the affected axes and their material interactions.
Do not repeat the entire review when unrelated facts have not changed.

## Worked example: caching a changing catalog

Scenario: reduce repeated lookup latency while consumers must see updates within a
user-specified freshness bound. Candidate: cache responses for a fixed duration.

- D1 defines the consumer's latency and freshness requirements.
- D3 identifies which fields must stay consistent and the authoritative source.
- D6 checks expiry, invalidation, and concurrent updates.
- D7 compares measured lookup cost with cache overhead.
- D9 checks whether responses differ by user or permission scope.

The decisive interaction is that lower lookup cost may increase staleness or expose
another user's cached response. A scoped, bounded cache is a candidate only if its
invalidation and keying meet the actual requirements. Otherwise retain the baseline
or investigate another option.

Proposed verification: warm the cache, change the source, and check the freshness
bound; where results are permission-dependent, repeat with distinct permission
contexts. These are illustrative scenarios, not results of executed tests.

## Output and stop condition

Lead with the recommended decision and its decisive evidence. Include a compact
dimension table only when comparison benefits from it, followed by the important
interaction, unresolved uncertainty, and any required next action. Report only
decision-relevant reasoning summaries, never private chain-of-thought.

Stop when the criteria are addressed, material interactions have been considered,
and further review is unlikely to change the decision. If blocked, identify the
specific missing evidence or choice instead of manufacturing a complete assessment.

This skill complements metacognitive supervision: it structures the properties of
the solution being evaluated. It does not require a separate supervisor or agent
for each dimension and does not activate other skills automatically.
