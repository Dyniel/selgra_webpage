# SELGRA Community Website (Static PoC)

This is a static HTML, CSS, and JavaScript Proof of Concept (PoC) for a private community website for the SELGRA student organization. It demonstrates the website's design and simulates a login system without requiring a backend server.

## Features

*   **Static Site:** A single `index.html` file that can be hosted on any static web hosting service (like GitHub Pages).
*   **Simulated Login:** Uses client-side JavaScript to simulate a login experience. User credentials are hardcoded for demonstration purposes.
*   **User Roles:** Differentiates between `admin` and `member` roles, with a special instruction panel visible only to administrators.
*   **"Cosmic" Theme:** A beautiful, space-themed design with a dark blue background and glowing accents.
*   **Embedded Content:** Includes placeholders for a dynamic social media feed (Juicer.io) and a Google Calendar.

## How It Works

This PoC operates entirely in the browser.

*   **Authentication:** The login logic is handled by a JavaScript script within the `index.html` file. It checks the entered username and password against hardcoded values.
    *   **Admin:** `username: admin`, `password: admin`
    *   **Member:** `username: member`, `password: member`
*   **Session Management:** A "session" is simulated by storing the logged-in user's role in the browser's `sessionStorage`. This state is lost when the browser tab is closed.

## Deployment

Simply upload the `index.html` file to any static hosting provider. No server-side configuration is needed.

## Admin Instructions

### Managing Users

Since this is a static PoC, users are not stored in a database or a file. The available users are hardcoded in the `<script>` section at the bottom of the `index.html` file. To add, remove, or change users, you must edit this JavaScript object directly:

```javascript
// Located inside the <script> tag in index.html
const users = {
    "admin": { password: "admin", role: "admin" },
    "member": { password: "member", role: "member" }
    // Add new users here, e.g.:
    // "new_user": { password: "new_password", role: "member" }
};
```

### Updating Content

All website content is located within the `index.html` file.

1.  **Text and Layout:** To change any text or structural elements, edit the HTML in the `<body>` of the file.

2.  **Social Media Feed:**
    *   The feed is an embed from [Juicer.io](https://www.juicer.io). To change it, replace the `<script>` and `<ul>` tags in the `social-feed` section with the embed code from your preferred social media aggregator.

3.  **Google Calendar:**
    *   The calendar is an embedded `<iframe>` from Google Calendar. To use your own calendar, go to your Google Calendar's settings, find the "Embed code," and replace the existing `<iframe>` in the `google-calendar` section with your own.
