# Business validation and sources (step 12)

For each signal a policy declares as coming from a business system, the runtime asks that system for the value. The value the policy then uses is the source's value, not the caller's.

The checks and their statuses are in [`TrustedSignalResolver.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/business-validation/TrustedSignalResolver.ts). The statuses are in [`business-validation.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/shared/src/domain/business-validation.ts).

- A source answers `observed` (a value), `not_found` or `conflicting`. Only `observed` can be used. See [`BusinessSignalSource.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/business-validation/BusinessSignalSource.ts).
- The production source is [`HttpBusinessSignalSource.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/business-sources/HttpBusinessSignalSource.ts). It signs its request, pins the endpoint, and checks the answer. When the source has a registered key, the answer's signature must verify. Without a key, the signature is not checked.
- The defaults are a maximum age of 300 seconds and a 10-second timeout per source.
- A caller's proposed value that differs from the source's value is `INVALID`.

Any status other than `VALID` refuses the request.
