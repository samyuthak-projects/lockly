import json

FILE = "users.json"

def load_users():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}
    
def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)