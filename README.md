# 🛡️ VulnScanner Pro v2.0

![Version](https://img.shields.io/badge/version-2.0-red)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional web vulnerability scanner with a stunning cyberpunk GUI. Built for security researchers, penetration testers, and cybersecurity students.

## ✨ Features

### 🔍 Scanning Modules

| Module | Description |
|--------|-------------|
| **Security Headers** | Checks CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy |
| **Exposed Files** | Detects .git/config, .env, backups, phpinfo, admin panels, and 15+ sensitive files |
| **Directory Enumeration** | Scans 25+ common directories (admin, backup, uploads, .git, wp-content, etc.) |
| **SQL Injection** | Form-based and URL parameter testing with multiple payloads |
| **XSS Detection** | Reflected cross-site scripting tests on input forms |
| **Port Scanner** | Scans 16 common ports with service detection (FTP, SSH, MySQL, RDP, etc.) |

### 🎨 GUI Features

- 🎯 Cyberpunk dark theme with live particle animations
- 📊 Real-time severity statistics (Critical/High/Medium/Low/Info)
- 🧪 One-click preset test targets
- 🎨 Color-coded result cards with severity badges
- 📁 Scan history with timestamps
- 📊 Dashboard with scan analytics
- 📥 One-click report export (.txt)
- 📱 Fully responsive design
- ⚡ Animated loading states

## 📸 Screenshots

![Dashboard](screenshots/demo.png)

*More screenshots in the `/screenshots` folder*

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + Flask |
| Frontend | HTML5 + CSS3 + Vanilla JavaScript |
| Scanning Engine | Requests, BeautifulSoup4, Socket |
| Data Storage | JSON (scan history) |
| Packaging | PyInstaller (standalone .exe) |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/MohidAkbar/VulnScanner.git
cd VulnScanner

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
Open your browser and go to: http://127.0.0.1:5000

Windows EXE
Download the latest VulnScannerPro.exe from Releases and double-click to run.

No Python installation required!

🎯 Usage Guide
Basic Scan
Launch the application

Enter a target URL or click a preset

Click ▶ Scan Now

View results with severity levels

Export report if needed

Tabs Overview
Tab	Function
New Scan	Run vulnerability scans
History	View all past scans with stats
Dashboard	Analytics: total scans, vulnerabilities found, last scan
Help	About, author info, and usage tips
Test Targets
URL	Description
https://testphp.vulnweb.com	Acunetix test site (safe to scan)
https://httpbin.org	HTTP request testing
http://scanme.nmap.org	Nmap test server
https://google.com	Live site (headers check only)


📁 Project Structure

text
VulnScanner/
├── app.py                 # Main Flask server with API routes
├── scanner/
│   ├── __init__.py        # Module initializer
│   ├── headers.py         # Security headers checker
│   ├── files.py           # Exposed files scanner
│   ├── dirs.py            # Directory enumeration
│   ├── sqli.py            # SQL injection tests
│   ├── xss.py             # XSS detection module
│   └── ports.py           # Port scanner
├── templates/
│   └── index.html         # Frontend GUI (cyberpunk theme)
├── requirements.txt       # Python dependencies
├── run.bat                # Windows quick launcher
├── scan_history.json      # Auto-generated scan history
└── README.md              # This file


🔧 Development

Adding New Scanning Modules
Create a new file in /scanner/

Define a scan(url, session) function

Import and add to FullScanner.run_all() in app.py

Building EXE
bash
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" --add-data "scanner;scanner" --name VulnScannerPro app.py

⚠️ Disclaimer
FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY

This tool is designed for:

Security researchers testing their own systems

Penetration testers with written authorization

Students learning about web security

Bug bounty hunters within program scope

Do NOT scan websites without explicit permission. Unauthorized scanning may be illegal and violate computer fraud laws. The author is not responsible for any misuse or damage caused by this tool.

👨‍💻 Author
Mohid Akbar

🎓 BS Cybersecurity — University of Management & Technology, Lahore

📧 GitHub

💼 LinkedIn

🌟 Acknowledgments
Test targets provided by Acunetix and Nmap project

Inspired by OWASP Top 10 vulnerabilities

Built as part of cybersecurity portfolio

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

⭐ If you find this useful, give it a star! ⭐
