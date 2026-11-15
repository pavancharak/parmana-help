# Authorize is a stage of its own (D22)

Authorize is the decision: it is made and recorded before anything is signed. Execute is the release: the signed authorization is checked again and the action is run.

The signed execution authorization is the handoff between the two. The code separates them: `RuntimeEngine.decide` makes the decision, and `execute` signs only after the approve gate passes.

The decision is recorded in [D22](https://github.com/pavancharak/parmana-core/blob/4982964e/docs/ASSURANCE_DECISIONS.md), in the `parmana-core` assurance decisions log.
