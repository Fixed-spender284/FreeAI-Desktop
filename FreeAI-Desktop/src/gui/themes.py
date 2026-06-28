T={'dark':{'bg':'#1a1a2e','fg':'#e0e0e0','accent':'#00d4ff'},'light':{'bg':'#fff','fg':'#333','accent':'#06c'},'cyberpunk':{'bg':'#0d0221','fg':'#f0f','accent':'#0ff'}}
def get_theme(n='dark'): return T.get(n,T['dark'])
