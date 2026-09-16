# External data and automation

Use for news gathering, automatic topic ideas, summaries, reports, third-party imports, scheduled jobs, or AI actions.

## Feasibility first

Identify the source, access method, authentication, update frequency, rate limits, terms, cost, scheduler, and failure behavior before implementation. Prefer documented APIs, RSS, webhooks, or user-authorized exports. Browser scraping is not a durable default.

Distinguish:

- an on-demand action while the app is open;
- a server-side background job;
- a scheduled task that runs even when the app is closed;
- an AI transformation that needs a model provider and usage budget.

## Product behavior

Show source and last-updated time for imported information. Preserve provenance for generated summaries. Provide retry/error states and avoid silently replacing user-authored data.

Never substitute static examples for a promised live feed or scheduled action. If credentials, billing, or consent are needed, explain the condition before building and request the minimum next user action.
