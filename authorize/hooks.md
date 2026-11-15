# Hooks

A hook observes the runtime at fixed points. The interface is [`RuntimeHook.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/hooks/RuntimeHook.ts), and the runner is [`RuntimeHookRunner.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/hooks/RuntimeHookRunner.ts).

The interface says hooks "must never modify deterministic Runtime behavior". The code does not enforce this.

Two hooks are registered in production, when their dependencies are configured ([`application.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/application.ts)):

- [`killSwitchReleaseHook`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/api/src/killSwitch/killSwitchReleaseHook.ts) throws before a release while the kill switch is on. It refuses the release, so it does change an outcome.
- [`DecisionAlertHook`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/runtime/src/alerts/DecisionAlertHook.ts) sends one alert per decision. It does not wait for delivery, and it swallows failures.

The runner does not catch errors. A hook that throws stops the request.
