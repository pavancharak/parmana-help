# Enums

Every enum the documents mention, with its values and where it is defined. Meanings are the code's own comments. Where the code has no comment on a value, the entry says so.

| Enum | Values | Defined in |
| ---- | ------ | ---------- |
| `BusinessTransactionStatus` | `RECEIVED`, `POLICY_EVALUATED`, `APPROVED`, `REJECTED`, `OVERRIDDEN`, `EXECUTING`, `EXECUTED`, `FAILED`, `VERIFIED` | [`business-transaction.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/business-transaction.ts). Only `RECEIVED` is ever set in the code. The others are declared and never set. |
| `AuthorityType` | `USER`, `ROLE`, `SERVICE`, `ORGANIZATION` | [`authority.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/authority.ts). The transaction's `authorityType` is a caller-declared label that no decision reads. The API key's `credentialHolderType` uses this enum, and the human-caller check accepts only `USER`. |
| `AuthorityStatus` | `AUTHORIZED`, `NOT_AUTHORIZED`, `AUTHORITY_UNCLEAR`, `AUTHORITY_EXPIRED` | [`business-validation.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/business-validation.ts) |
| `BusinessValidationStatus` | `VALID`, `INVALID`, `MISSING_DATA`, `CONFLICTING_DATA`, `SOURCE_UNAVAILABLE`, `VALIDATION_EXPIRED`, `NOT_EVALUATED` | [`business-validation.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/business-validation.ts) |
| `ExecutionAssessmentStatus` | `EXECUTED`, `NOT_EXECUTED`, `EXECUTION_FAILED`, `EXECUTION_UNKNOWN` | [`business-validation.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/business-validation.ts) |
| `DecisionOutcome` | `APPROVED`, `REJECTED` | [`decision.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/decision.ts) |
| `PolicyOutcome` | `APPROVE`, `REJECT` | [`PolicyOutcome.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/types/PolicyOutcome.ts) |
| `PolicyAction` | `approve`, `reject` | [`PolicyAction.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/types/PolicyAction.ts) |
| `VerificationStatus` | `VERIFIED`, `FAILED` | [`verification.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/verification.ts) |
| `ExecutionStatus` | `PROCESSING`, `COMPLETED`, `FAILED` | [`execution.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/execution.ts) |
| `ExecutionMode` | `SYNC`, `ASYNC` | [`execution.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/execution.ts). `ASYNC` is declared and never set. |
| `PendingPolicyChangeStatus` | `PENDING_APPROVAL`, `APPROVED`, `REJECTED` | [`pending-policy-change.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/pending-policy-change.ts) |
| Signal types | `boolean`, `number`, `string` | [`signalTypes.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/signalTypes.ts) |
| Governance anchor results | `NO_APPROVAL_RECORD`, `SIGNATURE_INVALID`, `CONTENT_MISMATCH`, `VERIFIED` | [`PolicyGovernanceAnchorResolver.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/governance/PolicyGovernanceAnchorResolver.ts) |
