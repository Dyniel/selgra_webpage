# SELGRA Community Website (Static PoC V2)

This is a static HTML, CSS, and JavaScript Proof of Concept (PoC) for a private community website for the SELGRA student organization. This version features a highly interactive and customizable dashboard.

## Features

*   **Static Site:** A single `index.html` file that can be hosted on any static web hosting service (like GitHub Pages).
*   **Interactive Dashboard:** Built with **GridStack.js**, the dashboard allows users to drag, drop, and resize content windows.
*   **Dual View Modes:**
    *   **Module View:** A customizable layout where all content widgets are visible and can be freely arranged.
    *   **Tab View:** A simplified, clean view where content is organized into clickable tabs.
*   **Layout Persistence:** The user's preferred layout in Module View is automatically saved in the browser's `localStorage` and restored on the next visit.
*   **Simulated Login & Roles:** Uses client-side JavaScript to simulate an admin/member login and shows an admin-only instruction panel.
*   **"Cosmic" Theme:** A beautiful, space-themed design with a dark blue background and glowing accents.

## How It Works

This PoC operates entirely in the browser.

*   **Authentication:** The login logic checks against hardcoded values.
    *   **Admin:** `username: admin`, `password: admin`
    *   **Member:** `username: member`, `password: member`
*   **Session Management:** A "session" is simulated using `sessionStorage`.
*   **Dashboard Views:** JavaScript handles switching between the static Tab View and the interactive Module View. In Module View, GridStack.js manages the widget layout.

## Deployment

Simply upload the `index.html` file to any static hosting provider. No server-side configuration is needed.

## Admin Instructions

### Managing Users

Users are hardcoded in the `<script>` section at the bottom of the `index.html` file. Edit this object to manage users:

```javascript
const users = {
    "admin": { password: "admin", role: "admin" },
    "member": { password: "member", role: "member" }
};
```

### Updating Content & Adding New Widgets

All website content is located within the `<body>` of the `index.html` file, inside the `<div class="grid-stack">` container. Each piece of content is a "widget."

**To add a new widget:**

1.  Copy an existing `<div class="grid-stack-item">...</div>` block.
2.  Paste it inside the `<div class="grid-stack">` container.
3.  Modify the inner `<div class="grid-stack-item-content" data-tab-id="...">`.
    *   **`data-tab-id`:** Give it a unique ID (e.g., `"contact"`). This ID is used for the tab navigation.
    *   **Content:** Change the `<h2>` and other HTML content inside this `div` to your new content.
4.  The new widget will appear on the dashboard. You can then position and resize it in **Module View**, and the layout will be saved automatically. The tab for the new widget will be generated automatically.

**Example of a new widget:**

```html
<!-- Add this inside the .grid-stack container -->
<div class="grid-stack-item" gs-w="6" gs-h="3">
    <div class="grid-stack-item-content" data-tab-id="contact">
        <h2>Contact Us</h2>
        <p>You can reach out to us via email or our social media channels.</p>
    </div>
</div>
```
