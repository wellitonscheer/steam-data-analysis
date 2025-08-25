# Ensure the project parent directory is on sys.path so tests can `import steam_data.*`
import sys
from pathlib import Path

# This file lives in steam_data/tests/conftest.py
# We need to add the parent of the package directory (i.e., the repo root) to sys.path
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
