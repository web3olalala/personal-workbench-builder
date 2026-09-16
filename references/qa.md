# Quality assurance and completion

Build a project-specific checklist from the confirmed feature map. Run checks, fix failures, and rerun affected checks.

## Engineering

- Install dependencies using the repository's chosen package manager.
- Run available typecheck, lint, unit/integration tests, and production build.
- Do not invent script names; inspect `package.json` or project tooling first.

## Interface

- Load the start page and each primary route.
- Check desktop, the target mobile width, keyboard access, focus visibility, empty/error/loading states, and horizontal overflow.
- Exercise primary navigation and the confirmed core workflow.

## Functions and data

- Test create, edit, delete, search/filter, and state changes that exist.
- Refresh after mutation and reopen the app; records must remain.
- Test migration paths when schemas changed.
- For sync, use two accounts and two sessions/devices when possible; verify isolation.

## PWA and production

- Validate manifest fields, icons, service worker, HTTPS, offline shell, installability, and production routing.
- Confirm private network data is not broadly cached.
- Smoke-test the deployed URL.

## Completion report

Report commands run and outcomes, manual paths exercised, production URL if deployed, and items not verified. Do not say “complete” when build, the core workflow, or persistence fails. Third-party behavior, real-device sync, install prompts, and credentials that were not available must be named explicitly as unverified.
