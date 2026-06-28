import requests, urllib3
urllib3.disable_warnings()
class NetworkClient:
    def __init__(s): s.s = requests.Session(); s.s.verify = False
    def post(s, u, h=None, j=None, t=30, r=3):
        for a in range(r):
            try: return s.s.post(u, headers=h, json=j, timeout=t)
            except Exception as e:
                if a == r-1: raise e
