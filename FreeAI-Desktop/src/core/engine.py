import requests, urllib3, json
urllib3.disable_warnings()

class AIEngine:
    def __init__(self):
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
        })

    def ask(self, message, history=None):
        if history is None:
            history = []
        
        prompt = "You are a helpful AI assistant. Answer in the user's language.\n\n"
        for h in (history or [])[-8:]:
            role = "User" if h["role"] == "user" else "Assistant"
            prompt += f"{role}: {h['content']}\n"
        prompt += f"User: {message}\nAssistant:"

        # HuggingFace Inference API — бесплатно, без ключа
        models = [
            ("https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3", "Mistral 7B"),
            ("https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct", "Phi-3 Mini"),
            ("https://api-inference.huggingface.co/models/Qwen/Qwen2.5-7B-Instruct", "Qwen 2.5"),
            ("https://api-inference.huggingface.co/models/google/gemma-2-2b-it", "Gemma 2"),
        ]

        for url, name in models:
            try:
                r = self.session.post(
                    url,
                    headers={"Content-Type": "application/json"},
                    json={
                        "inputs": prompt,
                        "parameters": {
                            "max_new_tokens": 500,
                            "temperature": 0.7,
                            "return_full_text": False,
                        }
                    },
                    timeout=60
                )
                if r.status_code == 200:
                    data = r.json()
                    if isinstance(data, list) and len(data) > 0:
                        text = data[0].get("generated_text", "")
                        return text.strip(), name
                elif r.status_code == 503:
                    # Модель загружается
                    continue
            except:
                continue

        return None, None