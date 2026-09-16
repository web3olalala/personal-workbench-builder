# Accounts, cloud data, and multi-device sync

Use when the user needs the same records on phone and computer or when multiple users require private accounts.

## Architecture

Supabase is a useful default when it fits, not a requirement. The minimum credible sync design includes:

- sign-up, sign-in, sign-out, and session recovery;
- records bound to the authenticated user;
- server-enforced row-level access rules;
- storage policies for uploaded files;
- conflict/refetch behavior across devices;
- loading, offline, expired-session, and error states.

With Supabase, enable RLS on user-owned tables and write policies using the authenticated user ID. Test that a second account cannot read or modify the first account's records.

## Secrets

Classify configuration before use:

- Client-safe public configuration may be bundled only when the provider is designed for it and server-side policies enforce access.
- Service-role keys, admin tokens, database passwords, signing secrets, and privileged credentials belong only in protected server or deployment environments.

Never commit real credentials, print them in logs, or paste them into client code. Provide `.env.example` with names only.

## Verification

Test with at least two accounts and, when possible, two browser profiles or real devices:

- computer create → phone sees it;
- phone edit/delete → computer updates;
- account A cannot access account B;
- signed-out users cannot access private data.

If real devices or accounts are unavailable, label sync as not yet fully verified.
