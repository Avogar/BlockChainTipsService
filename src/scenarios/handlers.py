from src.common.conf import *
from src.common.utils import *
from src.scenarios.employee_handler import EmployeeHandler
from src.scenarios.organization_handler import OrganizationHandler


def handle_user():
    user_type = None
    while not is_number_in_bounds(user_type, 1, 3):
        user_type = input("Select one number. Who are you?\n"
                          "1) Customer\n"
                          "2) Organization\n"
                          "3) Employee\n")
    user_type = UserType(int(user_type))
    if user_type == UserType.CUSTOMER:
        handle_customer()
    elif user_type == UserType.ORGANIZATION:
        handle_organization()
    elif user_type == UserType.EMPLOYEE:
        handle_employee()


def handle_customer():
    pass


def handle_organization():
    handler = OrganizationHandler()
    while True:
        action_type = None
        while not is_number_in_bounds(action_type, 0, 7):
            action_type = input("Select one number. What do you want to do?\n"
                                "1) Change organization name\n"
                                "2) Change organization address\n"
                                "3) Generate new QR-code\n"
                                "4) Add organization\n"
                                "5) Add employee\n"
                                "6) Remove organization\n"
                                "7) Remove employee\n"
                                "0) Exit\n")
        action_type = int(action_type)
        if action_type == 0:
            break
        elif action_type == 1:
            handler.organization_name = input("Enter your organization name: ")
        elif action_type == 2:
            handler.organization_address = input("Enter your organization address: ")
        elif action_type == 3:
            file_name = input("Enter desired filename for QR-code (leave empty for default): ")
            handler.generate_new_qr_code(file_name)
        elif action_type == 4:
            handler.add_organization()
        elif action_type == 5:
            handler.add_employee()
        elif action_type == 6:
            handler.remove_organization()
        elif action_type == 7:
            handler.remove_employee()


def handle_employee():
    handler = EmployeeHandler()
    while True:
        action_type = None
        while not is_number_in_bounds(action_type, 0, 3):
            action_type = input("Select one number. What do you want to do?\n"
                                "1) Change my organization name\n"
                                "2) Change my name\n"
                                "3) Generate new QR-code\n"
                                "0) Exit\n")
        action_type = int(action_type)
        if action_type == 0:
            break
        elif action_type == 1:
            handler.organization_name = input("Enter your organization name: ")
        elif action_type == 2:
            handler.employee_name = input("Enter your name: ")
        elif action_type == 3:
            file_name = input("Enter desired filename for QR-code (leave empty for default): ")
            handler.generate_new_qr_code(file_name)

