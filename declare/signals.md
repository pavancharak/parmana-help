# Signals

A **signal** is a fact the caller sends with the request, for example `amount` or `refundEligible`. The policy decides on the signals.

**Required.** `signals` must be an object. A request without it, or with it null or not an object, is refused with `400` (`signals is required and must be an object.`). This is owner decision D21. The type and the published schema already said so, and the SDKs send it. Before this, a missing value was silently treated as `{}`. The check is in [`BusinessTransactionValidator.ts`](https://github.com/pavancharak/parmana-core/blob/1a977714/packages/runtime/src/validators/BusinessTransactionValidator.ts). The published schema is [`transaction-create-request.schema.json`](https://github.com/pavancharak/parmana-core/blob/1a977714/schemas/requests/transaction-create-request.schema.json).

**Checked against the policy's types at declare.** The policy declares each signal's type in `signalsSchema` (`boolean`, `number` or `string`). A signal the request sends with a different type is refused with `400`, and the message names the signal and both types. Example: `signals.amount must be a number; got string.` Signals the schema does not declare are not checked. Absent signals are not checked here either.

**Checked again at evaluation.** The same rule runs when the policy is evaluated, so a mismatch is refused in both places. The rule is in [`signalTypes.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/signalTypes.ts), and the engine calls it in [`PolicyEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/PolicyEngine.ts).

**A missing fact is refused, not matched.** If a rule reads a fact the request did not send, the request is refused at evaluation. See [policy evaluation](../authorize/policy-evaluation.md).
