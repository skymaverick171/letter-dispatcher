# How to properly uninstall Letter Dispatcher (and why removing the icon isn't always enough)

When you "install" Letter Dispatcher, the browser doesn't just place a shortcut on your desktop — it registers the app as a separate application (on Android this is called a WebAPK; Windows and Mac use a similar mechanism). If you only remove the icon from the home screen or desktop, the system may still consider the app installed — so trying to install it again shows a message like "App already installed," and the install button stops working.

To install it fresh, you need to remove the app itself, not just its icon. Here's how, per system.

## Android (Chrome)

1. Open **Phone Settings → Apps** (or "Apps & notifications").
2. Find **Letter Dispatcher** in the list.
3. Tap **Uninstall**.

A quicker way to find it without digging through settings: type `chrome://apps` in Chrome's address bar — it lists every installed web app; long-press it there and choose **Remove**.

Once that's done, open the site again in Chrome — the install button will offer to install it fresh.

## Windows (Chrome or Edge)

1. Type `chrome://apps` in the address bar (`edge://apps` for Edge).
2. Find **Letter Dispatcher** → right-click → **Remove/Uninstall**.

Or through Windows itself: **Settings → Apps → Installed apps** → find Letter Dispatcher → **Uninstall**.

## macOS (Safari)

If it was added via **File → Add to Dock**:

1. Find the Letter Dispatcher icon in the Dock (or in the **Applications** folder).
2. Drag it to the Trash — just like a regular app.

If it was installed through Chrome/Edge on Mac instead, use the same `chrome://apps` method as under Windows above.

## iPhone / iPad

On iOS, removing an "Add to Home Screen" shortcut is complete and clean — there's no separate step needed:

1. Press and hold the icon on the Home Screen.
2. Choose **Remove App** → **Delete App**.

You can add the shortcut back right away via Safari (Share → "Add to Home Screen").

## If nothing else works

Sometimes the browser still "remembers" the install even after removing it via `chrome://apps`. In that case, a full site data reset fixes it:

1. Open [https://skymaverick171.github.io/letter-dispatcher/](https://skymaverick171.github.io/letter-dispatcher/) in Chrome.
2. Click the lock (or ⓘ) icon to the left of the address → **Site settings**.
3. Choose **Reset permissions and clear data**.

Or go to `chrome://settings/content/all`, find `skymaverick171.github.io` in the list, and delete it. This fully resets the install status, and the install button works like it's the first time again.

**Important:** clearing site data also erases any contacts/letters saved locally in that browser (they're stored right there, with no cloud backup) — if you haven't backed anything up yet, use **"Copy for Google Sheets"** or **"Download CSV"** on the Contacts tab first so you don't lose data.
