import json
from datetime import datetime
from .config import D
F = D / "history.json"
class History:
    def __init__(s): s.m = json.loads(F.read_text()) if F.exists() else []
    def save(s): F.write_text(json.dumps(s.m[-100:], indent=2))
    def add(s, r, c): s.m.append({"role":r,"content":c,"time":datetime.now().isoformat()})
    def get_recent(s, n=10): return s.m[-n:]
    def clear(s): s.m = []; s.save()
