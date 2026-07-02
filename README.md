# Pamp

Pamp is a local CyberSec/OSINT console tool for analyzing IP addresses, domains,
application routes, and public mentions.

The console and HTML reports default to English and can switch between English
and Russian. UI strings live in `pamp/locales/en.json` and `pamp/locales/ru.json`.

Each supported analysis flow writes the current report to `output/report.html`.
Diagnostic detail is written to `output/debug.log`.

## Scope

- The tool does not use paid APIs.
- The tool does not require or read `.env` files.
- Sensitive values are masked before they are stored in artifacts or reports.

## Stack

- Python 3.11+
- rich
- Jinja2
- networkx
- pyvis
- requests
- playwright
- beautifulsoup4
- cryptography

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```powershell
python -m pamp.main
```

You can also run:

```powershell
python pamp\main.py
```

## Menu

1. IP Analysis
2. Domain Analysis
3. Mentions Search
4. Switch Language
5. Exit

## Outputs

- Current report: `output/report.html`
- Current debug log: `output/debug.log`
- Active runtime state: `pamp/data/active_case.json`

Starting a new domain analysis resets runtime state, removes the previous
`output/report.html`, truncates `output/debug.log`, and automatically writes a
fresh report for the current target.

## Domain Analysis

The domain analyzer collects:

- DNS records: A, AAAA, MX, NS, TXT, SOA, CNAME, CAA
- Email auth hints: SPF, DMARC, fixed-selector DKIM hints
- Reverse DNS for linked IP addresses
- RDAP: registrar, created, updated, expires, nameservers, status, registrant org
  when available
- Passive IP ASN/BGP context from RDAP
- Certificate Transparency names from `crt.sh`
- TLS certificate: subject, issuer, validity, SAN domains, serial, SHA256
  fingerprint, TLS version
- HTTP surface: status, final URL, redirect chain, server, x-powered-by, content
  type, content length, security headers
- HTML: title, meta tags, canonical, favicon, forms, inputs, links, scripts, CSS,
  images, comments
- DevTools capture through Playwright Chromium when installed
- Traffic Chain: browser request sequence, critical path, API, third-party,
  failed, slow and WebSocket traffic
- JavaScript, OAuth, Cloud Bucket and Favicon intelligence
- Discovery and SQLi analysis inside the same domain workflow
- Tracker and technology hints
- Emails, phones, Telegram links, social links
- Fixed sensitive public file checks
- Public resources such as manifests, OpenAPI/Swagger hints, source maps, scripts,
  stylesheets, favicons, and WebSocket URLs
- Historical intelligence: Wayback snapshots, historical URLs, certificate history,
  historical subdomains, and first/last artifact dates where keyless sources return
  data
- Reputation intelligence: keyless public feed checks for the domain, resolved IPs,
  DevTools URLs, external domains, and endpoint URLs
- Security findings, security score, and attack-surface summary
- Decoded and classified artifacts

The HTML report includes client-side search, section filtering, collapsible
panels, a sidebar, copy/export controls, clickable values, RU/ENG switching, and
a vertical Traffic Chain timeline. Historical and reputation source failures are
captured in `output/debug.log`; the HTML report still renders when a source is
unavailable. Full diagnostic data is kept in `output/debug.log`.

## Data Decoder

The decoder classifies strings without cracking or decrypting secrets. It detects
JWT, Base64, Base64URL, hex, UUID, MD5/SHA1/SHA256-like hashes, Cloudflare cookie
names, analytics IDs, Telegram links, email-like strings, API key-like strings,
and bearer token-like strings.

JWT handling decodes only header and payload. Signatures are not inspected.
Sensitive values are shown as masked previews.

The sensitive file checker uses only a short fixed path list and does not brute
force. When a path is found, it stores URL, status, size, content type, and a
preview up to 300 characters.

## Public Sources

The MVP uses keyless public sources where available:

- `ip-api.com` for basic IP geolocation and hosting/proxy flags where returned
- `rdap.org` for IP, ASN/BGP, and domain RDAP
- `crt.sh` for Certificate Transparency names
- Internet Archive Wayback CDX API for historical snapshots and URL samples
- abuse.ch URLHaus and ThreatFox community APIs where publicly reachable
- OpenPhish and PhishTank public feeds where publicly reachable
- AlienVault OTX public indicator endpoints where publicly reachable
- reverse DNS through the local resolver
- Tor bulk exit list from `check.torproject.org`
- Cloudflare DNS over HTTPS for domain records
- direct HTTPS/TLS and HTTP responses for domain checks
- Playwright Chromium for browser-visible page data when available
