# Checks at declare

A request to `POST /transactions` is checked in this order. A refusal stops the request, and the status code and audit event are listed.

1. **The transaction ID is a UUID.** Refused with `400` and the audit event `caller.structural_rejected`. The check is in [`transactions.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/routes/transactions.ts).
2. **The caller may assert the principal, the tenant and the capability.** These run only when the request has an authenticated caller. Refusals are `403`, with the codes `TENANT_NOT_ALLOWED` and `CAPABILITY_NOT_ALLOWED` where they apply. The tenant refusal writes no audit event.
3. **The shape of the transaction.** Every object is present and of the right kind, including `signals`. Refused with `400`. The check is in [`BusinessTransactionValidator.ts`](https://github.com/pavancharak/parmana-core/blob/1a977714/packages/runtime/src/validators/BusinessTransactionValidator.ts).
4. **The trust chain.** `metadata.businessTransactionId` must equal `businessTransactionId`.
5. **The signals against the policy's types.** A present signal of the wrong type is refused with `400`. See [Signals](signals.md). The check is in [`business-transaction-service.ts`](https://github.com/pavancharak/parmana-core/blob/1a977714/packages/runtime/src/services/business-transaction-service.ts).
6. **Duplicate.** An ID already accepted is refused with `409`.

Only after these checks does the decision run (see [the decision steps](../authorize/decision-steps.md)).

The full list of steps, with the reasons written in the code, is in [`DECLARE_STAGE.md`](https://github.com/pavancharak/parmana-core/blob/1a977714/docs/DECLARE_STAGE.md).
