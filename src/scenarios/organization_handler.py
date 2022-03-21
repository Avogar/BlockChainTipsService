import json

from src.common.conf import *
from src.common.utils import *
from src.qr_manager.qr_manager import QRManager
from src.tips_service.tips_service import get_tips_service


class OrganizationHandler:
    def __init__(self):
        self.organization_name = input("Please enter your organization name: ")
        self.organization_address = input("Please enter your organization wallet address: ")
        self.organization_private_key = input("Please enter your organization private key: ")
        print()
        self.tips_service = get_tips_service()
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
            print()
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
                print()
                employees.append((employee_name, employee_address))
        elif get_employees_option == 2:
            while True:
                file_name = input("Enter json file name (leave empty to exit): ")
                if file_name == '':
                    break
                try:
                    with open(file_name) as f:
                        data = json.load(f)
                        if not isinstance(data, dict):
                            print("Json is not a dictionary\n")
                            continue
                        employees = data.items()
                    break
                except Exception as e:
                    print("Failed to open employees file {} with exception: {}".format(file_name, e))
        print()
        self.tips_service.add_organization((self.organization_name, self.organization_address), employees,
                                           self.organization_address, self.organization_private_key)

    def add_employee(self):
        employee_name = input("Enter your employee's name: ")
        employee_address = input("Enter your employee's address: ")
        print()
        self.tips_service.add_employee(self.organization_name, (employee_name, employee_address),
                                       self.organization_address, self.organization_private_key)

    def remove_employee(self):
        employee_name = input("Enter your employee's name: ")
        print()
        self.tips_service.remove_employee(self.organization_name, employee_name,
                                          self.organization_address, self.organization_private_key)

    def remove_organization(self):
        self.tips_service.remove_organization(self.organization_name, self.organization_address, self.organization_private_key)
