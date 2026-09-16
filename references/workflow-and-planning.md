# Workflow analysis and product proposal

Turn discovery into a decision-ready proposal before writing product code.

## Reconstruct the workflow

- Describe the current sequence, tools, handoffs, repeated entry, missing information, and failure points.
- Separate the user's real behavior from an idealized process.
- Identify the smallest coherent loop the first version should improve.
- Rank problems by frequency, consequence, and user importance.

## Derive information architecture

- Put daily/high-value actions on the home surface.
- Put weekly or supporting work in primary modules.
- Put rare administration in settings or secondary screens.
- A module must correspond to an observed job, record, or decision; avoid decorative dashboard widgets.

## Proposal format

Present a plain-language “My Personal Workbench Plan” containing:

1. One-sentence purpose.
2. Current workflow as a short sequence.
3. Core pain points.
4. Home surface and why each item belongs there.
5. Core modules, with first-version priority.
6. Proposed AI/automation, clearly separated from ordinary features.
7. Device usage.
8. Data mode: local-only or account-backed sync, with a simple reason.
9. Long-term access: local development versus production deployment and PWA.
10. Visual direction: mood, palette, typography feel, density, cards, and motion.
11. Out of scope for the first version.

Use the labels in `feasibility.md` on every non-trivial capability. Write the proposal to `feature-map.md` and update the phase to `proposal`.

## Confirmation gate

Invite additions, removals, and priority changes. Do not create the three prototypes until the user explicitly accepts the functional proposal. Record the acceptance and any scope changes in `decisions.md`, then set `feature_confirmed`.
