# Feasibility and honest capabilities

Evaluate non-trivial features before UI prototyping or implementation.

## Labels

- `✅ Direct`: implementable inside the chosen application with no new external dependency.
- `⚠️ Service`: requires an external database, API, feed, scheduler, email provider, or hosting service.
- `⚠️ User action`: requires account creation, consent, login, secret, payment, or a decision only the user can make.
- `❌ Unreliable`: no stable/legal data access or the available environment cannot support it reliably.

For every warning, state the condition and the user-visible limitation in everyday language. Offer a smaller honest alternative when useful.

## Questions to answer

- Where does the data originate and who owns it?
- Is there a documented API, RSS feed, export, or webhook?
- Is authentication required, and can it be done without exposing a secret in the client?
- Does “automatic” require a server or scheduled runner when the browser is closed?
- What happens on rate limits, offline use, revoked access, or provider failure?
- Can the feature be tested with real data in the present environment?

## Anti-fake-function rule

Never mark a capability complete when it is only:

- a button without a working action;
- sample data presented as the user's live data;
- a hard-coded AI answer;
- local storage on two devices described as synchronization;
- a browser-only timer described as a daily background job;
- a prototype interaction described as production behavior.

Mock content is allowed in the three design prototypes only when visibly labeled as example content. Prototype acceptance confirms design, not integration readiness.
