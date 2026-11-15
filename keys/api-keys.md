# Caller API keys

A caller API key identifies the caller of the API. The operator issues it with [`scripts/generate-api-key.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/scripts/generate-api-key.ts), using `--caller-id`.

- **What is stored:** only a SHA-256 hash of the key. The raw key is shown once. The code says: "Only the SHA-256 hash of the raw key is ever held here, never the key itself." ([`ApiKeyEntry.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/config/ApiKeyEntry.ts))
- **Holder type:** `--credential-holder-type` sets who holds the key. Without it, the key is treated as not human. See [the credential holder type](credential-holder-type.md).
- **Step-up key:** `--generate-step-up-key` also creates a step-up key. Only a key that may approve policy changes needs one. See [step-up keys](step-up-keys.md).
- **Rotation:** several entries may share one caller ID. To rotate, add the new hash, keep the old one active during migration, then remove the old entry to revoke it. The comment in [`ApiKeyEntry.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/config/ApiKeyEntry.ts) describes this.
