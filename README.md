# SELGRA Static Mockup

Static concept website for SELGRA: Student chapter of the European Low Gravity Research Association.

## Project Knowledge Base

- This is a pure HTML, CSS and JavaScript mockup for GitHub Pages.
- There is no backend, no real registration and no real authentication.
- Demo data lives in `data/*.json`; opportunities are real public calls, while the other member/demo datasets are fictional.
- The Member Mode password is `selgra-demo`.
- Member Mode is only a UI demonstration stored in `localStorage`; it must not be used for real personal or member data.

## Files

- `index.html` - page structure and public/member sections.
- `styles.css` - responsive public mode and dark Member Mode styling.
- `app.js` - JSON loading, rendering, filters, modals and Member Mode state.
- `data/feed.json` - public feed cards.
- `data/events.json` - public events.
- `data/professionals.json` - fictional professional directory.
- `data/opportunities.json` - the provided open calls only, with their source links and quoted descriptions.
- `assets/selgra-hero.png` - generated local hero image.

## Run Locally

Use any static server from the project directory:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy

This repository is ready for GitHub Pages from the `main` branch and `/` root directory.
Push to `main`, then use repository settings to set Pages source to `Deploy from a branch` if it is not enabled automatically.
