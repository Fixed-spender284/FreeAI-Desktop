from datetime import datetime
from pathlib import Path
L = Path.home() / '.freeai' / 'logs'
L.mkdir(parents=True, exist_ok=True)
def log(m, l='INFO'):
    t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = L / f"freeai_{datetime.now().strftime('%Y%m%d')}.log"
    with open(f, 'a', encoding='utf-8') as h: h.write(f'[{t}] [{l}] {m}\n')
