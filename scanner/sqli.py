import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

SQLI_PAYLOADS = ["'", '"', "1' OR '1'='1", "1 OR 1=1", "' OR 1=1 --", '" OR 1=1 --']

def scan(url, session):
    results = []
    try:
        r = session.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')

        for form in forms:
            action = form.get('action', '')
            method = form.get('method', 'get').lower()
            inputs = form.find_all('input')
            form_url = urljoin(url, action) if action else url

            for payload in SQLI_PAYLOADS[:2]:
                try:
                    data = {}
                    for inp in inputs:
                        name = inp.get('name', '')
                        if name:
                            data[name] = payload

                    if method == 'post':
                        res = session.post(form_url, data=data, timeout=5, verify=False)
                    else:
                        res = session.get(form_url, params=data, timeout=5, verify=False)

                    if 'sql' in res.text.lower() or 'error' in res.text.lower() or 'mysql' in res.text.lower():
                        results.append({'type': 'Possible SQLi', 'severity': 'High', 'detail': f'Form at {form_url} might be injectable (payload: {payload})'})
                        break
                except:
                    pass

        # URL parameter test
        parsed = urlparse(url)
        if parsed.query:
            for param in parse_qs(parsed.query):
                test_url = url.replace(f'{param}=', f'{param}=')
                try:
                    res = session.get(test_url + "'", timeout=5, verify=False)
                    if 'sql' in res.text.lower() or 'error' in res.text.lower():
                        results.append({'type': 'Possible SQLi (URL)', 'severity': 'High', 'detail': f'Parameter "{param}" might be injectable'})
                except:
                    pass

    except Exception as e:
        results.append({'type': 'Error', 'severity': 'Info', 'detail': f'SQLi scan error: {str(e)}'})

    if not results:
        results.append({'type': 'SQLi Check', 'severity': 'Info', 'detail': 'No obvious SQL injection points found'})
    return results