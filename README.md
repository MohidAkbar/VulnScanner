# 🛡️ VulnScanner Pro v2.0

![Version](https://img.shields.io/badge/version-2.0-red)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A professional web vulnerability scanner with a stunning cyberpunk GUI. Built for security researchers, penetration testers, and cybersecurity students.

## ✨ Features

### 🔍 6 Scanning Modules

- **Security Headers** — CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy
- **Exposed Files** — .git/config, .env, backups, phpinfo, admin panels, 15+ sensitive files
- **Directory Enumeration** — 25+ common directories (admin, backup, .git, wp-content, etc.)
- **SQL Injection** — Form-based and URL parameter testing with multiple payloads
- **XSS Detection** — Reflected cross-site scripting tests on input forms
- **Port Scanner** — 16 ports with service detection (FTP, SSH, MySQL, RDP, etc.)

### 🎨 GUI Features

- 🎯 Cyberpunk dark theme with live particle animations
- 📊 Real-time severity stats (Critical/High/Medium/Low/Info)
- 🧪 One-click preset test targets
- 📁 Scan history with timestamps
- 📊 Dashboard with scan analytics
- 📥 One-click report export (.txt)
- 📱 Fully responsive design

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3 + Flask |
| Frontend | HTML5 + CSS3 + Vanilla JavaScript |
| Scanning Engine | Requests, BeautifulSoup4, Socket |
| Data Storage | JSON (scan history) |
| Packaging | PyInstaller (.exe) |

## 📦 Installation


git clone https://github.com/MohidAkbar/VulnScanner.git
cd VulnScanner
pip install -r requirements.txt
python app.py
Open your browser at: http://127.0.0.1:5000

Windows EXE
Download VulnScannerPro.exe from Releases and double-click. No Python required!

🎯 Usage
Launch the application

Enter a target URL or click a preset

Click ▶ Scan Now

View results with severity levels

Click 📥 Export Report to download results

Test Targets
URL	Description
https://testphp.vulnweb.com	Acunetix test site (safe to scan)
http://scanme.nmap.org	Nmap port scan test
https://httpbin.org	HTTP request testing

```
📁 Project Structure
text
VulnScanner/
├── app.py                 # Main Flask server
├── scanner/
│   ├── headers.py         # Security headers checker
│   ├── files.py           # Exposed files scanner
│   ├── dirs.py            # Directory enumeration
│   ├── sqli.py            # SQL injection tests
│   ├── xss.py             # XSS detection
│   └── ports.py           # Port scanner
├── templates/
│   └── index.html         # Cyberpunk GUI
├── requirements.txt       # Python dependencies
└── README.md
```

⚠️ Disclaimer
FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY. Only scan websites you own or have explicit permission to test. The author is not responsible for misuse.

👨‍💻 Author
Mohid Akbar

🎓 BS Cybersecurity — UMT Lahore

💼 LinkedIn

📧 GitHub

📄 License
MIT License

⭐ Star this repo if you find it useful!

text
