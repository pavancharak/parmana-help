# Which policy version is in effect

A request names a policy and a version. The version in effect for a capability is the one most recently approved for that policy's name. The request's version is accepted only if it matches.

- The rule, and why there is no fallback to a version written in code (owner decision D18): [`createCurrentPolicyVersionSource.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/bootstrap/createCurrentPolicyVersionSource.ts).
- The source reads the most recent approval record for the name: [`GovernedPolicyVersionSource.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/governance/GovernedPolicyVersionSource.ts).
- The check is [`CapabilityPolicyBinding.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/capability-registry/src/CapabilityPolicyBinding.ts) (`CapabilityPolicyBinder`).

**Three outcomes.**

1. A version is approved: it is in effect, and the request must declare it.
2. No version of the name was ever approved: every request for the capability is refused (`409` on `GET /policies/in-effect`).
3. The lookup fails: every request is refused (`503`).

An older version that was approved in the past is refused once a newer one is approved.
