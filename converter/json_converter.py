import json
from typing import Dict

class JsonConverter:
    def read_json(self, filepath: str):
        json_data = None
        with open(filepath) as file:
            json_data = json.load(file)
        
        if json_data is None:
            raise Exception(f"Failed to open file {filepath}")
        
        return json_data

    def write_json(self, filepath: str, json_data: Dict):
        py_filepath = f'py_{filepath.replace(".json", ".py")}'
        with open(py_filepath, 'w') as f:
            f.write(f"json_data = {json_data}")
