---
name: contextual-structures
description: >
  Design or review structured interfaces whose meaning depends on typed relationships,
  local context, and changing versions. Use when flat labels lose necessary meaning
  or mutable graphs cause inconsistent interpretation, inspired by glycan recognition.
metadata:
  version: "1.0.0"
---

# Contextual Structures

Represent meaning through the relationships and state that a consumer actually
needs. Glycan branching inspires this approach; complexity is not a design goal.

## Establish the use case

Identify the consumer, its decision, the current representation, and a concrete
case where a flat label or sequence loses necessary information. If no such case
exists, keep the simpler representation. Review or design requests do not authorize
schema migrations or implementation.

Read [references/biology.md](references/biology.md) when describing the biological
basis. Do not treat surface patterns as a universal codebook with fixed meanings.

## Model only consequential context

1. Define node identity separately from display labels. Specify edge types,
   direction, multiplicity, and ordering only where they affect interpretation.
2. Decide whether a tree suffices or shared nodes and cycles require a graph.
   Define validity rules for missing references, cycles, and duplicate identities.
3. Define the context a reader uses: neighborhood, owner, environment, or version.
   Bound traversal depth or work when input can grow. Avoid enumerating all possible
   configurations.
4. Make interpretation explicit: identify which relationships change a result and
   which variations are equivalent. A label or pattern match alone is not proof of
   identity, permission, or truth.

## Handle change coherently

Specify the smallest consistent read unit. Use a snapshot, revision check, or an
existing transaction mechanism when readers must not mix old and new relationships.
Define the allowed edits and how they preserve validity; do not expose half-applied
edits to a consumer whose contract requires a complete structure.

If derived results are cached, identify their dependencies and invalidate or key
them by the relevant revision. Handle an unknown version or missing context as an
explicit incomplete result rather than silently reverting to a flat interpretation.
Choose history retention only when audit or recovery requirements justify it.

## Example

A capability labelled `read` belongs to a particular resource and environment.
Flattening all such labels into a global set loses their scope. Represent the
relationship between capability, resource, and environment; evaluate against one
coherent version. Keep actual authorization in the existing enforcement mechanism.

The same label on a different resource must not inherit the first resource's result.
A graph change must invalidate an affected cached interpretation.

## Verification

For an implementation, test the identified loss-of-context case: identical labels
with different relevant relationships should yield the intended different result.
Check one material update case, such as a stale cache or a reader observing a
changed relationship. Use existing focused checks, adding broader concurrency or
size tests only when the workload needs them. For designs, state these as acceptance
criteria and do not claim execution.

## Deliverable

Provide the smallest schema or focused change, a meaningful example, interpretation
rules, consistency rule, and verification status. Explain why each added relation
is necessary. Do not install a graph database or introduce an ontology merely to
match the biological metaphor; preserve the user's scope and existing architecture.
