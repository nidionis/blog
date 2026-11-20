#!/usr/bin/env python3
"""Compatibility wrapper: calculations live in tools/calc.py.

Usage (unchanged):
    python3 model/levers.py          # write SVGs and print baseline
    python3 model/levers.py --check  # verify baseline numbers
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Delegate to the unified tool.
sys.argv = [str(ROOT / "tools" / "calc.py")] + sys.argv[1:]
runpy.run_path(str(ROOT / "tools" / "calc.py"), run_name="__main__")
