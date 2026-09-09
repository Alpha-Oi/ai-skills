---
name: complementary-integrity
description: >
  Design or review data integrity and bounded recovery using redundant representations,
  trusted provenance, and explicit corruption models. Use for damaged copies, divergent
  replicas, backup restoration, or recovery workflows inspired by DNA complementarity.
metadata:
  version: "1.0.0"
---

# Complementary Integrity

Use DNA complementarity as inspiration for recoverable data systems. Distinguish
detection, correction, availability, authenticity, and historical recovery: each
requires evidence and may need a different mechanism.

## Scope

Begin with a concrete object, consumer, and failure: a damaged file, conflicting
replicas, interrupted write, or unwanted deletion. Inspect existing storage and
recovery contracts. A review authorizes findings and a design; implement repairs
only within the user's requested scope. Do not modify production data by default.

Read [references/biology.md](references/biology.md) when explaining the biological
analogy. This skill neither explains nor establishes the origin of life.

## Establish what can fail

- Identify the authoritative version and the evidence that makes it authoritative.
- Distinguish known-location erasure from unknown corruption, stale copies,
  concurrent valid edits, malicious alteration, and shared failure of all copies.
- Determine which copies and integrity records share storage, credentials, software,
  or failure domains. Two dependent copies are not independent recovery evidence.
- State acceptable loss and restoration time when they affect the design.

## Choose the smallest sufficient mechanism

- A checksum compared with a trusted expected value can detect a mismatch; it does
  not reconstruct missing data or by itself establish authorship.
- Mirroring improves availability for some failures but can propagate deletion or
  corruption. Preserve history separately when historical restoration is required.
- An independently retained backup can support recovery if its integrity, version,
  and readability are verified.
- Error-correcting codes correct only within their defined error model and budget.
- A deterministic complementary encoding provides a consistency relation; do not
  claim it adds information sufficient to resolve every disagreement.

Reuse existing mechanisms when adequate. Do not add replication or invent a custom
encoding solely because DNA has two strands.

## Resolve disagreement before repair

Compare object identity, version, provenance, trusted integrity records, and
application-level constraints. Do not pick a copy merely because it is newest,
most plausible, or one of two disagreeing copies. Majority agreement also requires
an explicit fault model and sufficiently independent replicas.

If two versions disagree and neither has adequate authority, report
`AMBIGUOUS_SOURCE`, preserve both, and identify the evidence or user decision needed.
Never silently manufacture a supposedly original value.

## Bounded recovery

1. Preserve the original evidence and identify the exact recovery target.
2. Reconstruct into an isolated candidate using a verified source or a justified
   correction rule. Record the source version and method.
3. Check both integrity and the application's ability to consume the result.
4. Activate only within authorization, using the storage system's supported atomic
   or recoverable mechanism where appropriate. Address concurrent writes explicitly.
5. Verify the consumer's outcome. Bound retries; stop if new evidence invalidates
   the chosen source or the recovery exceeds its correction budget.

Self-recovery means automation within these rules. It does not remove uncertainty,
authorization boundaries, or the need to stop on an ambiguous source.

## Example and acceptance scenarios

Two configuration copies disagree on a setting. A hash recomputed from each merely
describes each copy; it does not decide which setting was intended. A trusted
versioned manifest may identify an intact intended version. Without such evidence,
preserve both and report the conflict.

For an authorized implementation, verify recovery from a known damaged copy using
a trusted reference and rejection of an ambiguous disagreement. Add interrupted
activation or shared corruption checks only if the failure model calls for them.
For a design, label scenarios as proposed rather than executed.

## Deliverable

Provide the failure model, authority rule, chosen mechanism, recovery stopping
condition, and observed verification. Distinguish `DETECTED`, `RECOVERED`,
`AMBIGUOUS_SOURCE`, and `UNVERIFIED` outcomes. Stop once the requested failure is
addressed; keep unrelated resilience work as optional follow-up.
