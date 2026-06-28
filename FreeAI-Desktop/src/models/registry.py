ALL_MODELS = [
    {"id":"google/gemma-3-27b-it:free","name":"Gemma 3 27B","provider":"Google","speed":5,"quality":5},
    {"id":"nvidia/llama-3.1-nemotron-70b-instruct:free","name":"Llama 3.1 70B","provider":"NVIDIA","speed":4,"quality":5},
    {"id":"deepseek/deepseek-r1:free","name":"DeepSeek R1","provider":"DeepSeek","speed":5,"quality":5},
    {"id":"deepseek/deepseek-chat:free","name":"DeepSeek Chat","provider":"DeepSeek","speed":5,"quality":4},
    {"id":"mistralai/mistral-7b-instruct-v0.3:free","name":"Mistral 7B","provider":"Mistral","speed":5,"quality":3},
    {"id":"qwen/qwen-2.5-7b-instruct:free","name":"Qwen 2.5 7B","provider":"Alibaba","speed":5,"quality":4},
    {"id":"meta-llama/llama-3.2-3b-instruct:free","name":"Llama 3.2 3B","provider":"Meta","speed":5,"quality":3},
]
def get_free_models(): return [m for m in ALL_MODELS if ":free" in m["id"]]
