import json

from typing import Tuple, Dict
from web3 import Web3


class TipsService:
    def __init__(self, http_provider_url: str, contract_json_file: str):
        with open(contract_json_file) as file:
            self.web3 = Web3(Web3.HTTPProvider(http_provider_url))

            contract_info = json.load(file)
            self.contract = self.web3.eth.contract(address=contract_info["address"], abi=contract_info["abi"])

    def add_organization(self, organization: Tuple[str, str], employees: Dict[str, str]):
        pass
    
    def add_employee(self, organization: str, employee: Tuple[str, str]):
        pass

    def send_tips_to_organization(self, amount: float, name: str, review=None):
        pass

    def send_tips_to_employee(self, amount: float, organization_name: str, employee_name: str, review=None):
        pass

    def review_organization(self, name: str, review=None):
        pass

    def review_employee(self, organization_name: str, employee_name: str, review=None):
        pass

    def remove_organization(self, name: str):
        pass

    def remove_employee(self, organization_name: str, employee_name: str):
        pass

    def get_organization_reviews(self, name: str):
        pass

    def get_employee_reviews(self, organization_name: str, employee_name: str):
        pass

    def get_all_organizations(self):
        pass

    def get_all_employees(self, organization_name: str):
        pass
