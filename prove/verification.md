# Verifying an execution record

Verification checks a stored execution trust record. The check is [`verification-service.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/services/verification-service.ts). Each check adds a failure to a list. The result is `VERIFIED` when the list is empty, and `FAILED` otherwise. Either result is stored as a new, immutable verification.

If the record does not exist, verification fails with "Execution Trust Record not found." No record means no verification.

The checks:

1. **Integrity.** The hash recomputed over the record must equal `trustRecordHash`.
2. **Signature.** The record's signature must verify against the stored key.
3. **Authorization binding.** Every execution whose decision was `APPROVED` must carry an `authorizationId`.
4. **Chain integrity.** Each chain-protected execution's hash and signature must verify, and each `previousChainHash` must match its predecessor. Executions before the first chained one, with no chain fields, are legacy data and do not fail this check.

**Hybrid signatures.** When a record carries a `signatures` array, the signature check verifies every entry, and each must pass. The method is [`VerificationCrypto.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/crypto/src/VerificationCrypto.ts). If the array is removed, only the legacy signature is checked, unless `HYBRID_SIGNATURE_REQUIRED=true` is set. The setting is off by default.
