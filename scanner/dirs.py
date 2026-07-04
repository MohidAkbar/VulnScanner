import requests
from urllib.parse import urljoin

COMMON_DIRS = [
    'admin', 'backup', 'uploads', 'images', 'files', 'downloads',
    '.git', 'logs', 'tmp', 'temp', 'wp-content', 'wp-admin',
    'panel', 'dashboard', 'config', 'api', 'test', 'dev',
    'old', 'new', 'db', 'sql', 'phpmyadmin', 'mysql'
]

def scan(url, session):
    results = []
    found = 0
    for d in COMMON_DIRS:
        try:
            full_url = urljoin(url, d) + '/'
            r = session.get(full_url, timeout=5, verify=False)
            if r.status_code in [200, 301, 302, 403]:
                found += 1
                status = 'Accessible' if r.status_code == 200 else 'Redirect/Forbidden'
                sev = 'High' if r.status_code == 200 else 'Medium'
                results.append({'type': 'Directory Found', 'severity': sev, 'detail': f'/{d}/ — {status} ({r.status_code})'})
        except:
            pass

    results.append({'type': 'Directory Scan', 'severity': 'Info', 'detail': f'Found {found} accessible directories out of {len(COMMON_DIRS)} tested'})
    return results