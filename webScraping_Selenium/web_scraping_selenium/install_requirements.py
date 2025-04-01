import subprocess
import sys

# Lista de bibliotecas necessárias para rodar o script principal
required_packages = [
    'selenium',
    'webdriver-manager',
    'requests'
]

for package in required_packages:
    try:
        __import__(package.replace('-', '_'))
    except ImportError:
        print(f"[INFO] Instalando: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
