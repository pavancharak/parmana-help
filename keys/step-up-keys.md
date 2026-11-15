# Step-up keys

A step-up key signs an approve or reject request for a policy change. It is separate from the caller's API key, so a leak of one does not reveal the other.

- **Algorithm:** Ed25519, always. The rule is in [`PolicyChangeStepUpAuthorizationCrypto.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/crypto/src/PolicyChangeStepUpAuthorizationCrypto.ts).
- **Generated separately:** the script creates the key pair on its own, not from the API key. The key is shown to the operator once ([`generate-api-key.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/scripts/generate-api-key.ts)).
- **Per request:** each step-up envelope is signed by a key for the checker making that request. The check is in [`PolicyChangeStepUpVerifier.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/auth/PolicyChangeStepUpVerifier.ts).

The approval flow that uses these keys is described in [proposing and approving a policy change](../govern/proposal-and-approval.md).
