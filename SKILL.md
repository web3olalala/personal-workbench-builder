---
name: personal-workbench-builder
description: Plan, prototype, build, deploy, and iteratively improve a personal workbench for a non-technical user. Use when someone wants a personal dashboard, life or work operating system, creator workspace, student hub, client tracker, or an existing workbench changed without losing data.
---

# Personal Workbench Builder

Guide a non-technical user from real-life workflow discovery to a working, persistent, responsive personal workbench. Do not treat this as a one-shot dashboard prompt or a fixed template.

## Start by detecting the mode

Inspect the current directory before asking questions or writing code.

- If `.personal-workbench/project-state.json` exists, read it and the other state files first. Continue from the recorded phase and do not repeat answered questions.
- If an application already exists but state files do not, inspect its stack, features, data model, tests, and deployment configuration. Create state from observed facts, marking uncertain items as unknown.
- If the directory is empty or has no relevant application, start discovery. Do not scaffold an app yet.

Initialize state with `scripts/init_workbench_state.py --project-root <path>` only after identifying the intended project root. Never overwrite non-empty state without explicit user intent.

## Follow the phase gates

Use `.personal-workbench/project-state.json` as the durable phase record. The normal phases are:

1. `discovery` — understand the person and the real workflow.
2. `proposal` — synthesize positioning, workflow, pain points, features, data mode, and visual direction.
3. `feature_confirmed` — entered only after the user accepts the feature proposal.
4. `ui_prototypes` — build three meaningfully different, runnable, clickable directions.
5. `ui_confirmed` — entered only after the user selects or combines a direction.
6. `implementation` — build the real product incrementally.
7. `integration` — add persistence, sync, accounts, or automation that the confirmed scope requires.
8. `release` — complete production deployment and PWA work when long-term access is wanted.
9. `qa` — verify the actual app and fix failures.
10. `operational` — the confirmed release is usable; future requests are incremental changes.

Hard gates:

- Do not write product code during discovery or proposal.
- Do not start UI prototypes until the user confirms the functional proposal.
- Do not build the final application until the user has experienced and confirmed a prototype direction.
- Ask again only for third-party accounts, login/consent, secrets, data permissions, irreversible product choices, or choices only the user can make.
- Once implementation is authorized, handle ordinary technical choices, coding, bug fixes, and tests autonomously.

## Load only the reference needed for the current phase

- Discovery: read [references/interview.md](references/interview.md).
- Workflow synthesis and proposal: read [references/workflow-and-planning.md](references/workflow-and-planning.md).
- Feasibility labels and anti-fake-function rules: read [references/feasibility.md](references/feasibility.md).
- Three clickable UI directions: read [references/design-prototypes.md](references/design-prototypes.md).
- Existing-project changes and implementation: read [references/implementation.md](references/implementation.md).
- Local persistence or schema changes: read [references/storage.md](references/storage.md).
- Accounts, cloud data, or multi-device sync: read [references/sync-and-security.md](references/sync-and-security.md).
- Feeds, APIs, scheduled jobs, or AI automation: read [references/automation.md](references/automation.md).
- PWA or production hosting: read [references/pwa-and-deployment.md](references/pwa-and-deployment.md).
- Verification and completion reporting: read [references/qa.md](references/qa.md).
- State field meanings or migrations: read [references/state-schema.md](references/state-schema.md).

## Interaction rules

- Speak in the user's language and use everyday wording. Translate product and technical decisions instead of asking the user to make them.
- Ask at most two or three closely related questions per round. Adapt to previous answers; never mechanically exhaust a questionnaire.
- When the user does not know what features they need, infer candidates from their workflow, repeated work, lost information, and long-term records.
- Focus the first version on one core scenario. Avoid combining every identity and life area into one dashboard.
- Distinguish data synchronization from public availability: a database syncs devices; deployment provides a stable URL.
- Never represent mock data, a disabled control, a static AI response, or two independent local stores as a finished feature.

## Existing projects and later changes

Treat existing code and user data as durable. Inspect before editing, preserve the current stack when reasonable, and prefer incremental changes. Before a schema change, define a migration and rollback path. A visual redesign must preserve confirmed functions and data unless the user explicitly changes scope.

After each meaningful phase or decision, update the relevant Markdown state file and `project-state.json`. Append to `decisions.md`; do not silently rewrite history.

## Completion

Run the project's real checks plus the phase-specific checklist in [references/qa.md](references/qa.md). Fix failures and rerun. Do not claim completion while builds, core interactions, or persistence fail. Report anything that could not be verified, including real-device sync, third-party permissions, installability, and production credentials.

The bundled starter is optional and only for a truly new project. Copy it with `scripts/copy_starter.py`; that script must refuse non-empty destinations. Never replace an existing app to force use of the starter.
