# The gateway's checks before release

Before a signed authorization is released to a connector, the Execution Gateway checks it. The checks run in the order below. The gateway's own comment says: "side-effect-free checks first, nonce consumed last and only on success."

The gateway is [`ExecutionGateway.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/execution-gateway/src/ExecutionGateway.ts). The envelope checks are in [`EnvelopeVerifier.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/envelope-verifier/src/EnvelopeVerifier.ts).

1. **Version.** Only version 1 is accepted.
2. **Signature.** The signature over the payload must verify.
3. **Expiry.** An authorization past its expiry is refused.
4. **TTL policy.** The envelope's lifetime must be within the allowed maximum (300 seconds by default).
5. **Business transaction hash.** Recomputed from the content being forwarded. It must match.
6. **Policy still current.** The live policy's hash must equal the hash signed into the authorization. Required in production.
7. **Policy governance.** The approval record behind the policy must verify. Required in production.
8. **Signals still current.** Runs when the authorization carries a `signalsHash` and a signal-state verifier is wired. The signals are re-verified.
9. **Business conditions.** Each signed condition must still be within its `validUntil`.
10. **Authority grant.** Runs when an authority grant is present. The grant must be unexpired and still the active one.
11. **Decision approved.** Only `APPROVED` is released.
12. **Verification key scope.** A verification-only key may sign only the capabilities it is for.
13. **Not revoked.** The authorization must not be on the revocation list. A read error also refuses.
14. **Nonce.** Must be unseen, then consumed. Consumed last, and only when checks 1 to 13 pass. A forged or mismatched request does not use up a nonce.

**A refusal before the connector runs** is recorded against the nonce, so the outcome is not reported as unknown.

## Open points

- The release path when execution control is not configured. Only part of it was read. ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md))
- How a retry after a lost response is recovered, and which outcome is recorded (`executionOutcomeStore`). Not read. ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md))
- Whether the verification-key scope check (check 12) and the revocation check (check 13) are mandatory in every deployment, or only when their inputs are configured. Not probed in the deployment configuration. ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md))
