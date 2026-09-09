# Security Policy

## Scope

Security reports may concern unsafe skill instructions, hidden authority expansion,
prompt-injection paths, credential exposure, malicious dependencies or assets, and
other behavior that could cause an agent to cross a trust or permission boundary.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting for this repository:

1. Open the repository's **Security** tab.
2. Select **Advisories** and **Report a vulnerability**.
3. Include the affected skill and version or commit, a minimal reproduction, expected
   and observed behavior, impact, and any proposed mitigation.

Do not publish secrets, private data, or an exploitable proof of concept in a public
issue. If private vulnerability reporting is unavailable, contact the repository
owner through their GitHub profile before disclosing sensitive details.

Reports are assessed against the actual behavior demonstrated within the stated host,
model, permissions, and tool configuration. A prompt-only instruction is not treated
as a hard security boundary unless the environment enforces it.

## Supported versions

The current `main` branch receives security corrections. Older commits and external
forks are not maintained by this project.
