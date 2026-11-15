# Approval signals and the approval verifier

A policy can require a signed human approval for an action. The caller sets the signal to `true`, and attaches a `SignedApproval`.

The approval verifier is [`ApprovalVerifier.ts`](https://github.com/pavancharak/parmana-core/blob/509a47e5/packages/approval/src/ApprovalVerifier.ts). It runs ten checks in a fixed order and reports each one:

1. the payload version is supported;
2. the issuer is known;
3. the signature verifies with the issuer's key;
4. the approval has not expired;
5. the issuer is not revoked;
6. the approval's capability is the action being decided;
7. the issuer is granted the capability;
8. the approval's resource is the request's resource;
9. the approval's scope covers the requested value;
10. the nonce has not been used before.

The request is valid only when every check passes. The nonce is used only after the other nine pass, so a refused request does not use up an approval.

The gateway runs the same checks again at release, but does not use the nonce a second time.
