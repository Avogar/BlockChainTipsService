import json

from typing import Tuple, List
from web3 import Web3
from src.common.encryptor import Encryptor
from src.common.conf import *
from src.common.smart_service_metadata import CONTRACT_METADATA
from hashlib import sha256


class TipsService:
    def __init__(self, http_provider_url: str, contract_info):
        self.web3 = Web3(Web3.HTTPProvider(http_provider_url))

        self.contract = self.web3.eth.contract(address=contract_info["address"], abi=contract_info["abi"])
        self.encryptor = Encryptor()

    def add_organization(self, organization: Tuple[str, str], employees: List[Tuple[str, str]], address: str, private_key: str):
        organization_info = (self._hash(organization[0]), self.encryptor.encode(organization[0]), organization[1])
        employee_infos = list(map(lambda x: (self._hash(x[0]), self.encryptor.encode(x[0]), x[1]), employees))
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.addOrganization(organization_info, employee_infos).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)
    
    def add_employee(self, organization_name: str, employee: Tuple[str, str], address: str, private_key: str):
        organization_id = self._hash(organization_name)
        employee_info = (self._hash(employee[0]), self.encryptor.encode(employee[0]), employee[1])
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.addEmployeeToOrganization(organization_id, employee_info).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_tips_to_organization(self, amount: float, organization_name: str, review: str, action_id: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        review = self.encryptor.encode(review)
        tx_properties = self._get_tx_properties(address, value=amount)
        tx = self.contract.functions.sendTipsToOrganization(organization_id, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_tips_to_employee(self, amount: float, organization_name: str, employee_name: str, review: str, action_id: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        employee_id = self._hash(employee_name)
        review = self.encryptor.encode(review)
        tx_properties = self._get_tx_properties(address, value=amount)
        tx = self.contract.functions.sendTipsToEmployee(organization_id, employee_id, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_review_to_organization(self, organization_name: str, review: str, action_id: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        review = self.encryptor.encode(review)
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendOrganizationReview(organization_id, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def send_review_to_employee(self, organization_name: str, employee_name: str, review: str, action_id: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        employee_id = self._hash(employee_name)
        review = self.encryptor.encode(review)
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.sendEmployeeReview(organization_id, employee_id, review, action_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def remove_organization(self, organization_name: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.removeOrganization(organization_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def remove_employee(self, organization_name: str, employee_name: str, address: str, private_key: str):
        organization_id = self._hash(organization_name)
        employee_id = self._hash(employee_name)
        tx_properties = self._get_tx_properties(address)
        tx = self.contract.functions.removeEmployeeFromOrganization(organization_id, employee_id).buildTransaction(tx_properties)
        self._sign_and_send_tx(tx, private_key)

    def get_organization_reviews(self, organization_name: str) -> List[str]:
        organization_id = self._hash(organization_name)
        reviews = self.contract.functions.getOrganizationReviews(organization_id).call()
        return list(map(lambda x: self.encryptor.decode(x), reviews))

    def get_employee_reviews(self, organization_name: str, employee_name: str):
        organization_id = self._hash(organization_name)
        employee_id = self._hash(employee_name)
        reviews = self.contract.functions.getEmployeeReviews(organization_id, employee_id).call()
        return list(map(lambda x: self.encryptor.decode(x), reviews))

    def get_all_organizations(self) -> List[str]:
        organizations = self.contract.functions.getAllOrganizations().call()
        return list(map(lambda x: self.encryptor.decode(x), organizations))

    def get_all_employees(self, organization_name: str):
        organization_id = self._hash(organization_name)
        employees = self.contract.functions.getAllEmployeeInOrganization(organization_id).call()
        return list(map(lambda x: self.encryptor.decode(x), employees))

    def _get_tx_properties(self, address: str, value=0.):
        nonce = self.web3.eth.getTransactionCount(address)
        return {'gas': 5000000, 'gasPrice': self.web3.toWei('10', 'gwei'), 'from': address, 'nonce': nonce,
                'value': self.web3.toWei(value, "ether")}

    def _sign_and_send_tx(self, tx, private_key: str):
        signed_txn = self.web3.eth.account.signTransaction(tx, private_key=private_key)
        try:
            tx_hex = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction).hex()
            print("Transaction id: ", tx_hex)
        except Exception as e:
            print("Unable to send transaction: {}".format(e))

    def _hash(self, data: str):
        return sha256(data.encode()).hexdigest()


def get_tips_service():
    return TipsService(PROVIDER_URL, CONTRACT_METADATA)