# Contributing to AI Skills

Thank you for helping improve the collection. Contributions should make an agent's
decisions measurably clearer, safer, or more reliable without adding process for its
own sake. Participation is governed by the [Community Code of Conduct](CODE_OF_CONDUCT.md).

## Propose a change

- Use a skill proposal for a new capability and a bug report for a concrete problem.
- Describe a realistic user request, the expected observable result, and the failure
  or decision gap the skill addresses.
- For changes to an existing skill, show the current behavior and the intended one.
- Keep unrelated skills and broad formatting changes out of the same pull request.

## Skill acceptance criteria

Every skill must:

- live in `skills/<skill-name>/` with a matching lowercase hyphenated `name`;
- contain a `SKILL.md` with `name` and a discriminating `description` in YAML
  frontmatter;
- explain what changes the agent's decisions and when the workflow applies;
- preserve the user's task scope and authorization boundaries;
- distinguish observed verification from proposed checks;
- avoid unnecessary dependencies, placeholders, and duplicated documentation;
- link optional resources from `SKILL.md` at the point where they become relevant;
- include realistic acceptance scenarios when behavior is complex or consequential.

Supporting directories are optional:

```text
skill-name/
├── SKILL.md
├── references/     # conditional guidance and source material
├── scripts/        # repeated deterministic operations
└── assets/         # files used in generated output
```

Do not include credentials, private data, proprietary dumps, generated caches, or
instructions copied from another project without compatible licensing and attribution.

## Validate locally

Run the dependency-free repository check:

```bash
python scripts/validate_skills.py
```

Also inspect the final diff and exercise the changed skill on a realistic request
when its behavior warrants evaluation. Passing structural checks does not establish
that a skill is effective.

## Pull request checklist

- The scenario and desired result are clear.
- The change is focused and the skill description routes accurately.
- New local links resolve and optional resources are discoverable.
- Validation passes.
- Behavioral evidence or untested limitations are described honestly.
- External material has compatible licensing and attribution.

By contributing, you agree that your contribution is licensed under this repository's
[MIT License](LICENSE).
