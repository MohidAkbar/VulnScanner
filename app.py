#!/usr/bin/env python3
"""Vulnerability Scanner Pro - Main App"""
from flask import Flask, render_template, request, jsonify, send_file
import requests
import urllib3
import json
import os
from datetime import datetime
urllib3.disable_warnings()

from scanner.headers import scan as scan_headers
from scanner.files import scan as scan_files
from scanner.dirs import scan as scan_dirs
from scanner.sqli import scan as scan_sqli
from scanner.xss import scan as scan_xss
from scanner.ports import scan as scan_ports

app = Flask(__name__)
HISTORY_FILE = 'scan_history.json'

class FullScanner:
    def __init__(self, url):
        self.url = url if url.endswith('/') else url + '/'
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})

    def run_all(self):
        all_results = []
        modules = [
            ('Security Headers', scan_headers),
            ('Exposed Files', scan_files),
            ('Directory Enumeration', scan_dirs),
            ('SQL Injection', scan_sqli),
            ('XSS Detection', scan_xss),
            ('Port Scanner', scan_ports),
        ]
        for name, func in modules:
            all_results.append({'type': f'--- {name} ---', 'severity': 'Info', 'detail': f'Starting {name.lower()}...'})
            all_results.extend(func(self.url, self.session))
        return all_results

def save_scan(url, results):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    high = sum(1 for r in results if r['severity'] == 'High')
    medium = sum(1 for r in results if r['severity'] == 'Medium')
    low = sum(1 for r in results if r['severity'] == 'Low')
    history.append({
        'url': url,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'high': high, 'medium': medium, 'low': low,
        'total': len(results)
    })
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history[-50:], f, indent=2)  # Keep last 50 scans

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.json.get('url', '')
    if not url.startswith('http'):
        url = 'https://' + url
    scanner = FullScanner(url)
    results = scanner.run_all()
    save_scan(url, results)
    return jsonify({'results': results, 'url': url})

@app.route('/history', methods=['GET'])
def history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route('/export', methods=['POST'])
def export():
    data = request.json.get('results', [])
    url = request.json.get('url', 'target')
    filename = f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write(f"VULNSCANNER PRO - SCAN REPORT\n")
        f.write(f"{'='*50}\n")
        f.write(f"Target: {url}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'='*50}\n\n")
        for r in data:
            f.write(f"[{r['severity']}] {r['type']}\n")
            f.write(f"    {r['detail']}\n\n")
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    import webbrowser, threading
    threading.Timer(2.0, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    print("\n[+] VulnScanner Pro running at: http://127.0.0.1:5000\n")
    app.run(debug=False, port=5000)