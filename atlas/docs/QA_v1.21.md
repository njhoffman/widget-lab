# Master v1.21 — QA evidence

**JavaScript syntax:** scripts compile with Node.js `new Function`.

**Asset import algorithm:** Node.js isolated-function test with 172 real Deep Time image files and original artwork manifest: 172 matched, 172 SHA-256 verified, tampered image rejected, missing image flagged as incomplete, path traversal rejected, folder names with spaces supported. Data block untouched.

**Browser limitation:** Playwright Chromium returned `ERR_BLOCKED_BY_ADMINISTRATOR` navigating to a local test origin; end-to-end browser folder import, new tab, and IndexedDB persistence could not be verified here. Launcher v1.14 should receive Windows browser smoke testing before being considered fully deployed.

**Version history:** prior releases preserved. Shared Taxa original hashes and all six atlas HTML files unchanged compared to v1.20.
