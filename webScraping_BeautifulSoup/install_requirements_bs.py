import subprocess
import sys

required_packages = [
    'requests',
    'beautifulsoup4'
]

for package in required_packages:
    try:
        __import__(package.replace('-', '_'))
    except ImportError:
        print(f"[INFO] Instalando: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])