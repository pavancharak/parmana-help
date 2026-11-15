# Ties between approval records

Two approvals for the same policy name can have the same time. `approvedAt` has millisecond precision, and approvals of different pending changes are not serialized, so this can happen.

Before the fix, the repositories broke the tie differently. Postgres used the random record ID, and the lookup by name and version had no tie-break at all. The in-memory repository kept the later-inserted record.

After the fix (PR #641), every "most recent" lookup orders by time, then by insertion order, then by the record ID:

- Postgres: [`PostgresPolicyChangeApprovalRecordRepository.ts`](https://github.com/pavancharak/parmana-core/blob/df15cf65/packages/storage/src/postgres/PostgresPolicyChangeApprovalRecordRepository.ts)
- Memory: [`MemoryPolicyChangeApprovalRecordRepository.ts`](https://github.com/pavancharak/parmana-core/blob/df15cf65/packages/storage/src/memory/MemoryPolicyChangeApprovalRecordRepository.ts)
- The migration that adds the insertion order: [`20261115120000_policy_approval_insertion_order.sql`](https://github.com/pavancharak/parmana-core/blob/df15cf65/supabase/migrations/20261115120000_policy_approval_insertion_order.sql)
- The log export, which the deploy-time check reads: [`policy-approval-log.ts`](https://github.com/pavancharak/parmana-core/blob/df15cf65/scripts/policy-approval-log.ts)

Existing records are not changed. They have no insertion order, and they rank below a new record with the same time.
