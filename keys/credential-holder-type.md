# The credential holder type

Each API key can record what kind of entity holds it. This is the `credentialHolderType`.

- **Who sets it:** the operator, when the key is issued. A caller cannot set or change it in a request. The field is defined in [`ApiKeyEntry.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/config/ApiKeyEntry.ts).
- **Values:** the same enum as authority types (`USER`, `ROLE`, `SERVICE`, `ORGANIZATION`), defined in [`authority.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/authority.ts).
- **If it is absent:** the key is not verified, and it is treated as not human. The code's comment says an absent value means "not verified," never "assume human."
- **Who is refused:** the human-only checks accept only the exact value `USER`, as implemented in [`isHumanCaller.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/auth/isHumanCaller.ts). A key created before this field existed is refused on those endpoints until it is re-issued with `credentialHolderType: USER`.
