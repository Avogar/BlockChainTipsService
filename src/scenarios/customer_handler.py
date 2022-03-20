from src.tips_service.tips_service import get_tips_service
from src.qr_manager.qr_manager import QRManager
from src.common.conf import *

class CustomerHandler:
    def __init__(self):
        self.service = get_tips_service()
        self.qr_manager = QRManager()
        self.address = None
        self.private_key = None

    def get_all_organizations(self):
        print("List of organizations: {}".format(self.service.get_all_organizations()))

    def get_all_employees(self):
        organization_name = self._read_organization_name()
        employees = self.service.get_all_employees(organization_name)
        print("List of employees in the organization {}: {}".format(organization_name, employees))

    def get_organization_reviews(self):
        organization_name = self._read_organization_name()
        reviews = self.service.get_organization_reviews(organization_name)
        print("Reviews of the organization {}: {}".format(organization_name, reviews))

    def get_employee_reviews(self):
        organization_name = self._read_organization_name()
        employee_name = self._read_employee_name()
        reviews = self.service.get_employee_reviews(organization_name, employee_name)
        print("Reviews of the employee {} of the organization {}: {}".format(employee_name, organization_name, reviews))

    def send_review_to_organization(self):
        path_to_qr_code = self._read_organization_qr_code()
        if len(path_to_qr_code) == 0:
            return
        organization_info = self.qr_manager.qr_to_organization_info(path_to_qr_code)
        if organization_info is None:
            return
        organization_name = organization_info[ORG_NAME_QR_FIELD]
        action_id = organization_info[ID_QR_FIELD]
        review = self._read_organization_review()
        address = self.read_address()
        private_key = self.read_private_key()
        self.service.send_review_to_organization(organization_name, review, action_id, address, private_key)

    def send_review_to_employee(self):
        path_to_qr_code = self._read_employee_qr_code()
        if len(path_to_qr_code) == 0:
            return
        employee_info = self.qr_manager.qr_to_employee_info(path_to_qr_code)
        if employee_info is None:
            return
        organization_name = employee_info[ORG_NAME_QR_FIELD]
        employee_name = employee_info[EMPLOYEE_NAME_QR_FIELD]
        action_id = employee_info[ID_QR_FIELD]
        review = self._read_employee_review()
        address = self.read_address()
        private_key = self.read_private_key()
        self.service.send_review_to_employee(organization_name, employee_name, review, action_id, address, private_key)

    def send_tips_to_organization(self):
        path_to_qr_code = self._read_organization_qr_code()
        organization_info = self.qr_manager.qr_to_organization_info(path_to_qr_code)
        if organization_info is None:
            return
        organization_name = organization_info[ORG_NAME_QR_FIELD]
        action_id = organization_info[ID_QR_FIELD]
        tips = float(self._read_tips_amount())
        review = self._read_organization_review()
        address = self.read_address()
        private_key = self.read_private_key()
        self.service.send_tips_to_organization(tips, organization_name, review, action_id, address, private_key)

    def send_tips_to_employee(self):
        path_to_qr_code = self._read_employee_qr_code()
        employee_info = self.qr_manager.qr_to_employee_info(path_to_qr_code)
        if employee_info is None:
            return
        organization_name = employee_info[ORG_NAME_QR_FIELD]
        employee_name = employee_info[EMPLOYEE_NAME_QR_FIELD]
        action_id = employee_info[ID_QR_FIELD]
        tips = float(self._read_tips_amount())
        review = self._read_employee_review()
        address = self.read_address()
        private_key = self.read_private_key()
        self.service.send_tips_to_employee(tips, organization_name, employee_name, review, action_id, address, private_key)

    def _read_organization_name(self):
        return input("Please enter organization name: ")

    def _read_employee_name(self):
        return input("Please enter employee name: ")

    def read_address(self):
        if self.address is None:
            self.address = input("Please enter your address: ")
        return self.address

    def read_private_key(self):
        if self.private_key is None:
            self.private_key = input("Please enter your private_key: ")
        return self.private_key

    def _read_organization_qr_code(self):
        return input("Please enter path to QR code from organization (empty to exit): ")

    def _read_employee_qr_code(self):
        return input("Please enter path to QR code from employee (empty to exit): ")

    def _read_organization_review(self):
        return input("Please enter organization review: ")

    def _read_employee_review(self):
        return input("Please enter employee review: ")

    def _read_tips_amount(self):
        return input("Please enter the amount of tip: ")

