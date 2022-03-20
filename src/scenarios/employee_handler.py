from src.common.conf import *
from src.common.utils import *
from src.qr_manager.qr_manager import QRManager


class EmployeeHandler:
    def __init__(self):
        self.organization_name = input("Please enter your organization name: ")
        self.employee_name = input("Please enter your name: ")
        self.qr_gen = QRManager()

    def generate_new_qr_code(self, file_name: str):
        if file_name == '':
            file_name = DEFAULT_QR_FILENAME
        self.qr_gen.employee_info_to_qr(self.organization_name, self.employee_name, file_name)