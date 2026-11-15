# The credential holder type

Each API key can record what kind of entity holds it. This is the `credentialHolderType`.

- **Who sets it:** the operator, when the key is issued. A caller cannot set or change it in a request. The field is defined in [`ApiKeyEntry.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/config/ApiKeyEntry.ts).
- **Values:** the same enum as authority types (`USER`, `ROLE`, `SERVICE`, `ORGANIZATION`), defined in [`authority.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/authority.ts).
- **If it is absent:** the key is not verified, and it is treated as not human. The code's comment says an absent value means "not verified," never "assume human."
- **Who is refused:** the human-only checks accept only the exact value `USER`, as implemented in [`isHumanCaller.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/auth/isHumanCaller.ts). A key created before this field existed is refused on those endpoints until it is re-issued with `credentialHolderType: USER`.

## What this means in practice

- **To use a human-only endpoint, the key must be issued as `USER`.** The operator sets this when the key is issued. Changing the request does not help.
- **Setting `authority.authorityType` to `USER` in a transaction does not make the caller human.** The transaction's `authorityType` is a label, and the human-caller check does not read it.
- **A refused approval is fixed on the key, not in the request.** Re-issue the key with `credentialHolderType: USER`, then retry.

## Which endpoints check it

- The policy-change routes (propose, list, approve and reject) call `requireHumanCaller`, in [`governanceGuards.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/auth/governanceGuards.ts), which uses [`isHumanCaller.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/auth/isHumanCaller.ts).
- Three routes in [`execution-intents.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/routes/execution-intents.ts) check `isHumanCaller` directly.

## The two fields

| | `credentialHolderType` | `authority.authorityType` |
| --- | --- | --- |
| Where it is | On the API key | On the transaction |
| Who sets it | The operator, when issuing the key | The caller, in each request |
| What it does | The human-only endpoints check it | No decision reads it |
| Defined in | [`ApiKeyEntry.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/config/ApiKeyEntry.ts) | [`authority.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/authority.ts) |

Both use the same enum: `USER`, `ROLE`, `SERVICE`, `ORGANIZATION`. Only `USER` has an effect, and only on the key field.
