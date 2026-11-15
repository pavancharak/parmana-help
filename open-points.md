# Open points

Questions the code does not settle yet, grouped by topic. Each item links to its help page, where there is one, and to the source open list.

## Owner decisions

- Whether declare should be one call or two ([declare](declare/checks.md)).
- Whether a tenant refusal should write an audit event ([refusals](refusals/refusal-table.md)).
- Whether the stored transaction should drop a caller's `policy.contentHash` and `governanceAnchor` ([declare](declare/checks.md)).
- The contract test for the declare documents is not merged or run in CI ([declare](declare/checks.md)).
- The G-77 classification of write capabilities, which blocks the Razorpay binding ([08-connectors OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/08-connectors/OPEN.md)).

## Not read yet

- The receipt's HTTP status, and whether a `FAILED` verification is visible to a caller ([prove](prove/verification.md)).
- What `executions` and `overrides` contain in a trust record ([prove](prove/verification.md)).
- The contents of an approval record, and how it is signed ([governance](govern/proposal-and-approval.md)).
- The release path without execution control, and how a retry after a lost response is recovered ([execute](execute/gateway-checks.md)).
- The full list of audit event types ([refusals](refusals/refusal-table.md)).
- How the envelope and trust-record keys are provisioned, rotated, and whether they must differ ([signing keys](keys/signing-keys.md)).

## Connectors (no help page yet)

- The connector's own behaviour, including what it sends and returns ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md), [08-connectors OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/08-connectors/OPEN.md)).
- Whether registration rejects two connectors that list the same action. Not read ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md)).
- The reason for the registration-order rule in connector selection, and for the wire hash in `HttpConnector.ts`. No reason was found in the code read ([03-execute OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/03-execute/OPEN.md)).
- Whether the registration check on built-in namespaces covers names outside the namespace list. Answered: the check is per namespace ([external registration](https://github.com/pavancharak/finalflowparmana/blob/main/08-connectors/external-registration.md)).

## parmana-connect (no help page yet)

- The connector's behaviour against the external system: the HTTP call was not read ([parmana-connect OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/parmana-connect/OPEN.md)).
- Whether the bearer path applies the 16 KB result check that the signed-release path applies ([parmana-connect OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/parmana-connect/OPEN.md)).
- The reasons for the manifest validation rules ([parmana-connect OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/parmana-connect/OPEN.md)).
- The doctor command's checks, which were not read ([parmana-connect OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/parmana-connect/OPEN.md)).
- The fixtures and tests were not run ([parmana-connect OPEN](https://github.com/pavancharak/finalflowparmana/blob/main/parmana-connect/OPEN.md)).
