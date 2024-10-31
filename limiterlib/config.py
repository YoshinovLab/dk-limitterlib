from pathlib import Path
import os
LIMIT = 6
os.umask(0)
LOG_DIR = Path("log")
LOG_DIR.mkdir(parents=True, exist_ok=True, mode=0o777)
