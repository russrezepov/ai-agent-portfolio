import json, os
MEMORY_FILE = "memory/store.json"

def load_memory(tenant=None):
    if not os.path.exists(MEMORY_FILE): return {}
    with open(MEMORY_FILE) as f:
        data = json.load(f)
    return data.get(tenant, {}) if tenant else data

def save_memory(entry, tenant="default"):
    data = {}
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE) as f:
            data = json.load(f)
    if tenant not in data:
        data[tenant] = []
    data[tenant].append(entry)
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)
