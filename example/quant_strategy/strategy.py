from typing import Dict
import json

DATA_PATH = "./data"
LOG_PATH = ".log"

class Strategy:
    def __init__(
        self,
        exchange: str,
        symbol: str,
        contract_type: str,
    ) -> None:
        self.exchange = exchange
        self.symbol = symbol
        self.contract_type = contract_type
        self.key = f"{exchange}/{symbol}/{contract_type}"
    
    def __str__(self) -> str:
        return f"{self.key}/{self.account_id}/{self.account_pwd}"

    def run(self) -> None:
        count = 1
        print(f"start running strategy {self.key}")
        while True:
            print(f"Run {count}")
    
    def load_account_info(self) -> None:
        account_info_path = f"{DATA_PATH}/account.json"
        with open(account_info_path) as file:
            account_info = json.load(file)
            self.account_id = account_info['exchange_info'][self.exchange]['account_id']
            self.account_pwd = account_info['exchange_info'][self.exchange]['pwd']


