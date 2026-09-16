# PWA and production deployment

Use when the user wants daily/long-term access, installation, or a stable URL.

## Keep the concepts separate

- Hosting provides a stable URL and production runtime.
- A cloud database provides shared data across devices.
- PWA features provide installability and a controlled offline app shell.

One does not automatically provide the others.

## PWA baseline

Verify the manifest, app name, theme/background colors, mobile meta tags, 192px and 512px icons, service-worker registration, HTTPS, start URL, display mode, and offline app shell. Cache versioned static assets deliberately.

Do not cache authenticated API responses, tokens, or private cloud records in a broad service-worker rule. An offline shell is not proof that all features work offline.

## Deployment

Choose a provider compatible with the project, server needs, regions, and user preference. Check build/output settings, environment variables, redirects, SPA fallback, custom domain needs, and preview versus production targets.

Deployment mutates an external system. Confirm the intended provider/project/production target when it is not already explicit. Pause only for unavoidable login, account creation, consent, payment, DNS, or secret entry; give one concrete step at a time.

After deployment, test the production URL rather than relying only on local preview. Record provider, project, URL, release date, and verification status in project state.
