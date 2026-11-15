# How a policy is evaluated

The engine is [`PolicyEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/PolicyEngine.ts). It returns `APPROVE` or `REJECT` ([`PolicyOutcome.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/types/PolicyOutcome.ts)). Nothing else is returned.

**The order.**

1. **Signal types.** A signal present with the wrong type is `REJECT` (`signal-type-violation`). See [signals](../declare/signals.md).
2. **Rules, in order.** The first rule whose condition is true decides. Its action gives `APPROVE` or `REJECT`.
3. **A rule that cannot be decided.** If the condition reads an absent fact, the request is `REJECT` at once (`missing-fact`). Later rules are not tried.
4. **No rule matched.** `REJECT` (`no_rule_matched`).

**Absent facts.** A fact is absent when the request has no key for it. An absent fact is unknown for every operator, including `not_exists`, `is_null` and `is_false`. So a rule that depends on an absent fact refuses. A value sent as JSON `null` is present, and the operator decides it. The rule is in [`PolicyEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/PolicyEngine.ts) (`truthOf`).

**The operators.** There are 28. Each is defined in [`OperatorEvaluator.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/policy/src/OperatorEvaluator.ts). The groups are equality (`eq`, `neq`), numbers (`gt`, `gte`, `lt`, `lte`, `between`), sets (`in`, `not_in`), collections (`contains`, `not_contains`, `contains_all`, `contains_any`), strings (`starts_with`, `ends_with`, `matches`), existence (`exists`, `not_exists`), booleans (`is_true`, `is_false`), null (`is_null`, `is_not_null`), length (`length_eq`, `length_gt`, `length_gte`, `length_lt`, `length_lte`), and type (`type_is`).

**Two things a policy author should know.**
- `eq`, `neq`, `in`, `contains` and the other collection operators compare objects and arrays by identity. A value from a JSON request is never the same object as the policy's value, so `eq` on an array or object is always false. This is an open decision (FINDINGS 12 in the [finalflowparmana](https://github.com/pavancharak/finalflowparmana) repository).
- `length_eq 0` is true for any number, boolean or `null`, because their length is 0.
