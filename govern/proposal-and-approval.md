# Proposing and approving a policy change

A policy change is proposed by one person (the maker) and approved or rejected by another (the checker). An approval is recorded before the policy file is written.

**The endpoints** are in [`pending-policy-changes.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/routes/pending-policy-changes.ts):

- Propose: `POST /policies/:name/:version/pending-changes` (maker).
- Approve: `POST /policies/pending-changes/:id/approve` (checker).
- Reject: `POST /policies/pending-changes/:id/reject` (checker).

**The rules for approve and reject**, in the order the code applies them:

1. The caller is authenticated. Otherwise `401`.
2. The caller is a human. Otherwise `403`, `NON_HUMAN_CALLER_DENIED`.
3. The checker is listed for this policy. The list is read from `POLICY_CHANGE_CHECKERS` ([`policyChangeCheckers.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/governance/policyChangeCheckers.ts)). Otherwise `403`, `CHECKER_NOT_IN_SCOPE`.
4. The maker is not the checker. Otherwise refused with `SameActorCannotApproveOwnChangeError`.
5. The step-up signature is valid. Each request is signed by a different key, for the checker making the call. Otherwise refused with `StepUpAuthorizationInvalidError`.
6. The change is still pending. Otherwise a conflict.

**What approval does, in order.** The approval service writes the signed approval record first ([`PolicyChangeApprovalService.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/governance/PolicyChangeApprovalService.ts)). Only then is the policy file written. If the file were written first, a failure could leave a changed policy with no approval record.

**A rejection** writes no approval record and leaves the policy file as it was.

## Open points

- The contents of an approval record, and how it is signed. `PolicyChangeCrypto` was not read. ([05-policy-governance OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/05-policy-governance/OPEN.md))
- The step-up envelope's exact fields, and its expiry rule. The verifier's class comment was read only in part. ([05-policy-governance OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/05-policy-governance/OPEN.md))
