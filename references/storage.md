# Local persistence and data migrations

## Choose local storage deliberately

- Use IndexedDB for structured records, collections, larger data, blobs, indexes, or offline-first behavior.
- Use localStorage for small preferences or simple flags, not as a default application database.
- Never place the user's private records in source files, committed JSON fixtures, or static HTML.

## Persistence contract

For every record type, define an identifier, schema version, timestamps, validation, and deletion behavior. The app must preserve create/edit/delete results across refresh and browser restart.

## Migrations

Before changing a stored schema:

1. Document old and new versions.
2. Write an idempotent migration or compatible reader.
3. Back up/export data when the change is risky.
4. Test with representative old records and empty data.
5. Provide a rollback or recovery path.

Do not silently clear storage to fix development errors. Keep demo/seed records distinct from real user records.

## Portability

For local-only apps intended for long-term use, consider export/import and explain that browser storage is tied to a device and browser profile. Local persistence does not provide multi-device synchronization.
