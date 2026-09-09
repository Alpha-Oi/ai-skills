---
name: aquaporin-flow
description: >
  Design or review selective data boundaries and staged artifact delivery in AI
  workflows, APIs, and software pipelines using aquaporin and intracellular
  trafficking analogies. Use when allowed content must cross a boundary without
  carrying unintended authority or effects, or when artifacts need verified routing.
metadata:
  version: "1.0.0"
---

# Aquaporin Flow

Translate selective permeability and intracellular transport into explicit,
testable software contracts. Biological mechanisms inspire questions; software
evidence determines whether a proposed design works.

## Select the applicable mode

- **Selective channel:** define what may cross a data or trust boundary and what
  must remain excluded, including effects carried indirectly by valid-looking data.
- **Staged delivery:** define how an artifact is prepared, addressed, transferred,
  received, and activated at its intended destination.
- Use both only when the user scenario needs both. Do not introduce a pipeline,
  queue, agent team, or security subsystem merely to reproduce the metaphor.

For biological explanations or justification of an analogy, read
[references/biology.md](references/biology.md). Ordinary use does not require it.

## Establish the scenario

Identify the producer, intended payload, consumer, boundary, and observable success
condition. Inspect existing interfaces and verification before proposing changes.
If the user requests a design or review, return a design or findings; implement only
when implementation is authorized.

## Selective channel

1. **Specify permeability.** Describe allowed types, required fields, size limits,
   permitted meaning, and forbidden effects. Identify the invariant the boundary
   protects: for example, untrusted text must not become tool-execution authority.
2. **Choose the unit.** Make each accepted unit independently understandable where
   practical. Use bounded records or transactions when useful. Single-file water
   movement does not imply that all software processing must be serial.
3. **Inspect indirect transfer.** Consider what a syntactically valid payload could
   carry across the boundary: instructions, active markup, executable paths,
   destination changes, or references to privileged resources. Test relevant cases;
   do not assume every system has all these risks.
4. **Define the actual barrier.** Select controls that enforce the invariant at the
   receiving boundary: schema validation, escaping for the target context,
   capability checks, or separation of content from executable instructions.
   A prompt saying to ignore malicious content is not a proven security boundary.
5. **Preserve meaning.** If normalization is needed, specify what may change and
   what must remain exact. Revalidate the transformed representation. Reject or
   isolate ambiguous inputs rather than silently repairing consequential meaning.
6. **Keep the useful path efficient.** Measure acceptance, rejection, latency, and
   resource cost against the workload. Optimize repeated work only when freshness
   and trust assumptions still hold. Biological throughput is not a software target.

Acceptance criterion: authorized payload reaches its consumer with required meaning
preserved, while a representative forbidden effect is prevented by an observed
mechanism, not just a stated policy.

## Staged delivery

Map only the stages that already exist or are needed for the scenario:

`Create → Validate → Package → Route → Receive → Activate → Verify`

For each relevant stage, name its input, output, owner, completion evidence, and
failure outcome. One component may perform multiple stages.

- **Create and validate:** establish that the artifact satisfies its next consumer's
  contract before dispatch. Construction success is not proof of delivery.
- **Package:** carry the minimum metadata needed to identify and interpret the
  artifact. Consider an artifact ID, schema version, expected destination, and
  integrity digest only where they serve an actual requirement.
- **Route:** resolve a destination from a trusted routing rule. A payload's claimed
  address is not authority to send data there. Address, identity, and authorization
  are distinct properties.
- **Receive:** check the actual destination, applicable permissions, expected
  version, and integrity. A digest detects mismatch only when its expected value is
  trusted; it does not by itself authenticate the sender.
- **Activate:** integrate into the destination only after acceptance checks. Preserve
  the existing working state until the chosen activation method allows replacement.
- **Verify:** observe the intended consumer using the artifact successfully.
  Transport acknowledgement alone is insufficient.

Where delivery can retry, define duplicate handling and distinguish transient
failure from invalid content. Bound retries and report exhausted attempts. Add
idempotency, atomic replacement, rollback, or quarantine only when the failure model
requires them; never infer exactly-once delivery from an acknowledgement.

## Example: retrieved text entering an AI workflow

Scenario: a retrieval component supplies excerpts for an answer.

- Payload: bounded text excerpts plus source identifiers.
- Protected invariant: source text cannot grant tools or change the user's task.
- Channel: validate the record format and keep retrieved content marked as data.
- Indirect-effect probe: include a retrieved instruction to send private files to
  an external address. The system must not perform that action.
- Delivery: pass the excerpts to the intended answer step and verify that citations
  identify the supplied sources.
- Evidence limit: a successful adversarial probe covers that case; it does not
  establish universal prompt-injection resistance. Enforcement depends on the host's
  actual permission and tool boundaries.

## Proportionate verification

For an implementation, exercise a normal accepted payload and the material boundary
or delivery failure relevant to the change. Depending on the scenario, this may be
wrong destination, malformed input, changed content after validation, duplicate
delivery, or activation failure. Use existing focused checks where possible.

For a design, provide these as acceptance scenarios and label them not executed.
Report what was observed separately from what is proposed.

## Output

Deliver the smallest useful result: a focused design, review finding, or implemented
change with its verification. Make these clear in prose or a compact table:

- permitted payload and protected invariant;
- actual filter or receiving check;
- route and completion evidence, if applicable;
- relevant failure behavior;
- verification result and remaining uncertainty.

Stop when the requested scenario is addressed. A biological metaphor does not justify
additional agents, persistent memory, external writes, or unrelated architecture.
