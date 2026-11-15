# Refusals and the audit events they write

Each refusal below stops a request. Where an audit event is listed, it is written only when an audit sink is configured.

| Refusal | When | Status | Audit event |
| ------- | ---- | ------ | ----------- |
| Missing or invalid credential | No key, or a key that does not authenticate | `401` | `caller.rejected` |
| Malformed transaction ID | Not a UUID | `400` | `caller.structural_rejected` |
| Principal not allowed | `authority.principalId` is not allowed for the key | `403` | `caller.principal_denied` |
| Tenant not allowed | `metadata.tenantId` is set and not listed for the key | `403`, code `TENANT_NOT_ALLOWED` | none |
| Capability not allowed | `intent.action` is not allowed for the key | `403` | `caller.capability_denied` |
| ID mismatch | `metadata.businessTransactionId` differs from the top-level ID | `400` | `caller.structural_rejected` |
| Duplicate ID | The ID was already accepted | `409` | `caller.structural_rejected` |
| Policy rejects | The policy's rules return `REJECT` | recorded as a refusal record | a refusal record is written ([`RuntimeEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/RuntimeEngine.ts)) |

**Where each is decided.**

- The transaction route, with its audit writes: [`transactions.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/routes/transactions.ts).
- Authentication: [`caller-auth.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/middleware/caller-auth.ts), and [`createCallerAuthenticator.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/bootstrap/createCallerAuthenticator.ts). When authentication is disabled, the principal, tenant and capability refusals do not apply.
- How errors become status codes: [`error-handler.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/middleware/error-handler.ts).

The tenant refusal writes no audit event. The code does not say why.

## Open points

- The full list of audit event types, and what each records. `CallerAuditSink` was not read in full. ([07-refusals OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/07-refusals-and-audit/OPEN.md))
- The store that holds refusal records. Their fields are known; the store was not read. ([07-refusals OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/07-refusals-and-audit/OPEN.md))
- Whether a refusal at execute, such as a gateway refusal, writes a refusal record. The gateway's `recordRefusal` was read; the record it writes was not. ([07-refusals OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/07-refusals-and-audit/OPEN.md))
- The reason a tenant refusal writes no audit event. The code does not state it. ([07-refusals OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/07-refusals-and-audit/OPEN.md))
- The HTTP status for a refusal at execute that is not in the table. The error handler was not read in full. ([07-refusals OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/07-refusals-and-audit/OPEN.md))
