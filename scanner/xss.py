import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

XSS_PAYLOADS = ['<script>alert(1)</script>', '"><script>alert(1)</script>', '<img src=x onerror=alert(1)>']

def scan(url, session):
    results = []
    try:
        r = session.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            action = form.get('action', '')
            form_url = urljoin(url, action) if action else url
            inputs = form.find_all('input')

            for payload in XSS_PAYLOADS[:1]:
                try:
                    data = {}
                    for inp in inputs:
                        name = inp.get('name', '')
                        if name:
                            data[name] = payload

                    res = session.post(form_url, data=data, timeout=5, verify=False)
                    if payload in res.text:
                        results.append({'type': 'XSS Vulnerability', 'severity': 'High', 'detail': f'Form at {form_url} reflects injected script'})
                        break
                except:
                    pass

    except Exception as e:
        results.append({'type': 'Error', 'severity': 'Info', 'detail': f'XSS scan error: {str(e)}'})

    if not results:
        results.append({'type': 'XSS Check', 'severity': 'Info', 'detail': 'No reflected XSS found in forms'})
    return results
