import sys; sys.path.insert(0,'..')
from src.core.engine import AIEngine
def t():
    e = AIEngine()
    r, m = e.ask('Say test')
    assert r is not None
    print(f'OK: {m}')
if __name__=='__main__': t()
