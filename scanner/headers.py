import requests

def scan(url, session):
    results = []
    try:
        r = session.get(url, timeout=10, verify=False)
        security_headers = {
            'Content-Security-Policy': 'Prevents XSS and data injection',
            'X-Frame-Options': 'Prevents clickjacking',
            'X-Content-Type-Options': 'Prevents MIME sniffing',
            'Strict-Transport-Security': 'Enforces HTTPS',
            'Referrer-Policy': 'Controls referrer info',
            'Permissions-Policy': 'Controls browser features'
        }
        for header, desc in security_headers.items():
            if header not in r.headers:
                results.append({'type': 'Missing Header', 'severity': 'Medium', 'detail': f'{header} missing — {desc}'})
            else:
                results.append({'type': 'Header Present', 'severity': 'Low', 'detail': f'{header}: {r.headers[header]}'})

        server = r.headers.get('Server', '')
        if server:
            results.append({'type': 'Server Info', 'severity': 'Info', 'detail': f'Server header: {server}'})

        powered = r.headers.get('X-Powered-By', '')
        if powered:
            results.append({'type': 'Tech Stack', 'severity': 'Info', 'detail': f'X-Powered-By: {powered}'})

    except Exception as e:
        results.append({'type': 'Error', 'severity': 'High', 'detail': f'Headers scan failed: {str(e)}'})
    return results