class TypewriterLabel:
    def __init__(s, sp=0.002): s.sp = sp
    def print(s, t):
        import time
        for c in t: print(c, end='', flush=True); time.sleep(s.sp)
