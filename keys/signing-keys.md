# Signing keys

Parmana signs three kinds of record with a key: the execution authorization, the trust record, and the audit and refusal records.

**Which key.** The key is named by its ID. The default ID is `default` ([`KeyProvider.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/crypto/src/KeyProvider.ts)). A deployment can name its own key with `PARMANA_SIGNING_KEY_ID`. The value is read on every call. A tenant can have its own key, named `tenant.<tenantId>`. If no such key exists, the default key is used ([`TenantKeyResolver.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/TenantKeyResolver.ts)).

**Where the keys are read from.** The file provider reads `<keyId>.private.pem` from the directory set by `PARMANA_KEY_DIR`. Keys are created with [`scripts/generate-keypair.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/scripts/generate-keypair.ts).

**Which key signs an authorization.** The runtime's signer uses the key ID that `currentSigningKeyId()` returns, or the tenant key for the request ([`RuntimeAuthorizationSigner.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/RuntimeAuthorizationSigner.ts)).

**Which key signs the durable evidence.** Verification, refusal and audit records use their own signers, which use `currentSigningKeyId()` for new signatures ([`VerificationCrypto.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/crypto/src/VerificationCrypto.ts)).

**Not yet settled.** How the key for the authorization is provisioned in each deployment, how rotation works for the envelope and trust-record keys, and whether those two keys must differ. The [finalflowparmana](https://github.com/pavancharak/finalflowparmana) folder [06-keys-and-signing](https://github.com/pavancharak/finalflowparmana/tree/main/06-keys-and-signing) lists these as open.
