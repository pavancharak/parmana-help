# The decision steps

The runtime makes the decision in [`RuntimeEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/RuntimeEngine.ts), method `decide`. The steps run in the order below. Each one either passes the request on or refuses it.

1. Read the signals. An absent value becomes `{}`.
2. Run `beforePolicyLoad` hooks. None is registered for this step in production. See [hooks](hooks.md).
3. Load the policy named by the request, and validate it.
4. Run `afterPolicyLoad` hooks. None is registered for this step in production.
5. Hash the policy's content as loaded.
6. Resolve the governance anchor. This records a result; it never changes the outcome. See [the governance anchor](../govern/governance-anchor.md).
7. Check that the policy has an approval record. A missing one is refused as an authority problem.
8. Evaluate the authority grant, for policies that require one. See [business validation](business-validation.md) for the statuses it shares.
9. Check the signals against the policy's `boundSignals`, where the policy declares them.
10. Check that the policy named is the one in effect for the capability. See [the policy version in effect](policy-version.md).
11. The authority decision.
12. Business validation: the facts the policy needs are established by their sources. See [business validation](business-validation.md).
13. Evaluate the policy. The outcome is `APPROVE` or `REJECT`. See [policy evaluation](policy-evaluation.md).
14. Re-verify the signal state. See [approval signals](approval-verifier.md).
15. Record a refusal when the decision is `REJECT`.
16. Approve gate: only an approved decision is signed.

Only after step 16 does `execute` sign the authorization. That signed authorization is the handoff to Execute. See [the stage decision](stage.md).

The steps' numbering is the order of the documents. In the code, step 10 runs before steps 8 and 9 (see [`RuntimeEngine.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/RuntimeEngine.ts), lines 418, 437 and 458).
