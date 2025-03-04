import sys
from pathlib import Path

base_path = Path(__file__).resolve().parent if '__file__' in globals() else Path.cwd()
sys.path.append(base_path)