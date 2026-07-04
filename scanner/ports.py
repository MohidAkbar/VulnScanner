import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080, 8443]

def scan(url, session):
    results = []
    hostname = url.split('/')[2].split(':')[0] if '://' in url else url.split('/')[0]

    try:
        ip = socket.gethostbyname(hostname)
        results.append({'type': 'Port Scan', 'severity': 'Info', 'detail': f'Scanning {hostname} ({ip})...'})

        open_ports = []
        for port in COMMON_PORTS:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    service = {21: 'FTP', 22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL', 5432: 'PostgreSQL', 3389: 'RDP', 8080: 'HTTP-Alt'}.get(port, 'Unknown')
                    results.append({'type': 'Open Port', 'severity': 'Medium', 'detail': f'Port {port} ({service}) is open'})
                sock.close()
            except:
                pass

        if not open_ports:
            results.append({'type': 'Ports OK', 'severity': 'Info', 'detail': 'No common ports found open'})
    except Exception as e:
        results.append({'type': 'Error', 'severity': 'Info', 'detail': f'Port scan failed: {str(e)}'})

    return results