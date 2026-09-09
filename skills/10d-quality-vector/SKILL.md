---
name: 10d-quality-vector
description: >
  Assess non-trivial code changes, fixes, refactors, and architecture alternatives
  using ten engineering quality dimensions. Select the smallest justified intervention
  and produce evidence-backed review findings or comparative scores.
metadata:
  version: "1.0.0"
---

# 10D Quality Vector

Evaluate engineering work using the ten dimensions below. This skill adapts the
user's earlier 10D Quality Vector instructions. It is an engineering decision
framework, not model training or a claim about physical ten-dimensional space.

## Task boundary

Identify the requested outcome, current behavior, constraints, and relevant evidence.
Inspect the affected code, nearby tests, interfaces, and project instructions.
For diagnosis or review, investigate and report. For implementation, make the
bounded authorized change and verify it. This skill does not authorize commits,
publication, migrations, dependency changes, or a broader redesign.

For a small deterministic task, apply only consequential checks without producing
a ten-section report. For non-trivial work, consider all ten dimensions, giving
more attention to those that could change the decision.

## The ten dimensions

| Dimension | Criterion |
| --- | --- |
| Correctness | Solves the actual problem and meets the required behavior; a symptom workaround is not automatically a root-cause fix. |
| Reliability | Handles relevant edge cases, invalid inputs, partial failures, and unstable dependencies. |
| Maintainability | Is understandable and changeable without hidden coupling or unnecessary duplication. |
| Testability | Allows proportionate verification through focused tests or concrete manual checks. |
| Security | Preserves input, secret, permission, and trust boundaries without unsafe defaults. |
| Performance | Avoids consequential unnecessary computation, I/O, blocking, and database load under the relevant workload. |
| Compatibility | Preserves applicable public APIs, data contracts, and runtime assumptions unless their change is explicitly authorized. |
| Observability | Makes important failure modes diagnosable through suitable errors, logs, metrics, or structured diagnostics. |
| Simplicity | Uses the least complexity that adequately addresses the problem; abstractions need a concrete benefit. |
| Architectural Fit | Respects module boundaries, ownership, data flow, and source-of-truth rules. |

These dimensions can overlap. Avoid counting one finding repeatedly. Supporting
evidence may be shared, but a high score in one dimension does not prove another.

## Select the intervention

Distinguish the observed symptom, supported cause, affected layer, and remaining
uncertainty. Where there is no defect, describe the requested capability and design
constraint instead of inventing a root cause.

Classify the proposed intervention using the smallest applicable category:

- `local fix`: a focused correction within an existing contract;
- `refactor`: behavior-preserving restructuring justified by the task;
- `file rebuild`: replacing a file's implementation where a focused fix is inadequate;
- `module rebuild`: replacing a module implementation or design within authorized scope;
- `integration-layer fix`: correcting a mismatch between components or contracts;
- `architectural redesign`: changing system responsibilities or boundaries.

These are categories, not a mandatory escalation sequence. Explain why the selected
level addresses the cause and whether it fits the user's authorization. A higher
score for a redesign does not authorize it. If only a broader change can solve the
problem, present the evidence and the concrete scope decision required.

Prefer a focused solution that addresses the cause without creating avoidable debt.
If a temporary mitigation is justified, identify its residual limitation and the
condition for revisiting it. Do not disguise it as a complete repair.

## Evaluate and compare

For a single change, record relevant evidence and gaps without manufacturing scores.
When comparing alternatives or when a scorecard is requested, use a 1–5 scale with
the same scoped criteria for each option:

- `1`: observed failure of an essential criterion;
- `2`: supported material weakness or incomplete coverage;
- `3`: adequate for the stated scenario, with identified limitations;
- `4`: strong coverage supported by relevant evidence beyond the basic path;
- `5`: the stated demanding criterion is demonstrated within the evaluated scope.

Use `NOT_VERIFIED` when evidence is insufficient and `NOT_APPLICABLE` with a reason
when the criterion does not apply. Neither is zero. Five does not mean universally
perfect. Mark design-only judgments `PROJECTED`; distinguish them from executed
checks. Do not confuse a source-code observation with runtime validation.

Use a compact table when it improves comparison:

| Dimension | Option A | Option B | Evidence or uncertainty |
| --- | --- | --- | --- |
| Relevant criterion | Score or status | Score or status | Scope and supporting check |

Do not choose by the highest sum. First satisfy hard requirements, then weigh
root-cause coverage, implementation risk, maintainability, compatibility, time cost,
and regression risk against the user's priorities. A security or correctness blocker
cannot be offset by good performance or readability scores.

Inspect decisive interactions: retries can duplicate side effects, logging can
expose secrets, caching can serve stale data, and abstraction can increase maintenance
cost. Use only interactions supported by the scenario. Prefer measurement over
unsubstantiated performance claims.

## Review mode

Report actionable findings grounded in the changed code and affected behavior.
Include a location when available, the triggering condition, consequence, and a
proportionate correction. Group only when it helps:

- **Critical Issues:** correctness, security, data integrity, or production behavior;
- **Structural Issues:** boundaries, coupling, ownership, contracts, or maintainability;
- **Local Issues:** concrete local defects or useful simplifications, not personal taste.

Do not invent findings to fill groups. Cross-reference one issue across dimensions
instead of presenting it as several independent defects.

Give one review recommendation:

- `approve`: no blocking finding within the reviewed scope and adequate evidence;
- `approve with minor changes`: only clearly non-blocking corrections remain;
- `request changes`: material corrections or required verification remain;
- `block merge`: an essential criterion demonstrably fails or a mandatory merge gate
  is unsatisfied.

State limitations alongside the recommendation. These are review recommendations;
they do not claim that a merge gate was changed or that a formal approval was sent.

## Implementation and verification

Apply the chosen bounded intervention only when requested. Preserve unrelated work.
Run the narrowest meaningful project-defined check, then any additional check
required by the affected contract. Verify the observed problem and a consequential
regression case. A successful edit or passing syntax check is not proof of behavior.

If a check cannot run, report what remains unknown and the needed command or condition.
Revisit only affected dimensions after new evidence. Do not repeat all analysis after
an unrelated change or add tests that merely mirror implementation details.

## Result

Lead with the outcome or recommendation. For complex work, cover the useful parts of
the original structure without forcing empty sections:

1. **Analysis:** observed behavior, supported cause, affected layer, risk, intervention.
2. **Solution:** concrete correction or proposed design and why it fits.
3. **Implementation:** what actually changed, or where a proposed change would apply.
4. **Verification:** checks and actual outcomes, unverified claims, regression concerns.
5. **Next Step:** one useful follow-up only when needed.

Include a 10D scorecard only when requested or useful for a real comparison. Provide
decision-relevant evidence summaries, never private chain-of-thought.

## Acceptance examples

- **Retry bug:** a second attempt duplicates a write. Inspect transaction and retry
  behavior, choose the smallest correction, and verify the duplicate-effect case.
  Do not recommend a module rewrite merely for a higher projected quality score.
- **Fast but incompatible option:** an optimization breaks a required public contract.
  Treat compatibility as a blocker even if other scores improve.
- **Review without runtime access:** distinguish inspected source evidence from
  `NOT_VERIFIED` runtime behavior. Do not claim passing tests or assign a confident
  reliability score without evidence.

These are expected behavior scenarios, not claims of executed evaluations. Stop when
the requested outcome is addressed and additional analysis is unlikely to affect it.
