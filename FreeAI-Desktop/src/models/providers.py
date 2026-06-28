P={'openrouter':{'name':'OpenRouter','url':'https://openrouter.ai/api/v1/chat/completions','free':True,'requires_key':False},'deepseek':{'name':'DeepSeek','url':'https://api.deepseek.com/v1/chat/completions','free':True,'requires_key':True}}
def get_provider(n='openrouter'): return P.get(n,P['openrouter'])
