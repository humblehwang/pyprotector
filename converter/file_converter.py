import abc
from typing import List, Union
import pandas as pd
from converter.json_converter import JsonConverter

class FileConverter:
    def __init__(self) -> None:
        self.json_converter = JsonConverter()

    SUPPORT_FILE_EXTENSION = [".csv", ".xlsx", ".h5", ".txt", ".json"]

    def read_file(self, filepath: str):
        if filepath.endswith(".csv"):
            pass

        elif filepath.endswith(".xlsx"):
            pass

        elif filepath.endswith(".h5"):
            pass

        elif filepath.endswith(".txt"):
            pass

        elif filepath.endswith(".json"):
            json_data = self.json_converter.read_json(filepath)
            return json_data
            
        else:
            raise ValueError(f"Unsupported file extension is given. filepath={filepath}")

    def write_file(self, filepath: str, data) -> None:
        if filepath.endswith(".csv"):
            pass

        elif filepath.endswith(".xlsx"):
            pass

        elif filepath.endswith(".h5"):
            pass

        elif filepath.endswith(".txt"):
            pass

        elif filepath.endswith(".json"):
            self.json_converter.write_json(filepath, data)
            
            
        else:
            raise ValueError(f"Unsupported file extension is given. filepath={filepath}")

file_converter_ = FileConverter()

    



