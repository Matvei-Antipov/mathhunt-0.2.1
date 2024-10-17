import json
import os

def load_bradys_table(filename='__data\\bradis_table.json'):
    filepath = os.path.join(os.path.dirname(__file__), '../', filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data