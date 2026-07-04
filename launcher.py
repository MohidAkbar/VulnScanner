import subprocess
import webbrowser
import time
import sys
import os

# Get the path to the EXE
exe_path = os.path.join(os.path.dirname(__file__), 'dist', 'VulnScanner.exe')

# Launch the EXE
subprocess.Popen(exe_path, creationflags=subprocess.CREATE_NO_WINDOW)

# Wait for server to start
time.sleep(3)

# Open browser
webbrowser.open('http://127.0.0.1:5000')