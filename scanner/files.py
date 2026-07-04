import requests
from urllib.parse import urljoin

SENSITIVE_FILES = [
    '.git/config', '.env', '.env.backup', 'robots.txt',
    'phpinfo.php', 'info.php', 'backup.sql', 'dump.sql',
    'wp-config.php.bak', 'wp-config.php~', 'adminer.php',
    'phpmyadmin/index.php', '.DS_Store', 'web.config',
    'server-status', 'crossdomain.xml', 'sitemap.xml'
]

def scan(url, session):
    results = []
    for f in SENSITIVE_FILES:
        try:
            full_url = urljoin(url, f)
            r = session.get(full_url, timeout=5, verify=False, allow_redirects=True)
            if r.status_code == 200 and len(r.content) > 10:
                results.append({'type': 'Exposed File', 'severity': 'High', 'detail': f'{f} is publicly accessible ({len(r.content)} bytes)'})
        except:
            pass

    if not results:
        results.append({'type': 'Files OK', 'severity': 'Info', 'detail': 'No sensitive files found exposed'})
    return results