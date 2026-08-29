# Going live on Truehost (as a subdomain of j92labs.co.za)

This deploys as **letslearn.j92labs.co.za** — a subdomain of your existing, already-live
site. Since `j92labs.co.za` already points at Truehost with SSL active, this is faster
than the Hair By Mimmie setup: no new domain purchase, no nameserver changes, no DNS
propagation wait. cPanel's **Subdomains** tool creates the folder and wiring in one step.

This is a **static build** of a React app — everything it needs is already baked into
the files below (including the Supabase connection). There's no PHP, no database setup,
no server config beyond the one `.htaccess` file that's already included.

## Step 1 — Create the subdomain in cPanel

1. Log into **cPanel** (via Truehost Client Area → your hosting service → Login to cPanel).
2. Find **Domains → Subdomains** (or just **Subdomains** on older cPanel themes).
3. Fill in:
   - **Subdomain**: `letslearn`
   - **Domain**: `j92labs.co.za` (should already be selected/only option)
   - **Document Root**: cPanel will suggest `public_html/letslearn` — leave that as-is.
4. Click **Create**. cPanel now serves `letslearn.j92labs.co.za` from that new folder,
   completely separate from your main site in `public_html` root and from
   `public_html/hairbymimmie` if that's on the same account.

## Step 2 — Upload the built app into that folder

Everything you need is already built and zipped: **`lets-learn-dist.zip`** (in this
project folder). It contains the compiled app — `index.html`, `assets/`, `icons/`,
`.htaccess`, the PWA manifest and service worker — ready to serve as-is.

**Option A — cPanel File Manager (easiest, no extra software)**
1. Open **File Manager**, navigate into `public_html/letslearn` (the folder from Step 1)
   — **not** `public_html` itself.
2. **Upload** `lets-learn-dist.zip`, then right-click it in File Manager → **Extract**.
3. Confirm `index.html`, `assets/`, `.htaccess`, etc. end up directly inside
   `public_html/letslearn/` — not nested one level deeper. If it extracted into a
   subfolder, select everything inside it, cut, paste up one level, then delete the
   now-empty subfolder and the zip file.
4. **Important**: `.htaccess` is a hidden file (starts with a dot) — File Manager may
   hide it from view by default. Click **Settings** (top right of File Manager) →
   check **Show Hidden Files (dotfiles)** to confirm it actually extracted. Without it,
   every in-app page except the homepage will 404 on a direct visit or refresh.

**Option B — FTP/SFTP**
1. In cPanel, go to **FTP Accounts** — create a dedicated FTP user scoped to
   `public_html/letslearn`, or use your main account over SFTP.
2. Connect with **FileZilla** (enable "Show hidden files" in FileZilla's Server menu so
   `.htaccess` transfers too), navigate to `public_html/letslearn` on the server side,
   and drag in the *contents* of the extracted `dist/` folder (not the folder itself).

## Step 3 — Enable HTTPS for the subdomain

1. In cPanel, find **SSL/TLS Status** or **Let's Encrypt SSL**.
2. Subdomains of an already-secured domain are usually picked up by AutoSSL within a
   few minutes — if `letslearn.j92labs.co.za` isn't listed yet, trigger **Run AutoSSL**
   manually, or issue a certificate for it specifically.
3. Once active, enable **Force HTTPS Redirect** if cPanel offers it (the included
   `.htaccess` also force-redirects to HTTPS on its own either way).

## Step 4 — Test everything

Visit `https://letslearn.j92labs.co.za` fresh (hard-refresh or incognito) and check:

- [ ] The device-chooser screen loads ("Who's using this?")
- [ ] Refreshing the page on an inner route (e.g. after logging in, on `/parent` or
      `/home`) does **not** 404 — confirms `.htaccess` made it up correctly
- [ ] Register a parent account, log in as a child, read a passage, take a quiz —
      the full loop talks to Supabase correctly (open browser dev tools → Network tab
      if anything looks stuck, and check for failed requests to `*.supabase.co`)
- [ ] `https://letslearn.j92labs.co.za/manifest.webmanifest` loads and shows JSON
- [ ] Your existing `j92labs.co.za` site is completely unaffected

## Step 5 — Install it as a PWA (works today, no APK needed)

On an Android phone/tablet: open `https://letslearn.j92labs.co.za` in Chrome → menu
(⋮) → **Add to Home screen**. This gives a real home-screen icon, full-screen app
experience, and offline support for pages already visited — often all you actually
need for your kids' own devices, no APK required.

## Step 6 — Turn it into an installable APK (optional, via PWABuilder)

Once the site is live and confirmed working (Step 4), you can generate a real,
installable `.apk` file:

1. Go to **https://www.pwabuilder.com**.
2. Paste in `https://letslearn.j92labs.co.za` and click **Start**.
3. PWABuilder scores the manifest/service worker (should come back green/mostly green
   given what's already set up) — click **Package for stores**.
4. Choose **Android**, keep the defaults (package ID will default to something like
   `co.za.j92labs.letslearn` — fine as-is, or customize it), and click **Generate**.
5. Download the resulting `.apk` (or `.aab`) — this is a signed package you can send
   directly to your kids' Android devices (they'll need to allow "Install unknown apps"
   for whichever app you send it through, since it's outside the Play Store).

**Keep the keystore PWABuilder generates** (it may offer a download) — you'll need the
same signing key if you ever rebuild/update the APK later; a different key means
Android treats it as a different app and kids would need to uninstall the old one first.
