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


📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

⭐ If you find this useful, give it a star! ⭐
