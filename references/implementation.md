# Implementation and incremental change

## New application

Choose a stack that fits the confirmed scope and available environment. React + TypeScript + Vite is a reasonable default for a client-heavy workbench, but do not force it when an existing platform or a simpler implementation is better.

Translate the selected prototype into maintainable components and real domain data. Implement the confirmed core loop first, then secondary modules. Make desktop and mobile usable, prioritizing the user's main device.

## Existing application

Before editing, inspect the actual entry points, package scripts, data model, environment variables, deployment config, current tests, and working-tree state. Do not assume archived files, old demos, or generated builds are current. Preserve the stack and patterns when reasonable.

For a feature addition:

1. Read current state and the requested outcome.
2. Identify affected UI, data, permissions, tests, and migrations.
3. Implement incrementally.
4. Protect existing records and compatible behavior.
5. Update state and run relevant QA.

For a visual redesign, keep functions, routes, data schema, and user records unless the user explicitly changes them.

## User-dependent steps

When an external setup is required, ask for only the next necessary action. Say exactly where to go, what to click, what value to create or copy, and how the user can confirm completion. Continue the technical work after that step; do not hand the entire integration back as a tutorial.
