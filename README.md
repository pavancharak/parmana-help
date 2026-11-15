# Parmana help

Plain explanations of how Parmana works. Each statement links to the source file it describes, at a fixed commit, so the line you open is the line the explanation is about.

## Pinned commits

| Commit | What it is | Used for |
| ------ | ---------- | -------- |
| [`509a47e5`](https://github.com/pavancharak/parmana-core/blob/509a47e5/) | `parmana-core` before the 15 November 2026 changes | Most source files |
| [`1a977714`](https://github.com/pavancharak/parmana-core/blob/1a977714/) | `parmana-core` main after PR #644 | Declare-stage signal checks and the requirement for `signals` |
| [`df15cf65`](https://github.com/pavancharak/parmana-core/blob/df15cf65/) | `parmana-core` main after PR #641 | The tie-break fix and its migration |
| [`e771d973`](https://github.com/pavancharak/parmana-core/blob/e771d973/) | `parmana-core` main after PR #645 | The corrected verifier comment |
| [`4982964e`](https://github.com/pavancharak/parmana-core/blob/4982964e/) | `parmana-core` main after PR #646 | Decision D22 |

## Written so far

- **Declare**
  - [Checks at declare](declare/checks.md): what a request is checked for, in order, and what each refusal returns.
  - [Signals](declare/signals.md): signals are required, checked against the policy's types at declare and at evaluation, and a missing fact is refused.

## Not yet written

These are planned, with the source files already identified:

- Authorize: the decision steps, policy evaluation, policy version in effect, business validation, approval verifier, hooks, and the stage decision (D22).
- Govern: the governance anchor.
- Prove: the tie-break between approval records.
- Keys: the credential holder type.
- Enums: every enum, its values, and where it is defined.

Each source link is checked against its commit before the page is published.
