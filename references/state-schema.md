# Durable project state

The state directory is `.personal-workbench/` at the application root. Markdown files preserve human-readable context; `project-state.json` enables deterministic phase checks.

## project-state.json

Required fields:

- `schema_version`: integer, currently `1`.
- `project_name`: string.
- `phase`: one of the phases listed in `SKILL.md`.
- `created_at` and `updated_at`: ISO-8601 UTC timestamps.
- `primary_scenario`: string or `null`.
- `primary_device`: `mobile`, `desktop`, `both`, or `unknown`.
- `data_mode`: `undecided`, `local`, or `cloud-sync`.
- `feature_confirmation`: object with `confirmed` and `confirmed_at`.
- `ui_confirmation`: object with `confirmed`, `choice`, and `confirmed_at`.
- `third_party_dependencies`: array.
- `deployment`: object with `status`, `provider`, and `url`.
- `pwa`: object with `status`.
- `qa`: object with `status`, `last_run_at`, and `unverified`.

Update timestamps and affected status after each meaningful decision. Do not set confirmation booleans based on inference.

## Markdown files

- `requirements.md`: identity, focused scenario, pain points, long-term records, repeated tasks, devices, privacy, visual preferences, open questions.
- `workflow.md`: observed current flow and proposed improved flow.
- `feature-map.md`: priorities, feasibility labels, scope, and exclusions.
- `design-choice.md`: three directions, feedback, final choice, and responsive notes.
- `decisions.md`: append-only dated decisions, reasoning, and affected scope.

When adopting an existing project, separate facts observed in code from claims supplied by the user. If state schema changes later, add a migration rather than silently discarding unknown fields.
