# Cyber Reference Wiki

Quartz 5 website for the Obsidian notes in [xlaesch-Cookbook](https://github.com/xlaesch/xlaesch-Cookbook), hosted with GitHub Pages at https://wiki.alexsch.dev.

## Update notes

Edit and push notes in the source repository. The site imports its latest `main` branch on every deployment. An hourly schedule picks up note changes; use **Actions → Deploy wiki → Run workflow** for an immediate update. Scheduled GitHub Actions can be delayed and are disabled after 60 days without repository activity.

The `network-pentesting/` folder and other current subject folders are published; legacy remote trees, Obsidian settings, and agent instructions are excluded. The note repository remains the source of truth.

## Local preview

```shell
npm ci
python3 scripts/import-notes.py ~/Documents/Cyber
npx quartz plugin install
npx quartz build -d /tmp/cyber-wiki-content --serve
```

Visit http://localhost:8080. Site configuration lives in `quartz.config.yaml`; the homepage lives in `content/index.md`.

## Domain setup

In Squarespace, open **Domains → alexsch.dev → DNS → DNS Settings → Custom records** and add:

| Type | Host | Value |
| --- | --- | --- |
| CNAME | wiki | xlaesch.github.io |

Keep the existing root domain and `www` records. In this site's GitHub **Settings → Pages**, the custom domain is `wiki.alexsch.dev`. Once DNS validates and GitHub issues the certificate, enable **Enforce HTTPS**.

Quartz is MIT licensed; see `LICENSE.txt`.
