import os
import json

class File:
    def __init__(self):
        pass

    def load(self, path: str):
        content = None

        with open(path, 'r') as f:
            content = f.read()
        
        return (content)

    def save(self, path: str, data: dict):
        with open(path, 'w') as f:
            f.write(json.dumps(data, indent = 4))

    def search(self, path: str, extension: str):
        raw = os.listdir(path)
        clean = []

        for i in raw:
            if (i.endswith(f".{extension}") == True):
                clean.append(i)

        return (clean)