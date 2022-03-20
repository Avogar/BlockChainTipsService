import json
import time
from hashlib import sha1
from typing import Optional, Dict

from cryptography.fernet import Fernet
import qrcode
import cv2
from pyzbar.pyzbar import decode

from src.common.conf import *


class QRManager:
    def __init__(self):
        self.encryptor = Fernet(ENCRYPTION_KEY.encode())

    def organization_info_to_qr(self, organization_name: str, file_name: str) -> None:
        """ Transforms organization name into a QR-code

        Keyword arguments:
            file_name -- path to resulting file
        """
        qr_data = dict()
        qr_data[TYPE_QR_FIELD] = ORGANIZATION_TYPE
        qr_data[ORG_NAME_QR_FIELD] = self._hash_string(organization_name)
        qr_data[ID_QR_FIELD] = self._hash_string(str(time.time_ns()))
        self._info_to_qr(qr_data, file_name)

    def employee_info_to_qr(self, organization_name: str, employee_name: str, file_name: str) -> None:
        """Transforms employee's info into a QR-code

        Keyword arguments:
            file_name -- path to resulting file
        """
        qr_data = dict()
        qr_data[TYPE_QR_FIELD] = EMPLOYEE_TYPE
        qr_data[ORG_NAME_QR_FIELD] = self._hash_string(organization_name)
        qr_data[EMPLOYEE_NAME_QR_FIELD] = self._hash_string(employee_name)
        qr_data[ID_QR_FIELD] = self._hash_string(str(time.time_ns()))

        self._info_to_qr(qr_data, file_name)

    def qr_to_organization_info(self, file_name: str) -> Optional[Dict[str, str]]:
        """Transforms QR-code into organization info"""
        organization_info = self._qr_to_info(file_name)
        if organization_info is None:
            return None
        qr_code_type = self._get_qr_type_from_info(organization_info)
        if qr_code_type != ORGANIZATION_TYPE:
            print("Incorrect qr code type {} != {}, in file {}".format(qr_code_type, ORGANIZATION_TYPE, file_name))
            return None
        return organization_info

    def qr_to_employee_info(self, file_name: str) -> Optional[Dict[str, str]]:
        """Transforms QR-code into employee info"""
        employee_info = self._qr_to_info(file_name)
        if employee_info is None:
            return None
        qr_code_type = self._get_qr_type_from_info(employee_info)
        if qr_code_type != EMPLOYEE_TYPE:
            print("Incorrect qr code type {} != {}, in file {}".format(qr_code_type, EMPLOYEE_TYPE, file_name))
            return None
        return employee_info

    def _info_to_qr(self, info: Dict[str, str], file_name: str) -> None:
        raw_data = json.dumps(info)
        encrypted_data = self.encryptor.encrypt(raw_data.encode())

        img = qrcode.make(encrypted_data)
        img.save(file_name)

    def _qr_to_info(self, file_name: str) -> Optional[Dict[str, str]]:
        try:
            qr = cv2.imread(file_name)
            data = decode(qr)
            if len(data) == 0:
                print("No QR-code detected in file {}.".format(file_name))
                return None
            data = data[0].data
            decrypted_data = self.encryptor.decrypt(data)
            info = json.loads(decrypted_data)
            return info
        except Exception as e:
            print("Exception occured while reading qr from file {}: {}.".format(file_name, e))
            return None

    @staticmethod
    def _get_qr_type_from_info(info: Dict[str, str]) -> Optional[str]:
        if TYPE_QR_FIELD not in info:
            return None
        return info[TYPE_QR_FIELD]

    @staticmethod
    def _hash_string(string: str):
        return sha1(string.encode()).hexdigest()
