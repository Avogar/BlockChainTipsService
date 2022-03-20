import json

from src.common.conf import *
from src.common.smart_service_metadata import CONTRACT_METADATA
from src.common.utils import *
from src.qr_manager.qr_manager import QRManager
from src.tips_service.tips_service import TipsService


class OrganizationHandler:
    def __init__(self):
        bc_http_provider = input("Enter your blockchain http provider: ")
        self.organization_name = input("Please enter your organization name: ")
        self.organization_address = input("Please enter your organization wallet address: ")
        self.organization_private_key = input("Please enter your organization private key: ")
        self.tips_service = TipsService(bc_http_provider, CONTRACT_METADATA)
        self.qr_gen = QRManager()

    def generate_new_qr_code(self, file_name: str):
        if file_name == '':
            file_name = DEFAULT_QR_FILENAME
        self.qr_gen.organization_info_to_qr(self.organization_name, file_name)

    def add_organization(self):
        get_employees_option = None
        while not is_number_in_bounds(get_employees_option, 0, 2):
            get_employees_option = input("Select one number. What do you want to do?\n"
                                         "1) Enter employees manually\n"
                                         "2) Import employees from json. Json must be a simple map, where keys are "
                                         "employees' names and values are their wallet addresses \n"
                                         "0) Exit\n")
        get_employees_option = int(get_employees_option)
        employees = list()

        if get_employees_option == 0:
            return
        elif get_employees_option == 1:
            while True:
                employee_name = input("Enter employee's name (leave empty to exit): ")
                if employee_name == '':
                    break
                employee_address = input("Enter employee's wallet address: ")
                employees.append((employee_name, employee_address))
        elif get_employees_option == 2:
            while True:
                file_name = input("Enter json file name: ")
                try:
                    with open(file_name) as f:
                        data = json.load(f)
                        if not isinstance(employees, dict):
                            print("Json is not a dictionary")
                            continue
                        employees = data.items()
                    break
                except Exception as e:
                    print("Failed to open employees file {} with exception: {}".format(file_name, e))
        self.tips_service.add_organization((self.organization_name, self.organization_address), employees,
                                           self.organization_address, self.organization_private_key)

    def add_employee(self):
        employee_name = input("Enter your employee's name: ")
        employee_address = input("Enter your employee's address: ")
        self.tips_service.add_employee(self.organization_name, (employee_name, employee_address),
                                       self.organization_address, self.organization_private_key)

    def remove_employee(self):
        employee_name = input("Enter your employee's name: ")
        self.tips_service.remove_employee(self.organization_name, employee_name,
                                          self.organization_address, self.organization_private_key)

    def remove_organization(self):
        self.tips_service.remove_organization(self.organization_name, self.organization_address, self.organization_private_key)
