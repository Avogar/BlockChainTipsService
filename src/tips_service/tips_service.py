import json

from typing import Tuple, Dict, List
from web3 import Web3


class TipsService:
    def __init__(self, http_provider_url: str, contract_json_file: str):
        with open(contract_json_file) as file:
            self.web3 = Web3(Web3.HTTPProvider(http_provider_url))

            contract_info = json.load(file)
            self.contract = self.web3.eth.contract(address=contract_info["address"], abi=contract_info["abi"])

    def add_organization(self, organization: Tuple[str, str], employees: List[Tuple[str, str]], address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.addOrganization(organization, employees).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)
    
    def add_employee(self, organization: str, employee: Tuple[str, str], address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.addEmployeeToOrganization(organization, employee).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_tips_to_organization(self, amount: float, organization_name: str, action_id: str, address: str, private_key: str, review=""):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendTipsToOrganization(organization_name, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_tips_to_employee(self, amount: float, organization_name: str, employee_name: str, action_id: str, address: str, private_key: str, review=""):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendTipsToEmployee(organization_name, employee_name, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_review_to_organization(self, organization_name: str, review: str, action_id: str, address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendOrganizationReview(organization_name, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_review_to_employee(self, organization_name: str, employee_name: str, review: str, action_id: str, address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendEmployeeReview(organization_name, employee_name, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def remove_organization(self, organization_name: str, address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.removeOrganization(organization_name).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def remove_employee(self, organization_name: str, employee_name: str, address: str, private_key: str):
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.removeEmployeeFromOrganization(organization_name, employee_name).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def get_organization_reviews(self, organization_name: str) -> List[str]:
        return self.contract.functions.getOrganizationReviews(organization_name).call()

    def get_employee_reviews(self, organization_name: str, employee_name: str):
        return self.contract.functions.getEmployeeReviews(organization_name, employee_name).call()

    def get_all_organizations(self) -> List[str]:
        return self.contract.functions.getAllOrganizations().call()

    def get_all_employees(self, organization_name: str):
        return self.contract.functions.getAllEmployeeInOrganization(organization_name).call()

    def _get_tx_properties(self, address: str, value=0):
        nonce = self.web3.eth.getTransactionCount(address)
        return {'gas': 600000, 'gasPrice': self.web3.toWei('10', 'gwei'), 'from': address, 'nonce': nonce,
                'value': self.web3.toWei(float(value), "ether")}

    def _sign_and_send_tx(self, tx, private_key: str):
        signed_txn = self.web3.eth.account.signTransaction(tx, private_key=private_key)
        self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
