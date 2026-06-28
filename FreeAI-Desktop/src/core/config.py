import json
from pathlib import Path
D = Path.home() / ".freeai"
D.mkdir(exist_ok=True)
F = D / "config.json"
C = {"theme":"dark","active_model":"auto","max_history":100,"auto_save":True,"typing_speed":0.002,"first_run":True}
class Config:
    def __init__(s): s.data = {**C, **json.loads(F.read_text())} if F.exists() else C.copy()
    def save(s): F.write_text(json.dumps(s.data, indent=2))
    def get(s, k, d=None): return s.data.get(k, d)
    def set(s, k, v): s.data[k] = v; s.save()
