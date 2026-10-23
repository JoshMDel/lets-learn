"""Build lesson JSON from the specs: `python build.py [werkkaart numbers...]` (default: all)."""
import glob
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lessonkit import emit

wanted = {int(a) for a in sys.argv[1:]}
found = {}
for path in sorted(glob.glob(os.path.join(HERE, 'specs', '*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name, value in vars(mod).items():
        m = re.fullmatch(r'L(\d+)', name)
        if m and isinstance(value, dict):
            found[int(m.group(1))] = value
for num in sorted(found):
    if not wanted or num in wanted:
        emit(found[num])
