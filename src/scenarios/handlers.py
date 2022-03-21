from src.common.conf import *
from src.common.utils import *
from src.scenarios.employee_handler import EmployeeHandler
from src.scenarios.customer_handler import CustomerHandler
from src.scenarios.organization_handler import OrganizationHandler


def handle_user():
    user_type = None
    while True:
        while not is_number_in_bounds(user_type, 0, 3):
            user_type = input("Select one number. Who are you?\n"
                              "1) Customer\n"
                              "2) Organization\n"
                              "3) Employee\n"
                              "0) Exit\n")
            print()

        user_type = UserType(int(user_type))
        if user_type == UserType.NONE:
            break
        elif user_type == UserType.CUSTOMER:
            handle_customer()
        elif user_type == UserType.ORGANIZATION:
            handle_organization()
        elif user_type == UserType.EMPLOYEE:
            handle_employee()
        print()


def handle_customer():
    handler = CustomerHandler()
    while True:
        action_type = None
        while not is_number_in_bounds(action_type, 0, 10):
            action_type = input("Select one number. What do you want to do?\n"
                                "1) Get the list of all organizations\n"
                                "2) Get the list of employees in organization\n"
                                "3) Get the list of organization reviews\n"
                                "4) Get the list of employee reviews\n"
                                "5) Send an organization review\n"
                                "6) Send an employee review\n"
                                "7) Send a tip to an organization\n"
                                "8) Send a tip to an employee\n"
                                "9) Change my address\n"
                                "10) Change my private key\n"
                                "0) Exit\n")
            print()

        action_type = int(action_type)
        if action_type == 0:
            break
        elif action_type == 1:
            handler.get_all_organizations()
        elif action_type == 2:
            handler.get_all_employees()
        elif action_type == 3:
            handler.get_organization_reviews()
        elif action_type == 4:
            handler.get_employee_reviews()
        elif action_type == 5:
            handler.send_review_to_organization()
        elif action_type == 6:
            handler.send_review_to_employee()
        elif action_type == 7:
            handler.send_tips_to_organization()
        elif action_type == 8:
            handler.send_tips_to_employee()
        elif action_type == 9:
            handler.read_address()
        elif action_type == 10:
            handler.read_private_key()
        print()


def handle_organization():
    handler = OrganizationHandler()
    while True:
        action_type = None
        while not is_number_in_bounds(action_type, 0, 8):
            action_type = input("Select one number. What do you want to do?\n"
                                "1) Change organization name\n"
                                "2) Change organization address\n"
                                "3) Change organization private key\n"
                                "4) Generate new QR-code\n"
                                "5) Add organization\n"
                                "6) Add employee\n"
                                "7) Remove organization\n"
                                "8) Remove employee\n"
                                "0) Exit\n")
            print()
        action_type = int(action_type)
        if action_type == 0:
            break
        elif action_type == 1:
            handler.organization_name = input("Enter your organization name: ")
        elif action_type == 2:
            handler.organization_address = input("Enter your organization address: ")
        elif action_type == 3:
            handler.organization_private_key = input("Enter your organization private key: ")
        elif action_type == 4:
            file_name = input("Enter desired filename for QR-code (leave empty for default): ")
            handler.generate_new_qr_code(file_name)
        elif action_type == 5:
            handler.add_organization()
        elif action_type == 6:
            handler.add_employee()
        elif action_type == 7:
            handler.remove_organization()
        elif action_type == 8:
            handler.remove_employee()
        print()


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
            print()
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
        print()

