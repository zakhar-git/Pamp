# Pamp

> **Pamp** is an Attack Surface Intelligence Platform designed for security researchers and penetration testers. It combines infrastructure reconnaissance, application mapping, JavaScript intelligence, and interactive offline reporting into a single workflow.

---

## Features

- IP Intelligence
- Domain Intelligence
- DNS / RDAP / TLS Analysis
- HTTP Security Analysis
- Application Blueprint
- Application Route Intelligence
- JavaScript Intelligence
- Technology Fingerprinting
- Nmap Integration
- Public Mentions Search
- Interactive Offline HTML Reports
- English / Russian Localization

---

## Technology Stack

- Python 3.11+
- Rich
- Requests
- Playwright
- BeautifulSoup4
- Jinja2
- NetworkX
- PyVis
- Cryptography

---

## Installation

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python -m playwright install chromium
```

---

## Usage

Run Pamp:

```bash
python -m pamp.main
```

or

```bash
python pamp/main.py
```

---

## Available Modules

### IP Intelligence

Analyze an IP address and collect:

- Geolocation
- ASN Information
- Reverse DNS
- Hosting Information
- Infrastructure Details

---

### Domain Intelligence

Comprehensive domain reconnaissance including:

- DNS Records
- RDAP / WHOIS
- Certificate Transparency
- TLS Certificate Analysis
- HTTP Fingerprinting
- Security Headers
- HTML Analysis
- Technology Detection
- Tracker Detection
- Public Resources
- Historical Intelligence
- Reputation Intelligence

---

### Application Intelligence

Automatically discovers:

- Application Blueprint
- Route Structure
- JavaScript Assets
- API Endpoints
- OAuth Endpoints
- WebSocket Connections
- Cloud Storage References

---

### Reports

Pamp generates a fully interactive offline HTML report featuring:

- Search
- Filtering
- Sidebar Navigation
- Timeline
- Interactive Graphs
- Attack Surface Summary
- English / Russian Localization

---

## Public Data Sources

Pamp relies only on publicly available sources.

Examples include:

- RDAP
- crt.sh
- Cloudflare DNS
- Internet Archive
- AlienVault OTX
- OpenPhish
- PhishTank
- URLHaus
- ThreatFox

No paid APIs are required.

---

## Security

Pamp:

- does not require API keys
- does not require `.env`
- masks sensitive values in reports
- does not brute-force endpoints
- does not attempt to crack or decrypt secrets

---

## Disclaimer

Pamp is intended for authorized security testing, research, and educational purposes only.

Use this software only against systems you own or have explicit permission to assess.
