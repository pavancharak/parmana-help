# The governance anchor

The anchor records whether the approval behind a policy can be verified. It never changes the decision.

The resolver is [`PolicyGovernanceAnchorResolver.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/governance/PolicyGovernanceAnchorResolver.ts). It returns one of four results:

- `NO_APPROVAL_RECORD`: no approval record exists for the policy version.
- `SIGNATURE_INVALID`: a record exists, and its signature does not verify.
- `CONTENT_MISMATCH`: the signature verifies, but the approved content is not the content loaded.
- `VERIFIED`: the record exists, its signature verifies, and its content is the content loaded.

The execution-time governance check is a different thing. It runs the same three checks and refuses the execution. See [the decision steps](../authorize/decision-steps.md), step 7.
