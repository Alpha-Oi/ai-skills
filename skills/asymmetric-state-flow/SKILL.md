---
name: asymmetric-state-flow
description: >
  Design or review distinct forward and reverse transitions between state compartments,
  preserving intentional asymmetry and bounding reconciliation. Use for promotion,
  rollback, or partition rebalancing where bidirectional synchronization is incorrect.
metadata:
  version: "1.0.0"
---

# Asymmetric State Flow

Use directional lipid movement as inspiration for preserving intentional differences
between system compartments. This skill concerns distribution and transition rules;
Aquaporin Flow concerns payload filtering and delivery. Neither depends on the other.

## Establish the invariant

Identify the two compartments, the objects they contain, and why their states should
differ. Name the user-visible outcome. Inspect existing transition mechanisms before
proposing new ones. A review returns findings; implementation and migrations require
the corresponding user scope.

Read [references/biology.md](references/biology.md) for biological explanations.
Do not infer that every system should have exactly two compartments.

## Define direction-specific contracts

For each needed direction, state:

- eligible object and source state;
- authorized initiator and preconditions;
- transition effect, including copy versus move;
- invariant that must remain true;
- completion evidence and failure outcome.

Do not derive the reverse operation by mechanically reversing the forward one.
Promotion may require validation; rollback may require a retained compatible version
and may be unable to undo side effects. An allowed move does not imply an allowed
copy, and rollback is not synonymous with restoration of all external state.

## Control convergence explicitly

Treat reconciliation or mixing as a separate operation, not default two-way sync.
State its trigger, authorized objects, conflict rule, bounds, stop condition, and
which invariant it may intentionally relax. Preserve access and sensitivity
boundaries even when distribution changes.

If no justified mixing scenario exists, omit this operation. The biological presence
of scramblases does not require software to support unrestricted merging.

## Preserve consistency during movement

Use the system's existing transaction, version check, or coordination mechanism to
avoid lost updates and duplicate activation where relevant. Define whether partial
progress can remain visible. If retries are possible, specify deduplication and
bounded retry rules. Reject a stale transition when its preconditions no longer
hold instead of replaying it blindly.

Measure whether the intended distribution and consumer behavior hold after the
operation. An accepted command alone does not prove the transition completed.

## Example: draft and active configuration

Drafts may be incomplete; the active compartment requires a validated compatible
configuration. Promotion activates a specific validated revision. Rollback selects
a retained compatible revision rather than copying the current draft backwards.
Concurrent draft edits must not silently change the revision being promoted.

There is no default merge between draft and active states. If reconciliation is
requested, define how conflicts are resolved before changing either state.

## Verification and output

For implementation, check an allowed transition and a prohibited or stale one.
Check duplicate or interrupted movement only where relevant to the failure model.
For a design, give these as proposed acceptance scenarios.

Return a compact transition table when it improves clarity, along with the protected
invariant, any explicit reconciliation rule, and observed verification. Stop when
the requested transition behavior is addressed; do not broaden into an unrequested
deployment, migration, or synchronization subsystem.
